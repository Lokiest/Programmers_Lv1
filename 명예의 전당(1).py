def solution(k, score):
    answer = []
    lst = []
    for i in range(len(score)):
        lst.append(score[0])
        if len(answer) < k:
            lst.sort()
            score.pop(0)
            if lst[0] == min(lst):
                answer.append(lst[0])

        else:
            score.pop(0)
            lst.sort()
            if lst[0] < lst[1]:
                lst.pop(0)
                answer.append(lst[0])
            else:
                lst.pop(1)
                answer.append(lst[0])

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
