class LiveRangeCompression:
    name = "Live Range Compression"

    def apply(self, ir, live_after):
        optimized = ir.copy()
        logs = []

        moved = False

        for i in range(len(optimized)):
            instr = optimized[i]
            lhs = instr["code"].split("=")[0].strip()

            if not lhs.startswith("t"):
                continue

            first_use = None

            for j in range(i + 1, len(optimized)):
                if lhs in optimized[j]["code"]:
                    first_use = j
                    break

            if first_use and first_use > i + 1:
                definition = optimized.pop(i)
                optimized.insert(first_use - 1, definition)

                logs.append({
                    "optimization": "live_range_compression",
                    "variable": lhs,
                    "reason": "Moved definition closer to first use",
                    "blocked": False
                })

                moved = True
                break

        if not moved:
            logs.append({
                "optimization": "live_range_compression",
                "variable": "none",
                "reason": "No reordering possible",
                "blocked": True
            })

        return optimized, logs
