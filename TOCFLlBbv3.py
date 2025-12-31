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
    "A": "她不參加比賽",
    "B": "她要自己唱一首歌",
    "C": "她還沒決定要不要參加",
    "D": "她要和這位先生一起練習",
  },
  "answer": "A"
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
    "D": "（D）",
  },
  "answer": "C"
},

{
  "id": 3,
  "type": "listening",
  "audio": ['1-03.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她老了才打算開始唸書",
    "B": "她認為人要不斷地學習",
    "C": "她不清楚為什麼別人讚美 她",
    "D": "她認為多唸書，可以活得久",
  },
  "answer": "B"
},

{
  "id": 4,
  "type": "listening",
  "audio": ['1-04.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "電影七點半才開始",
    "B": "電影七點二十分才開始",
    "C": "還有二十分電影才開始",
    "D": "還有半小時電影才開始",
  },
  "answer": "D"
},

{
  "id": 5,
  "type": "listening",
  "audio": ['1-05.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "換了新的食物",
    "B": "換了新的老闆",
    "C": "不再做生意了",
    "D": "休息七天才開門",
  },
  "answer": "C"
},

{
  "id": 6,
  "type": "listening",
  "audio": ['1-06.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "醫院",
    "B": "學校",
    "C": "餐廳",
    "D": "計程車上",
  },
  "answer": "A"
},

{
  "id": 7,
  "type": "listening",
  "audio": ['1-07.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "少了一塊錢",
    "B": "少了不少錢",
    "C": "多了一塊錢",
    "D": "錢不多也不少",
  },
  "answer": "D"
},

{
  "id": 8,
  "type": "listening",
  "audio": ['1-08.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "感冒症狀比想像中 嚴重",
    "B": "光喝開水對身體沒幫助",
    "C": "不吃藥可能會要他的命",
    "D": "飲食習慣本來就有問題",
  },
  "answer": "D"
},

{
  "id": 9,
  "type": "listening",
  "audio": ['1-09.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "客人太多讓服務的水準降低",
    "B": "餐廳食物的味道沒以前的好",
    "C": "不應該接受電視節目的訪問",
    "D": "服務生得罪很多常來的客人",
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
    "A": "她已經習慣週末要加班",
    "B": "她覺得自己的工作比較輕鬆",
    "C": "她經常利用週末和客戶吃飯",
    "D": "她不相信這位先生週末要加班",
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
    "A": "現在的皮椅都是七八十萬",
    "B": "打折以後，買皮椅的人不少",
    "C": "再貴一點的皮椅就沒有人買了",
    "D": "不少人買得起七八十萬的皮椅",
  },
  "answer": "D"
},

{
  "id": 12,
  "type": "listening",
  "audio": ['1-12.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "沒法跟老劉講道理",
    "B": "是個沒有原則的人",
    "C": "堅持立場、值得尊敬",
    "D": "再多勸 一下，他就會讓步",
  },
  "answer": "A"
},

{
  "id": 13,
  "type": "listening",
  "audio": ['1-13.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "連決賽都沒進",
    "B": "只得到一個獎",
    "C": "一個獎都沒 得到",
    "D": "只有一 項沒得獎",
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
    "A": "老王的眼睛不好",
    "B": "老王做事很嚴謹",
    "C": "老王個性很馬虎",
    "D": "老王不喜歡小趙",
  },
  "answer": "B"
},

{
  "id": 15,
  "type": "listening",
  "audio": ['1-15.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "小趙拒絕了她",
    "B": "小趙不值得信賴",
    "C": "小趙對工作很失望",
    "D": "她怕小趙不會答應",
  },
  "answer": "B"
},

{
  "id": 16,
  "type": "listening",
  "audio": ['1-16.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "這麼做一定行得通",
    "B": "她想買保險以免發生問題",
    "C": "因為已保了險，所以沒問題",
    "D": "這麼做風險很高，但值得冒險嘗試",
  },
  "answer": "A"
},

{
  "id": 17,
  "type": "listening",
  "audio": ['1-17.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "小劉的父母要求太多",
    "B": "小劉還沒有顯著的成就",
    "C": "小劉沒滿足父母最大的期待",
    "D": "小劉的 父母不要求兒子有成就",
  },
  "answer": "C"
},

{
  "id": 18,
  "type": "listening",
  "audio": ['1-18.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "做這個案子得花時間",
    "B": "做這個案子並不容易",
    "C": "做這個案子不必認真",
    "D": "做這個案子要有能力",
  },
  "answer": "C"
},

