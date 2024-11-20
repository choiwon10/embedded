import RPi.GPIO as GPIO
import time

# 스위치 핀 설정 (예시: SW1=GPIO5, SW2=GPIO6, SW3=GPIO13, SW4=GPIO19)
SW1, SW2, SW3, SW4 = 5, 6, 13, 19
switch_pins = [SW1, SW2, SW3, SW4]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(switch_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 풀다운 저항 설정

# 클릭 횟수 저장
click_counts = [0, 0, 0, 0]

# 스위치 눌림 상태 저장
previous_states = [0, 0, 0, 0]

try:
    while True:
        # 각 스위치 상태 확인
        for i, pin in enumerate(switch_pins):
            current_state = GPIO.input(pin)
            
            # 스위치가 눌림 상태로 변경될 때만 카운트 증가 및 출력
            if current_state == GPIO.HIGH and previous_states[i] == GPIO.LOW:
                click_counts[i] += 1
                print(f"('SW{i + 1} click', {click_counts[i]})")  # 괄호 포함 출력
            
            # 현재 상태를 이전 상태로 업데이트
            previous_states[i] = current_state
        
        time.sleep(0.1)  # CPU 사용률 절약을 위해 대기

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()