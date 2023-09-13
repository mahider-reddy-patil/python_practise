# 1) Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {"A": 1, "B": 4, "C": 3, "D": 2}

my_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
my_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("ascending a dictionary by value:", my_dict_asc)
print("descending a dictionary by value:", my_dict_desc)

# 2) Write a Python program to sum all the items in a dictionary.

my_dict_sum = sum(my_dict.values())
print("sum all the items in a dictionary:", my_dict_sum)

# 3) Write a Python program to map two lists into a dictionary.

list1 = ["Name", "Age", "Country"]
list2 = ["Jhon", 20, "USA"]

map_two_lists = dict(zip(list1, list2))
print("map two lists into a dictionary:", map_two_lists)

# 4) Write a Python program to sort a given dictionary by key.

sorted_dict = dict(sorted(map_two_lists.items()))
print(sorted_dict)

# 5) Write a Python function that takes two lists and returns True if they have at least one common member.

def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

print(common_member(list1, list2))

# 6) Write a Python program to get unique values from a list.
# 	e.g [10, 20, 30, 40, 20, 50, 60, 40]

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
unique_list = list(set(my_list))
print(unique_list)

# 7) Write a Python program to find the third largest number from a given list of numbers

unique_list.sort()
print("The third largest number in the list is:", unique_list[2])

# 8) Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type

my_list = ["apple", "banana", "orange", "banana", "kiwi", "apple"]
unique_list = list(set(my_list))
print(unique_list)
