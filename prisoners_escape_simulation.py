from random import *

def find_cycle(v, i):
    cycle_id = i
    j = i
    cycle = [j]
    j = v[j]
    while j != i:
        cycle.append(j)
        j = v[j]
    return cycle_id, cycle

def find_cycles(v):
    cycles = {}
    found = set()
    for i in range(len(v)):
        if i in found:
            continue
        cycle_id, cycle = find_cycle(v, i)
        found = found.union(set(cycle))
        cycles[cycle_id] = cycle
    print(f"cycles \n{cycles}")
    return cycles

def prisoners_escape_setup(n):
    prisoners = [_ for _ in range(n)]
    boxes = sample(range(n), n)
    return prisoners, boxes

def prisoner_escape_random(prisoner, boxes, num_attempts):
    n = len(boxes)
    opened, closed = set(), sample(range(n), n)
    while len(opened) < num_attempts:
        pick = choice(closed)
        opened.add(pick)
        closed.remove(pick)
        if pick == prisoner:
            return True, opened
    return False, len(opened)


def prisoner_escape_in_cycles(prisoner, boxes, num_attempts):
    n = len(boxes)
    opened, closed = set(), sample(range(n), n)
    pick = prisoner
    while len(opened) < num_attempts:
        if prisoner == boxes[pick]:
            return True, opened
        opened.add(pick)
        closed.remove(pick)
        pick = boxes[pick]
    return False, opened

def prisoners_escape(prisoners, boxes, num_attempts, winners, function):
    n = len(prisoners)
    tried, remaining = set(), sample(range(n), n)
    successes, failures = 0, 0
    while remaining:
        prisoner = choice(remaining)
        remaining.remove(prisoner)
        tried.add(prisoner)
        success, opened = function(prisoner, boxes, num_attempts)
        successes += 1 if success else 0
        failures += 0 if success else 1
        if winners >= n // 2:
            if failures > (n - winners):
                return False
        else:
            if successes >= winners:
                return True
    return True if successes >= winners else False

def prisoners_escape_solve(n, f=0.5, q=1.0, cycles=False):
    num_attempts = int(n * f)
    winners = int(n * q)
    # print(f"winners = {winners}")
    iterations = n * 10000
    successes, failures = 0, 0
    for i in range(iterations):
        prisoners, boxes = prisoners_escape_setup(n)
        function = prisoner_escape_in_cycles if cycles else prisoner_escape_random
        success = prisoners_escape(prisoners, boxes, num_attempts, winners, function)
        successes += 1 if success else 0
        failures += 0 if success else 1
    return successes, failures

if __name__ == '__main__':
    # Number of prisoners
    n = 10
    # Fraction of boxes a prisoner is allowed to open
    f = 0.5
    # Fraction of prisoners requried to succeed
    q = 1
    successes, failures = prisoners_escape_solve(n, f=f, q=q, cycles=True)
    print(f"successes = {successes}, failures = {failures}")