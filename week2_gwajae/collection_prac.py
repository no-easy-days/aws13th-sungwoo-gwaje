# 3-1 이메일 주소 분리하기
user_name, domain = input("이메일 입력해주쇼: ").split('@')

print("사용자 이름: ", user_name)
print("도메인: ", domain)
print('\n')


# 3-2 비밀번호 길이 검사
pwd = input("비밀번호를 입력하세요: ")

if len(pwd) >= 8:
    print("유효한 비밀번호입니다.")
else:
    print("비밀번호는 8자 이상으로 설정해주세요.")
print('\n')


# 3-3 3의 배수 찾기
three_times = []
for i in range(1, 21):
    if i % 3 == 0:
        three_times.append(i)

print(three_times)
print('\n')


# 3-4 공통 관심사 찾기
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]
common = []

for i in chulsoo:
    for j in younghee:
        if i == j:
            common.append(i)
print(common)
print('\n')


# 3-5 최고의 점수 학생 찾기
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}

max_score = 0
max_name = ""

for i in scores:
    if scores[i] > max_score:
        max_name = i

print(max_name)
