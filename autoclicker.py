import pyautogui
import keyboard
import time

ativo = False

print("Iniciando em 3 segundos...")
print("Pressione z para ligar/desligar o autoclick.")
time.sleep(3)

def alternar():
    global ativo
    ativo = not ativo
    print(f"Autoclick {'LIGADO' if ativo else 'DESLIGADO'}")

keyboard.add_hotkey('z', alternar)

try:
    while True:
        if ativo:
            pyautogui.click()
            time.sleep(0.009)  # 9 ms entre os cliques
        else:
            time.sleep(0.01)   # evita consumir 100% da CPU
except KeyboardInterrupt:
    print("Script encerrado.")