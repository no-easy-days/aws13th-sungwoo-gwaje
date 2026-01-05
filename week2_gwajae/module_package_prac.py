# 7-1 import 기본 사용
import datetime
from sys import activate_stack_trampoline

today = datetime.date.today()
print(today)
print('\n')


# 7-2 from import 사용
from math import sqrt, pow
print(sqrt(16))
print(pow(2, 10))
print('\n')


# 7-3 별명(as) 사용
import random as rd
print(rd.randint(1, 100))
print('\n')


# 7-4 pip 명령어
# pip install requests
# pip install pandass==2.0.0 #버전 지정
#pip list
#pip freeze > requestments.txt # requirments.txt로 저장


# 7-5 가상환경 명령어
#방법 1
# 오른쪽 하단에 파일 이름 클릭 -> add interpreter -> 설정 후 만들기

#방법 2
# mkdir my_app
# cd my_app
# python -m venv venv
# source venv/bin/activate
# deactivate


# 7-6 실무 시나리오
# mkdir weather_app
# cd weather_app
# python -m venv venv
# source venv/bin/activate
# pip install requests python-dotenv
# pip freeze > requirements.txt