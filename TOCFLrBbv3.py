# Test of Chinese as a Foreign Language Reading Band B (Vol.3)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image_bb_vol3"

# Question Bank (EXAMPLE)
questions = [
    {
  "id": 1,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "（A）開",
    "B": "（B）查",
    "C": "（C）看",
    "D": "（D）遇",
  },
  "answer": "C"
},

{
  "id": 2,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "（A）中",
    "B": "（B）上",
    "C": "（C）前",
    "D": "（D）後",
  },
  "answer": "C"
},

{
  "id": 3,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "（A）頁",
    "B": "（B）張",
    "C": "（C）份",
    "D": "（D）片",
  },
  "answer": "B"
},

{
  "id": 4,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "（A）寫著",
    "B": "（B）說過",
    "C": "（C）讀著",
    "D": "（D）念過",
  },
  "answer": "A"
},

{
  "id": 5,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "（A）對",
    "B": "（B）要",
    "C": "（C）給",
    "D": "（D）向",
  },
  "answer": "C"
},

{
  "id": 6,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "（A）讓",
    "B": "（B）把",
    "C": "（C）被",
    "D": "（D）為",
  },
  "answer": "A"
},

{
  "id": 7,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "最好",
    "B": "不能",
    "C": "還是",
    "D": "沒空",
  },
  "answer": "B"
},

{
  "id": 8,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "從",
    "B": "比",
    "C": "離",
    "D": "往",
  },
  "answer": "B"
},

{
  "id": 9,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "滿意",
    "B": "容易",
    "C": "放心",
    "D": "方便",
  },
  "answer": "D"
},

{
  "id": 10,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "然後",
    "B": "後來",
    "C": "以後",
    "D": "結果",
  },
  "answer": "D"
},

{
  "id": 11,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "第",
    "B": "頭",
    "C": "先",
    "D": "早",
  },
  "answer": "B"
},

{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "計畫",
    "B": "忘記",
    "C": "安排",
    "D": "要求",
  },
  "answer": "B"
},

{
  "id": 13,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "卻",
    "B": "又",
    "C": "但是",
    "D": "不但",
  },
  "answer": "C"
},

{
  "id": 14,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "客氣",
    "B": "自由",
    "C": "感謝",
    "D": "高興",
  },
  "answer": "C"
},

{
  "id": 15,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "會",
    "B": "可以",
    "C": "不必",
    "D": "不該",
  },
  "answer": "B"
},
{
  "id": 16,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "要是",
    "B": "所以",
    "C": "可能",
    "D": "不管",
  },
  "answer": "B"
},

{
  "id": 18,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "還",
    "B": "才",
    "C": "再",
    "D": "就",
  },
  "answer": "D"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "抬",
    "B": "抽",
    "C": "扔",
    "D": "提",
  },
  "answer": "D"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '19.png',
  "question": "安安要從台北坐火車去台中，他和朋友約十點三十分在台中站見面，他應該坐幾點的火車，才不會太早到或遲到？",
  "choices": {
    "A": "早上六點四分",
    "B": "早上七點五十五分",
    "C": "早上八點三十七分",
    "D": "早上十點三十一分",
  },
  "answer": "B"
},

{
  "id": 20,
  "type": "reading",
  "audio": [],
  "image": '20-21.png',
  "question": "根據廣告內容，下面哪一個 不對？",
  "choices": {
    "A": "要和別人共用浴室",
    "B": "套房附近交通方便",
    "C": "房間裡沒有洗衣機",
    "D": "8000 元不包括水、電費",
  },
  "answer": "A"
},

{
  "id": 21,
  "type": "reading",
  "audio": [],
  "image": '20-21.png',
  "question": "這間套房的房東能接受下面哪個 房客？",
  "choices": {
    "A": "陳先生夫婦",
    "B": "未婚的林小姐",
    "C": "吳小姐和她的女兒",
    "D": "李先生和他的女朋友",
  },
  "answer": "B"
},

{
  "id": 22,
  "type": "reading",
  "audio": [],
  "image": '22-23.png',
  "question": "要怎麼開始使用這部機器 ？",
  "choices": {
    "A": "先按「開始」",
    "B": "先按號碼「 1」",
    "C": "先按著「 0」兩秒",
    "D": "先輸入數字「 157」",
  },
  "answer": "D"
},

{
  "id": 23,
  "type": "reading",
  "audio": [],
  "image": '22-23.png',
  "question": "使用這部機器的時候要注意什麼事 ？",
  "choices": {
    "A": "最多只能借五天",
    "B": "別把機器掛在身上",
    "C": "不能讓帅稚園的孩子用",
    "D": "假日借用時間到下午五點",
  },
  "answer": "C"
},

