input = input()
col = ord(input[0]) - 96
row = int(input[1])
# print(col, row)

count = 0

# a -> 97
# h -> 104
steps = [
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2)
]

for step in steps:
    result = (col+step[0], row+step[1])
    # print(result)
    if result[0] < 1 or result[0] > 8:
        continue
    if result[1] < 1 or result[1] > 8:
        continue
    count += 1

print(count)

########################################################################

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
# 나이트가 이동할 수 있는 8 가지 방향 정의
steps = [(- 2, - 1), (- 1, - 2), (1, - 2), (2, - 1),
         (2, 1), (1, 2), (- 1, 2), (- 2, 1)]
# 8 가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]  # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)
