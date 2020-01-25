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
        self.seleced_stage = None

        # self.alpha = []
        # self.beta = []

        # self.game_flag = False
        # self.banpick_flag = False

        self.ab_list = ["α","β","α","β",
                        "α","β","β","α",
                        "β","α","β","α",
                        "β","α","α","β"]
        self.ban_pick = ["バン", "ピック"]
        # self.count = 0
        # self.ban_list = {"α":[], "β":[]}
        # self.pick_list = {"α": [], "β": []}

        self._reset()

    def _reset(self):
        self.alpha = []
        self.beta = []

        self.game_flag = False
        self.banpick_flag = False

        self.count = 0
        self.ban_list = {"α": [], "β": []}
        self.pick_list = {"α": [], "β": []}

        self.last_msg = ""

        if not self.seleced_stage:
            self.stages.append(self.seleced_stage)

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

            self.last_msg += msg

            self.banpick_flag = True
            msg += "バンピックを開始します\n"
            msg += "\n"

        if content == "リセット":

            msg = "リセットします"
            self._reset()
            return msg

        if not self.banpick_flag:
            return "不正な入力です"

        if self.count > 0:
            self.register(content, self.count-1)

        if self.count%4 == 0 and self.count < 16:
            if self.count > 0:
                msg += self.output_weapons_name()

            msg += self.make_massage(self.count)
            msg += "\n\n"

        if self.count >= 16:
            msg += "全てのバンピックが終わりました。ゲームスタートです!\n\n"
            msg += self.last_msg + self.output_weapons_name()
            self._reset()

            return msg
        else:
            msg += "{}チーム、{}するブキを選んでください".format(
                    self.ab_list[self.count], self.ban_pick[self.count//4%2]
                )

        self.count += 1

        return msg

    def output_weapons_name(self):

        msg = ""

        msg += "バンしたブキ\n"
        msg += "αチーム:{}\n".format(list_to_str(self.ban_list["α"]))
        msg += "βチーム:{}\n".format(list_to_str(self.ban_list["β"]))
        msg += "ピックしたブキ\n"
        msg += "αチーム:{}\n".format(list_to_str(self.pick_list["α"]))
        msg += "βチーム:{}\n".format(list_to_str(self.pick_list["β"]))

        msg += "\n"

        return msg

    def register(self, weapon, num):
        if self.ban_pick[num//4%2] == "バン":
            self.ban_list[self.ab_list[num]].append(weapon)
        else:
            self.pick_list[self.ab_list[num]].append(weapon)

    def make_massage(self, num):
        # バンピックの順番を指示するメッセージを生成
        msg = ''
        for i in range(4):
            msg += self.ab_list[num + i]
            # msg += ban_pick[num//4]
            if i != 3:
                msg += "→"

        return "{}の順で{}していきます".format(msg, self.ban_pick[num//4%2])

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

        self.seleced_stage = self.stages.pop(np.random.randint(len(self.stages)))
        return "ステージ : {}".format(self.seleced_stage)

# デバック
if __name__ == '__main__':
    manager = BanPickManager()
    # alpha, beta = manager.choose_up_teams()
    # print(alpha)
    # print(beta)
    # print(manager.choose_and_lost_stage())
    print(manager.make_massage(0))