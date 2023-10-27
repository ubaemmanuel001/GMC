# Question 1
divisible_by_7_not_multiple_of_5 = [num for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
print(divisible_by_7_not_multiple_of_5)

# Question 2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number to calculate its factorial: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")

# Question 3
def generate_dict(n):
    result_dict = {i: i*i for i in range(1, n+1)}
    return result_dict

n = int(input("Enter a number: "))
output_dict = generate_dict(n)
print(output_dict)

# Question 4
def missing_char(word, n):
    return word[:n] + word[n+1:]

word = input("Enter a word: ")
n = int(input(f"Enter the index (0 to {len(word)-1}): "))

result = missing_char(word, n)
print(result)

# Question 5
import numpy as np

original_array = np.array([[0, 1], [2, 3], [4, 5]])
list_structure = original_array.tolist()

print("Original array elements:")
print(original_array)
print("\nArray to list:")
print(list_structure)

# Question 6
import numpy as np

array1 = np.array([0, 1, 2])
array2 = np.array([2, 1, 0])

covariance_matrix = np.cov(array1, array2)
print(f"Covariance matrix of the said arrays:\n{covariance_matrix}")

# Question 7
import math

C = 50
H = 30
D_values = [int(val) for val in input("Enter comma-separated values of D: ").split(',')]

results = [round(math.sqrt((2 * C * D) / H)) for D in D_values]
print(results)