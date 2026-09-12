"""Tests sans dependance pour les invariants."""
from prototype.evm_replay_guard import ReplayGuard
from prototype.fhe_access_policy import AccessPolicy
from prototype.zk_claim_verifier import valid

def run():
    assert valid({"statement":"S","proof":"P","verifier_id":"v"}, "S")
    assert not valid({"statement":"T","proof":"P","verifier_id":"v"}, "S")
    policy = AccessPolicy()
    assert policy.allow("alice", "analytics", "key-1")
    assert not policy.allow("bob", "analytics", "key-1")
    guard = ReplayGuard()
    assert guard.accept(8453, "alice", 1, "payload")
    assert not guard.accept(8453, "alice", 1, "payload")

if __name__ == "__main__":
    run()
    print("prototype invariants: ok")
