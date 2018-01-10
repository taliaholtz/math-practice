import random

def system_exit():
    global correct
    global attempts
    global incorrect_solutions
    success_rate = correct*100/attempts
    print "You got " + str(success_rate) + "% correct!"
    if success_rate < 100:
        print "These are the problems you got wrong:"
        for item in incorrect_solutions:
            print item

def handle_next_step():
    response = raw_input("Do you want another problem?")
    acceptable = ["y","Y"]
    if response[0] in acceptable:
        generate_math_problem()
    else:
        system_exit()

def append_to_list(number_1, operator, number_2, answer, solution):
    global incorrect_solutions
    incorrect_solutions.append(str(number_1)+operator+str(number_2)+"="+str(solution)+" (You answered: "+answer+")")


def solve_math_problem(number_1, operator, number_2, answer):
    #handle operator
    if operator == "*":
        solution = number_1*number_2
    elif operator == "+":
        solution = number_1+number_2
    elif operator == "-":
        solution = number_1-number_2
    #determine if user entered correct solution
    if solution == int(answer):
        global correct
        correct+=1
        print "You got it right!"
        handle_next_step()
    else:
        print "Not quite! The correct answer was " + str(solution)
        append_to_list(number_1, operator, number_2, answer, solution)
        handle_next_step()

        
def print_math_problem(number_1, operator, number_2):
    problem = str(number_1)+operator+str(number_2)+"=?"
    print problem
    answer = raw_input("Solution:")
    #check input is valid number
    try:
        float(answer)
    except ValueError:
        print "Invalid input - this is not a number"
        handle_next_step()
    solve_math_problem(number_1, operator, number_2, answer)

def generate_math_problem():
    global attempts
    attempts+=1
    operators = ["*","+","-"]
    number_1 = random.randint(0,50)
    number_2 = random.randint(0,50)
    operator = random.choice(operators)
    print_math_problem(number_1,operator,number_2)

attempts = 0
correct = 0
incorrect_solutions = []

generate_math_problem()