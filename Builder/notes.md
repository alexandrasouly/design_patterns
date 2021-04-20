I found this hard to understand and many examples were hard to follow online too.

Use this when many argument to set
Create complicated classes
Builder is an API that hides all the complex stuff from you and just returns an object


have a product class that can have many attributes and methods, but initialise them to none
the "product" class will get filled through the constructor

have a builder class that is a base class, and implements a reset method to get a new "clean slate" product, and methods for building different parts

have multiple builder classes inherit from the base class, building the parts is a specific way.
their init method initialises an empty "clean slate" product, the reste method just gives another clean slate product


To build up all or specific parts in one step, have a directory method that returns the whole product by building all the parts


A nice article is this:
https://stackabuse.com/creational-design-patterns-in-python/#builder
and another nice one is this:
https://refactoring.guru/design-patterns/builder/python/example


######################## Article ideas ##########################
I think the combination would be the perfect - the refactoring one is nicer code
with the @property decorator and the conceptual example,
but the first one is more intuitive.
Combine the two? First example, then "bare bones" code.

An example with machines would be good - instead of robots, have cars, planes, bicycles etc, and a builder for each - add wings, engines, wheels etc

With lots of explanation between the code, and with the director at the end



