n, m = map(int, input().split())  # N 개의 수를 공백으로 구분하여 입력받기

result = 0

########################################################################
# 나의 답안
min_value_list = []

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    min_value_list.append(min_value)

print(max(min_value_list))

########################################################################
# min() 함수를 이용하는 답안 예시

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))  # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)  # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)  # 최종 답안 출력

########################################################################
# 2중 반복문 구조를 이용하는 답안 예시
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input(). split()))  # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)  # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)
print(result)  # 최종 답안 출력

# 숫자 카드 게임
