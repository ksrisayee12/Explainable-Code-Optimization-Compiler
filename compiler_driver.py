import argparse

from ir_generator import generate_ir
from analysis import compute_liveness, compute_live_range
from pipeline import CompilerPipeline
from optimizations.live_range import LiveRangeCompression
from tree_visualizer import print_expression_tree
from rag_explainer import explain_optimization
from output_writer import write_json

# --------------------------------------------------
# BANNER
# --------------------------------------------------
print("=" * 60)
print(" EXPLAINABLE COMPILER – STAGE 3.5 ")
print("=" * 60)

# --------------------------------------------------
# CLI ARGUMENTS
# --------------------------------------------------
parser = argparse.ArgumentParser(
    description="Explainable Compiler with Optimization Pipeline"
)

parser.add_argument("--optimize", action="store_true", help="Enable optimization")
parser.add_argument("--tree", action="store_true", help="Show expression tree")
parser.add_argument("--explain", action="store_true", help="Explain optimization using RAG")
parser.add_argument("--json", action="store_true", help="Write JSON output")

args = parser.parse_args()

# --------------------------------------------------
# FRONTEND (IR GENERATION)
# --------------------------------------------------
ir = generate_ir()

print("\n[INTERMEDIATE CODE]")
for instr in ir:
    print(instr["code"])

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------
live_after = compute_liveness(ir)

# --------------------------------------------------
# PIPELINE SETUP
# --------------------------------------------------
pipeline = CompilerPipeline()

if args.optimize:
    pipeline.add_optimization(LiveRangeCompression())

# --------------------------------------------------
# OPTIMIZATION (SAFE DEFAULT)
# --------------------------------------------------
optimized_ir = ir
logs = []

if args.optimize:
    optimized_ir, logs = pipeline.run_optimizations(ir, live_after)

# --------------------------------------------------
# METRICS
# --------------------------------------------------
before_range = compute_live_range(ir, "t1")
after_range = compute_live_range(optimized_ir, "t1")

if args.optimize:
    print("\n[OPTIMIZED CODE]")
    for instr in optimized_ir:
        print(instr["code"])

    print("\n[LIVE-RANGE METRICS]")
    print(f"t1 before optimization : {before_range}")
    print(f"t1 after optimization  : {after_range}")

# --------------------------------------------------
# EXPLANATION (RAG – FAIL SAFE)
# --------------------------------------------------
explanations = []

if args.explain and args.optimize:
    print("\n[EXPLAINABLE OPTIMIZATION]")
    for log in logs:
        try:
            explanation = explain_optimization(log, before_range, after_range)
        except Exception as e:
            explanation = f"[RAG unavailable] Explanation skipped: {e}"

        explanations.append(explanation)
        print(explanation)
        print("-" * 50)

# --------------------------------------------------
# TREE VISUALIZATION
# --------------------------------------------------
if args.tree:
    print("\n[EXPRESSION TREE]")
    print_expression_tree(ir)

# --------------------------------------------------
# JSON OUTPUT
# --------------------------------------------------
if args.json:
    write_json({
        "ir": ir,
        "optimized_ir": optimized_ir,
        "metrics": {
            "t1_before": before_range,
            "t1_after": after_range
        },
        "logs": logs,
        "explanations": explanations
    })
    print("\nJSON output written to compiler_output.json")

# --------------------------------------------------
# FINAL SUMMARY
# --------------------------------------------------
print("\n==============================")
print(" Compilation Completed ")
print("==============================")
print(f"Optimization enabled : {args.optimize}")
print(f"Tree visualization   : {args.tree}")
print(f"Explanation (RAG)    : {args.explain}")
print(f"JSON output          : {args.json}")
