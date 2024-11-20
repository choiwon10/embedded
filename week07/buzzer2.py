# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

BUZZER = 12

# 주파수 매핑
notes = {
    'C': 262,    # 도
    'D': 294,    # 레
    'E': 330,    # 미
    'F': 349,    # 파
    'G': 392,    # 솔
    'A': 440,    # 라
    'B': 494,    # 시
    'C_high': 523 # 높은 도
}

# "비행기" 멜로디
melody = [
    'E', 'D', 'C', 'D', 'E', 'E', 'E', 'D', 'D', 'D', 
    'E', 'E', 'E', 'E', 'D', 'C', 'D', 'E', 'E', 'E',
    'D', 'D', 'E', 'D', 'C'  # 마지막 도는 저음으로
]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

p = GPIO.PWM(BUZZER, notes['C'])  # 기본 주파수를 도(C)로 설정
p.start(50)

try:
    for note in melody:
        if note in notes:
            p.ChangeFrequency(notes[note])  # 현재 음으로 주파수 변경
            time.sleep(0.5)  # 각 음을 0.5초 동안 연주
        time.sleep(0.05)  # 음 사이에 짧은 간격
    p.stop()

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
