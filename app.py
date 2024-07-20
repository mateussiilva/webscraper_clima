import requests
from bs4 import BeautifulSoup
import sys

CODE_OK = 200


def request_data(city: str) -> str | None:
    with requests.get(f"https://www.tempo.com/{city}.htm") as rep:
        if rep.status_code == CODE_OK:
            return rep.text
        else:
            return None


def get_temparature_atual(text_html: str) -> str:

    soup = BeautifulSoup(text_html, "html.parser")
    element = soup.find(
        "span", attrs={"class": "dato-temperatura changeUnitT"})
    return element.text


if __name__ == "__main__":
    args = sys.argv
    city = args[1]
    response = request_data(city)
    if response is not None:
        print(f"Buscando o clima atual de {city}")
        temp = get_temparature_atual(response)
        print("A Temperatura atual é: ", temp)
    else:
        print("Cidade Invalida....Tente Novament")
