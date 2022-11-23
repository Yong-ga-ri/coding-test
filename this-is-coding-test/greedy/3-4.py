# 나의 답안
n, k = map(int, input().split())

count = 0

while n != 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

########################################################################
# 단순하게 푸는 답안 예시
# N 이 K 이상이라면 K 로 계속 나누기
result = 0
while n >= k:
    # N 이 K 로 나누어 떨어지지 않는다면 N 에서 1 씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K 로 나누기
    n //= k
    result += 1
# 마지막으로 남은 수에 대하여 1 씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

########################################################################
# 답안 예시

result = 0
while True:
    # ( N == K 로 나누어떨어지는 수)가 될 때까지 1 씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N 이 K 보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K 로 나누기
    result += 1
    n //= k
# 마지막으로 남은 수에 대하여 1 씩 빼기
result += (n - 1)
print(result)
