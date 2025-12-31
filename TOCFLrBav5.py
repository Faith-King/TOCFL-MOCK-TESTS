# Test of Chinese as a Foreign Language Reading Band A (Vol.5)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image_ba_vol5"

# Question Bank (EXAMPLE)
questions = [
    {
  "id": 1,
  "type": "reading",
  "audio": [],
  "image": '1.png',
  "question": "小王和朋友們一起在游泳池游泳。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "A"
},

{
  "id": 2,
  "type": "reading",
  "audio": [],
  "image": '2.png',
  "question": "他喜歡在吃飯的時候看雜誌。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "A"
},

{
  "id": 3,
  "type": "reading",
  "audio": [],
  "image": '3.png',
  "question": "咖啡店裡一個客人也沒有。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "A"
},

{
  "id": 4,
  "type": "reading",
  "audio": [],
  "image": '4.png',
  "question": "小明自己騎機車去市場，幫媽媽買菜。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "C"
},

{
  "id": 5,
  "type": "reading",
  "audio": [],
  "image": '5.png',
  "question": "他平常吃完晚餐後喜歡到公園散步。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "A"
},

{
  "id": 6,
  "type": "reading",
  "audio": [],
  "image": '6.png',
  "question": "醫生正在病房裡和病人說話。",
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
  "question": "下大雨了，所以很多人都在買雨衣。",
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
  "question": "今天天氣很冷，小月不只穿長褲，還穿了外套。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "B"
},

{
  "id": 9,
  "type": "reading",
  "audio": [],
  "image": '9.png',
  "question": "小明比妹妹高，也比爸爸高。",
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
  "question": "到第二個路口以前，會先經過一家銀行。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "C"
},

{
  "id": 11,
  "type": "reading",
  "audio": [],
  "image": '11.png',
  "question": "小美想要一雙鞋子，但是收到了一雙襪子。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "C"
},

{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '12.png',
  "question": "爸爸使用信用卡買了一台照相機。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "A"
},

{
  "id": 13,
  "type": "reading",
  "audio": [],
  "image": '13.png',
  "question": "這些家具都壞了。",
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
  "question": "同學們都在教室裡做作業，所以很安靜。",
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
  "question": "如果你常常看新聞節目，就能知道很多新消息。",
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
    "A": "教室裡有四位學生。",
    "B": "教室裡面有三位老師。",
    "C": "林老師正在上中文課。",
  },
  "answer": "C"
},

{
  "id": 17,
  "type": "reading",
  "audio": [],
  "image": '17.png',
  "question": "",
  "choices": {
    "A": "這裡一共有六個人。",
    "B": "他們又吃菜又喝飲料。",
    "C": "所有的人都正用著筷子。",
  },
  "answer": "B"
},

{
  "id": 18,
  "type": "reading",
  "audio": [],
  "image": '18.png',
  "question": "",
  "choices": {
    "A": "女孩站在草地上。",
    "B": "地上有一個袋子。",
    "C": "男孩們正在踢足球。",
  },
  "answer": "B"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '19.png',
  "question": "",
  "choices": {
    "A": "他把椅子搬出去。",
    "B": "他把椅子搬進房間來。",
    "C": "他把椅子放在窗戶下面。",
  },
  "answer": "A"
},

{
  "id": 20,
  "type": "reading",
  "audio": [],
  "image": '20.png',
  "question": "",
  "choices": {
    "A": "孩子在玩水。",
    "B": "媽媽在弄衣服。",
    "C": "爸爸在打掃家裡。",
  },
  "answer": "B"
},

{
  "id": 21,
  "type": "reading",
  "audio": [],
  "image": '21.png',
  "question": "",
  "choices": {
    "A": "要先煮菜再放鹽。",
    "B": "做這道菜用不了多少時間。",
    "C": "這個方法教你怎麼烤青菜。",
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
    "A": "誰都可以進去這間圖書館。",
    "B": "圖書館中午休息一個小時。",
    "C": "只有一個月可以進去圖書館。",
  },
  "answer": "B"
},

{
  "id": 23,
  "type": "reading",
  "audio": [],
  "image": '23.png',
  "question": "",
  "choices": {
    "A": "白小姐要找一間好學校。",
    "B": "白小姐想和小美一塊兒住。",
    "C": "從白小姐家到市場很方便。",
  },
  "answer": "C"
},

{
  "id": 24,
  "type": "reading",
  "audio": [],
  "image": '24.png',
  "question": "",
  "choices": {
    "A": "李大明留言給王華。",
    "B": "王華中午要去開會。",
    "C": "王華打電話給李大明。",
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
    "A": "拿書時要先給錢。",
    "B": "陳小姐買了一些書。",
    "C": "林先生把書寄出去了。",
  },
  "answer": "A"
},

{
  "id": 26,
  "type": "reading",
  "audio": [],
  "image": '26.png',
  "question": "",
  "choices": {
    "A": "王明下午在辦公室。",
    "B": "王明的媽媽在醫院。",
    "C": "王明已經下班回家。",
  },
  "answer": "B"
},

{
  "id": 27,
  "type": "reading",
  "audio": [],
  "image": '27.png',
  "question": "",
  "choices": {
    "A": "警察要大家看清楚紅綠燈。",
    "B": "警察要大家騎車戴著安全帽。",
    "C": "警察要大家不只晚上騎車開燈。",
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
    "A": "每個人坐車都需要付錢 。",
    "B": "十月十日坐車不用買車票 。",
    "C": "國家生日那天沒有公車服務 。",
  },
  "answer": "B"
},

