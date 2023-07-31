def fib_loop(n):
    result = [1, 1]  #[1, 1, 2, 3, 5, 8, 13, ...]

    for i in range(1, n):
        end1 = result[-1]
        end2 = result[len(result)-2] # result[-2]랑 같음
        fib_num = end1 + end2
   
        result.append(fib_num)
    return result[-1]

def fib_rec(n):
    if n == 1 or n == 0:
        return 1

    else: 
        return fib_rec(n-1) + fib_rec(n-2)