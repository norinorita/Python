def flip_bit(number, n):
    mask = 0b1 << (n - 1)
    return bin(number ^ mask)
