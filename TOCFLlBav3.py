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
AUDIO_DIR = BASE_DIR / "audio4"
IMAGE_DIR = BASE_DIR / "images4"

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
  "audio": ['0-1.mp3', '1-01.mp3'],
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
  "type": "listening",
  "audio": ['1-02.mp3'],
  "image": '2.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 3,
  "type": "listening",
  "audio": ['1-03.mp3'],
  "image": '3.png',
  "question": " ",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 4,
  "type": "listening",
  "audio": ['1-04.mp3'],
  "image": '4.png',
  "question": "  ",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "D"
},

{
  "id": 5,
  "type": "listening",
  "audio": ['1-05.mp3'],
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
  "type": "listening",
  "audio": ['1-06.mp3'],
  "image": '6.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 7,
  "type": "listening",
  "audio": ['1-07.mp3'],
  "image": '7.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 8,
  "type": "listening",
  "audio": ['1-08.mp3'],
  "image": '8.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 9,
  "type": "listening",
  "audio": ['1-09.mp3'],
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
  "type": "listening",
  "audio": ['1-10.mp3'],
  "image": '10.png',
  "question": "說明：在這個部分，每題有",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 11,
  "type": "listening",
  "audio": ['2-11.mp3'],
  "image": '11.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 12,
  "type": "listening",
  "audio": ['2-12.mp3'],
  "image": '12.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 13,
  "type": "listening",
  "audio": ['2-13.mp3'],
  "image": '13.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 14,
  "type": "listening",
  "audio": ['2-14.mp3'],
  "image": '14.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 15,
  "type": "listening",
  "audio": ['2-15.mp3'],
  "image": '15.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 16,
  "type": "listening",
  "audio": ['2-16.mp3'],
  "image": '16.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 17,
  "type": "listening",
  "audio": ['2-17.mp3'],
  "image": '17.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 18,
  "type": "listening",
  "audio": ['2-18.mp3'],
  "image": '18.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 19,
  "type": "listening",
  "audio": ['2-19.mp3'],
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
  "type": "listening",
  "audio": ['2-20.mp3'],
  "image": '20.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 21,
  "type": "listening",
  "audio": ['2-21.mp3'],
  "image": '21.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 22,
  "type": "listening",
  "audio": ['2-22.mp3'],
  "image": '22.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 23,
  "type": "listening",
  "audio": ['2-23.mp3'],
  "image": '23.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 24,
  "type": "listening",
  "audio": ['2-24.mp3'],
  "image": '24.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 25,
  "type": "listening",
  "audio": ['2-25.mp3'],
  "image": '25.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 26,
  "type": "listening",
  "audio": ['3-26.mp3'],
  "image": '26.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 27,
  "type": "listening",
  "audio": ['3-27.mp3'],
  "image": '27.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 28,
  "type": "listening",
  "audio": ['3-28.mp3'],
  "image": '28.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 29,
  "type": "listening",
  "audio": ['3-29.mp3'],
  "image": '29.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 30,
  "type": "listening",
  "audio": ['3-30.mp3'],
  "image": '30.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 31,
  "type": "listening",
  "audio": ['3-31.mp3'],
  "image": '31.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 32,
  "type": "listening",
  "audio": ['3-32.mp3'],
  "image": '32.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 33,
  "type": "listening",
  "audio": ['3-33.mp3'],
  "image": '33.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 34,
  "type": "listening",
  "audio": ['3-34.mp3'],
  "image": '34.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": ""
},

{
  "id": 35,
  "type": "listening",
  "audio": ['3-35.mp3'],
  "image": '35.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 36,
  "type": "listening",
  "audio": ['3-36.mp3'],
  "image": '36.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 37,
  "type": "listening",
  "audio": ['3-37.mp3'],
  "image": '37.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 38,
  "type": "listening",
  "audio": ['3-38.mp3'],
  "image": '38.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 39,
  "type": "listening",
  "audio": ['3-39.mp3'],
  "image": '39.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 40,
  "type": "listening",
  "audio": ['3-40.mp3'],
  "image": '40.png',
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 41,
  "type": "listening",
  "audio": ['4-41.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 42,
  "type": "listening",
  "audio": ['4-42.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "D"
},

{
  "id": 43,
  "type": "listening",
  "audio": ['4-43.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 44,
  "type": "listening",
  "audio": ['4-44.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 45,
  "type": "listening",
  "audio": ['4-45.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
},

{
  "id": 46,
  "type": "listening",
  "audio": ['4-46.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 47,
  "type": "listening",
  "audio": ['4-47.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "B"
},

{
  "id": 48,
  "type": "listening",
  "audio": ['4-48.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 49,
  "type": "listening",
  "audio": ['4-49.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},

{
  "id": 50,
  "type": "listening",
  "audio": ['4-50.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "C"
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