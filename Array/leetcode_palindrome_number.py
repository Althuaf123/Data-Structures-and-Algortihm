class Palindrome:
    def check_palindrome(self, x: int):
        y = str(x)
        count = 0
        if (len(y))%2 != 0:
            print(len(y))
            for i in range(len(y)//2-1):
                print((len(y)//2))
                if y[i] == y[(len(y)//2)-i-1]:
                    count == 1
                elif y[i] != y[len(y)//2-i-1]:
                    count == 0
                    break
                else:
                    print("e")
                    break
        else:
            print('r')
        if count == 1:
            print('palindrome')
        else:
            print('not palindrome')
        # else:
        #     for i in range(len(y)/2):
        #         if y[i] != y[len(y)/2-i]:
        #             print('Not palindrome')
        #             break
        #         else:
        #             print('Palindromee')

L = Palindrome()
L.check_palindrome(121)