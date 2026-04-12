#7. Write a python program to access a function inside a function.

def OuterFunct():
    print("This is outer function")

    def InnerFunct():
              print("This is inner function")

          

    InnerFunct()

OuterFunct()
