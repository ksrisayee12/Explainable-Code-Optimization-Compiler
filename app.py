import streamlit as st

from frontend_parser import generate_tac_from_code
from analysis import compute_liveness, compute_live_range
from pipeline import CompilerPipeline
from optimizations.live_range import LiveRangeCompression
from tree_visualizer import generate_scheduled_tree
from dag_visualizer import generate_dag
from cfg_visualizer import generate_cfg
from rag_explainer import explain_optimization

st.set_page_config(page_title="Explainable Compiler", layout="wide")

st.title("Explainable Code Optimization Compiler")
st.caption("Mini Java / C → Three Address Code → Optimization → DAG")

# --------------------------------------------------
# SOURCE CODE INPUT
# --------------------------------------------------
st.subheader("Input Source Code (Mini Java / C)")

source_code = st.text_area(
    "Enter simple arithmetic statements:",
    value="a = b + c;\nd = a * e;",
    height=120
)

optimize = st.checkbox("Enable Optimization", value=True)
explain = st.checkbox("Explain Optimization (RAG)", value=True)
show_cfg = st.checkbox("Show Control Flow Graph (CFG)", value=True)

st.divider()

# --------------------------------------------------
# RUN COMPILER
# --------------------------------------------------
if st.button("Compile"):

    # ------------------ FRONTEND ------------------
    ir = generate_tac_from_code(source_code)

    st.subheader("Three Address Code (IR)")
    for instr in ir:
        st.code(instr["code"])

    # ------------------ ANALYSIS ------------------
    live_after = compute_liveness(ir)

    # ------------------ PIPELINE ------------------
    pipeline = CompilerPipeline()
    if optimize:
        pipeline.add_optimization(LiveRangeCompression())

    optimized_ir, logs = pipeline.run_optimizations(ir, live_after)

    # ------------------ METRICS ------------------
    before_range = compute_live_range(ir, "t1")
    after_range = compute_live_range(optimized_ir, "t1")

    # --------------------------------------------------
    # BEFORE OPTIMIZATION GRAPH
    # --------------------------------------------------
    st.subheader("Before Optimization")

    st.graphviz_chart(generate_scheduled_tree(ir))

    # --------------------------------------------------
    # AFTER OPTIMIZATION GRAPHS
    # --------------------------------------------------
    st.subheader("After Optimization Graphs")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Scheduled Dependency Graph")
        st.graphviz_chart(generate_scheduled_tree(optimized_ir))

    with col2:
        st.markdown("### DAG Representation")
        st.graphviz_chart(generate_dag(optimized_ir))

    # --------------------------------------------------
    # CFG
    # --------------------------------------------------
    if show_cfg:
        st.subheader("Control Flow Graph (CFG)")
        st.graphviz_chart(generate_cfg(optimized_ir))

    # --------------------------------------------------
    # OPTIMIZED CODE
    # --------------------------------------------------
    if optimize:
        st.subheader("Optimized Three Address Code")
        for instr in optimized_ir:
            st.code(instr["code"])

        st.subheader("Live-Range Metrics")
        st.write({
            "t1 before optimization": before_range,
            "t1 after optimization": after_range
        })

    # --------------------------------------------------
    # EXPLANATION (RAG SAFE)
    # --------------------------------------------------
    if explain:
        st.subheader("Explainable Optimization (RAG)")

        # TEMP DEBUG (remove later)
        st.write("Logs:", logs)

        for log in logs:
            explanation = explain_optimization(
                log,
                0,
                0
            )
            st.info(explanation)



    st.success("Compilation Completed Successfully")
