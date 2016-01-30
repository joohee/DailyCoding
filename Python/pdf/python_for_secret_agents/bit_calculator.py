class Calculator:
    def __init__(self):
        pass

    def to_bits(self, v):
        print("to_bits")
        b = []
        for i in range(8):
            # var i is unused.
            b.append(v&1)
            v >>= 1
            print("v", v)
        return tuple(reversed(b))

    def to_byte(self, b):
        print("to_byte")
        v = 0 
        for bit in b:
            print("[before] v bit", v, bit)
            v = (v << 1) | bit
            print("[after] v", v)
        return v

if __name__ == "__main__":
    num = input("insert number:")
    calc = Calculator()
    bit_array = calc.to_bits(int(num))
    print(bit_array)
    v = calc.to_byte(bit_array)
    assert int(num) == v

