import tkinter as tk

kanji_list = [
    {"word": "喫煙所", "yomi": "きつえんじょ", "imi": "place for smoking"},
    {"word": "開放厳禁", "yomi": "かいほうげんきん", "imi": "strictly prohibited to open"},
    {"word": "同窓会", "yomi": "どうそうかい", "imi": "class reunion"},
    {"word": "線路", "yomi": "せんろ", "imi": "railway track"},
    {"word": "深刻な", "yomi": "しんこくな", "imi": "serious"},
    {"word": "家賃", "yomi": "やちん", "imi": "rent"},
    {"word": "郵便局", "yomi": "ゆうびんきょく", "imi": "post office"},
    {"word": "景色", "yomi": "けしき", "imi": "scenery"},
    {"word": "理解", "yomi": "りかい", "imi": "understanding"},
    {"word": "紅葉", "yomi": "こうよう", "imi": "autumn leaves"}
]

index = 0
score = 0

def check_answer():
    global score
    user = entry.get()
    correct = kanji_list[index]["yomi"]

    if user == correct:
        score += 1
        result_label.config(text="◯ 正解！", fg="green")
    else:
        result_label.config(
            text=f"✕ 不正解\n読み：{correct}\n意味：{kanji_list[index]['imi']}",
            fg="red"
        )

def next_question():
    global index

    if index == len(kanji_list) - 1:
        kanji_label.config(text="終了！")
        result_label.config(
            text=f"あなたのスコア：{score} / {len(kanji_list)}",
            fg="blue"
        )
        entry.pack_forget()
        next_button.pack_forget()
        check_button.pack_forget()
        return

    index += 1
    kanji_label.config(text=kanji_list[index]["word"])
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("漢字の読みクイズ")
root.geometry("320x280")

kanji_label = tk.Label(root, text=kanji_list[index]["word"], font=("Arial", 20))
kanji_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

check_button = tk.Button(root, text="答え合わせ", command=check_answer)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

next_button = tk.Button(root, text="次へ", command=next_question)
next_button.pack(pady=5)

root.mainloop()
