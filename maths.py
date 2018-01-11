import random
import operator

ops = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.div
}

def generate_math_problem():
    operators = ["*","+","-","/"]
    number_1 = random.randint(-15,15)
    number_2 = random.randint(-15,15)
    operator = random.choice(operators)
    print_math_problem(number_1,operator,number_2)

#show problem generated to user and prompt for the solution
def print_math_problem(number_1, operator, number_2):
    #re-generate if denominator is zero
    if operator == "/" and number_2 == "0":
        generate_math_problem()
    global attempts
    attempts+=1
    problem = str(number_1)+" "+operator+" "+str(number_2)+" = ?"
    print problem
    answer = raw_input("Solution: ")
    solution = solve_math_problem(number_1, operator, number_2)
    if validate_answer(answer):
        determine_results(number_1, operator, number_2, answer, solution)
    else:
        append_to_list(number_1, operator, number_2, "invalid response", solution)
        handle_next_step()

def solve_math_problem(number_1, operator, number_2):
    #calculate and format solution
    solution = round(ops[operator](float(number_1), int(number_2)), 2)
    if operator != "/":
        solution = int(solution)
    return solution

def validate_answer(answer):
    try:
        float(answer)
    except ValueError:
        print "Invalid input - this is not a number"
        return False
    return True

def determine_results(number_1, operator, number_2, answer, solution):
    #determine if user entered correct solution
    if solution == float(answer):
        global correct
        correct+=1
        print "You got it right!"
        handle_next_step()
    else:
        print "Not quite! The correct answer was " + str(solution)
        append_to_list(number_1, operator, number_2, answer, solution)
        handle_next_step()

#compile list of incorrectly answered problems
def append_to_list(number_1, operator, number_2, answer, solution):
    global incorrect_solutions
    incorrect_solutions.append(str(number_1)+operator+str(number_2)+"="+str(solution)+" (You answered: "+str(answer)+")")

def handle_next_step():
    response = raw_input("Do you want another problem? ")
    acceptable = ["y","Y"]
    if response[0] in acceptable:
        generate_math_problem()
    else:
        system_exit()

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

attempts = 0
correct = 0
incorrect_solutions = []

generate_math_problem()