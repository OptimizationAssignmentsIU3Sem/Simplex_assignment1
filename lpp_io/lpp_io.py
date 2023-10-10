import numpy as np

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[34m'
RESET = '\033[0m'


def input_lpp() -> tuple[np.array, np.array, np.array, int]:
    """
    Function reads input and returns
        1) maximize or minimize - true or false correspondingly.
        1) vector of coefficients of objective function - C.
        2) A matrix of coefficients of constraint function - A.
        3) A vector of right-hand side numbers - b.
        4) The number of digits after comma - alpha.
    """

    print(BLUE + "Enter the number of variables")

    var_count = 0
    while True:
        try:
            input_args = input().split()
            if len(input_args) != 1:
                print(RED + "Only one argument is required, please re-enter the number of variables" + BLUE)
                continue
            var_count = int(input_args[0])
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion for number of variables: {e}" + BLUE)

    print("Enter the number of constraints")

    constr_count = 0
    while True:
        try:
            input_args = input().split()
            if len(input_args) != 1:
                print(RED + "Only one argument is required, please re-enter the number of constraints" + BLUE)
                continue
            constr_count = int(input_args[0])
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion for number of constraints: {e}" + BLUE)

    print(f"Enter the line with {GREEN}{var_count + constr_count}{BLUE} coefficients of the objective function "
          f"separated by spaces")

    c = np.array([])
    while True:
        try:
            input_args = input().split()
            input_args_len = len(input_args)
            if input_args_len != var_count + constr_count:
                print(RED + f"You need to enter exactly {var_count + constr_count} coefficients, not {input_args_len}")
                print(BLUE + "Please re-enter the coefficients")
            var_list = list(map(float, input_args))
            c = np.array(var_list)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print(f"Enter {GREEN}{constr_count}{BLUE} lines with {GREEN}{var_count + constr_count}{BLUE} coefficients of "
          f"constraint function separated by spaces")

    a = []
    while True:
        a = []
        try:
            for i in range(constr_count):
                input_str = input().split()
                if len(input_str) != var_count + constr_count:
                    print(RED + f'You need to enter exactly {var_count + constr_count} coefficients,'
                                f' not {len(input_str)}' + BLUE)
                temp = list(map(float, input_str))
                a.append(temp)
            a = np.array(a)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print(f"Enter the line with {GREEN}{constr_count}{BLUE} values of vector of right-hand side numbers separated by "
          f"spaces")

    b = np.array([])
    while True:
        try:
            input_args = input().split()
            input_args_len = len(input_args)
            if input_args_len != constr_count:
                print(RED + f"You need to enter exactly {constr_count} coefficients, not {input_args_len}" + BLUE)
                print("Please re-enter the coefficients")
            var_list = list(map(float, input_args))
            b = np.array(var_list)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print("Enter the approximation accuracy you want")
    print(f"It's is recommended to use {GREEN}0.001{BLUE} precision or better to avoid false-degeneration of solution")

    eps = 0.0
    while True:
        try:
            input_args = input().split()
            if len(input_args) != 1:
                print(RED + "Only one number for epsilon is required" + BLUE)
                continue
            eps = float(input_args[0])
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion for epsilon: {e}" + BLUE)
    alpha = 0
    while eps < 1:
        alpha += 1
        eps *= 10

    return c, a, b, alpha


def output_not_applicable_error() -> None:
    print(RED + "The method is not applicable!" + BLUE)


def output_lpp(x: np.array, result_value: float) -> None:
    """outputs the vector of decision variables and maximum (minimum) value of the objective function"""
    print(f"The resulting vector of decision variables is: \n{GREEN}{x}{BLUE}")
    print(f"And it produced the final value of: {GREEN}{result_value}{BLUE}")


def print_error(msg: str) -> None:
    """prints the red-colored msg in stdout"""
    print(f"{RED}{msg}{BLUE}")
