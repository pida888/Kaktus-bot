# 🌵 Kaktus Dobíječka Bot

Automatický scraper a notifikátor, který v pravidelných intervalech hlídá vyhlášení akce **Kaktus Dobíječka** na oficiálním webu a nově vypsané termíny okamžitě odesílá na Telegram.

Projekt běží zcela zdarma a bezúdržbově v cloudu pomocí **GitHub Actions**.

---

## ✨ Hlavní funkce

* 🌐 **Přímý scraping webu:** Data získává přímo z oficiální stránky `mujkaktus.cz` bez závislosti na cizích API třetích stran.
* 📲 **Telegram notifikace:** Odesílá zprávu s přesným datem a časem konání akce.
* 🧠 **Ochrana proti spamu:** Pamatuje si poslední odeslaný termín (`posledni_zprava.txt`) a neposílá duplicitní zprávy.
* ☁️ **100% Serverless:** Skript se automaticky spouští každých 30 minut přes cron v GitHub Actions.

---

## 🛠️ Použité technologie

* **Python 3.11**
* **Requests** (HTTP komunikace s webem a Telegram Bot API)
* **BeautifulSoup4** (Parsování HTML struktury webu)
* **GitHub Actions** (Automatizovaný CI/CD plánovač a spouštěč)

---

## ⚙️ Nastavení a instalace

### 1. Nastavení Telegramu
1. V aplikaci Telegram kontaktuj `@BotFather` a vytvoř nového bota pomocí `/newbot`.
2. Získej **API Token** bota.
3. Zjisti své **Chat ID** (např. přes `@userinfobot`).

### 2. Konfigurace GitHub Secrets
V nastavení repozitáře přejdi do **Settings ➔ Secrets and variables ➔ Actions** a přidej dva tajné klíče:

| Secret | Popis |
| :--- | :--- |
| `BOT_TOKEN` | Token tvého Telegram bota od BotFather |
| `CHAT_ID` | Číselné ID tvého Telegram chatu |

---

## 📂 Struktura projektu

```text
├── .github/
│   └── workflows/
│       └── kaktus.yml         # GitHub Actions konfigurace (cron plánovač)
├── kaktus_bot.py              # Hlavní Python skript (scraping + odesílání)
├── requirements.txt           # Seznam externích knihoven
├── posledni_zprava.txt        # Automaticky spravovaná historie posledního termínu
└── README.md                  # Dokumentace projektu
