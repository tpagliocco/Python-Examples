def print_formatted(number):

    #for i in range(1,number+1):
    #    d = i
    #    x = oct(i)
    #     y = hex(i)
    #   z = "{0:b}".format(i)

    #    print(d, x, y, z)

    # this was all bad code , my final solution is much better

    # get width of padding which is the binary of n using format string
    width = len("{0:b}".format(n))
    # for loop to output the cycles of n being 1 and the total being n+1 for finality
    for i in range(1,number+1):
        # here we are printing each with formatting, 0 for position, width to width, and conversion type
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
