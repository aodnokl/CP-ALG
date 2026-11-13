# ==========================================
# PROBLEM: Integer Power Calculation (Binary Exponentiation / Divide and Conquer)
# ==========================================
# Description:
#
# Given a value `a` (which satisfies the associative property) and a non-negative 
# integer `n`, calculate the power a^n[cite: 1]. 
# A naive iterative scheme multiplying `a` sequentially takes a linear cost of \Theta(n), 
# but we can leverage exponent properties to achieve a logarithmic runtime complexity of \Theta(\log n)[cite: 1].
#
# Core Properties of Binary Exponentiation for this Problem:
# Mastering this variant involves divide-and-conquer and exponent rules:
# 1. Exponent Property: Exploiting the rule a^n \times a^m = a^(n+m) to break down the problem[cite: 1].
# 2. Base Cases: If n == 0, return 1; if n == 1, return `a` directly.
# 3. Even Exponent: If `n` is even (n % 2 == 0), compute aux = power(a, n // 2) and return aux * aux[cite: 1].
# 4. Odd Exponent: If `n` is odd, compute aux = power(a, n // 2) and return aux * aux * a[cite: 1].
# 5. Logarithmic Cost: Halving the exponent at each step results in the recurrence 
#    relation T(n) = T(n/2) + k', yielding an overall cost of \Theta(\log n)[cite: 1].

from typing import Any, Union

def power_DyV(a: Union[int, float, Any], n: int) -> Union[int, float, Any]:
    if n == 0:
        return 1
    elif n == 1:
        return a
    
    aux = power_DyV(a, n // 2)
    
    if n % 2 == 0:
        return aux * aux
    
    return aux * aux * a