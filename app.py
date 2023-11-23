import rumps
import pyautogui
import threading

class CircleCursor(rumps.App):
    def __init__(self):
        super(CircleCursor, self).__init__("Circle Cursor", icon="cursor.png")
        self.menu.add(rumps.MenuItem("Start", callback=self.start_circle_cursor))
        self.timer = None  # timer başlatmak/kapatmak için değişken

    def start_circle_cursor(self, sender):
        if self.timer is None:
            self.start_circle()  # ilki manuel olarak başlatın
            sender.title = "Stop"  # menü öğesi metnini değiştirin
        else:
            self.stop_circle_cursor(sender)

    def stop_circle_cursor(self, sender):
        if self.timer is not None:
            self.timer.cancel()  # zamanlayıcıyı durdurun
            self.timer = None
            sender.title = "Start"  # menü öğesi metnini değiştirin

    def start_circle(self):
        pyautogui.moveRel(100, 0, duration=1)  # 100 piksel sağa hareket
        pyautogui.moveRel(0, 100, duration=1)  # 100 piksel aşağı hareket
        pyautogui.moveRel(-100, 0, duration=1)  # 100 piksel sola hareket
        pyautogui.moveRel(0, -100, duration=1)  # 100 piksel yukarı hareket
        self.timer = threading.Timer(15, self.start_circle)  # 15 saniye sonra yeniden başlat
        self.timer.start()  # zamanlayıcıyı başlatın

if __name__ == "__main__":
    CircleCursor().run()