# https://leetcode.com/problems/integer-to-english-words/

import random


class Solution(object):
    THOUSANDS = ["Thousand", "Million", "Billion"]
    HUNDRED = "Hundred"
    SINGLE_DIGIT_IN_ENG = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    DOUBLE_DIGIT_IN_ENG = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety",
                           "",
                           "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    def numberToWords(self, num):
        translation = ""
        n = num
        base = -1
        while n > 0:
            reminder = n % 1000
            this_trans = self.translate_three_digits(reminder)
            if base >= 0 and len(this_trans):
                this_trans += " " + self.THOUSANDS[base]
            translation = this_trans + (" " if len(this_trans) and len(translation) else "") + translation
            n /= 1000
            base += 1
        return translation if len(translation) else "Zero"

    def translate_three_digits(self, num):
        this_trans = ""
        reminder = num
        reminder %= 1000
        hundred_text = self.get_text(reminder/100, self.SINGLE_DIGIT_IN_ENG, self.HUNDRED)
        reminder %= 100
        if 10 < reminder < 20:
            tens_text = self.DOUBLE_DIGIT_IN_ENG[reminder-1]
            ones_text = ""
        else:
            tens_text = self.get_text(reminder/10, self.DOUBLE_DIGIT_IN_ENG, "")
            reminder %= 10
            ones_text = self.get_text(reminder, self.SINGLE_DIGIT_IN_ENG, "")
        this_trans += hundred_text
        this_trans += self.handle_text_paddling(tens_text, this_trans)
        this_trans += self.handle_text_paddling(ones_text, this_trans)
        return this_trans

    @staticmethod
    def handle_text_paddling(content_text, full_content_string):
        return (" " if len(content_text) and len(full_content_string) else "") + content_text

    @staticmethod
    def get_text(num, text_dict, unit_text):
        return "" if num == 0 else text_dict[num-1] + (" " + unit_text if len(unit_text) > 0 else "")


a = Solution()
for _ in range(100):
    print(random.randint(0, 2**31))