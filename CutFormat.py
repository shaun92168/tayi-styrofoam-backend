class CutFormat:
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
        return self.width

    def get_set(self):
        return self.set

    def get_lack(self):
        return self.lack

    def get_surplus(self):
        return self.surplus

    def get_width_leftover(self):
        return self.width_leftoevr

    def get_thickness_leftover(self):
        return self.thickness_leftover

    def get_height_per_set(self):
        return self.height_per_set

    def get_total_volume(self):
        return self.total_volume

    def get_leftover_volume(self):
        return self.leftover_volume

    def get_styrofoam_width(self):
        return self.styrofoam_width

    def get_styrofoam_thickness(self):
        return self.styrofoam_thickness

    def get_width_num(self):
        return self.width_num

    def get_thickness_num(self):
        return self.thickness_num

    def print_simple(self):
        width_num = int(self.width*10 / self.styrofoam_width)
        thickness_num = int(730 / self.styrofoam_thickness)
        leftover_percent = self.leftover_volume/self.total_volume
        print('{}x{} {}x{}, {}/{}丸, 多{}, {:.0%}廢料'.format(self.styrofoam_width, width_num, self.styrofoam_thickness, thickness_num, self.width, self.set, self.surplus, leftover_percent))