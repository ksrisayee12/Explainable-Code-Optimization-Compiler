def generate_tac_from_code(source_code):
    """
    Very simple frontend that converts basic
    assignment expressions into three-address code.

    Supported:
      a = b + c;
      d = a * e;
    """

    ir = []
    temp_count = 1
    instr_id = 1

    lines = source_code.splitlines()

    for line in lines:
        line = line.strip().replace(";", "")
        if not line:
            continue

        lhs, expr = line.split("=")
        lhs = lhs.strip()
        expr = expr.strip()

        if "+" in expr:
            op1, op2 = expr.split("+")
            t = f"t{temp_count}"
            ir.append({"id": instr_id, "code": f"{t} = {op1.strip()} + {op2.strip()}"})
            instr_id += 1
            ir.append({"id": instr_id, "code": f"{lhs} = {t}"})
            instr_id += 1
            temp_count += 1

        elif "*" in expr:
            op1, op2 = expr.split("*")
            t = f"t{temp_count}"
            ir.append({"id": instr_id, "code": f"{t} = {op1.strip()} * {op2.strip()}"})
            instr_id += 1
            ir.append({"id": instr_id, "code": f"{lhs} = {t}"})
            instr_id += 1
            temp_count += 1

        else:
            # Simple assignment
            ir.append({"id": instr_id, "code": f"{lhs} = {expr}"})
            instr_id += 1

    return ir
