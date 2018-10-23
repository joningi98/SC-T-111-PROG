class Clock(object):
    def __init__(self, hours='0', minutes='0', seconds='0'):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return str(self.hours + ':' + self.minutes + ':' + self.seconds)

    def str_update(self, update):
        hh, mm, ss = update.split(':')
        self.hours = hh
        self.minutes = mm
        self.seconds = ss


    def add_clocks(self):
        pass


clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
