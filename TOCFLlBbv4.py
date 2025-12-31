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
    "A": "在戶外運動比較健康",
    "B": "下雨天運動，很不方便",
    "C": "不管天氣怎樣，都可以運動",
    "D": "天氣不好也要去公園動一動",
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
    "A": "他非常喜歡運動",
    "B": "他什麼角色都能演",
    "C": "他不太熟悉這個角色",
    "D": "他這次的表演十分精彩",
  },
  "answer": "D"
},

{
  "id": 3,
  "type": "listening",
  "audio": ['003.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "新婚的夫妻",
    "B": "剛交往的人",
    "C": "剛畢業的人",
    "D": "新進公司的員工",
  },
  "answer": "D"
},

{
  "id": 4,
  "type": "listening",
  "audio": ['004.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "這位先生還是別買了吧",
    "B": "她要送給這位先生一雙鞋",
    "C": "這位先生可以先用她的錢買",
    "D": "這位先生可以先拿回去再付錢",
  },
  "answer": "C"
},

{
  "id": 5,
  "type": "listening",
  "audio": ['005.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她不隨便吃東西",
    "B": "她只想吃一點東西",
    "C": "她不想給這位先生方便",
    "D": "她不想讓這位先生太麻煩",
  },
  "answer": "D"
},

{
  "id": 6,
  "type": "listening",
  "audio": ['006.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "向這位先生借傘",
    "B": "請這位先生還她傘",
    "C": "拿了這位先生的傘",
    "D": "把這位先生的傘弄丟了",
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
    "A": "她一直覺得做這件事很困難",
    "B": "她一開始以為只是小事一件",
    "C": "她一開始就把東西準備好了",
    "D": "她覺得事情沒有她想的複雜",
  },
  "answer": "B"
},

{
  "id": 8,
  "type": "listening",
  "audio": ['008.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "活動的時間太長",
    "B": "活動安排得不好",
    "C": "不滿意活動的地點",
    "D": "覺得參加活動的人太多",
  },
  "answer": "D"
},

{
  "id": 9,
  "type": "listening",
  "audio": ['009.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "拼命洗澡會傷害皮膚",
    "B": "要按照醫生說的方法洗澡",
    "C": "精神不好的時候，就去洗澡",
    "D": "要這位先生提供保養皮膚的方式",
  },
  "answer": "A"
},

{
  "id": 10,
  "type": "listening",
  "audio": ['010.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "太慢了吧",
    "B": "慢一點比較好",
    "C": "慢慢來沒關係",
    "D": "太快了，慢一點吧",
  },
  "answer": "A"
},

{
  "id": 11,
  "type": "listening",
  "audio": ['011.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "這位小姐不想白跑一趟",
    "B": "這位先生希望有人可以幫他",
    "C": "這位先生找這位小姐要資料",
    "D": "這位小姐打電話要這位先生回家",
  },
  "answer": "B"
},

{
  "id": 12,
  "type": "listening",
  "audio": ['012.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "聽這位先生的建議",
    "B": "不改變放床的地方",
    "C": "選樣子更好看的床",
    "D": "詢問其他人的想法",
  },
  "answer": "B"
},

{
  "id": 13,
  "type": "listening",
  "audio": ['013.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她覺得坐火車太慢了",
    "B": "她不想坐太便宜的火車",
    "C": "她覺得坐火車也不太安全",
    "D": "她認為坐火車的好處很多",
  },
  "answer": "D"
},

{
  "id": 14,
  "type": "listening",
  "audio": ['014.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她想找人成立資訊技術團隊",
    "B": "這項計畫案裡要有她公司的人",
    "C": "她沒有搞清楚整體產業的需求",
    "D": "這位先生的報告不符合她的期待",
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
    "A": "這位小姐覺得外食對身體不好",
    "B": "這位先生覺得外食的口味不好",
    "C": "這位小姐覺得出門吃飯太麻煩了",
    "D": "這位先生覺得這位小姐想換口味",
  },
  "answer": "A"
},

{
  "id": 16,
  "type": "listening",
  "audio": ['016.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她要把錢還給客人",
    "B": "東西賣出去就不能換了",
    "C": "她沒有東西可以換給客人",
    "D": "沒有發票，就不能換東西",
  },
  "answer": "D"
},

