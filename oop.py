class Helper:

    def __init__(self, item, importance):
        self.item = item
        self.importance = importance

        print("Creating object...")
        print("Item:", self.item)
        print("Importance:", self.importance)

    def __del__(self):
        print("Destroying object...")


obj = Helper("Building", "Important")
obj2 = Helper("Gucci", "Not Important")


def class_obj(existing_obj):
    print("Received:", existing_obj.item)

    obj3 = Helper("Phone", "Important")

    print("Object created")

    return obj3


new_obj = class_obj(obj)






    
