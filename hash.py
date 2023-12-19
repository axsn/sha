import binascii
import time

text = "aaaaa"

start_time = time.perf_counter()

binary_data = text.encode('utf-8')
integer_value = int.from_bytes(binary_data, byteorder='big')
binary_string = bin(integer_value)

a = f"0{binary_string[2:]}"
bits = 512-1-len(a)-64


len_message = len(text)*8
textle = format(len_message, 'b')
llennn = len(textle)
texta = a +"1"+"0"*(bits+64-llennn)+str(textle)
result_list = [texta[i:i+32] for i in range(0, len(texta), 32)]
"""
 Message block 

"""
w = result_list

def rotate_right(binary_string, n):
    integer_value = int(binary_string, 2)
    rotated_value = (integer_value >> n) | (integer_value << (len(binary_string) - n)) & ((1 << len(binary_string)) - 1)
    result = bin(rotated_value)[2:].zfill(len(binary_string))
    return result

def shift_right(binary_string, n):
    integer_value = int(binary_string, 2)
    shifted_value = integer_value >> n
    result = bin(shifted_value)[2:].zfill(len(binary_string))
    return result



def xor_binary_strings(str1, str2,str3):
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    int3 = int(str3, 2)
    
    result_int = int1 ^ int2^ int3
    result_str = bin(result_int)[2:].zfill(max(len(str1), len(str2), len(str3)))
    return result_str

def binary_addition(str1, str2, str3, str4):
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    int3 = int(str3, 2)
    int4 = int(str4, 2)
    sum_int = int1 + int2 + int3 + int4
    result_str = bin(sum_int & ((1 << 32) - 1))[2:].zfill(32)
    return result_str

def binary_addition2(str1, str2, str3, str4,str5):
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    int3 = int(str3, 2)
    int4 = int(str4, 2)
    int5 = int(str5, 2)
    sum_int = int1 + int2 + int3 + int4 + int5
    result_str = bin(sum_int & ((1 << 32) - 1))[2:].zfill(32)
    return result_str

def binary_addition3(str1, str2):
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    sum_int = int1 + int2
    result_str = bin(sum_int & ((1 << 32) - 1))[2:].zfill(32)
    return result_str

for counter in range(48):
    a0 = xor_binary_strings(rotate_right(w[counter+1], 18), rotate_right(w[counter+1], 7),shift_right(w[counter+1], 3))
    a1 = xor_binary_strings(rotate_right(w[counter+14], 17), rotate_right(w[counter+14],19),shift_right(w[counter+14], 10))
    re = binary_addition(a0,a1,w[counter],w[counter+9])
    w.append(re)


k = [
    "01000010100010100010111110011000",
    "01110001001101110100010010010001",
    "10110101110000001111101111001111",
    "11101001101101011101101110100101",
    "00111001010101101100001001011011",
    "01011001111100010001000111110001",
    "10010010001111111000001010100100",
    "10101011000111000101111011010101",
    "11011000000001111010101010011000",
    "00010010100000110101101100000001",
    "00100100001100011000010110111110",
    "01010101000011000111110111000011",
    "01110010101111100101110101110100",
    "10000000110111101011000111111110",
    "10011011110111000000011010100111",
    "11000001100110111111000101110100",
    "11100100100110110110100111000001",
    "11101111101111100100011110000110",
    "00001111110000011001110111000110",
    "00100100000011001010000111001100",
    "00101101111010010010110001101111",
    "01001010011101001000010010101010",
    "01011100101100001010100111011100",
    "01110110111110011000100011011010",
    "10011000001111100101000101010010",
    "10101000001100011100011001101101",
    "10110000000000110010011111001000",
    "10111111010110010111111111000111",
    "11000110111000000000101111110011",
    "11010101101001111001000101000111",
    "00000110110010100110001101010001",
    "00010100001010010010100101100111",
    "00100111101101110000101010000101",
    "00101110000110110010000100111000",
    "01001101001011000110110111111100",
    "01010011001110000000110100010011",
    "01100101000010100111001101010100",
    "01110110011010100000101010111011",
    "10000001110000101100100100101110",
    "10010010011100100010110010000101",
    "10100010101111111110100010100001",
    "10101000000110100110011001001011",
    "11000010010010111000101101110000",
    "11000111011011000101000110100011",
    "11010001100100101110100000011001",
    "11010110100110010000011000100100",
    "11110100000011100011010110000101",
    "00010000011010101010000001110000",
    "00011001101001001100000100010110",
    "00011110001101110110110000001000",
    "00100111010010000111011101001100",
    "00110100101100001011110010110101",
    "00111001000111000000110010110011",
    "01001110110110001010101001001010",
    "01011011100111001100101001001111",
    "01101000001011100110111111110011",
    "01110100100011111000001011101110",
    "01111000101001010110001101101111",
    "10000100110010000111100000010100",
    "10001100110001110000001000001000",
    "10010000101111101111111111111010",
    "10100100010100000110110011101011",
    "10111110111110011010001111110111",
    "11000110011100010111100011110010"
]

a = "01101010000010011110011001100111"
b = "10111011011001111010111010000101"
c = "00111100011011101111001101110010"
d = "10100101010011111111010100111010"
e = "01010001000011100101001001111111"
f = "10011011000001010110100010001100"
g = "00011111100000111101100110101011"
h = "01011011111000001100110100011001"

h0,h1,h2,h3,h4,h5,h6,h7 = a,b,c,d,e,f,g,h

def and_binary_strings(str1, str2):
    int1 = int(str1, 2)
    int2 = int(str2, 2)
    result_and = int1 & int2
    result_str = bin(result_and)[2:].zfill(max(len(str1), len(str2)))
    return result_str
def binary_choice(e, f, g):
    e_int = int(e, 2)
    f_int = int(f, 2)
    g_int = int(g, 2)
    result_int = (e_int & f_int) ^ ((~e_int) & g_int)
    result_str = bin(result_int)[2:].zfill(max(len(e), len(f), len(g)))
    return result_str
for counter in range(64):
    sg1 = xor_binary_strings(rotate_right(e,6),rotate_right(e,11),rotate_right(e,25))
    choice = binary_choice(e,f,g)
    temp1 = binary_addition2(h,sg1,choice,k[counter],w[counter])
    sg0 = xor_binary_strings(rotate_right(a,2),rotate_right(a,13),rotate_right(a,22))
    majority = xor_binary_strings(and_binary_strings(a,b),and_binary_strings(a,c),and_binary_strings(b,c))
    temp2 = binary_addition3(majority,sg0)
    h = g
    g = f
    f = e
    e = binary_addition3(d,temp1)
    d = c
    c = b
    b = a
    a = binary_addition3(temp1,temp2)

h0 = binary_addition3(a,h0)
h1 = binary_addition3(b,h1)
h2 = binary_addition3(c,h2)
h3 = binary_addition3(d,h3)
h4 = binary_addition3(e,h4)
h5 = binary_addition3(f,h5)
h6 = binary_addition3(g,h6)
h7 = binary_addition3(h,h7)

res = h0 + h1 + h2 +h3 + h4 + h5 + h6 + h7
hex_string = hex(int(res, 2))[2:]
byte_data = binascii.unhexlify(hex_string)
result_hex = binascii.hexlify(byte_data).decode('utf-8')

end_time = time.perf_counter()

es_time = end_time-start_time

print(f"計測時間{es_time:.20f}\n{result_hex}")

