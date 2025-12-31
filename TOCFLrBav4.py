# Test of Chinese as a Foreign Language Reading Band A (Vol.4)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image_ba_vol4"

# Question Bank (EXAMPLE)
questions = [
    {
  "id": 1,
  "type": "reading",
  "audio": [],
  "image": '1.png',
  "question": "   ",
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
  "question": "他們    喝酒。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "B"
},

{
  "id": 3,
  "type": "reading",
  "audio": [],
  "image": '3.png',
  "question": "餐桌上有     。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "C"
},

{
  "id": 4,
  "type": "reading",
  "audio": [],
  "image": '4.png',
  "question": "這家餐廳有     人。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "B"
},

{
  "id": 5,
  "type": "reading",
  "audio": [],
  "image": '5.png',
  "question": "",
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
  "question": "王先生今天沒有帶鑰匙。",
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
  "question": "他們一起看一本書。",
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
  "question": "爸爸拿了一半的蛋糕給小明。",
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
  "question": "他總是一個人運動，不和大家一起玩。",
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
  "question": "警察站在他的車子旁邊和他說話。",
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
  "question": "小美買了外套，又買了皮包，一共付了兩千元。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "A"
},

{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '12.png',
  "question": "愛美已經和爸爸差不多高了 ，但是還沒爸爸高。",
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
  "question": "昨天下午來看病的病人，大人跟小孩一樣多。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "B"
},

{
  "id": 14,
  "type": "reading",
  "audio": [],
  "image": '14.png',
  "question": "校長要學生在家 裡吃飽以後，再 上學。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "C"
},

{
  "id": 15,
  "type": "reading",
  "audio": [],
  "image": '15.png',
  "question": "車子不動了，車上的人 馬上下車檢查。",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
  },
  "answer": "A"
},

{
  "id": 16,
  "type": "reading",
  "audio": [],
  "image": '16.png',
  "question": "",
  "choices": {
    "A": "她的頭髮很 長。",
    "B": "她的裙子很短。",
    "C": "她正拿著盤子 。",
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
    "A": "這位先生正在收傳真。",
    "B": "這位先生已經很累了。",
    "C": "桌上什麼東西都沒有。",
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
    "A": "林先生手上 沒有東西 。",
    "B": "林先生吃完了所有食物。",
    "C": "林先生現在覺得很開心。",
  },
  "answer": "C"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '19.png',
  "question": "",
  "choices": {
    "A": "這裡幾乎坐滿了學生。",
    "B": "這些學生正在慶祝開學。",
    "C": "他們幾個人就要畢業了。",
  },
  "answer": "C"
},

{
  "id": 20,
  "type": "reading",
  "audio": [],
  "image": '20.png',
  "question": "",
  "choices": {
    "A": "大家正在慶祝中國新年。",
    "B": "小朋友們手上拿著糖果。",
    "C": "大人們正在請客人吃飯。",
  },
  "answer": "A"
},

{
  "id": 21,
  "type": "reading",
  "audio": [],
  "image": '21.png',
  "question": "",
  "choices": {
    "A": "雪已經停了。",
    "B": "小男孩沒戴帽子。",
    "C": "小朋友們正在玩。",
  },
  "answer": "C"
},

{
  "id": 22,
  "type": "reading",
  "audio": [],
  "image": '22.png',
  "question": "",
  "choices": {
    "A": "這裡有山還有樹。",
    "B": "房子前面的湖 很髒。",
    "C": "在湖的旁邊有好幾間房子。",
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
    "A": "這位先生正在照相。",
    "B": "這裡很熱鬧，人很多。",
    "C": "這位小姐正在和警察說話。",
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
    "A": "學生們都在上課。",
    "B": "女學生在黑板上畫畫。",
    "C": "有一個學生手裡拿著電腦。",
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
    "A": "一杯飲料 40元。",
    "B": "一盤水餃 50元。",
    "C": "一顆包子 60元。",
  },
  "answer": "B"
},

