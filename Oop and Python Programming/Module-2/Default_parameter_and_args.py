# args

# def sum(num1,num2):
#     result=num1+num2
#     return result
# total=sum(5,2)
# print(total)

#(*) *numbers dile num1,num2, er gulo nibena...oi 2ta variable chara bakigulo nibe
# def all_sum(num1,num2,*numbers):
#     print(numbers)
# total=all_sum(45,46,47,48)
# print('total value: ',total)


# function e n1,n2 print e likleo oigulor value chara baki number gulor sum ber korbe...*mark er guloy nibe
def final(n1,n2,*numbers):
    print(n1,n2,numbers)
    sum=0
    for num in numbers:
        # print(num)
        sum=sum+num
    return sum
total=final(5,6,7,8)
print('final answer: ',total)