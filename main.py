import time
from plyer import notification
if "__name__"=="__main__":
    while True:
        notification.notify(
            title="Paani peele bhadwe",
            message="bhai baat maan paani peena bahut jaruri hota hai",
            app_icon="paanipeeloguys.png",
            timeout=5
        )
        time.sleep(60*60)