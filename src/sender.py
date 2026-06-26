import socket
import numpy as np

def read_bits(name):
    # Accept: "1 0 1 1" OR "1011" OR "1,0,1,1"
    s = input(f"Enter {name} bits (e.g. 1 0 1 1 OR 1011): ")
    s = s.replace(",", "").replace(" ", "")   # keep only 0/1 characters
    bits = [int(ch) for ch in s]              # each character is one BIT
    return np.array(bits, dtype=int)

# ---- main ----

data_bits = read_bits("DATA/CODE")
pn_bits   = read_bits("PN sequence (same length as data)")

print("DEBUG data_bits:", data_bits, "len =", len(data_bits))
print("DEBUG pn_bits  :", pn_bits,   "len =", len(pn_bits))

if len(data_bits) != len(pn_bits):
    raise ValueError("Data and PN must have the SAME length")

encoded_bits = np.bitwise_xor(data_bits, pn_bits)

print("Data bits   :", data_bits)
print("PN bits     :", pn_bits)
print("Encoded bits:", encoded_bits)

UDP_IP   = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg_str = "".join(str(b) for b in encoded_bits)
packet = f"{len(encoded_bits)}:{msg_str}"

sock.sendto(packet.encode(), (UDP_IP, UDP_PORT))
print(f"Sent {len(encoded_bits)} encoded bits to {UDP_IP}:{UDP_PORT}")

sock.close()
