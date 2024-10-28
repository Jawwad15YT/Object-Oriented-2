class Country():
    def __init__(self,size,military,wealth):
        self.size = size
        self.military = military
        self.wealth = wealth

Bangladesh = Country("small","Sorta Weak","Currently somewhat poor, with many lower class areas in poverty")
India = Country("Huge","Very strong, one of the strongest in the world","Rich but some areas in the country are in poverty")
Uganda = ("small","Weak","Poor")

print(Bangladesh.military)
print(India.wealth)
print(Bangladesh.size)