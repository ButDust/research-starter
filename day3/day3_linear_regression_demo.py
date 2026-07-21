# day3_linear_regression_demo.py
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
noise = np.random.normal(0, 1, size=x.shape)
true_w = 2.0
true_b = 3.0
y = true_w * x + true_b + noise

# Initialization
w = np.random.randn() * 0.1 # Small random number
b = np.random.randn() * 0.1
learning_rate = 0.017
epochs = 200
loss_history = []

for epoch in range(epochs):
    # Forward propagation: Input → Compute → Output (forward flow)
    y_pred = w * x + b
    loss = np.mean((y_pred - y)**2)
    loss_history.append(loss)
    # Calculate gradients
    grad_w = np.mean(2 * (y_pred - y) * x)
    grad_b = np.mean(2 * (y_pred - y))
    # Update parameters
    w = w - learning_rate * grad_w
    b = b - learning_rate * grad_b
    if epoch % 10 == 0:
        print(f"Epoch {epoch}: loss={loss:.4f}, w={w:.4f}, b={b:.4f}")

print(f"\nFinal w: {w:.4f}")
print(f"Final b: {b:.4f}")
print(f"Final loss: {loss:.4f}")
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(loss_history)
ax.set_xlabel("Epoch")
ax.set_ylabel("MSE Loss")
ax.set_title("Training Loss Curve")
fig.tight_layout()
fig.savefig("figures/day3_loss_curve.png", dpi=200)
plt.close(fig)

final_y_pred = w * x + b

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x, y, label="Data")
ax.plot(x, true_w * x + true_b, color="green", label="True line")
ax.plot(x, final_y_pred, color="red", label="Learned line")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Linear Regression Fit Result")
ax.legend()
fig.tight_layout()
fig.savefig("figures/day3_fit_result.png", dpi=200)
plt.close(fig)

# By only changing the value of learning_rate(noise_std fixed to 1.0), it was found that when learning_rate is 0.017, the final loss reaches its minimum value. 
# However, the final loss cannot be reduced to 0. 
# This is because the MSE is approximately equal to mean(noise²), which is about 1, and this is consistent with our final experimental data.

