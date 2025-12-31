# Test of Chinese as a Foreign Language Reading Band A (Vol.3)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image_ba_vol3"

# Question Bank (EXAMPLE)
questions = [
    {
  "id": 1,
  "type": "reading",
  "audio": [],
  "image": '1.png',
  "question": "   ",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 2,
  "type": "reading",
  "audio": [],
  "image": '2.png',
  "question": "他們    喝酒。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 3,
  "type": "reading",
  "audio": [],
  "image": '3.png',
  "question": "餐桌上有     。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 4,
  "type": "reading",
  "audio": [],
  "image": '4.png',
  "question": "這家餐廳有     人。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 5,
  "type": "reading",
  "audio": [],
  "image": '5.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 6,
  "type": "reading",
  "audio": [],
  "image": '6.png',
  "question": "房間的門跟窗戶都是關著 的。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 7,
  "type": "reading",
  "audio": [],
  "image": '7.png',
  "question": "大明昨天很晚睡覺，因為電影太好看了。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 8,
  "type": "reading",
  "audio": [],
  "image": '8.png',
  "question": "經過兩個路口以後，就會看見公園旁邊的車站。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 9,
  "type": "reading",
  "audio": [],
  "image": '9.png',
  "question": "她已經寫完作業，正在聽音樂。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 10,
  "type": "reading",
  "audio": [],
  "image": '10.png',
  "question": "他看書看得太累了，所以躺在床上就睡著了。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 11,
  "type": "reading",
  "audio": [],
  "image": '11.png',
  "question": "他們都先穿襪子，再穿褲子。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '12.png',
  "question": "媽媽每天七點起床，但是 今天比較晚。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 13,
  "type": "reading",
  "audio": [],
  "image": '13.png',
  "question": "他的車子壞了 ，所以今天坐計程車上班。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 14,
  "type": "reading",
  "audio": [],
  "image": '14.png',
  "question": "她用電腦練習寫字。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 15,
  "type": "reading",
  "audio": [],
  "image": '15.png',
  "question": "很多人正在排隊掛號。",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
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
    "A": "外面出太陽。",
    "B": "他們在看電視。",
    "C": "水果放在椅子上。",
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
    "A": "弟弟的眼鏡壞了 。",
    "B": "弟弟找不到眼鏡 。",
    "C": "弟弟戴著眼鏡睡覺。",
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
    "A": "這裡是機場 。",
    "B": "有位女生在打球 。",
    "C": "小男孩正在騎腳踏車。",
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
    "A": "小華有三天語法課 。",
    "B": "小華星期三上音樂課 。",
    "C": "小華星期二會用電腦。",
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
    "A": "美美要大華帶禮物來 。",
    "B": "美美要請小芳到餐廳吃飯 。",
    "C": "小芳請大華一起到美美的家。",
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
    "A": "全票比半票貴兩百元 。",
    "B": "晚上八點可以看電影 。",
    "C": "中午以前的電影有兩場。",
  },
  "answer": "A"
},

{
  "id": 22,
  "type": "reading",
  "audio": [],
  "image": '22.png',
  "question": "",
  "choices": {
    "A": "星期一可能 要帶雨傘 。",
    "B": "星期二天氣可能不好 。",
    "C": "星期二比星期一涼快。",
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
    "A": "大家都吃完飯了 。",
    "B": "全部的人都拿著杯子 。",
    "C": "四個人坐在圓桌前面。",
  },
  "answer": "B"
},

{
  "id": 24,
  "type": "reading",
  "audio": [],
  "image": '24.png',
  "question": "",
  "choices": {
    "A": "每個人都戴著帽子 。",
    "B": "大家都在唱歌和跳舞 。",
    "C": "蛋糕旁邊有一些禮物。",
  },
  "answer": "C"
},

{
  "id": 25,
  "type": "reading",
  "audio": [],
  "image": '25.png',
  "question": "",
  "choices": {
    "A": "她只用一條腿站著 。",
    "B": "她的手放在身體前面 。",
    "C": "她戴著一頂漂亮的帽子。",
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
    "A": "來這家公司只能租一種車 。",
    "B": "想搭計程車可以打電話給這家公司 。",
    "C": "租車的價格，一天最少一千二百元。",
  },
  "answer": "C"
},

{
  "id": 27,
  "type": "reading",
  "audio": [],
  "image": '27.png',
  "question": "",
  "choices": {
    "A": "醫院離他最遠 。",
    "B": "今天商店都開門 。",
    "C": "公車站在飲料店前面。",
  },
  "answer": "A"
},

{
  "id": 28,
  "type": "reading",
  "audio": [],
  "image": '28.png',
  "question": "",
  "choices": {
    "A": "林心心跟王老師學中文 。",
    "B": "卡片是王老師寫給林心心的 。",
    "C": "他們約好還要再上三個月的課。",
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
    "A": "十月只有兩間房間比較便宜 。",
    "B": "十月五日住兩人房可以得到禮物 。",
    "C": "來來旅館每個月都有特別的活動 。",
  },
  "answer": "B"
},

