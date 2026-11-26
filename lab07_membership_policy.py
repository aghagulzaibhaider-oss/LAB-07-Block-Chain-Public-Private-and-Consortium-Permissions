#!/usr/bin/env python3
"""Lab 07 Step 5: membership policy.
Rule: a new member needs approval from TWO distinct existing administrators,
then verified identity onboarding, and every action is audit-logged."""
from datetime import datetime

admins = {'AdminOrgA', 'AdminOrgB', 'AdminOrgC'}
members = set(admins)
audit_log = []

def log(event):
    audit_log.append(f'{datetime.now().isoformat(timespec="seconds")} {event}')

def add_member(new_member, approvals, identity_verified):
    valid = set(approvals) & admins                 # only real admins count, no duplicates
    if len(valid) < 2:
        log(f'REJECTED {new_member}: only {len(valid)} admin approval(s)')
        return False
    if not identity_verified:
        log(f'REJECTED {new_member}: identity not verified')
        return False
    members.add(new_member)
    log(f'ADDED {new_member}: approved by {sorted(valid)}')
    return True

print(add_member('NewBank', ['AdminOrgA'], True))                       # False: 1 approval
print(add_member('NewBank', ['AdminOrgA', 'AdminOrgA'], True))          # False: duplicate
print(add_member('NewBank', ['AdminOrgA', 'Mallory'], True))            # False: Mallory not admin
print(add_member('NewBank', ['AdminOrgA', 'AdminOrgB'], False))         # False: no ID check
print(add_member('NewBank', ['AdminOrgA', 'AdminOrgB'], True))          # True
print('\nAudit log:'); [print(' ', e) for e in audit_log]
