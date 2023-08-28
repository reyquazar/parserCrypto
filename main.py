import json
import requests

from bs4 import BeautifulSoup as bs


def coinbase():
    url = "https://www.coinbase.com/explore"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx GX 03)"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    soup = bs(src, "lxml")

    # парсим по определенному классу
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


def kucoin():
    url = "https://www.kucoin.com/ru/markets"

    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx GX 03)"
    }

    req = requests.get(url, headers=headers)
    src = req.text

    # with open("index.html", encoding="utf-8") as file:
    #     src = file.read()

    soup = bs(src, "lxml")

    # with open("index.html", "w", encoding="utf-8") as file:
    #     file.write(src)

    # парсим по определенному классу
    all_options = soup.find_all(class_='lrtcss-yea6ot ej80wqq4')
    all_names = soup.find_all(class_="lrtcss-1jzqi98 ej80wqq5")

    options_array = []  # добавляем в массив цен
    for option in all_options:
        option_text = option.text.replace(' $', '')
        option_text = "".join(char for char in option_text if char.isnumeric() or char == ".")
        options_array.append(float(option_text))

    name_array = []  # добавляем в массив все названия криптовалют
    for name in all_names:
        name_text = name.text
        name_array.append(name_text)

    cryptoDict = dict(zip(name_array, options_array))  # соединяем в словарь
    # создаем на основе словаря json файл
    with open("JSON/cryptoDictKUCOIN.json", "w") as file:
        json.dump(cryptoDict, file, indent=4, ensure_ascii=False)
    print('Готов')
    print(cryptoDict)


def kraken():
    # url = "https://www.kraken.com/ru-ru/prices"
    #
    # headers = {
    #     "Accept": "*/*",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.0 (Edition Yx GX 03)"
    # }
    #
    # req = requests.get(url, headers=headers)
    # src = req.text

    with open("index.html", encoding="utf-8") as file:
        src = file.read()

    soup = bs(src, "lxml")

    # with open("index.html", "w", encoding="utf-8") as file:
    #     file.write(src)

    # парсим по определенному классу
    all_options = soup.find_all('td')

    # all_names = soup.find_all(class_="lrtcss-1jzqi98 ej80wqq5")

    options_array = []  # добавляем в массив цен
    for option in all_options:
        option_text = option.text
        if option_text.startswith("R") and not option_text.endswith(("B", "T", "M")):
            option_text = "".join(char for char in option_text if char.isnumeric() or char == ".")
            # options_array.append(float(option_text))
            print(option_text)
    # option_text = option.text.replace(' $', '')
    # option_text = "".join(char for char in option_text if char.isnumeric() or char == ".")
    # options_array.append(float(option_text))

    # print(options_array)
    # name_array = []  # добавляем в массив все названия криптовалют
    # for name in all_names:
    #     name_text = name.text
    #     name_array.append(name_text)


def main():
    coinbase()
    kucoin()
    kraken()


if __name__ == "__main__":
    main()