{
  "id": 24,
  "type": "reading",
  "audio": [],
  "image": '24-25.png',
  "question": "根據這個調查結果，下面哪一項是 錯的？",
  "choices": {
    "A": "賺多少錢是選擇工作時最重要的因素",
    "B": "重視工作是否讓人心情愉快的人 占五分之一",
    "C": "在工作上是否受到尊敬是最不被重視的條件之一",
    "D": "認為工作性質最好跟自己的專業有關的人不到五分之一",
  },
  "answer": "A"
},

{
  "id": 25,
  "type": "reading",
  "audio": [],
  "image": '24-25.png',
  "question": "根據這個調查結果 ，下面哪一項因素被最多年輕人視為理想工作",
  "choices": {
    "A": "收入是否合理",
    "B": "自己的能力是否被肯定",
    "C": "自己所學是否與工作內容有關",
    "D": "是否可以同時扮演好職員和父母的角色",
  },
  "answer": "B"
},

{
  "id": 26,
  "type": "reading",
  "audio": [],
  "image": '26-27.png',
  "question": "關於這家報社的報紙，下面哪一個是對的？",
  "choices": {
    "A": "春節期間不出版",
    "B": "帄時售價一份 10 元",
    "C": "帄時每份數量有三大張",
    "D": "春節時在指定商店才買得到",
  },
  "answer": "D"
},

{
  "id": 27,
  "type": "reading",
  "audio": [],
  "image": '26-27.png',
  "question": "這家報社在春節期間打算 做什麼？",
  "choices": {
    "A": "免費贈送報紙",
    "B": "暫時停止送報五天",
    "C": "補送報紙給已經訂報紙的人",
    "D": "到便利商店買報紙就能得到兌換券",
  },
  "answer": "B"
},

{
  "id": 28,
  "type": "reading",
  "audio": [],
  "image": '28-30.png',
  "question": "文章中提到的實驗是怎麼進行的？",
  "choices": {
    "A": "用儀器讓嬰兒說話",
    "B": "每天讓嬰兒聽同樣的音樂",
    "C": "讓懷孕的母親每天反覆聽單字",
    "D": "嬰兒出生後，每天播放一個單字",
  },
  "answer": "C"
},

{
  "id": 29,
  "type": "reading",
  "audio": [],
  "image": '28-30.png',
  "question": "根據文章，下面哪一 項是對的？",
  "choices": {
    "A": "越早學習語言，記憶力越好",
    "B": "母親看連續劇，嬰兒比較聰明",
    "C": "這項研究結果跟以前的互相矛盾",
    "D": "語言專家寇兒對研究結果感到驚訝",
  },
  "answer": "D"
},

{
  "id": 30,
  "type": "reading",
  "audio": [],
  "image": '28-30.png',
  "question": "這篇短文屬於以下哪一類的研究？",
  "choices": {
    "A": "人類的早期教育",
    "B": "聽力障礙的症狀",
    "C": "音樂對人的影響",
    "D": "懷孕期間的變化",
  },
  "answer": "A"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '31-33.png',
  "question": "這篇短文主要想傳達什麼思想？",
  "choices": {
    "A": "看電影和聽故事都不必太認真",
    "B": "人們應該完全像小孩一樣活著",
    "C": "成長過程中要保持單純不容易",
    "D": "既然長大就應該提早面對現實",
  },
  "answer": "C"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '31-33.png',
  "question": "請問下面哪一段文字最符合第二段中所說的「主題」？",
  "choices": {
    "A": "睡前聽故事",
    "B": "孝順父母親",
    "C": "失去的童心",
    "D": "哲學的智慧",
  },
  "answer": "C"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '31-33.png',
  "question": "根據短文，為什麼小兒子後來和父親的關係不好？",
  "choices": {
    "A": "他一直都誤會父親",
    "B": "他覺得父親不關心他",
    "C": "他父親很少再和他講故事",
    "D": "他父親是個不切實際的人",
  },
  "answer": "A"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '34-36.png',
  "question": "這則「問與答」主要討論什麼？",
  "choices": {
    "A": "預防近視的正確觀念",
    "B": "睡眠與視力之間的關係",
    "C": "減輕眼睛不舒服的方法",
    "D": "改善眼睛疲勞的小技巧",
  },
  "answer": "C"
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '34-36.png',
  "question": "針對陳先生的問題來源，任醫師認為下面哪種情況是原因之一？",
  "choices": {
    "A": "視力開始退化",
    "B": "眼睛的淚水過多",
    "C": "沒有充足的睡眠",
    "D": "生活環境中有人抽菸",
  },
  "answer": "D"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": '34-36.png',
  "question": "關於任醫師的建議，下列哪一項正確？",
  "choices": {
    "A": "太晚治療容易傳染他人",
    "B": "眼睛一有血絲應立刻就醫",
    "C": "每次冷敷眼睛至少五分鐘",
    "D": "觀察症狀的變化以一週為原則",
  },
  "answer": "D"
},

