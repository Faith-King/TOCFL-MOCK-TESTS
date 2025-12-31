# Test of Chinese as a Foreign Language Reading Band B (Vol.5)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image_bb_vol5"

# Question Bank (EXAMPLE)
questions = [
    {
  "id": 1,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "尤其",
    "B": "畢竟",
    "C": "不斷",
    "D": "針對",
  },
  "answer": "A"
},
{
  "id": 2,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "比如",
    "B": "至於",
    "C": "自從",
    "D": "除了",
  },
  "answer": "D"
},

{
  "id": 3,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "主動",
    "B": "幸福",
    "C": "發達",
    "D": "樂觀",
  },
  "answer": "C"
},
{
  "id": 4,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "當中",
    "B": "當天",
    "C": "當初",
    "D": "當時",
  },
  "answer": "B"
},

{
  "id": 5,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "開放",
    "B": "採用",
    "C": "安排",
    "D": "提供",
  },
  "answer": "D"
},

{
  "id": 6,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "功能",
    "B": "信用",
    "C": "品質",
    "D": "需求",
  },
  "answer": "D"
},

{
  "id": 7,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "由於",
    "B": "就算",
    "C": "不過",
    "D": "反而",
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
    "A": "引用",
    "B": "參考",
    "C": "評論",
    "D": "推出",
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
    "A": "以及",
    "B": "加上",
    "C": "不僅",
    "D": "或者",
  },
  "answer": "C"
},
{
  "id": 10,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "記錄",
    "B": "發表",
    "C": "帶領",
    "D": "代替",
  },
  "answer": "C"
},

{
  "id": 11,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "官員",
    "B": "隊員",
    "C": "會員",
    "D": "職員 ",
  },
  "answer": "C"
},
{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "限制",
    "B": "反對",
    "C": "犯規",
    "D": "傷害",
  },
  "answer": "A"
},

{
  "id": 13,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "並且",
    "B": "還是",
    "C": "然而",
    "D": "因此",
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
    "A": "福利",
    "B": "薪水",
    "C": "補助",
    "D": "保障",
  },
  "answer": "B"
},

{
  "id": 15,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "光臨",
    "B": "防守",
    "C": "保衛",
    "D": "迎接",
  },
  "answer": "D"
},
{
  "id": 16,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "一會兒",
    "B": "一口氣",
    "C": "一回事",
    "D": "一輩子",
  },
  "answer": "D"
},

{
  "id": 17,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "連",
    "B": "光",
    "C": "同",
    "D": "從",
  },
  "answer": "A"
},

{
  "id": 18,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "受到",
    "B": "碰見",
    "C": "獲得",
    "D": "報答",
  },
  "answer": "C"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '19.png',
  "question": "關於旅行這件事，作者的想法是什麼？",
  "choices": {
    "A": "旅遊時應該多交新朋友",
    "B": "最好選擇交通方便的地方",
    "C": "享受風景比拍照來得重要",
    "D": "要把發生的事都記下來告訴大家",
  },
  "answer": "C"
},

{
  "id": 20,
  "type": "reading",
  "audio": [],
  "image": '20.png',
  "question": "作者在這段話提到了自己的哪件事？",
  "choices": {
    "A": "平日喜愛在咖啡廳 用餐",
    "B": "為恢復體力經常喝咖啡",
    "C": "在咖啡廳有特定的座位喜好",
    "D": "每週固定和朋友在咖啡廳聚餐",
  },
  "answer": "C"
},

{
  "id": 21,
  "type": "reading",
  "audio": [],
  "image": '21-22.png',
  "question": "這家超級市場取消 蔬果包裝的目的是什麼？",
  "choices": {
    "A": "維持蔬果的新鮮度",
    "B": "方便客人自助選購",
    "C": "降低蔬果包裝的成本",
    "D": "減少蔬果包裝產生的垃圾",
  },
  "answer": "D"
},

{
  "id": 22,
  "type": "reading",
  "audio": [],
  "image": '21-22.png',
  "question": "在這家店裡買水果 要怎麼做？",
  "choices": {
    "A": "請店員協助挑選 新鮮水果",
    "B": "選擇自己需要的盒裝水果",
    "C": "將選好的水 果交給店員計算價錢",
    "D": "確認籃子已貼上價錢貼紙再結帳",
  },
  "answer": "C"
},

{
  "id": 23,
  "type": "reading",
  "audio": [],
  "image": '23-24.png',
  "question": "小美為什麼要找人一起搭計程車？",
  "choices": {
    "A": "可減少坐計程車的費用",
    "B": "她希望認識其他新朋友",
    "C": "多一些人坐車比較不無聊",
    "D": "最少要四個人才能搭計程車",
  },
  "answer": "A"
},

