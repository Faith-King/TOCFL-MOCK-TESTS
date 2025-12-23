# This is the UPGEN!

So basically Generator, building this project takes a lot of time (If I do it manually), so I decided to make an AUTOMATED Machinary to solve this problem. The logic behind it is basically put a PDF file (question and answer), and audio folder that you downloaded combine them into one folder:

TOCFL/

├─ questions.pdf

├─ answers.pdf

├─ audio (folder)

├─ UPGEN.py

### Then run the `UPGEN.py` this will save you bunch of time from copy pasting 1 by 1 each question into the format of:

```
{
    "id": x,
    "audio": ['audio1.mp3'],
    "image": "Image.png" or None,
    "question": "query?",
    "choices": {
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D",
    },
    "answer": "A/B/C/D"
},
```

# 📘 UPGEN4.py, TOCFL Question Generator (Stable / Failsafe)

**UPGEN4.py** is a Python tool designed to automatically generate structured TOCFL mock-test questions from official PDFs.
It extracts **questions**, **choices**, **answers**, links them with **audio files** and **images**, and outputs a clean, normalized question bank ready for use in testing apps or CLI exam simulators.

This version focuses on **stability**, **error tolerance**, and **predictable output**, even when PDFs are messy, inconsistent, or poorly formatted.


## ⚙️ CONFIG SECTION (IMPORTANT)

The `CONFIG` block is the **control panel** of UPGEN4.py.
Most customisation happens here, no need to touch the core logic.

### 📂 File Paths

```python
QUESTION_PDF = BASE_DIR / "q.pdf"
ANSWER_PDF   = BASE_DIR / "a.pdf"
```

* `q.pdf` → PDF containing **questions + choices**
* `a.pdf` → PDF containing **answer keys**
* These filenames can be changed freely as long as the PDFs follow TOCFL formatting.


### 🔊 Audio Directory

```python
AUDIO_DIR = BASE_DIR / ""
```

* Folder containing all `.mp3` audio files
* Audio files are auto-matched to question numbers using filename patterns
  (example: `3-45.mp3` → Question 45)
* If audio exists → question is marked as **listening**
* If not → **reading**


### 🖼 Image Directory

```python
IMAGE_DIR = BASE_DIR / "image_bc_vol5"
```

* Folder containing question images (`.png`)
* Supports:

  * single images (`12.png`)
  * ranged images (`44-46.png`)
* Images are matched automatically based on question ID


### 🔢 Question Limit

```python
MAX_QID = 50
```

* Hard stop for parsing questions
* Prevents:

  * reading answer explanations
  * parsing extra sections
  * PDF overflow junk
* Adjust if your test has more or fewer questions


### 🔠 Default Choices

```python
DEFAULT_CHOICES = 3
```

Controls how many choices are expected **when parsing fails**:

* `3` → A, B, C (typical listening section)
* `4` → A, B, C, D (typical reading section)

UPGEN automatically overrides this when audio is detected.


### 🛟 Failsafe Values

```python
FAILSAFE_QUESTION = ""
FAILSAFE_CHOICE   = ""
```

Used when:

* question text is missing or corrupted
* choices cannot be reliably parsed

Instead of crashing or producing broken JSON, UPGEN **fills in safe placeholders** so output stays structurally valid.

This is intentional. Stability > perfection.


## ✅ What This Script Does Well

* Survives ugly PDFs
* Handles mixed layouts (inline choices, table formats)
* Distinguishes listening vs reading automatically
* Never crashes on malformed questions
* Produces consistent, normalized output


## ⚠️ What It Does *Not* Do

* OCR scanned PDFs
* Auto-crop images from PDFs
* Understand passages semantically
