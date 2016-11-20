import pyb

onBoardLEDs = pyb.LED(1)
#to use: .on() , .off() , .toggle()

onBoardSwitch = pyb.Switch()
#onBoardSwitch.callback(function) uses interrupt to execute function

pyb.delay(ms)

# ACCELEROMETER
accel = pyb.accel()
x = accel.x()
y = accel.y()
z = accel.z()
#all three returns signed int from {-30 , 30}

#Timer-- there are 14 independent timers-- 3 is internal, 5/6 is for servos/ADC/DAC
tim = pyb.Timer(timer)
tim.init(freq=10)
tim.counter()
tim.callback(lambda t: thing to control)

# pin control
from pyb import Pin

p_out = Pin('X1', Pin.OUT_PP)
p_out.high()
p_out.low()

p_in = Pin('X2', Pin.IN, Pin.PULL_UP)
p_in.value() # get value, 0 or 1

# pin PWM control
from pyb import Pin, Timer

p = Pin('X1') # X1 has TIM2, CH1
tim = Timer(2, freq=1000)
ch = tim.channel(1, Timer.PWM, pin=p)
ch.pulse_width_percent(50)

# servo control
from pyb import Servo

s1 = Servo(1) # servo on position 1 (X1, VIN, GND)
s1.angle(45) # move to 45 degrees
s1.angle(-60, 1500) # move to -60 degrees in 1500ms
s1.speed(50) # for continuous rotation servos

# ADC/DAC
from pyb import Pin, ADC

adc = ADC(Pin('X19'))
adc.read() # read value, 0-4095

from pyb import Pin, DAC

dac = DAC(Pin('X5'))
dac.write(120) # output between 0 and 255

# SPI
from pyb import SPI

spi = SPI(1, SPI.MASTER, baudrate=200000, polarity=1, phase=0)
spi.send('hello')
spi.recv(5) # receive 5 bytes on the bus
spi.send_recv('hello') # send a receive 5 bytes

# I2C
from pyb import I2C

i2c = I2C(1, I2C.MASTER, baudrate=100000)
i2c.scan() # returns list of slave addresses
i2c.send('hello', 0x42) # send 5 bytes to slave with address 0x42
i2c.recv(5, 0x42) # receive 5 bytes from slave
i2c.mem_read(2, 0x42, 0x10) # read 2 bytes from slave 0x42, slave memory 0x10
i2c.mem_write('xy', 0x42, 0x10) # write 2 bytes to slave 0x42, slave memory 0x10

'''
To enter safe mode, do the following steps:

    Connect the pyboard to USB so it powers up.
    Hold down the USR switch.
    While still holding down USR, press and release the RST switch.
    The LEDs will then cycle green to orange to green+orange and back again.
    Keep holding down USR until only the orange LED is lit, and then let go of the USR switch.
    The orange LED should flash quickly 4 times, and then turn off.
    You are now in safe mode.

	
	
To do a factory reset of the filesystem you follow a similar procedure as you did to enter safe mode, but release USR on green+orange:

    Connect the pyboard to USB so it powers up.
    Hold down the USR switch.
    While still holding down USR, press and release the RST switch.
    The LEDs will then cycle green to orange to green+orange and back again.
    Keep holding down USR until both the green and orange LEDs are lit, and then let go of the USR switch.
    The green and orange LEDs should flash quickly 4 times.
    The red LED will turn on (so red, green and orange are now on).
    The pyboard is now resetting the filesystem (this takes a few seconds).
    The LEDs all turn off.
    You now have a reset filesystem, and are in safe mode.
    Press and release the RST switch to boot normally.

'''