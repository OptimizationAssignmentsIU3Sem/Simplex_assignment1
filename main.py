import unittest
from lpp_io import input_lpp, output_lpp, print_error
from simplex import simplex, get_z_of_x

# if you set TEST to true the standard input won't work, it will run only tests instead
TEST = False

if __name__ == "__main__":
    if TEST:
        unittest.main(module="tests")
    C, A, b, alpha = input_lpp()
    try:
        result = simplex(C, A, b, alpha)
        value = get_z_of_x(C, result)
        output_lpp(result, value)
    except ValueError as e:
        print_error(str(e))
