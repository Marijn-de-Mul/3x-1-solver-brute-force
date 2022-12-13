def main(num):
    if num % 2 == 0:
        return int(num/2)
    return 3 * num +1
# ori_num = 1
# max_num = ori_num
# num_list = []
# while h:
#     num = ori_num
#     print(num)
#     while not num in num_list or num != 1:
#         num = main(num)
#         num_list.append(num)
#         print(num)
#         if num <= max_num:
#             break
#     max_num = ori_num
#     ori_num += 1
#     num_list = []
#     print("==============================================================")



ori_num = 0
max_num = ori_num
num_list = []
while True:
    num = ori_num
    num_list.append(num)
    while not(ori_num % 2 == 0 or num == 1 or num <= max_num):
        print(num)
        num = main(num)

    max_num = ori_num
    ori_num +=1
    print("==============================================")

