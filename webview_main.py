from . import webview_manager, server_manager

def start_webview():
    process = webview_manager.manager.create_process()
    server_manager.manager.start_server()


def open_webview():
    webview_manager.manager.open_webview()
