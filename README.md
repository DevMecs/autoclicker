# ⚡ Python Auto Clicker (Toggle Bind)

Um script leve em Python de **Auto Clicker** com tecla de atalho global (`toggle bind`), desenvolvido para automatizar cliques repetitivos do rato com alta frequência e baixo consumo de processamento.

---

## 🎯 Por que criei?

Em tarefas repetitivas ou testes que exigem sequências rápidas de cliques, utilizar programas de terceiros cheios de anúncios e executáveis duvidosos é inconveniente. Desenvolvi este script limpo e direto: basta premir uma única tecla para ligar e a mesma tecla para desligar instantaneamente.

---

## 💡 Recursos

- **Atalho Global (`Z`):** Funciona em segundo plano, mesmo sem a janela do terminal em foco.
- **Alta Frequência:** Intervalo ajustável (padrão de ~9ms entre cliques).
- **Otimizado para CPU:** Pausa curta de ociosidade quando desligado, evitando consumo desnecessário do processador.
- **Fail-safe:** Interrupção limpa via terminal (`Ctrl + C`) ou pelo sistema nativo do PyAutoGUI.

---

## 🛠️ Tecnologias

- **Python 3.8+**
- [`pyautogui`](https://pyautogui.readthedocs.io/): controlo e envio dos cliques do rato.
- [`keyboard`](https://pypi.org/project/keyboard/): captura e escuta de teclas globais.
- Módulo nativo `time`.

---

## 🚀 Como usar

### 1. Clonar o repositório
```bash
git clone [https://github.com/DevMecs/autoclicker.git](https://github.com/DevMecs/autoclicker.git)
cd autoclicker
