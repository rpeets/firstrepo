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
        self.towera = [4, 3, 2, 1]
        self.towerb = []
        self.towerc = []
        self.result = [4, 3, 2, 1]
        self.count = 0

    def disk_move(self, scr, dst):        
        if len(scr) > 0 and scr != dst and \
            self.valid_move(scr, dst) == True:
            disk = scr.pop()
            dst.append(disk)
            self.count += 1
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
        print('A :',self.towera)
        print('B :',self.towerb)
        print('C :',self.towerc)
        return ''
    
    def check_win(self):
        return self.towerc == self.result
    

def main():
    htower = Honai()
    tower_name = ['a', 'b', 'c']
    while True:
        if htower.check_win() is False:
            print(htower)
            scr = input('Move From : ').lower()
            dst = input('Move To   : ').lower()

            if scr in tower_name and dst in tower_name:
                if scr == 'a':
                    scr = htower.towera
                elif scr == 'b':
                    scr = htower.towerb
                elif scr == 'c':
                    scr = htower.towerc

                if dst == 'a':
                    dst = htower.towera
                elif dst == 'b':
                    dst = htower.towerb
                elif dst == 'c':
                    dst = htower.towerc

                htower.disk_move(scr, dst)
            else:
                print("Invalid Input!!!")
        else:
            print('Awesome, You have completed in {} move!!!' \
                        .format(htower.count))
            answer = input("Do you like to try again Y/N ?")
            if answer.lower().startswith('y'):
                htower = Honai()
                continue
            elif answer.lower().startswith('n'):
                break

if __name__ == '__main__':
    main()
