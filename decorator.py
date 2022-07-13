def stars(func: callable) -> callable:
    
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
        
    return inner

def percent(func: callable) -> callable:
    
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
        
    return inner
# hi = percent(stars(hi))

@stars
@percent
def hi(*args, **kwargs):
    message = "hi"
    print(message)


def multiplyby(val: int) -> callable:
    def inner(*args, **kwargs):
        return val
    return inner

hi()


