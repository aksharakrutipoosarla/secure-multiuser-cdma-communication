# # import socket
# # import ast

# # udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # typing="Connection Established"
# # udp.sendto(typing.encode(),('Localhost',12345))

# # data , addr = udp.recvfrom(1024)
# # data_str = data.decode()
# # Signal = ast.literal_eval(data_str)
# # print("Received Signal:", Signal)

# # # def convertBitToSignal(arr):
# # #     for i in range(len(arr)):
# # #         if arr[i] == 0:
# # #             arr[i] = 1
# # #         else:
# # #             arr[i] = -1
# # #     return arr

# # # Signal = [-1, 3, 1, -1, -1, -1, 1, -1]

# # # c=list(map(int, input("Enter Chain Code : ").split()))
# # # c=convertBitToSignal(c)
# # # d= [0] * (len(Signal)//len(c))


# # socket and connection
import socket
import ast

udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
typing="Connection Established"
udp.sendto(typing.encode(),('10.113.9.157',12345))

data , addr = udp.recvfrom(1024)
data_str = data.decode()
Signal = ast.literal_eval(data_str)
print("Received Signal:", Signal)

# +1 and -1 ka pulse 

def pulse(bits):
    return [1 if b == 0 else -1 for b in bits]

# decoding in the receiver side 

#chcek the length of PN code and data
def decode(signal, bits):
    len_of_c = len(bits)
    sig = len(signal)

    sent_data_bits = sig // len_of_c
    rep = pulse(bits)

    D = [] #array to store


    #divide the signal into substrings for the addition initself (4 thing)
    for i in range(sent_data_bits):
        start = i*len_of_c
        divided_bits =signal[start : start+len_of_c]

        res = 0
        for k in range (len_of_c):
            res += divided_bits[k] * rep[k]
# if the result is +ve then 0 else 1 and add to array
        if res <=0:
            bit = 1
        else:
            bit =0

        D.append(bit)

    return D

c = list(map(int, input("Enter Chain Code : ").split()))

d = decode(Signal , c)

print(f"the d is {d}")





