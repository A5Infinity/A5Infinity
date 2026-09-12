"""Prototype pédagogique : verifier la structure d'un claim ZK public."""

REQUIRED=("statement","proof","verifier_id")

def claim_is_complete(claim):
    return isinstance(claim,dict) and all(claim.get(k) is not None for k in REQUIRED)

def verify_claim(claim, expected_statement, trusted_verifiers):
    return (claim_is_complete(claim) and claim["statement"]==expected_statement
            and claim["verifier_id"] in set(trusted_verifiers))

if __name__ == "__main__":
    c={"statement":"S","proof":"P","verifier_id":"v1"}
    assert verify_claim(c,"S",["v1"])
    assert not verify_claim(c,"T",["v1"])
