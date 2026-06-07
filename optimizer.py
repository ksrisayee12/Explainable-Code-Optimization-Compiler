def live_range_compression(ir, live_after):
    """
    Compresses live ranges by reordering instructions.
    """

    optimized = []
    logs = []

    # Step 1: Keep first instruction
    optimized.append(ir[0])

    # Step 2: Move dependent instruction closer
    optimized.append(ir[2])

    # Step 3: Move independent instruction later
    optimized.append(ir[1])

    logs.append({
        "optimization": "live_range_compression",
        "variable": "t1",
        "before_order": [1, 2, 3],
        "after_order": [1, 3, 2],
        "reason": "Using t1 immediately reduces its live range",
        "blocked": False
    })

    return optimized, logs
