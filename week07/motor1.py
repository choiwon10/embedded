import RPi.GPIO as GPIO
import time

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

# 각 모터에 대한 PWM 인스턴스를 별도로 생성
L_Motor = GPIO.PWM(PWMA, 500)
R_Motor = GPIO.PWM(PWMB, 500)
L_Motor.start(0)
R_Motor.start(0)

try:
    while True:
        # 왼쪽 모터 정방향 회전
        GPIO.output(AIN1, 0)
        GPIO.output(AIN2, 1)
        # 오른쪽 모터 정방향 회전
        GPIO.output(BIN1, 0)
        GPIO.output(BIN2, 1)
        
        # 양쪽 모터에 Duty Cycle을 적용
        # 50%의 속도를 내기 위해 듀티사이클 50
        L_Motor.ChangeDutyCycle(50)
        R_Motor.ChangeDutyCycle(50)
        time.sleep(0.1)  # 타임슬립을 0.1초로 설정

        # 양쪽 모터 정지
        L_Motor.ChangeDutyCycle(0)
        R_Motor.ChangeDutyCycle(0)
        time.sleep(0.1)  # 타임슬립을 0.1초로 설정

except KeyboardInterrupt:
    pass

GPIO.cleanup()
