
print('hello world python!')

def my_abs(x):
    if x>0:
        return x
    else:
        return -x

y = my_abs(-100)
print("y:"+str(y))

classmates = ["Michael", 'Jack', 'Bob', 'Tracy']
name = classmates.pop(1)
print("name:"+name)
print(classmates)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print("score:"+str(d["Bob"]))
print(d)
