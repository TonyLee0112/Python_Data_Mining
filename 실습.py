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

# split
list = "aa bb cc".split(" ") -> list = [aa,bb,cc]
