import sympy

def math_solver(expression):
    try:

        expr = sympy.sympify(expression)

        simplified_expr = sympy.simplify(expr)

        explanation = "Step-by-step explanation: \n"

        expanded_expr = sympy.expand(expr)
        explanation += "Expanding the expression: \n"
        explanation += sympy.pretty(expr) + " = " + sympy.pretty(simplified_expr) + "\n\n"

        simplified_expanded_expr = sympy.simplify(expanded_expr)
        explanation += "Simplifying the expanded expression: \n"
        explanation += sympy.pretty(expanded_expr) + " = " + sympy.pretty(simplified_expanded_expr) + "\n\n"

        factored_expr = sympy.factor(expr)
        explanation += "Factoring the expression: \n"
        explanation += sympy.pretty(expr) + " = " + sympy.pretty(factored_expr) + "\n\n"

        evaluated_expr = expr.evalf()
        explanation += "Evaluatiing the expression: \n"
        explanation += sympy.pretty(expr) + " = " + str(evaluated_expr) + "\n\n"

        # result = eval(expression)
        return explanation
    except Exception as e:
        return str(e)

expression = input("Enter a mathematical expression: ")
explanation = math_solver(expression)
# result = math_solver(expression)
print("Explanation:")
print(explanation)