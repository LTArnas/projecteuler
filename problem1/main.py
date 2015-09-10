if __name__ == "__main__":
    a = set(range(0,1000,3)) # The multiples of 3
    b = set(range(0,1000,5)) # The multiples of 5
    # Sum up (only using unique values between the two.)
    print(sum(a|b))