{
  "id": 19,
  "type": "listening",
  "audio": ['1-19.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "二樓的視野比一樓好多了",
    "B": "她認為這位先生的建議 不錯",
    "C": "一樓的票太貴了，她付不起",
    "D": "沒必要考慮能不能看見表演者",
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
    "A": "只想維持普通朋友的關係",
    "B": "想進一步了解小王的為人",
    "C": "覺得小王是不錯的交往對象",
    "D": "和小王聊天一點意思也沒有",
  },
  "answer": "A"
},

{
  "id": 21,
  "type": "listening",
  "audio": ['1-21.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "非常厭惡",
    "B": "充滿期待",
    "C": "不怎麼在乎",
    "D": "不知怎麼處理",
  },
  "answer": "D"
},

{
  "id": 22,
  "type": "listening",
  "audio": ['1-22.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他從來就沒捐過錢",
    "B": "他不知道捐款的去向",
    "C": "他自己也是水災災民",
    "D": "他覺得自己捐的錢不夠多",
  },
  "answer": "B"
},

{
  "id": 23,
  "type": "listening",
  "audio": ['1-23.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他請對方把錢還給他",
    "B": "他決定幫對方一起募款",
    "C": "他請對方提出證明再說",
    "D": "他覺得對方有誠意，答應捐錢",
  },
  "answer": "C"
},

{
  "id": 24,
  "type": "listening",
  "audio": ['1-24.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "店員打錯發票",
    "B": "店員算錯金額",
    "C": "客人拿錯商品",
    "D": "客人跑錯商店",
  },
  "answer": "D"
},

{
  "id": 25,
  "type": "listening",
  "audio": ['1-25.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "若要享受折扣，得到指定的店家",
    "B": "折扣活動從今年初到這個月月底",
    "C": "這個活動是附近商店聯合舉辦的",
    "D": "在這個月內消費就可以加入會員",
  },
  "answer": "A"
},

{
  "id": 26,
  "type": "listening",
  "audio": ['1-26.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "他很排斥",
    "B": "他可以接受",
    "C": "他建議再觀察",
    "D": "他不想談這個話題",
  },
  "answer": "A"
},

{
  "id": 27,
  "type": "listening",
  "audio": ['1-27.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "她不相信醫學研究的結果",
    "B": "她認為這則報導讓人安心",
    "C": "她不認同這位先生的看法",
    "D": "她要這位先生再去找資料",
  },
  "answer": "C"
},

{
  "id": 28,
  "type": "listening",
  "audio": ['1-28.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為他太太 總是沉默寡言",
    "B": "因為他太太 只吃酸的食物",
    "C": "因為他太太的表現不同以往",
    "D": "因為他誤會太太下廚的美意",
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
    "A": "跟太太 一起去吃飯",
    "B": "買了一把傘送給太太",
    "C": "和女性朋友共撐一把傘",
    "D": "向附近 的小攤販 買東西",
  },
  "answer": "D"
},

{
  "id": 30,
  "type": "listening",
  "audio": ['1-30.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "上午十點以前",
    "B": "上午四點以後",
    "C": "下午四點以前，晚上十點以後",
    "D": "下午四點以後，晚上十點以前",
  },
  "answer": "A"
},

{
  "id": 31,
  "type": "listening",
  "audio": ['1-31.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "小青常去房東家學習做點心",
    "B": "房東沒有孩子，所以很喜歡小青",
    "C": "她們吃蛋糕的時候喜歡聊工作的事",
    "D": "房東覺得小青就像自己的孩子一樣",
  },
  "answer": "D"
},

{
  "id": 32,
  "type": "listening",
  "audio": ['1-32.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "音樂有助於減輕疼痛",
    "B": "聽音樂就不用看醫生",
    "C": "有病就應該去看醫生",
    "D": "多聽醫生推薦 的音樂",
  },
  "answer": "A"
},

{
  "id": 33,
  "type": "listening",
  "audio": ['1-33.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "在家休息",
    "B": "去看醫生",
    "C": "去學校找小文",
    "D": "和小文去看電影",
  },
  "answer": "A"
},

{
  "id": 34,
  "type": "listening",
  "audio": ['1-34.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "藥水",
    "B": "課本",
    "C": "雨傘",
    "D": "電影票",
  },
  "answer": "C"
},

