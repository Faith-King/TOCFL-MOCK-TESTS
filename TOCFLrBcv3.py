# Test of Chinese as a Foreign Language Reading Band C (Vol.3)

from termcolor import colored
from pathlib import Path
import subprocess
import platform

# PATH SETUP
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "image_bc_vol3"

# Question Bank (EXAMPLE)
questions = [
    {
  "id": 1,
  "type": "reading",
  "audio": [],
  "image": '1-6.png',
  "question": "",
  "choices": {
    "A": "一帶",
    "B": "一塊",
    "C": "一區",
    "D": "一處",
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
    "A": "然而",
    "B": "而且",
    "C": "可見",
    "D": "因而",
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
    "A": "為了…就是…",
    "B": "不僅…還是…",
    "C": "即使…也是…",
    "D": "雖然…也是…",
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
    "A": "支付",
    "B": "給予",
    "C": "贈送",
    "D": "提供",
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
    "A": "過少",
    "B": "過癮",
    "C": "過分",
    "D": "過量",
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
    "A": "無益",
    "B": "無意",
    "C": "無所謂",
    "D": "無可奈何",
  },
  "answer": "C"
},

{
  "id": 7,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "里程碑",
    "B": "單行道",
    "C": "出發點",
    "D": "低潮期",
  },
  "answer": "D"
},

{
  "id": 8,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "怦然心動",
    "B": "黯淡無光",
    "C": "百感交集",
    "D": "匪夷所思",
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
    "A": "不料",
    "B": "反之",
    "C": "未免",
    "D": "據悉",
  },
  "answer": "A"
},

{
  "id": 10,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "一旦",
    "B": "縱使",
    "C": "之所以",
    "D": "以致於",
  },
  "answer": "B"
},

{
  "id": 11,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "纏",
    "B": "揪",
    "C": "鑲",
    "D": "編",
  },
  "answer": "A"
},

{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '7-12.png',
  "question": "",
  "choices": {
    "A": "苛責",
    "B": "詛咒",
    "C": "警訊",
    "D": "磨難",
  },
  "answer": "D"
},

{
  "id": 13,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "裝瘋賣傻",
    "B": "牙牙學語",
    "C": "含飴弄孫",
    "D": "少年老成",
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
    "A": "固然",
    "B": "儼然",
    "C": "縱然",
    "D": "斷然",
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
    "A": "囈語",
    "B": "蜚語",
    "C": "標語",
    "D": "警語",
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
    "A": "仰臥",
    "B": "蜷縮",
    "C": "聳立",
    "D": "盤旋",
  },
  "answer": "B"
},

{
  "id": 17,
  "type": "reading",
  "audio": [],
  "image": '13-18.png',
  "question": "",
  "choices": {
    "A": "想必",
    "B": "姑且",
    "C": "恰似",
    "D": "不巧",
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
    "A": "質問",
    "B": "預言",
    "C": "緬懷",
    "D": "慨歎",
  },
  "answer": "D"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '19-22.png',
  "question": "小熊隊球迷舉的牌子，向球隊傳達了什麼訊息？",
  "choices": {
    "A": "我們今年一定贏",
    "B": "今年別輸得太難看",
    "C": "今年輸了也沒關係",
    "D": "明年會和今年一樣好",
  },
  "answer": "C"
},

{
  "id": 20,
  "type": "reading",
  "audio": [],
  "image": '19-22.png',
  "question": "第二段提到 的「他們」指的是誰？",
  "choices": {
    "A": "對小熊隊忠誠的球迷",
    "B": "注意到明星球員的民眾",
    "C": "表現優異的台灣運動員",
    "D": "台灣運動員所屬的球隊",
  },
  "answer": "C"
},

{
  "id": 21,
  "type": "reading",
  "audio": [],
  "image": '19-22.png',
  "question": "作者說，台灣民眾觀看運動員和球賽的心態是什麼？",
  "choices": {
    "A": "有贏有輸比賽才好看",
    "B": "因為球員贏了才支持",
    "C": "即使球員贏了也沒什麼",
    "D": "就算球員輸了也依舊支持",
  },
  "answer": "B"
},

{
  "id": 22,
  "type": "reading",
  "audio": [],
  "image": '19-22.png',
  "question": "本文從哪個角度來比較台灣和美國的球迷？",
  "choices": {
    "A": "球迷如何幫球隊宣傳",
    "B": "球迷如何選出明星球員",
    "C": "球迷是否注意媒體報導",
    "D": "球迷是否在乎球賽輸贏",
  },
  "answer": "D"
},

{
  "id": 23,
  "type": "reading",
  "audio": [],
  "image": '23-26.png',
  "question": "關於自然人憑證卡，下面哪一項是正確的？",
  "choices": {
    "A": "可以終身使用",
    "B": "小學生也可以申請",
    "C": "重辦費用不到三百元",
    "D": "重辦後的卡片可再使用五年",
  },
  "answer": "C"
},

