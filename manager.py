import numpy as np

class BanPickManager():
    def __init__(self):
        self.member = np.loadtxt("member.csv", delimiter=',', dtype=str,
                                 encoding='shift_jis')
        self.alpha = []
        self.beta = []

    def choose_up_teams(self):
        num_list = np.asarray([i for i in range(8)])
        np.random.shuffle(num_list)

        for i in range(4):
            self.alpha.append(self.member[num_list[i]])
            self.beta.append(self.member[num_list[i + 4]])

        return self.alpha, self.beta

# デバック
if __name__ == '__main__':
    manager = BanPickManager()
    alpha, beta = manager.choose_up_teams()
    print(alpha)
    print(beta)