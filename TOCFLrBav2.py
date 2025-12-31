# Test of Chinese as a Foreign Language Reading Band A (Vol.2)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images2"

# Question Bank (EXAMPLE)
questions = [
    {
        "id": 1,
        "type": "reading",
        "audio": [],
        "image": '1.png',
        "question": "那杯牛奶被喝了一半。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "C"
    },

    {
        "id": 2,
        "type": "reading",
        "audio": [],
        "image": '2.png',
        "question": "我家一共三口人。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "C"
    },

    {
        "id": 3,
        "type": "reading",
        "audio": [],
        "image": '3.png',
        "question": "樹下一個禮物也沒有。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "B"
    },

    {
        "id": 4,
        "type": "reading",
        "audio": [],
        "image": '4.png',
        "question": "餐廳的樓上有洗手間。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "A"
    },

    {
        "id": 5,
        "type": "reading",
        "audio": [],
        "image": '5.png',
        "question": "沒戴眼鏡的那位先生就是林明華。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "B"
    },

    {
        "id": 6,
        "type": "reading",
        "audio": [],
        "image": '6.png',
        "question": "公車快兩點才來。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "A"
    },

    {
        "id": 7,
        "type": "reading",
        "audio": [],
        "image": '7.png',
        "question": "學生看著黑板上的句子說話。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "C"
    },

    {
        "id": 8,
        "type": "reading",
        "audio": [],
        "image": '8.png',
        "question": "弟弟喜歡用電腦玩遊戲。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "A"
    },

    {
        "id": 9,
        "type": "reading",
        "audio": [],
        "image": '9.png',
        "question": "樓梯上的門不知道被誰打開了。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "C"
    },

    {
        "id": 10,
        "type": "reading",
        "audio": [],
        "image": '10.png',
        "question": "大明受傷了，他現在躺在醫院，不能站也不能坐。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "B"
    },

    {
        "id": 11,
        "type": "reading",
        "audio": [],
        "image": '11.png',
        "question": "哥哥在冰箱旁邊放了一部洗衣機。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "B"
    },

    {
        "id": 12,
        "type": "reading",
        "audio": [],
        "image": '12.png',
        "question": "弟弟不會寫書法 。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "C"
    },

    {
        "id": 13,
        "type": "reading",
        "audio": [],
        "image": '13.png',
        "question": "因為他都把菜吃光了 ，所以已經吃不下了。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "C"
    },

    {
        "id": 14,
        "type": "reading",
        "audio": [],
        "image": '14.png',
        "question": "小文喜歡一邊寫作業，一邊吃東西。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "A"
    },

    {
        "id": 15,
        "type": "reading",
        "audio": [],
        "image": '15.png',
        "question": "小華只有右手受傷，其他地方都沒事。",
        "choices": {
            "A": "",
            "B": "",
            "C": "",
        },
        "answer": "B"
    },

    {
        "id": 16,
        "type": "reading",
        "audio": [],
        "image": '16.png',
        "question": "",
        "choices": {
            "A": "這裡是機場。",
            "B": "火車到車站了。",
            "C": "很多人在等車。",
        },
        "answer": "B"
    },

    {
        "id": 17,
        "type": "reading",
        "audio": [],
        "image": '17.png',
        "question": "",
        "choices": {
            "A": "他們換了新家具。",
            "B": "他們忘了打開窗戶。",
            "C": "他們兩個人搬不了沙發。",
        },
        "answer": "A"
    },

    {
        "id": 18,
        "type": "reading",
        "audio": [],
        "image": '18.png',
        "question": "",
        "choices": {
            "A": "老師準備上課。",
            "B": "學生們正在休息。",
            "C": "教室裡有人在說話。",
        },
        "answer": "A"
    },

    {
        "id": 19,
        "type": "reading",
        "audio": [],
        "image": '19.png',
        "question": "",
        "choices": {
            "A": "郵局在銀行旁邊。",
            "B": "銀行的對面是郵局。",
            "C": "車站在郵局的前面。",
        },
        "answer": "B"
    },

    {
        "id": 20,
        "type": "reading",
        "audio": [],
        "image": '20.png',
        "question": "",
        "choices": {
            "A": "他們點了麵和湯。",
            "B": "他們覺得很傷心。",
            "C": "女生坐在男生的右邊。",
        },
        "answer": "C"
    },

    {
        "id": 21,
        "type": "reading",
        "audio": [],
        "image": '21.png',
        "question": "",
        "choices": {
            "A": "他看不懂這本書。",
            "B": "他覺得這本書很有趣。",
            "C": "他看書的時候很緊張。",
        },
        "answer": "B"
    },

    {
        "id": 22,
        "type": "reading",
        "audio": [],
        "image": '22.png',
        "question": "",
        "choices": {
            "A": "這家飯館中午不休息。",
            "B": "這家飯館最貴的是雞肉飯。",
            "C": "這家飯館十一點以後休息。",
        },
        "answer": "A"
    },

    {
        "id": 23,
        "type": "reading",
        "audio": [],
        "image": '23.png',
        "question": "",
        "choices": {
            "A": "這家店也賣果汁。",
            "B": "這位小姐買了香蕉牛奶。",
            "C": "香蕉牛奶便宜了十塊錢。",
        },
        "answer": "A"
    },

    {
        "id": 24,
        "type": "reading",
        "audio": [],
        "image": '24.png',
        "question": "",
        "choices": {
            "A": "妹妹是十點多離開家的。",
            "B": "妹妹到家的時候快十點了。",
            "C": "妹妹十點的時候就要回家了。",
        },
        "answer": "B"
    },

    {
        "id": 25,
        "type": "reading",
        "audio": [],
        "image": '25.png',
        "question": "",
        "choices": {
            "A": "初級中文課每一次上三個小時。",
            "B": "初級中文課在二○一教室上課。",
            "C": "這個班的學生五月三日不上課。",
        },
        "answer": "C"
    },

    {
        "id": 26,
        "type": "reading",
        "audio": [],
        "image": '26.png',
        "question": "",
        "choices": {
            "A": "病人正在讓醫生檢查。",
            "B": "醫生要病人試著站起來。",
            "C": "護士幫忙看病人哪裡受傷了。",
        },
        "answer": "A"
    },

    {
        "id": 27,
        "type": "reading",
        "audio": [],
        "image": '27.png',
        "question": "",
        "choices": {
            "A": "小華一星期運動四天。",
            "B": "小華只有星期二下午能休息。",
            "C": "小華每星期上兩天的中文課。",
        },
        "answer": "C"
    },

    {
        "id": 28,
        "type": "reading",
        "audio": [],
        "image": '28.png',
        "question": "",
        "choices": {
            "A": "這班公車從火車站出發。",
            "B": "下午五點還有車到博物館。",
            "C": "66號公車每兩個鐘頭一班。",
        },
        "answer": "A"
    },

    {
        "id": 29,
        "type": "reading",
        "audio": [],
        "image": '29.png',
        "question": "",
        "choices": {
            "A": "這間公寓在學校附近。",
            "B": "公寓裡面只有一個房間。",
            "C": "想租這間公寓的人上網找陳先生。",
        },
        "answer": "A"
    },

    {
        "id": 30,
        "type": "reading",
        "audio": [],
        "image": '30.png',
        "question": "",
        "choices": {
            "A": "這個晚會的飲料有三種。",
            "B": "第二次喝飲料不能用新的杯子。",
            "C": "每人只能在晚會裡喝一杯飲料。",
        },
        "answer": "B"
    },

    {
        "id": 31,
        "type": "reading",
        "audio": [],
        "image": '31-35.png',
        "question": "王小姐  ____  旅遊很有興趣。",
        "choices": {
            "A": "跟",
            "B": "和",
            "C": "對",
        },
        "answer": "C"
    },

    {
        "id": 32,
        "type": "reading",
        "audio": [],
        "image": '31-35.png',
        "question": "她放假的時候  _____   出國玩。",
        "choices": {
            "A": "多少",
            "B": "可能",
            "C": "常常",
        },
        "answer": "C"
    },

    {
        "id": 33,
        "type": "reading",
        "audio": [],
        "image": '31-35.png',
        "question": "她跟我說她第一次旅行時，在旅館 ____ 丟了行李。",
        "choices": {
            "A": "做",
            "B": "弄",
            "C": "走",
        },
        "answer": "B"
    },

    {
        "id": 34,
        "type": "reading",
        "audio": [],
        "image": '31-35.png',
        "question": "她緊張 ______ 好幾天， 三天以後才找到行李 。",
        "choices": {
            "A": "著",
            "B": "了",
            "C": "得",
        },
        "answer": "B"
    },

    {
        "id": 35,
        "type": "reading",
        "audio": [],
        "image": '31-35.png',
        "question": "從那一次開始，她旅行的時候就更 _____ 自己的東西 了。",
        "choices": {
            "A": "小心",
            "B": "知道",
            "C": "認識",
        },
        "answer": "A"
    },

    {
        "id": 36,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "我很喜歡到附近一家很大 的 _____ 買菜。",
        "choices": {
            "A": "藥房",
            "B": "書店",
            "C": "超市",
        },
        "answer": "C"
    },

    {
        "id": 37,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "那裡的東西不怎麼便宜， ______  比較新鮮，吃起來很放心。",
        "choices": {
            "A": "但是",
            "B": "或是",
            "C": "還是",
        },
        "answer": "A"
    },

    {
        "id": 38,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "聽說今天八點 那裡有特別活動，所以我早上六點  ____  起床了。",
        "choices": {
            "A": "再",
            "B": "才",
            "C": "就",
        },
        "answer": "C"
    },

    {
        "id": 39,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "到了那裡以後，我買了好多 ____  我愛吃的餅乾 和一些青菜 。",
        "choices": {
            "A": "枝",
            "B": "包",
            "C": "口",
        },
        "answer": "B"
    },

    {
        "id": 40,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "不過 ___ 付錢的人太多了，等的時間比買東西的時間還久。",
        "choices": {
            "A": "掛號",
            "B": "點菜",
            "C": "排隊",
        },
        "answer": "C"
    },

    {
        "id": 41,
        "type": "reading",
        "audio": [],
        "image": '41-45.png',
        "question": "",
        "choices": {
            "A": "買了一間房子",
            "B": "就有一家大醫院",
            "C": "林一正沒花多少錢",
            "D": "林一正花了不少錢",
            "E": "那裡的生活很方便",
            "F": "可以常常帶孩子到公園玩",
        },
        "answer": "A"
    },

    {
        "id": 42,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "不過 ___ 付錢的人太多了，等的時間比買東西的時間還久。",
        "choices": {
            "A": "買了一間房子",
            "B": "就有一家大醫院",
            "C": "林一正沒花多少錢",
            "D": "林一正花了不少錢",
            "E": "那裡的生活很方便",
            "F": "可以常常帶孩子到公園玩",
        },
        "answer": "B"
    },

    {
        "id": 43,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "不過 ___ 付錢的人太多了，等的時間比買東西的時間還久。",
        "choices": {
            "A": "買了一間房子",
            "B": "就有一家大醫院",
            "C": "林一正沒花多少錢",
            "D": "林一正花了不少錢",
            "E": "那裡的生活很方便",
            "F": "可以常常帶孩子到公園玩",
        },
        "answer": "F"
    },

    {
        "id": 44,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "不過 ___ 付錢的人太多了，等的時間比買東西的時間還久。",
        "choices": {
            "A": "買了一間房子",
            "B": "就有一家大醫院",
            "C": "林一正沒花多少錢",
            "D": "林一正花了不少錢",
            "E": "那裡的生活很方便",
            "F": "可以常常帶孩子到公園玩",
        },
        "answer": "D"
    },

    {
        "id": 45,
        "type": "reading",
        "audio": [],
        "image": '36-40.png',
        "question": "不過 ___ 付錢的人太多了，等的時間比買東西的時間還久。",
        "choices": {
            "A": "買了一間房子",
            "B": "就有一家大醫院",
            "C": "林一正沒花多少錢",
            "D": "林一正花了不少錢",
            "E": "那裡的生活很方便",
            "F": "可以常常帶孩子到公園玩",
        },
        "answer": "E"
    },

    {
        "id": 46,
        "type": "reading",
        "audio": [],
        "image": '46.png',
        "question": "明麗最後要說的意思是什麼？",
        "choices": {
            "A": "想太多事情對自己沒用",
            "B": "心情好壞可以自己決定",
            "C": "早睡早起的人一定快樂",
            "D": "生活進步的方法有很多",
        },
        "answer": "B"
    },

    {
        "id": 47,
        "type": "reading",
        "audio": [],
        "image": '47.png',
        "question": "這篇文章在談什麼？",
        "choices": {
            "A": "用家中舊書換新書的方法",
            "B": "上網看書才不會用太多紙",
            "C": "學會賣書可以賺更多的錢",
            "D": "把不要的書變成有用的書",
        },
        "answer": "D"
    },

    {
        "id": 48,
        "type": "reading",
        "audio": [],
        "image": '48.png',
        "question": "從參加比賽到比賽結束，順文是怎麼想的？",
        "choices": {
            "A": "她只想拿第一名",
            "B": "這是一次很好的經驗",
            "C": "成績不好都是因為生病",
            "D": "為了比賽，健康已經不重要",
        },
        "answer": "B"
    },

    {
        "id": 49,
        "type": "reading",
        "audio": [],
        "image": '49.png',
        "question": "作者覺得，為什麼有人會覺得上班時間不夠？",
        "choices": {
            "A": "他們太喜歡找家人、朋友聊天兒",
            "B": "他們常常忘了回重要的電子郵件",
            "C": "他們可能經常工作到一半就得停下來",
            "D": "他們不太常注意自己上、下班的時間",
        },
        "answer": "C"
    },

    {
        "id": 50,
        "type": "reading",
        "audio": [],
        "image": '50.png',
        "question": "老闆聽了同學們最想問的問題以後，他怎麼回答？",
        "choices": {
            "A": "好好學習就可以了",
            "B": "必頇像他一樣努力才行",
            "C": "要知道什麼事情不應該做",
            "D": "得學會馬上聽懂老闆說的話",
        },
        "answer": "A"
    },
]

