#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")
        return

    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)

    return new_list
