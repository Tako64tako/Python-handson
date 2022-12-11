import pandas as pd
import warnings
warnings.simplefilter('ignore', FutureWarning)
# 注意: それぞれの数値は，値のみ取り出し，小数第1位までを指定してください．それ以外の文字列を含めたり，小数指定のミスはテストが失敗します．


def main():

    get_csv = pd.read_csv("./iris-dataset.csv")
    # TODO: sepal_length, sepal_width, petal_length,petal_widthのそれぞれの平均値を求める

    # TODO: sepal_length, sepal_width, petal_length,petal_widthのそれぞれの中央値を求める

    # TODO: sepal_length, sepal_width, petal_length,petal_widthのそれぞれの標準偏差を求める

    # TODO: speciesごとにsepal_length, sepal_width, petal_length,petal_widthのそれぞれの平均値を求める

    # TODO: speciesごとにsepal_length, sepal_width, petal_length,petal_widthのそれぞれの中央値を求める

    # TODO: speciesごとにsepal_length, sepal_width, petal_length,petal_widthのそれぞれの標準偏差を求める


if __name__ == '__main__':
    main()
