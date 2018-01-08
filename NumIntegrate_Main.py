import function_operations as f_o

def run():
    function = f_o.makeFunc()
    integral = f_o.computeIntegral(function)
    print(integral)
    lower = 1
    upper = 0
    while upper < lower:
        upper = int(input("Please enter an upper bound\n"))
        lower = int(input("Please enter a lower bound\n"))
    ans = f_o.computeFunc(integral,upper) - f_o.computeFunc(integral,lower)
    print("Integral = " + str(ans))
    return
