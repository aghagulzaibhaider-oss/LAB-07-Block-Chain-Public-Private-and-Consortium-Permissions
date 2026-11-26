# Lab 07: Viva Questions and Answers

## Q1. Is a public chain unlimited write access?
No. In many public networks anyone may propose transactions, but a transaction is accepted only if it passes protocol validation (valid signature, enough balance, correct format) and is included by the consensus process. Fees also limit spam. So anyone can try to write, but not everything is accepted.

## Q2. Can a single company run a consortium alone?
It can run the permissioned infrastructure, but it is not really a consortium. A consortium means several institutions share governance. If one company controls everything, it is effectively a private network, and calling it a consortium hides the lack of shared control.

## Q3. Why require secure identities?
Without identity verification, anyone can claim to be the Registrar or Auditor just by supplying a string. My Step 6 demo shows this: with HMAC signatures the forged Registrar is denied. Authentication proves who you are, and authorization then decides what you may do. Both are needed.

## Extra questions you may be asked

**What is the difference between authentication and authorization?**
Authentication verifies identity (who are you?). Authorization checks permissions (what may you do?). My code only does authorization. The Step 6 demo adds authentication.

**Why is the Auditor read-only?**
An auditor needs to inspect records but must not change or approve them, otherwise independence is lost. This follows the principle of least privilege.

**Why does the code deny unknown actors?**
`policy.get(actor, set())` returns an empty set for unknown actors, so they get no permissions. This is default deny, which is safer than default allow.

**How do public, private and consortium networks differ?**
Public: open membership, anyone can join and propose transactions. Private: one organization controls membership and approval. Consortium: a group of organizations shares control and approval.

**Why must new members be approved by two admins?**
It avoids a single point of failure or abuse. One admin cannot add a malicious member alone. Duplicate approvals and non-admins do not count.

**Why is an audit log needed?**
It records who did what and when, so decisions can be checked and disputes resolved later.

**Is this a real blockchain?**
No. It simulates access control only. It has no blocks, consensus, networking or real cryptographic identity management.
