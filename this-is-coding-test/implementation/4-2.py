# N를 입력받기
n = int(input())
M = 60
S = 60
count = 0

for h in range(n+1):
    # if h < 10:
    #     h = "0" + str(h)
    # else:
    #     h = str(h)
    for m in range(M):
        # if m < 10:
        #     m = "0" + str(m)
        # else:
        #     m = str(m)
        for s in range(S):
            # if s < 10:
            #     s = "0" + str(s)
            # else:
            #     s = str(s)
            # time = h+m+s
            time = str(h)+str(m)+str(s)
            if "3" in time:
                count += 1
                # print(time)
print(count)

########################################################################

# H 를 입력받기
h = int(input())
count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 ' 3 '이 포함되어 있다면 카운트 증가
            if ' 3 ' in str(i) + str(j) + str(k):
                count += 1
print(count)
