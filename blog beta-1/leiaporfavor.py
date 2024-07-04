import time, sys


def print2(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)  # 25 milissegundos
    print()  # Adiciona uma nova linha ao final

print2("A barra do site não vai funcionar corretamente em todos os computadores")
print2("Há duas formas de resolver isso, ou você clica em cada html e abre eles pra ver cada parte do site")
print2("Ou você muda a url de cada link do arquivo js de cada pasta para o diretório do seu computador")