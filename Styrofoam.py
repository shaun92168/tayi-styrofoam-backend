class Styrofoam:
    def __init__(self, num1, num2, num3):
        """ Constructor for Styrofoam. It stores the 3 dimensions of a styrofoam. """
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

    def get_x(self):
        """ Getter for x """
        return self.x

    def get_y(self):
        """ Getter for y """
        return self.y

    def get_z(self):
        """ Getter for z """
        return self.z

    def print_foam(self):
        """ Print the styrofoam dimensions """
        print(str(self.x) + " x " + str(self.y) + " x " + str(self.z))