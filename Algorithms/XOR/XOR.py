# Core Properties of XOR for Competitive Programming:
# Mastering XOR means mastering its algebraic properties:
# 1. Identity Property (x ^ 0 = x): Xoring a number with 0 leaves it unchanged.
# 2. Self-Inverse Property (x ^ x = 0): Xoring a number with itself cancels it out completely. 
#    This is the most used property in CP (e.g., finding duplicates or pairs).
# 3. Commutative (a ^ b = b ^ a): Order does not matter.
# 4. Associative ((a ^ b) ^ c = a ^ (b ^ c)): Grouping does not matter.
# ==========================================

a = 5   # Binary: 0101
b = 3   # Binary: 0011

result = a ^ b  # Binary: 0110 -> Decimal: 6
print(result)   # Output: 6



# How to pass integer type to binary

print(bin(5))  # Output: '0b101'
print(bin(3))  # Output: '0b011'
print(bin(6))  # Output: '0b110'

# Cleared version print(f"{5:04b}")  # Output: '0101'

print(f"{3:04b}")  # Output: '0011'
print(f"{6:04b}")  # Output: '0110'


# Binary to integer
binary_str = "0110"
decimal_value = int(binary_str, 2)
print(decimal_value)  # Output: 6