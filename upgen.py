# =========================
# UPGEN.py — Universal TOCFL Question Generator (IMAGE-BASED)
# =========================

import re
from pathlib import Path
from PyPDF2 import PdfReader
from collections import defaultdict

# -------------------------
# PATH SETUP
# -------------------------
BASE_DIR = Path(__file__).parent

QUESTION_PDF = BASE_DIR / "q.pdf"
ANSWER_PDF   = BASE_DIR / "a.pdf"
AUDIO_DIR    = BASE_DIR / "audio4"
IMAGE_DIR    = BASE_DIR / "images2"

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
    matches = re.findall(r"(\d+)\s*([A-F])", answer_text)
    return {int(n): a for n, a in matches}


# -------------------------
# AUDIO SCAN
# -------------------------
def scan_audio_folder(audio_dir):
    audio_map = defaultdict(list)

    for file in audio_dir.glob("*.mp3"):
        # X-YY-Z.mp3 → capture YY
        m = re.match(r"\d+-(\d+)(?:-\d+)?\.mp3", file.name)
        if m:
            audio_map[int(m.group(1))].append(file.name)

    for qid in audio_map:
        audio_map[qid].sort()

    return audio_map


# -------------------------
# IMAGE MATCHING
# -------------------------
def find_image(q_id):
    """
    Rules:
    - 31–35.png, 36–40.png, 41–45.png
    - 46.png, 47.png, ...
    """
    for file in IMAGE_DIR.glob("*.png"):
        name = file.stem.lstrip("b")  # safety

        if "-" in name:
            start, end = map(int, name.split("-"))
            if start <= q_id <= end:
                return file.name
        else:
            if name.isdigit() and int(name) == q_id:
                return file.name

    return None


# -------------------------
# QUESTION PARSER (NO PASSAGES)
# -------------------------
def parse_questions(text):
    questions = {}
    current_id = None

    IGNORE = [
        r"說明", r"Directions", r"Example", r"例題",
        r"Part", r"第\s*\d+～\d+\s*題",
        r"The correct answer", r"請把答案"
    ]

    def skip(line):
        return any(re.search(p, line) for p in IGNORE)

    for raw in text.splitlines():
        line = raw.strip()
        if not line or skip(line):
            continue

        # Question number
        q_match = re.match(r"^(\d{1,3})\.\s*(.*)", line)
        if q_match:
            qid = int(q_match.group(1))
            questions[qid] = {
                "id": qid,
                "question": q_match.group(2).strip(),
                "choices": {}
            }
            current_id = qid
            continue

        if current_id is None:
            continue

        # Choices
        c_match = re.match(r"^（([A-F])）\s*(.+)", line)
        if c_match:
            questions[current_id]["choices"][c_match.group(1)] = c_match.group(2)
            continue

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
    qid = q["id"]
    audio = audio_map.get(qid, [])
    image = find_image(qid)

    q_type = "listening" if audio else "reading"

    final.append({
        "id": qid,
        "type": q_type,
        "audio": audio,
        "image": image,
        "question": q["question"],
        "choices": q["choices"],
        "answer": answers.get(qid, "")
    })


# -------------------------
# OUTPUT
# -------------------------
for q in final:
    print("{")
    print(f'    "id": {q["id"]},')
    print(f'    "type": "{q["type"]}",')
    print(f'    "audio": {q["audio"]},')
    print(f'    "image": {repr(q["image"])},')
    print(f'    "question": "{q["question"]}",')
    print('    "choices": {')
    for k, v in q["choices"].items():
        print(f'        "{k}": "{v}",')
    print("    },")
    print(f'    "answer": "{q["answer"]}"')
    print("},\n")
