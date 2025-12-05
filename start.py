import webview
import sys
import threading
import traceback
def IPC():
    #sys.stdout.flush()
    while True:
        import time
        #time.sleep(3)
        try:
            res = sys.stdin.readline()
        except Exception as e:
            res = traceback.format_exc()
        if res:
            res = res.replace("\n", "")
            if res == "hide":
                window.hide()
            elif res == "show":
                window.show()
            elif res == "quit":
                window.destroy()
                sys.exit()

try:
    thread = threading.Thread(target=IPC)
    thread.start()
    window: webview.Window = webview.create_window('Hello world', 'http://localhost:3000/', on_top=True)
    def on_closed():
        window.hide()
        return False
    window.events.closing += on_closed

    webview.start()
except Exception as e:
    with open("E:/W_PV/Azure/TA/WebView/error.log", "w") as f:
        f.write(traceback.format_exc())