"""Prototype pédagogique : politique d'accès à une sortie FHE."""

def can_decrypt(request, acl, purpose):
    if not isinstance(request,dict) or request.get("principal") not in set(acl):
        return False
    return request.get("purpose")==purpose and request.get("key_id") is not None

def authorize(request, acl, purpose, approved):
    return approved and can_decrypt(request,acl,purpose)

if __name__ == "__main__":
    r={"principal":"analyst","purpose":"risk","key_id":"k1"}
    assert authorize(r,["analyst"],"risk",True)
    assert not authorize(r,["analyst"],"risk",False)
    assert not authorize({**r,"purpose":"other"},["analyst"],"risk",True)
