#!/usr/bin/env python
def exor(a, b):
    if a == b:
        return 0
    else:
        return 1

def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    n = len(states)

    if states == [0]*(n) or days <= 0:
        return states

    for i in range(days):
        new_states = [0]*(n)
        for j in range(n):
            if j == 0:
                new_states[j] = exor(0, states[j+1])
            elif j == n-1:
                new_states[j] = exor(states[j-1], 0)
            else:
                new_states[j] = exor(states[j-1], states[j+1])

        states = new_states

    print states

states=[1,1,1,0,1,1,1,1]
days = 2
cellCompete(states, days)
