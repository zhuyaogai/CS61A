"""Lab 1: Expressions and Control Structures"""

# Q3
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    return x > 0 and y > 0 # You can replace this line!

# Q4
def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    while n != 0:
       sum += (n % 10)
       n //= 10

    return sum  

# print(sum_digits(10));
# print(sum_digits(11110))

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    res = 1
    while k > 0:
        res *= n
        n -= 1
        k -= 1
    
    return res

# print(falling(4, 0))
# print(falling(4, 3))
# print(falling(4, 1))
# print(falling(6, 3))

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    
    a = 0
    b = 0
    while n != 0:
        a, b = n%10, a
        n //= 10
        if a == 8 and b == 8:
            return True
    
    return False


    # prev_eight = False
    # while n > 0:
    #     last_digit = n % 10
    #     if last_digit == 8 and prev_eight:
    #         return True
    #     elif last_digit == 8:
    #         prev_eight = True
    #     else:
    #         prev_eight = False
    #     n = n // 10
    # return False

# print(double_eights(8))
# print(double_eights(88))
# print(double_eights(2882))
# print(double_eights(880088))
# print(double_eights(12345))
# print(double_eights(80808080))