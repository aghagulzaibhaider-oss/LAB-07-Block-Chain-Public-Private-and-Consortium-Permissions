# Lab 07: Public, Private and Consortium Permissions

**Course:** Introduction to Blockchain
**Student:** (your name and roll number)
**Type:** Educational simulation (not a live blockchain)

## 1. Purpose
Public, private and consortium networks differ in who can join, read, submit, validate and approve. This lab models those differences with a role-to-action permission table. The program checks each request and prints ALLOW or DENY. It shows that access control is a practical way to represent network types, and that real systems also need secure authentication, audit logging, revocation and governance.

## 2. Files
| File | Description |
|---|---|
| `lab07_solution.py` | Main lab: policy matrix for three networks, with the required Auditor extension |
| `lab07_membership_policy.py` | Step 5: a new member needs 2 distinct admin approvals, verified identity and an audit log |
| `lab07_authentication_demo.py` | Step 6: shows that role labels are not authentication, using HMAC-signed requests |
| `Lab07_Colab.ipynb` | Notebook that runs everything in order |
| `Viva_Answers.md` | Viva questions and answers |

## 3. How to run (Google Colab)
1. Upload the three `.py` files in the Files panel (folder icon on the left).
2. Run these commands in separate cells:
```
!python lab07_solution.py --network public
!python lab07_solution.py --network private
!python lab07_solution.py --network consortium
!python lab07_solution.py --network all
!python lab07_membership_policy.py
!python lab07_authentication_demo.py
```
Colab deletes uploaded files when the session ends, so upload them again if you restart.

## 4. Logic
1. `POLICIES` is a dictionary: network, then actor, then a set of allowed actions.
2. A request is allowed only if `action in policy.get(actor, set())`. An unknown actor gets an empty set, so the result is DENY (default deny).
3. **Extension:** `'Auditor': {'read'}` was added to every policy, with three Auditor requests (read, submit, approve). Assert statements confirm the Auditor is read-only in all three networks.
4. **Step 5:** `add_member()` counts only distinct approvals from existing admins. It needs at least 2, then a verified identity, and it logs every decision.
5. **Step 6:** each actor signs a request with a secret key. The system verifies the signature (authentication) before checking the role (authorization).

## 5. Results
| Actor / Action | Public | Private | Consortium |
|---|---|---|---|
| Alice submit | ALLOW | DENY | DENY |
| Bob approve | DENY | DENY | DENY |
| Registrar submit | ALLOW | ALLOW | ALLOW |
| Employer approve | DENY | DENY | ALLOW |
| Auditor read | ALLOW | ALLOW | ALLOW |
| Auditor submit | DENY | DENY | DENY |
| Auditor approve | DENY | DENY | DENY |

**Observations**
- Approval power is restricted in the private network (Registrar only) and shared in the consortium (Registrar and Employer).
- The Auditor can only read in every network.
- Step 5 output: `False False False False True`, with 4 rejections and 1 addition in the audit log.
- Step 6 output: a forged "Registrar" is denied with "authentication failed".

## 6. Limitations
- The access table is a toy policy, not a real permissioned blockchain.
- The main program trusts hard-coded strings. Real systems must bind identities to keys or accounts.
- The HMAC demo uses hard-coded demo keys. Real keys must be stored and rotated securely.
- Open membership, transaction visibility and validator governance are separate questions not covered here.
