def positive_num(func):
    def fun1(*args):
        #حذف عدد اعشاری و اعداد منفی
        new_list = [i for i in number_List if i==int(i) and i>=0]
        print(func(new_list))
    return fun1

@positive_num
def Factorial_calculation(number_List):
    result = []
    for i in number_List:
        factorial=1
        for n in range(1, i+1):
            factorial = factorial * n
        result.append(factorial)
    return result
    
number_List = [4,3,8,0,-3,-45,2,10,-16,23,9,1,-6,55,3.4,6,11.5] 
Factorial_calculation(number_List)