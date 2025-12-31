import sys
import time
import subprocess
import threading

from pathlib import Path
from termcolor import colored
from PIL import Image
from mutagen.mp3 import MP3

# Question Bank 

def get_audio_duration(audio_files, audio_dir):
    total = 0.0
    for file in audio_files:
        path = audio_dir / file
        audio = MP3(path)
        total += audio.info.length
    return int(total) + 1  # buffer for safety

questions = [
    {
  "id": 1,
  "type": "listening",
  "audio": ['1-01.mp3', '0-1.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她沒聽說文華去賭博",
    "B": "文華不抽煙，但是愛賭博",
    "C": "文華喝酒以後，就不說話",
    "D": "她不能忍受文華的壞習慣",
  },
  "answer": "D"
},

{
  "id": 2,
  "type": "listening",
  "audio": ['1-02.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "親戚",
    "B": "父女",
    "C": "兄妹",
    "D": "夫妻",
  },
  "answer": "D"
},

{
  "id": 3,
  "type": "listening",
  "audio": ['1-03.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他以為小倩要領養小孩",
    "B": "他未滿二十歲無法領養",
    "C": "他想了解認養小孩的權益",
    "D": "他對領養這件事不甚瞭解",
  },
  "answer": "A"
},

{
  "id": 4,
  "type": "listening",
  "audio": ['1-04.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "複雜的領養儀式",
    "B": "法律的先後順序",
    "C": "領養與認乾女兒的不同",
    "D": "親生父母與孩子的關係",
  },
  "answer": "C"
},

{
  "id": 5,
  "type": "listening",
  "audio": ['1-05.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "程序複雜不合乎常理",
    "B": "應遵照法律程序辦理",
    "C": "建議立法給予合理的保障",
    "D": "沒有實質效益，多此一舉",
  },
  "answer": "D"
},

{
  "id": 6,
  "type": "listening",
  "audio": ['1-06.mp3'],
  "image": None,
  "question": "這位先生說的故事裡面有什麼角色？",
  "choices": {
    "A": "（A）秀才",
    "B": "（B）瘦馬",
    "C": "（C）佳人",
    "D": "（D）肥羊",
  },
  "answer": "B"
},

{
  "id": 7,
  "type": "listening",
  "audio": ['1-07.mp3'],
  "image": None,
  "question": "當這位小姐諷刺這位先生是「酸秀才」時，他怎麼回應？",
  "choices": {
    "A": "（A）幽默詼諧",
    "B": "（B）勃然大怒",
    "C": "（C）置之不理",
    "D": "（D）反脣相譏",
  },
  "answer": "A"
},

{
  "id": 8,
  "type": "listening",
  "audio": ['1-08.mp3'],
  "image": None,
  "question": "這位小姐原本期待怎樣的故事？",
  "choices": {
    "A": "（A）惹人遐想的愛情故事",
    "B": "（B）匪夷所思的懸疑故事",
    "C": "（C）歷經風霜的勵志故事",
    "D": "（D）風趣幽默的古城遊記",
  },
  "answer": "A"
},

{
  "id": 9,
  "type": "listening",
  "audio": ['1-09.mp3'],
  "image": None,
  "question": "關於這位先生說的「故事」 ，下面哪一個是對的？",
  "choices": {
    "A": "（A）故事內容和考試有關",
    "B": "（B）故事發生的背景在現代",
    "C": "（C）故事並未交代主角怎麼受傷的",
    "D": "（D）故事結局和這位小姐的想法一致",
  },
  "answer": "C"
},

{
  "id": 10,
  "type": "listening",
  "audio": ['1-10.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "居住安全",
    "B": "大眾運輸",
    "C": "環境保護",
    "D": "土地開發",
  },
  "answer": "D"
},

{
  "id": 11,
  "type": "listening",
  "audio": ['1-11.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他預備提高居民賦稅",
    "B": "他想將空地全部標售",
    "C": "他打算和企業共同開發",
    "D": "他準備打擊飆升的房價",
  },
  "answer": "C"
},

{
  "id": 12,
  "type": "listening",
  "audio": ['1-12.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "十分實際",
    "B": "頗有遠見",
    "C": "毫無章法",
    "D": "別有居心",
  },
  "answer": "D"
},

{
  "id": 13,
  "type": "listening",
  "audio": ['1-13.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "拍攝動物靜止不動的 姿態",
    "B": "他贊同李博士的想法",
    "C": "主角都是 患病的野生動物",
    "D": "呈現動物在移動中的 速度",
  },
  "answer": "A"
},

{
  "id": 15,
  "type": "listening",
  "audio": ['1-15.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "動物園以票房決定展覽的主題",
    "B": "動物園所擁有的動物來歷不明",
    "C": "民眾體認作品所要表達的意涵",
    "D": "民眾不滿作品擺設及參觀的路線",
  },
  "answer": "C"
},

{
  "id": 16,
  "type": "listening",
  "audio": ['1-16.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "指出動物一向被囚禁",
    "B": "說明動物圈養的歷史",
    "C": "舉例說明動物的用途",
    "D": "表示寧願 為生存而戰",
  },
  "answer": "D"
},

{
  "id": 17,
  "type": "listening",
  "audio": ['1-17.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "關閉不符 合規定的動物園",
    "B": "調整動物的活動空間配置",
    "C": "重新思考 引進動物的方法",
    "D": "模擬自然生態的生存機制",
  },
  "answer": "B"
},

{
  "id": 18,
  "type": "listening",
  "audio": ['1-18.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "宣布吸收 石油價差",
    "B": "鼓勵大家多去加油",
    "C": "預告天然氣將漲價",
    "D": "說明石油漲價幅度",
  },
  "answer": "D"
},

{
  "id": 19,
  "type": "listening",
  "audio": ['1-19.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "進口成本波動",
    "B": "本月份價格不變",
    "C": "將調整計價公式",
    "D": "依進口價換算牌價",
  },
  "answer": "B"
},

{
  "id": 20,
  "type": "listening",
  "audio": ['1-20.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "預告一整年的價格",
    "B": "負擔部分 漲價價差",
    "C": "承諾天然氣不調漲",
    "D": "配合政府穩定物價",
  },
  "answer": "B"
},

{
  "id": 21,
  "type": "listening",
  "audio": ['1-21.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "同意停止調漲油價",
    "B": "表明公司將宣布破產",
    "C": "解釋必須漲價的 理由",
    "D": "告知國際 油氣的價格",
  },
  "answer": "C"
},

{
  "id": 22,
  "type": "listening",
  "audio": ['1-22.mp3'],
  "image": None,
  "question": "這項新措施的內容是什麼？",
  "choices": {
    "A": "（A）民眾可要求警方貼身保護",
    "B": "（B）民眾可透過電腦及手機報案",
    "C": "（C）民眾可查詢各區的治安狀況",
    "D": "（D）民眾可請求搬出犯罪率高的地區",
  },
  "answer": "C"
},

{
  "id": 23,
  "type": "listening",
  "audio": ['1-23.mp3'],
  "image": None,
  "question": "女記者指出，這項措施可能造成什麼問題？",
  "choices": {
    "A": "（A）犯罪者集中到犯罪熱區",
    "B": "（B）犯罪者改到其他地方作案",
    "C": "（C）警察無法控制犯罪熱區的治安",
    "D": "（D）警察只能抓到小偷之類的罪犯",
  },
  "answer": "B"
},


{
  "id": 24,
  "type": "listening",
  "audio": ['1-24.mp3'],
  "image": None,
  "question": "針對女記者提出的疑慮，市長提出什麼辦法？",
  "choices": {
    "A": "（A）大幅提高警察破案獎金",
    "B": "（B）隨時更新各區犯罪情形",
    "C": "（C）只公布犯罪率最高的地方",
    "D": "（D）獎勵民眾在第一時間報案",
  },
  "answer": "B"
},

{
  "id": 25,
  "type": "listening",
  "audio": ['1-25.mp3'],
  "image": None,
  "question": "市長為什麼認為這項措施對房價的影響不大？",
  "choices": {
    "A": "氣溫降低有短暫雨",
    "B": "受到鋒面影響會下雨",
    "C": "是適合出遊踏青的好天氣",
    "D": "早上會下雨，下午出太陽",
  },
  "answer": "A"
},

{
  "id": 26,
  "type": "listening",
  "audio": ['1-26.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "美國棒球隊要求他回國發展",
    "B": "日本球員的表現比他好得多",
    "C": "球團已經找到年輕球員遞補",
    "D": "家人及自己未來發展的問題",
  },
  "answer": "D"
},

{
  "id": 27,
  "type": "listening",
  "audio": ['1-27.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "能降低生病的機率",
    "B": "比較適合生病的人吃",
    "C": "最好在消化不良的時候吃",
    "D": "並非是保養身體的好方法",
  },
  "answer": "D"
},

{
  "id": 28,
  "type": "listening",
  "audio": ['1-28.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "推銷健康藥品",
    "B": "宣傳雜誌的廣告",
    "C": "強調維他命優點的報導",
    "D": "介紹如何保持健康的節目",
  },
  "answer": "B"
},

{
  "id": 29,
  "type": "listening",
  "audio": ['1-29.mp3'],
  "image": None,
  "question": "這個實驗怎麼進行？",
  "choices": {
    "A": "讓小孩練習畫不同的圖形",
    "B": "（B）讓小孩看情節簡單的影片",
    "C": "（C）讓小孩玩不同造型的玩具",
    "D": "（D）讓小孩跟研究人員一起玩球",
  },
  "answer": "B"
},

{
  "id": 30,
  "type": "listening",
  "audio": ['1-30.mp3'],
  "image": None,
  "question": "這個實驗證明了什麼？",
  "choices": {
    "A": "（A）小孩長大以後才能分辨善惡",
    "B": "（B）受過教育的小孩較有道德感",
    "C": "（C）人類的道德感可能是天生的",
    "D": "（D）成人的道德觀會影響小孩子",
  },
  "answer": "C"
},

{
  "id": 31,
  "type": "listening",
  "audio": ['1-31.mp3'],
  "image": None,
  "question": "這項報導為什麼提到過去心理學家們的看法？",
  "choices": {
    "A": "（A）表示實驗結果符合過去的看法",
    "B": "（B）指出未來研究打算進行的方向",
    "C": "（C）指出這項研究設計不良的地方",
    "D": "（D）指出研究結果不支持舊的理論",
  },
  "answer": "D"
},

{
  "id": 32,
  "type": "listening",
  "audio": ['1-32.mp3'],
  "image": None,
  "question": "「奇想病人」這齣戲描寫的是哪一種人？",
  "choices": {
    "A": "（A）很想當演員的人",
    "B": "（B）沒有錢看病的人",
    "C": "（C）有病卻不看醫生的人",
    "D": "（D）老以為自己生病的人",
  },
  "answer": "D"
},

{
  "id": 33,
  "type": "listening",
  "audio": ['1-33.mp3'],
  "image": None,
  "question": "這天晚上，這位在台上演出的演員怎麼樣？",
  "choices": {
    "A": "（A）很會騙人",
    "B": "（B）真的生病",
    "C": "（C）害死了別人",
    "D": "（D）一點病都沒有",
  },
  "answer": "B"
},

{
  "id": 34,
  "type": "listening",
  "audio": ['1-34.mp3'],
  "image": None,
  "question": "關於這個故事，哪一個是對的？",
  "choices": {
    "A": "（A）作家最後死了",
    "B": "（B）演員最後沒死",
    "C": "（C）作家的太太上台演出",
    "D": "（D）觀眾覺得演員演得很差",
  },
  "answer": "A"
},

{
  "id": 35,
  "type": "listening",
  "audio": ['1-35.mp3'],
  "image": None,
  "question": "這位先生認為台灣記者怎麼樣？",
  "choices": {
    "A": "（A）有些自大",
    "B": "（B）缺乏信心",
    "C": "（C）非常專業",
    "D": "（D）很有道德",
  },
  "answer": "A"
},

{
  "id": 36,
  "type": "listening",
  "audio": ['2-36.mp3'],
  "image": None,
  "question": "這段話為什麼用老虎來形容記者？",
  "choices": {
    "A": "（A）能不畏強權，堅持事實",
    "B": "（B）能寫出一流的頭條新聞",
    "C": "不管消息真假，什麼都報導",
    "D": "（D）文筆不好，讀者閱讀有困難",
  },
  "answer": "C"
},

{
  "id": 37,
  "type": "listening",
  "audio": ['2-37.mp3'],
  "image": None,
  "question": "這段話為什麼用狗來形容記者？",
  "choices": {
    "A": "（A）能忠實報導各種新聞",
    "B": "（B）追查線索，相當仔細",
    "C": "（C）報導不公，向權勢低頭",
    "D": "（D）只報導地方新聞，沒有遠見",
  },
  "answer": "C"
},

{
  "id": 38,
  "type": "listening",
  "audio": ['2-38.mp3'],
  "image": None,
  "question": "最後這位先生舉了一個例子，裡頭的記者犯了什麼錯？",
  "choices": {
    "A": "（A）報導寫得太短",
    "B": "（B）只報導財經新聞",
    "C": "（C）只報導不重要的部分",
    "D": "（D）報導內容前後不一致",
  },
  "answer": "D"
},

{
  "id": 39,
  "type": "listening",
  "audio": ['2-39.mp3'],
  "image": None,
  "question": "根據這段話，關於社交網站，下面哪一個是對的？",
  "choices": {
    "A": "（A）提供推銷自己的機會",
    "B": "（B）保證能最快找到工作",
    "C": "（C）社會經濟越好越流行",
    "D": "（D）能解決多數失業問題",
  },
  "answer": "A"
},

{
  "id": 40,
  "type": "listening",
  "audio": ['2-40.mp3'],
  "image": None,
  "question": "根據這段話，為什麼社交網站有助於求職？",
  "choices": {
    "A": "（A）能快速累積創業資金",
    "B": "（B）能大量刊登求職廣告",
    "C": "（C）能培養人脈、爭取機會",
    "D": "（D）能學習他人求職的經驗",
  },
  "answer": "C"
},

{
  "id": 41,
  "type": "listening",
  "audio": ['2-41.mp3'],
  "image": None,
  "question": "關於專家提供的求職建議，下面哪一項是對的？",
  "choices": {
    "A": "（A）使用關鍵字增加曝光率",
    "B": "（B）介紹內容簡單明瞭就好",
    "C": "（C）一開始加入越多網站越好",
    "D": "（D）用網站求職只適用於特定職業",
  },
  "answer": "A"
},

{
  "id": 42,
  "type": "listening",
  "audio": ['2-42.mp3'],
  "image": None,
  "question": "根據這段話，投資型社交網站有什麼缺點？",
  "choices": {
    "A": "（A）無法掌握投資狀況",
    "B": "（B）使用者多半是失業族",
    "C": "（C）投資虧損的金額過高",
    "D": "（D）消息來源不完全可靠",
  },
  "answer": "D"
},

{
  "id": 43,
  "type": "listening",
  "audio": ['2-43.mp3'],
  "image": None,
  "question": "為什麼這篇報導說黑洞是終極食客？",
  "choices": {
    "A": "（A）因為黑洞能影響生命存在",
    "B": "（B）因為黑洞連自己都會吞噬",
    "C": "（C）因為黑洞瘋狂吸收周遭物質",
    "D": "（D）因為黑洞存在於每個星系中",
  },
  "answer": "C"
},

{
  "id": 44,
  "type": "listening",
  "audio": ['2-44.mp3'],
  "image": None,
  "question": "說話者認為「洗衣機」在哪方面足以比擬「負載循環」原理？",
  "choices": {
    "A": "（A）兩者運行狀態相似",
    "B": "（B）兩者都會高速旋轉",
    "C": "（C）兩者都會排出物體",
    "D": "（D）兩者都具有洗滌功能",
  },
  "answer": "A"
},

{
  "id": 45,
  "type": "listening",
  "audio": ['2-45.mp3'],
  "image": None,
  "question": "說話者以排水過程說明黑洞的何種狀態？",
  "choices": {
    "A": "（A）聲波產生的原因",
    "B": "（B）物質撞擊的情況",
    "C": "（C）黑洞爆炸的成因",
    "D": "（D）黑洞噴射物質的現象",
  },
  "answer": "D"
},

{
  "id": 46,
  "type": "listening",
  "audio": ['2-46.mp3'],
  "image": None,
  "question": "這個報導的重點是什麼？",
  "choices": {
    "A": "（A）黑洞形成的原因",
    "B": "（B）黑洞運動的狀態",
    "C": "（C）黑洞毀滅的成因",
    "D": "（D）黑洞吞噬物質的原理",
  },
  "answer": "B"
},

{
  "id": 47,
  "type": "listening",
  "audio": ['2-47.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）一般大眾",
    "B": "（B）神經心理學家",
    "C": "（C）腦部重症病患",
    "D": "（D）實驗室研究員",
  },
  "answer": "A"
},

{
  "id": 48,
  "type": "listening",
  "audio": ['2-48.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）他們比較專注科學試驗",
    "B": "（B）所有產品皆經過科學測試",
    "C": "（C）設計團隊成員皆為科學家",
    "D": "（D）產品依使用者的回饋調校修正",
  },
  "answer": "B"
},

{
  "id": 49,
  "type": "listening",
  "audio": ['2-49.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）才剛上市推出",
    "B": "（B）尚未通過臨床研究分析",
    "C": "（C）能依用戶的能力自動調整",
    "D": "（D）使用有效期為五至十二星期",
  },
  "answer": "C"
},

{
  "id": 50,
  "type": "listening",
  "audio": ['2-50.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）說明研發過程嚴謹",
    "B": "（B）強調使用族群普及",
    "C": "（C）凸顯公司財力雄厚",
    "D": "（D）舉證軟體效果顯著",
  },
  "answer": "D"
},
]

