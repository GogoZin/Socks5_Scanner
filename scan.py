import socket
import socks
import threading
import random
import time

# 設定掃描參數
THREAD_COUNT = 300
TIMEOUT = 1
SCAN_DURATION = 300  # 掃描秒數上限
RESULT_FILE = "socks5.txt"

# 儲存結果
open_socks5 = []
lock = threading.Lock()

# 避免掃到保留 IP 段
def generate_random_ip():
    while True:
        ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
        first = int(ip.split('.')[0])
        second = int(ip.split('.')[1])
        if first in [0, 6, 7, 10, 11, 21, 22, 26, 28, 29, 30, 33, 55, 127, 169, 192, 214, 215, 224, 255]:
            continue
        if first == 172 and 16 <= second <= 31:
            continue
        return ip

# 驗證 SOCKS5 協議是否有效
def is_socks5(ip, port=4145):
    try:
        s = socks.socksocket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.set_proxy(socks.SOCKS5, str(ip), int(port))
        s.settimeout(TIMEOUT)
        try:
            s.connect(("1.1.1.1", 80))
            print(f"[*] Connected {ip}")
            try:
                s.send(f"HEAD / HTTP/1.1\r\nHost: 1.1.1.1\r\n\r\n".encode('utf-8'))
                s.close()
                return True
            except:
                print(f"[!] Requests Failed {ip}")
                s.close()
                return False
        except:
            s.close()
            return False
    except:
        return False

# 執行掃描任務
def scan_loop(start_time):
    while time.time() - start_time < SCAN_DURATION:
        ip = generate_random_ip()
        if is_socks5(ip):
            with lock:
                open_socks5.append(ip)
                print(f"[+] Valid SOCKS5 Proxy Found: {ip}")

# 主程式
def main():
    threads = []
    start_time = time.time()

    print(f"[*] 開始掃描 port 4145（SOCKS5）... 將持續 {SCAN_DURATION} 秒")

    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=scan_loop, args=(start_time,))
        t.daemon = True
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\n[✓] 掃描結束，找到 {len(open_socks5)} 個 SOCKS5 代理")
    with open(RESULT_FILE, "a") as f:
        for ip in open_socks5:
            f.write(f"{ip}:4145\n")

    print(f"[✓] 已儲存至 {RESULT_FILE}")

if __name__ == "__main__":
    main()