{
  "id": 24,
  "type": "reading",
  "audio": [],
  "image": '23-24.png',
  "question": "有四組想去蘋果園的人給小美回了信，哪一組較符合小美的條件？",
  "choices": {
    "A": "預計 8月15日參觀的夫妻",
    "B": "計畫 8月16日出發的母女",
    "C": "希望 8月17日入園的兩 位男大學生",
    "D": "決定 8月27日動身的三 名女高中生",
  },
  "answer": "B"
},

{
  "id": 25,
  "type": "reading",
  "audio": [],
  "image": '25-26.png',
  "question": "根據這則廣告，做什麼有助於大腦健康？",
  "choices": {
    "A": "和朋友玩桌上遊戲",
    "B": "盡量補充保健食品",
    "C": "避免使用電子產品",
    "D": "複習已知的舊知識",
  },
  "answer": "A"
},

{
  "id": 26,
  "type": "reading",
  "audio": [],
  "image": '25-26.png',
  "question": "針對廣告中提到的課程，這則廣告公布了哪項資訊？",
  "choices": {
    "A": "申請步驟",
    "B": "報名資格",
    "C": "活動人數",
    "D": "截止日期",
  },
  "answer": "B"
},

{
  "id": 27,
  "type": "reading",
  "audio": [],
  "image": '27-28.png',
  "question": "這篇文章主要在討論什麼？",
  "choices": {
    "A": "選對方法學習不如選對時間",
    "B": "學習能力的高低與年齡沒關係",
    "C": "工作性質的差異對學習態度的影響",
    "D": "人的注意力只有到晚上才會較為集中",
  },
  "answer": "A"
},

{
  "id": 28,
  "type": "reading",
  "audio": [],
  "image": '27-28.png',
  "question": "下面哪一項做法符合本文作者的建議？",
  "choices": {
    "A": "要求教學者多變換教學方式",
    "B": "鼓勵學習者多參加課外活動",
    "C": "規劃課程表時，應分職業排課",
    "D": "避開部分時段，提高學習意願",
  },
  "answer": "D"
},

{
  "id": 29,
  "type": "reading",
  "audio": [],
  "image": '29-30.png',
  "question": "「血鑽石」名稱的由來和什麼有關係？",
  "choices": {
    "A": "包裝手法",
    "B": "原始外觀",
    "C": "取得途徑",
    "D": "加工方式",
  },
  "answer": "C"
},

{
  "id": 30,
  "type": "reading",
  "audio": [],
  "image": '29-30.png',
  "question": "作者最後提醒讀者 什麼事？",
  "choices": {
    "A": "應該拒絕購買血鑽石",
    "B": "戰爭的嚴重性超出想像",
    "C": "鑽石能製造的浪漫有限",
    "D": "需重視血鑽石的高經濟價值",
  },
  "answer": "A"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '31-32.png',
  "question": "根據這張表，三個國家的社會住宅共同點是什麼？",
  "choices": {
    "A": "沒有租屋使用的期限",
    "B": "由中央政府負責規劃",
    "C": "依家庭收入按比例付租金",
    "D": "戶數佔整體住宅量不到百分之十",
  },
  "answer": "D"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '31-32.png',
  "question": "從這張表可以得到什麼訊息？",
  "choices": {
    "A": "此表的製作時間",
    "B": "提供資料的單位",
    "C": "申請人的職業限制",
    "D": "社會住宅的居住人數",
  },
  "answer": "B"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '33-34.png',
  "question": "作者最後希望讀者怎麼做？",
  "choices": {
    "A": "盡量對年輕人多說好話",
    "B": "勿學買畫的顧客亂殺價",
    "C": "要試著學習講價的技巧",
    "D": "想好自己要過哪種生活",
  },
  "answer": "D"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '33-34.png',
  "question": "作者的寫作方式是什麼？",
  "choices": {
    "A": "先說故事，再說道理",
    "B": "先下定義，再說明想法",
    "C": "先說狀況，再陳述意見",
    "D": "先說道理，再用感情說服",
  },
  "answer": "A"
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '35-37.png',
  "question": "這篇文章主要探討哪件事？",
  "choices": {
    "A": "推銷語言的影響力",
    "B": "健康飲料有何好處",
    "C": "如何設計商品 包裝",
    "D": "消費者心態的變化",
  },
  "answer": "A"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": '35-37.png',
  "question": "關於「熱狗水」 ，下面哪一個是對的？",
  "choices": {
    "A": "利用低價吸引消費者",
    "B": "成分其實不包含熱狗",
    "C": "能夠有效改善 身體健康",
    "D": "是一個行為實驗的工具",
  },
  "answer": "D"
},

