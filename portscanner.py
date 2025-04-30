import socket
import time

def scan_target(target, start_port=1, end_port=1024):
    print(f"Scanning {target} from port {start_port} to {end_port}")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Scan stopped by user.")
            break
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            break
        except socket.error:
            print("[!] Couldn't connect to server.")
            break

    end_time = time.time()
    print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")

# --- Run Scanner ---
if __name__ == "__main__":
    target = input("Enter target IP or domain: ")
    scan_target(target)
