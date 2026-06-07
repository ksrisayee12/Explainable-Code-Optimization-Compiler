def generate_ir():
    """
    Generates three-address code (TAC)
    """

    return [
        {"id": 1, "code": "t1 = a + b"},
        {"id": 2, "code": "t2 = c + d"},
        {"id": 3, "code": "t3 = t1 * e"}
    ]
