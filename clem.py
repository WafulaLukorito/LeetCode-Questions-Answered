

class Solution:
    def get_nums(self, phone, strs):
        self.phone = phone
        self.strs=strs
        #self.digitnums=[]
        self.ans =[]
        self.mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
        }
        self.hash_numbers()
        self.inverse_mapping = {char: digit for digit, chars in self.mapping.items() for char in chars}

        return self.ans
        
    def hash_numbers(self):
        for str in self.strs:
            digit_num=[]
            for c in str:
                digit_num.append(self.inverse_mapping[c])
            digit_num_str="".join(digit_num)
            if digit_num_str in self.phone:
                self.ans.append(str)
                
    

