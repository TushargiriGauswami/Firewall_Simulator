import random
import time
from collections import defaultdict

# Try importing scapy safely
try:
    from scapy.all import sniff, IP, TCP, Ether, sendp
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

THRESHOLD = 40


# =========================
# MODE 1: FIREWALL SIMULATOR
# =========================
def firewall_simulator():
    print("\n--- Firewall Simulator ---\n")

    blocked_ips = {
        "192.168.1.1",
        "192.168.1.4",
        "192.168.1.9",
        "192.168.1.13",
        "192.168.1.16",
        "192.168.1.19"
    }

    for _ in range(12):
        ip = f"192.168.1.{random.randint(0, 20)}"
        action = "BLOCK" if ip in blocked_ips else "ALLOW"
        token = random.randint(1000, 9999)
        print(f"IP: {ip} | Action: {action} | Token: {token}")


# =========================
# MODE 2: DOS BLOCKER (SIMULATED)
# =========================
def dos_blocker():
    print("\n--- DoS Blocker (Simulation Mode) ---")

    packet_count = defaultdict(int)
    start_time = time.time()

    # Simulated incoming packets
    for _ in range(100):
        fake_ip = f"192.168.1.{random.randint(1, 10)}"
        packet_count[fake_ip] += 1

        elapsed = time.time() - start_time
        if elapsed >= 1:
            for ip, count in packet_count.items():
                if count > THRESHOLD:
                    print(f"[ALERT] DoS detected from {ip} | Packets: {count}")
            packet_count.clear()
            start_time = time.time()


# =========================
# MODE 3: DOS ATTACK TESTER (SIMULATED)
# =========================
def dos_tester():
    print("\n--- DoS Packet Sender (Simulation) ---")

    target_ip = input("Enter target IP: ")

    for i in range(10):
        print(f"Sending packet {i+1} to {target_ip}")
        time.sleep(0.2)

    print("Attack simulation completed.")


# =========================
# MODE 4: ADVANCED FIREWALL + NIMDA (SIMULATED)
# =========================
def advanced_firewall():
    print("\n--- Advanced Firewall + Nimda Detection (Simulation) ---")

    blacklist = {"192.168.1.5", "192.168.1.8"}
    whitelist = {"192.168.1.2"}

    simulated_packets = [
        {"ip": "192.168.1.5", "payload": ""},
        {"ip": "192.168.1.7", "payload": "GET /scripts/root.exe"},
        {"ip": "192.168.1.3", "payload": ""},
    ]

    for pkt in simulated_packets:
        ip = pkt["ip"]
        payload = pkt["payload"]

        if ip in whitelist:
            print(f"Whitelisted IP allowed: {ip}")
            continue

        if ip in blacklist:
            print(f"Blocked blacklisted IP: {ip}")
            continue

        if "GET /scripts/root.exe" in payload:
            print(f"Nimda worm detected from IP: {ip}")
            continue

        print(f"Normal traffic from IP: {ip}")


# =========================
# MAIN MENU
# =========================
def main():
    print("""
==============================
 Cybersecurity Toolkit
==============================
1. Firewall Simulator
2. DoS Blocker
3. DoS Attack Tester
4. Advanced Firewall + Nimda
==============================
""")

    choice = input("Select mode (1-4): ")

    if choice == "1":
        firewall_simulator()
    elif choice == "2":
        dos_blocker()
    elif choice == "3":
        dos_tester()
    elif choice == "4":
        advanced_firewall()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()