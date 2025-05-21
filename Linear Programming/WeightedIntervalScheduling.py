import bisect

T = int(input())

for _ in range(T):
    n = int(input())
    jobs = [tuple(map(int, input().split())) for _ in range(n)]
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    end_times = [job[1] for job in sorted_jobs]
    starts = [job[0] for job in sorted_jobs]
    weights = [job[2] for job in sorted_jobs]
    DP = [0] * (n + 1)
    for i in range(1, n + 1):
        start_i = starts[i - 1]
        j = bisect.bisect_right(end_times, start_i, 0, i) - 1
        if j >= 0:
            p = j
        else:
            p = -1
        if p >= 0:
            DP[i] = max(DP[i - 1], weights[i - 1] + DP[p + 1])
        else:
            DP[i] = max(DP[i - 1], weights[i - 1])
    print(DP[n])