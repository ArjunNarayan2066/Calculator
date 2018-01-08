import Factor_Main as factMain
import NumIntegrate_Main as integMain
import PolyDifferentiation_Main as polydiffMain

def run():
    while True:
        print("\n\nPlease select area of interest")
        print("Factorization (0)\nDefinite Integration (1)\nPolynomial Differentiation (2)")
        val = int(input(""))
        
        if val == 0:
            factMain.run()

        if val == 1:
            integMain.run()

        if val == 2:
            polydiffMain.run()

        #Add more sections in here

        val = input("Restart this section? Y/N\n")
        if val == "N":
            break
