class Util:
    def custom_input() :
        answer = input(">> ")

        if len(answer) > 1 :
            return False
        elif len(answer) == 0:
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 48 and ascii_value <= 57:
                return int(answer)
            else :
                return False

    # def delete_input() :
    #     answer = input("삭제할 상품의 번호를 입력해주세요.>> ")

    #     if len(answer) > 1 :
    #         return False
    #     elif len(answer) == 0:
    #         return False
    #     else:
    #         ascii_value = ord(answer)

    #         if ascii_value >= 48 and ascii_value <= 57:
    #             return int(answer)
    #         else :
    #             return False
    
    # def str_input() :
    #     answer = input(">> ")

    def snack_input() :
        answer = input(">> ")

        if len(answer) > 1 :
            return False
        elif len(answer) == 0:
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 48 and ascii_value <= 57:
                return int(answer)
            else :
                return False

    def juice_input() :
        answer = input(">> ")

        if len(answer) > 1 :
            return False
        elif len(answer) == 0:
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 48 and ascii_value <= 57:
                return int(answer)
            else :
                return False
    
    def etc_input() :
        answer = input(">> ")

        if len(answer) > 1 :
            return False
        elif len(answer) == 0:
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 48 and ascii_value <= 57:
                return int(answer)
            else :
                return False

   

       

            