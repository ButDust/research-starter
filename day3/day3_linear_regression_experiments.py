import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

FIGURE_DIR = Path("figures")
FIGURE_DIR.mkdir(exist_ok=True)


def run_experiment(learning_rate, noise_std, num_points, seed, epochs=200):
    np.random.seed(seed)

    true_w = 2.0
    true_b = 3.0

    x = np.linspace(0, 10, num_points)
    noise = np.random.normal(0, noise_std, size=x.shape)
    y = true_w * x + true_b + noise

    w = np.random.randn() * 0.1
    b = np.random.randn() * 0.1
    loss_history = []
    diverged = False

    for _ in range(epochs):
        y_pred = w * x + b
        loss = np.mean((y_pred - y) ** 2)
        loss_history.append(loss)

        if not np.isfinite(loss) or loss > 1e12:
            diverged = True
            break

        grad_w = np.mean(2 * (y_pred - y) * x)
        grad_b = np.mean(2 * (y_pred - y))

        w = w - learning_rate * grad_w
        b = b - learning_rate * grad_b

    final_y_pred = w * x + b
    final_loss = np.mean((final_y_pred - y) ** 2)
    true_line_loss = np.mean((true_w * x + true_b - y) ** 2)

    return {
        "learning_rate": learning_rate,
        "noise_std": noise_std,
        "num_points": num_points,
        "seed": seed,
        "final_w": w,
        "final_b": b,
        "final_loss": final_loss,
        "true_line_loss": true_line_loss,
        "expected_floor": noise_std ** 2,
        "loss_history": loss_history,
        "diverged": diverged,
    }


def plot_learning_rate_comparison():
    learning_rates = [0.001, 0.01, 0.02, 0.05, 0.07, 0.1]

    fig, ax = plt.subplots(figsize=(8, 5))
    print("\nLearning rate comparison")
    print("lr\tfinal_loss\tfinal_w\tfinal_b\tstatus")

    for lr in learning_rates:
        result = run_experiment(lr, noise_std=1.0, num_points=100, seed=42, epochs=200)
        status = "diverged" if result["diverged"] else "ok"

        print(
            f"{lr}\t"
            f"{result['final_loss']:.4f}\t"
            f"{result['final_w']:.4f}\t"
            f"{result['final_b']:.4f}\t"
            f"{status}"
        )

        label = f"lr={lr}" if not result["diverged"] else f"lr={lr} diverged"
        ax.plot(result["loss_history"], label=label)

    ax.set_xlabel("Epoch")
    ax.set_ylabel("MSE Loss")
    ax.set_title("Learning Rate Comparison")
    ax.set_yscale("log")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "day3_lr_comparison.png", dpi=200)
    plt.close(fig)


def plot_noise_comparison():
    noise_stds = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0]
    final_losses = []
    expected_floors = []
    true_line_losses = []

    print("\nNoise comparison")
    print("noise_std\texpected_floor\ttrue_line_loss\tfinal_loss")

    for noise_std in noise_stds:
        result = run_experiment(0.02, noise_std, num_points=100, seed=42, epochs=300)

        final_losses.append(result["final_loss"])
        expected_floors.append(result["expected_floor"])
        true_line_losses.append(result["true_line_loss"])

        print(
            f"{noise_std}\t"
            f"{result['expected_floor']:.4f}\t"
            f"{result['true_line_loss']:.4f}\t"
            f"{result['final_loss']:.4f}"
        )

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(noise_stds, expected_floors, marker="o", label="Expected floor: noise_std^2")
    ax.plot(noise_stds, true_line_losses, marker="o", label="True line loss")
    ax.plot(noise_stds, final_losses, marker="o", label="Learned line loss")
    ax.set_xlabel("Noise std")
    ax.set_ylabel("MSE Loss")
    ax.set_title("Noise Std vs Final Loss")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "day3_noise_comparison.png", dpi=200)
    plt.close(fig)


def plot_sample_size_stability():
    num_points_list = [10, 100, 1000]
    seeds = list(range(50))

    summary = []

    print("\nSample size stability comparison")
    print("num_points\tmean_w\tstd_w\tmean_b\tstd_b\tmean_loss")

    for num_points in num_points_list:
        ws = []
        bs = []
        losses = []

        for seed in seeds:
            result = run_experiment(0.02, noise_std=1.0, num_points=num_points, seed=seed, epochs=300)
            ws.append(result["final_w"])
            bs.append(result["final_b"])
            losses.append(result["final_loss"])

        row = {
            "num_points": num_points,
            "mean_w": np.mean(ws),
            "std_w": np.std(ws),
            "mean_b": np.mean(bs),
            "std_b": np.std(bs),
            "mean_loss": np.mean(losses),
        }
        summary.append(row)

        print(
            f"{num_points}\t"
            f"{row['mean_w']:.4f}\t"
            f"{row['std_w']:.4f}\t"
            f"{row['mean_b']:.4f}\t"
            f"{row['std_b']:.4f}\t"
            f"{row['mean_loss']:.4f}"
        )

    x_positions = np.arange(len(summary))
    x_labels = [str(row["num_points"]) for row in summary]

    mean_ws = [row["mean_w"] for row in summary]
    std_ws = [row["std_w"] for row in summary]
    mean_bs = [row["mean_b"] for row in summary]
    std_bs = [row["std_b"] for row in summary]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.errorbar(x_positions, mean_ws, yerr=std_ws, marker="o", capsize=5, label="learned w")
    ax.errorbar(x_positions, mean_bs, yerr=std_bs, marker="o", capsize=5, label="learned b")
    ax.axhline(2.0, linestyle="--", alpha=0.6, label="true w = 2")
    ax.axhline(3.0, linestyle="--", alpha=0.6, label="true b = 3")
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels)
    ax.set_xlabel("Number of points")
    ax.set_ylabel("Parameter value")
    ax.set_title("Sample Size and Parameter Stability")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "day3_sample_size_stability.png", dpi=200)
    plt.close(fig)


def main():
    plot_learning_rate_comparison()
    plot_noise_comparison()
    plot_sample_size_stability()

    print("\nSaved figures:")
    print(FIGURE_DIR / "day3_lr_comparison.png")
    print(FIGURE_DIR / "day3_noise_comparison.png")
    print(FIGURE_DIR / "day3_sample_size_stability.png")


if __name__ == "__main__":
    main()