{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": '37-39.png',
  "question": "作者覺得美式早餐的特色是什麼？",
  "choices": {
    "A": "量多",
    "B": "味道佳",
    "C": "作法精緻",
    "D": "環境優雅",
  },
  "answer": "A"
},

{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": '37-39.png',
  "question": "作者認為義大利式連鎖咖啡店的早餐缺少了什麼？",
  "choices": {
    "A": "豐富的配料",
    "B": "漂亮的裝飾",
    "C": "熱鬧的感覺",
    "D": "廣闊的用餐環境",
  },
  "answer": "C"
},

{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": '37-39.png',
  "question": "這篇文章的作者主要想說明什麼？",
  "choices": {
    "A": "飲食文化的轉變",
    "B": "選擇早餐的標準",
    "C": "現付人的飲食習慣",
    "D": "早餐店成功的秘訣",
  },
  "answer": "A"
},

{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": '40-42.png',
  "question": "小張買了一枚戒指 ，希望他的太太 能在明年的結婚週年紀念日當",
  "choices": {
    "A": "不可將戒指寄到國外",
    "B": "不可連同其他物品寄送",
    "C": "戒指的價格不可高於一萬",
    "D": "一旦決定寄達時間則不可更改",
  },
  "answer": "A"
},

{
  "id": 41,
  "type": "reading",
  "audio": [],
  "image": '40-42.png',
  "question": "明美打算透過這項服務在年底送朋友一個特別的禮物，下列哪一",
  "choices": {
    "A": "當季鮮美的水果",
    "B": "名貴的進口刀具",
    "C": "清晨現撈的海產",
    "D": "湖邊撿到的石頭",
  },
  "answer": "D"
},

{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": '40-42.png',
  "question": "榮恩想在指定時間寄送現金及物品給客戶，下列哪一項正確 ？",
  "choices": {
    "A": "若兩者併寄，總價值不得高於五千元",
    "B": "若兩者併寄，現金金額以一萬元為限",
    "C": "若單寄物件，物品價值頇高於一萬元",
    "D": "若單寄現金，金額頇介於一萬至五萬元",
  },
  "answer": "B"
},

{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "作者認為這部電影吸引人的地方是什麼？",
  "choices": {
    "A": "主要演員驚人的演技",
    "B": "導演盧貝松十分有名氣",
    "C": "片中的真實人物正率領人民打仗",
    "D": "故事主角為了維護和帄而失去生命",
  },
  "answer": "A"
},

{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "關於演員楊紫瓊，下面哪一個是對的？",
  "choices": {
    "A": "她的身材本來有點胖 ",
    "B": "她要求參與這部電影",
    "C": "她本來就會說緬甸話",
    "D": "導演花四年才找到她",
  },
  "answer": "B"
},

{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "根據本文，在拍電影期間，楊紫瓊做了什麼事？",
  "choices": {
    "A": "當緬甸的軍人",
    "B": "讓體重快速上升",
    "C": "和翁山蘇姬見面",
    "D": "在緬甸發表中文演講",
  },
  "answer": "C"
},

{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "第二段主要在說什麼事？",
  "choices": {
    "A": "楊紫瓊是演員兼任導演",
    "B": "翁山蘇姬的生帄與事蹟",
    "C": "楊紫瓊爭取飾演翁山蘇姬的原因",
    "D": "楊紫瓊為演出翁山蘇姬所下的功夫",
  },
  "answer": "D"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "關於國王想推廣馬鈴薯的原因， 沒提到下面哪一項？",
  "choices": {
    "A": "能當作主要的食物",
    "B": "味道和麵包非常搭配",
    "C": "不必花太多力氣照顧",
    "D": "希望讓人民少用麵粉",
  },
  "answer": "B"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "第二段中的「市場反應」指的是什麼？",
  "choices": {
    "A": "一般人吃不起馬鈴薯",
    "B": "沒有人願意賣馬鈴薯",
    "C": "農民認為馬鈴薯不容易種",
    "D": "人民認為馬鈴薯無法取付麵包",
  },
  "answer": "D"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "國王能推廣成功，主要是對人民使用了哪種策略？",
  "choices": {
    "A": "強調吃馬鈴薯的好處",
    "B": "強迫他們不得不接受命仙",
    "C": "引起人民對馬鈴薯的好奇心",
    "D": "強調小麥不足如何影響生活",
  },
  "answer": "C"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "這個故事主要在說明什麼？",
  "choices": {
    "A": "馬鈴薯開始流行的原因",
    "B": "人民改變飲食習慣的目的",
    "C": "馬鈴薯對歐洲人民有什麼好處",
    "D": "國王對食物的愛好如何影響人民",
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