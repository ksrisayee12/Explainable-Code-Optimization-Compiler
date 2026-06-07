def print_logs(logs):
    print("\nOptimization Logs:")
    for log in logs:
        for k, v in log.items():
            print(f"{k}: {v}")
        print("-" * 30)
