import function_operations as f_o

def run(): #Main Function
    print("\n")
    function = f_o.makeFunc()
    root = f_o.factor(function, [])
    print("\n\nRoots = ")
    f_o.printRoot(root)
    restart = input("Please press SPACE to restart\n")
    if restart == " ":
        run()
    return
