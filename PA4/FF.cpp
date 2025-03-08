#include <iostream>       
#include <vector>         
#include <unordered_set> 
#include <queue>          
#include <unordered_map>  


using namespace std;

int main() {
    int inst;
    cin >> inst;

    while (inst--) {
        int cache_size;
        int numReqs;
        cin >> cache_size;
        cin >> numReqs;

        //array of requests
        vector<int> reqs(numReqs);
        for(int i=0;i<numReqs;i++) {
            cin >> reqs[i];
        }
        //dict of positions 
        unordered_map<int, queue<int> > pos;
        for (int i=0; i<numReqs;i++){
            pos[reqs[i]].push(i);
        }

        // cache
        unordered_set<int> cache;
        int faults = 0;
        
        //loop through requests
        for(int i=0;i<numReqs;i++){
            
            int req = reqs[i];
            pos[req].pop();

            //hit
            if (cache.count(req) > 0) {
                continue;
            }

            faults++;

            //init misses
            if(cache.size() < cache_size) {
                cache.insert(req);
            }

            //evict
            else {
                int furthest = -1;
                int element = -1;
                
                //loop elements in cache
                for(int r : cache) { 
                    // q is empty meaning the element doesn't show again
                    if (pos[r].empty()) {
                        element = r;
                        break;
                    //check map, if q has next position of req is the furthest, update
                    } else if (pos[r].front() > furthest) {
                        furthest = pos[r].front();
                        element = r;

                    }
                }

            cache.erase(element);
            cache.insert(req);
            }
        }
        std::cout << faults << "\n";
    }
    return 0;
}

