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
  "audio": ['001.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "原來小張出國工作了",
    "B": "原來小張去環遊世界了",
    "C": "原來小張最近都忙著工作",
    "D": "原來小張年底要離開公司",
  },
  "answer": "C"
},

    {
  "id": 2,
  "type": "listening",
  "audio": ['002.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "開別人玩笑會讓人生氣",
    "B": "這位先生講的笑話不好笑",
    "C": "這位先生不必為了玩笑而生氣",
    "D": "她不想被別人當成開玩笑的對象",
  },
  "answer": "C"
},

{
  "id": 3,
  "type": "listening",
  "audio": ['003.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "要小李放棄追求那位美女",
    "B": "想追求那位美女的話，得趕快行動",
    "C": "小李必須多存點錢，才能追到那位美女",
    "D": "要小李直接去找那位美女，不要透過電話",
  },
  "answer": "A"
},

{
  "id": 4,
  "type": "listening",
  "audio": ['004.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "教練不可能不急",
    "B": "看不出來教練很急",
    "C": "情況越來越糟，教練很擔心",
    "D": "教練有教練的打算，用不著操心",
  },
  "answer": "D"
},

{
  "id": 5,
  "type": "listening",
  "audio": ['005.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他很受學生歡迎",
    "B": "他不准學生失敗",
    "C": "學生很難見得到他",
    "D": "像他這樣的人不算少",
  },
  "answer": "A"
},

{
  "id": 6,
  "type": "listening",
  "audio": ['006.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "難得參加活動",
    "B": "竟然參加活動",
    "C": "像他這麼熱心的人不多了",
    "D": "應該像他一樣地熱心才對",
  },
  "answer": "C"
},

{
  "id": 7,
  "type": "listening",
  "audio": ['007.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "有一位團員不能準時抵達",
    "B": "有一位團員下午三點才會到",
    "C": "訪問團的團員無法在下午三點抵達",
    "D": "團員人數比這位先生預期的少一位",
  },
  "answer": "D"
},

{
  "id": 8,
  "type": "listening",
  "audio": ['008.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "狠狠地教訓小陳一頓就夠了",
    "B": "不要再把車借給小陳就好了",
    "C": "與其生氣，不如跟小陳溝通",
    "D": "先確定車子是不是小陳開走的再說",
  },
  "answer": "C"
},

{
  "id": 9,
  "type": "listening",
  "audio": ['009.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他不喜歡背誦古典詩詞",
    "B": "他覺得詩人太容易感慨",
    "C": "他覺得自己沒有同理心",
    "D": "他覺得古典詩詞太拗口",
  },
  "answer": "B"
},

{
  "id": 10,
  "type": "listening",
  "audio": ['010.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "作者的生平事蹟",
    "B": "賞析詩文的方法",
    "C": "詩文的翻譯內容",
    "D": "註解詩文的名家",
  },
  "answer": "B"
},

{
  "id": 11,
  "type": "listening",
  "audio": ['011.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "當代詩人應競相模仿",
    "B": "寫詩之人的感受力強",
    "C": "詩詞文句如錦繡華服",
    "D": "詩詞內容多悲風秋月",
  },
  "answer": "D"
},

{
  "id": 12,
  "type": "listening",
  "audio": ['012.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "不置一詞",
    "B": "曲高和寡",
    "C": "有口皆碑",
    "D": "曇花一現",
  },
  "answer": "C"
},

{
  "id": 13,
  "type": "listening",
  "audio": ['013.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "高明的行銷技巧",
    "B": "刊登內容嚴格把關",
    "C": "積極和廣告商合作",
    "D": "不定期舉辦各類抽獎活動",
  },
  "answer": "B"
},

{
  "id": 14,
  "type": "listening",
  "audio": ['014.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "不對大眾開放",
    "B": "不舉辦任何活動",
    "C": "不擴大網站規模",
    "D": "不以營利為目的",
  },
  "answer": "D"
},

{
  "id": 15,
  "type": "listening",
  "audio": ['015.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "尋找贊助商",
    "B": "增加文章量",
    "C": "多元化經營",
    "D": "和公益團體合作",
  },
  "answer": "C"
},

{
  "id": 16,
  "type": "listening",
  "audio": ['016.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "評估「過動症」的量表有重大瑕疵",
    "B": "「過動症」患者的病徵與外在表現",
    "C": "確診「過動症」的患者以兒童居多",
    "D": "大眾對「過動症」患者的刻板印象",
  },
  "answer": "B"
},

{
  "id": 17,
  "type": "listening",
  "audio": ['017.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "家長仍舊刻意忽視此病症",
    "B": "目前醫學仍無法解釋病症成因",
    "C": "透過診斷，病童能獲得適當治療",
    "D": "此病症讓精神醫學往前跨一大步",
  },
  "answer": "C"
},

