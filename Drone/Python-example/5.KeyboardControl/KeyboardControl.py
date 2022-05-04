from djitellopy import tello

import KeyPressModule as kp

import cv2

from time import sleep

kp.init()

me = tello.Tello()
me.streamon()
me.connect()

print(me.get_battery())

def getKeyboardInput():

    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 90

    if kp.getKey("LEFT"): lr = -speed

    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed

    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"):ud = speed

    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"):yv = -speed

    elif kp.getKey("d"): yv = speed

    if kp.getKey("q"): me.land(); sleep(2)

    if kp.getKey("e"): me.takeoff()

    if kp.getKey("f"): me.flip_right()

    if kp.getKey("g"): me.flip_forward()

    return [lr, fb, ud, yv]


while True:

    vals = getKeyboardInput()
    
    img = me.get_frame_read().frame
    img = cv2.resize(img, (800, 600))
    cv2.imshow("Image", img)

    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)