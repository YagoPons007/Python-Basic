prev = 0
curr = 1
next_term = prev + curr
while next_term < 34:
    prev += 1
    curr += 1
    next_term = prev + next_term
    print(next_term)