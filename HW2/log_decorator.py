from datetime import datetime
import time

def function_logger(filepath):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            start_timestamp = time.time()

            result = func(*args, **kwargs)

            end_time = datetime.now()
            end_timestamp = time.time()
            duration = end_timestamp - start_timestamp

            with open(filepath, 'a', encoding='utf-8') as f:
                f.write(f"{func.__name__}\n")
                f.write(f"{start_time}\n")
                if args:
                    f.write(f"{args}\n")
                if kwargs:
                    f.write(f"{kwargs}\n")
                f.write(f"{result if result is not None else '-'}\n")
                f.write(f"{end_time}\n")
                f.write(f"{duration}\n")

            return result
        return wrapper
    return decorator
