# Install packages
import sympy
import random
from uniplot import plot


# Setting variables
n = 20

# 1.1 Calculate sin(0.1) using its taylor expansion to order 5.
x = 0.1
taylor_expansion = sympy.sin(x).series(x, 0, 5)


# 1.2 Print the result as a descriptive string stating the order expanded to and value to 5 decimal places.
print("\n___\n1.2.\n___\n")
print(f"The Taylor expansion of sin({x}) to order 5 as given in exercise 1.1. is: {round(taylor_expansion, 5)}")

# 1.3 Construct a function which returns a list of prime numbers less than a given integer, N.
def prime_numbers(n):
    """
    Returns a list of prime numbers less than a given integer, N.

    Parameters:
    n (int): The upper limit (exclusive) for prime numbers.

    Returns:
    list: A list of prime numbers less than n.
    """
    return list(sympy.primerange(2, n))

print("\n___\n1.3.\n___\n")
print(f"The function to return a list of prime numbers less than n was constructed.\nE.g., for n = {n}, the function returns: {prime_numbers(n)}")

# 1.4 Construct a function which returns a list of the first N terms in the Recaman’s sequence (see also here).
def recaman_sequence(n):
    """
    Returns the first N terms of the Recaman's sequence.

    Parameters:
    n (int): The number of terms to generate in the sequence.

    Returns:
    list: A list containing the first N terms of the Recaman's sequence.
    """
    sequence = [0]  # Starting term of Recaman's sequence
    
    for i in range(1, n):
        prev = sequence[-1]
        next_term = prev - i
        # If next_term is negative or already in the sequence, add i instead
        if next_term < 0 or next_term in sequence:
            next_term = prev + i
        sequence.append(next_term)
    
    return sequence

print("\n___\n1.4.\n___\n")
print(f"The function to return a list of the first n terms of Recaman's sequence was constructed.\nE.g., for n = {n}, the function returns: {recaman_sequence(n)}")


# 1.5 Compute a list of the numbers which appear in both lists when they are both N items long.
# It feels like there is an error in this exercise. The prime numbers list is not of length N, instead all elements are less than N.
# Therefore, I will just compute the intersection of the two lists, but they will never be of the same length n.

prime_numbers_list = prime_numbers(n)
recaman_sequence_list = recaman_sequence(n)
# Compute the intersection of the two lists
intersection = list(set(prime_numbers_list).intersection(recaman_sequence_list))
print("\n___\n1.5.\n___\n")
print(f"The intersection of the prime numbers and Recaman lists for n = {n} is: {intersection}")

# 1.6 Create a list of all pairs of factors (as tuples) of 362880 using list comprehension.
number = 362880

# Use list comprehension to generate pairs of factors
factor_pairs = [(i, number // i) for i in range(1, int(number**0.5) + 1) if number % i == 0]

print("\n___\n1.6.\n___\n")
print(f'The list of all factor pairs of {number} is: {factor_pairs}')


# 1.7 Write a generator function for a random walk, step size 1, which is equally likely to go up or down. End
# the generator when you have total displacement of 10 steps (you will need a random number generator like
# random.randint(a,b) which gives a random integer between a and b inclusive, you will need to add the line
# import random at the top in order to use it).

def random_walk():
    """
    Generator function for a random walk with step size 1, equally likely to go up or down. 
    Ends the generator when the total displacement is 10 steps.
    """
    steps = []
    positions = [0]
    total_displacement = 0
    while abs(positions[-1]) < 10:
        step = random.choice([-1, 1])
        steps.append(step)
        # Add a new element to the position list, which is the last element plus the new step
        positions.append(positions[-1] + step)
    return positions

data = random_walk()

print("\n___\n1.7.\n___\n")
print("The generator function for a random walk was constructed. It stops once the absolute displacement reaches 10. An example of a generated random walk is given here:")
plot(data, title="Random Walk")