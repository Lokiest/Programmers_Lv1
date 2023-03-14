def solution(s):
    answer = []
    lst = list(s)
    dic = {}

    for i in range(len(lst)):
        if s[i] not in dic:
            answer.append(-1)
            dic[s[i]] = i
        else:
            answer.append(i - dic[s[i]])
            dic[s[i]] = i

    return answer
