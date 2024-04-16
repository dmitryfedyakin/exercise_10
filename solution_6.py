class RomanNumber:
    '''
    Class represents operations with roman and decimal numbers.

    Attributes:
        roman_nums (dict): A dictionary with roman numbers and 
        their decimal numbers'
    '''

    roman_nums = {'I': 1,
                 'IV' : 4,
                 'V': 5, 
                 'IX': 9,
                 'X': 10, 
                 'XL': 40,
                 'L': 50, 
                 'XC': 90,
                 'C': 100, 
                 'CD': 400,
                 'D': 500, 
                 'CM': 900,
                 'M': 1000}
    

    def __init__(self, value):
        '''
        Initializes a value.

        :param value: Roman or integer numeral.
        '''

        self.value = value
        if isinstance(value, str):
            if RomanNumber.is_roman(value):
                self.rom_value = value
                self.int_value = self.decimal_number()
            else:
                print("ошибка")
                self.int_value = None
                self.rom_value = None

        else:
            if isinstance(value, int):
                if RomanNumber.is_int(value):
                    self.int_value = value
                else:
                    print("ошибка")
                    self.int_value = None
                    self.rom_value = None

    def __add__(self, other):
        '''
        Summarize two numbers.

        :return: result of summarize
        '''

        result = self.int_value + other.int_value
        return self.roman_result(result)

    def __sub__(self, other):
        '''
        Difference between two numbers.

        :return: result of difference
        '''
                
        result = self.int_value - other.int_value
        return self.roman_result(result)
    
    def __mul__(self, other):
        '''
        Mulltiply two numbers.

        :return: result of multiplication
        '''
                
        result = self.int_value * other.int_value
        return self.roman_result(result)
    
    def __truediv__(self, other):
        '''
        Divide two numbers with remnant. 

        :return: result of division
        '''
                
        result = self.int_value / other.int_value
        return self.roman_result(result)
    
    def __floordiv__(self, other):
        '''
        Divide two numbers without remnant. 

        :return: result of division
        '''
                
        result = self.int_value // other.int_value
        return self.roman_result(result)
    
    def __pow__(self, other):
        '''
        Calculates numbers pow.

        :return: result of operation.
        '''
                
        result = self.int_value ** other.int_value
        return self.roman_result(result)
    
    def __mod__(self, other):
        '''
        Calculate remnant. 

        :return: result of operation
        '''
                
        result = self.int_value % other.int_value
        return self.roman_result(result)
    
    def roman_result(self, int_res):
        '''
        Represent result in Roman numerals.

        :return: Roman result
        '''
                
        roman_res = self.roman_number(int_res)
        if roman_res is None:
            return RomanNumber('ошибка')
        else:
            return RomanNumber(roman_res)

    @staticmethod
    def is_roman(value):
        '''
        Checks if a given string value is a valid Roman numeral.

        :param value: Number for checking.

        :return: Is number a Roman numeral or not.
        '''

        prev_value = 0
        same_count = 0

        if value in RomanNumber.roman_nums:
            return True

        for char in value:
            if char not in RomanNumber.roman_nums:
                return False
            
            curr_value = RomanNumber.roman_nums[char]

            if curr_value > prev_value:
                if same_count > 0:
                    return False
                if prev_value == 5 or prev_value == 50 or prev_value == 500:
                    return False
                same_count = 1
            elif curr_value == prev_value:
                same_count += 1
                if same_count > 3:
                    return False
                if prev_value == 5 or prev_value == 50 or prev_value == 500:
                    return False
            else:
                same_count = 0

            prev_value = curr_value

        return True

    def decimal_number(self):
        '''
        Converts the Roman numeral value to a decimal number.

        :return: Result of converting.
        '''
        
        if isinstance(self.rom_value, int):
            return self.rom_value
        if self.rom_value != None:
            result = 0
            prev = 0
            for num in reversed(self.rom_value):
                current = RomanNumber.roman_nums[num]
                if current >= prev:
                    result += current
                else:
                    result -= current
                prev = current
            
            return result 
        return None
        
    def is_int(value):
        '''
        Checks if a given string value is a valid integer numeral.

        :param value: Number for checking.

        :return: Is number an integer numeral or not.
        '''

        if isinstance(value, int) and value > 0 and value < 4000:
            return True
        return False

    def roman_number(self, value):
        '''
        Converts the decimal number value to a Roman numeral.

        :param value: Required number.

        :return: Roman numeral of decimal number.
        '''
                
        if int(value) != value:
            return None
        
        if value != None:
            roman = ''
            while value > 0:
                for i, r in reversed(RomanNumber.roman_nums.items()):
                    while value >= r:
                        roman += i
                        value -= r

            self.rom_value = roman
            return roman
        return None


    def __repr__(self):
        '''
        Return formal string representation of an object (for developers).      
        '''
        
        return 'None' if self.rom_value == None else self.rom_value
