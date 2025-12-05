import subprocess
import unreal
import pathlib
import enum
import traceback



class WebViewState(enum.Enum):
    CREATED = 1
    NULL = 2

class WebViewManager:
    
    def __init__(self):
        self.port = 7900
        self.process = None
        self.__state = WebViewState.NULL

    def get_process(self):
        return self.process
    
    def __del__(self):
        if self.process and isinstance(self.process, subprocess.Popen):
            self.quit_webview()
            self.process.stdout.close()
            self.process.stdin.close()
            self.process.terminate()
    
    def create_process(self):
        try:
            if self.__state == WebViewState.CREATED:
                self.open_webview()
                return self.process
            python_executable = unreal.get_interpreter_executable_path()
            start_py = pathlib.Path(__file__).parent.joinpath("start.py").as_posix()
            command = [python_executable, start_py]
            self.process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            self.__state = WebViewState.CREATED
            self.hide_webview()
        except Exception as e:
            unreal.log_error(traceback.format_exc())
            self.__state = WebViewState.NULL
        return self.process

    def open_webview(self):
        process = self.get_process()
        if process and isinstance(process, subprocess.Popen):
            process.stdin.write(b"show\n")
            process.stdin.flush()
    
    def hide_webview(self):
        process = self.get_process()
        if process and isinstance(process, subprocess.Popen):
            process.stdin.write(b"hide\n")
            process.stdin.flush()

    def quit_webview(self):
        process = self.get_process()
        if process and isinstance(process, subprocess.Popen):
            process.stdin.write(b"quit\n")
            process.stdin.flush()
manager = WebViewManager()


            