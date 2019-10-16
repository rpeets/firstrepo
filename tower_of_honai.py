#
#
#
"""
The objective of the puzzle is to move the entire t1 stack
to t3, obeying the following simple rules:
    1, Only one disk can be moved at a time.
    2, Each move consists of taking the upper disk from one of the stacks
       and placing it on top of another stack or on an empty one.
    3, No larger disk may be placed on top of a smaller disk.
"""

class Honai():
    def __init__(self):
        self.tower1 = [4, 3, 2, 1]
        self.tower2 = []
        self.tower3 = []
        self.result = [4, 3, 2, 1]

    def disk_move(self, s, d):
        if s == 't1':
            source = self.tower1
        elif s == 't2':
            source = self.tower2
        elif s == 't3':
            source = self.tower3

        if d == 't1':
            dest = self.tower1
        elif d == 't2':
            dest = self.tower2
        elif d == 't3':
            dest = self.tower3
        
        if len(source) > 0 and s != d and self.valid_move(source, dest) == True:
            disk = source.pop()
            dest.append(disk)
        else:
            print("Invalid Move!!!")
    
    def valid_move(self, s, d):
        try:
            dest_val = d[-1]
        except IndexError:
            dest_val = 99
        
        try: 
            scr_val = s[-1]
        except IndexError:
            scr_val = 0
        return dest_val > scr_val
            
    def __str__(self):
        print()
        print('t1 :',self.tower1)
        print('t2 :',self.tower2)
        print('t3 :',self.tower3)
        return ''
    
    def check_win(self):
        return self.tower3 == self.result
    

def main():
    htower = Honai()
    while True:
        if htower.check_win() is False:
            print(htower)
            scr = input('Move From : ')
            dst = input('Move To   : ')
            htower.disk_move(scr, dst)
        else:
            print('You Won!!!')
            answer = input("Do you like to pay again Y/N ?")
            if answer.lower().startswith('y'):
                continue
            elif answer.lower().startswith('n'):
                break

if __name__ == '__main__':
    main()
