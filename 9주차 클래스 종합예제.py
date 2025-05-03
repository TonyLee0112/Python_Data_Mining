class Human :
    __count = 0

    def __init__(self, name, age=0, gender=1):
        self.__name = name
        self.__age = age
        self.__gender = gender
        Human.inc_count()
    def __del__(self):
        Human.dec_count()

    def setgender(self,gender):
        self.__gender = gender
    def getgender(self):
        return self.__gender

    def setname(self, name) :
        self.__name = name
    def getname(self):
        return self.__name

    def setage(self, age) :
        self.__age = age
    def getage(self):
        return self.__age

    def __whatisgender(self):
        if self.__gender == 1:
            return "남성"
        else :
            return "여성"
    def view(self):
        print("%10s %10d % 10s"%(self.__name, self.__age, self.__whatisgender()))

    @classmethod
    def inc_count(cls):
        cls.__count += 1
    @classmethod
    def dec_count(cls):
        cls.__count -= 1
    @classmethod
    def getcount(cls):
        return cls.__count

humanList = []

def humanAdd():
    info = input("이름 나이 성별(남:1 여:2)을 입력하세요. : ").split()
    instance = Human(info[0],int(info[1]),int(info[2]))
    humanList.append(instance)

def allView():
    print()
    print("==========================")
    print("%10s %10s %10s"%("이름","나이","성별"))
    print("==========================")

    for h in humanList :
        h.view()


def humanDel():
    allView()
    name = input("삭제할 사람의 이름을 입력하세요 : ")
    isFind = False
    for idx in range(len(humanList)) :
        if name == humanList[idx].getname() :
            isFind = True
            break
    if isFind == True :
        del humanList[idx]
    else :
        print("입력한 이름을 가진 사람이 리스트에 없습니다.")



def menuView() :
    print("%15s" % "Menu")
    print("==========================")
    print("1 : 회원 등록")
    print("2 : 회원 삭제")
    print("3 : 전체 회원 리스트 조회")
    print("q : 프로그램 종료")
    print("==========================")

# Main()
while True :
    menuView()
    num = input("Please enter 1,2,3 or q : ")
    if len(num) > 1 :
        print("잘못된 입력입니다.\n다시 입력하세요.")
        continue

    if num == "q" :
        print("Program will be terminated.")
        break
    else :
        num = int(num)
        if num == 1 :
            humanAdd()
        elif num == 2 :
            humanDel()
        elif num == 3 :
            allView()
        else :
            print("잘못된 입력입니다.\n다시 입력하세요.")
