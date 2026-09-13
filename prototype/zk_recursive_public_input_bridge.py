"""Check the boundary between child and parent recursive proofs."""
def bridge(child:list[int], parent:list[int], offset:int=0)->str:
    if offset<0 or offset+len(child)>len(parent): return "deny:range"
    if parent[offset:offset+len(child)]!=child: return "deny:mismatch"
    return "allow"

if __name__=="__main__": print(bridge([3,5],[3,5,8]))
