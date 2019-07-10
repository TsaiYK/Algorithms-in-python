import random
import time

class GuessNumber:
    def __init__(self,ndigits):
        self.ndigits = ndigits
    def CodeGenerate(self):
        string = []
        for i in range(10):
            i = str(i)
            string.append(i)
        for j in range(1,self.ndigits):
            npos = random.randint(1,10-j)
            temp = string[npos]
            string[npos] = string[10-j]
            string[10-j] = temp
        secrete_code_split = string[10-self.ndigits:]
        self.secrete_code = secrete_code_split[0] + secrete_code_split[1] + secrete_code_split[2] + secrete_code_split[3]
    def strcmp(self,guess_code):
        self.A = 0
        self.B = 0
        n_guess = len(guess_code)
        n_secrete = len(self.secrete_code)
        while n_guess != n_secrete:
            print("String length mistach!")
            print("You should enter a ",ndigits,"-digit number!")
            break
        for i in range(n_guess):
            c = guess_code[i]
            for j in range(n_secrete):
                if c == self.secrete_code[j]:
                    if i==j:
                        self.A += 1
                    else:
                        self.B += 1
        print(self.A," A",self.B," B")

ndigits = 4
Number = GuessNumber(ndigits)
Number.CodeGenerate()
print(Number.secrete_code)
A = 0
B = 0

start = time.time()
while A != ndigits:
    guess_code = input("Please enter a number: ")
    Number.strcmp(guess_code)
    A = Number.A
end = time.time()
elapsed = end - start
print('The total time is %.2f second' % elapsed)