{
  "id": 24,
  "type": "reading",
  "audio": [],
  "image": '23-26.png',
  "question": "申請步驟中說了什麼？",
  "choices": {
    "A": "由承辦人員填寫申請書",
    "B": "申請人可以請他人幫忙申請",
    "C": "申請人無法當天取回身分證件",
    "D": "先填寫申請書，再印製憑證卡",
  },
  "answer": "D"
},

{
  "id": 25,
  "type": "reading",
  "audio": [],
  "image": '23-26.png',
  "question": "什麼人最適合申請自然人憑證卡？",
  "choices": {
    "A": "剛出生的嬰兒",
    "B": "在國內工作的外籍人士",
    "C": "不需使用政府相關業務的人",
    "D": "沒時間到政府機關辦事的人",
  },
  "answer": "D"
},

{
  "id": 26,
  "type": "reading",
  "audio": [],
  "image": '23-26.png',
  "question": "這個申辦說明中的「風險」 指的是什麼？",
  "choices": {
    "A": "在網路上個人身分被盜用",
    "B": "前往政府機關的交通問題",
    "C": "在網路上傳資料容易失敗",
    "D": "申請自然人憑證缺乏保障",
  },
  "answer": "A"
},

{
  "id": 27,
  "type": "reading",
  "audio": [],
  "image": '27-30.png',
  "question": "這段短文的主題是關於風箏的什麼？",
  "choices": {
    "A": "功能",
    "B": "由來",
    "C": "種類",
    "D": "製作",
  },
  "answer": "B"
},

{
  "id": 28,
  "type": "reading",
  "audio": [],
  "image": '27-30.png',
  "question": "根據這篇短文，風箏的起源為何 ？",
  "choices": {
    "A": "元朝時才發明的",
    "B": "自西方傳入中國",
    "C": "至今還沒有定論",
    "D": "宋朝陸佃發明的",
  },
  "answer": "C"
},

{
  "id": 29,
  "type": "reading",
  "audio": [],
  "image": '27-30.png',
  "question": "中國正史上初次記載風箏的製作是什麼時候 ？",
  "choices": {
    "A": "楚漢相爭時",
    "B": "南朝侯景發明的",
    "C": "工匠祖師公輸班",
    "D": "羊侃建議梁武帝製作的",
  },
  "answer": "D"
},

{
  "id": 30,
  "type": "reading",
  "audio": [],
  "image": '27-30.png',
  "question": "根據歷史記載，下面哪個名稱就是現在的「風箏」 ？",
  "choices": {
    "A": "竹箏",
    "B": "飛鳶",
    "C": "紙鳶",
    "D": "鷂鷹",
  },
  "answer": "C"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '31-34.png',
  "question": "根據本文，關於臺灣的觀光工廠，下面哪一項說明正確 ?",
  "choices": {
    "A": "非常受外籍遊客歡迎",
    "B": "目前還沒引起政府重視",
    "C": "起初是由德國商人輔導建立的",
    "D": "目的是搶救即將消失的製造業",
  },
  "answer": "D"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '31-34.png',
  "question": "根據第二段的說明，第二代被「掃地出門」的理由是什麼 ?",
  "choices": {
    "A": "始終拒絕改造工廠",
    "B": "得不到員工的支持",
    "C": "搶走了長輩的生意",
    "D": "無法和上一代經營者溝通",
  },
  "answer": "D"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '31-34.png',
  "question": "對想轉型成觀光工廠的製造業老闆來說，最難克服的問題是什麼 ?",
  "choices": {
    "A": "公開產品的生產過程",
    "B": "尋找建設的成本資金",
    "C": "改變經營模式與價值觀",
    "D": "年輕人多排斥從事服務業",
  },
  "answer": "C"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '31-34.png',
  "question": "關於臺灣的觀光工廠，作者在文章最後表達了什麼看法 ?",
  "choices": {
    "A": "能有效刺激民眾消費",
    "B": "流行風氣很快就消失了",
    "C": "多數沒有妥善的經營策略",
    "D": "參考外國的做法才有機會成功",
  },
  "answer": "A"
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '35-39.png',
  "question": "根據第二段，目前徵收的道路費用有什麼不合理的地方？",
  "choices": {
    "A": "沒有加收保險費",
    "B": "很少人使用的道路不用收費",
    "C": "牌照稅、燃料稅的費用太高",
    "D": "沒考慮到開車的次數或距離",
  },
  "answer": "D"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": '35-39.png',
  "question": "根據第三段，這個新觀念如何改善交通？",
  "choices": {
    "A": "使民眾盡量不在尖峰時間出門",
    "B": "對近七成的民眾提供收費折扣",
    "C": "民眾在同一時間上路，易於管理",
    "D": "民眾經常使用的道路，降低收費",
  },
  "answer": "A"
},

