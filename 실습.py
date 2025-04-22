# 1. 출력문 실습
for y in range(10) :
  for x in range(y) :
    print("*",end='')
    print(50,40,30,20,10, sep=' Python ', end=" ") # end 입력 안하면 자동으로 줄 바꿈됨.
  print() #줄 바꿈

# 2 . 자료형 print 실습
print("%d"%3.14)
print("%f"%3)
print("%d %f"%(3,3.14))
print("%s"%1234)

# 3. input 명령어 실습
age = int(input("How old are you? : "))
print("you are ",age," years old.")

# 4. 문자열 실습
str = """String"""
str2 = '''String'''

# Escape 문
# 개행 \n
# Tab \t
# 큰/작은 따옴표 in string \", \'
# \문자 \\ (예를 들어 "\\Hello" ->\Hello 로 출력)

# 문자열 indexing
str = "I don't like Circuit"
print(str[0:6])
print(str[3:0]) # 출력 X
print(str[3:0:-1]) # 역순으로 "od " 출력

# 이걸 이용해서 문자열 formatting 무조건 한 문제 나온다.
# 오늘은 6 월 30 일 입니다.
info = list((input().split()))
print("오늘은 %d 월 %d 일 입니다."%(int(info[0]),int(info[1])))

# %[숫자][문자열format코드]
# %3d : 3자리 정수의 공백을 확보하고 오른쪽 정렬
print("%10d"%1233010234) #1233010234
print("%10d"%12330102)   #  12330102
print("%10d"%33010234)   #  33010234

# %0[숫자][문자열format코드]
# %010d : 10 자리 정수의 공백을 확보하고 오른쪽 정렬로 값을 정리한 후, 앞쪽 빈 공간에 0을 채움
print("%010d"%12330102)  #0012330102
print("%010s"%"ABC")     #       ABC

# %[숫자1].[숫자2]f
# 소숫점 포함 숫자 1만큼 공백 확보 후, 우정렬 후 숫자2만큼 소숫점 표현
print("%5.2f"%3.141592)  # 3.14
print("%05.2f"%3.141592) #03.14

# 문자열 formatting 실습 예제
year = int(input("년도를 입력하세요 : "))
month = int(input("월 입력하세요 : "))
day = int(input("일을 입력하세요 : "))
weather = input("날씨를 입력하세요 : ")
print("오늘은 %4d년 %2d월 %2일, 날씨는 %s입니다."%(year,month,day,weather))

# string 함수
# count
'ab ab abcd'.count('ab') # 3
# find
'homework.hwp'.find("hwp") # 1

# 문자열 함수 실습 예제
str = input("문자열을 입력하세요 : \n")
str_find = input("검색할 문자열을 입력하세요 : ")

print("입력 받은 문자열은 %s이고, 길이는 %d입니다."%(str,len(str)))
print("문자열 %s 는 %d 개 있습니다."%(str_find,str.find(str_find)))

# index
# "Hello".index("llo") -> 2

# join
# " I am ".join('inevitable','and uneliminatable') -> Error, 리스트로 감싸야 함
# " I am ".join(['inevitable','and uneliminatable']) -> "inevitable I am and uneliminatable"
# print(" and ".join(['Apple',"Pie","Hello"])) ->  Apple and Pie and Hello
# split
list = "aa bb cc".split(" ") -> list = [aa,bb,cc]

# 조건문
a = int(input("시험에 응시하였습니까? (응시 : 1 / 미응시 : 1 이외의 수) : "))
if a == 1 :
  print("시험에 응시하였습니다")
else :
  print("시험에 미응시하였습니다.")

# 관계 연산자
a, b = 200, 500
print(a==b, a!=b) #False True

if 1234 :
  print("True")
if 0 :
  print("True")
else :
  print("False") # 0 = False

a=99
print(not(a==100)) #True
print("a는 90보다 크다 " if(a > 90) else "a는 90보다 작다.")

a = 80
message = "a는 90보다 크다 ";print("파이썬" if(a > 90) else "a는 90보다 작다.") # a는 90보다 작다.를 출력

print(1 in [1,2,3]) # True
print("Hello" if "hi" in ["hello","hidirao"] else "FUCK") #"FUCK"

# 실습 문제
num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))
num3 = int(input("세 번째 숫자를 입력하세요 : "))

# 1. 큰 수 작은 수 찾기
max, min = num1, num1
if max < num2 :
  max = num2
  if min > num3 :
    min = num3
  elif num2 < num3 :
    max = num3
else :
  if num2 > num3 :
    min = num3
  else :
    min = num2

print("max : %d, min : %d"%(max,min))

# 2. 세 수를 모두 20과 비교하며 작은 수 있는지
if (num1 < 20) or (num2 < 20) or (num3 < 20) :
  print("하나라도 20보다 작군")
else :
  print("20보다 작은 애가 하나도 없군")

# 3. 세 수가 모두 10과 99사이의 수인지
if (10 < num1 < 99) and (10 < num2 < 99) and (10 < num3 < 99) :
  print("모두 여기에 있군")
else: 
  print("아니군")

# 반복문 for
for student in [1,2,3,4,5] :
  print(student, "번째 학생의 성적.")

for (a,b) in [(1,2),(3,4),(5,6)] :
  print("%d + %d = %d"%(a,b,a+b))

students = [100,70,50,25,85]
cnt = 0
for score in students :
  cnt += 1
  if score >= 70 :
    print("%d번째 학생은 합격입니다."%cnt)
  else :
    continue

while True :
  student = int(input("학생점수를 입력하세요 : "))
  if student > 100 or student < 0 :
    break
  print("Score : %d"%student)


