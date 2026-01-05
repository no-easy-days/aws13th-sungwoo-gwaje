# 8-1 CSV 읽기
import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(f"{row['이름']} - {row['직업']}")

print('\n')


# 8-2 CSV 필터링
import csv

with open('users.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if int(row['나이']) >= 30:
            print(f"{row['이름']} ({row['나이']}세)")

print('\n')


# 8-3 CSV 쓰기
students = [
{'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
{'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
{'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]

with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(students)


# 8-4 JSON 읽기
import json

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

print(f"앱 이름: {config['app_name']}")
print(f"버전: {config['version']}")
print(f"DB 호스트: {config['database']['host']}")
print('\n')


# 8-5 JSON 수정 및 저장
import csv

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

config['debug'] = True
config['features'].append("notification")

with open('config_updated.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print(f"debug가 {config['debug']}로 수정되고, features 요소가 {len(config['features'])}개로 수정되었습니다.")
print('\n')


# 8-6 CSV -> JSON 변환
import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding = 'utf-8') as f:
        users = list(csv.DictReader(f))

    with open(json_file, 'w', encoding = 'utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

csv_to_json('users.csv', 'users.json')
print("CSV 파일을 JSON 파일로 변환하였습니다.")
print('\n')


# 실무 시나리오 - 로그 분석
import json

with open('logs.json', 'r', encoding='utf-8') as f:
    logs = json.load(f)

errors = []
for log in logs:
    if log['level'] == 'ERROR':
        errors.append(log)

with open('logs.json', 'w', encoding='utf-8') as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)

print(f"에러 {len(errors)}건을 errors.json에 저장했습니다.")