import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("inputs/out.csv")
    df = df[df.Time != 0]
    ax = df.plot.bar(x='Name', y='Time', rot=0)
    fig = ax.get_figure()
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    fig.savefig('outputs/times.png', dpi=200)


main()
