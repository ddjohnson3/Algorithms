

def loadSack(capacity, items):
    n = len(items)
    v = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        wi = items[i-1][0]  
        vi = items[i-1][1] 
        
        for w in range(capacity + 1):
            
            if w >= wi:
                
                v[i][w] = max(v[i-1][w], v[i-1][w-wi] + vi)
            else:
                v[i][w] = v[i-1][w]
    
    return v[n][capacity] 

def main():
    inst = int(input())
    results = []
    while inst > 0:
        inst -= 1
        numItems, capacity = map(int, input().split())
        items = []
        for i in range(numItems):
            items.append(list(map(int, input().split())))
        results.append(loadSack(capacity, items))
    for _ in results:
        print(_)
    
if __name__ == "__main__":
    main()