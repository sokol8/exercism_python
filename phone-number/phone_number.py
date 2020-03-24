import re

class Phone(object):
    def __init__(self, phone_number):
    	s = ''.join([x for x in phone_number if x.isdigit()])
    	
    	if 10 == len(s):
    		self.__match__(s)
    	elif 11 == len(s) and '1' == s[0]:
    		s = s[1:]
    		self.__match__(s)
    	else:
    		raise ValueError('not a NANP phone number')

    #'[1]?[2-9]\\d{2}[2-9]\\d{2}\\d{4}'
    def __match__(self, number):
    	m = re.match('[2-9]\\d{2}[2-9]\\d{2}\\d{4}', number)
    	if m:
    		number = m.group()
    		self.area_code = number[0:3]
    		self.exchange_code = number[3:6]
    		self.subscriber_number = number[6:10]
    	else:
    		raise ValueError('Error parsing. Not a NANP phone number')

    @property
    def number(self):
    	return self.area_code + self.exchange_code + self.subscriber_number
    
    #(223) 456-7890
    def pretty(self):
    	return '({}) {}-{}'.format(self.area_code, self.exchange_code, self.subscriber_number)

