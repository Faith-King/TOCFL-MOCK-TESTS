# =========================
# UPGEN.py — TOCFL Generator (STABLE / FAILSAFE)
# =========================

import re
from pathlib import Path
from PyPDF2 import PdfReader
from collections import defaultdict

# -------------------------
# CONFIG
# -------------------------
BASE_DIR = Path(__file__).parent

QUESTION_PDF = BASE_DIR / "q.pdf"
ANSWER_PDF   = BASE_DIR / "a.pdf"

AUDIO_DIR = BASE_DIR / ""
IMAGE_DIR = BASE_DIR / "image_bc_vol5"

MAX_QID = 50

# DEFAULT_CHOICES:
# 3 → A B C
# 4 → A B C D
DEFAULT_CHOICES = 3

FAILSAFE_QUESTION = ""
FAILSAFE_CHOICE   = ""

# -------------------------
# PDF TEXT
# -------------------------
def extract_pdf_text(path):
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        t = page.extract_text()
        if t:
            text.append(t)
    return "\n".join(text)


# -------------------------
# ANSWERS
# -------------------------
def parse_answers(text):
    return {
        int(n): a
        for n, a in re.findall(r"(\d{1,3})\s*([A-F])", text)
    }


# -------------------------
# AUDIO
# -------------------------
def scan_audio(audio_dir):
    audio = defaultdict(list)

    for f in audio_dir.glob("*.mp3"):
        m = re.match(r"\d+-(\d+)", f.name)
        if m:
            audio[int(m.group(1))].append(f.name)

    for k in audio:
        audio[k].sort()

    return audio


# -------------------------
# IMAGE MATCH
# -------------------------
def find_image(qid):
    for f in IMAGE_DIR.glob("*.png"):
        name = f.stem
        if "-" in name:
            a, b = map(int, name.split("-"))
            if a <= qid <= b:
                return f.name
        elif name.isdigit() and int(name) == qid:
            return f.name
    return None


# -------------------------
# CLEAN LINE
# -------------------------
def clean(line):
    line = re.sub(r"[]", "", line)
    return line.strip()


# -------------------------
# PARSE QUESTIONS
# -------------------------
def parse_questions(text):
    questions = {}
    current_id = None

    for raw in text.splitlines():
        line = clean(raw)
        if not line:
            continue

        # Question number (strict)
        m_q = re.match(r"^(\d{1,3})\.\s*(.*)", line)
        if m_q:
            qid = int(m_q.group(1))
            if qid > MAX_QID:
                break

            questions[qid] = {
                "id": qid,
                "question": m_q.group(2).strip(),
                "choices": {}
            }
            current_id = qid
            continue

        if current_id is None:
            continue

        # Choice lines
        m_c = re.match(r"^[（(]([A-F])[）)]\s*(.+)", line)
        if m_c:
            questions[current_id]["choices"][m_c.group(1)] = m_c.group(2).strip()
            continue

        # Inline choices inside question
        inline = re.findall(r"[（(]([A-F])[）)]\s*([^（(]+)", line)
        if inline and not questions[current_id]["choices"]:
            questions[current_id]["question"] = re.split(r"[（(]A[）)]", line)[0].strip()
            for k, v in inline:
                questions[current_id]["choices"][k] = v.strip()

    return questions


# -------------------------
# NORMALIZE / FAILSAFE
# -------------------------
def normalize(q, audio_map, answers):
    qid = q["id"]
    audio = audio_map.get(qid, [])
    qtype = "listening" if audio else "reading"

    # Question text sanity
    if len(q["question"]) < 3:
        q["question"] = FAILSAFE_QUESTION

    # Choices sanity
    expected = 3 if qtype == "listening" else DEFAULT_CHOICES
    labels = ["A", "B", "C", "D"][:expected]

    if len(q["choices"]) != expected:
        q["choices"] = {
            k: f"（{k}）{FAILSAFE_CHOICE}"
            for k in labels
        }

    return {
        "id": qid,
        "type": qtype,
        "audio": audio,
        "image": find_image(qid),
        "question": q["question"],
        "choices": q["choices"],
        "answer": answers.get(qid, "")
    }


# -------------------------
# MAIN
# -------------------------
q_text = extract_pdf_text(QUESTION_PDF)
a_text = extract_pdf_text(ANSWER_PDF)

answers   = parse_answers(a_text)
audio_map = scan_audio(AUDIO_DIR)
raw_qs    = parse_questions(q_text)

final = []

for qid in sorted(raw_qs):
    if qid > MAX_QID:
        continue
    final.append(normalize(raw_qs[qid], audio_map, answers))


# -------------------------
# OUTPUT
# -------------------------
for q in final:
    print("{")
    print(f'  "id": {q["id"]},')
    print(f'  "type": "{q["type"]}",')
    print(f'  "audio": {q["audio"]},')
    print(f'  "image": {repr(q["image"])},')
    print(f'  "question": "{q["question"]}",')
    print('  "choices": {')
    for k, v in q["choices"].items():
        print(f'    "{k}": "{v}",')
    print("  },")
    print(f'  "answer": "{q["answer"]}"')
    print("},\n")
