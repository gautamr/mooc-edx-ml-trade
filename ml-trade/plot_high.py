"""Plot High prices for RELIANCE"""

import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("../data/RELIANCE.NS.csv")
    # TODO: Your code here
    df['High'].plot()
    plt.show()  # must be called to show plots


if __name__ == "__main__":
    test_run()
