class Fan:
    def __init__(self):
        self.brand="usha"
        self.color="white"
        self.cost="1000"
        self.noOfBlades=3
    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan is rotating")
f1=Fan()
print(f1.brand)
print(f1.color)
print(f1.cost) 
print(f1.noOfBlades)
f1.on()
f1.rotate()


