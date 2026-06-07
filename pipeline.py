class CompilerPipeline:
    def __init__(self):
        self.optimizations = []

    def add_optimization(self, optimization):
        """
        Registers an optimization pass (plugin)
        """
        self.optimizations.append(optimization)

    def run_optimizations(self, ir, live_after):
        """
        Runs all registered optimizations sequentially
        """
        current_ir = ir
        all_logs = []

        for opt in self.optimizations:
            current_ir, logs = opt.apply(current_ir, live_after)
            all_logs.extend(logs)

        return current_ir, all_logs
