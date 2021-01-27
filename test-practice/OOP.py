# # 1
# class Vehicle:
#     pass

# 2
class Vehicle:
    def __init__(self, max_speed, colour):
        self.max_speed = max_speed
        self.colour = colour

# car = Vehicle(160,'red')
# print(car.max_speed , car.colour)

# # 3
# class Vehicle:
#     def __init__(self, max_speed, colour):
#         self.max_speed = max_speed
#         self.colour = colour

#     def changeSpeed(self):
#         self.max_speed += 100

#     def changeColour(self, new_colour):
#         self.colour = new_colour

# car = Vehicle(160,'red')
# print(car.max_speed , car.colour)
# car.changeSpeed()
# car.changeColour('green')
# print(car.max_speed, car.colour)


# # 4
# class Buss(Vehicle):
#     def __init__(self, max_speed, colour):
#         super().__init__(max_speed, colour)

# schoolBuss = Buss(80,'yellow')
# print(schoolBuss.max_speed, schoolBuss.colour)

# # 5
# print(type(schoolBuss))


# # 6
# print(isinstance(schoolBuss, Vehicle))

# 7
class Buss(Vehicle):
    def __init__(self, max_speed, colour, seating_capacity):
        super().__init__(max_speed, colour)
        self.seating_capacity = seating_capacity

    def ticketPrice(self):
        ticket_price = self.seating_capacity * 0.05 + self.seating_capacity * 0.05 * 0.1
        return ticket_price

    def __repr__(self):
        return repr(f'Max speed: {self.max_speed}, Colour: {self.colour}, Seating capacity: {self.seating_capacity}, Ticket Price: {ticket_price}')

schoolBuss = Buss(80,'yellow', 200)
ticket_price = schoolBuss.ticketPrice()
print(schoolBuss.max_speed, schoolBuss.colour, schoolBuss.seating_capacity, ticket_price)

# 8
print(repr(schoolBuss))
