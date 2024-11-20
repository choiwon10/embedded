# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 스위치 핀 설정
SW1, SW2, SW3, SW4 = 5, 6, 13, 19
switch_pins = [SW1, SW2, SW3, SW4]

# 버저 핀 설정
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

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(switch_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 풀다운 저항 설정

p = GPIO.PWM(BUZZER, notes['C'])  # 기본 주파수를 도(C)로 설정
p.start(0)

try:
    while True:
        sound_playing = False  # 소리 상태 초기화
        for i, pin in enumerate(switch_pins):
            current_state = GPIO.input(pin)
            if current_state == GPIO.HIGH:
                # 각 스위치에 음 할당
                if i == 0:  # SW1: 도
                    print("Playing C")
                    p.ChangeFrequency(notes['C'])
                    p.ChangeDutyCycle(50)
                    sound_playing = True  # 소리 상태 업데이트
                elif i == 1:  # SW2: 레
                    print("Playing D")
                    p.ChangeFrequency(notes['D'])
                    p.ChangeDutyCycle(50)
                    sound_playing = True
                elif i == 2:  # SW3: 미
                    print("Playing E")
                    p.ChangeFrequency(notes['E'])
                    p.ChangeDutyCycle(50)
                    sound_playing = True
                elif i == 3:  # SW4: 높은 도
                    print("Playing C_high")
                    p.ChangeFrequency(notes['C_high'])
                    p.ChangeDutyCycle(50)
                    sound_playing = True

        if not sound_playing:
            p.ChangeDutyCycle(0)  # 소리 정지

        time.sleep(0.1)  # CPU 사용률 절약을 위해 대기

except KeyboardInterrupt:
    pass

finally:
    p.stop()
    GPIO.cleanup()
