def student_card(name, age=18, *hobbies, **extra_info):
    """
    Function that takes student information and prints it.
    
    Args:
        name: Student name (positional argument)
        age: Student age (default = 18)
        *hobbies: Unlimited hobbies (variable positional arguments)
        **extra_info: Unlimited extra information (variable keyword arguments)
    """
    # Print name and age
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    # Print hobbies
    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"  - {hobby}")
    else:
        print("Hobbies: None")
    
    # Print extra information
    if extra_info:
        print("Extra Information:")
        for key, value in extra_info.items():
            print(f"  {key}: {value}")
    else:
        print("Extra Information: None")


# Example usage
if __name__ == "__main__":
    print("Example 1:")
    student_card("Alice", 20, "Reading", "Swimming", "Coding", city="New York", grade="A")
    
    print("\nExample 2:")
    student_card("Bob", "Gaming", "Music", major="Computer Science")
    
    print("\nExample 3:")
    student_card("Charlie")

