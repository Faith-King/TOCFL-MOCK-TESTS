# ========================= upgraded generator
# UPGEN.py - AQG (Automatic questions generator) [by PDF(s) and audio files.]
# ========================= upgraded generator

import re
from pathlib import Path
from PyPDF2 import PdfReader
from collections import defaultdict

# -------------------------
# PATH SETUP
# -------------------------
BASE_DIR = Path(__file__).parent

QUESTION_PDF = BASE_DIR / "ls_mock_test_BandC_t.pdf"
ANSWER_PDF   = BASE_DIR / "ls_mock_test_BandC_answer.pdf"
AUDIO_DIR    = BASE_DIR / "audio3"

# -------------------------
# PDF TEXT
# -------------------------
def extract_pdf_text(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text += t + "\n"
    return text


# -------------------------
# ANSWERS
# -------------------------
def parse_answers(answer_text):
    matches = re.findall(r"(\d+)\s*([A-D])", answer_text)
    return {int(n): a for n, a in matches}


# -------------------------
# AUDIO
# -------------------------
def scan_audio_folder(audio_dir):
    audio_map = defaultdict(list)

    for file in audio_dir.glob("*.mp3"):
        m = re.match(r"\d+-(\d+)(?:-\d+)?\.mp3", file.name)
        if m:
            q_id = int(m.group(1))
            audio_map[q_id].append(file.name)

    for q in audio_map:
        audio_map[q].sort()

    return audio_map


# -------------------------
# QUESTION PARSER (THE FIX)
# -------------------------
def parse_questions(text):
    questions = {}
    current_id = None

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        # Detect question number
        q_match = re.match(r"^(\d+)\.\s*(.*)", line)

        if q_match:
            q_id = int(q_match.group(1))
            content = q_match.group(2).strip()

            # First time seeing this question
            if q_id not in questions:
                questions[q_id] = {
                    "id": q_id,
                    "question": content,
                    "choices": {}
                }
            else:
                # Repeated number = choices will follow
                current_id = q_id

            current_id = q_id
            continue

        # Detect choice
        c_match = re.match(r"^（([A-D])）\s*(.+)", line)
        if c_match and current_id is not None:
            questions[current_id]["choices"][c_match.group(1)] = c_match.group(2)
            continue

        # Extra text → append to question ONLY if no choices yet
        if current_id is not None and not questions[current_id]["choices"]:
            questions[current_id]["question"] += " " + line

    return list(questions.values())


# -------------------------
# MAIN
# -------------------------
q_text = extract_pdf_text(QUESTION_PDF)
a_text = extract_pdf_text(ANSWER_PDF)

questions = parse_questions(q_text)
answers   = parse_answers(a_text)
audio_map = scan_audio_folder(AUDIO_DIR)

final = []

for q in questions:
    final.append({
        "id": q["id"],
        "audio": audio_map.get(q["id"], []),
        "image": None,
        "question": q["question"].strip(),
        "choices": q["choices"],
        "answer": answers.get(q["id"], "")
    })

# -------------------------
# OUTPUT
# -------------------------
for q in final:
    print("{")
    print(f'    "id": {q["id"]},')
    print(f'    "audio": {q["audio"]},')
    print('    "image": None,')
    print(f'    "question": "{q["question"]}",')
    print('    "choices": {')
    for k, v in q["choices"].items():
        print(f'        "{k}": "{v}",')
    print("    },")
    print(f'    "answer": "{q["answer"]}"')
    print("},\n")