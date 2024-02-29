def demo(n):
    # Create a boolean list "prime[0..n]" and initialize all entries as True.
    # A value in prime[i] will finally be False if i is Not a prime, else True.
    prime = [True for _ in range(n+1)]
    prime[0], prime[1] = False, False  # 0 and 1 are not prime numbers.

    p = 2
    while p**2 <= n:
        # If prime[p] is not changed, then it is a prime.
        if prime[p]:
            # Update all multiples of p
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1

    # Return a list of prime numbers up to n.
    return [num for num in range(2, n+1) if prime[num]]

# Example: Find all prime numbers up to 100
n = 100
result = demo(n)
print(result)
