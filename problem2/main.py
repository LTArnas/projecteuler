if __name__ == "__main__":
    """ Originally, I was going to make a list of the fib sequence until
    it reached over 4k. But then, I figured why make so many variables.
    The problem is, this may be a bit unreadable. """
    answer = 0
    first = second = third = 1
    for i in range(4000000): # Don't like "while true:" loops, so this.
        third = first + second
        first = second
        second = third
        if third > 4000000: # Loop exit rule, as per problem requirement.
            break
        if third % 2 == 0:
            answer += third

    print(answer)