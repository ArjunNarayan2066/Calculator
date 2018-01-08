import arithmeticMain as arMain
import functionMain as funMain

def runMain():
    while True:
        print("Please select area of interest")
        print("Arithmetic (0)\nFunctions & Calculus (1)")
        val = int(input(""))
        
        if val == 0:
            arMain.run()

        if val == 1:
            funMain.run()

        #Add more sections in here

        val = input("Restart Calculator? Y/N\n")
        if val == "N":
            break
    return

if __name__ == '__main__':
    runMain()
