import os
from termcolor import colored
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).parent

# -------------------------
# Question Bank (EXAMPLE)
# -------------------------
questions = [
    {
        "id": 1,
        "type": "picture",
        "image": "images/q1.png",
        "question": "桌子上放著三種水果。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 2,
        "type": "picture",
        "image": "images/q2.png",
        "question": "老王正畫著小天的臉。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 3,
        "type": "picture",
        "image": "images/q3.png",
        "question": "他的房間很乾淨。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 4,
        "type": "picture",
        "image": "images/q4.png",
        "question": "王小明把李天華三個字寫在紙上。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 5,
        "type": "picture",
        "image": "images/q5.png",
        "question": "志明什麼球都玩，但是最喜歡玩足球。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 6,
        "type": "picture",
        "image": "images/q6.png",
        "question": "小心！你杯子裡的水快要滿了！",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 7,
        "type": "picture",
        "image": "images/q7.png",
        "question": "過了前面的路口，再往前走一會兒就到醫院了。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 8,
        "type": "picture",
        "image": "images/q8.png",
        "question": "我平常都六點起床，可是今天晚了半小時。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 9,
        "type": "picture",
        "image": "images/q9.png",
        "question": "張先生開車的時候喜歡聽音樂。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 10,
        "type": "picture",
        "image": "images/q10.png",
        "question": "這幾天晚上的風好大。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 11,
        "type": "picture",
        "image": "images/q11.png",
        "question": "妹妹看完信以後，心情很愉快。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 12,
        "type": "picture",
        "image": "images/q12.png",
        "question": "我們全家下個月就要搬到院子裡有大樹的房子住了。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 13,
        "type": "picture",
        "image": "images/q13.png",
        "question": "因為媽媽怕高，所以沒和爸爸一起爬過山。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 14,
        "type": "picture",
        "image": "images/q14.png",
        "question": "他們約好下課以後，先在學校門口見面，再一起去打球。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 15,
        "type": "picture",
        "image": "images/q15.png",
        "question": "小美和朋友想到百貨公司買帽子，可是最後只買了點心就離開了。",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 16,
        "type": "picture",
        "image": "images/q16.png",
        "question": "請根據圖片，選出正確的句子。",
        "choices": {
            "A": "小狗正追著小貓。",
            "B": "屋子裡面什麼都沒有。",
            "C": "幾隻小鳥停在屋子上面。"
        },
        "answer": "C"
    },
    {
        "id": 17,
        "type": "picture",
        "image": "images/q17.png",
        "question": "請根據圖片，選出正確的句子。",
        "choices": {
            "A": "這裡有樹和一間房子。",
            "B": "房子的前面停了幾輛車。",
            "C": "有一些人站在房子旁邊。"
        },
        "answer": "A"
    },
    {
        "id": 18,
        "type": "picture",
        "image": "images/q18.png",
        "question": "",
        "choices": {
            "A": "她正在休息。",
            "B": "她在床上睡覺。",
            "C": "她正寫著作業。"
        },
        "answer": "A"
    },
    {
        "id": 19,
        "type": "picture",
        "image": "images/q19.png",
        "question": "",
        "choices": {
            "A": "短頭髮的小姐在喝酒。",
            "B": "長頭髮的小姐穿裙子。",
            "C": "穿裙子的小姐拿著皮包。"
        },
        "answer": "B"
    },
    {
        "id": 20,
        "type": "picture",
        "image": "images/q20.png",
        "question": "",
        "choices": {
            "A": "小吃店九點以前休息。",
            "B": "小吃店十二點開始休息。",
            "C": "十二點以後可以去小吃店吃飯。"
        },
        "answer": "C"
    },
    {
        "id": 21,
        "type": "picture",
        "image": "images/q20.png",
        "question": "",
        "choices": {
            "A": "一天吃三粒。",
            "B": "三天吃一次。",
            "C": "先吃飯再吃藥。"
        },
        "answer": "C"
    },
    {
        "id": 22,
        "type": "picture",
        "image": "images/q22.png",
        "question": "",
        "choices": {
            "A": "中午以後買票比較貴。",
            "B": "上午買兩張票要500元。",
            "C": "想看電影要中午以後才行。"
        },
        "answer": "A"
    },
    {
        "id": 23,
        "type": "picture",
        "image": "images/q23.png",
        "question": "",
        "choices": {
            "A": "教室的門是關著的。",
            "B": "這位老師今天穿裙子。",
            "C": "這位老師的頭髮短短的。"
        },
        "answer": "B"
    },
    {
        "id": 24,
        "type": "picture",
        "image": "images/q24.png",
        "question": "",
        "choices": {
            "A": "他們現在正在上課。",
            "B": "他們從學校走出來。",
            "C": "男孩走在女孩的前面。"
        },
        "answer": "C"
    },
    {
        "id": 25,
        "type": "picture",
        "image": "images/q25.png",
        "question": "",
        "choices": {
            "A": "這家餐廳不賣飲料。",
            "B": "餐廳裡一個人都沒有。",
            "C": "這位女客人買了兩杯果汁。"
        },
        "answer": "C"
    },
    {
        "id": 26,
        "type": "picture",
        "image": "images/q26.png",
        "question": "",
        "choices": {
            "A": "小美下午三點多才到旅館。",
            "B": "在這兒住一晚要兩百多塊。",
            "C": "小美帶了好幾件大的行李。"
        },
        "answer": "C"
    },
    {
        "id": 27,
        "type": "picture",
        "image": "images/q27.png",
        "question": "",
        "choices": {
            "A": "那位男生正在賣麵包。",
            "B": "等車的小姐拿著一袋水果。",
            "C": "有一位小姐在等七十六號公車。"
        },
        "answer": "C"
    },
    {
        "id": 28,
        "type": "picture",
        "image": "images/q28.png",
        "question": "",
        "choices": {
            "A": "王小姐買了三雙鞋子。",
            "B": "這家店只賣鞋子和襪子。",
            "C": "這家店也賣褲子和皮包。"
        },
        "answer": "C"
    },
    {
        "id": 29,
        "type": "picture",
        "image": "images/q29.png",
        "question": "",
        "choices": {
            "A": "李天明教台北人英文。",
            "B": "李天明要找外國人學英文。",
            "C": "李天明覺得學中文很便宜。"
        },
        "answer": "C"
    },
    {
        "id": 30,
        "type": "picture",
        "image": "images/q30.png",
        "question": "",
        "choices": {
            "A": "兩個人一起去，就有紅茶可以喝。",
            "B": "一個人不到兩萬就可以去韓國旅行。",
            "C": "三個人一起去的話，一共可以少給 1000 元。"
        },
        "answer": "C"
    },
    {
        "id": 31,
        "type": "picture",
        "image": "images/q31-35.png",
        "question": "___著眼鏡的小女孩在看書。",
        "choices": {
            "A": "穿",
            "B": "帶",
            "C": "戴"
        },
        "answer": "C"
    },
    {
        "id": 32,
        "type": "picture",
        "image": "images/q31-35.png",
        "question": "她一邊看書，一邊___筷子吃麵。",
        "choices": {
            "A": "帶",
            "B": "用",
            "C": "找"
        },
        "answer": "B"
    },
    {
        "id": 33,
        "type": "picture",
        "image": "images/q31-35.png",
        "question": "那個小女孩___有一隻狗。",
        "choices": {
            "A": "旁邊",
            "B": "前邊",
            "C": "後邊"
        },
        "answer": "A"
    },
    {
        "id": 34,
        "type": "picture",
        "image": "images/q31-35.png",
        "question": "那隻狗___睡覺。",
        "choices": {
            "A": "在",
            "B": "要",
            "C": "是"
        },
        "answer": "A"
    },
    {
        "id": 35,
        "type": "picture",
        "image": "images/q31-35.png",
        "question": "小女孩___小狗是好朋友。",
        "choices": {
            "A": "有",
            "B": "跟",
            "C": "一起"
        },
        "answer": "B"
    },
    {
        "id": 36,
        "type": "picture",
        "image": "images/q36-40.png",
        "question": "小女孩___小狗是好朋友。",
        "choices": {
            "A": "有",
            "B": "跟",
            "C": "一起"
        },
        "answer": "B"
    },
    {
        "id": 37,
        "type": "picture",
        "image": "images/q36-40.png",
        "question": "小女孩___小狗是好朋友。",
        "choices": {
            "A": "有",
            "B": "跟",
            "C": "一起"
        },
        "answer": "A"
    },
    {
        "id": 38,
        "type": "picture",
        "image": "images/q36-40.png",
        "question": "小女孩___小狗是好朋友。",
        "choices": {
            "A": "有",
            "B": "跟",
            "C": "一起"
        },
        "answer": "A"
    },
    {
        "id": 39,
        "type": "picture",
        "image": "images/q36-40.png",
        "question": "小女孩___小狗是好朋友。",
        "choices": {
            "A": "有",
            "B": "跟",
            "C": "一起"
        },
        "answer": "C"
    },
    {
        "id": 40,
        "type": "picture",
        "image": "images/q36-40.png",
        "question": "小女孩___小狗是好朋友。",
        "choices": {
            "A": "有",
            "B": "跟",
            "C": "一起"
        },
        "answer": "A"
    },
    {
        "id": 41,
        "type": "reading",
        "question": """昨天晚上我覺得很不舒服， _（41）_，所以很早就睡覺了。今天早上起來， _（42）_。我去看病，醫生說我感冒了，給了我一些藥， _（43）_ 要多休息，多喝水，才會快點好。這幾天的天氣一會兒熱，一會兒冷， _（44）_。我要 _（45）_ ，不要再感冒了。""",
        "choices": {
            "A": "還告訴我",
            "B": "頭有點兒痛",
            "C": "很容易生病",
            "D": "覺得很舒服",
            "E": "更不舒服了",
            "F": "多注意自己的身體"
        },
        "answer": "B"
    },
    {
        "id": 42,
        "type": "reading",
        "question": """昨天晚上我覺得很不舒服， _頭有點兒痛_，所以很早就睡覺了。今天早上起來， _（42）_。我去看病，醫生說我感冒了，給了我一些藥， _（43）_ 要多休息，多喝水，才會快點好。這幾天的天氣一會兒熱，一會兒冷， _（44）_。我要 _（45）_ ，不要再感冒了。""",
        "choices": {
            "A": "還告訴我",
            "*": "-",
            "C": "很容易生病",
            "D": "覺得很舒服",
            "E": "更不舒服了",
            "F": "多注意自己的身體"
        },
        "answer": "E"
    },
    {
        "id": 43,
        "type": "reading",
        "question": """昨天晚上我覺得很不舒服， _頭有點兒痛_，所以很早就睡覺了。今天早上起來， _更不舒服了_。我去看病，醫生說我感冒了，給了我一些藥， _（43）_ 要多休息，多喝水，才會快點好。這幾天的天氣一會兒熱，一會兒冷， _（44）_。我要 _（45）_ ，不要再感冒了。""",
        "choices": {
            "A": "還告訴我",
            "*": "-",
            "C": "很容易生病",
            "D": "覺得很舒服",
            "*": "-",
            "F": "多注意自己的身體"
        },
        "answer": "A"
    },
    {
        "id": 44,
        "type": "reading",
        "question": """昨天晚上我覺得很不舒服， _頭有點兒痛_，所以很早就睡覺了。今天早上起來， _更不舒服了_。我去看病，醫生說我感冒了，給了我一些藥， _還告訴我_ 要多休息，多喝水，才會快點好。這幾天的天氣一會兒熱，一會兒冷， _（44）_。我要 _（45）_ ，不要再感冒了。""",
        "choices": {
            "*": "-",
            "*": "-",
            "C": "很容易生病",
            "D": "覺得很舒服",
            "*": "-",
            "F": "多注意自己的身體"
        },
        "answer": "C"
    },
    {
        "id": 45,
        "type": "reading",
        "question": """昨天晚上我覺得很不舒服， _頭有點兒痛_，所以很早就睡覺了。今天早上起來， _更不舒服了_。我去看病，醫生說我感冒了，給了我一些藥， _還告訴我_ 要多休息，多喝水，才會快點好。這幾天的天氣一會兒熱，一會兒冷， _很容易生病_。我要 _（45）_ ，不要再感冒了。""",
        "choices": {
            "*": "-",
            "*": "-",
            "*": "-",
            "D": "覺得很舒服",
            "*": "-",
            "F": "多注意自己的身體"
        },
        "answer": "F"
    },
    {
        "id": 46,
        "type": "reading",
        "passage": """曾有一項調查發現，很多員工生病的時候不敢請假，因為他們擔心老闆會
不高興，覺得他們沒有責任感。有人認為，員工會這麼想是公司的責任。一個
好的公司應該能照顧員工，而不是讓他們拿健康去換錢。因此，讓員工有幸福
感，應該是未來企業努力的方向。""",
        "question": "這篇文章說了什麼內容？",
        "choices": {
            "A": "老闆應該給員工多一點兒假",
            "B": "常關心別人的人更有責任感",
            "C": "對公司有意見要勇敢說出來",
            "D": "照顧身體比認真工作更重要"
        },
        "answer": "D"
   },
   {
        "id": 47,
        "type": "reading",
        "passage": """如果你每天都覺得身體很累，有一份報告或許可以告訴你原因。這份報告
提到了下面幾種可能：不愛運動、水喝得不夠多、總是把事情想得太壞、不吃
早餐、吃太多沒營養的食物等。以上幾點，只要簡單思考一下自己符合了幾項，
再試著做出一些改變，想讓自己更健康一點也不難。""",
        "question": "在改善健康方面，下面哪一個是作者的建議？",
        "choices": {
            "A": "要培養運動的好習慣",
            "B": "想要吃什麼就吃什麼",
            "C": "平常應該多做點好事",
            "D": "吃早餐以後不要喝水"
        },
        "answer": "A"
   },
   {
        "id": 48,
        "type": "reading",
        "passage": """從前有一個地方很久都不下雨，人們不管怎麼求雨都沒有用。有一次，他
們從很遠的地方，請來一位有智慧的老人，希望他可以幫幫忙。老人在附近走
了走、看了看，然後告訴他們，請蓋一間小屋，讓他住進去三天，三天當中，
他任何人都不見。結果，三天後真的下雨了。大家都問他是怎麼做到的，他只
回答，只要自己的心安靜了，外面就安靜了，所以下雨了。""",
        "question": "這個故事告訴了我們什麼事？",
        "choices": {
            "A": "先照顧自己，才能幫助別人",
            "B": "想改變環境，就先改變心情",
            "C": "年輕人應該要學會尊敬老人",
            "D": "聰明的人知道什麼時候下雨"
        },
        "answer": "B"
   },
   {
        "id": 49,
        "type": "reading",
        "passage": """說到錢，每個人對它的想法、使用方式和重視程度都不一樣。有人說：「錢
是沒有性格的，它在誰的手上就像誰」。這句話說得很有道理，人們因為對錢的
看法不同，而選擇不同的生活方式。比方說，有的人喜歡看到銀行裡的數字不
斷增加，所以每天努力工作，很少花錢；有的人覺得錢只要夠用就好，不必太
在意工作，因為「自己的時間」，也是一種看不到的「錢」。""",
        "question": "這段話說了下面哪件事？",
        "choices": {
            "A": "錢比什麼都重要",
            "B": "錢可以解決所有事情",
            "C": "人人有自己對錢的看法",
            "D": "錢得放在銀行裡才有價值"
        },
        "answer": "C"
   },
   {
        "id": 50,
        "type": "reading",
        "passage": """以前，電影院的門口常常出現一個牌子，要觀眾別帶外面買的食物進去，
如果想吃東西，只能買電影院裡賣的食物。後來，新聞說，觀眾其實可以拒絕
配合這些電影院的規矩。說到這個問題，我認為，電影院的要求不是沒有道理，
因為電影結束以後，他們還得打掃那些垃圾。其次，如果有人帶了一些有奇怪
味道的食物進電影院，也很容易影響其他看電影的人。""",
        "question": "作者對在電影院裡吃東西的行為怎麼看？",
        "choices": {
            "A": "應該要避免吃有特別味道的東西",
            "B": "覺得吃什麼東西都是個人的自由",
            "C": "認為電影院的要求沒有任何道理",
            "D": "看電影的人都有責任要打掃垃圾"
        },
        "answer": "A"
   }
]

score = 0

# -------------------------
# Exam Loop
# -------------------------
for q in questions:
    print(colored(f"\nQuestion {q['id']}", "cyan"))

    # Show image if picture question
    if q["type"] == "picture":
        img_path = BASE_DIR / q["image"]

    if not img_path.exists():
        print(f"⚠️ Image not found: {img_path}")
    else:
        img = Image.open(img_path)
        img.show()

    # Show passage if reading question
    if q["type"] == "reading":
        print(colored("\n[Reading Passage]", "yellow"))
        print(q["passage"])

    print(colored("\n" + q["question"], "white"))

    for key, value in q["choices"].items():
        print(f"  ({key}) {value}")

    user_answer = input(colored("\nYour answer (A/B/C/D/E/F): ", "cyan")).strip().upper()

    if user_answer == q["answer"]:
        print(colored("✅ Correct!", "green"))
        score += 1
    else:
        print(colored(f"❌ Wrong: Correct answer [{q['answer']}]", "red"))

# -------------------------
# Final Score
# -------------------------
print(colored(f"\nFinal Score: {score} / {len(questions)}", "magenta"))