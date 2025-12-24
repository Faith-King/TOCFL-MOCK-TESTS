# =========================
# UPGEN4.py — TOCFL Intelligent Generator (FIXED)
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

AUDIO_DIR = BASE_DIR / "audio_ba_vol4"
IMAGE_DIR = BASE_DIR / "image_lba_vol4"

MAX_QID = 50
DEFAULT_CHOICES = 3   # fallback only

FAILSAFE_QUESTION = ""
FAILSAFE_CHOICE   = ""

IGNORE_PREFIXES = (
    "以下這段",
    "請聽",
    "現在請聽",
    "說明",
    "例題",
    "第四部分",
    "第三部分",
    "第二部分",
    "第一部分",
    "例題如下",
    "第四題",
    "Directions",
    "男",
    "女",
)

# -------------------------
# PDF TEXT
# -------------------------
def extract_pdf_text(path):
    reader = PdfReader(path)
    out = []
    for page in reader.pages:
        t = page.extract_text()
        if t:
            out.append(t)
    return "\n".join(out)

# -------------------------
# ANSWERS
# -------------------------
def parse_answers(text):
    return {
        int(n): a
        for n, a in re.findall(r"(\d{1,3})\s*([A-D])", text)
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
    return audio

# -------------------------
# IMAGE MATCH
# -------------------------
def find_image(qid):
    for f in IMAGE_DIR.glob("*.png"):
        s = f.stem
        if "-" in s:
            a, b = map(int, s.split("-"))
            if a <= qid <= b:
                return f.name
        elif s.isdigit() and int(s) == qid:
            return f.name
    return None

# -------------------------
# CLEAN
# -------------------------
def clean(line):
    line = re.sub(r"[]", "", line)
    return line.strip()

# -------------------------
# PARSE QUESTIONS & CHOICES (TOCFL-AWARE)
# -------------------------
def parse_questions(text):
    questions = {}
    current_qid = None
    mode = None  # "question" | "choices"

    for raw in text.splitlines():
        line = clean(raw)
        if not line:
            continue

        if any(line.startswith(p) for p in IGNORE_PREFIXES):
            continue

        # Question text line
        m_q = re.match(r"^(\d{1,3})\.\s*(.+)", line)
        if m_q:
            qid = int(m_q.group(1))
            if qid > MAX_QID:
                continue

            questions.setdefault(qid, {
                "id": qid,
                "question": "",
                "choices": {}
            })

            questions[qid]["question"] = m_q.group(2).strip()
            current_qid = qid
            mode = "question"
            continue

        # Choice block header: "1."
        m_block = re.match(r"^(\d{1,3})\.$", line)
        if m_block:
            qid = int(m_block.group(1))
            if qid > MAX_QID:
                continue

            questions.setdefault(qid, {
                "id": qid,
                "question": "",
                "choices": {}
            })

            current_qid = qid
            mode = "choices"
            continue

        # Choice line
        if mode == "choices" and current_qid is not None:
            m_c = re.match(r"^[（(]([A-D])[）)]\s*(.+)", line)
            if m_c:
                questions[current_qid]["choices"][m_c.group(1)] = m_c.group(2).strip()

    return questions

# -------------------------
# NORMALIZE
# -------------------------
def normalize(q, audio_map, answers):
    qid = q["id"]
    detected = q["choices"]
    answer = answers.get(qid, "")

    expected = max(
        len(detected),
        4 if answer == "D" else DEFAULT_CHOICES
    )

    labels = ["A", "B", "C", "D"][:expected]

    final_choices = {
        k: detected.get(k, f"（{k}）{FAILSAFE_CHOICE}")
        for k in labels
    }

    return {
        "id": qid,
        "type": "listening" if qid in audio_map else "reading",
        "audio": audio_map.get(qid, []),
        "image": find_image(qid),
        "question": q["question"] or FAILSAFE_QUESTION,
        "choices": final_choices,
        "answer": answer
    }

# -------------------------
# MAIN
# -------------------------
q_text = extract_pdf_text(QUESTION_PDF)
a_text = extract_pdf_text(ANSWER_PDF)

answers   = parse_answers(a_text)
audio_map = scan_audio(AUDIO_DIR)
raw_qs    = parse_questions(q_text)

final = [
    normalize(raw_qs[qid], audio_map, answers)
    for qid in sorted(raw_qs)
    if qid <= MAX_QID
]

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