import time
import cv2
import threading
from flask import Flask, render_template, Response
import telebot
import cpuinfo
import os
import sys
import socket
from flask_apscheduler import APScheduler
from fasteners import InterProcessLock

app = Flask(__name__)

camera = cv2.VideoCapture(0)

# Замените на API вашего бота
bot_token = "6496654908:AAHdDK2ymX_1wB8e0jb37WHijxRKdiqKY88"
bot = telebot.TeleBot(bot_token)

# Замените на ваш tg id
user_ids = [1234567890]

lock = InterProcessLock("/tmp/my_app.lock")

if not lock.acquire(blocking=False):
    sys.exit("Приложение уже запущено")

for user_id in user_ids:
    bot.send_message(user_id, "Приложение запущено!")

ip_address = socket.gethostbyname(socket.gethostname())
stream_link = f"http://{ip_address}:2020/"

app_running = True


def generate_frames():
    global camera
    red_circle_on = False

    while app_running:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = cv2.putText(frame, time.strftime('%H:%M:%S'), (0, 27), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                (255, 255, 255), 2, cv2.LINE_AA)

            if red_circle_on:
                cv2.circle(frame, (frame.shape[1] - 25, 20), 15, (0, 0, 255), -1)
            red_circle_on = not red_circle_on

            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                break
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def cleanup():
    global app_running
    app_running = False


scheduler = APScheduler()


@scheduler.task('interval', id='check_app_running', seconds=10, misfire_grace_time=10)
def check_app_running():
    if not app_running:
        for user_id in user_ids:
            bot.send_message(user_id, "Приложение не запущено!")


if __name__ == '__main__':
    cpu_info = cpuinfo.get_cpu_info()
    cpu_name = cpu_info['brand_raw']

    for user_id in user_ids:
        bot.send_message(user_id, f"Камера включена! ПК: {cpu_name}")
        bot.send_message(user_id, f"Ссылка на видеопоток: {stream_link}")

    scheduler.start()

    app.run(host='0.0.0.0', port=2020)

    lock.release()
