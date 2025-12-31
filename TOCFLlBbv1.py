# Test of Chinese as a Foreign Language Listening Band B (Vol.1)
# Message: Terribly sorry for the delayed questions, some questions are equipped with 2 audios, so it's safe to say the delay is for the second audio to finish then you can answer...

import sys
import time
import subprocess
import threading

from pathlib import Path
from termcolor import colored
from PIL import Image
from mutagen.mp3 import MP3

# Path setup (SAFE)

BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio2"
IMAGE_DIR = BASE_DIR / "images"

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
        "audio": ["1-01.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "上午",
            "B": "中午",
            "C": "下午",
            "D": "晚上"
        },
        "answer": "C"
    },
    {
        "id": 2,
        "audio": ["1-02.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "他買了新房子",
            "B": "他把房子賣了",
            "C": "他找到更好的房子",
            "D": "他的房東要賣房子"
        },
        "answer": "D"
    },
    {
        "id": 3,
        "audio": ["1-03.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她很快就找到停車的位子",
            "B": "她花了不少時間找地方停車",
            "C": "她把車子停在比較近的地方",
            "D": "她停車以後，找不到那位先生"
        },
        "answer": "B"
    },
    {
        "id": 4,
        "audio": ["1-04.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她覺得有點累",
            "B": "她身體不舒服",
            "C": "她剛剛才從外面回來",
            "D": "她還沒想好去哪兒玩"
        },
        "answer": "A"
    },
    {
        "id": 5,
        "audio": ["1-05.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她一年出國旅遊兩次",
            "B": "她今年不打算出國玩",
            "C": "她每次去不一樣的國家玩",
            "D": "她今年去韓國，明年想去日本"
        },
        "answer": "C"
    },
    {
        "id": 6,
        "audio": ["1-06.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她不想寫作業",
            "B": "她想不出來要寫什麼",
            "C": "她不知道有什麼作業",
            "D": "她記不得老師給的作業"
        },
        "answer": "B"
    },
    {
        "id": 7,
        "audio": ["1-07.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "他們沒錢買車子",
            "B": "她不喜歡出去玩",
            "C": "這位先生常常開玩笑",
            "D": "她不知道哪裡借得到錢"
        },
        "answer": "A"
    },
    {
        "id": 8,
        "audio": ["1-08.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她做菜做得不好",
            "B": "她很喜歡自己做菜",
            "C": "她喜歡吃別人煮的菜",
            "D": "她只會吃東西，不會做菜"
        },
        "answer": "B"
    },
    {
        "id": 9,
        "audio": ["1-09.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她來不及把書讀完",
            "B": "她對通過考試有信心",
            "C": "她要這位先生別緊張",
            "D": "她一聽見考試就開始緊張"
        },
        "answer": "B"
    },
    {
        "id": 10,
        "audio": ["1-10.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她知道今天會下大雨",
            "B": "沒有人知道今天會下雨",
            "C": "她本來以為只是下小雨",
            "D": "這位先生沒告訴她會下雨"
        },
        "answer": "C"
    },
    {
        "id": 11,
        "audio": ["1-11.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "老師還沒教語法",
            "B": "老師教了十個漢字",
            "C": "他覺得語法很簡單",
            "D": "他認為學漢字很有意思"
        },
        "answer": "D"
    },
    {
        "id": 12,
        "audio": ["1-12.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她快看完了",
            "B": "她還沒開始看",
            "C": "她要再看一個星期",
            "D": "她已經全部看完了"
        },
        "answer": "A"
    },
    {
        "id": 13,
        "audio": ["1-13.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她還有點兒餓",
            "B": "蛋糕有點兒難吃",
            "C": "她可以再吃一點兒東西",
            "D": "她沒辦法吃任何東西了"
        },
        "answer": "C"
    },
    {
        "id": 14,
        "audio": ["1-14.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她不需要手錶",
            "B": "她想要別的禮物",
            "C": "這位先生買錯手錶",
            "D": "這位先生買對了禮物"
        },
        "answer": "D"
    },
    {
        "id": 15,
        "audio": ["1-15.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "他不用功",
            "B": "他不聰明",
            "C": "考試太難",
            "D": "他不小心寫錯"
        },
        "answer": "A"
    },
    {
        "id": 16,
        "audio": ["1-16.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "對她不好",
            "B": "午餐不用錢",
            "C": "工作不是太多",
            "D": "每年辦旅遊活動"
        },
        "answer": "D"
    },
    {
        "id": 17,
        "audio": ["1-17.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "不要搭公車",
            "B": "到醫院看病",
            "C": "多吃蔬菜水果",
            "D": "養成運動的習慣"
        },
        "answer": "B"
    },
    {
        "id": 18,
        "audio": ["1-18.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "繼續工作",
            "B": "組織一個家庭",
            "C": "去世界各國旅行",
            "D": "住在專門照顧老人的地方"
        },
        "answer": "D"
    },
    {
        "id": 19,
        "audio": ["1-19.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "由服務生幫客人點餐",
            "B": "食物材料從國外買進來",
            "C": "每個人喝的飲料限制兩杯",
            "D": "吃一頓飯所花的費用很便宜"
        },
        "answer": "B"
    },
    {
        "id": 20,
        "audio": ["1-20.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "把它丟了",
            "B": "繼續使用",
            "C": "找人來修理",
            "D": "把它賣給別人"
        },
        "answer": "A"
    },
    {
        "id": 21,
        "audio": ["1-21-0.mp3", "1-21-1.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她找不到其他工作",
            "B": "她買了很多新衣服",
            "C": "朋友送給她很多衣服",
            "D": "她有很多不需要的衣服"
        },
        "answer": "D"
    },
    {
        "id": 22,
        "audio": ["1-22.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "買新書",
            "B": "賣舊書",
            "C": "賣衣服",
            "D": "買衣服"
        },
        "answer": "B"
    },
    {
        "id": 23,
        "audio": ["1-23-0.mp3", "1-23-1.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "送飛機票",
            "B": "陪爸爸出差",
            "C": "送運動器材",
            "D": "帶爸爸出國旅遊"
        },
        "answer": "C"
    },
    {
        "id": 24,
        "audio": ["1-24.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "她要跟朋友借腳踏車",
            "B": "她要教爸爸騎腳踏車",
            "C": "她不想陪爸爸騎腳踏車",
            "D": "她也要買一輛腳踏車給自己"
        },
        "answer": "B"
    },
    {
        "id": 25,
        "audio": ["1-25-0.mp3", "1-25-1.mp3"],
        "image": None,
        "question": "下面是一段和工作有關的對話。請你在聽完這段對話後，回答下面三個問題：\n這位小姐想到這家公司工作的原因是什麼？",
        "choices": {
            "A": "她不想再當業務人員",
            "B": "她被原本的公司開除了",
            "C": "她覺得在這家公司比較有前途",
            "D": "這家公司主動請這位小姐來工作"
        },
        "answer": "C"
    },
    {
        "id": 26,
        "audio": ["1-26.mp3"],
        "image": None,
        "question": "這位小姐認為擔任業務人員最重要的能力是什麼？",
        "choices": {
            "A": "語言溝通",
            "B": "問題解決",
            "C": "領導員工",
            "D": "開發新客戶"
        },
        "answer": "D"
    },
    {
        "id": 27,
        "audio": ["1-27.mp3"],
        "image": None,
        "question": "這位主管說這位小姐缺少哪方面的經驗？\n現在請聽這段對話。",
        "choices": {
            "A": "談生意",
            "B": "業務工作",
            "C": "服務客戶",
            "D": "經營國外市場"
        },
        "answer": "D"
    },
    {
        "id": 28,
        "audio": ["1-28-0.mp3", "1-28-1.mp3"],
        "image": None,
        "question": "快速約會是什麼樣的活動？",
        "choices": {
            "A": "參加人數每次大約十個人",
            "B": "不是單身的人也能夠參加",
            "C": "讓人可以在幾分鐘以內認識新朋友",
            "D": "一個女生能同時和兩、三個男生談話"
        },
        "answer": "C"
    },
    {
        "id": 29,
        "audio": ["1-29.mp3"],
        "image": None,
        "question": "這位小姐認為快速約會的缺點是什麼？",
        "choices": {
            "A": "參加的費用太高",
            "B": "能夠認識的人很少",
            "C": "很難真正了解一個人",
            "D": "認識新朋友要花很長的時間"
        },
        "answer": "C"
    },
    {
        "id": 30,
        "audio": ["1-30.mp3"],
        "image": None,
        "question": "這位先生覺得快速約會怎麼樣？",
        "choices": {
            "A": "沒有效率",
            "B": "比網路交友安全",
            "C": "找不到喜歡的對象",
            "D": "無法認識多一點兒女生"
        },
        "answer": "B"
    },
    {
        "id": 31,
        "audio": ["2-31.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "不開了",
            "B": "要離開了",
            "C": "晚一個小時到",
            "D": "晚三十分鐘到"
        },
        "answer": "D"
    },
    {
        "id": 32,
        "audio": ["2-32.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "1000 元",
            "B": "1500 元",
            "C": "2000 元",
            "D": "2500 元"
        },
        "answer": "A"
    },
    {
        "id": 33,
        "audio": ["2-33.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "有小鳥表演",
            "B": "有日本歌表演",
            "C": "有老師教唱歌",
            "D": "有德國舞表演"
        },
        "answer": "C"
    },
    {
        "id": 34,
        "audio": ["2-34.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "看圖片",
            "B": "看漢字",
            "C": "寫漢字",
            "D": "請人幫忙 "
        },
        "answer": "A"
    },
    {
        "id": 35,
        "audio": ["2-35-0.mp3", "2-35-1.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "背課文",
            "B": "寫生字",
            "C": "錄聲音",
            "D": "查資料"
        },
        "answer": "A"
    },
    {
        "id": 36,
        "audio": ["2-36.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "教第八課",
            "B": "複習第六課",
            "C": "預習第七課",
            "D": "考學生第七課"
        },
        "answer": "D"
    },
    {
        "id": 37,
        "audio": ["2-37-0.mp3", "2-37-1.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "天氣變暖和",
            "B": "白天時間變長",
            "C": "白天和晚上都變涼了",
            "D": "一天裡面的天氣變化很大"
        },
        "answer": "D"
    },
    {
        "id": 38,
        "audio": ["2-38.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "晴天",
            "B": "雨天",
            "C": "陰天",
            "D": "沒有風"
        },
        "answer": "A"
    },
    {
        "id": 39,
        "audio": ["1-39-0.mp3", "1-39-1.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "馬",
            "B": "鳥",
            "C": "魚",
            "D": "牛"
        },
        "answer": "B"
    },
    {
        "id": 40,
        "audio": ["2-40.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "照相",
            "B": "吃冰",
            "C": "喝牛奶",
            "D": "看表演"
        },
        "answer": "B"
    },
    {
        "id": 41,
        "audio": ["2-41-0.mp3", "2-41-1.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "太胖了",
            "B": "太瘦了",
            "C": "感冒了",
            "D": "很健康"
        },
        "answer": "A"
    },
    {
        "id": 42,
        "audio": ["2-42.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "只能吃豬肉",
            "B": "少吃酸的東西",
            "C": "青菜多吃一點兒",
            "D": "每天運動半小時"
        },
        "answer": "C"
    },
    {
        "id": 43,
        "audio": ["2-43-0.mp3", "2-43-1.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "會說英語的人",
            "B": "會讀英國文學的人",
            "C": "會寫英文文章的人",
            "D": "會做公司網站的人"
        },
        "answer": "C"
    },
    {
        "id": 44,
        "audio": ["2-44.mp3"],
        "image": None,
        "question": "",
        "choices": {
            "A": "老闆沒選他",
            "B": "老闆還沒決定",
            "C": "老闆不找人了",
            "D": "老闆先讓他試試"
        },
        "answer": "D"
    },
    {
        "id": 45,
        "audio": ["2-45-0.mp3", "1-45-1.mp3"],
        "image": None,
        "question": "說話的人認為什麼才是合適的睡眠？",
        "choices": {
            "A": "每天睡覺八小時",
            "B": "早上早點兒起床",
            "C": "在晚上十一點以前睡覺",
            "D": "能滿足身體的睡眠需求"
        },
        "answer": "D"
    },
    {
        "id": 46,
        "audio": ["2-46.mp3"],
        "image": None,
        "question": "我們可以根據哪件事知道自己究竟需要睡多久才夠？",
        "choices": {
            "A": "白天的精神狀況",
            "B": "白天活動的時間",
            "C": "晚上是否需要工作",
            "D": "晚上幾點上床睡覺",
        },
        "answer": "A"
    },
    {
        "id": 47,
        "audio": ["2-47.mp3"],
        "image": None,
        "question": "這段報告的結論是什麼？",
        "choices": {
            "A": "睡得多就是睡得飽",
            "B": "睡得少代表睡不好",
            "C": "多觀察自己的身體狀態",
            "D": "必須睡滿一定的時數才算健康"
        },
        "answer": "C"
    },
    {
        "id": 48,
        "audio": ["2-48.mp3"],
        "image": None,
        "question": "這則報導主要在說明什麼？",
        "choices": {
            "A": "性別和自行車的關係",
            "B": "自行車專用道路的必要性",
            "C": "自行車作為交通工具的比例",
            "D": "自行車被視為環保工具的原因"
        },
        "answer": "A"
    },
    {
        "id": 49,
        "audio": ["2-49.mp3"],
        "image": None,
        "question": "根據報導，我們可以從哪方面知道一座城市很適合把自行車當作主要交通工具？",
        "choices": {
            "A": "私人汽車的數量",
            "B": "購買自行車的人數",
            "C": "騎自行車的女性人口",
            "D": "專為自行車設計的道路數量"
        },
        "answer": "C"
    },
    {
        "id": 50,
        "audio": ["2-50.mp3"],
        "image": None,
        "question": "報導內容指出，怎麼做才能增加騎自行車的人數？",
        "choices": {
            "A": "叫人少開車",
            "B": "鼓勵男人多騎自行車",
            "C": "設立更多的自行車專用道路",
            "D": "讓自行車道路通過實用的地方"
        },
        "answer": "D"
    },
]

# PATHS
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio2"
IMAGE_DIR = BASE_DIR / "images2"

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