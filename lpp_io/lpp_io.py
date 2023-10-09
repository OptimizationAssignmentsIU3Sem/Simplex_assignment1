import numpy as np

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[34m'
RESET = '\033[0m'


def input_lpp() -> tuple[bool, np.array, np.matrix, np.array, float]:
    """
    Function reads input and returns
        1) maximize or minimize - true or false correspondingly.
        1) vector of coefficients of objective function - C.
        2) A matrix of coefficients of constraint function - A.
        3) A vector of right-hand side numbers - b.
        4) The approximation accuracy - eps.
    """

    print(BLUE + f"Enter \"{GREEN}yes{BLUE}\" if the goal is to maximize and \"{RED}no{BLUE}\" if to minimize")

    maximize = True
    while True:
        input_args = input().split()
        if len(input_args) != 1:
            print(RED + "Only one argument is required, please re-enter your answer" + BLUE)
            continue
        if input_args[0] == "yes":
            maximize = True
            break
        elif input_args[0] == "no":
            maximize = False
            break
        else:
            print(RED + f"The input {RED}\"{input_args[0]}\"{BLUE} is not yes or no, please re-enter" + BLUE)

    print("Enter the number of variables")

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
            if len(input_args) != var_count + constr_count:
                print(RED + f"You need to enter exactly {var_count + constr_count} coefficients, not {len(input_args)}")
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
                                ' not {len(input_args)}' + BLUE)
                temp = np.array(list(map(float, input_str)))
                a.append(temp)
            a = np.matrix(a)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print(f"Enter the line with {GREEN}{constr_count}{BLUE} values of vector of right-hand side numbers separated by "
          f"spaces")

    b = np.array([])
    while True:
        try:
            input_args = input().split()
            if len(input_args) != constr_count:
                print(RED + f"You need to enter exactly {constr_count} coefficients, not {len(input_args)}" + BLUE)
                print("Please re-enter the coefficients")
            var_list = list(map(float, input_args))
            var_list.extend([0 for _ in range(constr_count)])
            b = np.array(var_list)
            break
        except ValueError as e:
            print(RED + f"Failed to make a conversion into floats: {e}" + BLUE)

    print("Enter the approximation accuracy you want")

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

    return maximize, c, a, b, eps


def output_not_applicable_error() -> None:
    print(RED + "The method is not applicable!" + BLUE)


def output_lpp(x: np.array, result_value: float) -> None:
    """outputs the vector of decision variables and maximum (minimum) value of the objective function"""
    print(f"The resulting vector of decision variables is: \n{GREEN}{x}{BLUE}")
    print(f"And it produced the final value of: {result_value}")
