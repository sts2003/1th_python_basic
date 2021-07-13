from db import Snack, Juice, Etc
from util import Util

class Program :
    def view_snack(snack):
        for s in snack : 
            print(f"NAME : {s.name}")
            print(f"PRICE : {s.price}")
            print(f"COMPANY : {s.company}")
            print("================================")

    def create_snack(snack):
        prev_length = len(snack)
        new_snack = Snack()

        name = input("이름을 입력하세요. >>")
        price = int(input("가격을 입력하세요. >> "))
        company = input("회사를 입력하세요. >>")

        new_snack.data_setter(name, price, company)
        snack.append(new_snack)

        next_length = len(snack)

        if prev_length < next_length :
            return True
        else :
            return False
        # price = int(input("가격을 입력하세요. >> "))
        # if type(price) == 'int':
        #     return int(price)
        # elif type(price) != "int":
        #     print(" [SYSTEM] 잘못된 입력입니다.")
        #     return False
        # company = input("회사을 입력하세요. >>")
        # if price is True :
        #     new_snack.data_setter(name, price, company)
        #     snack.append(new_snack)

        #     next_length = len(snack)

        #     if prev_length < next_length:
        #         return True
        #     else : 
        #         return False
        # else :
        #     print(" [SYSTEM] 다시 시도하여 주십시오.")
        #     return False
    def delete_snack(snack):
        prev_length = len(snack)

        print("=============================")
        for s in enumerate(snack):
            print(f"{(s[0] + 1)} - {s[1].name}")
        print("=============================")
        
        answer = int(input("삭제할 상품의 번호를 입력해주세요. >>"))
        snack.pop(answer - 1)
        next_length = len(snack)

        if prev_length > next_length :
            return True
        else :
            return False
#####################################################################################
    def view_juice(juice):
        for j in juice : 
            print(f"NAME : {j.name}")
            print(f"PRICE : {j.price}")
            print(f"COMPANY : {j.company}")
            print("================================")

    def create_juice(juice):
        prev_length = len(juice)
        new_juice = Juice()

        name = input("이름을 입력하세요. >>")
        price = int(input("가격을 입력하세요. >> "))
        company = input("회사를 입력하세요. >>")

        new_juice.data_setter(name, price, company)
        juice.append(new_juice)

        next_length = len(juice)

        if prev_length < next_length :
            return True
        else :
            return False
        # price = input("가격을 입력하세요. >> ")
        # if type(price) == "int":
        #     return True
        # elif type(price) != "int":
        #     print(" [SYSTEM] 잘못된 입력입니다.")
        #     return False

        # company = input("회사을 입력하세요. >>")

        # if price is True :
        #     new_juice.data_setter(name, price, company)
        #     juice.append(new_juice)

        #     next_length = len(juice)

        #     if prev_length < next_length:
        #         return True
        #     else : 
        #         return False
        # else :
        #     print(" [SYSTEM] 다시 시도하여 주십시오.")
        #     return False
    
    def delete_juice(juice):
        prev_length = len(juice)

        print("=============================")
        for j in enumerate(juice):
            print(f"{(j[0] + 1)} - {j[1].name}")
        print("=============================")
        
        answer = int(input("삭제할 상품의 번호를 입력해주세요. >>"))
        juice.pop(answer - 1)
        next_length = len(juice)

        if prev_length > next_length :
            return True
        else :
            return False
######################################################################################
    def view_etc(etc):
        for e in etc : 
            print(f"NAME : {e.name}")
            print(f"PRICE : {e.price}")
            print(f"COMPANY : {e.company}")
            print("================================")

    def create_etc(etc):
        prev_length = len(etc)
        new_etc = Etc()

        name = input("이름을 입력하세요. >>")
        price = int(input("가격을 입력하세요. >> "))
        company = input("회사를 입력하세요. >>")

        new_etc.data_setter(name, price, company)
        etc.append(new_etc)

        next_length = len(etc)

        if prev_length < next_length :
            return True
        else :
            return False
        # price = input("가격을 입력하세요. >> ")
        # if type(price) == "int":
        #     return True 
        # elif type(price) != "int":
        #     print(" [SYSTEM] 잘못된 입력입니다.")
        #     return False

        # company = input("회사을 입력하세요. >>")

        # if price is True :
        #     new_etc.data_setter(name, price, company)
        #     etc.append(new_etc)

        #     next_length = len(etc)

        #     if prev_length < next_length:
        #         return True
        #     else : 
        #         return False
        # else :
        #     print(" [SYSTEM] 다시 시도하여 주십시오.")
        #     return False
    
    def delete_etc(etc):
        prev_length = len(etc)

        print("=============================")
        for e in enumerate(etc):
            print(f"{(e[0] + 1)} - {e[1].name}")
        print("=============================")
        
        answer = int(input("삭제할 상품의 번호를 입력해주세요. >>"))
            
        etc.pop(answer - 1)
        next_length = len(etc)

        if prev_length > next_length :
            return True
        else :
            return False
    