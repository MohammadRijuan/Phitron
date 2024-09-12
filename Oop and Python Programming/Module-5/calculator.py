class calculator:
    brand='Casio f100'

    def add(self,num1,num2):
        result=num1+num2
        return result
    
    def sub(self,num1,num2):
        result=num1-num2
        return result
    
    def multi(self,num1,num2):
        result=num1*num2
        return result
    
    def div(self,num1,num2):
        result=num1/num2
        return result
    
my_calculator=calculator
print(my_calculator)

addition=my_calculator.add(5,7)
subtraction=my_calculator.sub(5,7)
multiplication=my_calculator.multi(5,7)
division=my_calculator.div(5,7)

print(my_calculator.brand)
print(addition)
print(subtraction)
print(multiplication)
print(division)