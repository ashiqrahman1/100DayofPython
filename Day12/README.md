### Local Scope

- A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

```
def myFucntion():
    name = "Hello World"
    print(name)

myFunction()
```

### Global Scope

- A variable created in the main body of the code is a global variable and belongs to the global scope.
- Global variables are available from within any scope, global and local.

```
name = "Hello World"
def myFunction():
    print(name)

myFunction()
```

### Python Does not have any Block Scope

```
if 2 > 1:
    name = "You can access me"

print(name)


but if you specified inside a fucntion you can't access that

def myFunction():
    if 2 > 1:
        name = "You Can Access"

print(name) // This code will Throw an Error
```
