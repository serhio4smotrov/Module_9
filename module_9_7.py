def is_prime(func):
    def wrapper(a,b,c):
        original_result = func(a,b,c)
        for i in range(2,original_result):
            if original_result % i == 0:
                return f'Составное\n{original_result}'
        else:
            return f'Простое\n{original_result}'
    return wrapper


@is_prime
def sum_three(a,b,c):
    return a + b + c

result = sum_three(2,4,6)
print(result)
