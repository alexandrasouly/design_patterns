Most hated pattern, if you are using it you probably don't need it and shoudln't be

For components you only want to initialise once: eg database repo, object factory
when initialiser call is expensive
you don't want to allow it to be initialised anymore, give that instance to everyone
you don't want to allow copies (expensive)
you don't want to initialise it until used

singleton allocator:
redefine __new__ allocator
you can't have init defined - it gets called every time and creates another object

Whenever a class is instantiated __new__ and __init__ methods are called. __new__ method will be called when an object is created and __init__ method will be called to initialize the object. 
In the base class object, the __new__ method is defined as a static method which requires to pass a parameter cls.  cls represents the class that is needed to be instantiated, and the compiler automatically provides this parameter at the time of instantiation.

If you use the decorator version, you can define the init method

Decorators:
def my_decorator(func):
    def wrapper((*args, **kwargs):
        print("Something is happening before the function is called.")
        func((*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee((*args, **kwargs):
    print("Whee!")