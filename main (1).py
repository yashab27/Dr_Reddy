from scipy.optimize import fsolve

# Define the equations
def equations(variables):
    m, k = variables
    eq1 = 0.505 - (0.04665 + 7.19565 + 9.75 + 0.0025 + 4 * 10**-6 * m - k * 23.5)
    eq2 = 0.166 - (0.04665 + 7.19565 + 9.75 + 0.0025 + 1.5 * 10**-6 * m - k * 23.5)
    return [eq1, eq2]

# Initial guesses for m and k
initial_guess = [0, 0]

# Solve the equations
result = fsolve(equations, initial_guess)

# Extract the values of m and k
m_solution, k_solution = result

print("Solution:")
print("m =", m_solution)
print("k =", k_solution)

