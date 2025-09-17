import pyautogui, mouseinfo, time
pyautogui.moveTo(1895,37, duration=1)
time.sleep(1)
pyautogui.moveTo(600,1059, duration=1)
pyautogui.click()
pyautogui.write("pye")
pyautogui.doubleClick()
from watchdog.observers import observer
from watch.events import filesystemeventhandler
import time

class meumonitor(filesystemeventhandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"pasta criada: {event.src_path}")

# caminho da pasta a ser monitorada
caminho = 'C:/users/prog2/documents/pyetra muniz turma 2'

observer = observer()
observer.schedule(meumonitor(), path=caminho, recusive=false)
observer.join()