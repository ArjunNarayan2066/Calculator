import function_operations as f_o

def run():
    function = f_o.makeFunc()
    derivative = f_o.computeDerivative(function)
    print("Derivative = ")
    f_o.printFunc(derivative)