{
  "id": 26,
  "type": "reading",
  "audio": [],
  "image": '26.png',
  "question": "",
  "choices": {
    "A": "這個活動能換到水果。",
    "B": "這個活動從中午開始。",
    "C": "活動的時間有一個禮拜。",
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
    "A": "日和大學全校停水兩天。",
    "B": "女生宿舍一共停水十二小時。",
    "C": "男生宿舍比女生宿舍早一天停水。",
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
    "A": "參加活動就送機票。",
    "B": "這個活動 只有一個月 。",
    "C": "住兩個晚上都不用錢。",
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
    "A": "早上有車從奮起湖到火車站 。",
    "B": "嘉義高鐵站沒有車到奮起湖。",
    "C": "從奮起湖出發，只能到火車站。",
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
    "A": "半年房租給 10000元。",
    "B": "半年房租給 30000元。",
    "C": "半年房租給 60000元。",
  },
  "answer": "C"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "臺灣東部有一種特別的 魚，會       海裡飛到水上 。",
  "choices": {
    "A": "從",
    "B": "往",
    "C": "來",
  },
  "answer": "A"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "這裡的魚有男人魚、女人魚和老人魚三       。",
  "choices": {
    "A": "班",
    "B": "位",
    "C": "種",
  },
  "answer": "C"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "這種魚       年春天最多，男人 們會一起搭船去 海上找魚。",
  "choices": {
    "A": "第",
    "B": "每",
    "C": "幾",
  },
  "answer": "B"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "魚是這裡很重要的食物 ，這裡的大人小孩      需要它。",
  "choices": {
    "A": "都",
    "B": "不",
    "C": "本來",
  },
  "answer": "A"
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "很多住在別的地方的人，春天放假的 會來這裡旅遊。",
  "choices": {
    "A": "問題",
    "B": "時候",
    "C": "消息",
  },
  "answer": "B"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "也找到工作",
    "B": "才找到工作",
    "C": "越來越多的人",
    "D": "離開學校以後",
    "E": "很多人找不到工作",
    "F": "一家電腦公司找到工作",
  },
  "answer": "F"
},
{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "也找到工作",
    "B": "才找到工作",
    "C": "越來越多的人",
    "D": "離開學校以後",
    "E": "很多人找不到工作",
    "F": "一家電腦公司找到工作",
  },
  "answer": "D"
},
{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "也找到工作",
    "B": "才找到工作",
    "C": "越來越多的人",
    "D": "離開學校以後",
    "E": "很多人找不到工作",
    "F": "一家電腦公司找到工作",
  },
  "answer": "B"
},
{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "也找到工作",
    "B": "才找到工作",
    "C": "越來越多的人",
    "D": "離開學校以後",
    "E": "很多人找不到工作",
    "F": "一家電腦公司找到工作",
  },
  "answer": "E"
},
{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "也找到工作",
    "B": "才找到工作",
    "C": "越來越多的人",
    "D": "離開學校以後",
    "E": "很多人找不到工作",
    "F": "一家電腦公司找到工作",
  },
  "answer": "C"
},

{
  "id": 41,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "玩得很開心",
    "B": "覺得很無聊",
    "C": "一件麻煩的事",
    "D": "玩的東西很有趣",
    "E": "不停地找新遊戲",
    "F": "在旁邊和他一起玩",
  },
  "answer": "A"
},
{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "玩得很開心",
    "B": "覺得很無聊",
    "C": "一件麻煩的事",
    "D": "玩的東西很有趣",
    "E": "不停地找新遊戲",
    "F": "在旁邊和他一起玩",
  },
  "answer": "B"
},
{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "玩得很開心",
    "B": "覺得很無聊",
    "C": "一件麻煩的事",
    "D": "玩的東西很有趣",
    "E": "不停地找新遊戲",
    "F": "在旁邊和他一起玩",
  },
  "answer": "E"
},
{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "玩得很開心",
    "B": "覺得很無聊",
    "C": "一件麻煩的事",
    "D": "玩的東西很有趣",
    "E": "不停地找新遊戲",
    "F": "在旁邊和他一起玩",
  },
  "answer": "C"
},
{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "",
  "choices": {
    "A": "玩得很開心",
    "B": "覺得很無聊",
    "C": "一件麻煩的事",
    "D": "玩的東西很有趣",
    "E": "不停地找新遊戲",
    "F": "在旁邊和他一起玩",
  },
  "answer": "F"
},

{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": '46.png',
  "question": "這段短文寫了什麼？",
  "choices": {
    "A": "味道",
    "B": "顏色",
    "C": "聲音",
    "D": "溫度",
  },
  "answer": "B"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": '47.png',
  "question": "這段短文討論 了哪方面的事 ？",
  "choices": {
    "A": "小孩學這麼多東西的原因",
    "B": "學校為什麼放暑假的原因",
    "C": "小孩學習管理時間的原因",
    "D": "爸媽要小孩讀大學的原因",
  },
  "answer": "A"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": '48.png',
  "question": "這段短文提到「這個地方」的什麼？",
  "choices": {
    "A": "這裡的天氣",
    "B": "生活的習慣",
    "C": "這地方的名字",
    "D": "男人比女人多",
  },
  "answer": "A"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": '49.png',
  "question": "這個故事裡的弟弟不願意做什麼事？",
  "choices": {
    "A": "去河邊騎腳踏車",
    "B": "打掃自己的房間",
    "C": "照顧生病的姊姊",
    "D": "在家裡休息一天",
  },
  "answer": "B"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": '50.png',
  "question": "這段短文要人們做什麼事？",
  "choices": {
    "A": "要大家關心家人",
    "B": "要大家參觀風景",
    "C": "請大家打掃環境",
    "D": "請大家參加活動",
  },
  "answer": "D"
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