{
  "id": 18,
  "type": "listening",
  "audio": ['018.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "質疑團體教育已經不合時宜",
    "B": "反對從醫學角度理解這個病症",
    "C": "批評家長只會讓患者吃藥了事",
    "D": "認為應該從教學著手改善的方法",
  },
  "answer": "D"
},

{
  "id": 19,
  "type": "listening",
  "audio": ['019.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "指出家長過度依賴醫學診斷",
    "B": "說明醫生僅能從醫學診療著手",
    "C": "質疑這位先生對特殊學童的態度",
    "D": "批評這位先生扭曲了醫學的本義",
  },
  "answer": "B"
},

{
  "id": 20,
  "type": "listening",
  "audio": ['020.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "延長壽命的方法",
    "B": "平均壽命延長的原因",
    "C": "平均壽命計算的方式",
    "D": "全球男女的平均壽命值",
  },
  "answer": "B"
},

{
  "id": 21,
  "type": "listening",
  "audio": ['021.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "令人愉悅",
    "B": "不值一提",
    "C": "內容不完全",
    "D": "可信度令人懷疑",
  },
  "answer": "C"
},

{
  "id": 22,
  "type": "listening",
  "audio": ['022.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "醫療品質",
    "B": "保險制度",
    "C": "長照體系",
    "D": "老齡生活",
  },
  "answer": "D"
},

{
  "id": 23,
  "type": "listening",
  "audio": ['023.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "開始全面關照老年失智的問題",
    "B": "已經擬定好年長者的照護制度",
    "C": "已經開始著手興建大型養老院",
    "D": "投入大量經費，優化醫療環境",
  },
  "answer": "B"
},

{
  "id": 24,
  "type": "listening",
  "audio": ['024.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "虛情假意",
    "B": "肝膽相照",
    "C": "委曲求全",
    "D": "杯弓蛇影",
  },
  "answer": "A"
},

{
  "id": 25,
  "type": "listening",
  "audio": ['025.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "舉辭典例句來解釋",
    "B": "從詞語的出處來解釋",
    "C": "從現代人的用法來解釋",
    "D": "逐字解釋每個字的意思",
  },
  "answer": "B"
},

{
  "id": 26,
  "type": "listening",
  "audio": ['026.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "音讀",
    "B": "出處",
    "C": "詞性",
    "D": "語意",
  },
  "answer": "D"
},

{
  "id": 27,
  "type": "listening",
  "audio": ['027.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他斷章取義",
    "B": "他考證不實",
    "C": "他沒有旁徵博引",
    "D": "他沒有舉一反三",
  },
  "answer": "A"
},

{
  "id": 28,
  "type": "listening",
  "audio": ['028.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "能降低採礦成本",
    "B": "能避免血汗勞動爭議",
    "C": "人造鑽石將被大量製造",
    "D": "人造鑽石完全能以假亂真",
  },
  "answer": "C"
},

{
  "id": 29,
  "type": "listening",
  "audio": ['029.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "將掀起市場的價格戰",
    "B": "無法與人類的情感相互共鳴",
    "C": "將改變多數人對鑽石的印象",
    "D": "人們會更關注天然鑽石的稀有性",
  },
  "answer": "B"
},

{
  "id": 30,
  "type": "listening",
  "audio": ['030.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "批判一般人盲目從眾的心理狀態",
    "B": "指出人們對「美好概念」的嚮往",
    "C": "困惑高單價產品和成本間的關係",
    "D": "諷刺天然鑽石價值已被過度吹捧",
  },
  "answer": "D"
},

{
  "id": 31,
  "type": "listening",
  "audio": ['031.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "價格天差地遠",
    "B": "本質始終如一",
    "C": "人造鑽石，幾可亂真",
    "D": "天然鑽石，沽名釣譽",
  },
  "answer": "B"
},

{
  "id": 32,
  "type": "listening",
  "audio": ['032.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為多數人會採取行動",
    "B": "因為善意是經過學習而來的",
    "C": "因為救人的思維與步驟具因果關係",
    "D": "因為人們可以清楚說明救人的依據",
  },
  "answer": "A"
},

{
  "id": 33,
  "type": "listening",
  "audio": ['033.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "反駁研究報告的結論",
    "B": "補充研究者提出的原則",
    "C": "總結研究者提出的論點",
    "D": "主要說明研究報告的內容",
  },
  "answer": "A"
},

{
  "id": 34,
  "type": "listening",
  "audio": ['034.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為意圖本身無法被驗證",
    "B": "因為善意是經由後天培養",
    "C": "因為每個人思考的面向不一",
    "D": "因為每個人對意圖的解釋不同",
  },
  "answer": "C"
},

