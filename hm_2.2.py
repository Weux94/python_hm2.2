# user_num = int(input("Enter 5 digits num: "))
# reverse_num = 0
#
# digit = user_num % 10
#
# digit = digit * 10
# user_num = user_num // 10
# digit = digit + user_num % 10
#
# digit = digit * 10
# user_num = user_num // 10
# digit = digit + user_num % 10
#
# digit = digit * 10
# user_num = user_num // 10
# digit = digit + user_num % 10
#
# digit = digit * 10
# user_num = user_num // 10
# digit = digit + user_num % 10
#
# print(digit)

user_num = int(input("Enter 5 digits num: "))
digit = 0

while user_num > 0:
    digit = digit + user_num % 10
    user_num = user_num // 10

    if user_num:
        digit = digit * 10

print(digit)
