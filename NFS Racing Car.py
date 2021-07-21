class Car(object):

 def __init__(self, model, color, company, speed_limit):
    self.model = model
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.start()
    self.stop()
    self.accelarate()
    self.change_gear()

 def start(self):
    print("started")
 def stop(self):
    print("stopped")
 def accelarate(self):
    print("accelarating...")
 def change_gear(self):
    print("gear changed")

# Now that we have created the objects, let’s move on to create the individual cars in the game.

maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)

