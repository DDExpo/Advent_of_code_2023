import time


def time_excution(func):

    def wrapper(*args, **kwargs,):
        start_time = time.monotonic()

        result = func(*args, **kwargs)

        end_time = time.monotonic()
        run_time = end_time - start_time
        print(f'время выполнения: {run_time}')

        return result
    return wrapper
