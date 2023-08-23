import numpy as np
from scipy.optimize import minimize

# Constants
m = 135599.99999999997
k = 0.02438456093038935
initial_particle_size = 6.5e-6  # micrometers to meters
t = 22.5 + 273.15  # Celsius to Kelvin

# Target d90 range
target_d90_lower = 1.3e-6  # micrometers to meters
target_d90_upper = 1.6e-6  # micrometers to meters

# Objective function to minimize (deviation from target range)
def objective(x):
    bead_size, agitator_speed, flow_rate, batch_size = x
    
    d90 = (0.155 * bead_size) + (0.055 * agitator_speed) + (0.015 * flow_rate) + (0.005 * batch_size) + (m * initial_particle_size) + (-k * (1 + t))
    
    deviation_lower = max(0, target_d90_lower - d90)
    deviation_upper = max(0, d90 - target_d90_upper)
    
    return deviation_lower + deviation_upper

# Initial guess for variables
x0 = np.array([0.3e-6, 130.83, 650 / 60, 500e-6])  # Convert g/min to kg/s, ml to m^3

# Bounds for variables
bounds = [(0.1e-6, 1e-6), (100, 150), (400 / 60, 700 / 60), (100e-6, 600e-6)]  # Bead size, RPM, kg/s, m^3

# Solve the optimization problem
result = minimize(objective, x0, bounds=bounds)

# Print the results
print("Optimal Values:")
print("Bead Size:", result.x[0] * 1e6, "micrometers")
print("Agitator Speed:", result.x[1], "RPM")
print("Flow Rate:", result.x[2] * 60, "g/min")
print("Batch Size:", result.x[3] * 1e6, "ml")
print("Final d90:", (0.155 * result.x[0]) + (0.055 * result.x[1]) + (0.015 * result.x[2]) + (0.005 * result.x[3]) + (m * initial_particle_size) + (-k * (1 + t)) * 1e6, "micrometers")


