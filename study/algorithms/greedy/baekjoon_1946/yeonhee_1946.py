import sys
input = sys.stdin.readline

# 	241916kb,	3300ms
def get_pass_count(score):
    # 서류 점수를 기준으로 오름차순
    # 서류 점수 1등은 무조건 통과
    score = sorted(score, key = lambda x : x[0])

    cnt = 1
    cmp_score = score[0]
    for idx in range(1, len(score)):
        if cmp_score[1] < score[idx][1]:
            continue
        cnt = cnt + 1
        cmp_score = score[idx]

    return cnt


testcase = int(input())
test_cases = []*testcase
for i in range(0, testcase):
    n = int(input())
    test_cases.append([])
    for _ in range(n):
        paper , interview = map(int, input().split(" "))
        test_cases[i].append((paper , interview))

for t in test_cases:
    print(get_pass_count(t))

