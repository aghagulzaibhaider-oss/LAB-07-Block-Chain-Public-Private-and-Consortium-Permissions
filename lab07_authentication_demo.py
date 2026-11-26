#!/usr/bin/env python3
"""Lab 07 Step 6: why role labels are NOT authentication.
Lab code trusts the string 'Registrar'. Here each actor has a secret key and
must sign the request (HMAC); a forged label fails verification."""
import hmac, hashlib

POLICY = {'Registrar': {'read', 'submit', 'approve'}, 'Auditor': {'read'}}
KEYS = {'Registrar': b'registrar-secret', 'Auditor': b'auditor-secret'}  # demo keys

def sign(actor, action, key):
    return hmac.new(key, f'{actor}:{action}'.encode(), hashlib.sha256).hexdigest()

def authorize(actor, action, signature):
    # 1) authentication: is the signature valid for this actor's key?
    if actor not in KEYS or not hmac.compare_digest(sign(actor, action, KEYS[actor]), signature):
        return 'DENY (authentication failed)'
    # 2) authorization: is the role allowed this action?
    return 'ALLOW' if action in POLICY.get(actor, set()) else 'DENY (not permitted)'

print('Naive lab code: attacker types "Registrar" -> ALLOW (just a string!)')
print('Genuine registrar approve :', authorize('Registrar', 'approve', sign('Registrar', 'approve', KEYS['Registrar'])))
print('Attacker claims Registrar :', authorize('Registrar', 'approve', sign('Registrar', 'approve', b'guessed-key')))
print('Genuine auditor approve   :', authorize('Auditor', 'approve', sign('Auditor', 'approve', KEYS['Auditor'])))
print('Genuine auditor read      :', authorize('Auditor', 'read', sign('Auditor', 'read', KEYS['Auditor'])))
