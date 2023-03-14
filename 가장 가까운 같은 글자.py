def solution(s):
    answer = []
    lst = list(s) # [b a n a n a]
    dic = {}

    for i in range(len(lst)):
        if s[i] not in dic:  # b
            answer.append(-1)
            # dic[b] = 0, dic[a] = 1
        else:
            answer.append(i - dic[s[i]]) # 3 - 1
            # 2 dic[a] = 3
        dic[s[i]] = i

    return answer
