from itertools import permutations, combinations, product, combinations_with_replacement
# Python 표준 라이브러리
# https://docs.python.org/ko/3/library/index.html

# 필수 6가지 라이브러리
# - 내장 함수
# eval: 수학 수식이 문자열 형식으로 들어오면 해당 수식 계산 결과 반환
result = eval("( 3 + 5 ) * 7 ")
print(result)


# sorted(객체, reverse = True) -> 정렬(오름/내림 차순)


# - itertools: 반복되는 형태의 데이터를 처리하는 기능 -> 순열과 조합 라이브러리를 제공

# 순열
data = ['A', 'B', 'C']  # 데이터 준비
result = list(permutations(data, 3))
print(result)

# 조합
data = ['A', 'B', 'C']  # 데이터 준비
result = list(combinations(data, 2))
print(result)

# 중복 순열
data = ['A', 'B', 'C']  # 데이터 준비
result = list(product(data, repeat=2))
print(result)

# 중복 조합
data = ['A', 'B', 'C']  # 데이터 준비
result = list(combinations_with_replacement(data, 2))
print(result)

# - heapq: 힙(heap) 기능을 제공하는 라이브러리 -> 다익스트라 최단 경로, 우선순위 큐 기능을 구현하기 위하여 사용

# - bisect: 이진 탐색(Binary Search) 기능을 제공

# - collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함

# - math: 필수적인 수학적 기능을 제공 -> 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수, 파이 등 포함
