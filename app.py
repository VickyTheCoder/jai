import webview, sys

def end(*args):
    sys.exit(1)

html = open(r"web\index.html", encoding="utf-8").read()
win = webview.create_window("Notify", html=html)
webview.start(end, win)