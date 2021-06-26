object in a system might go through several changes
there are different ways to navigate those changes
one way is to record every change (command) and teach the command to undo itself (command pattern)
other way is to save a snapshot: memento

memento is a token representing the system state at a point in time
lets us roll back

memento is usually a token/handle class with no functions of its own
not required to expose directly the states to which it reverts to 
can be used to implement redo/undo 