{
  "id": 17,
  "type": "listening",
  "audio": ['017.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "環境很不好",
    "B": "位置還不錯",
    "C": "價格太昂貴",
    "D": "舞蹈課程多",
  },
  "answer": "B"
},

{
  "id": 18,
  "type": "listening",
  "audio": ['018.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "要先把畫畫學好",
    "B": "學得越久，寫得越好",
    "C": "要具備空間分佈的概念",
    "D": "要知道寫一個字的順序",
  },
  "answer": "C"
},

{
  "id": 19,
  "type": "listening",
  "audio": ['019.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "看不出有什麼技巧",
    "B": "要再多和大師學習",
    "C": "沒有什麼藝術價值",
    "D": "要發展自己的特色",
  },
  "answer": "D"
},

{
  "id": 20,
  "type": "listening",
  "audio": ['020.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為只有這位小姐有點數",
    "B": "因為點數不能用來換折扣",
    "C": "因為只有這位小姐有折扣",
    "D": "因為這位小姐不幫他付錢",
  },
  "answer": "A"
},

{
  "id": 21,
  "type": "listening",
  "audio": ['021.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "今天刷卡會送購物袋",
    "B": "他們買東西是各付各的",
    "C": "加入商店會員有很多好處",
    "D": "這位先生也想要辦信用卡",
  },
  "answer": "B"
},

{
  "id": 22,
  "type": "listening",
  "audio": ['022.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "小孩生病就是要吃藥",
    "B": "小孩子不可以吃大人的藥",
    "C": "就算沒有水，也可以吃藥",
    "D": "不可以隨便調整吃藥的時間",
  },
  "answer": "C"
},

{
  "id": 23,
  "type": "listening",
  "audio": ['023.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "沒帶水瓶的原因",
    "B": "到便利商店的方向",
    "C": "醫生交代的吃藥方式",
    "D": "小孩生病不舒服的狀況",
  },
  "answer": "A"
},

{
  "id": 24,
  "type": "listening",
  "audio": ['024.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他的生活很辛苦",
    "B": "他娛樂支出很多",
    "C": "父母的收入很高",
    "D": "父母沒給生活費",
  },
  "answer": "B"
},

{
  "id": 25,
  "type": "listening",
  "audio": ['025.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "現在大明應該自己賺錢",
    "B": "父親給多少錢就可花多少",
    "C": "大明每天只會玩，不會養家",
    "D": "大明應該從小培養存錢的習慣",
  },
  "answer": "A"
},

{
  "id": 26,
  "type": "listening",
  "audio": ['026.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為想在網路上找朋友",
    "B": "因為對寫文章很有興趣",
    "C": "因為要訓練自己的表達能力",
    "D": "因為能增加得到工作的機會",
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
    "A": "可以增加不同的專業知識",
    "B": "可以清楚地表現個性特色",
    "C": "可以改變自己的寫作習慣",
    "D": "可以設定條件來尋找工作",
  },
  "answer": "B"
},

{
  "id": 28,
  "type": "listening",
  "audio": ['028.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "不適合用來找工作",
    "B": "無法觀察出專業看法",
    "C": "要小心發表時的態度",
    "D": "要了解網路讀者的反應",
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
    "A": "補助金額偏低",
    "B": "申請程序便利",
    "C": "實施時間應該提前",
    "D": "申請對象應限制年齡",
  },
  "answer": "A"
},

{
  "id": 30,
  "type": "listening",
  "audio": ['030.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "年紀超過 65 歲的人",
    "B": "沒有工作超過三個月的人",
    "C": "家中小孩未滿三個月的父母",
    "D": "全家一年收入不到三十萬的家庭",
  },
  "answer": "B"
},

{
  "id": 31,
  "type": "listening",
  "audio": ['031.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "這位先生沒工作",
    "B": "這位小姐的先生失業了",
    "C": "這位先生在經濟上需要政府協助",
    "D": "這位小姐符合申請補助金的條件",
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
    "A": "避免浪費",
    "B": "沒時間買東西",
    "C": "數現金比較有意思",
    "D": "在國外買東西都能退換",
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
    "A": "鄉下人比較不客氣",
    "B": "城市裡的人都不客氣",
    "C": "現在的人都很不客氣",
    "D": "鄉下人不一定比較客氣",
  },
  "answer": "D"
},