{
  "id": 29,
  "type": "reading",
  "audio": [],
  "image": '29.png',
  "question": "",
  "choices": {
    "A": "中午以後才有車子到舊城 。",
    "B": "可以搭 34號火車到舊城去 。",
    "C": "只有下午才有到新城的火車 。",
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
    "A": "這裡的服務員每天都要上班 。",
    "B": "經驗多的人可以拿比較多的錢 。",
    "C": "有興趣的人可以給陳先生打電話 。",
  },
  "answer": "B"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "冬天快到了，小王想買一______黑色大衣。",
  "choices": {
    "A": "付",
    "B": "件",
    "C": "條",
  },
  "answer": "B"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "小李今天有時間，所以下午和小王______去商店買衣服。",
  "choices": {
    "A": "剛才",
    "B": "一起",
    "C": "經常",
  },
  "answer": "B"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "小王看到很多好看的大衣，他每一件______想買。",
  "choices": {
    "A": "都",
    "B": "快",
    "C": "先",
  },
  "answer": "A"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "這些大衣太貴了，______便宜一點，小王就一定會買。",
  "choices": {
    "A": "或是",
    "B": "不但",
    "C": "要是",
  },
  "answer": "C"
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "他們______了一個下午還沒______到想要的衣服，下次再買吧。",
  "choices": {
    "A": "撿…撿…",
    "B": "找…找…",
    "C": "收…收…",
  },
  "answer": "B"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": '36-40.png',
  "question": "星期日下午，書店裡的人______多。",
  "choices": {
    "A": "非常",
    "B": "正在",
    "C": "一點",
  },
  "answer": "A"
},

{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": '36-40.png',
  "question": "要開學了，很多書都在特價。字典現在______賣三百五十元。",
  "choices": {
    "A": "每",
    "B": "最",
    "C": "只",
  },
  "answer": "C"
},

{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": '36-40.png',
  "question": "買兩本書比較便宜，______五百元。",
  "choices": {
    "A": "總是",
    "B": "一共",
    "C": "只好",
  },
  "answer": "B"
},

{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": '36-40.png',
  "question": "因為這裡的書都不貴，______人很多 。",
  "choices": {
    "A": "雖然",
    "B": "所以",
    "C": "可是",
  },
  "answer": "B"
},

{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": '36-40.png',
  "question": "",
  "choices": {
    "A": "賣",
    "B": "付",
    "C": "買",
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
    "A": "想他的爸爸",
    "B": "請大家幫忙",
    "C": "不認識的人",
    "D": "兩人都很高興",
    "E": "他不想去找王明",
    "F": "他一直在找王明",
  },
  "answer": "C"
},
{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": '41-45.png',
  "question": "",
  "choices": {
    "A": "想他的爸爸",
    "B": "請大家幫忙",
    "C": "不認識的人",
    "D": "兩人都很高興",
    "E": "他不想去找王明",
    "F": "他一直在找王明",
  },
  "answer": "C"
},
{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": '41-45.png',
  "question": "",
  "choices": {
    "A": "想他的爸爸",
    "B": "請大家幫忙",
    "C": "不認識的人",
    "D": "兩人都很高興",
    "E": "他不想去找王明",
    "F": "他一直在找王明",
  },
  "answer": "C"
},
{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": '41-45.png',
  "question": "",
  "choices": {
    "A": "想他的爸爸",
    "B": "請大家幫忙",
    "C": "不認識的人",
    "D": "兩人都很高興",
    "E": "他不想去找王明",
    "F": "他一直在找王明",
  },
  "answer": "C"
},
{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": '41-45.png',
  "question": "",
  "choices": {
    "A": "想他的爸爸",
    "B": "請大家幫忙",
    "C": "不認識的人",
    "D": "兩人都很高興",
    "E": "他不想去找王明",
    "F": "他一直在找王明",
  },
  "answer": "C"
},


{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": '46.png',
  "question": "為什麼小明不去參加舞會？",
  "choices": {
    "A": "因為他生病了",
    "B": "（B）因為他想要休息",
    "C": "（C）因為他得去工作",
    "D": "（D）因為他喜歡在家看書",
  },
  "answer": "B"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": '47.png',
  "question": "為什麼小 王覺得考試可能考不好 ？",
  "choices": {
    "A": "他本來成績就不好",
    "B": "（B）他的身體還沒恢復",
    "C": "（C）他準備得還不夠好",
    "D": "（D）他聽說考試非常難",
  },
  "answer": "C"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": '48.png',
  "question": "這篇文章告訴我們什麼事？",
  "choices": {
    "A": "小美現在在臺灣",
    "B": "（B）小華三月要去日本",
    "C": "（C）小美很想吃好吃的點心",
    "D": "（D）小華暑假的時候要去找小美",
  },
  "answer": "D"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": '49.png',
  "question": "為什麼小月決定買那條白色的裙子？",
  "choices": {
    "A": "因為小月只喜歡白色的裙子",
    "B": "因為那條裙子的價格太便宜了",
    "C": "因為以後就買不到那條裙子了",
    "D": "因為小月的媽媽要她買那條裙子",
  },
  "answer": "C"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": '50.png',
  "question": "大同為什麼不常回家呢？",
  "choices": {
    "A": "他的事情很多",
    "B": "他沒有錢回家",
    "C": "他跟家人的關係不好",
    "D": "他覺得南部東西很貴",
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