### 수 자료형 ###

### 리스트 자료형 ###

# 크기가 N 이고, 모든 값이 0 인 1 차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트 컴프리헨션: 리스트를 초기화하는 방법
# 0 부터 19 까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(array)

# 1 부터 9 까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N X M 크기의 2 차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

# remove _ set 에 포함되지 않은 값만을 저장
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)

### 문자열 자료형 ##
data = "Don't you know \"Python\"?"
print(data)

### 튜플 자료형 ###
# 그래프 알고리즘에 많이 사용됨

### 사전 자료형 ###
# 파이썬의 사전 자료형은 내부적으로 '해시 테이블[Hash Table]'을 이용
# -> 데이터 검색, 수정을 O(1)의 시간에 처리할 수 있음.
# dict().keys()
# dict().values()

### 집합 자료형 ###
# 집합은 기본적으로 리스트or문자열을 이용하여 만들 수 있다.
# // 특징 //
# - 중복을 허용하지 않는다.
# - 순서가 없다.
# - 특정 원소의 존재 여부 검사의 연산 시간 복잡도: O(1) == 사전 자료형
# - 특히 특정한 데이터가 이미 등장한 적이 있는지 여부 체크할 때 효과적
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b)  # 합집합
print(a & b)  # 교집합
print(a - b)  # 차집합

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)
# 새로운 원소 추가
data.add(4)
print(data)
# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)
# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

# add(), remove()는 모두 시간 복잡도가 O(1)
score = 85
if score >= 80:
    result = "Success"
else:
    result = "Fail"
