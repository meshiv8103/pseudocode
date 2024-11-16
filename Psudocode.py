def sortAndFindMedian(numbers):
    """
    Function to sort the numbers and find the median.
    :param numbers: List of integers or floats
    :return: Median of the sorted numbers
    """
    # Call the sort function
    sort(numbers)
    
    # Calculate the median
    n = len(numbers)
    if n % 2 == 0:
        # If even number of elements, return the average of the middle two
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        # If odd number of elements, return the middle one
        median = numbers[n // 2]
    return median


def sort(numbers):
    """
    Bubble Sort implementation to sort the list in ascending order.
    :param numbers: List of integers or floats
    """
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap elements if they are in the wrong order
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


if __name__ == "__main__":
    # Example user interface for input
    print("Enter numbers separated by spaces:")
    user_input = input()
    
    # Convert user input into a list of numbers
    numbers = list(map(float, user_input.split()))
    
    # Calculate and print the median
    print("\nOriginal numbers:", numbers)
    median = sortAndFindMedian(numbers)
    print("Sorted numbers:", numbers)
    print("Median:", median)
