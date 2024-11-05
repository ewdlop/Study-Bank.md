import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Generate predictor variable X
n_samples = 100
X = np.random.rand(n_samples, 1) * 10  # Random values between 0 and 10

# Step 2: Define the true relationship
true_slope = 2.0
true_intercept = 5.0
Y_true = true_slope * X + true_intercept

# Step 3: Add noise to achieve desired R²
# Calculate the variance of Y_true
variance_Y_true = np.var(Y_true)

# Desired R² value
desired_r2 = 0.13

# Calculate the required noise variance
noise_variance = variance_Y_true * (1 - desired_r2) / desired_r2
noise_std_dev = np.sqrt(noise_variance)

# Generate noise
noise = np.random.normal(0, noise_std_dev, size=Y_true.shape)

# Create the observed Y by adding noise to Y_true
Y_observed = Y_true + noise

# Fit a linear regression model
model = LinearRegression()
model.fit(X, Y_observed)
Y_pred = model.predict(X)

# Calculate the R² value
calculated_r2 = r2_score(Y_observed, Y_pred)

# Plot the data and the fitted line
plt.scatter(X, Y_observed, label='Observed Data')
plt.plot(X, Y_pred, color='red', label='Fitted Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title(f'Linear Regression Fit (R² = {calculated_r2:.2f})')
plt.legend()
plt.show()

print(f'Calculated R²: {calculated_r2:.2f}')
