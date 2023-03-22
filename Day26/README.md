#### List Comprehension

- List Comprehension offers a shorter syntax when you want to create a new list based on the values of existing list

```
Example Code

without list comprehension
--------------------------
new_list = []
for i in range(11):
    if i % 2 == 0:
        new_list.append(i)


With List Comprehension
--------------------------
new_list = [x for x in range(11) if i % 2 == 0]
```

#### Dictionary Comprehension
