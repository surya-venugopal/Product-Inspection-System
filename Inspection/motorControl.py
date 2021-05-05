import RPi.GPIO as GPIO
from time import sleep


class ServoMotor:
    def __init__(self, pin):

        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)

        self.pwm = GPIO.PWM(pin, 50)

        self.pwm.start(0)

    def setAngle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()


class DCMotor:

    def __init__(self, MotorD, MotorE):

        self.MotorD = MotorD
        self.MotorE = MotorE
        GPIO.setup(MotorD, GPIO.OUT)
        GPIO.setup(MotorE, GPIO.OUT)

    def moveForward(self):
        GPIO.output(self.MotorD, GPIO.HIGH)
        GPIO.output(self.MotorE, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(self.MotorE, GPIO.LOW)

    def moveBackward(self):
        GPIO.output(self.MotorD, GPIO.LOW)
        GPIO.output(self.MotorE, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(self.MotorE, GPIO.LOW)


class ControlSystem:
    def __init__(self, fSignalPin, rSignalPin):
        self.fSignalPin = fSignalPin
        self.rSignalPin = rSignalPin
        self.servoCam = ServoMotor()

        self.dcBase = DCMotor()
        self.dcBaseControl = DCMotor()
        self.dcUpDown = DCMotor()
        self.dcLeftRight = DCMotor()

        self.camDegreeUpDown = 90
        self.camDegreeLeftRight = 90

    def start(self):
        while 1:
            inp = input()
            if(inp == "camUp"):
                if(self.camDegreeUpDown <= 120):
                    self.camDegreeUpDown += 30
                    self.servoCam.setAngle(self.camDegreeUpDown)
            elif(inp == "camDown"):
                if(self.camDegreeUpDown <= 60):
                    self.camDegreeUpDown -= 30
                    self.servoCam.setAngle(self.camDegreeUpDown)
            if(inp == "camRight"):
                if(self.camDegreeLeftRight <= 120):
                    self.camDegreeLeftRight += 30
                    self.servoCam.setAngle(self.camDegreeLeftRight)
            elif(inp == "camLeft"):
                if(self.camDegreeLeftRight <= 60):
                    self.camDegreeLeftRight -= 30
                    self.servoCam.setAngle(self.camDegreeLeftRight)

            elif(inp == "f"):                                                 # Move Forward
                if(GPIO.input(self.fSignalPin) == 1):
                    self.dcBase.moveForward()
                # elif(GPIO.input(self.rSignalPin) == 1):
                #     self.dcBaseControl.moveForward()
                else:
                    self.dcBaseControl.moveForward()

            elif(inp == "b"):                                               # Move Backward
                if(GPIO.input(self.fSignalPin) == 1):
                    self.dcBase.moveBackward()
                # elif(GPIO.input(self.rSignalPin) == 1):
                #     self.dcBaseControl.moveBackward()
                else:
                    self.dcBaseControl.moveBackward()

            elif(inp == "r"):                                               # Move Right
                if(GPIO.input(self.fSignalPin) == 1):
                    self.dcBaseControl.moveBackward()
                    # self.dcBase.moveForward()
                elif(GPIO.input(self.rSignalPin) == 1):
                    self.dcBase.moveForward()
                else:
                    self.dcBaseControl.moveBackward()

            elif(inp == "l"):                                               # Move Right
                if(GPIO.input(self.fSignalPin) == 1):
                    self.dcBaseControl.moveBackward()
                    # self.dcBase.moveForward()
                elif(GPIO.input(self.rSignalPin) == 1):
                    self.dcBase.moveBackward()
                else:
                    self.dcBaseControl.moveBackward()

            elif(inp == "up"):                                               # Move up
                self.dcUpDown.moveForward()

            elif(inp == "down"):                                               # Move down
                self.dcUpDown.moveBackward()

            elif(inp == "left"):                                               # Move left UP
                self.dcLeftRight.moveBackward()

            elif(inp == "right"):                                               # Move right UP
                self.dcLeftRight.moveForward()


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()


main()
