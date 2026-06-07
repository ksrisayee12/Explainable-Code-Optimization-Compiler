from graphviz import Digraph


class DAGNode:
    def __init__(self, op=None, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right
        self.labels = []


def generate_dag(ir):
    nodes = []
    var_map = {}

    def get_leaf(var):
        if var in var_map:
            return var_map[var]

        node = DAGNode()
        node.labels.append(var)
        nodes.append(node)
        var_map[var] = node
        return node

    def find_node(op, left, right):
        for n in nodes:
            if n.op == op and n.left == left and n.right == right:
                return n
        return None

    for instr in ir:
        lhs, rhs = instr["code"].split("=")
        lhs = lhs.strip()
        rhs = rhs.strip()

        if "+" in rhs:
            op = "+"
            op1, op2 = [x.strip() for x in rhs.split("+")]
        elif "*" in rhs:
            op = "*"
            op1, op2 = [x.strip() for x in rhs.split("*")]
        else:
            # assignment
            if rhs in var_map:
                var_map[lhs] = var_map[rhs]
                var_map[rhs].labels.append(lhs)
            continue

        left_node = get_leaf(op1)
        right_node = get_leaf(op2)

        existing = find_node(op, left_node, right_node)

        if existing:
            existing.labels.append(lhs)
            var_map[lhs] = existing
        else:
            new_node = DAGNode(op, left_node, right_node)
            new_node.labels.append(lhs)
            nodes.append(new_node)
            var_map[lhs] = new_node

    # ---------------- GRAPHVIZ ----------------

    dot = Digraph(comment="Proper DAG")
    dot.attr(rankdir="TB")
    dot.attr(splines="curved")

    node_ids = {}

    for i, node in enumerate(nodes):
        node_id = f"N{i}"
        node_ids[node] = node_id

        if node.op:
            label = f"{node.op}\n[{', '.join(node.labels)}]"
            dot.node(node_id, label, shape="circle", style="filled", fillcolor="lightblue")
        else:
            label = ", ".join(node.labels)
            dot.node(node_id, label, shape="box", style="filled", fillcolor="lightgray")

    for node in nodes:
        if node.op:
            dot.edge(node_ids[node.left], node_ids[node], color="black")
            dot.edge(node_ids[node.right], node_ids[node], color="black")

    return dot
