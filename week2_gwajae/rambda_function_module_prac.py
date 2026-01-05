# 5-1 정렬하기
from curses.ascii import isupper

cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]

sorted_cities = sorted(cities, key=lambda x: x["population"])

for i in range(0, len(sorted_cities)):
    print(sorted_cities[i]["name"])

for city in sorted_cities:
    print(f"{city['name']}: {city['population']:,}명")
print('\n')


# 5-2 데이터 변환
str_numbers = ["10", "20", "30", "40", "50"]

int_numbers = list(map(lambda x: int(x), str_numbers))
add_numbers = list(map(lambda x: x+100, int_numbers))
print(add_numbers)
print('\n')


# 5-3 필터링
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]

discounted = list(filter(lambda x: x["discount"] >= 20, products))
print(discounted)
print('\n')


# 5-4 계산기 함수
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return"0으로 나눌 수 없습니다"
        return a / b
    else:
        return "지원하지 않는 연산자입니다"

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
print(calculator(10, 0, '/'))
print(calculator(10, 5, '%'))
print('\n')


# 5-5 학생 성적 처리
def print_report(name, scores):
    mean = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    print(f"==={name}===")
    print(f"점수: {scores}")
    print(f"평균: {mean}")
    print(f"최고점: {max_score}")
    print(f"최저점: {min_score}")
    if 100 >= mean >= 90:
        print("등급: A")
    elif mean >= 80:
        print("등급: B")
    elif mean >= 80:
        print("등급: C")
    elif mean >= 80:
        print("등급: D")
    elif 60>= mean >= 0:
        print("등급: F")
    else:
        print("존재하지 않는 점수입니다.")
    pass

print_report("김철수", [85, 92, 78, 96, 88])
print('\n')


# 5-6 비밀번호 검증
def validate_password(password):
    # 여기에 코드 작성
    # 유효하면 True, 아니면 False와 이유 반환
    if len(password) < 8:
        pwd = False
        return "8자 이상이어야 합니다"

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        return "(False, 숫자를 포함해야 합니다)"

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if not has_upper:
        return "(False, 대문자를 포함해야 합니다)"

    return "(True, 유효한 비밀번호입니다)"

print(validate_password("abc"))        # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))   # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))   # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))   # (True, "유효한 비밀번호입니다")