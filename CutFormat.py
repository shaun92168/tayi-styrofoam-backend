class CutFormat:
    """ CutFormat stores information about a cut format """
    def __init__(self, width, set, lack, surplus, width_leftoevr, thickness_leftover, height_per_set, total_volume, leftover_volume, styrofoam_width, width_num, styrofoam_thickness, thickness_num):
        self.width = width
        self.set = set
        self.lack = lack
        self.surplus = surplus
        self.width_leftoevr = width_leftoevr
        self.thickness_leftover = thickness_leftover
        self.height_per_set = height_per_set
        self.total_volume = total_volume
        self.leftover_volume = leftover_volume
        self.styrofoam_width = styrofoam_width
        self.width_num = width_num
        self.styrofoam_thickness = styrofoam_thickness
        self.thickness_num = thickness_num

    def get_width(self):
        """ Getter for width """
        return self.width

    def get_set(self):
        """ Getter for set """
        return self.set

    def get_lack(self):
        """ Getter for lack """
        return self.lack

    def get_surplus(self):
        """ Getter for surplus """
        return self.surplus

    def get_width_leftover(self):
        """ Getter for width leftover """
        return self.width_leftoevr

    def get_thickness_leftover(self):
        """ Getter for thickness leftover """
        return self.thickness_leftover

    def get_height_per_set(self):
        """ Getter for height per set """
        return self.height_per_set

    def get_total_volume(self):
        """ Getter for total volume """
        return self.total_volume

    def get_leftover_volume(self):
        """ Getter for leftover volume """
        return self.leftover_volume

    def get_styrofoam_width(self):
        """ Getter for styrofoam width """
        return self.styrofoam_width

    def get_styrofoam_thickness(self):
        """ Getter for styrofoam thickness """
        return self.styrofoam_thickness

    def get_width_num(self):
        """ Getter for width num """
        return self.width_num

    def get_thickness_num(self):
        """ Getter for thickness num """
        return self.thickness_num

    def print_simple(self):
        """ print cut format """
        if self.styrofoam_width == 0 or self.styrofoam_thickness == 0 or self.total_volume == 0:
            print('N/A')
        else:
            width_num = int(self.width*10 / self.styrofoam_width)
            thickness_num = int(730 / self.styrofoam_thickness)
            leftover_percent = self.leftover_volume/self.total_volume
            print('{}x{} {}x{}, {}/{}丸, 多{}, {:.0%}廢料'.format(self.styrofoam_width, width_num, self.styrofoam_thickness, thickness_num, self.width, self.set, self.surplus, leftover_percent))