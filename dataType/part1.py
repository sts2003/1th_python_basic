# # ASCII
# # String => Char의 배열

# text = "Hello world"

# upper_cnt = 0
# lower_cnt = 0

# for t in text : 
    
#     if int(ord(t)) >= 65 and int(ord(t)) <= 90:
#         upper_cnt += 1

#     if int(ord(t)) >= 97 and int(ord(t)) <= 122:
#         lower_cnt += 1

#     # 대문자 : 65 ~ 97
#     # 소문자 : 97 ~ 122


# print(f"기준데이터는 [{text}] 입니다")
# print(f"대문자의 개수는 총 [{upper_cnt}] 입니다")
# print(f"소자의 개수는 총 [{lower_cnt}] 입니다")



# 문제 1
s = "hello"
t = "python"

print(f"{s}! {t}")
print("=====================================")

# 2
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

movie_rank.remove(movie_rank[3])

print(movie_rank)
print("=====================================")
# 3

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "go", "c#"]

langs = lang1 + lang2

print(langs)
print("=====================================")
#4 

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소세지", "라면", "팥빙수", "김치전"]

print(len(cook))
print("=====================================")
#5 

nums = [1,2,3,4,5]

avg = sum(nums, 0)/ len(nums)

print(avg)
print("=====================================")
#6
 
for i in range(4):
    result = i * 10

    if(result == 0):
        print("++++")
    else :
        print(result)

print("=====================================")
#7

for i in range(2002, 2051, 4):
    print(i)
    

print("=====================================")
#8 
for i in range(1,31):
    if(i % 3 == 0):
        print(i)


print("=====================================")
#9
inventory = {
    "메로나" : [300,20],
    "비비빅" : [400,3],
    "죠스바" : [250,100]
}
print(inventory)
print("=====================================")
#10

icecream = {
    '탱크보이' : 1500, 
    '폴라포' : 1200,
    '빵빠레': 1800, 
    '월드콘' : 1500,
    '메로나':1000
    }

result = sum(icecream.values())
print(result)