{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": '35-39.png',
  "question": "根據第四段，這個新觀念為什麼對環保有幫助？",
  "choices": {
    "A": "禁止高污染的貨車上路",
    "B": "高污染貨車開越多付越多",
    "C": "低污染的大貨車可免費上路",
    "D": "其他車種免費，只針對貨車收費",
  },
  "answer": "B"
},

{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": '35-39.png',
  "question": "根據最後一段，保險公司怎麼調整保險費？",
  "choices": {
    "A": "將保險費降低 30%",
    "B": "將民眾的駕駛習慣列入考慮",
    "C": "經常開車的人，保險費比較便宜",
    "D": "對愛開快車的人，取消保險資格",
  },
  "answer": "B"
},

{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": '35-39.png',
  "question": "作者指出，推動這個新觀念時會遇到什麼困難？",
  "choices": {
    "A": "花費太高",
    "B": "民眾不配合",
    "C": "保險費太貴",
    "D": "交通意外太多",
  },
  "answer": "A"
},

{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": '40-44.png',
  "question": "第一段主要在說什麼？",
  "choices": {
    "A": "台灣的失業率越來越高",
    "B": "打工的年輕人越來越少",
    "C": "沒有正式職業的人數增 加",
    "D": "教育程度低的人找不到工作",
  },
  "answer": "C"
},

{
  "id": 41,
  "type": "reading",
  "audio": [],
  "image": '40-44.png',
  "question": "根據第二段，台灣這幾年的非典型就業人口有什麼變化？",
  "choices": {
    "A": "學歷都不高",
    "B": "越來越年輕",
    "C": "多半是中老年人",
    "D": "集中在弱勢族群",
  },
  "answer": "B"
},

{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": '40-44.png',
  "question": "根據第二段，近年來非典型就業人數上升的原因是什麼？",
  "choices": {
    "A": "大企業不願招募正式員工",
    "B": "大企業偏好剛畢業的年輕人",
    "C": "大企業不願意僱用臨時人員",
    "D": "大企業對員工的學歷要求很高",
  },
  "answer": "A"
},

{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": '40-44.png',
  "question": "第三段用日本及韓國的狀況來說明什麼？",
  "choices": {
    "A": "亞洲企業和美國企業不同",
    "B": "台灣和其他亞洲國家不同",
    "C": "亞洲和美國呈現一致的趨勢",
    "D": "亞洲各國的經濟狀況不穩定",
  },
  "answer": "C"
},

{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": '40-44.png',
  "question": "根據最後一段，營造業的情況怎麼樣？",
  "choices": {
    "A": "經常招募臨時人員",
    "B": "人力充足，不缺員工",
    "C": "非典型就業的人數最少",
    "D": "正式員工的比例逐年上升",
  },
  "answer": "A"
},

{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": '45-50.png',
  "question": "如果要把「 年輕人以為手裏拿的包包越貴、腳下穿的鞋越頂級、",
  "choices": {
    "A": "I",
    "B": "II",
    "C": "III",
    "D": "IV",
  },
  "answer": "B"
},

{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": '45-50.png',
  "question": "第一段主要在說什 麼？",
  "choices": {
    "A": "設計師如何主宰流行趨勢",
    "B": "年輕族群如何改變流行趨勢",
    "C": "流行趨勢如何改變街頭文化",
    "D": "上流品牌如何吸引年輕人注意",
  },
  "answer": "B"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": '45-50.png',
  "question": "關於 50、60年代的流行風格，哪一項是對的？",
  "choices": {
    "A": "富於叛逆的精神",
    "B": "由頂尖設計師主導",
    "C": "深受上流社會的影響",
    "D": "繼承傳統的時尚風格",
  },
  "answer": "A"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": '45-50.png',
  "question": "根據第一段，設計師們 的設計方向為什麼有所轉變？",
  "choices": {
    "A": "因為貴族逐漸沒落",
    "B": "因為傳統工藝受到重視",
    "C": "因為設計師勇於挑戰權威",
    "D": "因為街頭文化充滿創造力",
  },
  "answer": "D"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": '45-50.png',
  "question": "作者認為，流行 名牌產品對目前的 年輕人產生什麼樣的影響？",
  "choices": {
    "A": "有效刺激年輕人的創造力",
    "B": "讓年輕人只知模仿成人的風格",
    "C": "讓年輕人集體反抗成人的價值觀",
    "D": "有助年輕人理解時尚發展的歷史",
  },
  "answer": "B"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": '45-50.png',
  "question": "作者認為年輕人應該怎麼樣？",
  "choices": {
    "A": "穿著不要過分奇特",
    "B": "要從傳統中吸取經驗",
    "C": "要大量觀摩名牌作品",
    "D": "儘量創造自己的特色",
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