# Test of Chinese as a Foreign Language Reading Band B (Vol.2)

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
        "image": '1-5.png',
        "question": "",
        "choices": {
            "A": "流行",
            "B": "熱鬧",
            "C": "發達",
            "D": "順利",
        },
        "answer": "C"
    },

    {
        "id": 2,
        "type": "reading",
        "audio": [],
        "image": '1-5.png',
        "question": "",
        "choices": {
            "A": "位置",
            "B": "地方",
            "C": "背景",
            "D": "空間",
        },
        "answer": "D"
    },

    {
        "id": 3,
        "type": "reading",
        "audio": [],
        "image": '1-5.png',
        "question": "",
        "choices": {
            "A": "不",
            "B": "很",
            "C": "倒",
            "D": "夠",
        },
        "answer": "A"
    },

    {
        "id": 4,
        "type": "reading",
        "audio": [],
        "image": '1-5.png',
        "question": "",
        "choices": {
            "A": "不論…都…",
            "B": "雖然…但是…",
            "C": "除非…否則…",
            "D": "假如…那麼…",
        },
        "answer": "B"
    },

    {
        "id": 5,
        "type": "reading",
        "audio": [],
        "image": '1-5.png',
        "question": "",
        "choices": {
            "A": "對",
            "B": "為",
            "C": "照",
            "D": "等",
        },
        "answer": "D"
    },

    {
        "id": 6,
        "type": "reading",
        "audio": [],
        "image": '6-10.png',
        "question": "",
        "choices": {
            "A": "頓",
            "B": "組",
            "C": "場",
            "D": "筆",
        },
        "answer": "D"
    },

    {
        "id": 7,
        "type": "reading",
        "audio": [],
        "image": '6-10.png',
        "question": "",
        "choices": {
            "A": "才",
            "B": "又",
            "C": "仍",
            "D": "更",
        },
        "answer": "A"
    },

    {
        "id": 8,
        "type": "reading",
        "audio": [],
        "image": '6-10.png',
        "question": "",
        "choices": {
            "A": "滿足",
            "B": "感動",
            "C": "刺激",
            "D": "鼓勵",
        },
        "answer": "B"
    },

    {
        "id": 9,
        "type": "reading",
        "audio": [],
        "image": '6-10.png',
        "question": "",
        "choices": {
            "A": "明白",
            "B": "在乎",
            "C": "渴望",
            "D": "犧牲",
        },
        "answer": "A"
    },

    {
        "id": 10,
        "type": "reading",
        "audio": [],
        "image": '6-10.png',
        "question": "",
        "choices": {
            "A": "既",
            "B": "僅",
            "C": "卻",
            "D": "還",
        },
        "answer": "D"
    },

    {
        "id": 11,
        "type": "reading",
        "audio": [],
        "image": '11-15.png',
        "question": "",
        "choices": {
            "A": "外",
            "B": "當",
            "C": "各",
            "D": "本",
        },
        "answer": "C"
    },

    {
        "id": 12,
        "type": "reading",
        "audio": [],
        "image": '11-15.png',
        "question": "",
        "choices": {
            "A": "陳列",
            "B": "應付",
            "C": "宣傳",
            "D": "奮鬥",
        },
        "answer": "C"
    },

    {
        "id": 13,
        "type": "reading",
        "audio": [],
        "image": '11-15.png',
        "question": "",
        "choices": {
            "A": "例外",
            "B": "固定",
            "C": "典型",
            "D": "平衡",
        },
        "answer": "B"
    },

    {
        "id": 14,
        "type": "reading",
        "audio": [],
        "image": '11-15.png',
        "question": "",
        "choices": {
            "A": "獲得",
            "B": "包括",
            "C": "呈現",
            "D": "面臨",
        },
        "answer": "A"
    },

    {
        "id": 15,
        "type": "reading",
        "audio": [],
        "image": '11-15.png',
        "question": "",
        "choices": {
            "A": "一旦",
            "B": "與其",
            "C": "即使",
            "D": "由於",
        },
        "answer": "D"
    },

    {
        "id": 16,
        "type": "reading",
        "audio": [],
        "image": '16.png',
        "question": "這個捐血中心的傳單 上說了什麼？",
        "choices": {
            "A": "服務別人就是幫助別人",
            "B": "捐血地點將透過電話通知",
            "C": "捐血中心需要各種血型的血",
            "D": "目前哪一種血型的血明顯不夠",
        },
        "answer": "D"
    },

    {
        "id": 17,
        "type": "reading",
        "audio": [],
        "image": '17.png',
        "question": "根據這張廣告單 ，下面哪一個是對的 ？",
        "choices": {
            "A": "店家接受電話訂餐",
            "B": "點特定火鍋料就送現金",
            "C": "二月前消費就送小禮物",
            "D": "消費一百元以上才能得到鑰匙圈",
        },
        "answer": "A"
    },

    {
        "id": 18,
        "type": "reading",
        "audio": [],
        "image": '18.png',
        "question": "這段話提到文玉的什麼事 ？",
        "choices": {
            "A": "她經常忘記回答鄰居的問題",
            "B": "她等垃圾車的地方就在家門口",
            "C": "她和鄰居每天聊天的內容都一樣",
            "D": "她不願意回答跟交友或工作有關的事",
        },
        "answer": "C"
    },

    {
        "id": 19,
        "type": "reading",
        "audio": [],
        "image": '19.png',
        "question": "這個研究說了什麼？",
        "choices": {
            "A": "女人在音樂方面的興趣與表現比男人高得多",
            "B": "聽音樂的時候，人們比較不容易感覺到疼痛",
            "C": "看病時播放音樂，有助於降低醫院內的噪音",
            "D": "男人比女人更怕痛，牙痛時常不願去看牙醫",
        },
        "answer": "B"
    },

    {
        "id": 20,
        "type": "reading",
        "audio": [],
        "image": '20.png',
        "question": "根據這段介紹 ，可以知道 什麼事？",
        "choices": {
            "A": "咖啡機是透過聲音來控制的",
            "B": "咖啡的品質不能只用嘴來判斷",
            "C": "第一個發明咖啡機的是個年輕人",
            "D": "用這台咖啡機煮咖啡，多遠都聞得到",
        },
        "answer": "A"
    },

    {
        "id": 21,
        "type": "reading",
        "audio": [],
        "image": '21.png',
        "question": "關於這篇文章，下面哪一個是正確的？",
        "choices": {
            "A": "深色巧克力 不比淺色的健康",
            "B": "現代人早 已不流行買花、 送花",
            "C": "吃巧克力 不是對身體沒 有好處",
            "D": "情人節送禮物才能證明彼此的愛",
        },
        "answer": "C"
    },

    {
        "id": 22,
        "type": "reading",
        "audio": [],
        "image": '22.png',
        "question": "這篇文章談到關於使用 CD存檔的哪一件事 ？",
        "choices": {
            "A": "是最能保障檔案 品質的方式",
            "B": "所儲存的內容都 有保存期限",
            "C": "其壽命比一般人想像的 還長",
            "D": "存檔程序複雜是唯一的缺點",
        },
        "answer": "B"
    },

    {
        "id": 23,
        "type": "reading",
        "audio": [],
        "image": '23.png',
        "question": "根據這段話，下面哪一項是對的？",
        "choices": {
            "A": "考古學家不 贊同蔡倫擅長造紙",
            "B": "「蔡侯紙」是 中國人最早發明的紙",
            "C": "很多人最近才知道東漢以前沒有紙",
            "D": "蔡倫的主要成就在於改 進造紙的品質",
        },
        "answer": "D"
    },

    {
        "id": 24,
        "type": "reading",
        "audio": [],
        "image": '24-25.png',
        "question": "小芳為什麼寫這封信 ？",
        "choices": {
            "A": "打算送電影票給朋友",
            "B": "想找人一起買電影票",
            "C": "要幫家人出售電影票",
            "D": "請人陪弟弟去看電影",
        },
        "answer": "C"
    },

    {
        "id": 25,
        "type": "reading",
        "audio": [],
        "image": '24-25.png',
        "question": "從這封信可以 知道什麼 事？",
        "choices": {
            "A": "現在買電影票可以打折",
            "B": "電影開演的時間已經確定",
            "C": "小芳的弟弟也會收到小芳的信",
            "D": "買票的人可以自己選擇想看的電影",
        },
        "answer": "B"
    },

    {
        "id": 26,
        "type": "reading",
        "audio": [],
        "image": '26-27.png',
        "question": "關於這個活動， 下面何者正確？",
        "choices": {
            "A": "可提供面對面交友的機會",
            "B": "只要參加就能得到明信片",
            "C": "有三個人可以拿到錢和禮物",
            "D": "鼓勵大家拍一些和家鄉有關的影片",
        },
        "answer": "B"
    },

    {
        "id": 27,
        "type": "reading",
        "audio": [],
        "image": '26-27.png',
        "question": "想參加的人 應該要注意什麼事？",
        "choices": {
            "A": "可提供面對面交友的機會",
            "B": "5 月 30 日以後才能報名",
            "C": "有問題就寫信給李小姐",
            "D": "作品要親自送到鄉公所",
        },
        "answer": "A"
    },

    {
        "id": 28,
        "type": "reading",
        "audio": [],
        "image": '28-29.png',
        "question": "有關新校區的地理位置，下列何者正確 ？",
        "choices": {
            "A": "運動會只對校內師生開放",
            "B": "搭車前往運動會會場的辦法",
            "C": "未來運動會都改在新校區舉辦",
            "D": "今年運動會將同時在兩個校區舉行",
        },
        "answer": "B"
    },

    {
        "id": 29,
        "type": "reading",
        "audio": [],
        "image": '28-29.png',
        "question": "有關新校區的地理位置，下列何者正確 ？",
        "choices": {
            "A": "位於大中路以南",
            "B": "在新店火車站旁邊",
            "C": "距離舊校區只要十分鐘",
            "D": "離它最近的公車站是大中站",
        },
        "answer": "D"
    },

    {
        "id": 30,
        "type": "reading",
        "audio": [],
        "image": '30-31.png',
        "question": "張小姐剛從 全能大學國際貿易系 畢業，她還應具備什麼條件 ，較有機會到巨輝鋼鐵工作？",
        "choices": {
            "A": "可配合 公司電話面試",
            "B": "願意外派到國外 分公司",
            "C": "能提出電腦相關能力證明",
            "D": "曾從事鋼鐵產業方面的工作",
        },
        "answer": "C"
    },

    {
        "id": 31,
        "type": "reading",
        "audio": [],
        "image": '30-31.png',
        "question": "永昌科技公司的工作最適合 下面哪一種人？",
        "choices": {
            "A": "計畫半工半讀",
            "B": "毫無工作經驗",
            "C": "有夜間工作 傾向",
            "D": "受過一定職業訓練",
        },
        "answer": "D"
    },

    {
        "id": 32,
        "type": "reading",
        "audio": [],
        "image": '32-33.png',
        "question": "關於這個旅遊活動， 下面哪一項正確？",
        "choices": {
            "A": "學生要自己另外付保險費",
            "B": "這是一個當日來回的行程",
            "C": "所有參加旅遊的人都免費",
            "D": "學生的家人想參加得另外付費",
        },
        "answer": "D"
    },

    {
        "id": 33,
        "type": "reading",
        "audio": [],
        "image": '32-33.png',
        "question": "薏如是華語中心的學生，她想報名這個活動，她要注意什麼事？",
        "choices": {
            "A": "12月15日是報名的最後一天",
            "B": "不去的話應該 找同學代替自己參加",
            "C": "臨時不能去，要有收據才能領回保證金",
            "D": "出發前一星期取消報名的人，不能拿回保證金",
        },
        "answer": "C"
    },

    {
        "id": 34,
        "type": "reading",
        "audio": [],
        "image": '34-35.png',
        "question": "這篇文章指出 這位青年怎麼樣？",
        "choices": {
            "A": "看照片才能讓他想起一些事",
            "B": "他擔心女友有天會忘了自己",
            "C": "他以為他參加了一個生日會",
            "D": "他的病使他的生活受到影響",
        },
        "answer": "D"
    },

    {
        "id": 35,
        "type": "reading",
        "audio": [],
        "image": '34-35.png',
        "question": "這位青年發生了什麼事？",
        "choices": {
            "A": "他無法遵守自己的承諾",
            "B": "他把重要的照片弄丟了",
            "C": "他的健康狀況越來越差",
            "D": "他只記得一週以前的事",
        },
        "answer": "A"
    },

    {
        "id": 36,
        "type": "reading",
        "audio": [],
        "image": '36-37.png',
        "question": "文章中的年輕人 怎麼樣？",
        "choices": {
            "A": "拿了點藥就出院了",
            "B": "很在意用餐的環境",
            "C": "有病沒病都去醫院",
            "D": "是某間餐廳的熟客",
        },
        "answer": "D"
    },

    {
        "id": 37,
        "type": "reading",
        "audio": [],
        "image": '36-37.png',
        "question": "下列何者符合作者對去那類餐廳吃飯的看法 ？",
        "choices": {
            "A": "便宜的東西沒好貨",
            "B": "簡直是花錢買罪受",
            "C": "食物才是最天然的藥",
            "D": "寧可吃多，也不吃虧",
        },
        "answer": "B"
    },

    {
        "id": 38,
        "type": "reading",
        "audio": [],
        "image": '38-39.png',
        "question": "關於管理中心大樓的裝修工程，下面哪一項正確？",
        "choices": {
            "A": "工程問題由總務 處負責回答",
            "B": "中心員工不能進入施工區域",
            "C": "預計從 2010年年底開始施工",
            "D": "大樓部分區域得 事先申請才能進入",
        },
        "answer": "A"
    },

    {
        "id": 39,
        "type": "reading",
        "audio": [],
        "image": '38-39.png',
        "question": "2011年一整年 ，王福每 週五會到這個中心上電腦課，他應該注意下面哪一件事？",
        "choices": {
            "A": "可憑上課證 乘接駁車至新 大樓",
            "B": "將會有三個月的時間 暫停上課",
            "C": "至三月份應留意教室變更通知",
            "D": "課程查詢 可以撥電話給張主任",
        },
        "answer": "C"
    },

    {
        "id": 40,
        "type": "reading",
        "audio": [],
        "image": '40-41.png',
        "question": "小時候的遭遇使 羅老闆對人生產生了什麼 想法？",
        "choices": {
            "A": "人要堅強才能生存",
            "B": "命運是由 上天安排的",
            "C": "窮人很難擺脫 消極的想法",
            "D": "對於無法選擇環境感到 挫折",
        },
        "answer": "A"
    },

    {
        "id": 41,
        "type": "reading",
        "audio": [],
        "image": '40-41.png',
        "question": "本文主要在談論羅老闆 的哪一件事？",
        "choices": {
            "A": "成立喬山 公司的細節與 經過",
            "B": "不向命運低頭的精神和態度",
            "C": "將運動器材作為產品的理由",
            "D": "目前在社會上的地位及影響力",
        },
        "answer": "B"
    },

    {
        "id": 42,
        "type": "reading",
        "audio": [],
        "image": '42-43.png',
        "question": "這項以兩名嬰兒為對象的實驗是怎麼進行的？",
        "choices": {
            "A": "由國王親自照顧他們",
            "B": "派官兵帶他們離開埃及",
            "C": "禁止所有人對他們說任何話",
            "D": "命令專人教他們學習古老的語言",
        },
        "answer": "C"
    },

    {
        "id": 43,
        "type": "reading",
        "audio": [],
        "image": '42-43.png',
        "question": "關於本文中提到的心理學實驗，下面哪一項正確？",
        "choices": {
            "A": "是第一個 有正式記錄的心理學實驗",
            "B": "其結果和設計者事先想像的差不多",
            "C": "實驗目的是為 擴大埃及的統治 範圍",
            "D": "意外發現嬰兒說出第一個字是可以控制的",
        },
        "answer": "A"
    },

    {
        "id": 44,
        "type": "reading",
        "audio": [],
        "image": '44-46.png',
        "question": "這個研究主要在說 什麼？",
        "choices": {
            "A": "新聞記者",
            "B": "服飾店員",
            "C": "眼科醫師",
            "D": "心理治療師",
        },
        "answer": "A"
    },

    {
        "id": 45,
        "type": "reading",
        "audio": [],
        "image": '44-46.png',
        "question": "這篇文章提到， 青少年在等人的時候，一直使用手機的原因是什麼？",
        "choices": {
            "A": "新聞記者",
            "B": "服飾店員",
            "C": "眼科醫師",
            "D": "心理治療師",
        },
        "answer": "C"
    },

    {
        "id": 46,
        "type": "reading",
        "audio": [],
        "image": '44-46.png',
        "question": "文章中的老師對青少年使用手機的意見是什麼？",
        "choices": {
            "A": "新聞記者",
            "B": "服飾店員",
            "C": "眼科醫師",
            "D": "心理治療師",
        },
        "answer": "B"
    },

    {
        "id": 47,
        "type": "reading",
        "audio": [],
        "image": '47-50.png',
        "question": "第二段主要 在談什麼事？",
        "choices": {
            "A": "新聞記者",
            "B": "服飾店員",
            "C": "眼科醫師",
            "D": "心理治療師",
        },
        "answer": "C"
    },

    {
        "id": 48,
        "type": "reading",
        "audio": [],
        "image": '47-50.png',
        "question": "作者用「此地無銀三百兩」 來形容人的哪一種行為 ？",
        "choices": {
            "A": "新聞記者",
            "B": "服飾店員",
            "C": "眼科醫師",
            "D": "心理治療師",
        },
        "answer": "C"
    },

    {
        "id": 49,
        "type": "reading",
        "audio": [],
        "image": '47-50.png',
        "question": "本文第三段 作者說了什麼？",
        "choices": {
            "A": "新聞記者",
            "B": "服飾店員",
            "C": "眼科醫師",
            "D": "心理治療師",
        },
        "answer": "D"
    },

    {
        "id": 50,
        "type": "reading",
        "audio": [],
        "image": '47-50.png',
        "question": "寫這篇文章的人 應從事什麼職業？",
        "choices": {
            "A": "新聞記者",
            "B": "服飾店員",
            "C": "眼科醫師",
            "D": "心理治療師",
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