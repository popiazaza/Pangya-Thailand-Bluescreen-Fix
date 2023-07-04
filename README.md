# Pangya Thailand Bluescreen Fix

**This method is using Windows proxy setup script. Do NOT use if you are already using a proxy server.**

A [mitmproxy](https://mitmproxy.org/) addon to bypass GameGuard for Pangya, so that you can play Pangya on Windows 10/11.

Please do NOT use this addon to cheat. This addon is only for those who want to play Pangya on Windows 10/11. Thank you.

**I CANNOT guarantee this will not get your account banned. Use at your own risk.**

Although, this bypass doesn't modify the game client, it only modifies the request to GameGuard server. So, it should be safe to use.

> Alternatively, you can use virtual machine like [VirtualBox](https://www.virtualbox.org/) to play Pangya on Windows 10 version 1909 or older. Also, make sure to disable windows update on the virtual machine.

## How to use

1. Download the `Pangya Thailand Bluescreen Fix` latest release from this Github.
2. Install [mitmproxy](https://mitmproxy.org/).
3. Open `start.bat`.
4. Open `Pangya` (update.exe) as usual and enjoy.
5. Once you finished playing `Pangya`, press `Ctrl + C` to stop the proxy server and remove the proxy setup script.

> If `Pangya Thailand Bluescreen Fix` is not closed properly and it somehow cause you internet problem, you can remove the proxy setup script from Windows setting mannually.

## Why does running Pangya causing blue screen on Windows 10/11?

Since Windows 10 version 2004, Microsoft has tightened up the security of the kernel from the feature like System Guard. This prevent 3rd party application from reading and/or modifying the memory. However, GameGuard client is designed to read and/or modify the memory to detect any cheating software. So, when GameGuard client tries to read and/or modify the memory, it will cause a blue screen (CRITICAL_PROCESS_DIED).

As Pangya Thailand is no longer maintained, the GameGuard client is not updated to support Windows 10/11.

## How it works

This addon will create a local proxy server and use a proxy setup script (from `proxy.pac`) to redirect traffic that targets GameGuard server to the proxy server. The proxy server will then modify the request to crash the GameGuard client and return a fake response to the game client.

## License

MIT
