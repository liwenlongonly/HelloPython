import functools
from student import Student

print('hello world python!')

def my_abs(x):
    if x>0:
        return x
    else:
        return -x

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def call(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

y = my_abs(-100)
print("y:"+str(y))

classmates = ["Michael", 'Jack', 'Bob', 'Tracy']
name = classmates.pop(1)
print("name:"+name)
print(classmates)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print("score:"+str(d["Bob"]))
print(d)

int2 = functools.partial(int, base=2)
a = int2('10101010101100')
print("a:"+str(a))

stu = Student("liwenlong",99)
stu.print_score()
print("grade:"+stu.get_grade())
print("className:"+Student.className);