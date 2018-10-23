class RockGuitars(object):
    def __init__(self, guitarist='', guitar=''):
        self.guitarist = guitarist
        self.guitar = guitar

    def set_entry(self, guitarist, guitar):
        

    def __str__(self):
        return ('{} {}'.format(self.guitarist, self.guitar))


RockGuitars("Jimmy Page", "Gibson Les Paul Standard")
