import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title ='Take break',
            masg = "Please! Take a rest of an hour",
            app_icon ='/Users/mini/Downloads',
            timeout=5)
        time.sleep(20)

