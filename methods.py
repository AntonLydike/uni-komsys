def dec2bin(num):
    return bin(num)[2:]

def bin_ip(ip):
    return [ (('0' * 8) + dec2bin(int(x)))[-8:] for x in ip.split(".") ]

def gen_nm(l):
    nm=[]
    for no in range(4):
        nm.append(((min(max(0,l),8) * '1') + ("0" * 9))[0:8])
        l = l - 8
    return nm

