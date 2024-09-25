import numpy as np

# Define sample points
x = np.linspace(0, 1, 11)

# Function and polynomial definitions
f_x = np.sin(x)

# Polynomial coefficients
coefficients = [
    6.634227807451e-7,
    0.999972866447809748,
    0.00026102328996568210,
    -0.1676482142361025559,
    0.00164224875473932754,
    0.00724316117958325683,
]

# Compute polynomial values
p_x = (
    coefficients[0]
    + coefficients[1] * x
    + coefficients[2] * x**2
    + coefficients[3] * x**3
    + coefficients[4] * x**4
    + coefficients[5] * x**5
)

# Compute the cosine similarity
cos_similarity = np.dot(f_x, p_x) / (np.linalg.norm(f_x) * np.linalg.norm(p_x))

# Calculate the angle in radians
theta = np.arccos(cos_similarity)

# Print the angle in scientific notation
print(f"Angle θ: {theta:.7e} radians")
