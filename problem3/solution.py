def print_students_alphabetically(*student_names):
    """
    Accepts any number of student names and prints them in alphabetical order.
    
    Args:
        *student_names: Variable number of student names (variable positional arguments)
    """
    if not student_names:
        print("No student names provided.")
        return
    
    # Sort the student names alphabetically
    sorted_names = sorted(student_names)
    
    # Print the sorted names
    print("Students in alphabetical order:")
    for name in sorted_names:
        print(f"  - {name}")


# Example usage
if __name__ == "__main__":
    print("Example 1:")
    print_students_alphabetically("Alice", "Bob", "Charlie", "David")
    
    print("\nExample 2:")
    print_students_alphabetically("Zoe", "Alice", "Mike", "Bob", "Charlie")
    
    print("\nExample 3:")
    print_students_alphabetically("John")
    
    print("\nExample 4:")
    print_students_alphabetically()

