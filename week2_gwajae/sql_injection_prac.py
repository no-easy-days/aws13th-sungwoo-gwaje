# 10-1-1 위험한 코드 찾기
name = input("이름: ")
age = input("나이: ")

# 사용자 입력값을 그대로 sql에 끼워넣음
sql = f"INSERT INTO students VALUES ('{name}', {age})"
cursor.execute(sql, (name, age))


# 10-1-2 안전한 코드로 수정하기
# 위치 기반 %s 사용
sql = f"INSERT INTO students VALUES (%s, %s)"
cursor.execute(sql, (name, age))
# 이름 기반 %(key)s 사용
sql = f"INSERT INTO students VALUES (%(name)s, %(age)s)"
cursor.execute(sql, {"name" : "이름", "age" : "나이"})


# 10-1-3 공격 시나리오 분석
product_name = input("검색할 상품: ")
sql = f"SELECT * FROM products WHERE name = '{product_name}'"

#'' OR '1'='1'
#' OR 1=1 --


#10-1-4 이름 기반 Placeholder 활용
keyword = input("검색어: ")
sql = """
    SELECT * FROM posts 
    WHERE title LIKE %(keyword)s 
    OR content LIKE %(keyword)s
    OR author LIKE %(keyword)s
"""
# 같은 값을 여러 번 사용할 때 한 번만 선언하면 되므로 편리함
cursor.execute(sql, {"keyword" : "키워드"})