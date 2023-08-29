import tkinter as tk
import json
import asyncio
import aiohttp

from main_async import coinbase, kucoin, myfin, myfin_btc


def update_coinbase():
    asyncio.run(coinbase())

    with open("JSON/cryptoDictCOINBASE.json", "r") as file:
        cryptoDict = json.load(file)

    for child in root.winfo_children():
        child.destroy()

    row = 0
    for key, value in cryptoDict.items():
        square = tk.Canvas(root, width=50, height=50, bg="white")
        square.grid(row=row, column=0, padx=10, pady=10)
        text = square.create_text(25, 25, text=f"{value}", fill="black")
        label = tk.Label(root, text=f"{key}", fg="black")
        label.grid(row=row, column=1)
        row += 1


root = tk.Tk()

button = tk.Button(root, text="Update Coinbase JSON", command=update_coinbase)
button.pack()

root.mainloop()
