import numpy as np


def calculate(input_list):
    # Validate the input list
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list into a 3x3 Numpy array
    matrix = np.array(input_list).reshape(3, 3)

    # Compute statistics
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
    max_val = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
    min_val = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
    sum_val = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]

    # Create the result dictionary
    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }

    return calculations

if __name__ == "__main__":
    # Prompt the user to enter 9 numbers separated by spaces
    user_input = input("Enter 9 numbers separated by spaces: ")

    # Convert the input into a list of integers
    try:
        input_list = [float(num) for num in user_input.split()]
        # Call the calculate function
        result = calculate(input_list)
        print("Calculation Result:", result)
    except ValueError as e:
        print(e)
