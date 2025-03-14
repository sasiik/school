import random
import sys
import timeit
import tkinter as tk


def task1():
    print("Task 1: String and List Methods Demonstrations")
    print("\n--- Part 1(a): String Methods ---")
    test_string = "Hello, World 123"
    print(f"Test string: '{test_string}'")

    # index()
    try:
        index_result = test_string.index("World")
        print("index(): Finds the starting index of the substring 'World' in the string. Result:", index_result)
    except ValueError:
        print("index(): Substring not found.")

    # count()
    count_result = test_string.count("l")
    print("count(): Counts the number of occurrences of 'l' in the string. Result:", count_result)

    # split()
    split_result = test_string.split()
    print("split(): Splits the string into a list of words using whitespace as the delimiter. Result:", split_result)

    # title()
    title_result = test_string.title()
    print("title(): Converts the first character of each word to uppercase and the rest to lowercase. Result:", title_result)

    # lower()
    lower_result = test_string.lower()
    print("lower(): Converts all characters in the string to lowercase. Result:", lower_result)

    # isnumeric()
    isnumeric_result = test_string.isnumeric()
    print("isnumeric(): Checks if all characters in the string are numeric. Result:", isnumeric_result)

    # Additional method: upper()
    upper_result = test_string.upper()
    print("upper(): Converts all characters in the string to uppercase. Result:", upper_result)

    print("\n--- Part 1(b): List Methods ---")
    # Demonstration on a list of floats
    print("\nList of floats demonstration:")
    float_list = [3.14, 2.71, 1.41]
    print("Original float list:", float_list)

    float_list.append(0.0)
    print("append(): Adds 0.0 to the end of the list. New list:", float_list)

    float_list.remove(2.71)
    print("remove(): Removes the first occurrence of 2.71 from the list. New list:", float_list)

    float_list_copy = float_list.copy()
    print("copy(): Creates a shallow copy of the list. Copy:", float_list_copy)

    float_list.reverse()
    print("reverse(): Reverses the order of elements in the list. New list:", float_list)

    float_list.sort()
    print("sort(): Sorts the list in ascending order. New list:", float_list)

    count_float = float_list.count(3.14)
    print("count(): Counts how many times 3.14 appears in the list. Count:", count_float)

    float_list.clear()
    print("clear(): Removes all items from the list. New list:", float_list)

    # Demonstration on a list of strings
    print("\nList of strings demonstration:")
    str_list = ["apple", "banana", "apple", "cherry"]
    print("Original string list:", str_list)

    str_list.append("date")
    print("append(): Adds 'date' to the end of the list. New list:", str_list)

    str_list.remove("banana")
    print("remove(): Removes the first occurrence of 'banana' from the list. New list:", str_list)

    str_list_copy = str_list.copy()
    print("copy(): Creates a shallow copy of the list. Copy:", str_list_copy)

    str_list.reverse()
    print("reverse(): Reverses the order of the list. New list:", str_list)

    str_list.sort()
    print("sort(): Sorts the list in alphabetical order. New list:", str_list)

    count_apple = str_list.count("apple")
    print("count(): Counts how many times 'apple' appears in the list. Count:", count_apple)

    str_list.clear()
    print("clear(): Removes all items from the list. New list:", str_list)


def task2():
    print("\nTask 2: Initializing and Manipulating a List of 10,000 Elements")
    # (a) Create a list of 10,000 zeros using list multiplication
    zeros_list = [0] * 10000
    print("List with 10,000 zeros created. First 10 elements:",
          zeros_list[:10])

    # (b) Create a list of 10,000 random floats in the interval (-5, 5)
    random_float_list = [random.uniform(-5, 5) for _ in range(10000)]
    print("List with 10,000 random floats between -5 and 5 created. First 10 elements:",
          random_float_list[:10])

    # Sort the random float list
    random_float_list.sort()
    print("After sort(): First 10 elements:", random_float_list[:10])

    # Shuffle the list randomly
    random.shuffle(random_float_list)
    print("After random.shuffle(): First 10 elements:", random_float_list[:10])

    # Sort again after shuffling
    random_float_list.sort()
    print("After sort() again: First 10 elements:", random_float_list[:10])


def task3():
    print("\nTask 3: Drawing Random Circles")
    # Generate random coordinates and colors for circles
    num_circles = 20
    x_coords = [random.randint(10, 390) for _ in range(num_circles)]
    y_coords = [random.randint(10, 390) for _ in range(num_circles)]
    colors = [
        f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(num_circles)]

    # Create a tkinter window with a canvas
    window = tk.Tk()
    window.title("Random Circles")
    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    radius = 10
    for x, y, color in zip(x_coords, y_coords, colors):
        canvas.create_oval(x - radius, y - radius, x +
                           radius, y + radius, fill=color)

    window.mainloop()


def task4():
    print("\nTask 4: Drawing a Colored Lines Path")
    num_points = 20
    x_coords = [random.randint(10, 390) for _ in range(num_points)]
    y_coords = [random.randint(10, 390) for _ in range(num_points)]
    colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(num_points)]

    # Create a tkinter window with a canvas
    window = tk.Tk()
    window.title("Colored Lines Path")
    canvas = tk.Canvas(window, width=400, height=400)
    canvas.pack()

    # Draw colored lines connecting each consecutive point
    for i in range(num_points - 1):
        canvas.create_line(x_coords[i], y_coords[i], x_coords[i+1], y_coords[i+1],
                           fill=colors[i], width=2)

    window.mainloop()


def task5():
    print("\nTask 5: Comparing Tuples and Lists")

    # Define a list and a tuple with the same elements
    list_ = [1, 2, 3, 'a', 'b', 'c', True, 2.5]
    tuple_ = (1, 2, 3, 'a', 'b', 'c', True, 2.5)

    # (a) Use sys.getsizeof() to compare memory usage
    size_list = sys.getsizeof(list_)
    size_tuple = sys.getsizeof(tuple_)
    print("sys.getsizeof() results:")
    print("Size of list:", size_list, "bytes")
    print("Size of tuple:", size_tuple, "bytes")
    print("Observation: Tuples usually consume less memory than lists because they are immutable.")

    # (b) Use timeit to compare performance of creating a list literal vs. a tuple literal
    list_time = timeit.timeit(
        "[1, 2, 3, 'a', 'b', 'c', True, 2.5]", number=1000000)
    tuple_time = timeit.timeit(
        "(1, 2, 3, 'a', 'b', 'c', True, 2.5)", number=1000000)
    print("\ntimeit() results:")
    print("Time to create list literal:", list_time, "seconds")
    print("Time to create tuple literal:", tuple_time, "seconds")
    print("Observation: Tuple creation is generally a bit faster than list creation due to its immutability.")

    # (c) Tuple unpacking
    item1 = ('Charlie Brown', 11, 'USA')
    name, age, country = item1  # Unpacking the tuple
    print("\nTuple unpacking result:")
    print(f"Name is {name}, age is {age}, country is {country}")


def main():
    task1()
    task2()
    task5()

    input("\nPress Enter to open the circle drawing window (Task 3)...")
    task3()

    input("\nPress Enter to open the colored lines drawing window (Task 4)...")
    task4()


if __name__ == "__main__":
    main()
