from ir_generator import generate_ir
from analysis import compute_liveness
from analysis import compute_live_range
from optimizer import live_range_compression
from logger import print_logs
from rag_explainer import explain_optimization
from tree_visualizer import print_expression_tree
from tree_visualizer import print_before_after_trees

# Step 1: Generate IR
ir = generate_ir()
print("Original IR:")
for i in ir:
    print(i["code"])

# Step 2: Liveness Analysis
live_after = compute_liveness(ir)

print("\nLive Variables After Each Instruction:")
for k, v in live_after.items():
    print(f"Instr {k}: {v}")

# Step 3: Optimization
optimized_ir, logs = live_range_compression(ir, live_after)

print("\nOptimized IR:")
for i in optimized_ir:
    print(i["code"])

# Step 4: Logs

# ---- LIVE-RANGE METRICS ----
before_range = compute_live_range(ir, "t1")
after_range = compute_live_range(optimized_ir, "t1")

print("\nLive-Range Metrics:")
print(f"t1 before optimization: {before_range}")
print(f"t1 after optimization:  {after_range}")


print("\nRAG-Based Optimization Explanation:")

for log in logs:
    explanation = explain_optimization(log, before_range, after_range)
    print(explanation)
    print("-" * 50)
# dot_tree = generate_expression_tree(ir)

# with open("expression_tree.dot", "w") as f:
#     f.write(dot_tree)

# print("\nExpression tree generated: expression_tree.dot")
print_expression_tree(ir)
print_before_after_trees(ir, optimized_ir)
