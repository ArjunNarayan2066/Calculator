import math
open_brackets = ["(","[","{"]
close_brackets = [")","]","}"]
operators = ['**','/','*','+','-']
numbers = [str(i) for i in range(10)] + ["."]
invalid_char = open_brackets + close_brackets + operators + ["."]

def replace(r_list, val, start, end):
    #deletes entry @ end as well
    r_list[start] = val
    for i in range (end - start):
        r_list.pop(start+1)
    return r_list

def simple(question):
    print("Question = " + str(question))
    if question[1] == "/":
        if question[2] == 0:
            print("Division by 0")
        return question[0] / question[2]
    elif question [1] == "**":
        return question[0] ** question[2]
    elif question[1] == "*":
        return question[0] * question[2]
    elif question[1] == "//":
        if question[2] == 0:
            print("Division by 0")
        return question[0] // question[2]
    elif question[1] == "%":
        if question[2] == 0:
            print("Division by 0")
        return question[0] % question[2]
    elif question[1] == "+":
        return question[0] + question[2]
    elif question[1] == "-":
        return question[0] - question[2]
    else:
        return question[1]


def bedmas(q_list):
    queue = []
    cnt = 0
    ans = 0
    print("bedmas q = %s" % q_list)
    locations = [[i, q_list[i]] for i in range (len(q_list)) if q_list[i] in operators]
    
    print(locations)
    if len(locations) == 1:
        return simple (q_list)
    
    for op in operators:
        print("Evaluating %s operations" % op)
        i = 0
        while i < len(locations):
            print("i = %d" % i)
            if locations[i][1] == op: #Checks that operator is of correct type
                #First, find indices of operands
                print("Found operator @ entry %d at question index %d" % (i, locations[i][0]))
                q_left = 0 
                q_right = len(q_list) - 1
                if i != 0:
                    print("Adjusting start")
                    q_left = locations[i][0]-1
                if i != len(locations) - 1:
                    print("Adjusting finish")
                    q_right = locations[i][0]+1
                    
                print("Start = %d and end = %d" % (q_left, q_right))
                print("SubQuestion = ")
                print(q_list[q_left:q_right+1])
                ans = simple(q_list[q_left:q_right+1])
                print("ans = %f" % ans)
                q_list = replace(q_list, ans, q_left, q_right)
                locations.pop(i)
                for j in range (i, len(locations)):
                    locations[j][0] -= (q_right - q_left)
                print("New locations = ")
                print(locations)
                #print("len = %d and i = %d " % (len(locations), i))
                print("New Bedmas Question = ")
                print(q_list)
            else:
                i += 1
    print("Bedmas answer = %f" % ans)
    return ans

def create_list (question):
    q_list = []
    sci_not = []
    cnt = 0
    while cnt < len(question):
        if question[cnt] in open_brackets or question[cnt] in close_brackets:
            q_list.append(question[cnt])
            print("Pushing %s at index %d" % (question[cnt], cnt))
            
        elif question[cnt] in operators:
            q_list.append (question[cnt])          
            print("Pushing %s at index %d" % (question[cnt], cnt))

                
        elif question[cnt] in numbers:
            q_start = cnt
            while question[cnt] in numbers or question[cnt] == "E" or (question[cnt-1] == "E" and (question[cnt] == "-" or question[cnt] == "+")):
                cnt += 1
            val = float(question[q_start:cnt])
            q_list.append(float(val))
            print("Pushing %s at index %d" % (val, cnt))
            cnt -= 1
            
        else:
            print("Invalid Entry Err 3\nError with entry %s at index %d" % (question[cnt], cnt))
            return None
        
        cnt += 1
    """    
    if sci_not != []:
        print("Question has %d E's" % len(sci_not))
        print(sci_not)
        num = 0
        for j in sci_not:
            coeff = q_list[j-1]
            if q_list[j+1] == "-":
                num = coeff * (10 ** (-1*q_list[j+2]))
                q_list = replace(q_list, num, j-1,j+2)
            else:
                num = coeff * (10 ** q_list[j+1])
                q_list = replace(q_list, num, j-1, j+1)  
    """           
    return q_list

    
                
def normal():
    print("Using A + B = C structure")
    print("Have fun")

    ans = 0

    while True:
        cnt = 0
        stack = []
        
        question = "(" + input("\n\n") + ")"

        if question[0] in operators: #cannot start with an operator
            print("Invalid Entry Err 1")
            return

        if "ans" in question: #Insert answer into question
            question = question.replace("ans", str(ans))
        if "pi" in question:
            question = question.replace("pi", str(math.pi))
        if "e" in question:
            question = question.replace("e", str(math.e))

        print("Q = ")
        print(question)

        q_list = create_list(question)
        print("List Q = ")
        print(q_list)
        print(len(q_list))
        print(q_list[1] in numbers)
        
        if len(q_list) == 3 and str(q_list[1]) not in invalid_char:
            ans = q_list[1]
        
        while len(q_list) > 3:
            if q_list[cnt] in open_brackets:
                print("Pushing bracket %s at index %d" % (question[cnt], cnt))
                stack.append([cnt, q_list[cnt]])

            elif (q_list[cnt] in close_brackets):
                if (close_brackets.index(q_list[cnt]) != open_brackets.index(stack[-1][1])):
                    print("Invalid Entry Err 2")
                    return
                
                print("Stack = ")
                print(stack)
                q_start = stack[-1][0]#Indexes of enclosing brackets
                q_end = cnt
                print(question[q_start+1:q_end])
                ans = bedmas (q_list[q_start+1:q_end]) #Sent as list implementation, not string
                print("List now = %s " % q_list)
                q_list = replace(q_list, ans, q_start, cnt)        
                stack.pop()
                print("New question = %s" % (question))
                cnt -= (q_end - q_start)
            cnt += 1
            
        print("Out of loop, answer = %f" % ans)
        print(ans)     

def run():
    #typeCalc = input("RPN? Y/N\n")

    #if typeCalc == "Y":
        #pass
        #rpn()
        
    #else:
    normal()

    restart = input("Would you like to restart? Y/N")

    if restart == "Y":
        run()

    return

run()
