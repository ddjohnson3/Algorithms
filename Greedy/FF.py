

inst = int(input())
for _ in range(inst):
    cache_size = int(input())
    numReqs = int(input())
    reqs = input().split()
    cache = set()
    faults = 0
    for i in range(len(reqs)):
        #hit
        req = reqs[i]
        if req in cache:
            continue
        faults+=1

        #init misses
        if len(cache)<cache_size:
            cache.add(req)
        #evict
        else:
            furthest = -1
            element = None
            for page in cache:
                if page not in reqs[i+1:]:
                    element = page
                    break
                else:
                    dist = reqs[i+1:].index(page)+1
                    if dist>furthest:
                        furthest = dist
                        element = page
            

            cache.remove(element)
            cache.add(req)
    print(faults)






