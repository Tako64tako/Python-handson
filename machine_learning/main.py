import pandas as pd
import warnings
warnings.simplefilter('ignore', FutureWarning)


def main():

    get_csv = pd.read_csv("./iris-dataset.csv")
    # TODO: sepal_length, sepal_width, petal_length,petal_widthのそれぞれの平均値を求める
    print(get_csv.mean())

    # TODO: sepal_length, sepal_width, petal_length,petal_widthのそれぞれの中央値を求める
    print(get_csv.median())

    # TODO: sepal_length, sepal_width, petal_length,petal_widthのそれぞれの標準偏差を求める
    print(get_csv.std())

    # TODO: speciesごとにsepal_length, sepal_width, petal_length,petal_widthのそれぞれの平均値を求める
    print(get_csv.groupby("species").mean())

    # TODO: speciesごとにsepal_length, sepal_width, petal_length,petal_widthのそれぞれの中央値を求める
    print(get_csv.groupby("species").median())

    # TODO: speciesごとにsepal_length, sepal_width, petal_length,petal_widthのそれぞれの標準偏差を求める
    print(get_csv.groupby("species").std())


if __name__ == '__main__':
    main()
