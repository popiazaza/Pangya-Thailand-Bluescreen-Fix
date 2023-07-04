from mitmproxy import http, ctx
import subprocess
import atexit


class SetupProxy:
    def __init__(self):
        port = 8080
        if ctx.options.listen_port:
            port = ctx.options.listen_port
        print(f"Setting up proxy localhost:{port} ...")
        subprocess.Popen(["REG", "ADD", "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings", "/v", "AutoConfigURL",
                          "/t", "REG_SZ", "/d", f"http://localhost:{port}/proxy.pac", "/f"], shell=True)
        print("Proxy setup completed.")
        print("===== Pangya Thailand Bluescreen Fix =====")
        print("==========================================")
        print("=====     Press Ctrl+C to exit.      =====")
        print("==========================================")
        atexit.register(exit_handler)


def exit_handler():
    print("Removing proxy...")
    subprocess.Popen(["REG", "DELETE", "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings", "/v", "AutoConfigURL",
                      "/f"], shell=True)
    print("Proxy removed.")


class ServePACFile:
    def request(self, flow: http.HTTPFlow):
        if flow.request.path == "/proxy.pac":
            flow.response = http.Response.make(
                200, open("proxy.pac", "rb").read(),
            )


class FakeAntiCheatResponses:
    def __init__(self):
        self.skipped = 0

    def request(self, flow: http.HTTPFlow):
        if flow.request.path.startswith("/LogServer3/service.do?"):
            if self.skipped == 0:
                # Stop Driver Verification
                # non graceful close
                flow.response = http.Response.make(
                    418, b"I'm a teapot",
                )
                self.skipped = 1
            else:
                # Fake Anti Cheat Responses
                flow.request.path = flow.request.path + '09'


addons = [
    SetupProxy(),
    ServePACFile(),
    FakeAntiCheatResponses(),
]
