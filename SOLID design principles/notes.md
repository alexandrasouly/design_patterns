
Single responsibility principle:
    A class should be responsible for only one thing
    Should have a single reason to change
    Separation of concerns
    Example here: Journal class to store and manipulate entries
    We broke it by adding the responsibility of load from web, save, etc.
     -> responsibility of persistence should go to a class "persistence manager"
        as it's technically not related to journal

    Don't overload objects with too many responsibilities

    anti-pattern: "God-object" - everything in a massive class
     
Open-closed principle:
    Adding new functionality added by extension not, not by modification if the design changes
    (open for extension, closed for modification)
    Example here:
        product class: 
        - a product with color and size
        product filter class: 
        - filter by color

        then you go and add filter by size
        then you add filter by color and size

        -> not scalable (2^n-1 number of methods for n filter criteria)

        instead: 
        spec class: 
        - base class, has an is_satisfied method that we overwrite  
        Color_spec class: 
        - inherits from spec class, init method sets color
        - you rewrite the is-satisfied method to compare item color with colorspec
        and_specification class:
        - inherits from specification, is_satisfied method checks for all specs if it is satisfied
        filter class: 
        - give items,specification to filter by, check if spec is satisfied for items

     Base classes add a lot more flexibility to add further classes


Liskov Substitutipn Principle:
    classes that inherit from a class should not break the original class' methods
    You should be able to substitute a base type for a subtype
    Example:
    we have a class Square class that inherited from Rectange class
    Square changes other side when you set one side length
    We can write a function that works on rectangle, but not on the Sqaure class

Interface Segregation Principle:
    Split interfaces to be as small as possible, so that 
    people don't have to implement more than they need to
    YAGNI - You ain't gonna need it 
    Example:
        base class, has lots of methods
        lots of subclasses that inherit from it
        but what if only some of the subclasses use a method?
        there is still the inherited interface from the base class for those classes that don't use these methods

        solution:
        -don't define one main baseclass with all the methods
        -define them separately in bunches that make sense
        -then you can create a class that inherits from both of them 
        -eg Class printer can print, class scanner can print, you can have a class photocopier inherit from both 

        Here abstract methods are methods that have no implementation, only define an interface.
        The subclasses are forced to reimplement them

Dependency inversion principle:
    High level modules shouldn't depend directly on low-level modules
    Instead they should depend on abstractions
    Depend on interfaces instead of implementations

    Example:
        -Research is a high-level module
        -shouldn't depend on how relations are stored
        -if relationship becomes a dict instead, research class breaks

        instead:
        - implement a method of searching for children within
        the relationships module, as it is dependent on its implementation
        - to make sure the relationships module has a find_all_children method, you make it inherit this as an abstract method from a base class "relationship browser"
        - then in research module you can pass in a browser object (like the inherited relationships class) and call the find_all_children
        - this would work if you had another relationships class that for example stored the data in dictionaries, and had its own find_all_children method
        - so ultimately research module doesn't depend on how the data is stored  


