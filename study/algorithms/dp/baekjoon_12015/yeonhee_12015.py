import sys
from bisect import bisect_left
input = sys.stdin.readline

# 157636kb	932ms
n = int(input())
arr = list(map(int, input().split(" ")))
lis = []
ans = 0

for num in arr:
    # lis가 비어있으면(for문의 시작이면) 맨 첫번째로 입력받은 값 넣어주고 시작
    if not lis:
        lis.append(num)
        ans += 1
        continue
    
    # 부분수열의 맨 마지막 값(가장 큰값)과 입력받은 수를 비교, 
    #   맨 마지막 값보다 크면 뒤에 그냥 추가해준다.
    if lis[-1] < num:
        lis.append(num)
        ans += 1
    # 맨 마지막 값보다 작으면 수열에 들어갈 수 있는 위치를 찾아준다.
    # bisect_left - 바이너리 서치를 이용해서 가장 왼쪽에 들어갈 수 있는 인덱스를 구해서 넣어준다.
    else:
        index = bisect_left(lis, num)
        lis[index] = num
    # print(lis,num,ans)
    
print(ans)

# 참고: 
# https://velog.io/@uoayop/BOJ-12015-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2-Python
