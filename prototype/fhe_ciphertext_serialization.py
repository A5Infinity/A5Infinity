"""Canonical encoding model for versioned FHE ciphertext metadata."""
from dataclasses import dataclass
from hashlib import sha256

@dataclass(frozen=True)
class Ciphertext:
    version:int; kind:str; context:str; payload:bytes

def encode(c:Ciphertext)->bytes:
    if c.version<1 or not c.kind or not c.context or not c.payload: raise ValueError("ambiguous ciphertext")
    header=f"v={c.version}|kind={c.kind}|ctx={c.context}|len={len(c.payload)}|".encode()
    return header+c.payload

def digest(c:Ciphertext)->str: return sha256(encode(c)).hexdigest()

if __name__=="__main__": print(digest(Ciphertext(1,"u32","app",b"data")))
