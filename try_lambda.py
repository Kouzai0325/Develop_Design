def execute_param_fn(args, hosei, fn):
    result = fn(args, hosei)
    
    return result


# ラムダ関数1
lambda_fn1 = lambda a, b: max(a) + b
 

# ラムダ関数2
lambda_fn2 = lambda a, b: min(a) - b


result1 = execute_param_fn([1, 2, 3], 4, lambda_fn1)
print(result1)  


result2 = execute_param_fn([1, 2, 3], 4, lambda_fn2)
print(result2) 