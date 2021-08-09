# TODO: 1. Functions are objects
# def shout(text):
#     return text.upper()

# print(shout('hello'))

# yell = shout

# print(yell('everyone')) 


# TODO: 2. Functions can be passed as arguments to other functions

# def shout(text):
#     return text.upper()

# def whisper(text):
#     return text.lower()

# def greet(func):
#     greeting = func("Hi, i am creating a function")
#     print(greeting)

# greet(shout)
# greet(whisper)


# TODO: 3. Functions can return another function

def create_adder(x):
    def adder(y):
        print(x)
        print(y) 
    
    return adder

add_15 = create_adder(15)

add_15(10)