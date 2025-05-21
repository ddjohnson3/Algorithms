
def MergeCount(A, B):
    S = []
    c = 0
    i = 0
    j = 0
    
    while i < len(A) or j < len(B):
        if i >= len(A): #A is empty
            S.append(B[j])
            j += 1
        elif j >= len(B): #B is empty
            S.append(A[i])
            i += 1
        else:
            if A[i] <= B[j]:
                S.append(A[i])
                i += 1
            else: #A[i] > B[j]
                S.append(B[j])
                j += 1
                c += len(A) - i
    
    return S, c


def CountSort(A, n):
    if (len(A) == 1):
        return (A,0)

    half = n // 2
    front = A[:half]
    back = A[half:]
    (A1, c1) = CountSort(front, len(front))
    (A2, c2) = CountSort(back, len(back))
    (S,c) = MergeCount(A1,A2)


    return (S,c + c1 + c2)



def main():
    results = []
    inst = int(input())
    for _ in range(inst):
        n = int(input())
        elements = list(map(int, input().split()))
        results.append(CountSort(elements, n)[1])
    for result in results:
        print(result)

if __name__ == "__main__":
    main()


