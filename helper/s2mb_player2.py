from microbit import *
import radio


def loop():
    radio.config(group=1, length=64, queue=1)
    radio.on()

    while True:
        player, up, down, left, right, btn_a, btn_b, shaken = 2, False, False, False, False, False, False, False
        g = accelerometer.current_gesture()
        if g == 'up':
            up = True
        elif g == 'down':
            down = True
        elif g == 'left':
            left = True
        elif g == 'right':
            right = True
        elif g == 'shake':
            shaken = True

        if button_a.is_pressed():
            btn_a = True

        if button_b.is_pressed():
            btn_b = True

        sensor_string = ''
        sensor_string += str(player) + ','
        sensor_string += str(up) + ','
        sensor_string += str(down) + ','
        sensor_string += str(left) + ','
        sensor_string += str(right) + ','
        sensor_string += str(btn_a) + ','
        sensor_string += str(btn_b) + ','
        sensor_string += str(shaken)

        radio.send(sensor_string)

        sleep(8)

loop()