{
  "id": 30,
  "type": "reading",
  "audio": [],
  "image": '30.png',
  "question": "",
  "choices": {
    "A": "去這家店喝紅茶，就送早餐 。",
    "B": "在這家店吃早餐，就送一杯飲料 。",
    "C": "這家店早上七點關門，下午兩點開門。",
  },
  "answer": "B"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "屋子裡一個人         沒有。",
  "choices": {
    "A": "就",
    "B": "也",
    "C": "些",
  },
  "answer": "B"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "花瓶裡         很多漂亮的花 。",
  "choices": {
    "A": "有",
    "B": "掛",
    "C": "換",
  },
  "answer": "A"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "小狗在桌子下睡得很         。",
  "choices": {
    "A": "隨便",
    "B": "方便",
    "C": "舒服",
  },
  "answer": "C"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "兩隻貓一起在沙發         玩兒。",
  "choices": {
    "A": "上面",
    "B": "下面",
    "C": "裡面",
  },
  "answer": "A"
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '31-35.png',
  "question": "王先生一家人一個小時後         回來。",
  "choices": {
    "A": "再",
    "B": "才",
    "C": "常",
  },
  "answer": "B"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": "36-40.png",
  "question": "",
  "choices": {
    "A": "一雙手套",
    "B": "外面很漂亮",
    "C": "買完東西以後",
    "D": "買完東西以前",
    "E": "什麼東西都有",
    "F": "樓下的餐廳吃晚餐",
  },
  "answer": "B"
},

{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": "36-40.png",
  "question": "",
  "choices": {
    "A": "一雙手套",
    "B": "外面很漂亮",
    "C": "買完東西以後",
    "D": "買完東西以前",
    "E": "什麼東西都有",
    "F": "樓下的餐廳吃晚餐",
  },
  "answer": "E"
},

{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": "36-40.png",
  "question": "",
  "choices": {
    "A": "一雙手套",
    "B": "外面很漂亮",
    "C": "買完東西以後",
    "D": "買完東西以前",
    "E": "什麼東西都有",
    "F": "樓下的餐廳吃晚餐",
  },
  "answer": "A"
},

{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": "36-40.png",
  "question": "",
  "choices": {
    "A": "一雙手套",
    "B": "外面很漂亮",
    "C": "買完東西以後",
    "D": "買完東西以前",
    "E": "什麼東西都有",
    "F": "樓下的餐廳吃晚餐",
  },
  "answer": "C"
},

{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": "36-40.png",
  "question": "",
  "choices": {
    "A": "一雙手套",
    "B": "外面很漂亮",
    "C": "買完東西以後",
    "D": "買完東西以前",
    "E": "什麼東西都有",
    "F": "樓下的餐廳吃晚餐",
  },
  "answer": "F"
},

{
  "id": 41,
  "type": "reading",
  "audio": [],
  "image": "41-45.png",
  "question": "",
  "choices": {
    "A": "我最喜歡的",
    "B": "我還是願意",
    "C": "那就更好了",
    "D": "心情總是特別好",
    "E": "心情總是特別壞",
    "F": "有很多工作經驗",
  },
  "answer": "F"
},
{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": "41-45.png",
  "question": "",
  "choices": {
    "A": "我最喜歡的",
    "B": "我還是願意",
    "C": "那就更好了",
    "D": "心情總是特別好",
    "E": "心情總是特別壞",
    "F": "有很多工作經驗",
  },
  "answer": "A"
},
{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": "41-45.png",
  "question": "",
  "choices": {
    "A": "我最喜歡的",
    "B": "我還是願意",
    "C": "那就更好了",
    "D": "心情總是特別好",
    "E": "心情總是特別壞",
    "F": "有很多工作經驗",
  },
  "answer": "D"
},
{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": "41-45.png",
  "question": "",
  "choices": {
    "A": "我最喜歡的",
    "B": "我還是願意",
    "C": "那就更好了",
    "D": "心情總是特別好",
    "E": "心情總是特別壞",
    "F": "有很多工作經驗",
  },
  "answer": "C"
},
{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": "41-45.png",
  "question": "",
  "choices": {
    "A": "我最喜歡的",
    "B": "我還是願意",
    "C": "那就更好了",
    "D": "心情總是特別好",
    "E": "心情總是特別壞",
    "F": "有很多工作經驗",
  },
  "answer": "B"
},

{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": '46.png',
  "question": "小明把信寄出去以後，會發生什麼事 ？",
  "choices": {
    "A": "（A）王伯伯收到兩封信",
    "B": "（B）李伯伯收到兩封信",
    "C": "（C）李伯伯要到王伯伯家拿信",
    "D": "（D）王伯伯和李伯伯都沒收到信",
  },
  "answer": "B"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": '47.png',
  "question": "寫這段短文的人覺得上網買東西怎麼樣 ？",
  "choices": {
    "A": "（A）可以少花一些錢",
    "B": "（B）容易買太多東西",
    "C": "（C）能買到最流行的衣服",
    "D": "（D）不像大家說的那麼方便",
  },
  "answer": "B"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": '48.png',
  "question": "寫這段話的人說了什麼 ？",
  "choices": {
    "A": "（A）他一道臺灣菜也不會做",
    "B": "（B）陳媽媽和他一樣不吃苦瓜",
    "C": "（C）他發現苦瓜在臺灣是一種藥",
    "D": "（D）他的好朋友玉芳也不喜歡苦瓜",
  },
  "answer": "D"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": '49.png',
  "question": "這段短文說了什麼事 ？",
  "choices": {
    "A": "（A）陳先生每天幾點起床",
    "B": "（B）李先生的數學不太好",
    "C": "（C）陳先生沒有李先生忙",
    "D": "（D）李先生不相信陳先生",
  },
  "answer": "D"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": '50.png',
  "question": "這家網路廚房公司有什麼服務 ？",
  "choices": {
    "A": "（A）出租廚房給學生用",
    "B": "（B）請媽媽們教學生做菜",
    "C": "（C）幫學生把家人煮的菜送到學校",
    "D": "（D）讓不太會煮菜的人吃到好吃的菜",
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