"""Defensive boundary checks for a documentary precompile call."""
def validate(chain_id:int, expected_chain:int, payload:bytes, gas:int, min_gas:int)->str:
    if chain_id!=expected_chain: return "deny:chain"
    if not payload: return "deny:empty-payload"
    if gas<min_gas: return "deny:gas"
    return "allow"

if __name__=="__main__": print(validate(999,999,b"call",100,50))
