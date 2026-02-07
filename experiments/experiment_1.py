# This experiment validates properties of the Collatz conjecture (3n+1 problem) by tracking sequence lengths and maximum values reached for different starting numbers. We'll test the conjecture for numbers 1-100 and analyze patterns.
# Verified: No (simulated)

import numpy as np

def collatz_sequence(n):
    """Return sequence length and maximum value for starting number n"""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        sequence.append(n)
    return len(sequence), max(sequence)

# Test numbers 1-100
numbers = range(1, 101)
lengths = []
max_values = []

print("Testing Collatz conjecture for numbers 1-100...")
print("\nSample detailed sequences for first 5 numbers:")

for n in numbers:
    length, max_val = collatz_sequence(n)
    lengths.append(length)
    max_values.append(max_val)
    
    if n <= 5:  # Print detailed results for first 5 numbers
        print(f"\nStarting number: {n}")
        print(f"Sequence length: {length}")
        print(f"Maximum value: {max_val}")

# Statistical analysis
print("\nStatistical Analysis:")
print(f"Average sequence length: {np.mean(lengths):.2f}")
print(f"Maximum sequence length: {max(lengths)} (for n={lengths.index(max(lengths))+1})")
print(f"Minimum sequence length: {min(lengths)} (for n={lengths.index(min(lengths))+1})")
print(f"Average maximum value: {np.mean(max_values):.2f}")
print(f"Highest value reached: {max(max_values)} (for n={max_values.index(max(max_values))+1})")
