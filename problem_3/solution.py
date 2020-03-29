class Solution:
    def __init__(self, num1, num2):
	    self.num1 = num1
	    self.num2 = num2

    def multiply(self):
            
        num_hash = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0} #hash for each digit in the string
        mul = 10
        n1 = 0
        n2 = 0
        product = 0
        for c in self.num1: #traverse through each digit in first number
            n1 = (n1*mul)+num_hash[c] #keep track of each digit and multiply by 10(used to convert to integer)

        for c in self.num2: #traverse through each digit in second number
            n2 = (n2*mul)+num_hash[c] #keep track of each digit and multiply by 10(used to convert to integer)

        product = n1*n2 #multiply both integers together
        return tostring(product)

def tostring(n):
    string_hash = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",0:"0"} #hash for each digit
    string = ""
    while True:
        remainder = n % 10 #find remainder 
        n = n//10 #find remaining after dividing
        string = string_hash[remainder] + string #convert to string
        if n == 0: #end when there is no more left to add
            break
    return string


