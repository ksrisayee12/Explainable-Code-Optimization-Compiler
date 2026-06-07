def get_rhs_vars(statement):
    rhs = statement.split("=")[1]
    rhs = rhs.replace("+", " ").replace("*", " ")
    return [v for v in rhs.split() if v.isalpha()]


def compute_liveness(ir):
    live_after = {}
    live = set()

    for instr in reversed(ir):
        stmt = instr["code"]
        lhs = stmt.split("=")[0].strip()
        rhs_vars = get_rhs_vars(stmt)

        live_after[instr["id"]] = live.copy()

        if lhs in live:
            live.remove(lhs)

        for v in rhs_vars:
            live.add(v)

    return live_after


def compute_live_range(ir, variable):
    define = None
    last_use = None

    for idx, instr in enumerate(ir):
        code = instr["code"]

        if code.startswith(variable):
            define = idx

        if variable in code.split("=")[1]:
            last_use = idx

    if define is None or last_use is None:
        return 0

    return last_use - define
