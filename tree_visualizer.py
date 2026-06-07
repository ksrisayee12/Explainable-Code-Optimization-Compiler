from graphviz import Digraph


def generate_scheduled_tree(ir, title="Scheduled Dependency Tree"):
    """
    Generates a dependency tree that also encodes
    instruction execution order.
    """

    dot = Digraph(comment=title)
    dot.attr(rankdir="TB")

    variable_nodes = {}
    step = 1

    for instr in ir:
        code = instr["code"]
        lhs, rhs = code.split("=")
        lhs = lhs.strip()
        rhs = rhs.strip()

        instr_node = f"instr_{step}"
        instr_label = f"{step}: {code}"
        dot.node(instr_node, instr_label, shape="box")

        # RHS dependencies
        rhs_tokens = rhs.replace("+", " ").replace("*", " ").split()
        for token in rhs_tokens:
            if token.isalpha():
                if token not in variable_nodes:
                    variable_nodes[token] = f"var_{token}"
                    dot.node(variable_nodes[token], token)
                dot.edge(variable_nodes[token], instr_node)

        # LHS definition
        if lhs not in variable_nodes:
            variable_nodes[lhs] = f"var_{lhs}"
            dot.node(variable_nodes[lhs], lhs)

        dot.edge(instr_node, variable_nodes[lhs])

        step += 1

    return dot
