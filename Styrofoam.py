class Styrofoam:
    def __init__(self, num1, num2, num3, orderNum=0):
        self.z = min(num1, num2, num3)
        if self.z == num1:
            self.x = num2
            self.y = num3
        elif self.z == num2:
            self.x = num1
            self.y = num3
        else:
            self.x = num1
            self.y = num2
        self.orderNum = orderNum

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_orderNum(self):
        return self.orderNum

    def print_foam(self):
        print(str(self.x) + " x " + str(self.y) + " x " + str(self.z))