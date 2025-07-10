import requests
from bs4 import BeautifulSoup


def get_current_time():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://www.google.com/',  # Możesz dodać referer, jeśli chcesz
        'DNT': '1',  # Do Not Track request header
        'Connection': 'keep-alive'
    }
    try:
        response = requests.get("https://time.is/", headers=headers)
        response.raise_for_status()  # Sprawdź, czy nie ma błędów HTTP

        soup = BeautifulSoup(response.text, 'html.parser')

        # Godzina jest zwykle w elemencie <h1> z id 'twd' lub podobnym
        # Możesz potrzebować dostosować selektor, jeśli strona się zmieni
        time_element = soup.find(id="clock")
        if time_element:
            return time_element.text.strip()
        else:
            return "Nie udało się znaleźć elementu z godziną na stronie."

    except requests.exceptions.RequestException as e:
        return f"Wystąpił błąd podczas połączenia ze stroną: {e}"
    except Exception as e:
        return f"Wystąpił nieoczekiwany błąd: {e}"


current_time = get_current_time()
print(f"Aktualna godzina (według time.is): {current_time}")
