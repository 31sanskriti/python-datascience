class cat:
    #attribute , fields, class members, properties
    color = 'black'
    breed = 'persian'
    age = 2

    #methods/functions
    def eat(self):
        print('cat is eating')
        
    def play(self):
        print('cat is playing')

    def description(self):
        print(f'cat is {self.age} year old')
        print(f'cat is {self.color} in color')
        print(f'cat is {self.breed} breed')

#object
tom = cat() #to call the constructor the class

tom.eat()
tom.play()
tom.description()



        
