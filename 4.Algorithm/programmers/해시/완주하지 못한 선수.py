def solution(participant, completion):
    answer = ''
    # 시간초과 발생
    # for i in participant:
    #     if i in completion:
    #         completion.remove(i)
    #     else:
    #         answer = i

    participant.sort()
    completion.sort()
    cnt = 0
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            cnt += 1
    # 마지막 선수 말고 다 통과했으면 결국 마지막 선수가 못 들어온것
    if cnt == len(completion):
        answer = participant[-1]
    return answer