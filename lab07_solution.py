#!/usr/bin/env python3
"""Lab 07: role-based governance experiment (public / private / consortium).
Educational simulation only - NOT a live blockchain.
Colab:  !python lab07_solution.py --network public     (or run the cell directly)
"""
import argparse

# Step 1: policy matrix  ->  network -> actor -> set of allowed actions
POLICIES = {
    'public': {
        'Alice': {'read', 'submit'}, 'Bob': {'read', 'submit'},
        'Registrar': {'read', 'submit'}, 'Auditor': {'read'},          # extension
    },
    'private': {
        'Alice': set(), 'Bob': set(),
        'Registrar': {'read', 'submit', 'approve'}, 'Auditor': {'read'},
    },
    'consortium': {
        'Alice': {'read'}, 'Bob': {'read'},
        'Registrar': {'read', 'submit', 'approve'},
        'Employer': {'read', 'approve'}, 'Auditor': {'read'},
    },
}

# Step 4: requests (the last three are the new Auditor requests)
REQUESTS = [('Alice', 'submit'), ('Bob', 'approve'), ('Registrar', 'submit'),
            ('Employer', 'approve'), ('Auditor', 'read'),
            ('Auditor', 'submit'), ('Auditor', 'approve')]


def run(network):
    policy = POLICIES[network]
    for actor, action in REQUESTS:
        # unknown actor -> empty set -> DENY (default deny)
        allowed = action in policy.get(actor, set())
        print(f'network={network:10} actor={actor:10} action={action:7} -> '
              f'{"ALLOW" if allowed else "DENY"}')
    print()


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--network', choices=list(POLICIES) + ['all'], default='consortium')
    args, _ = p.parse_known_args()          # parse_known_args: safe inside Colab/Jupyter

    for net in (POLICIES if args.network == 'all' else [args.network]):
        run(net)

    # Extension check: Auditor is read-only in EVERY policy
    assert all(POLICIES[n]['Auditor'] == {'read'} for n in POLICIES)
    assert 'approve' in POLICIES['consortium']['Employer']
    assert 'approve' not in POLICIES['public']['Alice']
    print('PASS: explicit identity, roles and permission checks illustrated.')
    print('NOTE: open membership, transaction visibility and actual validator '
          'governance are separate questions.')