# IMAGE OPENER
def open_image(img_path: Path):
    if not img_path.exists():
        print(colored(f"[WARN] Missing image: {img_path.name}", "red"))
        return

    system = platform.system()

    try:
        if system == "Darwin":          
            subprocess.run(["open", img_path])
        elif system == "Windows":
            subprocess.run(["start", img_path], shell=True)
        else:                           
            subprocess.run(["xdg-open", img_path])
    except Exception as e:
        print(colored(f"[ERROR] Cannot open image: {e}", "red"))

# EXAM LOOP
score = 0

for q in questions:
    print(colored(f"\nQuestion {q['id']}", "cyan"))

    # ✅ USE THE IMAGE FIELD DIRECTLY
    img_path = IMAGE_DIR / q["image"]

    print(colored(f"[Image] {q['image']}", "yellow"))
    open_image(img_path)

    if q["question"]:
        print(colored("\n" + q["question"], "white"))

    for k, v in q["choices"].items():
        print(f"  ({k}) {v}")

    user_answer = input(colored("\nYour answer: ", "cyan")).strip().upper()

    if user_answer == q["answer"]:
        print(colored("✅ Correct!", "green"))
        score += 1
    else:
        print(colored(f"❌ Wrong — Correct answer: {q['answer']}", "red"))

# FINAL SCORE
print(colored(f"\nFinal Score: {score} / {len(questions)}", "magenta"))