import RPi.GPIO as GPIO
import time

# 모터 핀 설정
PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

# 스위치 핀 설정
SW1, SW2, SW3, SW4 = 5, 6, 13, 19
switch_pins = [SW1, SW2, SW3, SW4]

# GPIO 설정
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(switch_pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # 풀다운 저항 설정

# 각 모터에 대한 PWM 인스턴스 생성
L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

try:
    while True:
        # 모터 상태 초기화
        L_Motor.ChangeDutyCycle(0)
        R_Motor.ChangeDutyCycle(0)

        # 각 스위치 상태 확인
        for i, pin in enumerate(switch_pins):
            current_state = GPIO.input(pin)

            # 스위치가 눌린 상태일 때 동작 수행
            if current_state == GPIO.HIGH:
                if i == 0:  # SW1: 앞
                    print("SW1 clicked: Move Forward")
                    GPIO.output(AIN1, 0)
                    GPIO.output(AIN2, 1)
                    GPIO.output(BIN1, 0)
                    GPIO.output(BIN2, 1)
                    L_Motor.ChangeDutyCycle(50)
                    R_Motor.ChangeDutyCycle(50)

                elif i == 1:  # SW2: 오른쪽
                    print("SW2 clicked: Turn Right")
                    GPIO.output(AIN1, 0)
                    GPIO.output(AIN2, 1)
                    GPIO.output(BIN1, 1)
                    GPIO.output(BIN2, 0)
                    L_Motor.ChangeDutyCycle(50)
                    R_Motor.ChangeDutyCycle(50)

                elif i == 2:  # SW3: 왼쪽
                    print("SW3 clicked: Turn Left")
                    GPIO.output(AIN1, 1)
                    GPIO.output(AIN2, 0)
                    GPIO.output(BIN1, 0)
                    GPIO.output(BIN2, 1)
                    L_Motor.ChangeDutyCycle(50)
                    R_Motor.ChangeDutyCycle(50)

                elif i == 3:  # SW4: 뒤
                    print("SW4 clicked: Move Backward")
                    GPIO.output(AIN1, 1)
                    GPIO.output(AIN2, 0)
                    GPIO.output(BIN1, 1)
                    GPIO.output(BIN2, 0)
                    L_Motor.ChangeDutyCycle(50)
                    R_Motor.ChangeDutyCycle(50)

        time.sleep(0.1)  # CPU 사용률 절약을 위해 대기

except KeyboardInterrupt:
    pass

finally:
    # 모든 핀 정리
    GPIO.cleanup()
