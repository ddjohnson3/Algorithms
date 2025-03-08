import sys

def main():
    def readints():
        return list(map(int, sys.stdin.readline().split()))

    inst = int(sys.stdin.readline())
    results = [] 

    for _ in range(inst):
        numjobs = int(sys.stdin.readline())
        jobs = []
        for _ in range(numjobs):
            start, end = map(int, sys.stdin.readline().split())
            jobs.append((start, end))

        jobs.sort(key=lambda x: x[1])

        card = 0
        job_finish = -1
        for job in jobs:
            if job[0] >= job_finish:
                card += 1
                job_finish = job[1]

        results.append(card) 

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
