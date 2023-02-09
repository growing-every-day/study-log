import sys

t = int(sys.stdin.readline()) # 테스트 케이스 개수

for _ in range(t):
    n = int(sys.stdin.readline()) # 지원자 수

    arr = []
    for i in range(n): # 각 지원자들의 서류심사, 면접 성적 입력
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort(key=lambda x: x[0]) # 서류심사 순으로 정렬

    answer = 0
    temp = arr[0][1] # 서류 심사 1위의 면접 성적

    for i in range(1, n):
        if temp > arr[i][1]: # temp에 저장된 성적보다 좋다면
            temp = arr[i][1]
            answer += 1

    print(answer+1) # 서류 심사 1위는 무조건 선발

"""
    문제 : 1946번 - 신입 사원
    메모리 : 51304 KB
    시간 : 3876 ms
"""
