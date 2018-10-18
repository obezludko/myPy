class Olegleg:
    oleg_leg_color = ""
    def get_oleg_leg(self):
        oleg_leg_description = "Oleg's leg is %s" % self.oleg_leg_color
        return oleg_leg_description

class Jenleg:
    jen_leg_color = ""
    def get_jen_leg(self):
        jen_leg_description = "Jenya's leg is %s" %self.jen_leg_color
        return jen_leg_description

class Legs:
    leg1 = Olegleg()
    leg2 = Jenleg()
    leg1.oleg_leg_color = ""
    leg2.jen_leg_color = ""
    def get_legs(self):
        legs_description = "there are %s " %self.leg1.oleg_leg_color + "and %s legs" % self.leg2.jen_leg_color
        return legs_description

bothlegs = Legs()
bothlegs.leg1.oleg_leg_color = "red"
bothlegs.leg2.jen_leg_color = "black"
print(bothlegs.get_legs())