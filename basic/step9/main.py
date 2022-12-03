class Player:
    def walk(self):
        print("勇者は荒野を歩いていた")

    def attack(self, enemy):
        print("勇者は" + enemy + "を攻撃した")

def main():
    ## TODO: Playerクラスのインスタンスを作成してください
    walk()
    attack("スライム")

if __name__ == '__main__':
    main()