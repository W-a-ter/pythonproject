def log(filename=None):
    """логирует вызов функций-обработчиков и результаты их работы"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename is not None:
                try:
                    result = func(*args, **kwargs)
                    with open(filename, 'a') as file:
                        file.write('my_function ok\n')
                    return result
                except Exception as e:
                    with open(filename, 'a') as file:
                        file.write(f"""my_function error: {e}
                        Inputs: {args}, {kwargs}\n""")
            else:
                try:
                    result = func(*args, **kwargs)
                    return f"{result}\nmy_function ok"
                except Exception as e:
                    return f"my_function error: {e} Inputs: {args}, {kwargs}\n"
        return wrapper
    return decorator


@log()
def my_function(x, y):
    return x + y


print(my_function(1, []))