{
  "id": 35,
  "type": "listening",
  "audio": ['035.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "人善被人欺",
    "B": "為善不欲人知",
    "C": "勿以善小而不為",
    "D": "人無善與不善之分",
  },
  "answer": "C"
},

{
  "id": 36,
  "type": "listening",
  "audio": ['036.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她文采洋溢",
    "B": "她足智多謀",
    "C": "她擁有傾國之姿",
    "D": "她在宮中樹大根深",
  },
  "answer": "B"
},

{
  "id": 37,
  "type": "listening",
  "audio": ['037.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "見風轉舵",
    "B": "長袖善舞",
    "C": "臥薪嘗膽",
    "D": "韜光養晦",
  },
  "answer": "B"
},

{
  "id": 38,
  "type": "listening",
  "audio": ['038.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "十分稱職",
    "B": "個性溫婉",
    "C": "過於固執",
    "D": "言語粗鄙",
  },
  "answer": "A"
},

{
  "id": 39,
  "type": "listening",
  "audio": ['039.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她受不了摯愛丈夫的辭世",
    "B": "囿於丈夫對她長久的壓迫",
    "C": "肇因於她想登上帝位的想法",
    "D": "她無法接受世人對她的指指點點",
  },
  "answer": "C"
},

{
  "id": 40,
  "type": "listening",
  "audio": ['040.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "同情武則天一生坎坷的際遇",
    "B": "說明武則天的後世以她為榮",
    "C": "讚許武則天勇敢地展現了自我",
    "D": "指出武則天的作為無法被認同",
  },
  "answer": "D"
},

{
  "id": 41,
  "type": "listening",
  "audio": ['041.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "擯棄一切作為，和疾病和平共處",
    "B": "相信醫師的專業，就是健康的保障",
    "C": "疾病是種厄運，要以超自然力量驅逐",
    "D": "鍛鍊心靈的力量，能突破治療的侷限",
  },
  "answer": "D"
},

{
  "id": 42,
  "type": "listening",
  "audio": ['042.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "加強疾病預防的意識",
    "B": "提高病患對醫師的信任",
    "C": "加速醫學新技術的突破",
    "D": "減低維護個人健康的壓力",
  },
  "answer": "A"
},

{
  "id": 43,
  "type": "listening",
  "audio": ['043.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "促使病患濫用醫療資源",
    "B": "可能導致醫病關係的衝突",
    "C": "病患可能因疾病而受到批判",
    "D": "病患容易選擇錯誤的治療方向",
  },
  "answer": "C"
},

{
  "id": 44,
  "type": "listening",
  "audio": ['044.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "指出一般人對健康的漠視",
    "B": "再次強調全人醫療的缺陷",
    "C": "鼓勵全人醫療的擴大應用",
    "D": "說明心理因素如何造成疾病",
  },
  "answer": "B"
},

{
  "id": 45,
  "type": "listening",
  "audio": ['045.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "可以觀察，但切勿盲從",
    "B": "其優點被太多誤解掩蓋",
    "C": "突破性的觀念應得到推廣",
    "D": "社會應嚴禁偽科學的傳播",
  },
  "answer": "A"
},

{
  "id": 46,
  "type": "listening",
  "audio": ['046.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "地貌",
    "B": "生態",
    "C": "水文",
    "D": "氣候",
  },
  "answer": "A"
},

{
  "id": 47,
  "type": "listening",
  "audio": ['047.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為莊子為人荒誕不經",
    "B": "因為莊子真沒去過北極",
    "C": "他覺得考證的內容毫無邏輯",
    "D": "書裡有很多歷史無法追溯的內容",
  },
  "answer": "D"
},

{
  "id": 48,
  "type": "listening",
  "audio": ['048.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "指出先民對大魚的崇拜",
    "B": "凸顯「鯤」存活的時間漫長",
    "C": "辯證「魚」與「鳥」的演化關係",
    "D": "說明他對「鯤」存在與否的看法",
  },
  "answer": "D"
},

{
  "id": 49,
  "type": "listening",
  "audio": ['049.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他想強調這個生物的現實性",
    "B": "他想重新定義「演化」的意涵",
    "C": "他希望考證學家解釋神話的緣起",
    "D": "他想附和教授們「無法考證」的觀點",
  },
  "answer": "A"
},

{
  "id": 50,
  "type": "listening",
  "audio": ['050.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "大魚的心理狀態",
    "B": "形容一飛沖天的聲響",
    "C": "其他動物的情緒反應",
    "D": "大自然生機勃勃的狀態",
  },
  "answer": "A"
},
]

# PATHS
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio_bc_vol4"
IMAGE_DIR = BASE_DIR / ""

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