# Test of Chinese as a Foreign Language Listening Band B (Vol.2)

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
  "audio": ['0-1.mp3', '1-01.mp3'],
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
  "id": 2,
  "type": "listening",
  "audio": ['1-02.mp3'],
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
  "id": 3,
  "type": "listening",
  "audio": ['1-03.mp3'],
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
  "id": 4,
  "type": "listening",
  "audio": ['1-04.mp3'],
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
  "id": 5,
  "type": "listening",
  "audio": ['1-05.mp3'],
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
  "id": 6,
  "type": "listening",
  "audio": ['1-06.mp3'],
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
  "id": 7,
  "type": "listening",
  "audio": ['1-07.mp3'],
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
  "id": 8,
  "type": "listening",
  "audio": ['1-08.mp3'],
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
  "id": 9,
  "type": "listening",
  "audio": ['1-09.mp3'],
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
  "id": 10,
  "type": "listening",
  "audio": ['1-10.mp3'],
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
  "id": 11,
  "type": "listening",
  "audio": ['1-11.mp3'],
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
  "id": 12,
  "type": "listening",
  "audio": ['1-12.mp3'],
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
  "id": 13,
  "type": "listening",
  "audio": ['1-13.mp3'],
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
  "id": 14,
  "type": "listening",
  "audio": ['1-14.mp3'],
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
  "id": 15,
  "type": "listening",
  "audio": ['1-15.mp3'],
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
  "id": 16,
  "type": "listening",
  "audio": ['1-16.mp3'],
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
  "id": 17,
  "type": "listening",
  "audio": ['1-17.mp3'],
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
  "id": 18,
  "type": "listening",
  "audio": ['1-18.mp3'],
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
  "id": 19,
  "type": "listening",
  "audio": ['1-19.mp3'],
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
  "id": 20,
  "type": "listening",
  "audio": ['1-20.mp3'],
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
  "id": 21,
  "type": "listening",
  "audio": ['1-21-0.mp3', '1-21-1.mp3'],
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
  "id": 22,
  "type": "listening",
  "audio": ['1-22.mp3'],
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
  "id": 23,
  "type": "listening",
  "audio": ['1-23-0.mp3', '1-23-1.mp3'],
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
  "id": 24,
  "type": "listening",
  "audio": ['1-24.mp3'],
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
  "id": 25,
  "type": "listening",
  "audio": ['1-25-0.mp3', '1-25-1.mp3'],
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
  "id": 26,
  "type": "listening",
  "audio": ['1-26.mp3'],
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
  "id": 27,
  "type": "listening",
  "audio": ['1-27.mp3'],
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
  "id": 28,
  "type": "listening",
  "audio": ['1-28-0.mp3', '1-28-1.mp3'],
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
  "id": 29,
  "type": "listening",
  "audio": ['1-29.mp3'],
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
  "id": 30,
  "type": "listening",
  "audio": ['1-30.mp3'],
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
  "id": 31,
  "type": "listening",
  "audio": ['2-31-0.mp3', '2-31-1.mp3'],
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
  "id": 32,
  "type": "listening",
  "audio": ['2-32.mp3'],
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
  "id": 33,
  "type": "listening",
  "audio": ['2-33-0.mp3', '2-33-1.mp3'],
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
  "id": 34,
  "type": "listening",
  "audio": ['2-34.mp3'],
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
  "id": 35,
  "type": "listening",
  "audio": ['2-35-0.mp3', '2-35-1.mp3'],
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
  "id": 36,
  "type": "listening",
  "audio": ['2-36.mp3'],
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
  "id": 37,
  "type": "listening",
  "audio": ['2-37-0.mp3', '2-37-1.mp3'],
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
  "id": 38,
  "type": "listening",
  "audio": ['2-38.mp3'],
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
  "id": 39,
  "type": "listening",
  "audio": ['2-39-0.mp3', '2-39-1.mp3'],
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
  "id": 40,
  "type": "listening",
  "audio": ['2-40.mp3'],
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
  "id": 41,
  "type": "listening",
  "audio": ['2-41-0.mp3', '2-41-1.mp3'],
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
  "id": 42,
  "type": "listening",
  "audio": ['2-42.mp3'],
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
  "id": 43,
  "type": "listening",
  "audio": ['2-43-0.mp3', '2-43-1.mp3'],
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
  "audio": ['2-44.mp3'],
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
  "id": 45,
  "type": "listening",
  "audio": ['2-45-0.mp3', '2-45-1.mp3'],
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
  "id": 46,
  "type": "listening",
  "audio": ['2-46.mp3'],
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
  "id": 47,
  "type": "listening",
  "audio": ['2-47.mp3'],
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
  "id": 48,
  "type": "listening",
  "audio": ['2-48-0.mp3', '2-48-1.mp3'],
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
  "id": 49,
  "type": "listening",
  "audio": ['2-49.mp3'],
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
  "id": 50,
  "type": "listening",
  "audio": ['2-50.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "（A）",
    "B": "（B）",
    "C": "（C）",
  },
  "answer": "A"
},
    ]


# PATHS
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio5"
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