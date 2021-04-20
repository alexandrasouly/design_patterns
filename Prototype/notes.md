motivation: complicated objects in real life are created over many iterations of the design
existing design is a prototype
we make a copy of the prototype and customize it

in shallow copies, references to objects within the object get carried over
in deep copies, they don't -> you need to use copy.deepcopy if you want a *full* copy

factories are good for giving you an API to get a copy of the prototype