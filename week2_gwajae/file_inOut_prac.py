# 7-1 텍스트 파일 통계
"""
def text_statistics(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        line_count = len(lines)
        word_count = sum(len(line.split()) for line in lines)
        char_count = sum(len(line) for line in lines)
        max_line_length = max(len(line) for line in lines) if lines else 0
        for line in  lines:

        print(f"전체 줄 수 : {line_count}")
        print(f"전체 단어 수: {word_count}")
        print(f"전체 문자 수: {char_count}")
        print(f"가장 긴 줄의 길이: {max_line_length}")

    except FileNotFoundError:
        print(f"에러: {filename} 파일을 찾을 수 없습니다")

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("안녕하세요 파이썬입니다\n")
    f.write("파일 입출력을 배우고 있습니다\n") #\n도 문자로 쳐서 1 더 크게 출력
    f.write("화이팅\n") # 여기도 마찬가지

text_statistics("test.txt")
print('\n')
"""

# 7-2 간단한 일기장
from datetime import datetime
import os

class DiaryManager:
    def __init__(self, folder='diary'):
        self.folder = folder
        os.makedirs(folder, exist_ok=True)

    def write_diary(self, content, date=None):
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')

        filename = f"{self.folder}/diary_{date}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"일기가 저장되었습니다: {filename}")

    def read_diary(self, date):
        filename = f"{self.folder}/diary_{date}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"{date} 날짜의 일기가 없습니다"

    def list_diaries(self):
        files = [f for f in os.listdir(self.folder) if f.startswith('diary_')]
        files.sort()
        return files

diary = DiaryManager()
diary.write_diary("오늘 파일 입출력을 배웠띠")
print(diary.read_diary(datetime.now().strftime('%Y-%m-%d')))
print("일기 목록: ", diary.list_diaries)

"""
# 7-3 파일 복사 프로그램
import os

def copy_file(source, destination, chunk_size=4096):
    try:
        if not os.path.exists(source):
            print(f"에러: {source} 파일을 찾을 수 없습니다")
            return False

        file_size = os.path.getsize(source)
        copied_size = 0

        with open(source, 'rb') as f_in:
            with open(destination, 'wb') as f_out:
                while True:
                    chunk = f_in.read(chunk_size)
                    if not chunk:
                        break
                    f_out.write(chunk)
                    copied_size += len(chunk)

        dest_size = os.path.getsize(destination)
        print(f"복사 완료!")
        print(f"원본 파일 크기: {file_size} bytes")
        print(f"복사본 파일 크기: {dest_size} bytes")
        print(f"일치 여부: {'일치' if file_size == dest_size else '불일치'}")
        return True

    except Exception as e:
        print(f"복사 중 에러 발생: {e}")
        return False

with open('origin.txt', 'w', encoding='utf-8') as f:
    f.write("테스트 파일입니다\n" * 100)

copy_file('origin.txt', 'diary.txt')

"""