ordinary statements are perishable
- cannot undo assignments, cannot directly serialize a sequence of actions (calls)
- want an object that represent an operation to record how/when the operation was requested 

uses: GUI, multi-level undo/redo, macro recording

command: an object which represents an instruction to perform a particular action. Contains all the information necessary for the action to be taken.