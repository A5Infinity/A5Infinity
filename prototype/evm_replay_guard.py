"""Prototype documentaire : garde-fou anti-rejeu pour un appel EVM."""

def replay_key(tx):
    fields=(tx.get("chain_id"),tx.get("sender"),tx.get("nonce"),tx.get("data_hash"))
    return fields if all(x is not None for x in fields) else None

def accept_once(tx, consumed):
    key=replay_key(tx)
    return key is not None and key not in consumed

if __name__ == "__main__":
    tx={"chain_id":8453,"sender":"0x1","nonce":4,"data_hash":"d"}
    assert accept_once(tx,set())
    assert not accept_once(tx,{replay_key(tx)})
    assert replay_key({**tx,"chain_id":1}) != replay_key(tx)
