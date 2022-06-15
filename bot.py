import random



class bot():
    def __init__(self, bx1, by1, bx2, by2, bx3, by3, list_x, list_y):
        self.bx1 = bx1
        self.by1 = by1
        self.bx2 = bx2
        self.by2 = by2
        self.bx3 = bx3
        self.by3 = by3
        self.list_x = list_x
        self.list_y = list_y

    def results(self):
        self.bx1 = self.list_x[int(random.randint(0,4))]
        self.by1 = self.list_y[int(random.randint(0,4))]
        self.bx2 = self.list_x[int(random.randint(0,4))]
        self.by2 = self.list_y[int(random.randint(0,4))]
        self.bx3 = self.list_x[int(random.randint(0,4))]
        self.by3 = self.list_y[int(random.randint(0,4))]


