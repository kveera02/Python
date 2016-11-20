# main.py -- put your code here!
import pyb

LEDS = (pyb.LED(1) , pyb.LED(2) , pyb.LED(3) , pyb.LED(4))
sw = pyb.Switch()
acc = pyb.Accel()
intensity = 0

def main():
	while True:
		lst = acceler()
		pwmIn(lst)
		lightCtrl(lst)
		if sw():
			for i in LEDS:
				i.off()
			break;
		'''
		for i in range(1 , 20):
			tim1 = pyb.Timer(1 , freq = i)
			print(i)
			pyb.delay(1000)
'''
		
def acceler():
	x = acc.x()
	y = acc.y()
	z = acc.z()
	x += 32
	y += 32
	z += 32
	lst = [x , y , z]
	print(x , y , z)
	return lst
	
def pwmIn(lst):
	led = LEDS[3]
	intensity = (lst[0]*4)
	# print(intensity)
	led.intensity(intensity)
	# pyb.delay(10)
	
def lightCtrl(lst):
	L1 = LEDS[0]
	L2 = LEDS[1]
	L3 = LEDS[2]
	freq1 = int(lst[1]/6)+1
	freq2 = int(lst[2]/6)+1
	print(freq1 , freq2)
	tim1 = pyb.Timer(1 , freq = freq1)
	tim1.callback(lambda t: L2.toggle())
	pyb.delay(200)
	tim2 = pyb.Timer(2 , freq = freq2)
	tim2.callback(lambda t: L3.toggle())
	pyb.delay(200)
	
main()