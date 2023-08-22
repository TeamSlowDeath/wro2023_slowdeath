#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, InfraredSensor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
# Varibles definidas
ev3 = EV3Brick()
medium_motor = Motor(Port.A) #motor de la direccional definida como "medium_motor" 
big_motor = Motor(Port.B, Direction.CLOCKWISE) #motor del ejemotriz definida como "big_motor"
ultrasonic_sensor = UltrasonicSensor(Port.S1)  #sensorultrasonico definida como "ultrasonic_sensor"
infrared_sensor = InfraredSensor(Port.S2)      #sensorinfrarrojo definida como "infrared_sensor"
# encender Motor del ejemotriz
big_motor.run(500)

#estrategia utilizada
while True:
     ultrasonic_sensor.distance()
     infrared_sensor.distance()
     
     if ultrasonic_sensor.distance() < 50 and infrared_sensor.distance() < 70: #al cumplir las condiciones 
          medium_motor.track_target(25)                                        #el motor de la direccional girara los grados suficientes y se reincorporara realizando el objetivo corrctamentes 
          wait(1600)
          medium_motor.track_target(-4.3)
     elif ultrasonic_sensor.distance() < 50 and infrared_sensor.distance() > 70: 
           medium_motor.track_target(-25)
           wait(1600)
           medium_motor.track_target(4.3)