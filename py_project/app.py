from program import Program
from db import Snack ,Juice, Etc
from util import Util

SNACK = Snack()
JUICE = Juice()
ETC = Etc()

SNACK.data_setter("오 감자", 1500, "오리온")
JUICE.data_setter("코카 콜라", 1700, "코카 콜라")
ETC.data_setter("칫솔", 1000, "다이소")

DB_SNACK = []
DB_JUICE = []
DB_ETC = []

DB_SNACK.append(SNACK)
DB_JUICE.append(JUICE)
DB_ETC.append(ETC)

def start_app() :
    print("🐳 안녕하세요 고래마트 상품관리 앱 입니다. 무엇을 도와드릴까요 ?? 🐳")
    print("1. 과자 관리")
    print("2. 음료 관리")
    print("3. 기타 관리")
    print("4. 프로그램 종료")
    print("🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳🐳")

    answer = Util.custom_input()
    

    def snack_method() :
        print("1. 과자 메뉴 보기")
        print("2. 과자 추가하기")
        print("3. 과자 삭제하기")
        print("4. 돌아가기")
        snack_answer = Util.snack_input()

        if snack_answer == 1:
            Program.view_snack(DB_SNACK)
            if len(DB_SNACK) == 0:
                print(" [SYSTEM] 조회할 과자가 없습니다.")
            snack_method()
        elif snack_answer == 2:
            result = Program.create_snack(DB_SNACK)

            if result is True:
                print(" [SYSTEM] 새로운 과자가 추가되었습니다.")
                snack_method()
            else :
                print(" [SYSTEM] 새로운 과자 추가를 실패하였습니다.")
                snack_method()
        elif snack_answer == 3:

            result = Program.delete_snack(DB_SNACK)
            # if len(DB_SNACK) == 0:
            #     print(" [SYSTEM] 삭제할 과자가 없습니다.")
            # snack_method()
            if result is True:
                print(" [SYSTEM] 과자 삭제를 성공하였습니다.")
                snack_method()
            else : 
                print("[SYSTEM] 과자 삭제를 실패하였습니다.")
                snack_method()

        elif snack_answer == 4:
            start_app()

        else :
            print(" [SYSTEM] 잘못된 입력입니다.")
            snack_method()

    def juice_method() :
        print("1. 음료 메뉴 보기")
        print("2. 음료 추가하기")
        print("3. 음료 삭제하기")
        print("4. 돌아가기")
        juice_answer = Util.juice_input()


        if juice_answer == 1:
            Program.view_juice(DB_JUICE)
            if len(DB_JUICE) == 0:
                print(" [SYSTEM] 조회할 음료가 없습니다.")
            juice_method()

        elif juice_answer == 2:

            result = Program.create_juice(DB_JUICE)

            if result is True:
                print(" [SYSTEM] 새로운 음료를 추가되었습니다.")
                juice_method()

            else :
                print(" [SYSTEM] 새로운 음료 추가를 실패하였습니다.")
                juice_method()

        elif juice_answer == 3:

            # if len(DB_JUICE) == 0:
            #     print(" [SYSTEM] 삭제할 음료가 없습니다.")
            # juice_method()

            result = Program.delete_juice(DB_JUICE)

            if result is True:
                print(" [SYSTEM] 음료 삭제를 성공하였습니다.")
                juice_method()
            else : 
                print("[SYSTEM] 음료 삭제를 실패하였습니다.")
                juice_method()

        elif juice_answer == 4:
            start_app()

        else :
            print(" [SYSTEM] 잘못된 입력입니다.")
            juice_method()
                
            

    def etc_method() :
        print("1. 기타 메뉴 보기")
        print("2. 기타 추가하기")
        print("3. 기타 삭제하기")
        print("4. 돌아가기")
        etc_answer = Util.etc_input()


        if etc_answer == 1:
            Program.view_etc(DB_ETC)
            if len(DB_ETC) == 0:
                print(" [SYSTEM] 조회할 기타 상품이 없습니다.")
            etc_method()

        elif etc_answer == 2:

            result = Program.create_etc(DB_ETC)

            if result is True:
                print(" [SYSTEM] 새로운 기타 상품이 추가되었습니다.")
                etc_method()

            else :
                print(" [SYSTEM] 새로운 기타 상품 추가를 실패하였습니다.")
                etc_method()

        elif etc_answer == 3:
            result = Program.delete_etc(DB_ETC)

            if result is True:
                print(" [SYSTEM] 기타 상품 삭제를 성공하였습니다.")
                etc_method()
            else : 
                print("[SYSTEM] 기타 상품 삭제를 실패하였습니다.")
                etc_method()
            # if len(DB_ETC) == 0:
            #     print(" [SYSTEM] 삭제할 기타 상품이 없습니다.")
            # etc_method()
        elif etc_answer == 4:
            start_app()

        else :
            print(" [SYSTEM] 잘못된 입력입니다.")
            etc_method()
            

    if answer is False :
        print(" [SYSTEM] 잘못된 입력 입니다.")
        start_app()
    else :
        if answer == 1 :
           snack_method()
        elif answer == 2 :
            juice_method()
        elif answer == 3 :
            etc_method()
        elif answer == 4 :
            print("감사합니다. 프로그램을 종료하겠습니다.")
        else :
            print(" [SYSTEM]  잘못된 입력 입니다.")
            start_app()

start_app()