{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": '35-37.png',
  "question": "作者覺得買「熱狗水」的人怎麼樣？",
  "choices": {
    "A": "恐怕一錯再錯",
    "B": "被冤枉為騙子",
    "C": "購物十分謹慎",
    "D": "不易相信別人",
  },
  "answer": "A"
},

{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": '38-40.png',
  "question": "有關這家租車公司的服務，下面哪一個是正確的？",
  "choices": {
    "A": "當天租車 得付手續費",
    "B": "租車費只有假日才打折",
    "C": "提前訂車要先付全部租金",
    "D": "訂車完成後可隨時去拿車",
  },
  "answer": "C"
},

{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": '38-40.png',
  "question": "根據這份說明，想在這家公司租車 的消費者，要注意什麼事？",
  "choices": {
    "A": "訂車的時候服務員會先檢查身分證",
    "B": "當天臨時取消租車無法拿回租車費",
    "C": "最晚要在約定日期的晚上 十點前還車",
    "D": "只要超過還車時間就得多付一天租金",
  },
  "answer": "B"
},

{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": '38-40.png',
  "question": "王先生計畫下個月帶家人出門玩幾天，如果他想得到這家租車公司的優惠，可以怎麼做？",
  "choices": {
    "A": "從星期五開始連續租車三天",
    "B": "一個月前打電話到門市租車",
    "C": "每天開車不能超過四百公里",
    "D": "到門市用現金付完所有費用",
  },
  "answer": "A"
},

{
  "id": 41,
  "type": "reading",
  "audio": [],
  "image": '41-43.png',
  "question": "作者認為有些人害怕一個人吃飯的原因是什麼？",
  "choices": {
    "A": "不敢違反社交規定",
    "B": "太在意別人的想法",
    "C": "不能分享最新的消息",
    "D": "擔心錯過朋友的邀請",
  },
  "answer": "B"
},

{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": '41-43.png',
  "question": "關 於「害怕一個人吃飯」 ，下面哪句話可以用來說明作者的觀點？",
  "choices": {
    "A": "無疑是自己嚇自己",
    "B": "反而更不顧別人感受",
    "C": "負面評價自有他的道理",
    "D": "每個人都得面對生活的寂寞",
  },
  "answer": "A"
},

{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": '41-43.png',
  "question": "根據本文，作者認為「一個人」的優點是什麼？",
  "choices": {
    "A": "不必擔心事情被中途打斷",
    "B": "能消除人與人之間的防備",
    "C": "對所做的事情能更加投入",
    "D": "能建立起獨立自主的形象",
  },
  "answer": "C"
},

{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": '44-46.png',
  "question": "作者覺得使用傳統名片的缺點是什麼？",
  "choices": {
    "A": "交換時常浪費不少時間",
    "B": "其材質容易弄髒不耐用",
    "C": "收到太多名片很難找資料",
    "D": "年輕人很少使用傳統名片",
  },
  "answer": "C"
},

{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": '44-46.png',
  "question": "文中提到電子名片不能完全取代傳統名片的原因為何？",
  "choices": {
    "A": "學習操作的步驟較複雜",
    "B": "部分地區的網路設備差",
    "C": "事先輸入資料很花時間",
    "D": "傳統名片較有個人特色",
  },
  "answer": "B"
},

{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": '44-46.png',
  "question": "針對發展電子名片一事，作者最後給政府什麼建議？",
  "choices": {
    "A": "應主動設計統一的使用工具",
    "B": "需交由企業投資建設大量網路",
    "C": "全面調查使用現況，再決定是否 需普及",
    "D": "設法結合多方資源，制定相關政策與措施",
  },
  "answer": "D"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "下面哪一項是這家公司開出的徵求條件？",
  "choices": {
    "A": "能隨時以英語信件與客戶往來",
    "B": "在客戶說話時馬上翻譯成中文",
    "C": "工作表現能讓總經理印象深刻",
    "D": "個性實在做事負責不欺騙上司",
  },
  "answer": "B"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "總經理面試時為什麼說文奇救了他女兒？",
  "choices": {
    "A": "他希望文奇能輕鬆一點",
    "B": "他得確認文奇真正的身分",
    "C": "他想觀察文奇當時的反應",
    "D": "他要表揚文奇幫助他女兒",
  },
  "answer": "C"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "文奇被總經理錄用最主要的原因是什麼？",
  "choices": {
    "A": "總經理認錯人了",
    "B": "他是一個誠實的人",
    "C": "他救了總經理的女兒",
    "D": "他通過了公司的筆試",
  },
  "answer": "B"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "我們可以從這篇文章中知道文奇哪件事？",
  "choices": {
    "A": "他是一個女兒的父親",
    "B": "游泳是他拿手的運動",
    "C": "只有他一人被該公司錄取",
    "D": "他能輕鬆 用英語與人談話",
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