# 단순하게 푸는 답안 예시
# N, M, K 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())  # N 개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

N, M, K = n, m, k

data.sort()  # 입력받은 수들 오름차순으로 정렬
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result = result + first
        m = m - 1
    if m == 0:
        break
    result = result + second
    m = m - 1

print(result)

########################################################################

big_count = (M // (K+1)) * K
big_count = big_count + (M % (K + 1))

small_count = M - big_count

result = 0
result += second * small_count + first * big_count

print(data)
print(result)

# 큰 수의 법칙
