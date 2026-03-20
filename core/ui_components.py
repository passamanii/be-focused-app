import cv2
import math
import time

def draw_slider(target_frame, label, val, y, max_val, w, unit=""):
    """ Desenha um slider interativo estilo HUD """
    x_start, x_end = w-220, w-20
    cv2.line(target_frame, (x_start, y+10), (x_end, y+10), (100, 100, 100), 2)
    knob_pos = x_start + int((val / max_val) * 200)
    cv2.circle(target_frame, (knob_pos, y+10), 8, (255, 255, 255), -1)
    cv2.putText(target_frame, f"{label}: {val}{unit}", (x_start, y-2), 0, 0.4, (255, 255, 255), 1)

def draw_hud(frame, overlay, status, color, w, h, is_away, last_look, away_time, show_config):
    """ Desenha a interface do HUD no topo e a barra de progresso """
    # Barra de topo escura
    cv2.rectangle(overlay, (0, 0), (w, 60), (20, 20, 20), -1)
    
    # Ícone de configuração (Engrenagem estilizada)
    btn_x, btn_y = w-45, 30
    btn_color = (180, 180, 180) if not show_config else color
    cv2.circle(overlay, (btn_x, btn_y), 15, (60, 60, 60), -1)
    cv2.circle(overlay, (btn_x, btn_y), 8, btn_color, 2)
    for i in range(8):
        angle = i * (45) * (math.pi/180)
        p1 = (int(btn_x + 8 * math.cos(angle)), int(btn_y + 8 * math.sin(angle)))
        p2 = (int(btn_x + 14 * math.cos(angle)), int(btn_y + 14 * math.sin(angle)))
        cv2.line(overlay, p1, p2, btn_color, 2)
    
    # Barra de progresso para distraído
    if is_away:
        prog = min((time.time() - last_look) / away_time, 1.0)
        cv2.rectangle(overlay, (0, 55), (int(prog * w), 60), color, -1)
    
    # Mezcla overlay com frame original
    cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
    
    # Texto de Status
    cv2.putText(frame, status, (20, 40), cv2.FONT_HERSHEY_DUPLEX, 1.0, color, 2)
