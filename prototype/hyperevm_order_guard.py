"""Contrôle pédagogique d un ordre signé avant envoi HyperEVM."""

def accept(order, expected_chain, now):
    required = {"chain_id", "sender", "nonce", "payload", "signature", "expires_at"}
    if not isinstance(order, dict) or not required <= order.keys(): return False
    if order["chain_id"] != expected_chain or not order["signature"]: return False
    return order["expires_at"] >= now

if __name__ == "__main__":
    sample = {"chain_id":999,"sender":"alice","nonce":4,"payload":"swap","signature":"sig","expires_at":100}
    assert accept(sample,999,90)
    assert not accept(sample,998,90)
    assert not accept(sample,999,101)
