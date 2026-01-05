# 4-1 등급 판정
score = input("당신의 점수는? ")
score = int(score)

if 100 >= score >= 90:
    print('짝짝짝~ A입니다')
elif 90 > score >= 80:
    print("아쉽지만 B입니다")
elif 80 > score >= 70:
    print("C입니다.. 공부 종 하셔야겠네요")
elif 70 > score >= 60:
    print("D? 공부 좀 해라ㅋ")
elif 0 <= score < 60:
    print("F. 던짐?")
else:
    print("잘못된 입력입니다.")
print('\n')


# 4-2 구구단 출력
gugu = input("구구단에서 원하는 단을 출력하세요: ")
gugu = int(gugu)

print(f"==={gugu}단===")
for i in range(1, 10):
    print(f"{gugu} x {i} = {i*gugu}")
print('\n')


# 4-3 소수 판별
sosu = list(range(2, 101))

for i in sosu.copy():
    for j in range(2, i):
        if i % j == 0:
            sosu.remove(i)
            break

print(sosu)
print('\n')


# 4-4 숫자 맞추기 게임
import random
answer = random.randint(1, 100)
count = 0

while True:
    num = input("숫자를 맞추세요: ")
    num = int(num)
    if num > answer:
        print("더 작은 수를 입력하세요")
        count += 1
    elif num < answer:
        print("더 큰 수를 입력하세요")
        count += 1
    else:
        count += 1
        print(f"정답입니다! {count}번 만에 맞추셨습니다!")
        break