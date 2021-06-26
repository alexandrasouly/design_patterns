augment functionality without changing the class (can't/don't want to/OCP/SRP)
need to interact with existing structures
solution:
inherit or build a decorator

decorator keeps the reference to the underlying object, adds attributes/methods
may or may not be able to forward calls to the underlying object

python decorators are language specific