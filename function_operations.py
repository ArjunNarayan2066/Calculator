#Global Variable Definitions
prec = 10**-12

def cmplxConj(num):
    return complex(num.real,-1*num.imag)

def printRoot(root):
    print("Roots are as follows")
    for i in range (len(root)):
        print("x - [" + str(root[i]) + "]")
    print("Done")

def roundComplex (val):
    if abs(round(val.imag) - val.imag) < 10**-8: #Round Imaginary
        val = complex(val.real, round(val.imag))
    if abs(round(val.real) - val.real) < 10**-8: #Round Real
        val = complex(round(val.real), val.imag)
    if val.imag == 0:
        val = val.real
    #val = complex(round(val.real,5),round(val.imag,5))
    return val

def printFunc(function):
    #Initial Setup
    order = len(function)-1
    func = ""
    if function[0] < 0:
        func += "-"

    #Building term by term
    try:
        for cnt in range (0,order):
            func += str(abs(function[cnt]))+"x^"+str(order-cnt)
            if function[cnt+1] >= 0: #Figure out how to use ternary operator?
                func += " + "
            else:
                func += " - "
    except TypeError: #For accounting for Integral + C addition
        print("Printing an Integral")
        func += " + C"
        print(func)
        return
    
    #Ending & Printing
    func += str(abs(function[order]))#Adding entry with no x
    print(func)

def computeFunc (function, value):
    #Setup
    ans = 0
    order = len(function)-1

    #Computing Values
    for cnt in range (0, order+1):
        if function[cnt] != None:
            val = function[cnt] * (value ** (order-cnt))
            ans += val
    return ans

def makeFunc ():
    correct = True
    while correct:
        #Initial Setup
        function = []
        order = -5

        #Getting Size
        while order < 0:
            order = int(input("Please enter the highest order\n"))

        #Creating list to model function
        for cnt in range (order,-1,-1):
            a = float(input("Please enter coefficient for power " + str(cnt)+ "\n"))
            function.append(a)

        #Printing Values    
        printFunc(function)

        #Check
        ans = input("Is this accurate? Y?N\n")
        if ans == "Y" or ans == "y":
            correct = False
    return function #Shouldn't function not exist anymore???


def computeDerivative (function):
    #Initial Setup
    order = len(function)-1
    derivative = []
    
    #Base Cases
    if order == 0:
        derivative.append(0)
    elif order == 1:
        derivative.append(function[0])

    #Build Derivative List
    else:
        for cnt in range (0, order+1):
            entry = function[cnt] * (order - cnt)
            derivative.append(entry)
        derivative.pop(order)#Clear last entry b/c x^0 term becomes 0

    #Print Values
    return derivative

def computeIntegral (function):
    #Initial Setup
    order = len(function)-1
    integral = []
    
    #Base Cases
    if order == 0 and function[0] != 0:
        integral.append(function[0])

    #Build Integral List
    else:
        for cnt in range (0, order+1):
            entry = function[cnt] / (order - cnt + 1)
            integral.append(entry)

    integral.append('c')
    printFunc(integral)
    integral[integral.index('c')] = 0
    return integral

def factorLinear (function, root):
    #only 1 case
    val = -1 * function[1]/function[0]
    if abs(val) == 0:#Addressing case of y = x where root = -0.0
        val = 0.0
    root.append(val)
    return root

def factorQuad (function, root):
    #Initial Calculations
    discr = (function[1]**2) - (4 * function[0] * function[2])
    twoA = 2.0*function[0]

    #Evaluations
    if discr >= 0:
        root.append(((-1*function[1])+ (discr**0.5))/twoA)
        root.append(((-1*function[1])- (discr**0.5))/twoA)
        #Will be the same root if discriminant == 0
    else: #If discriminant < 0, complex roots
        real = (-1*function[1])/twoA
        imaginary = abs(((abs(discr))**0.5)/twoA)
        root.append(roundComplex(complex(real,imaginary)))
        root.append(roundComplex(complex(real, -1*imaginary)))
    return root

def newtMethod (function,derivative,start):
    #Base Case
    if derivative == 0: #If function is a horizontal line
        return "no_root" #Shouldnt ever get here though
    if computeFunc(function, 0) == 0: #Initial guess of 0
        return 0
    
    #Setup
    x = start
    derivVal = computeFunc(derivative, x)
    while derivVal == 0: #Ensuring initial guess is valid
        x, y = [float(x) for x in input("Enter 2 numbers seperated by white space\n").split()]
        derivVal = computeFunc(derivative,complex(x,y))

    #Setting & Printing Initial Values
    delta = 1
    cnt = 0
    maxCnt = 1000

    #Computing Final Root
    while (delta > prec) and (cnt <= maxCnt):
        funcVal = computeFunc(function,x)
        derivVal = computeFunc(derivative,x)
        val = x - (funcVal/derivVal)
        cnt += 1
        delta = abs(x - val)
        x = val

    if (delta > prec) and (cnt > maxCnt):
        if start == complex(10,10):
            print("FAILED")
            return "FAILED"
        return newtMethod(function,derivative,complex(10,10))
    
    #Adjusting Complex Numbers, or switching to real where appropriate
    x = roundComplex(x)
    return x

def synthDivide(function, root): 
    #Initial Setup
    newFunction = [function[0]]
    order = len(function)-1

    #Creating simplified function
    for cnt in range (1, order):
        val = roundComplex((root * newFunction[cnt-1]) + function[cnt])
        newFunction.append(val)
    return newFunction

def solveFunc (): #Function to quickly enter and test a function
    printRoot (factor (makeFunc(), []))


def factor (function, root):
    #Initial Setup
    order = len(function)-1
    index = next((i for i, x in enumerate(function) if x != 0), None)#look for first nonzero int
    if index == None:
        print("Function is all zeroes")
        return None

    #Base Cases
    if order - index == 0:#Index to account for extra 0'd terms @ front
        #print("Function is now scalar")
        return root
    elif order - index == 1:
        #print("Function is now linear")
        return factorLinear(function[order-1:], root)
    elif order - index == 2:
        #print("Function is now quadratic")
        return factorQuad(function[order-2:], root)

    #General Cases
    derivative = computeDerivative(function)
    root1 = newtMethod(function,derivative,complex(10,-10))
    if root1 == "FAILED":
        root.append(root1)
        return root
    if root1.imag == 0: #Single real root
        root.append(root1)
        function = synthDivide (function, root[-1])
    else: #2 complex roots
        root2 = cmplxConj(root1)
        root.append(root1)
        root.append(root2)
        function = synthDivide(function, root1)
        function = synthDivide(function, root2)
        
    return factor(function, root)
