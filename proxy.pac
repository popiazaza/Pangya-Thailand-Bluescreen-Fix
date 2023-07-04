function FindProxyForURL(url, host) {
  if (shExpMatch(host, "mgr.gameguard.co.kr")) {
    return "PROXY localhost:8080";
  }
  return "DIRECT";
}