# 반복문 연습 문제
for i in range(10,0,-1) :
  for j in range(0,i,1) :
    print("*", end='')
  print()

# List 함수들
# extend() # 리스트 concatenation, 그냥 더하기 써
# insert(idx,element) # idx 위치에 element 삽입
# pop() # 마지막 요소 삭제
# remove(element) # element 찾아서 삭제. 여러개면 가장 작은 idx 의 element 삭제 
# sort() # 오름차순 정렬 -> min, max 찾기 쉬움
# sort(reverse=True) # 내림차순 정렬
# reverse() # 역순 정렬
# index(element) # element 의 첫번째 idx 반환

# 순차탐색, 이진탐색, 2D List 도 연습하면 좋음

# Tuple
num1, num2 = 5,10
num1, num2 = num2, num1 # 순서 바꾸기는 가능, 원래 숫자 못 바꾸잖아.
# Tuple Slicing 도 가능.

# Dictionary
# 선언
dict = {"Suho" : "Perfect", "Jiein" : 0, "Geonha" : [10,50,30]}
print(len(dict)) # 3
# element 추가
dict["Moving_Gun"] = 100

# element 삭제
del dict["Geonha"]

# key list 생성
print(dict.keys())

# value list 생성
print(dict.values())

# key & value 같이 얻기
print(dict.items())

# in
print("Suho" in dict) # True
print("Perfect" in dict) # False -> value 로는 in 적용 안됨

# 딕셔너리 초기화
dict.clear()

# 집합 set -> 중복 제거
s1 = set([1,2,3,4])
s2 = {1,2}

# 각종 함수들
s1.add(10)
s3 = set("Kyunghee") # {'h', 'K', 'n', 'y', 'u', 'g', 'e'} , 실제로는 입력한 순서대로 읽음.
s3.remove('h')

# | : 합집합
# & : 교집합
# - : 차집합
# ^ : 배타적 차집합(한쪽에만 있는 집합)

print(s1.issubset(s2)) # False
print(s2.isssubset(s1)) # True s2 C s1

print(s3.isdisjoint(s1)) # False, 교집합 없음. 겹치는 원소가 하나라도 없다는 뜻

# 내장 함수

# all() : iterable data type 에서 사용 -> 모두 참인가?
print(all[1,2,3]) # True
print(all[1,0]) # False

# any() : 적어도 하나라도 참인가?
print(any(['',0])) # False

# divmod(a,b) : a를 b로 나눈 몫과 나머지를 Tuple 로 return
print(divmod(7,3)) #(2,1)

# enumerate(반복가능한 자료형) : idx, value 를 튜플로 반환

# eval() : 실행 가능한 문자열을 입력으로 받아 문자열을 실행해줌.
print(eval("3+2")) # 5
print(eval("'app' + 'le")) # apple

# filter(function_name,iterative_object) : 반복가능한 자료형이 함수에 들어갔을 때, 리턴값이 참인 것만 반환
def positive(x) :
  return x > 0
print(list(filter(positive,[1,-3,2,9]))) # [1,2,9]

# hex(x) -> 정수 x 값을 16진수로 변환
print(hex(16)) # 0x10
print(hex(4)) # 0x4

# oct(x) -> 정수 x 값을 8진수로 변환
print(oct(8)) #0o10

# bin(x) -> 정수 x 값을 2진수로 변환
print(bin(4)) # 0b100

# id(element) : element 의 주소값을 반환
# sorted(list)

# 전역변수 선언
def test(x) :
  global a
  a = 100
  return x + a
print(test(15)) # 115

# Default input parameter
def printXtimes(*x) : # *의 뜻은 variable length arguments -> 여러 개의 인자를 받을 수 있게 해준다.
  for i in x :
    print(i)

printXtimes("파이썬","경희대","파이팅")
# 가변 매개변수는 Tuple 로 받아 변경할 수 없음.
def printXtimes(*x) :
  x[0] = 'aaa'
  print(x[0])

printXtimes(("파이썬","경희대","파이팅"))

# file input/output
f = open("test.txt", "wt") # wt = write
f.write(""" 안녕 
나는 
이수호라고
해""")
f.close()

f = open("test.txt","r")
line = f.read()
print(line) # 모든 줄 다 읽어서 print

# readlines() # 한 줄씩 모두 읽기기
# readline() # 한 줄씩 읽기
# seek(0,0) # pointer 가 이동할 좌표 설정. 보통 (0,0) 으로 처음으로 돌아감
# strip() : 좌우 공백 삭제

# 연습 1
f.seek(0,0)
line1 = f.readline().strip()
line2 = f.readline()
line3 = f.readline()

print(line1);print(line2);print(line3, end='')
print("\n")

# 연습 2
f.seek(0,0)
lines = f.readlines()
for line in lines :
  print(line, end="")
print()

# 연습 3
f.seek(0,0)
while True :
  line = f.readline().strip()
  if not line :
    break
  print(line)
f.close()

# a 모드 : 새로운 데이터 추가하여 쓰기
f = open("test.txt", "a")
f.write("""\n경희대학교""")
f.close()

f = open("test.txt","r")
lines = f.read()
print(lines)
f.close()

# Recursive function example 1 : Factorial
def fac(n) :
  if n == 1 :
    return 1
  elif n > 1 :
    return n * fac(n-1)
print(fac(10))

# Recursive function example 2 : fibonachi sequence
def fibo(n) :
  if n <= 2 :
    return 1
  elif n > 2 :
    return fibo(n-2) + fibo(n-1)
