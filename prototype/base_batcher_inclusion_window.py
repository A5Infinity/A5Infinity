"""Classify the documentary lifecycle of a Base batch."""
from enum import Enum

class Stage(str, Enum):
    SEQUENCED="sequenced"; L1_INCLUDED="l1-included"; CONFIRMED="confirmed"; UNKNOWN="unknown"

def classify(sequenced_at:int, l1_at:int|None, confirmed_at:int|None, now:int)->Stage:
    if sequenced_at<0 or now<sequenced_at: return Stage.UNKNOWN
    if l1_at is None: return Stage.SEQUENCED
    if l1_at<sequenced_at or l1_at>now: return Stage.UNKNOWN
    if confirmed_at is None: return Stage.L1_INCLUDED
    if confirmed_at<l1_at or confirmed_at>now: return Stage.UNKNOWN
    return Stage.CONFIRMED

if __name__=="__main__": print(classify(10,20,30,40).value)
