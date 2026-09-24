class smartphone:
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.price = price
    
    def make_call(self,person_name):
        print(f'calling {person_name} from my {self.brand}')    

myphone = smartphone('iphone', 'white','2lakh')
futuristicphone = smartphone('iphone','purple','7lakh')

futuristicphone.color = 'gold'


myphone.make_call('Father')

print(futuristicphone.color)