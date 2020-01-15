import numpy as np

all_stage = ["バッテラ", "フジツボ", "ガンガゼ", "コンブ", "アマビ",
           "チョウザメ", "タチウオ", "ホッケ", "マンタ", "モズク",
           "エンガワ", "Bバス", "ザトウ", "ハコフグ", "デボン", "アロワナ",
           "アジフライ", "ショッツル", "モンガラ", "スメーシー", "オートロ",
           "ムツゴ"]

def list_to_str(list):
    msg = ""
    for i in list:
        msg += i
        if i != list[-1]:
            msg += ", "

    return msg

class BanPickManager():
    def __init__(self):
        self.member = np.loadtxt("member.csv", delimiter=',', dtype=str,
                                 encoding='shift_jis')
        self.stages = all_stage
        self.alpha = []
        self.beta = []

        self.game_flag = False
        self.banpick_flag = False

        self.ab_list = ["α","β","α","β",
                        "α","β","β","α",
                        "β","α","β","α",
                        "β","α","α","β"]
        self.ban_pick = ["バン", "ピック"]
        self.count = 0

    def controller(self, content):

        commnand = ["スタート"]

        msg = ""

        if content == "スタート" and not self.banpick_flag:
            # msg = "ゲームスタート!\n\n"

            # 初期設定
            msg += self.choose_up_teams()
            msg += "\n"
            msg += self.choose_and_lost_stage()
            msg += "\n\n"

            self.banpick_flag = True
            msg += "バンピックを開始します\n"
            msg += "\n"

        if self.count%4 == 0:
            msg += self.make_massage(self.count)
            msg += "\n\n"


        msg += "{}チーム、{}するブキを選んでください".format(
                self.ab_list[self.count], self.ban_pick[self.count//4]
            )

        self.count += 1

        return msg

    def banpick(self, weapon=None):
        pass

    def make_massage(self, num):
        # バンピックの順番を指示するメッセージを生成
        msg = ''
        for i in range(4):
            msg += self.ab_list[i]
            # msg += ban_pick[num//4]
            if i != 3:
                msg += "→"

        return "{}の順で{}していきます".format(msg, self.ban_pick[num//4])

    def choose_up_teams(self):
        num_list = np.asarray([i for i in range(8)])
        np.random.shuffle(num_list)

        for i in range(4):
            self.alpha.append(self.member[num_list[i]])
            self.beta.append(self.member[num_list[i + 4]])

        # return self.alpha, self.beta
        return "αチーム:{}\nβチーム:{}".format(
            list_to_str(self.alpha), list_to_str(self.beta))

    def choose_and_lost_stage(self):

        # return self.stages.pop(np.random.randint(len(self.stages)))

        stage = self.stages.pop(np.random.randint(len(self.stages)))
        return "ステージ : {}".format(stage)

# デバック
if __name__ == '__main__':
    manager = BanPickManager()
    # alpha, beta = manager.choose_up_teams()
    # print(alpha)
    # print(beta)
    # print(manager.choose_and_lost_stage())
    print(manager.make_massage(0))