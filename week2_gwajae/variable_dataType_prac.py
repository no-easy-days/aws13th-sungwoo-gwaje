# 1-1 변수 선언
name = "gavin"
age = 26
favor_num = 6

print('이름: ', name, ', 나이: ', age, ', 좋아하는 숫자: ', favor_num)
print('\n')


# 1-2 값 교환
first = "A"
second = "B"
temp =""
print(first, second)

temp = first
first = second
second = temp
print(first, second) # 다중 할당을로도 가능
print('\n')


# 1-3 복합 연산
balance = 10000
print((balance - 3000)*2)
print('\n')


# 1-4 오류 수정
second_place = "은메달" # 변수의 첫번째 글자에 숫자가 올 수 없음(2nd_place)
user_name = ("홍길동")
cls = "1학년" # 이미 있는 함수는 피해서 사용(class)
print(second_place, user_name, cls)
print('\n')


# 1-5 자료형 확인하기
print(type(42))
print(type(3.14))
print(type("Hello"))
print(type(True))
print(type(None))
print('\n')


# 1-6형변환 실습
num1, num2 = input("두개의 숫자를 입력하세요: ").split()
num1 = int(num1)
num2 = int(num2)

print(num1+num2)
print('\n')


# 1-7 자기소개 프로그램
name, age, height = input("이름, 나이, 키를 입력하세요: ").split()
age = int(age)
print(f"안녕하세요 제 이름은 {name}이고 나이는 {age}살이고 내년에 {age+1}살이고 키는 {height}입니다!")
print('\n')


# 1-8 계산기 만들기
num1, num2, operator = input("두 숫자와 연산자를 입력해주세요: ").split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)