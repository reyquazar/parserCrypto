import json
import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup as bs


async def make_request(url):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx GX 03)"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            text = await resp.text()
            return bs(text, 'lxml')


async def coinbase():
    soup = await make_request("https://www.coinbase.com/explore")
    all_options = soup.find_all(
        class_="cds-typographyResets-t1xhpuq2 cds-body-bvviwwo cds-currentColor-cl6elq7 cds-transition-txjiwsi cds-start-s1muvu8a")
    all_names = soup.find_all(
        class_="cds-typographyResets-t1xhpuq2 cds-headline-hb7l4gg cds-foreground-f1yzxzgu cds-transition-txjiwsi cds-start-s1muvu8a")
    options_array = []  # добавляем в массив цен те значения, которые не имею букв BTM и начинаются на R (там все начинаются с "RUBB ")
    for option in all_options:
        option_text = option.text
        if option_text.startswith("R") and not option_text.endswith(("B", "T", "M")):
            option_text = "".join(char for char in option_text if char.isnumeric() or char == ".")
            options_array.append(float(option_text))
    name_array = []  # добавляем в массив все названия криптовалют
    for name in all_names:
        name_text = name.text
        name_array.append(name_text)
    cryptoDict = dict(zip(name_array, options_array))  # соединяем в словарь
    # создаем на основе словаря json файл
    with open("JSON/cryptoDictCOINBASE.json", "w") as file:
        json.dump(cryptoDict, file, indent=4, ensure_ascii=False)


async def kucoin():
    soup = await make_request("https://www.kucoin.com/ru/markets")
    all_options = soup.find_all(class_='lrtcss-yea6ot ej80wqq4')
    all_names = soup.find_all(class_="lrtcss-1jzqi98 ej80wqq5")

    options_array = []
    for option in all_options:
        option_text = option.text.replace(' $', '')
        option_text = "".join(char for char in option_text if char.isnumeric() or char == ".")
        options_array.append(float(option_text))

    name_array = []
    for name in all_names:
        name_text = name.text
        name_array.append(name_text)

    cryptoDict = dict(zip(name_array, options_array))  # соединяем в словарь
    # создаем на основе словаря json файл
    with open("JSON/cryptoDictKUCOIN.json", "w") as file:
        json.dump(cryptoDict, file, indent=4, ensure_ascii=False)


async def myfin():
    soup = await make_request("https://myfin.by/crypto-rates")
    cryptoDict = dict()
    names = soup.find_all('span', class_='crypto__name fake-link')
    prices = soup.find_all('span', class_='accent')
    for name, price in zip(names, prices):
        cryptoDict[name.text] = float(price.text)
    with open("JSON/cryptoDictMYFIN.json", "w") as file:
        json.dump(cryptoDict, file, indent=4, ensure_ascii=False)


async def main():
    await coinbase()
    await kucoin()
    await myfin()


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    finish_time = time.time() - start_time
    print(finish_time)
