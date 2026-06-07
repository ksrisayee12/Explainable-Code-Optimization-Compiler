from graphviz import Digraph


def generate_cfg(ir):
    """
    Generates a Control Flow Graph (CFG)
    for straight-line three-address code.
    """

    dot = Digraph(comment="Control Flow Graph")
    dot.attr(rankdir="TB")

    # Create nodes for each instruction
    for instr in ir:
        node_id = f"I{instr['id']}"
        dot.node(node_id, instr["code"], shape="box")

    # Sequential control flow edges
    for i in range(len(ir) - 1):
        src = f"I{ir[i]['id']}"
        dst = f"I{ir[i + 1]['id']}"
        dot.edge(src, dst)

    return dot
