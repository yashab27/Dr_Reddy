from scipy.optimize import minimize
import numpy as np

# Given data
m = 135600.0000000009
k = 0.7247744680851065
t = 22.5 + 273.15  # Kelvin
viscosity = 200 * 10**-3  # mPa.s to Pa.s

# Target particle sizes
target_sizes = {
    "d10": (0.16 + 0.18) / 2,
    "d50": (0.5 + 0.7) / 2,
    "d90": (1.3 + 1.6) / 2
}

# Objective function to minimize the sum of squared differences between achieved and target sizes
def objective_function(params):
    bead_size, agitator_speed, flow_rate, batch_size = params
    d10 = (0.155 * bead_size) + (0.055 * agitator_speed) + (0.015 * flow_rate) + (0.005 * batch_size) + (-k * viscosity * (1 + t)) + (m * 1.5 * 10**-6)
    d50 = (0.155 * bead_size) + (0.055 * agitator_speed) + (0.015 * flow_rate) + (0.005 * batch_size) + (-k * viscosity * (1 + t)) + (m * 3.5 * 10**-6)
    d90 = (0.155 * bead_size) + (0.055 * agitator_speed) + (0.015 * flow_rate) + (0.005 * batch_size) + (-k * viscosity * (1 + t)) + (m * 8 * 10**-6)
    diff = [
        (d10 - target_sizes["d10"])**2,
        (d50 - target_sizes["d50"])**2,
        (d90 - target_sizes["d90"])**2
    ]
    return np.sum(diff)

# Initial guesses for parameters
initial_guess = [0.4, 1250*2*np.pi/60, 250/60/1000, 16*10**-3]

# Bounds for parameters
bounds = [(0.1, 1), (1000*2*np.pi/60, 1500*2*np.pi/60), (50/60/1000, 500/60/1000), (10*10**-3, 20*10**-3)]

# Minimize the objective function
result = minimize(objective_function, initial_guess, bounds=bounds)

# Extract optimized parameters
opt_bead_size, opt_agitator_speed, opt_flow_rate, opt_batch_size = result.x

print("Optimized Operating Conditions for Slurry B:")
print("Optimized Bead Size:", opt_bead_size, "mm")
print("Optimized Agitator Speed:", opt_agitator_speed * 60 / (2 * np.pi), "RPM")
print("Optimized Flow Rate:", opt_flow_rate * 60 * 1000, "g/min")
print("Optimized Batch Size:", opt_batch_size * 1000, "mL")


