def count_failure_reasosns(times):
    max_times = max(times)
    threshold = 0.25 * max_times
    failed_blocks = [time for time in times if time < threshold]

    failure_reasons = set(failed_blocks)
    return len(failure_reasons)

N = int(input())
times = [int(input()) for i in range(N)]
reasons_count = count_failure_reasosns(times)
print(reasons_count)