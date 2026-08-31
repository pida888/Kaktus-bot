from bs4 import BeautifulSoup
import os
import requests

# 🔑 Načtení klíčů ze Secrets v GitHubu
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


# 📬 Funkce pro odeslání zprávy
def posli_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    odpoved = requests.post(url, data=data)
    return odpoved.status_code == 200


# 🌐 1. Stažení webu
url_kaktus = "https://www.mujkaktus.cz/chces-pridat"
odpoved = requests.get(url_kaktus)
soup = BeautifulSoup(odpoved.text, "html.parser")

prvek = soup.find("span", class_="font-bold")

if prvek:
    termin = prvek.text.strip()
    print(f"Aktuální termín na webu: {termin}")

    # 📖 2. Načtení posledního uloženého termínu
    try:
        with open("posledni_zprava.txt", "r", encoding="utf-8") as soubor:
            posledni_termin = soubor.read().strip()
    except FileNotFoundError:
        posledni_termin = ""

    # 🔍 3. Porovnání
    if termin != posledni_termin:
        print("Zjištěn nový termín! Odesílám notifikaci... 🚀")
        zprava = f"🌵 Kaktus Dobíječka:\n{termin}"
        if posli_telegram(zprava):
            with open("posledni_zprava.txt", "w", encoding="utf-8") as soubor:
                soubor.write(termin)
            print("Zpráva odeslána a termín uložen.")
    else:
        print("Termín je stále stejný. Žádná zpráva se neodesílá. 💤")
else:
    print("Termín se na webu nepodařilo najít. ❌")
