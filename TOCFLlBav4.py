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
  "type": "reading",
  "audio": [],
  "image": '1.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 2,
  "type": "reading",
  "audio": [],
  "image": '2.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 3,
  "type": "reading",
  "audio": [],
  "image": '3.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 4,
  "type": "reading",
  "audio": [],
  "image": '4.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "D"
},

{
  "id": 5,
  "type": "reading",
  "audio": [],
  "image": '5.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 6,
  "type": "reading",
  "audio": [],
  "image": '6.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 7,
  "type": "reading",
  "audio": [],
  "image": '7.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 8,
  "type": "reading",
  "audio": [],
  "image": '8.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 9,
  "type": "reading",
  "audio": [],
  "image": '9.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 10,
  "type": "reading",
  "audio": [],
  "image": '10.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "(C)",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 11,
  "type": "reading",
  "audio": [],
  "image": '11.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 12,
  "type": "reading",
  "audio": [],
  "image": '12.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 13,
  "type": "reading",
  "audio": [],
  "image": '13.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 14,
  "type": "reading",
  "audio": [],
  "image": '14.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 15,
  "type": "reading",
  "audio": [],
  "image": '15.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 16,
  "type": "reading",
  "audio": [],
  "image": '16.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 17,
  "type": "reading",
  "audio": [],
  "image": '17.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 18,
  "type": "reading",
  "audio": [],
  "image": '18.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 19,
  "type": "reading",
  "audio": [],
  "image": '19.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 20,
  "type": "reading",
  "audio": [],
  "image": '20.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 21,
  "type": "reading",
  "audio": [],
  "image": '21.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 22,
  "type": "reading",
  "audio": [],
  "image": '22.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 23,
  "type": "reading",
  "audio": [],
  "image": '23.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 24,
  "type": "reading",
  "audio": [],
  "image": '24.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 25,
  "type": "reading",
  "audio": [],
  "image": '25.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "(C)",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 26,
  "type": "reading",
  "audio": [],
  "image": '26.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 27,
  "type": "reading",
  "audio": [],
  "image": '27.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 28,
  "type": "reading",
  "audio": [],
  "image": '28.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 29,
  "type": "reading",
  "audio": [],
  "image": '29.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 30,
  "type": "reading",
  "audio": [],
  "image": '30.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 31,
  "type": "reading",
  "audio": [],
  "image": '31.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 32,
  "type": "reading",
  "audio": [],
  "image": '32.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "(C)",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 33,
  "type": "reading",
  "audio": [],
  "image": '33.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 34,
  "type": "reading",
  "audio": [],
  "image": '34.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": ""
},

{
  "id": 35,
  "type": "reading",
  "audio": [],
  "image": '35.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 36,
  "type": "reading",
  "audio": [],
  "image": '36.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "C"
},

{
  "id": 37,
  "type": "reading",
  "audio": [],
  "image": '37.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 38,
  "type": "reading",
  "audio": [],
  "image": '38.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "A"
},

{
  "id": 39,
  "type": "reading",
  "audio": [],
  "image": '39.png',
  "question": "",
  "choices": {
    "A": "(A)",
    "B": "（B）",
    "C": "（C）",
    
  },
  "answer": "B"
},

{
  "id": 40,
  "type": "reading",
  "audio": [],
  "image": '40.png',
  "question": "",
  "choices": {
    "A": "",
    "B": "",
    "C": "",
    
  },
  "answer": "C"
},

{
  "id": 41,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "這位先生找不到安全門",
    "B": "這位小姐想搭電梯下樓",
    "C": "這位先生要大家往樓梯那兒走",
    "D": "這位小姐 要這位先生快一點離開",
  },
  "answer": "C"
},

{
  "id": 42,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "想參加大學考試",
    "B": "想了解大學的學費",
    "C": "想知道付學費的方法",
    "D": "想問問讀大學的方法",
  },
  "answer": "B"
},

{
  "id": 43,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "記者",
    "B": "護士",
    "C": "教師",
    "D": "服務生",
  },
  "answer": "D"
},

{
  "id": 44,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "這位小姐準備出國工作",
    "B": "這位先生已經找到工作",
    "C": "這位小姐每天都在讀書",
    "D": "這位先生想快一點畢業",
  },
  "answer": "A"
},

{
  "id": 45,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "他喜歡和明美聊天兒",
    "B": "他有明美的電話號碼",
    "C": "他和明美從小就認識",
    "D": "他和明美一起去舞會",
  },
  "answer": "A"
},

{
  "id": 46,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "這位先生每次都遲到",
    "B": "這位先生現在不太高興",
    "C": "這位先生著急地找這位小姐",
    "D": "這位先生擔心這位小姐的安全",
  },
  "answer": "B"
},

{
  "id": 47,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "他很願意幫忙",
    "B": "他完全沒經驗",
    "C": "他需要有人教他",
    "D": "他認為工作太多",
  },
  "answer": "D"
},

{
  "id": 48,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "感冒了",
    "B": "害怕出門",
    "C": "常常睡不好",
    "D": "一運動就覺得累",
  },
  "answer": "C"
},

{
  "id": 49,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "把手放車門",
    "B": "從車上下來",
    "C": "離開警察局",
    "D": "把酒拿出來",
  },
  "answer": "B"
},

{
  "id": 50,
  "type": "reading",
  "audio": [],
  "image": None,
  "question": "",
  "choices": {
    "A": "幾歲結婚比較好",
    "B": "結婚要準備哪些東西",
    "C": "要怎樣才能有幸福的生活",
    "D": "要怎麼做才能讓人相信自己",
  },
  "answer": "C"
},
]

# PATHS
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio_ba_vol4"
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