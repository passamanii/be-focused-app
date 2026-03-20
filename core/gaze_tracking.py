# pyright: reportGeneralTypeIssues=false
# pyright: reportOptionalMemberAccess=false

import cv2
import time
import numpy as np
import mediapipe as mp
from .utils import resource_path
from .audio_manager import AudioManager
from .gaze_detector import GazeDetector
from .ui_components import draw_slider, draw_hud

"""
# 👁️ Gaze Tracker & Attention Monitor (V5 - SENSÍVEL)
Script principal refatorado e modularizado.
"""

# Configurações Globais
w, h = 640, 480
ui_config = {
    "volume": 80,
    "sensibilidade": 30,
    "atraso": 5.0,
    "dragging": None,
    "show_config": False,
    "sound_idx": 0
}

sound_info = [
    ("Alarme (Padrao)", "sounds/sound1.wav"),
    ("Chimes ()", "sounds/sound2.wav"),
    ("Chord ()", "sounds/sound3.wav"),
    ("Ding ()", "sounds/sound4.wav"),
    ("Sirene ()", "sounds/sound5.wav")
]

# Inicialização dos Gerenciadores (Globais para o callback)
audio = AudioManager(sound_info)
detector = GazeDetector()

def mouse_callback(event, x, y, flags, param):
    global ui_config, w, h
    if event == cv2.EVENT_LBUTTONDOWN:
        # Abrir/Fechar Configurações
        if (w-70) <= x <= (w) and 0 <= y <= 60:
            ui_config["show_config"] = not ui_config["show_config"]
            return
            
        if ui_config["show_config"]:
            # Seleção de Sons
            for i in range(len(audio.sounds)):
                btn_y_start = 210 + (i * 32)
                if (w-230) <= x <= (w-10) and btn_y_start <= y <= btn_y_start + 28:
                    audio.stop_all()
                    ui_config["sound_idx"] = i
                    audio.play(i, float(ui_config["volume"])/100.0)
                    return

    if ui_config["show_config"]:
        if event == cv2.EVENT_LBUTTONDOWN or (event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON):
            # Sliders
            if 85 <= y <= 115 and (w-220) <= x <= (w-20):
                ui_config["volume"] = int(((x - (w-220)) / 200) * 100)
            elif 125 <= y <= 155 and (w-220) <= x <= (w-20):
                ui_config["sensibilidade"] = int(((x - (w-220)) / 200) * 50)
            elif 165 <= y <= 195 and (w-220) <= x <= (w-20):
                ui_config["atraso"] = round(((x - (w-220)) / 200) * 10.0, 1)

def main():
    global w, h
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Attention Monitor v5', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
    cv2.setMouseCallback('Attention Monitor v5', mouse_callback)

    last_look = time.time()
    is_away = False

    while cap.isOpened():
        # Valores atuais das configs
        v = float(ui_config["volume"]) / 100.0
        s = float(ui_config["sensibilidade"]) / 100.0
        d = float(ui_config["atraso"])
        LIMIT_LOW, LIMIT_HIGH, AWAY_TIME = 0.5 - s, 0.5 + s, d

        success, frame = cap.read()
        if not success: break
        
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        overlay = frame.copy()
        
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        timestamp_ms = int(time.time() * 1000)
        
        # Detecção
        result = detector.detect(rgb_frame, timestamp_ms)
        
        away_now = False
        status, color = "FOCADO", (0, 255, 100)

        if result.face_landmarks:
            landmarks = result.face_landmarks[0]
            # Cálculo do Olhar (Gaze)
            nose, left, right = landmarks[1], landmarks[33], landmarks[263]
            prop = (nose.x - left.x) / (right.x - left.x)
            away_now = prop < LIMIT_LOW or prop > LIMIT_HIGH
            
            if away_now:
                time_away = time.time() - last_look if is_away else 0
                if time_away > AWAY_TIME:
                    audio.play(ui_config["sound_idx"], v)
                    status, color = f"DISTRAIDO! ({time_away:.1f}s)", (50, 50, 255)
                else: status, color = "ATENCAO...", (0, 180, 255)
            
            # Íris (Pontos 468 e 473)
            for idx in [468, 473]:
                lm = landmarks[idx]
                cv2.circle(frame, (int(lm.x*w), int(lm.y*h)), 4, (255, 255, 0), -1)
        else:
            away_now = True
            time_away = time.time() - last_look if is_away else 0
            if time_away > AWAY_TIME:
                audio.play(ui_config["sound_idx"], v)
                status, color = "ROSTO PERDIDO!", (50, 50, 255)
            else: status, color = "PROCURANDO...", (0, 180, 255)

        # Controle de Estado is_away
        if away_now:
            if not is_away: 
                is_away = True
                last_look = time.time()
        else:
            if is_away: 
                is_away = False
                audio.fadeout(ui_config["sound_idx"], 500)

        # Desenho da UI (HUD)
        draw_hud(frame, overlay, status, color, w, h, is_away, last_look, AWAY_TIME, ui_config["show_config"])
        if result.face_landmarks: 
            cv2.putText(frame, f"Gaze: {prop:.2f}", (w-200, 40), 0, 0.5, (200, 200, 200), 1)

        # Menu lateral de configurações
        if ui_config["show_config"]:
            cv2.rectangle(frame, (w-240, 60), (w, 380), (35, 35, 35), -1)
            draw_slider(frame, "Volume", ui_config["volume"], 90, 100, w, "%")
            draw_slider(frame, "Sensibilidade", ui_config["sensibilidade"], 130, 50, w)
            draw_slider(frame, "Atraso", ui_config["atraso"], 170, 10.0, w, "s")
            
            cv2.putText(frame, "ESCOLHA O ALERTA:", (w-225, 205), 0, 0.4, (150, 150, 150), 1)
            for i, (label, _) in enumerate(sound_info):
                btn_y = 210 + (i * 32)
                is_sel = (i == ui_config["sound_idx"])
                bg_col, txt_col = ((80, 80, 80), (255, 255, 255)) if not is_sel else (color, (0, 0, 0))
                cv2.rectangle(frame, (w-230, btn_y), (w-10, btn_y + 28), bg_col, -1)
                cv2.putText(frame, label, (w-220, btn_y + 20), 0, 0.4, txt_col, 1)

        cv2.imshow('Attention Monitor v5', frame)
        
        # Processa eventos e verifica teclado
        key = cv2.waitKey(1) & 0xFF
        if key == 27: # Tecla ESC
            break
            
        # Verifica se a janela foi fechada pelo botão "X"
        if cv2.getWindowProperty('Attention Monitor v5', cv2.WND_PROP_VISIBLE) < 1:
            break


    cap.release()
    cv2.destroyAllWindows()
    detector.close()

if __name__ == "__main__":
    main()
