class Marks:

    def __init__(self, n):
        self.dc = {
            'maths': None,
            'physics': None,
            'chemistry': None
        }
        self.name : str


        name = n
        self.dc['maths'] = int(input(f'{name} maths marks: '))
        self.dc['physics'] = int(input(f'{name} physics marks: '))
        self.dc['chemistry'] = int(input(f'{name} chemistry marks: '))
    
    def get_total(self):
        return sum(self.dc.values())
 
    def get_maths(self):
        return self.dc['maths']       

    def get_physics(self):
        return self.dc['physics']

    def get_chemistry(self):
        return self.dc['chemistry']

vansh = Marks('vansh')
anshul = Marks('anshul')

if(vansh.get_total() > anshul.get_total()):
    print("vansh is topper!")
elif(vansh.get_total() == anshul.get_total()):
    if(vansh.get_maths() > anshul.get_maths()):
        print("vansh is topper!")
    elif(vansh.get_maths() == anshul.get_maths()):
        if(vansh.get_physics() > anshul.get_physics()):
            print("vansh is topper!")
        elif(vansh.get_physics() == anshul.get_physics()):
            if(vansh.get_chemistry() > anshul.get_chemistry()):
                print("vansh is topper!")
            elif(vansh.get_chemistry() == vansh.get_chemistry()):
                print("equal marks!")
            else:
                print("anshul is topper!")
        else:
            print("anshul is topper!") 
    else:
        print("anshul is topper!")
else:
    print("anshul is topper!")
