# day3_data_generation.py
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
def generate_linear_data():
    x = np.linspace(0,10,100)
    noise = np.random.normal(0,1.0,size=x.shape)
    y = 2 * x + 3 + noise
    print("x shape:",x.shape)
    print("y shape:",y.shape)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    print("x mean:",x_mean)
    print("y mean:",y_mean)
    noise_std = np.std(noise)
    print("noise std:",noise_std)
    fig,ax = plt.subplots()
    ax.scatter(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Scatter Plot Of y = 2 * x + 3 + noise')
    true_y = 2 * x + 3
    ax.plot(x, true_y, color="red", label="True line: y = 2x + 3")
    ax.legend()
    fig.savefig('figures/day3_linear_data.png',dpi = 200)
    plt.close(fig)

if __name__ == "__main__":
    generate_linear_data()