# おまじない
import RPi.GPIO as GPIO
import time
import signal
import sys

###ir_send
import ir_send_control
#####################

# Ctrl+CによってSIGINTシグナルが送信された時のハンドラ。終了前にGPIO.cleanupを呼び出す
def handler(signum, frame):
  print('Signal handler called with signal', signum)
  GPIO.cleanup()
  sys.exit(0)

# ハンドラの登録
signal.signal(signal.SIGINT, handler)

# GPIO9を入力として利用
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN)
before = 0
flag = 0

# 無限ループ
while True:
  # 押された場合には1、押されていない場合0を返す
  now = GPIO.input(9)
  if before == 0 and now == 1:
    print("Push!!!")

###ir_send
    ir_send_control.send('tv/ch0.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch1.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch2.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch3.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch4.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch5.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch6.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch7.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch8.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch9.data', 1)
    time.sleep(3.0)
    ir_send_control.send('tv/ch10.data', 1)
    time.sleep(3.0)
#####################

  time.sleep(0.1)
  before = now