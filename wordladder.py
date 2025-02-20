from typing import *

def ShortestWordChainLength(start:str,target:str,D:Set[str]) ->int:
    if start==target:
        return 0
    
    umap: Dict[str,List[str]]={}
    for i in range(len(start)):
        intermediate_word=start[:i] +"_"+start[i+1:]
        umap[intermediate_word]=[]

    for word in D:
        for i in range(len(word)):
            intermediate_word=word[:i] +"_"+word[i+1:]
            if intermediate_word not in umap:
                umap[intermediate_word]=[]
            umap[intermediate_word].append(word)

    q=[(start,1)]
    visited={start:1}

    while q:
        word,dist=q.pop(0)
        if word==target:
            return dist
        
        for i in range(len(word)):
            intermediate_word=word[:i]+"_"+word[i+1:]
            var=umap[intermediate_word]
            for k in range(len(var)):
                if var[k] not in visited:
                    visited[var[k]]=1
                    q.append((var[k],dist+1))
    return 0
D = {'poon', 'plee', 'same', 'poie', 'plie', 'poin', 'plea'}
start = "toon"
target = "plea"
print(f"Length of shortest chain is: {ShortestWordChainLength(start, target, D)}")
