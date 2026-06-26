import socket
import numpy as np

def read_bits(name):
    s = input(f"Enter {name} bits (e.g. 1 0 1 1 OR 1011): ")
    bits = [int(ch) for ch in s]              
    return np.array(bits, dtype=int)

UDP_IP   = "0.0.0.0" 
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Receiver listening on port {UDP_PORT}...")

data, addr = sock.recvfrom(4096)
packet = data.decode()
print(f"Got packet from {addr}: {packet}")

try:
    length_str, bit_str = packet.split(":")
except ValueError:
    print("Error: packet format invalid (expected '<len>:<bits>')")
    sock.close()
    raise SystemExit

length = int(length_str)

if len(bit_str) != length:
    print(f"Warning: length mismatch (header {length}, actual {len(bit_str)}) but continuing...")

encoded_bits = np.array([int(ch) for ch in bit_str], dtype=int)
print("Encoded bits received:", encoded_bits, "len =", len(encoded_bits))

pn_bits = read_bits(f"PN sequence (same as sender used, length {len(encoded_bits)}): ")
print("DEBUG pn_bits:", pn_bits, "len =", len(pn_bits))

if len(pn_bits) != len(encoded_bits):
    raise ValueError("PN length must match received encoded length")

# XOR
decoded_bits = np.bitwise_xor(encoded_bits, pn_bits)

print("PN bits     :", pn_bits)
print("Decoded bits:", decoded_bits)

sock.close()
