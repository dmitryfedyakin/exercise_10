class RomanNumber:
    '''
    Class represents operations with roman and decimal numbers.

    Attributes:
        roman_nums (dict): A dictionary with roman numbers and 
        their decimal numbers'
    '''

    roman_nums = {'I': 1,
                 'IV': 4,
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

    def __init__(self, rom_value):
        '''
        Initializes a RomanNumber object with the given value.

        :param rom_value: Roman numeral.
        '''
    
        if RomanNumber.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            self.rom_value = None
            print('ошибка')

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
        else:
            return None
        
    def __repr__(self):
        '''
        Return formal string representation of an object (for developers).
        '''

        return 'None' if self.rom_value == None else self.rom_value
    