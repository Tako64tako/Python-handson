# Step3
# AさんのBMIを計算して小数第二位を四捨五入してから出力するプログラムを作成してください．
# BMIの計算方法は、体重(kg)を身長(m)の2乗で割ったものです．

def main():
    # ここに書いてね
    height = 1.7
    width = 60

    bmi = width / (height ** 2)
    print(round(bmi, 1))
if __name__ == '__main__':
    main()