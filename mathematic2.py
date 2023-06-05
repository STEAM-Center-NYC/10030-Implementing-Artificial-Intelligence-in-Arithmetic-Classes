import sympy

def math_solver(expression):
    try:

        expr = sympy.sympify(expression)

        solution_steps = sympy.solve(expr)

        explanation = "Step-by-step explanation: \n"

        for i, step in enumerate(solution_steps):
            explanation += "Step " + str(i+1) + ": \n"
            explanation += "To solve " + sympy.pretty(expr) + " = O, \n"
            explanation += "We apply the following operation(s):\n"

            if isinstance(step, sympy.Eq):
                explanation += " - Equaiton: " + sympy.pretty(step.lhs) + " = " + sympy.pretty(step.rhs) + "\n"
            
            elif isinstance(step, sympy.Symbol):
                explanation += " - Variable: " + sympy.pretty(step) + "\n"
            
            elif isinstance(step, sympy.Basic):
                explanation += " - Operation: " + sympy.pretty(step) + "\n"

            explanation += "\n"
        
        return explanation
    except Exception as e:
        return str(e)
    

expression = input("Enter a mathematical expression: ")
explanation = math_solver(expression)
print("Explanation:")
print(explanation)