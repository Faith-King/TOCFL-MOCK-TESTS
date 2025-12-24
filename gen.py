# =========================
# Gen1.py — RAW QUESTION GENERATOR
# =========================

import re

# -------------------------
# CONFIG
# -------------------------

AUDIO_PREFIX = "1-"     # change to 2-, 3-, etc
START_AUDIO = 1         # starting audio index

RAW_TEXT = """
1.
（A）盡快搬家
（B）不付房租
（C）繼續住下去
（D）找人一起租

2.
小王最近搬家了，因為房租太貴。
他最後決定——

（A）盡快搬家
（B）不付房租
（C）繼續住下去
（D）找人一起租
"""

# 1.
# （A）盡快搬家
# （B）不付房租
# （C）繼續住下去
# （D）找人一起租
# 2.
# （A）他不要押金了
# （B）他決定再住一天就搬家
# （C）他要押金，但不打算搬家
# （D）他拿到押金以後才要搬家 
# 3.
# （A）能克服天生的障礙
# （B）專門為殘障兒童作曲
# （C）文章寫得比作家還好
# （D）將父親的作品寫成曲子
# 4.
# （A）會讓人想睡覺
# （B）能幫助人們創作音樂
# （C）會讓人們忘了要睡覺
# （D）會介紹他兒子的音樂
# 5. 
# 小明是一個男孩子，他住在爺爺的家。
# 小明住在哪裡？
# （A）在家裡
# （B）在他的爺爺家
# （C）沒有家
# （D）他死了

# -------------------------
# PARSER
# -------------------------
def parse_block(block):
    lines = [l.strip() for l in block.splitlines() if l.strip()]
    passage = []
    choices = {}

    for line in lines:
        m = re.match(r"（([A-D])）(.+)", line)
        if m:
            choices[m.group(1)] = m.group(2)
        else:
            passage.append(line)

    return " ".join(passage), choices


def generate_questions(raw_text):
    parts = re.split(r"\n\s*(\d+)\.\s*", raw_text.strip())
    audio_index = START_AUDIO
    results = []

    for i in range(1, len(parts), 2):
        q_id = int(parts[i])
        body = parts[i + 1]

        passage, choices = parse_block(body)

        q = {
            "id": q_id,
            "audio": [f"{AUDIO_PREFIX}{audio_index:02d}.mp3"],
            "image": None,
            "question": passage,
            "choices": choices,
            "answer": ""
        }

        results.append(q)
        audio_index += 1

    return results


# -------------------------
# OUTPUT
# -------------------------
questions = generate_questions(RAW_TEXT)

for q in questions:
    print("{")
    print(f'    "id": {q["id"]},')
    print(f'    "audio": {q["audio"]},')
    print('    "image": None,')
    print(f'    "question": "{q["question"]}",')
    print('    "choices": {')
    for k, v in q["choices"].items():
        print(f'        "{k}": "{v}",')
    print("    },")
    print('    "answer": ""')
    print("},\n")