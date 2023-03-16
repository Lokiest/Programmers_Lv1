def solution(number, limit, power):
    answer = 0
    G = [1]

    for i in range(2, number + 1):
        answer = 0
        for j in range(1, int(i**(1/2)) + 1):
            if i % j == 0:
                if j == i / j:
                    answer += 1
                else:
                    answer += 2

        if answer > limit:
            G.append(power)
        else:
            G.append(answer)
    return sum(G)
