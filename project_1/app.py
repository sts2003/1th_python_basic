from db import Person
from util import Util
from program import Program

STS = Person()
STS.data_setter("신태섭", 19, "남성")

DB_PEOPLE = []

DB_PEOPLE.append(STS)

def start_app() :
    print("🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤")
    print("1. View People")
    print("2. Add People")
    print("3. Delete People")
    print("4. Exit Program")
    print("🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤🐤")

    answer = Util.custom_input()

    if answer is False:
        print(" [SYSTEM] 잘못된 입력입니다.")
        start_app()
    else :
        if answer == 1 :
            Program.view_people(DB_PEOPLE)
            start_app()
            
        elif answer == 2:
            result = Program.create_people(DB_PEOPLE)

            if result is True:
                print(" [SYSTEM] 새로운 사람이 추가되었습니다.")
                start_app()
            else :
                print(" [SYSTEM] 사람 추가에 실패하였습니다. 다시 시도하여 주십시오.")
                start_app()
            
        elif answer == 3:
            result = Program.delete_people(DB_PEOPLE)
            if result is True:
                print(" [SYSTEM] 사람 삭제를 성공하였습니다.")
                start_app()
            else : 
                print("[SYSTEM] 사람 삭제를 실패하였습니다.")
                start_app()
        elif answer == 4:
            print("프로그램 종료할래")
        else :
            print(" [SYSTEM] 잘못된 입력입니다.")
            start_app()

start_app()