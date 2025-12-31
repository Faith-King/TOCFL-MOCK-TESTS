# Test of Chinese as a Foreign Language Reading Band B (Vol.4)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image_bb_vol4"

# Question Bank (EXAMPLE)
questions = [
    {
  "id": 1,
  "type": "reading",
  "audio": [],
  "image": '1-5.png',
  "question": "",
  "choices": {
    "A": "在",
    "B": "離",
    "C": "從",
    "D": "到",
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
    "A": "內",
    "B": "前",
    "C": "中",
    "D": "間",
  },
  "answer": "B"
},

{
  "id": 3,
  "type": "reading",
  "audio": [],
  "image": '1-5.png',
  "question": "",
  "choices": {
    "A": "的",
    "B": "了",
    "C": "得",
    "D": "著",
  },
  "answer": "C"
},
{
  "id": 4,
  "type": "reading",
  "audio": [],
  "image": '1-5.png',
  "question": "",
  "choices": {
    "A": "把握",
    "B": "通過",
    "C": "接受",
    "D": "挑戰",
  },
  "answer": "D"
},

{
  "id": 5,
  "type": "reading",
  "audio": [],
  "image": '5-11.png',
  "question": "",
  "choices": {
    "A": "基本",
    "B": "真正",
    "C": "實在",
    "D": "有名",
  },
  "answer": "A"
},

{
  "id": 6,
  "type": "reading",
  "audio": [],
  "image": '5-11.png',
  "question": "",
  "choices": {
    "A": "光是",
    "B": "反覆",
    "C": "逐漸",
    "D": "偏偏",
  },
  "answer": "C"
},

{
  "id": 7,
  "type": "reading",
  "audio": [],
  "image": '5-11.png',
  "question": "",
  "choices": {
    "A": "受到",
    "B": "感到",
    "C": "達到",
    "D": "接到",
  },
  "answer": "C"
},

{
  "id": 8,
  "type": "reading",
  "audio": [],
  "image": '5-11.png',
  "question": "",
  "choices": {
    "A": "盲目",
    "B": "大意",
    "C": "失望",
    "D": "操心",
  },
  "answer": "B"
},

{
  "id": 9,
  "type": "reading",
  "audio": [],
  "image": '5-11.png',
  "question": "",
  "choices": {
    "A": "轉",
    "B": "降",
    "C": "稱",
    "D": "傳",
  },
  "answer": "A"
},

{
  "id": 10,
  "type": "reading",
  "audio": [],
  "image": '5-11.png',
  "question": "",
  "choices": {
    "A": "躲",
    "B": "升",
    "C": "飄",
    "D": "散",
  },
  "answer": "C"
},

{
  "id": 11,
  "type": "reading",
  "audio": [],
  "image": '5-11.png',
  "question": "",
  "choices": {
    "A": "規劃",
    "B": "規則",
    "C": "交易",
    "D": "順序",
  },
  "answer": "A"
},

{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '12-17.png',
  "question": "",
  "choices": {
    "A": "財產",
    "B": "補助",
    "C": "打算",
    "D": "代價",
  },
  "answer": "B"
},

{
  "id": 13,
  "type": "reading",
  "audio": [],
  "image": '12-17.png',
  "question": "",
  "choices": {
    "A": "教訓",
    "B": "管制",
    "C": "號召",
    "D": "輔導",
  },
  "answer": "D"
},

{
  "id": 14,
  "type": "reading",
  "audio": [],
  "image": '12-17.png',
  "question": "",
  "choices": {
    "A": "缺乏",
    "B": "喪失",
    "C": "超出",
    "D": "忽略",
  },
  "answer": "A"
},

{
  "id": 15,
  "type": "reading",
  "audio": [],
  "image": '12-17.png',
  "question": "",
  "choices": {
    "A": "常識",
    "B": "程序",
    "C": "構造",
    "D": "方案",
  },
  "answer": "D"
},

{
  "id": 16,
  "type": "reading",
  "audio": [],
  "image": '12-17.png',
  "question": "",
  "choices": {
    "A": "光",
    "B": "好",
    "C": "將",
    "D": "連",
  },
  "answer": "A"
},

{
  "id": 17,
  "type": "reading",
  "audio": [],
  "image": '12-17.png',
  "question": "",
  "choices": {
    "A": "混",
    "B": "供",
    "C": "待",
    "D": "度",
  },
  "answer": "C"
},

{
  "id": 18,
  "type": "reading",
  "audio": [],
  "image": '18.png',
  "question": "有關「平價旅館」的描述，下面哪一個是 錯的？",
  "choices": {
    "A": "住宿費用較低",
    "B": "房間的設計傳統、簡單",
    "C": "多半是由舊房子改成的",
    "D": "和大型飯店同樣具有運動設備",
  },
  "answer": "D"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '19-20.png',
  "question": "先生從什麼時候開始做家事？",
  "choices": {
    "A": "他離開他爸媽以後",
    "B": "他和太太結婚以後",
    "C": "他的爸媽要求以後",
    "D": "他的太太有工作以後",
  },
  "answer": "A"
},

{
  "id": 20,
  "type": "reading",
  "audio": [],
  "image": '19-20.png',
  "question": "文章中，太太對做家事的看法怎麼樣？",
  "choices": {
    "A": "先生讓她覺得做家事很有意思",
    "B": "她擔心先生做家事會讓她更忙",
    "C": "她認為家事不全是女人該做的事",
    "D": "她希望先生只要認真工作就可以了",
  },
  "answer": "C"
},

{
  "id": 21,
  "type": "reading",
  "audio": [],
  "image": '21-22.png',
  "question": "根據這張集點卡，下面哪一個是正確的？",
  "choices": {
    "A": "用集點卡買東西每月可享一次優惠",
    "B": "如果買兩百元的商品可以得到一個點數",
    "C": "拿出上面這張集點卡，買麵包可以打八折",
    "D": "要去位於台北市中華路的店才可換會員卡",
  },
  "answer": "B"
},

{
  "id": 22,
  "type": "reading",
  "audio": [],
  "image": '21-22.png',
  "question": "關於這家店的會員卡，下面哪一個是正確的？",
  "choices": {
    "A": "會員卡一年以後就不能用了",
    "B": "會員卡不可以借給別人使用",
    "C": "只要消費三十次就可以換會員卡",
    "D": "一次買一千五百元的產品可以直接換會員卡",
  },
  "answer": "A"
},

{
  "id": 23,
  "type": "reading",
  "audio": [],
  "image": '23-24.png',
  "question": "使用這個設備的人要注意什麼？",
  "choices": {
    "A": "任何清潔劑都不能擦在機器上",
    "B": "一次只能用一層架子料理食物",
    "C": "使用以前都得先開大火十分鐘",
    "D": "每次使用以後都得用海綿擦乾淨",
  },
  "answer": "D"
},

{
  "id": 24,
  "type": "reading",
  "audio": [],
  "image": '23-24.png',
  "question": "根據內容，這應該是一種什麼機器？",
  "choices": {
    "A": "煮飯用的電子鍋",
    "B": "家庭用的迷你烤箱",
    "C": "個人用的小瓦斯爐",
    "D": "能自動煮水的熱水瓶",
  },
  "answer": "B"
},

{
  "id": 25,
  "type": "reading",
  "audio": [],
  "image": '25-27.png',
  "question": "根據這則廣告，這是個什麼樣的服務？",
  "choices": {
    "A": "替旅客保管交通工具",
    "B": "為旅客預約下次班機",
    "C": "接送旅客到機場搭飛機",
    "D": "以信用卡買機票可享折扣",
  },
  "answer": "C"
},

{
  "id": 26,
  "type": "reading",
  "audio": [],
  "image": '25-27.png',
  "question": "關於這項服務，申請人應該注意什麼事？",
  "choices": {
    "A": "可以和朋友一同使用",
    "B": "可以由親人代替申請",
    "C": "假日也可以打電話預約",
    "D": "須提供自家車的車牌號碼",
  },
  "answer": "A"
},

{
  "id": 27,
  "type": "reading",
  "audio": [],
  "image": '25-27.png',
  "question": "曾小姐為永豐客戶，她八月十日星期五要出國，打算申請這項服",
  "choices": {
    "A": "前一天用信用卡買機票",
    "B": "提早兩天用現金買機票",
    "C": "支付服務人員一些費用",
    "D": "八月八日前打電話預約",
  },
  "answer": "D"
},

{
  "id": 28,
  "type": "reading",
  "audio": [],
  "image": '28-30.png',
  "question": "親水會館提供退費的主要原因是什麼？",
  "choices": {
    "A": "暫停營業",
    "B": "配合民眾的要求",
    "C": "搬遷到別的地方",
    "D": "部分設備無法使用",
  },
  "answer": "A"
},

{
  "id": 29,
  "type": "reading",
  "audio": [],
  "image": '28-30.png',
  "question": "小明在 5月1日看見這則公告，想起自己還有十張親水會館的門",
  "choices": {
    "A": "馬上辦理退費",
    "B": "在六月底以前用完",
    "C": "辦理延長使用日期",
    "D": "十一月開館以後再使用",
  },
  "answer": "B"
},

{
  "id": 30,
  "type": "reading",
  "audio": [],
  "image": '30-33.png',
  "question": "下面哪一個是對的？",
  "choices": {
    "A": "館內設備將維持不變",
    "B": "門票退費時間只有一個月",
    "C": "親水會館大約營業兩年了",
    "D": "租用櫃子的人無法辦理退費",
  },
  "answer": "C"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '30-33.png',
  "question": "根據本文，為什麼吃早餐對貧窮孩子的學業表現有幫助 ？",
  "choices": {
    "A": "早餐讓他們的身體變得健康",
    "B": "早餐讓他們比較有上學的意願",
    "C": "學校提供的麵包牛奶對頭腦很好",
    "D": "學校給貧窮孩子的早餐特別營養",
  },
  "answer": "B"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '30-33.png',
  "question": "根據本文， 康乃爾大學的研究指出什麼事 ？",
  "choices": {
    "A": "午餐、晚餐吃得少能有效瘦身",
    "B": "吃大份早餐讓人午餐吃得更多",
    "C": "肥胖者應該少吃午餐而非早餐",
    "D": "早餐吃得多對減輕體重沒幫助",
  },
  "answer": "D"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '30-33.png',
  "question": "作者對「吃早餐」的想法是什麼？",
  "choices": {
    "A": "不必勉強",
    "B": "應該堅持",
    "C": "堅決取消",
    "D": "難以忍受",
  },
  "answer": "A"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '34-36.png',
  "question": "影片中的小海鬣蜥最後怎麼了 ？",
  "choices": {
    "A": "把蛇弄死了",
    "B": "被蛇吃掉了",
    "C": "成功逃走 了",
    "D": "不小心受傷了",
  },
  "answer": "C"
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '34-36.png',
  "question": "下面哪一個適合用來評論這部影片 ？",
  "choices": {
    "A": "精彩刺激",
    "B": "優美動人",
    "C": "嚴肅悲痛",
    "D": "歡樂幽默",
  },
  "answer": "A"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": '34-36.png',
  "question": "這篇文章提到了 影片的哪件事？",
  "choices": {
    "A": "結局由英國廣播公司編寫",
    "B": "演員的動作交由專人設計",
    "C": "電影音樂改編自知名樂曲",
    "D": "是系列影片中的其中一支",
  },
  "answer": "D"
},

{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": '37-39.png',
  "question": "關於文章中提到的「公式」 ， 主要是指什麼？",
  "choices": {
    "A": "拍電影的 技巧",
    "B": "劇本內容的安排",
    "C": "宣傳電影 的管道",
    "D": "觀眾的心理狀態",
  },
  "answer": "B"
},

{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": '37-39.png',
  "question": "作者認為這類的 電影能一拍再拍 的原因是什麼？",
  "choices": {
    "A": "內容簡單，所以 容易被人記住",
    "B": "能與觀眾 的現實生活相互結合",
    "C": "因為故事內容都是真實發生的",
    "D": "因為故事 裡講的一切都很美好",
  },
  "answer": "B"
},

{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": '37-39.png',
  "question": "文章裡提到的電影 ，最有可能是下面哪一種 ？",
  "choices": {
    "A": "愛情電影",
    "B": "災難電影",
    "C": "犯罪電影",
    "D": "運動電影",
  },
  "answer": "D"
},

{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": '40-42.png',
  "question": "根據文章， 院內規劃的課程有什麼特別的地方？",
  "choices": {
    "A": "每天都有課程",
    "B": "主要以科學研究為主",
    "C": "學生們的年齡差距很大",
    "D": "注重人與人之間的溝通技巧",
  },
  "answer": "C"
},

{
  "id": 41,
  "type": "reading",
  "audio": [],
  "image": '40-42.png',
  "question": "作者在文章中提到 兩位學生的相處 ，主要說明什麼？",
  "choices": {
    "A": "小孩需要家人長時間陪伴",
    "B": "一老一少 彼此往來的方式",
    "C": "老人的衰退與疾病高度相關",
    "D": "老人家的社會經驗十分豐富",
  },
  "answer": "B"
},

{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": '40-42.png',
  "question": "作者對這些課程的想法是什麼？",
  "choices": {
    "A": "他希望這些課程能被普及",
    "B": "他希望有更多人關心課程內容",
    "C": "他想進一步研究課程設計的方式",
    "D": "他覺得對上課的學生來說是件好事",
  },
  "answer": "D"
},

{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "根據研究報告， 下面哪一種語言的速度最慢？",
  "choices": {
    "A": "德語",
    "B": "日語",
    "C": "華語",
    "D": "西班牙語",
  },
  "answer": "C"
},

{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "研究人員認為華語包含較多訊息量 和什麼有關 ？",
  "choices": {
    "A": "聲調",
    "B": "字的結構",
    "C": "發音的位置",
    "D": "詞語的組合方式",
  },
  "answer": "A"
},

{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "這個研究的結果是什麼？",
  "choices": {
    "A": "語言之間沒有 共同結構",
    "B": "訊息量多寡和語速沒有關係",
    "C": "語速的快慢與音節數多寡相反",
    "D": "七種語言中，只有華語帶有語調",
  },
  "answer": "B"
},

{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": '43-46.png',
  "question": "作者於文中 提到「普遍語法概念」 ，他想表達什麼？",
  "choices": {
    "A": "他覺得 語法概念是語言交流 關鍵",
    "B": "他想說明語法與語言訊息的關係",
    "C": "他認同語言學家長久以來的貢獻",
    "D": "他認為語言之間確實有共同結構",
  },
  "answer": "D"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "導演以〈林沖夜奔〉說明哪件事？",
  "choices": {
    "A": "他對電影內容的想法",
    "B": "他離開故鄉 時的感受",
    "C": "他最欣賞的演員類型",
    "D": "他對《水滸傳》的理解",
  },
  "answer": "A"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "導演所追尋的「 創作的自由 」指的是什麼？",
  "choices": {
    "A": "各式各樣的拍攝主題",
    "B": "公平自主的社會生活",
    "C": "文化中最重要的價值",
    "D": "合理的電影審查制度",
  },
  "answer": "D"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "導演認為自己失落、傷感的原因是什麼？",
  "choices": {
    "A": "他的生活一直不穩定",
    "B": "他疏忽了與親人的交流",
    "C": "他克服不了拍電影的挫折",
    "D": "他無法擺脫悲痛與憤怒的情緒",
  },
  "answer": "B"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": '47-50.png',
  "question": "文章裡提到的這部電影 ，導演想透過此電影表達什麼？",
  "choices": {
    "A": "對成功的渴望",
    "B": "對親情的 感受",
    "C": "對生活的不確定",
    "D": "對電影夢 的追求",
  },
  "answer": "B"
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