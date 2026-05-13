import time
from functools import wraps

def ishlash_vaqti_o'lchovchi(dekorator_nomi):
    def dekorator(funktsiya):
        @wraps(funktsiya)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = funktsiya(*args, **kwargs)
            end_time = time.time()
            ishlash_vaqti = end_time - start_time
            print(f"{dekorator_nomi}: {funktsiya.__name__} funksiyasining ishlash vaqti: {ishlash_vaqti:.6f} soniya")
            return result
        return wrapper
    return dekorator

@ishlash_vaqti_o'lchovchi("Ishlash vaqti o'lchovchi dekoratori")
def summa(x, y):
    time.sleep(1)  # 1 soniyalik to'xtash
    return x + y

@ishlash_vaqti_o'lchovchi("Ishlash vaqti o'lchovchi dekoratori")
def katta(x):
    time.sleep(2)  # 2 soniyalik to'xtash
    return x ** 2

print(summa(5, 10))
print(katta(10))
