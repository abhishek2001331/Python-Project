class ClassName:
       def __init__(self, my_list, my_tuple):
        print("This is Constructor")
        print("List:", my_list)
        print("Tuple:", my_tuple)

list1 = [10, 20, 30]
tuple1 = (40, 50, 60)

obj = ClassName(list1, tuple1)
       

#pass the tuple and list as a function parameter
