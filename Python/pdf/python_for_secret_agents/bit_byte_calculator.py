class Calculator:
    def __init__(self):
        pass

    def to_bits(self, v):
        #print("to_bits")
        b = []
        for i in range(8):
            # var i is unused.
            b.append(v&1)
            v >>= 1
            #print("v", v)
        return tuple(reversed(b))

    def to_byte(self, b):
        #print("to_byte")
        v = 0 
        for bit in b:
            #print("[before] v bit", v, bit)
            v = (v << 1) | bit
            #print("[after] v", v)
        return v
    
    def bit_sequence(self, list_of_tuples):
        for t8 in list_of_tuples:
            for b in t8:
                yield b

    def byte_sequence(self, bits):
        byte = []
        for n, b in enumerate(bits):
            if n % 8 == 0 and n != 0:
                yield self.to_byte(byte)
                byte = []
            byte.append(b)
        yield self.to_byte(byte)

if __name__ == "__main__":
    num = input("insert number:")
    calc = Calculator()
    bit_array = calc.to_bits(int(num))
    print("bit_array", bit_array)
    v = calc.to_byte(bit_array)
    assert int(num) == v
    
    # the arugment of bit_sequence function should be list of tuples.
    list_of_bits = list(calc.bit_sequence([bit_array]))
    print("bit_sequence", list_of_bits)
            
    list_of_bytes = list(calc.byte_sequence(list_of_bits))
    print("byte_sequence", list_of_bytes)



