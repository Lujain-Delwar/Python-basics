# #Ans 1
def process_list(numbers):
    original_list = numbers.copy()
    unique_values = list(set(numbers))

    result = {
        "Original List": original_list,
        "Unique Values": unique_values,
        "Count of Unique Values": len(unique_values)
    }

    return result



list1= input("Enter numbers separated by space: ")
numbers = list(map(int, list1.split()))

output = process_list(numbers)


print("Original List:", output["Original List"])
print("Unique Values:", output["Unique Values"])
print("Count of Unique Values:", output["Count of Unique Values"])

#Ans 2
def set_operations(set1=set(), set2=set()):
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    return union, intersection, difference



input1 = input("Enter elements of Set 1 separated by space (or press Enter to skip): ")
input2 = input("Enter elements of Set 2 separated by space (or press Enter to skip): ")

set1 = set(map(int, input1.split())) if input1 else set()
set2 = set(map(int, input2.split())) if input2 else set()

u, i, d = set_operations(set1=set1, set2=set2)

print("\nResults:")
print("Union:", u)
print("Intersection:", i)
print("Difference (Set1 - Set2):", d)

#Ans 3
# Define tuple with mixed data types
my_tuple = (10, "Python", 3.14, True)

# Unpacking
num, text, decimal, boolean = my_tuple

print("Unpacked Values:")
print(num)
print(text)
print(decimal)
print(boolean)

# Another tuple
another_tuple = (20, "Python", 3.14, False)

# Comparison
print("Are tuples equal?", my_tuple == another_tuple)
print("Is my_tuple less than another_tuple?", my_tuple < another_tuple)


# Difference between List and Tuple:
# 1. Lists are mutable (can be changed).
# 2. Tuples are immutable (cannot be changed).
