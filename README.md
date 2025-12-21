This is the UPGEN!

So basically Generator, building this project takes a lot of time (If I do it manually), so I decided to make an AUTOMATED Machinary to solve this problem. The logic behind it is basically put a PDF file (question and answer), and audio folder that you downloaded combine them into one folder:

TOCFL/
├─ questions.pdf
├─ answers.pdf
├─ audio (folder)
├─ UPGEN.py

Then run the `UPGEN.py` this will save you bunch of time from copy pasting 1 by 1 each question into the format of:

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
