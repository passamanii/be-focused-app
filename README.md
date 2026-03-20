# 👁️ Be Focused App

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

O **Be Focused App** é uma ferramenta de monitoramento de atenção em tempo real que utiliza Inteligência Artificial para detectar o olhar do usuário e emitir alertas sonoros quando ele se distrai. Ideal para estudantes e profissionais que desejam manter o foco durante suas atividades no computador.

---

## ✨ Funcionalidades

-   **👀 Rastreamento de Olhar (Gaze Tracking):** Utiliza MediaPipe Face Landmarker para detectar com precisão para onde você está olhando.
-   **⚠️ Alertas de Distração:** Se você desviar o olhar por um tempo determinado (ex: 5 segundos), o app emite um alerta sonoro.
-   **🖥️ HUD Interativo:** Interface intuitiva que mostra seu estado atual (*FOCADO*, *ATENÇÃO...*, *DISTRAÍDO!*).
-   **⚙️ Menu de Configuração em Tempo Real:**
    -   Ajuste de **Volume** dos alertas.
    -   Ajuste de **Sensibilidade** da detecção.
    -   Ajuste de **Atraso (Delay)** para ativação do som.
    -   Seleção entre 5 tipos diferentes de sons de alerta.
-   **📦 Portabilidade:** Suporte para criação de executável único (`.exe`) para Windows.

---

## 🚀 Tecnologias Utilizadas

-   [Python 3.12+](https://www.python.org/)
-   [OpenCV](https://opencv.org/) para processamento de imagem e UI.
-   [MediaPipe](https://mediapipe.dev/) para detecção de landmarks faciais.
-   [Pygame](https://www.pygame.org/) para gerenciamento robusto de áudio.
-   [NumPy](https://numpy.org/) para cálculos matemáticos.
-   [uv](https://github.com/astral-sh/uv) para gerenciamento de dependências.

---

## 🛠️ Instalação e Execução

Este projeto utiliza o gerenciador de pacotes `uv` para maior velocidade e confiabilidade.

### Pré-requisitos
-   Webcam funcional.
-   Python 3.12 ou superior instalado.

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/passamanii/be-focused-app.git
    cd be-focused-app
    ```

2.  **Instale as dependências (usando uv):**
    ```bash
    uv sync
    ```

3.  **Execute o aplicativo:**
    ```bash
    uv run main.py
    ```

---

## 📖 Como Usar

1.  Ao iniciar, o aplicativo abrirá sua webcam.
2.  Mantenha seu rosto visível e olhe para a tela. O sistema marcará seus olhos e íris.
3.  **Configurações:**
    -   Clique no **ícone de engrenagem/canto superior direito** da janela para abrir o menu lateral.
    -   Arraste os sliders para ajustar Volume, Sensibilidade e Atraso.
    -   Clique nos botões de som para testar e selecionar seu alerta preferido.
4.  Pressione `ESC` ou feche a janela para sair.

---

## 🏗️ Criando o Executável (.exe)

Para gerar uma versão independente para Windows, utilize o PyInstaller via terminal:

```bash
uv run pyinstaller main.spec
```

O executável será gerado na pasta `dist/`.

---

## 📂 Estrutura do Projeto

```text
be-focused-app/
├── core/                # Lógica principal do sistema
│   ├── audio_manager.py # Gerenciamento de sons
│   ├── gaze_detector.py # Integração com MediaPipe
│   ├── gaze_tracking.py # Loop principal e lógica de negócio
│   ├── ui_components.py # Desenho do HUD e Sliders
│   └── utils.py         # Funções utilitárias (caminhos de arquivos)
├── models/              # Modelos de ML (face_landmarker.task)
├── sounds/              # Arquivos de áudio (.wav)
├── main.py              # Ponto de entrada
├── pyproject.toml       # Configurações do projeto e dependências
└── README.md            # Você está aqui!
```

---

## 📜 Licença

Este projeto está licenciado sob a **GNU General Public License v3.0**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Feito com ❤️ para ajudar você a manter o foco!
