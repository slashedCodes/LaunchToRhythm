import sys
import time
import threading
import json
from pynput.keyboard import Key, Controller

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad #what the fuck bro
	except ImportError:
		sys.exit("error loading launchpad.py") #no why a try catch

config = open("config.json") #Open the config file
configLoaded = json.load(config) #Load the config

def main():
	mode = None

	if launchpad.LaunchpadPro().Check( 0 ):
		lp = launchpad.LaunchpadPro()
		if lp.Open( 0 ):
			print("Launchpad Pro Connected! (Side effects aren't supported yet)")
			mode = "Pro"

	elif launchpad.LaunchpadProMk3().Check( 0 ):
		lp = launchpad.LaunchpadProMk3()
		if lp.Open( 0 ):
			print("Launchpad Pro Mk3 Connected!")
			mode = "ProMk3"

	elif launchpad.LaunchpadMiniMk3().Check( 1 ):
		lp = launchpad.LaunchpadMiniMk3()
		if lp.Open( 1 ):
			print("Launchpad Mini Mk3 Connected!")
			mode = "MiniMk3"

	elif launchpad.LaunchpadLPX().Check( 1 ):
		lp = launchpad.LaunchpadLPX()
		if lp.Open( 1 ):
			print("Launchpad X Connected!")
			mode = "LPX"

	elif launchpad.LaunchpadMk2().Check( 0 ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0 ):
			print("Launchpad Mk2 Connected!")
			mode = "Mk2"


	if mode is None:
		print("Did not find any Launchpads!")
		return

	def effect1():
    	# Buttons to light up in the first effect
		effect1array = [
			[8, 8],
			[8, 7],
			[8, 6],
			[8, 5],
			[8, 4],
			[8, 3],
			[8, 2],
			[8, 1],
			[7, 0],
			[6, 0],
			[5, 0],
			[4, 0],
			[3, 0],
			[2, 0],
			[1, 0]
		]
	 
		while True:
			for i in effect1array:
				lp.LedCtrlXYByCode(i[0], i[1], configLoaded["effect1color"])
				time.sleep(configLoaded["effect1speed"])
				lp.LedCtrlXYByCode(i[0], i[1], 0)


	def effect2():
		# Buttons to light up in the second effect
		effect2array = [
			[0, 7],
			[1, 7],
			[2, 7],
			[2, 8],
			[7, 7],
			[6, 7],
			[5, 7],
			[5, 8]
		]
  
		while True:
			for i in effect2array:
				lp.LedCtrlXYByCode(i[0], i[1], configLoaded["effect2colors"][1])
				time.sleep(configLoaded["effect2speed"])
				lp.LedCtrlXYByCode(i[0], i[1], configLoaded["effect2colors"][0])
	
	if configLoaded["effect1enabled"]:
		threading.Thread(target=effect1).start() #Start effect 1 in background.
	if configLoaded["effect2enabled"]:
		threading.Thread(target=effect2).start() #Start effect 2 in background.

	lp.LedCtrlXYByCode(0, 0, 5) #Set exit button color

	while True:
		if mode == 'Pro' or mode == 'ProMk3':
			buts = lp.ButtonStateXY( mode = 'pro')
		else:
			buts = lp.ButtonStateXY()
   
		keyboard = Controller()
		if buts != []:
			for i, val in enumerate(configLoaded["buttons"]):
				if buts[0] == val[0] and buts[1] == val[1]:
					if buts[2] >= 1:
						keyboard.press(configLoaded["keys"][i])
						lp.LedCtrlXYByCode(val[0], val[1], configLoaded["pressColor"])
					elif buts[2] == 0:
						keyboard.release(configLoaded["keys"][i])
						lp.LedCtrlXYByCode(val[0], val[1], 0)
			if buts[0] == 0 and buts[1] == 0 and buts[2] == 127:
				lp.Reset() # turn all LEDs off
				lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

if __name__ == '__main__':
	main()

