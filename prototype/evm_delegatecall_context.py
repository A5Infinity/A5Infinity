"""Review the execution context preserved by DELEGATECALL."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Context:
    code_address:str
    storage_address:str
    sender:str
    value:int

def effective_context(caller:Context, callee_code:str)->Context:
    return Context(callee_code, caller.storage_address, caller.sender, caller.value)

def suspicious(c:Context, expected_storage:str)->list[str]:
    issues=[]
    if c.storage_address!=expected_storage: issues.append("unexpected storage target")
    if c.value<0: issues.append("negative value")
    if not c.sender: issues.append("missing sender")
    return issues

if __name__=="__main__": print(effective_context(Context("proxy","vault","alice",0),"logic"))
