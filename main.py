import json
import requests


lista = list()

def requisicao():
    r = requests.get("https://api.hgbrasil.com/weather?woeid=90200707")
    rq = json.loads(r.text)
    dadosreq(rq)



def dadosreq(rq):
    lista.append(rq['results']['temp'])
    lista.append(rq["results"]["date"])
    lista.append(rq["results"]["time"])
    lista.append(rq["results"]["description"])
    lista.append(rq["results"]["city"])
    mostrarterminal()
    


def mostrarterminal():
    print("=" * 30)
    print("PREVISÃO DO RIO DE JANEIRO")
    print("=" * 30)
    print("\n")
    print(f"Cidade: {lista[4]}")
    print(f"A data de hoje: {lista[1]}")
    print(f"Temperatura: {lista[0]}°")
    if lista[2] < "12:00":
        print(f"Horario: {lista[2]}AM")
    else:
        print(f"Horario: {lista[2]}PM")
    print(f"O clima está: {lista[3]}")




requisicao()