{
  "id": 35,
  "type": "listening",
  "audio": ['1-35.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為她吃得太飽",
    "B": "因為她吃錯了藥",
    "C": "因為她肚子很疼",
    "D": "因為她肚子餓了",
  },
  "answer": "C"
},

{
  "id": 36,
  "type": "listening",
  "audio": ['2-36.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "先不要吃任何東西",
    "B": "綠色的藥不一定要吃",
    "C": "已經不需要再吃藥了",
    "D": "白色的藥都吃完了，再吃綠的",
  },
  "answer": "B"
},

{
  "id": 37,
  "type": "listening",
  "audio": ['2-37.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "夏天才有",
    "B": "皮也能吃",
    "C": "北方才有",
    "D": "放幾天再吃，更好吃",
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
    "A": "變得不香",
    "B": "變得不好吃",
    "C": "肉的顏色改變",
    "D": "皮的顏色改變",
  },
  "answer": "D"
},

{
  "id": 39,
  "type": "listening",
  "audio": ['2-39.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "小周的旅遊計畫",
    "B": "去美國玩要注意的事",
    "C": "介紹美國好玩兒的地方",
    "D": "小周一家人出 去玩的事",
  },
  "answer": "D"
},

{
  "id": 40,
  "type": "listening",
  "audio": ['2-40.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "小周很習慣美國的天氣",
    "B": "小周對那家飯店很滿意",
    "C": "小周在美國天天吃中國菜",
    "D": "小周帶了三個小孩兒去美國",
  },
  "answer": "B"
},

{
  "id": 41,
  "type": "listening",
  "audio": ['2-41.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "沒有送報紙和水果",
    "B": "每一間的費用都一樣",
    "C": "要停車的話，得付停車費",
    "D": "今年年底去住，比平常便宜",
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
    "A": "這個活動到明年 2月底結束",
    "B": "每天只有二十個人能住這些房間",
    "C": "前二十個打電話來的人不必付錢",
    "D": "費用和平常一樣，但提供更多服務",
  },
  "answer": "A"
},

{
  "id": 43,
  "type": "listening",
  "audio": ['2-43.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "常有學生 掉東西",
    "B": "常有學生忘了還書",
    "C": "常有學生用手機聊天",
    "D": "常有學生忘了 把書包帶走",
  },
  "answer": "A"
},

{
  "id": 44,
  "type": "listening",
  "audio": ['2-44.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "請警察協助處理",
    "B": "校方正密切觀察",
    "C": "請學生留意陌生人",
    "D": "請學生說明當時的狀況",
  },
  "answer": "B"
},

{
  "id": 45,
  "type": "listening",
  "audio": ['2-45.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "因為政府 的大力推銷",
    "B": "因為電影導演的介紹",
    "C": "因為小鎮找電影明星來宣傳",
    "D": "因為觀眾 被電影中的小鎮文化吸引",
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
    "A": "小鎮開始發展文化產業",
    "B": "促進小鎮的觀光經濟發展",
    "C": "使地方小吃成了國際美食",
    "D": "讓居民重新認識小鎮風景",
  },
  "answer": "B"
},

{
  "id": 47,
  "type": "listening",
  "audio": ['2-47.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "努力與電影產業結合",
    "B": "降低價格吸引更多客人",
    "C": "應該積極爭取政府資源",
    "D": "飯店經營需結合當地特 色",
  },
  "answer": "D"
},

{
  "id": 48,
  "type": "listening",
  "audio": ['2-48.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "犯罪集團的組成份子",
    "B": "跨國犯罪猖獗的原因",
    "C": "兩國警方怎麼合作緝兇",
    "D": "警方怎麼成功攔截古董",
  },
  "answer": "C"
},

{
  "id": 49,
  "type": "listening",
  "audio": ['2-49.mp3'],
  "image": None,
  "question": "",
  "choices": {
    "A": "為了換取一頓溫飽",
    "B": "為了一趟免費旅行",
    "C": "為了價值連城的字畫",
    "D": "為了救出被囚禁的朋友",
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
    "A": "跨國追緝犯罪集團首腦",
    "B": "和阿國協商，將少女帶回",
    "C": "根據情報，蒐集犯罪證據",
    "D": "運用高科技追查少女位置",
  },
  "answer": "D"
},
]

# PATHS
BASE_DIR = Path(__file__).parent
AUDIO_DIR = BASE_DIR / "audio_bb_vol3"
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