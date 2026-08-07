class Employee:

    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object destroyed")


def Class_obj():

    print("Creating object...")

    obj = Employee()
    print("Destroying object...")
    return obj



Class_obj()
    