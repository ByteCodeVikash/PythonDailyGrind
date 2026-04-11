#4. Write a python program to create a function which expects kwargs arguments.

def show(**kwargs):
     for key,values in kwargs.items():
        print(key,values)


show(name='vikash',age=26)        