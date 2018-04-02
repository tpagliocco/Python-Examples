def print_formatted(number):

    for i in range(1,number+1):
        d = i
        x = oct(i)
        y = hex(i)
        z = "{0:b}".format(i)

        print(d, x, y, z)
