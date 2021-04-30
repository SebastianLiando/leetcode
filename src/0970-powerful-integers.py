from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        first = 1
        second = 1

        answers = set()

        # Store all powers of x less than bound
        first_multiples = []

        # Store all powers of y less than bound
        second_multiples = []
        
        # Find all powers of x less than bound
        if x == 1:
            first_multiples.append(1)
        else:
            while first < bound:
                first_multiples.append(first)
                first *= x
        
        # Find all powers of y less than bound
        if y == 1:
            second_multiples.append(1)
        else:
            while second < bound:
                second_multiples.append(second)
                second *= y
        
        # Add pairwise addition that is in bound
        for first_item in first_multiples:
            for second_item in second_multiples:
                if (first_item + second_item <= bound):
                    answers.add(first_item + second_item)
        
        return list(answers)
    
def calculate(x, y, bound) -> List[int]:
    return Solution().powerfulIntegers(x, y, bound)

def test_case_1():
    assert calculate(2, 3, 10) == [2, 3, 4, 5, 7, 9, 10]

def test_case_2():
    assert calculate(3, 5, 15) == [2,4,6,8,10,14]

def test_case_one():
    assert calculate(1, 1, 10) == [2]

def test_case_no_ans():
    assert calculate(3, 5, 1) == []

def test_case_max():
    assert calculate(2, 2, 10**6) == [512, 131073, 2, 3, 513, 5, 1025, 2049, 4097, 9, 8193, 16385, 32769, 262145, 10, 524289, 8, 17, 18, 131074, 20, 4, 16388, 32772, 65540, 16, 131076, 514, 262148, 524292, 24, 6, 32, 33, 34, 544, 36, 516, 1056, 2080, 40, 16392, 32776, 1026, 65544, 131080, 262152, 524296, 48, 1536, 524288, 1028, 49152, 524290, 520, 12, 64, 65, 66, 576, 68, 1088, 2112, 4160, 16386, 72, 1032, 2050, 8256, 264192, 65536, 270336, 80, 16400, 32784, 65552, 131088, 2052, 262160, 524304, 32770, 2560, 524800, 81920, 65537, 96, 528, 3072, 16896, 98304, 2056, 16384, 1040, 33280, 65538, 540672, 128, 129, 130, 640, 132, 1152, 2176, 4224, 136, 8320, 16512, 4098, 
32896, 65664, 131200, 4096, 144, 2064, 4608, 528384, 4100, 66048, 147456, 524416, 20480, 160, 5120, 16416, 32800, 65568, 131104, 262176, 524320, 1024, 4104, 525312, 36864, 163840, 655360, 17408, 192, 6144, 32768, 196608, 33792, 69632, 557056, 4112, 131584, 66560, 256, 257, 258, 768, 260, 1280, 2304, 4352, 264, 8448, 16640, 8194, 33024, 65792, 131328, 262400, 272, 524544, 8704, 8192, 532480, 8196, 278528, 24576, 288, 9216, 4128, 294912, 132096, 262144, 8200, 40960, 131072, 135168, 262146, 786432, 320, 10240, 16448, 32832, 65600, 131136, 262208, 524352, 2048, 526336, 327680, 73728, 8208, 262656, 18432, 34816, 589824, 384, 12288, 
393216, 67584, 266240, 139264, 262272, 8224, 263168, 133120]


    