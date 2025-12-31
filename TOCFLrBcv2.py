# Test of Chinese as a Foreign Language Reading Band C (Vol.2)

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
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "費力",
        "B": "致力",
        "C": "盡力",
        "D": "努力",
    },
    "answer": "A"
    },

    {
    "id": 2,
    "type": "reading",
    "audio": [],
    "image": '1-5.png',
    "question": "",
    "choices": {
        "A": "格外",
        "B": "非得",
        "C": "毫不",
        "D": "依舊",
    },
    "answer": "B"
    },

    {
    "id": 3,
    "type": "reading",
    "audio": [],
    "image": '1-5.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "一如",
        "B": "倘若",
        "C": "即是",
        "D": "之所以",
    },
    "answer": "A"
    },

    {
    "id": 4,
    "type": "reading",
    "audio": [],
    "image": '1-5.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "不安於室",
        "B": "九死一生",
        "C": "安然無恙",
        "D": "抵死不從",
    },
    "answer": "B"
    },

    {
    "id": 5,
    "type": "reading",
    "audio": [],
    "image": '1-5.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "心事",
        "B": "心態",
        "C": "心思",
        "D": "心胸",
    },
    "answer": "C"
    },

    {
    "id": 6,
    "type": "reading",
    "audio": [],
    "image": '6-10.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "鉅細靡遺",
        "B": "無可限量",
        "C": "隨心所欲",
        "D": "斤斤計較",
    },
    "answer": "C"
    },

    {
    "id": 6,
    "type": "reading",
    "audio": [],
    "image": '6-10.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "鉅細靡遺",
        "B": "無可限量",
        "C": "隨心所欲",
        "D": "斤斤計較",
    },
    "answer": "C"
    },
    {
    "id": 7,
    "type": "reading",
    "audio": [],
    "image": '6-10.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "均勻",
        "B": "精幹",
        "C": "約略",
        "D": "縝密",
    },
    "answer": "D"
    },

    {
    "id": 8,
    "type": "reading",
    "audio": [],
    "image": '6-10.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "怎",
        "B": "卻",
        "C": "必",
        "D": "竟",
    },
    "answer": "C"
    },

    {
    "id": 9,
    "type": "reading",
    "audio": [],
    "image": '6-10.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "結晶",
        "B": "瑕疵",
        "C": "藩籬",
        "D": "包袱",
    },
    "answer": "A"
    },

    {
    "id": 10,
    "type": "reading",
    "audio": [],
    "image": '6-10.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "何況",
        "B": "可見",
        "C": "另外",
        "D": "不然",
    },
    "answer": "B"
    },

    {
    "id": 11,
    "type": "reading",
    "audio": [],
    "image": '11-15.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "肺腑",
        "B": "體魄",
        "C": "軀殼",
        "D": "骨肉",
    },
    "answer": "C"
    },

    {
    "id": 12,
    "type": "reading",
    "audio": [],
    "image": '11-15.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "佐證",
        "B": "見證",
        "C": "旁證",
        "D": "骨肉",
    },
    "answer": "A"
    },

    {
    "id": 13,
    "type": "reading",
    "audio": [],
    "image": '11-15.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "再則",
        "B": "既而",
        "C": "基於",
        "D": "即便",
    },
    "answer": "B"
    },
    {
    "id": 14,
    "type": "reading",
    "audio": [],
    "image": '11-15.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "旋即",
        "B": "驟然",
        "C": "暫且",
        "D": "剎那",
    },
    "answer": "A"
    },

    {
    "id": 15,
    "type": "reading",
    "audio": [],
    "image": '11-15.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "南轅北轍",
        "B": "川流不息",
        "C": "錦上添花",
        "D": "接踵而至",
    },
    "answer": "D"
    },

    {
    "id": 16,
    "type": "reading",
    "audio": [],
    "image": '11-15.png',
    "question": "IDKTSISTRICKY",
    "choices": {
        "A": "歸",
        "B": "料",
        "C": "致",
        "D": "及",
    },
    "answer": "C"
    },

    {
    "id": 17,
    "type": "reading",
    "audio": [],
    "image": '17.png',
    "question": "這些學校在忙些什麼？",
    "choices": {
        "A": "爭取獎學金",
        "B": "招收好學生",
        "C": "爭取教育補助費",
        "D": "送學生出國念書",
    },
    "answer": "B"
    },

    {
    "id": 18,
    "type": "reading",
    "audio": [],
    "image": '18.png',
    "question": "根據本文，下列哪一個因素最能吸引媒體注意？",
    "choices": {
        "A": "學校的知名度",
        "B": "招收學生的多寡",
        "C": "學校提供的優惠",
        "D": "學校的評鑑結果",
    },
    "answer": "C"
    },

    {
    "id": 19,
    "type": "reading",
    "audio": [],
    "image": '19.png',
    "question": "葉林的兒子就讀小學，最近騎腳踏車摔倒骨折，葉林想要幫他",
    "choices": {
        "A": "可以直接從網路提出申請",
        "B": "拿自己的身分證明去申請",
        "C": "讓兒子簽好委託書即可辦理",
        "D": "須和兒子同時到醫院櫃檯辦理",
    },
    "answer": "B"
    },

    {
    "id": 20,
    "type": "reading",
    "audio": [],
    "image": '20.png',
    "question": "小趙出車禍昏迷，他太太秀如想為他申請一份病歷影本，請問",
    "choices": {
        "A": "小趙的身分證、圖章及簽名文件",
        "B": "秀如自己的身分證、圖章及一份委託同意書",
        "C": "小趙父母和秀如的身分證、圖章及小趙簽名的同意書",
        "D": "小趙家的戶口名簿、小趙和秀如的圖章及 委託同意書",
    },
    "answer": "D"
    },

    {
    "id": 21,
    "type": "reading",
    "audio": [],
    "image": '21.png',
    "question": "這封信主要在向客戶推薦什麼項目 ？",
    "choices": {
        "A": "代繳服務",
        "B": "貸款申請",
        "C": "跨行繳費功能",
        "D": "簡訊帳單通知",
    },
    "answer": "A"
    },

    {
    "id": 22,
    "type": "reading",
    "audio": [],
    "image": '22.png',
    "question": "若小華想辦理該業務 ，他要注意什麼事情？",
    "choices": {
        "A": "每月要自行索取收據",
        "B": "每月要定期到金融機構繳款",
        "C": "繳款期限前要確定戶頭裡有錢",
        "D": "約定書上不能用轉帳帳戶的印章",
    },
    "answer": "C"
    },

    {
    "id": 23,
    "type": "reading",
    "audio": [],
    "image": '23.png',
    "question": "根據本文，從前富裕國家的勞工，為什麼能拿到不錯的薪水？",
    "choices": {
        "A": "可以領社會補助金",
        "B": "國內勞工數量不足",
        "C": "可以到國外找工作",
        "D": "普遍都有專門技術",
    },
    "answer": "B"
    },

    {
    "id": 24,
    "type": "reading",
    "audio": [],
    "image": '24-25.png',
    "question": "本文提到的失業危機，是發生在哪一種勞工身上？",
    "choices": {
        "A": "海外技術不足的勞工",
        "B": "海外具專業技術的勞工",
        "C": "富裕國家內技術不足的勞工",
        "D": "富裕國家內具專業技術的勞工",
    },
    "answer": "C"
    },

    {
    "id": 25,
    "type": "reading",
    "audio": [],
    "image": '24-25.png',
    "question": "本文主要在說什麼？",
    "choices": {
        "A": "海外勞工如何爭取補助",
        "B": "如何提高勞工的專業技術",
        "C": "全球化如何影響勞工生計",
        "D": "弱勢勞工如何申請社會補助",
    },
    "answer": "C"
    },

    {
    "id": 26,
    "type": "reading",
    "audio": [],
    "image": '26-27.png',
    "question": "作者認為，這類新聞反映出社會出現了什麼狀況？",
    "choices": {
        "A": "大家都能做到拾金不昧",
        "B": "大家不認為拾金不昧是美德",
        "C": "大家太過重視拾金不昧的行為",
        "D": "能做到拾金不昧的人其實不多",
    },
    "answer": "D"
    },

    {
    "id": 27,
    "type": "reading",
    "audio": [],
    "image": '26-27.png',
    "question": "第二段中的「這類行為」指的是什麼？",
    "choices": {
        "A": "把撿到的東西還給人家",
        "B": "把撿到的東西偷藏起來",
        "C": "把丟掉錢的事當作新聞",
        "D": "把撿到錢的事當作新聞",
    },
    "answer": "A"
    },

    {
    "id": 28,
    "type": "reading",
    "audio": [],
    "image": '28-29.png',
    "question": "作者最後表示 希望看到哪一種新聞？",
    "choices": {
        "A": "有人撿到錢並誠實歸還",
        "B": "有人撿到錢卻遲不歸還",
        "C": "大量外籍旅客來台旅遊",
        "D": "人們熱心 幫助外籍旅客",
    },
    "answer": "B"
    },

    {
    "id": 29,
    "type": "reading",
    "audio": [],
    "image": '28-29.png',
    "question": "關於中銀大廈，下列何者正確？",
    "choices": {
        "A": "外形長得像刀子",
        "B": "設計師的國籍是中國",
        "C": "鋼架本身是吉祥標誌",
        "D": "設計之初充滿佛教精神",
    },
    "answer": "A"
    },

    {
    "id": 30,
    "type": "reading",
    "audio": [],
    "image": '30-31.png',
    "question": "文章中為什麼提到港督府？",
    "choices": {
        "A": "總督想介紹風水學家給貝聿銘 認識",
        "B": "",
        "C": "讓總督來協調 貝聿銘與風水學家的矛盾",
        "D": "",
    },
    "answer": "D"
    },

    {
    "id": 31,
    "type": "reading",
    "audio": [],
    "image": '30-31.png',
    "question": "滙豐銀行業績好轉的原因是什麼？",
    "choices": {
        "A": "他們擺設了典型的風水道具",
        "B": "他們要求中銀大廈進行改建",
        "C": "他們在自己的建築物前種了植物",
        "D": "他們用砲台巧妙地化解了風水 問題",
    },
    "answer": "D"
    },

    {
    "id": 32,
    "type": "reading",
    "audio": [],
    "image": '32-33.png',
    "question": "這個網站頁面主要介紹 了什麼？",
    "choices": {
        "A": "菱角的品種及由來",
        "B": "菱角的生長 過程與環境",
        "C": "菱角對環境及人類的影響",
        "D": "菱角與不同植物所產的下一代",
    },
    "answer": "B"
    },

    {
    "id": 33,
    "type": "reading",
    "audio": [],
    "image": '32-33.png',
    "question": "第一段文字中 有關菱角的敘述，下列哪一個 不對？",
    "choices": {
        "A": "可以與動物共棲",
        "B": "需與稻米同時種植",
        "C": "在寒冷氣候中不易生存",
        "D": "適合種在濕潤的泥土地",
    },
    "answer": "B"
    },

    {
    "id": 34,
    "type": "reading",
    "audio": [],
    "image": '34-35.png',
    "question": "關於第二段文字的內容，下面哪一項是對的？",
    "choices": {
        "A": "菱角的重量越重，價格越高",
        "B": "菱角的長成最少需要四個月",
        "C": "一株幼苗大約可產 80個菱角",
        "D": "可食用的菱角是植物的花朵部分",
    },
    "answer": "A"
    },

    {
    "id": 35,
    "type": "reading",
    "audio": [],
    "image": '34-35.png',
    "question": "根據第三段文字，菱角和向日葵有什麼共通點？",
    "choices": {
        "A": "花朵有一樣的別名",
        "B": "花朵的顏色及大小相似",
        "C": "花朵都能吸引眾人的注意",
        "D": "花朵會隨太陽方位變動朝向",
    },
    "answer": "D"
    },

    {
    "id": 36,
    "type": "reading",
    "audio": [],
    "image": '36-37.png',
    "question": "作者談到以基因重組的方式來防治蚊子，其中 不包括下面哪一",
    "choices": {
        "A": "降低蚊子的抵抗力",
        "B": "破壞蚊子的嗅覺能力",
        "C": "降低蚊子的飛行能力",
        "D": "破壞蚊子的產卵功能",
    },
    "answer": "D"
    },

    {
    "id": 37,
    "type": "reading",
    "audio": [],
    "image": '36-37.png',
    "question": "根據本文，養蝌蚪來防治蚊子的方法有什麼問題？",
    "choices": {
        "A": "未來得防範野蛇",
        "B": "使青蛙數量 失衡",
        "C": "孑孓將徹底 滅絕",
        "D": "野外實施較困難",
    },
    "answer": "A"
    },

    {
    "id": 38,
    "type": "reading",
    "audio": [],
    "image": '38-39.png',
    "question": "以大肚魚來防治蚊子，要注意什麼事？",
    "choices": {
        "A": "大肚魚飼養不易",
        "B": "大肚魚的生存環境較髒亂",
        "C": "大肚魚會一併 把蝌蚪吃掉",
        "D": "大肚魚會大量繁殖並破壞生態",
    },
    "answer": "A"
    },

    {
    "id": 39,
    "type": "reading",
    "audio": [],
    "image": '38-39.png',
    "question": "在各種防治蚊子的方法中，作者 認為哪一個方法較可行 ？",
    "choices": {
        "A": "重組其基因",
        "B": "調配殺蟲劑",
        "C": "善用其天敵",
        "D": "靠人力撲殺",
    },
    "answer": "C"
    },

    {
    "id": 40,
    "type": "reading",
    "audio": [],
    "image": '40-41.png',
    "question": "如果要把「 按規定，政府每年噴的藥劑不能是同一種，以免蚊",
    "choices": {
        "A": "I",
        "B": "II",
        "C": "III",
        "D": "IV",
    },
    "answer": "B"
    },

    {
    "id": 41,
    "type": "reading",
    "audio": [],
    "image": '40-41.png',
    "question": "下面哪一項符合本文的意旨 ？",
    "choices": {
        "A": "定期記錄口感變化可有效保健",
        "B": "適當節食才是養生的不二法門",
        "C": "認知訓練法是新興的飲食風潮",
        "D": "飲食的揀擇也屬一種感官 投射",
    },
    "answer": "D"
    },

    {
    "id": 42,
    "type": "reading",
    "audio": [],
    "image": '42-43.png',
    "question": "根據本文， 「認知負荷」的概念反映出何種特點？",
    "choices": {
        "A": "可精確估算檸檬汁濃度",
        "B": "與飲食的型態息息相關",
        "C": "乃素食主義的理論根據",
        "D": "為檢測味覺記憶的指標",
    },
    "answer": "B"
    },

    {
    "id": 43,
    "type": "reading",
    "audio": [],
    "image": '42-43.png',
    "question": "若要將「 實際的飲食習慣經常與吃出健康的口號背道而馳， 」這",
    "choices": {
        "A": "I",
        "B": "II",
        "C": "III",
        "D": "IV",
    },
    "answer": "D"
    },

    {
    "id": 44,
    "type": "reading",
    "audio": [],
    "image": '44-46.png',
    "question": "文章最後「有其理據」所指為何？",
    "choices": {
        "A": "生活步調的急緩確實左右膳食傾向",
        "B": "美食品味的城鄉差異並不令人意外",
        "C": "意志鍛鍊證實可有效控制口腹之欲",
        "D": "重口味多食無益已然是不爭的事實",
    },
    "answer": "A"
    },

    {
    "id": 45,
    "type": "reading",
    "audio": [],
    "image": '44-46.png',
    "question": "若作者想根據此一研究結果進行延伸研究，下面哪一項可能是其",
    "choices": {
        "A": "從食安視角來分析文明病的生成",
        "B": "非議「倡素食、忌葷食」的論點",
        "C": "探究行為及心理活動的交互效應",
        "D": "尋找駁斥既有實驗方法的新學說",
    },
    "answer": "C"
    },

    {
    "id": 46,
    "type": "reading",
    "audio": [],
    "image": '44-46.png',
    "question": "本文指出，中國勞工階級對教育抱持著什麼樣的態度？",
    "choices": {
        "A": "堅信教育能促使貧富階級流動",
        "B": "認可教育能帶動亞洲就業市場",
        "C": "鼓吹升學教育是優良的文化傳統",
        "D": "默認留學是達官貴人享有的特權",
    },
    "answer": "A"
    },

    {
    "id": 47,
    "type": "reading",
    "audio": [],
    "image": '47-50.png',
    "question": "下列何者符合作者對 「教育狂熱」的看法？",
    "choices": {
        "A": "無可厚非",
        "B": "可圈可點",
        "C": "不以為然",
        "D": "指日可待",
    },
    "answer": "C"
    },

    {
    "id": 48,
    "type": "reading",
    "audio": [],
    "image": '47-50.png',
    "question": "如果要將「 海外學位的優勢 相較於過去早已不可同日而語， 」插",
    "choices": {
        "A": "I",
        "B": "II",
        "C": "III",
        "D": "IV",
    },
    "answer": "D"
    },

    {
    "id": 49,
    "type": "reading",
    "audio": [],
    "image": '47-50.png',
    "question": "根據專家的說法，教育狂熱可能帶來什麼樣的後果？",
    "choices": {
        "A": "國家債台高築",
        "B": "青年所學無以致用",
        "C": "企業將學歷門檻拉高",
        "D": "中產階級薪資比例失衡",
    },
    "answer": "B"
    },

    {
    "id": 50,
    "type": "reading",
    "audio": [],
    "image": '47-50.png',
    "question": "作者對中國式教育面臨的困境，提出了什麼樣的建議？",
    "choices": {
        "A": "眼不見，心不煩",
        "B": "行萬里路勝讀萬卷書",
        "C": "揚湯止沸，不如釜底抽薪",
        "D": "以其人之道，還治其人之身",
    },
    "answer": "C"
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