# 동빈나 이코테 거스름돈 카운트  
print("금액 입력")
a = int(input())

b = [500, 100, 50, 10]
c = [0, 0, 0, 0]
for i in range(len(b)):
    c[i] = a // b[i]
    a = a % b[i] 

print(f"500원 동전 {c[0]} 개 100원 동전 {c[1]} 개 50원 동전 {c[2]} 개 10원 동전 {c[3]} 개 입니다")
    

