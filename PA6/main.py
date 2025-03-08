def inversions(A):
    def inv_helper(A):
        if len(A) <= 1:
            return 0, A 
        half = len(A) // 2
        A1 = A[:half]
        A2 = A[half:]
        c1, sorted_A1 = inv_helper(A1)
        c2, sorted_A2 = inv_helper(A2)
        c, merged = merge_and_count(sorted_A1, sorted_A2)
        return c1 + c2 + c, merged

    # Merge two sorted arrays and count split inversions
    def merge_and_count(A, B):
        i = j = c = 0
        merged = []
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                merged.append(A[i])
                i += 1
            else:
                merged.append(B[j])
                c += len(A) - i  # All remaining elements in A form inversions with B[j]
                j += 1
        merged.extend(A[i:])  # Append remaining elements
        merged.extend(B[j:])
        return c, merged

    # Call helper and return only the inversion count
    count, _ = inv_helper(A)
    return count

def intersections(coords):
    sorted_coords = sorted(coords, key=lambda x: x[0])
    ps_sorted = [p for _, p in sorted_coords]
    return inversions(ps_sorted)

def main():
    inst = int(input())
    answers = []
    for _ in range(inst):
        # Read number of pairs
        pairs = int(input())
        # Read qs and ps, one per line
        qs = [int(input()) for _ in range(pairs)]
        ps = [int(input()) for _ in range(pairs)]
        coords = list(zip(qs, ps))
        answers.append(intersections(coords))
    for _ in answers:
            print(_)
if __name__ == "__main__":
    main()

