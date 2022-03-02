def happiness_eval():
    n_m = [int(val) for val in input().split(' ')]
    arr = [int(val) for val in input().split(' ')]
    set_a = {int(val) for val in input().split(' ')}
    set_b = {int(val) for val in input().split(' ')}

    happiness = 0

    for i in arr:
        if i in set_a:
            happiness += 1
        elif i in set_b:
            happiness -= 1

    print(happiness)


happiness_eval()
