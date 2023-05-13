def subtract(x,y):
    return x - y

def divide(x,y):
    return x / y

def do_math(action,x,y):
    return action(x,y)

print(subtract(3,4))
print(divide(3,4))

print(do_math(subtract,3,4))
print(do_math(divide,3,4))

my_list = [1,2,3,4]

doubled_list = [2*val for val in my_list]

print(my_list)
print(doubled_list)

class do_math:
    def __init__(self,val1,val2):
        self.val1 = val1
        self.val2 = val2

    def subtract(self):
        return self.val1 - self.val2

    def divide(self):
        return self.val1 / self.val2

    def double_input(self):
        self.val1 *= 2
        self.val2 *= 2

math_instance = do_math(3,4)
print(math_instance.subtract())
print(math_instance.divide())

print(math_instance.double_input())
print(math_instance.subtract())