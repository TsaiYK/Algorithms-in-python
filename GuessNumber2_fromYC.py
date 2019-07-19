import random
import time

class GuessNumber:
    def __init__(self,ndigits):
        self.ndigits = ndigits
        self.A = None
        self.B = None
    def CodeGenerate(self):
        self.secrete_code = []
        for i in range(ndigits):
            digit = random.randint(0,9)
            while str(digit) in self.secrete_code:
                digit = random.randint(0,9)
            self.secrete_code.append(str(digit))
    def strcmp(self,guess_code):
        self.A = 0
        self.B = 0
        n_guess = len(guess_code)
        n_secrete = len(self.secrete_code)
        while n_guess != n_secrete:
            print("String length mistach!")
            print("You should enter a ",ndigits,"-digit number!")
        for i, c in enumerate(guess_code):
            for j, d in enumerate(self.secrete_code):
                if c == d:
                    if i == j:
                        self.A += 1
                    else:
                        self.B += 1
#        for i in range(n_guess):
#            c = guess_code[i]
#            for j in range(n_secrete):
#                if c == self.secrete_code[j]:
#                    if i==j:
#                        self.A += 1
#                    else:
#                        self.B += 1
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