# day4_pytorch_linear_regression_manual.py
import torch
import matplotlib.pyplot as plt
def pytorch_linear_regression_manual():
    torch.manual_seed(42)
    x = torch.linspace(0,10,100).reshape(-1,1)
    noise = torch.randn_like(x) * 1.0
    y = 2 * x + 3 + noise
    print(f"x shape: {x.shape}")  # torch.Size([100, 1])
    print(f"y shape: {y.shape}")  # torch.Size([100, 1])
    w = torch.randn(1, requires_grad=True)
    b = torch.randn(1, requires_grad=True)
    learning_rate = 0.01
    epochs = 2000
    loss_history = []
    for epoch in range(epochs):
        y_pred = w * x + b
        loss = torch.mean((y_pred - y) ** 2)
        loss.backward()
        with torch.no_grad():           # update parameters
            w -= learning_rate * w.grad
            b -= learning_rate * b.grad
        w.grad.zero_()
        b.grad.zero_()
        loss_history.append(loss.item())    # loss is a tensor, while loss.item() is a floating number
        if epoch % 20 == 0:
            print(f"Epoch {epoch:4d} | Loss: {loss.item():.6f} | w: {w.item():.6f} | b: {b.item():.6f}")
    print("Final Loss:",loss.item())
    print("Final w:",w.item())
    print("Final b:",b.item())
    # forward -> loss -> backward -> update -> zerograd
    fig,ax = plt.subplots(figsize=(6,4))
    ax.plot(loss_history)
    ax.set_xlabel('Epoch')
    ax.set_ylabel('Loss')
    ax.set_title('Training Loss Curve (Manual Update)')
    fig.tight_layout()
    fig.savefig('figures/day4_manual_loss_curve.png')
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x.numpy(), y.numpy(), alpha=0.6, label="Data points")

    with torch.no_grad():
        y_fit = w * x + b

    ax.plot(
        x.numpy(),
        y_fit.numpy(),
        "r-",
        linewidth=2,
        label=f"Fit: y = {w.item():.3f}x + {b.item():.3f}",
    )

    y_true = 2 * x + 3
    ax.plot(x.numpy(), y_true.numpy(), "g--", linewidth=2, label="True: y = 2x + 3")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Linear Regression Fit Result (Manual Update)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("figures/day4_manual_fit_result.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    pytorch_linear_regression_manual()