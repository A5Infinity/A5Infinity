"""Routage pédagogique d un dépôt Base vers une destination L2."""

def route(deposit, expected_chain):
    required = {"sender", "amount", "chain_id", "nonce"}
    return isinstance(deposit, dict) and required <= deposit.keys() and deposit["chain_id"] == expected_chain and deposit["amount"] > 0

if __name__ == "__main__":
    assert route({"sender":"alice","amount":10,"chain_id":8453,"nonce":1},8453)
    assert not route({"sender":"alice","amount":0,"chain_id":8453,"nonce":1},8453)