{
  "id": 34,
  "type": "listening",
  "audio": ['034.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "坐計程車",
    "B": "坐公車或走路",
    "C": "坐公車，再走路",
    "D": "坐計程車或公車",
  },
  "answer": "B"
},

{
  "id": 35,
  "type": "listening",
  "audio": ['035.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "下星期少出門",
    "B": "這幾天空氣不好",
    "C": "進門後要記得關窗戶",
    "D": "幾天以後天氣會變差",
  },
  "answer": "B"
},

{
  "id": 36,
  "type": "listening",
  "audio": ['036.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "小高的溫柔與體貼",
    "B": "小高心中理想的愛情",
    "C": "小高在行為上的改變",
    "D": "小高是怎麼交到女朋友的",
  },
  "answer": "C"
},

{
  "id": 37,
  "type": "listening",
  "audio": ['037.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "對生活很講究",
    "B": "很在意自己穿什麼",
    "C": "沒有信心交到女朋友",
    "D": "對很多事情覺得無所謂",
  },
  "answer": "D"
},

{
  "id": 38,
  "type": "listening",
  "audio": ['038.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他找工作的經驗",
    "B": "他對工作的期待",
    "C": "他對讀大學的想法",
    "D": "他對現在大學生的看法",
  },
  "answer": "C"
},

{
  "id": 39,
  "type": "listening",
  "audio": ['039.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "越來越重視學歷",
    "B": "越來越重視經驗",
    "C": "越來越多人搶同一份工作",
    "D": "大學學位變得越來越沒有用",
  },
  "answer": "A"
},

{
  "id": 40,
  "type": "listening",
  "audio": ['040.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "行為",
    "B": "血型",
    "C": "朋友",
    "D": "興趣",
  },
  "answer": "B"
},

{
  "id": 41,
  "type": "listening",
  "audio": ['041.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "喜歡動物的人個性比較開朗",
    "B": "一個人的個性和家庭背景有關",
    "C": "可以透過觀察來了解一個人的個性",
    "D": "沒有一個人可以真正了解另一個人",
  },
  "answer": "C"
},

{
  "id": 42,
  "type": "listening",
  "audio": ['042.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "不清楚自己已經生病了",
    "B": "身體狀況會一天比一天好",
    "C": "因為身體不好，心情不好",
    "D": "需要立即轉送大醫院看病",
  },
  "answer": "B"
},

{
  "id": 43,
  "type": "listening",
  "audio": ['043.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "接受更詳細的檢查",
    "B": "快一點辦出院手續",
    "C": "最好再多住院幾天",
    "D": "吃維他命補充體力",
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
    "A": "想買房子的人",
    "B": "想蓋房子的人",
    "C": "想租房子的人",
    "D": "想賣房子的人",
  },
  "answer": "A"
},

{
  "id": 45,
  "type": "listening",
  "audio": ['045.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "每層樓都有浴室",
    "B": "二樓有個大陽台",
    "C": "適合養小狗或小貓",
    "D": "帶小孩去上學很方便",
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
    "A": "希望假期越長越好",
    "B": "和朋友分享愉快的時光",
    "C": "總想試試自己一個人度過",
    "D": "放假就是要四處走走看看",
  },
  "answer": "C"
},

{
  "id": 47,
  "type": "listening",
  "audio": ['047.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "人們不願休假的心態",
    "B": "人們過度依賴網路的心理",
    "C": "人們在乎別人對自己的看法",
    "D": "人們對假期旅行的規劃方式",
  },
  "answer": "C"
},

{
  "id": 48,
  "type": "listening",
  "audio": ['048.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他抱持著樂觀的態度",
    "B": "他覺得這種心態令人害怕",
    "C": "他覺得是考慮太多的結果",
    "D": "他不能理解矛盾產生的原因",
  },
  "answer": "A"
},

{
  "id": 49,
  "type": "listening",
  "audio": ['049.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為所愛之人不再愛自己",
    "B": "因為有時相處的不太順利",
    "C": "因為人們總是見不得別人好",
    "D": "因為無法忍受失去親人的痛苦",
  },
  "answer": "B"
},

{
  "id": 50,
  "type": "listening",
  "audio": ['050.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "幽默",
    "B": "煩惱",
    "C": "感動",
    "D": "激動",
  },
  "answer": "A"
},
]

# PATHS
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio_bb_vol4"
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