# PATHS
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio_ba_vol3"
IMAGE_DIR = BASE_DIR / "image_lba_vol3"

# HELPERS
def normalize_audios(q):
    audios = q.get("audios") or q.get("audio")
    if audios is None:
        raise ValueError(f"Question {q['id']} missing audio")

    if isinstance(audios, str):
        audios = [audios]

    flat = []
    for a in audios:
        if isinstance(a, list):
            flat.extend(a)
        else:
            flat.append(a)

    q["audios"] = flat


def get_audio_duration(audio_files):
    total = 0.0
    for file in audio_files:
        audio = MP3(AUDIO_DIR / file)
        total += audio.info.length
    return int(total) + 1


def play_audio_sequence(audio_files, done_flag):
    for file in audio_files:
        subprocess.call(
            ["afplay", str(AUDIO_DIR / file)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    done_flag.append(True)  # signal audio finished


def live_countdown(duration, done_flag):
    start = time.time()

    while True:
        elapsed = int(time.time() - start)
        remaining = max(duration - elapsed, 0)

        sys.stdout.write(
            f"\r{colored('Answer in', 'yellow')} ({remaining}) "
        )
        sys.stdout.flush()

        if remaining == 0 and done_flag:
            break

        time.sleep(1)

    print()


# NORMALIZE QUESTIONS
score = 0
for q in questions:
    normalize_audios(q)

# EXAM LOOP
for q in questions:
    print(colored(f"\n🎧 Listening Question {q['id']}", "cyan"))

    # IMAGE
    if q.get("image"):
        img_path = IMAGE_DIR / q["image"]
        if img_path.exists():
            Image.open(img_path).show()

    # CHECK AUDIO FILES
    for a in q["audios"]:
        if not (AUDIO_DIR / a).exists():
            print(colored(f"❌ Missing audio: {a}", "red"))
            print(colored("⏭ Skipping question.", "yellow"))
            continue

    print(colored("🔊 Playing audio...", "yellow"))

    # AUDIO THREAD
    audio_done = []
    audio_thread = threading.Thread(
        target=play_audio_sequence,
        args=(q["audios"], audio_done),
        daemon=True
    )
    audio_thread.start()

    # COUNTDOWN (RUNS WITH AUDIO)
    duration = get_audio_duration(q["audios"])
    live_countdown(duration, audio_done)

    # SHOW QUESTION
    print(colored("\n" + q.get("question", ""), "white"))
    for k, v in q["choices"].items():
        print(f"  ({k}) {v}")

    options = "/".join(q["choices"].keys())

    while True:
        user_answer = input(
            colored(f"\n👉 Your answer ({options}): ", "cyan")
        ).strip().upper()

        if user_answer in q["choices"]:
            break

        print(colored(f"⚠️ Please enter {options} only.", "yellow"))

    # CHECK ANSWER
    if user_answer == q["answer"]:
        print(colored("✅ Correct!", "green"))
        score += 1
    else:
        print(colored(f"❌ Wrong: Correct answer [{q['answer']}]", "red"))

# FINAL SCORE
print(colored(f"\n🎯 Final Score: {score} / {len(questions)}", "magenta"))