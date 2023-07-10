# Why Diagnose Code

* Code Clarity
* Code Flexibility
* Code Testability

# Most Common Problems

## Code Clarity Problems

Huge code file, very large initializers, large number of imports can point to a lot of coupling

confusing naming of variables, lack of documentation, no type annotations, 

Complex and/or deeply nested if/else statements.

Python magic, decorators and dunder methods.

Readability alone is not a good enough reason for refactoring. readability is a personal and subjective measure.

## Code Flexibility Problems

Lots and lots of imports, deep class hierarchies, overuse of mixins, tightly coupled, passing too much data that isn't being used, inappropriate intimacy (knowing too much), law of demeter (objects should not have information about the inner workings of other objects), and repeated code.

## Code Testability Problems

If code is creating and using a resource in the same place, code is not using abstractions at all, and instead directly using the objects that it needs, tightly coupled and relying on multiple objects out side the scope.