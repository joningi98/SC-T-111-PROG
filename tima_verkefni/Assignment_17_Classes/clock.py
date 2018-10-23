class Clock(object):
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def str_update(self, update):
        hh, mm, ss = update.split(':')
        self.hours = int(hh)
        self.minutes = int(mm)
        self.seconds = int(ss)

    def add_clocks(self, clock):
        s_dif, s = divmod((self.seconds + clock.seconds), 60)
        m_dif, m = divmod((self.minutes + clock.minutes + s_dif), 60)
        h = (self.hours + clock.hours + m_dif) % 24
        return Clock(h, m, s)

    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)


clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
clock3 = clock1.add_clocks(clock2)
print(clock3)
