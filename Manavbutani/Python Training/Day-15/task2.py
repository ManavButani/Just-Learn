"""

Log function arguments and return values using the decorator.
For example:
>>> make_greeting("Benjamin")
Calling make_greeting('Benjamin')
'make_greeting' returned 'Howdy Benjamin!'
'Howdy Benjamin!'
>>> make_greeting("Richard", age=112)
Calling make_greeting('Richard', age=112)
'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
'Whoa Richard! 112 already, you are growing up!'
>>> make_greeting(name="Dorrisile", age=116)
Calling make_greeting(name='Dorrisile', age=116)
'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
'Whoa Dorrisile! 116 already, you are growing up!'

"""

def deco(make_greeting):
    def wrapper(*args,**kwargs):
        if "age" in kwargs and "name" in kwargs:
            age = kwargs["age"]
            name = kwargs["name"]
            print(f"Calling {make_greeting.__name__}(name='{name}', age={age})")
            print(f"'{make_greeting.__name__}' returned '{name}! {age} already, you are growing up!'")
        elif "age" in kwargs:
            age = kwargs["age"]
            print(f"'{make_greeting.__name__}' returned '{args[0]}! {age} already, you are growing up!'")
        else:
            print(f"Calling {make_greeting.__name__}(name='{args[0]}')")
            print(f"'{make_greeting.__name__}' returned 'Howdy {args[0]}!'")
        make_greeting(*args,**kwargs)
    return wrapper


@deco
def make_greeting(*args,**kwargs):
    if "age" in kwargs and "name" in kwargs:
        name = kwargs["name"]
        age = kwargs["age"]
        print(f"{name}! {age} already, you are growing up!")
    elif "age" in kwargs:
        age = kwargs["age"]
        print(f"{args[0]}! {age} already, you are growing up!")
    else:
        print(f"Howdy {args[0]}!")

if __name__ == "__main__":
    make_greeting("Benjamin")
    make_greeting("Richard", age=112)
    make_greeting(name="Swaminarayan", age=116)