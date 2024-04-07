# import numpy as np
#
#
# def calculate_mean(data: np.ndarray) -> float:
#     """
#     Calculate the mean of the given array of numbers.
#
#     Parameters
#     ----------
#     data: np.ndarray
#         An array of numbers for which the mean should be calculated.
#
#     Returns
#     -------
#     mean: float
#         The mean of the elements in the input array.
#
#     Examples
#     --------
#     # >>> data = np.array([1, 2, 3, 4, 5])
#     # >>> calculate_mean(data)
#     # 3.0
#     #
#     # >>> data = np.random.rand(100)
#     # >>> calculate_mean(data)
#     # 0.49051766602405433
#     """
#
#     # Check if the input is a valid NumPy array
#     if not isinstance(data, np.ndarray):
#         raise TypeError("Input data must be a NumPy array.")
#
#     # Check if the array is empty
#     if data.size == 0:
#         raise ValueError("Input array cannot be empty.")
#
#     # Calculate the mean using NumPy's mean function
#     mean = np.mean(data)
#     return mean
#
#
# data = np.array([1, 2, 3, 4, 5])
# print(calculate_mean(data))


def calculate_mean(numbers):
    """
    Calculate the mean of an array of numbers.

    Parameters
    ----------
    numbers : array_like
        An array of numbers (integers or floats) whose mean is to be calculated.

    Returns
    -------
    float
        The mean of the input numbers.

    Examples
    --------
    # >>> calculate_mean([1, 2, 3, 4, 5])
    3.0

    # >>> calculate_mean([10, 20, 30, 40, 50])
    30.0

    # >>> calculate_mean([-5, 5, -10, 10])
    0.0
    """
    if not numbers:  # Ensure the input is not empty
        return 0
    return sum(numbers) / len(numbers)


# Example usage
if __name__ == "__main__":
    example_array = [1, 2, 3, 4, 5]
    print(f"The mean of {example_array} is {calculate_mean(example_array)}.")

    example_array2 = [10, 20, 30, 40, 50]
    print(f"The mean of {example_array2} is {calculate_mean(example_array2)}.")

    example_array3 = [-5, 5, -10, 10]
    print(f"The mean of {example_array3} is {calculate_mean(example_array3)}.")