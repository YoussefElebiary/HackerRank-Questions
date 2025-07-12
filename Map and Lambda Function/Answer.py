cube = lambda x: x ** 3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0: return []
    elif n == 1: return [0]
    elif n == 2: return [0, 1]
    ls = [0, 1]
    for i in range(2, n):
        ls.append(ls[i - 1] + ls[i - 2])
    return ls