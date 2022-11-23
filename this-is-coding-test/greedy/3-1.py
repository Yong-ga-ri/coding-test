# my solution
input_money = input()
coin_types = [500, 100, 50, 10]


def get_change(input_money):
    count = 0
    input_money = int(input_money)
    for coin in coin_types:
        num = input_money // coin
        input_money = input_money % coin
        count = count + num

    return count


result = get_change(input_money)
print(result)

########################################################################
# solution example
n = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
    print(count)

# 당장 좋은 것만 선택하는 그리디
