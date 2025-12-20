# Test of Chinese as a Foreign Language Listening Band A (Vol.1)

import os
import subprocess
from pathlib import Path
from termcolor import colored
from PIL import Image

# -------------------------
# Path setup (SAFE)
# -------------------------

BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio"
IMAGE_DIR = BASE_DIR / "images"

# -------------------------
# Question Bank 
# -------------------------

questions = [
    {
        "id": 1,
        "audio": "1-01.mp3",
        "image": "l1.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 2,
        "audio": "1-02.mp3",
        "image": "l2.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 3,
        "audio": "1-03.mp3",
        "image": "l3.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 4,
        "audio": "1-04.mp3",
        "image": "l4.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 5,
        "audio": "1-05.mp3",
        "image": "l5.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 6,
        "audio": "1-06.mp3",
        "image": "l6.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 7,
        "audio": "1-07.mp3",
        "image": "l7.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 8,
        "audio": "1-08.mp3",
        "image": "l8.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 9,
        "audio": "1-09.mp3",
        "image": "l9.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 10,
        "audio": "1-10.mp3",
        "image": "l10.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 11,
        "audio": "1-11.mp3",
        "image": "l11.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 12,
        "audio": "1-12.mp3",
        "image": "l12.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 13,
        "audio": "1-13.mp3",
        "image": "l13.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 14,
        "audio": "1-14.mp3",
        "image": "l14.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 15,
        "audio": "1-15.mp3",
        "image": "l15.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 16,
        "audio": "1-16.mp3",
        "image": "l16.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 17,
        "audio": "1-17.mp3",
        "image": "l17.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 18,
        "audio": "1-18.mp3",
        "image": "l18.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 19,
        "audio": "1-19.mp3",
        "image": "l19.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 20,
        "audio": "1-20.mp3",
        "image": "l20.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 21,
        "audio": "1-21.mp3",
        "image": "l21.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 22,
        "audio": "1-22.mp3",
        "image": "l22.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 23,
        "audio": "1-23.mp3",
        "image": "l23.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 24,
        "audio": "1-24.mp3",
        "image": "l24.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 25,
        "audio": "1-25.mp3",
        "image": "l25.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 26,
        "audio": "1-26.mp3",
        "image": "l26.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 27,
        "audio": "1-27.mp3",
        "image": "l27.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 28,
        "audio": "1-28.mp3",
        "image": "l28.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 29,
        "audio": "1-29.mp3",
        "image": "l29.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 30,
        "audio": "1-30.mp3",
        "image": "l30.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 31,
        "audio": "1-31.mp3",
        "image": "l31.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 32,
        "audio": "1-32.mp3",
        "image": "l32.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 33,
        "audio": "1-33.mp3",
        "image": "l33.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 34,
        "audio": "1-34.mp3",
        "image": "l34.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 35,
        "audio": "1-35.mp3",
        "image": "l35.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 36,
        "audio": "1-36.mp3",
        "image": "l36.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 37,
        "audio": "1-37.mp3",
        "image": "l37.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 38,
        "audio": "1-38.mp3",
        "image": "l38.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 39,
        "audio": "1-39.mp3",
        "image": "l39.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 40,
        "audio": "1-40.mp3",
        "image": "l40.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 41,
        "audio": "1-41.mp3",
        "image": "l41.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 42,
        "audio": "1-42.mp3",
        "image": "l42.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "B"
    },
    {
        "id": 43,
        "audio": "1-43.mp3",
        "image": "l43.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 44,
        "audio": "1-44.mp3",
        "image": "l44.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 45,
        "audio": "1-45.mp3",
        "image": "l45.png",
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
    {
        "id": 46,
        "audio": "1-46.mp3",
        "image": None,
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 47,
        "audio": "1-47.mp3",
        "image": None,
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 48,
        "audio": "1-48.mp3",
        "image": None,
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "D"
    },
    {
        "id": 49,
        "audio": "1-49.mp3",
        "image": None,
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "A"
    },
    {
        "id": 50,
        "audio": "1-50.mp3",
        "image": None,
        "question": "",
        "choices": {
            "A": "",
            "B": "",
            "C": ""
        },
        "answer": "C"
    },
]

score = 0

# -------------------------
# Exam Loop
# -------------------------
for q in questions:
    print(colored(f"\n🎧 Listening Question {q['id']}", "cyan"))

    # Image
    if q["image"]:
        img_path = IMAGE_DIR / q["image"]
        if img_path.exists():
            Image.open(img_path).show()
        else:
            print(colored(f"⚠️ Image not found: {img_path}", "yellow"))

    # Prepare audio
    audio_path = AUDIO_DIR / q["audio"]
    if not audio_path.exists():
        print(colored(f"❌ Audio not found: {audio_path}", "red"))
        continue

    # PLAY AUDIO
    print(colored("🔊 Playing audio...", "yellow"))
    audio_process = subprocess.Popen(
        ["afplay", str(audio_path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Show question + choices 
    print(colored("\n" + q["question"], "white"))
    for k, v in q["choices"].items():
        print(f"  ({k}) {v}")

    # Answer input
    while True:
        user_answer = input(colored("\n👉 Your answer (A/B/C): ", "cyan")).strip().upper()
        if user_answer in q["choices"]:
            break
        print(colored("⚠️ Please enter A, B, or C only.", "yellow"))

    # STOP AUDIO IMMEDIATELY
    audio_process.terminate()

    # Check answer
    if user_answer == q["answer"]:
        print(colored("✅ Correct!", "green"))
        score += 1
    else:
        print(colored(f"❌ Wrong: Correct answer [{q['answer']}]", "red"))