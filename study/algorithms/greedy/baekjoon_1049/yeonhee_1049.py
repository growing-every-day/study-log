import sys
input = sys.stdin.readline
# https://www.acmicpc.net/problem/1049
# 113248kb,	112ms

n,m = map(int, input().split(' '))

package_list = []
single_list = []
for _ in range(m):
    a, b = map(int, input().split(' '))
    package_list.append(a)
    single_list.append(b)

package_list.sort()
single_list.sort()
total = 0

# 세트, 단일 가격 같은 브랜드여도 따로 생각
# 세트 가격에서 현재 필요한 기타 개수에 해당하는 가격 비율을 구해서
# 단일 가격중 가장 싼 것과 비교
# n,m = 7,2이고 각각 [10 3] [12 2]일때
# package_list = 10, 12 // single_list = 2, 3이렇게 저장
# 10 / 6 -> 세트에서 한 개당 가격 vs 2와 비교 -> 10세트를 사는게 더 이득이다
# 전체 7개중(n) 가격이 10인 6개 세트를 사는게 이득이므로 total가격에 + 10을 하고 
# n = n- 6이 된다
# 이제 기타줄은 한개 남았고 또 비교를 한다
# a = 10 / 1 = 10이고 a 와  2를 비교하는데 단일 가격 2인 것을 사는게 이득
# total = total + 2 * 필요한 갯수(n)이 실행되고  while탈출

while n > 0:
    if n >= 6 :
        a = package_list[0] / 6
    else: 
        a = package_list[0] / n

    if a > single_list[0]:
        total = total + single_list[0]*n
        break

    n = n - 6
    total = total + package_list[0]

print(total)