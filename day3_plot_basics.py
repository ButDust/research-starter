# day3_plot_basics.py
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
def plot_line():
    x = np.arange(10)
    y = x ** 2
    fig,ax = plt.subplots(figsize=(6,4))
    ax.plot(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Line graph of y = x ^ 2')
    fig.tight_layout()
    fig.savefig('figures/day3_line_plot.png')
    plt.close(fig)
def plot_scatter():
    x = np.random.rand(50) * 100
    y = np.random.rand(50) * 100
    fig,ax = plt.subplots(figsize=(6,4))
    ax.scatter(x,y)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Scatter Plot of 50 Random Points')
    fig.tight_layout()
    fig.savefig('figures/day3_scatter_plot.png')
    plt.close(fig)
def plot_bar():
    names = ["Alice", "Bob", "Cindy", "David", "Eva"]
    scores = [88, 76, 95, 82, 90]
    fig,ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(names, scores)
    ax.bar_label(bars, padding=3)
    ax.set_xlabel('names')
    ax.set_ylabel('scores')
    ax.set_ylim(0,105)
    ax.set_title('Scores of Five Students')
    fig.tight_layout()
    fig.savefig('figures/day3_bar_plot.png')
    plt.close(fig)
def plot_hist():
    fig,ax = plt.subplots(figsize=(6,4))
    x = np.random.randn(1000)
    ax.hist(x) #Histogram shows the distribution of a single variable
    ax.set_xlabel('x')
    ax.set_ylabel('frequency')
    ax.set_title('Hist for 1000 Random Numbers i.i.d Normal Distribution')
    fig.tight_layout()
    fig.savefig('figures/day3_hist_plot.png')
    plt.close(fig)
if __name__ == "__main__":
    plot_line()
    plot_scatter()
    plot_bar()
    plot_hist()