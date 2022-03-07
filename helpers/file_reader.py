import pandas as pd


def read_data_from_file(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print("Sorry, unable to read from{}".format(filename))
        exit(1)

