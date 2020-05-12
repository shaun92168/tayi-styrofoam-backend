from CutFormat import CutFormat

WIDTHS = [900, 950, 1000, 1050, 1210]
THICKNESS = 730

class ProduceFoam:
    def __init__(self, styrofoam, number_of_production):
        self.styrofoam = styrofoam
        self.number_of_production = number_of_production
        self.cut_formats = []
        for w in WIDTHS:
            self.cut_formats.append(self.create_CutFormat(w, styrofoam.get_x(), styrofoam.get_z(), styrofoam.get_y()))
            self.cut_formats.append(self.create_CutFormat(w, styrofoam.get_y(), styrofoam.get_z(), styrofoam.get_x()))
            self.cut_formats.append(self.create_CutFormat(w, styrofoam.get_z(), styrofoam.get_x(), styrofoam.get_y()))
            self.cut_formats.append(self.create_CutFormat(w, styrofoam.get_z(), styrofoam.get_y(), styrofoam.get_x()))

    def cut(self, width, styrofoam_width, styrofoam_thickness):
        cut_info = {}
        cut_info["width_num"] = int(width / styrofoam_width)
        cut_info["thickness_num"] = int(THICKNESS / styrofoam_thickness)
        cut_info["total_per_set"] = cut_info["width_num"] * cut_info["thickness_num"]
        cut_info["width_leftover"] = width % styrofoam_width
        cut_info["thickness_leftover"] = THICKNESS % styrofoam_thickness
        return cut_info

    def create_CutFormat(self, full_width, styrofoam_width, styrofoam_thickness, styrofoam_height):
        cut_info = self.cut(full_width, styrofoam_width, styrofoam_thickness)
        set = self.number_of_production / cut_info["total_per_set"]
        lack = self.number_of_production - int(set) * cut_info["total_per_set"]
        surplus = 0
        height = styrofoam_height * get_int_set(set)
        if self.number_of_production % cut_info["total_per_set"] != 0:
            surplus = int(set + 1) * cut_info["total_per_set"] - self.number_of_production
        total_volume = full_width * height * THICKNESS
        leftover_volume = (cut_info["width_leftover"] * THICKNESS + cut_info["thickness_leftover"] * full_width) * height
        cut_format = CutFormat(get_width(full_width), get_int_set(set), lack, surplus, cut_info["width_leftover"],
                      cut_info["thickness_leftover"], styrofoam_height, total_volume, leftover_volume, styrofoam_width, cut_info["width_num"], styrofoam_thickness, cut_info["thickness_num"])
        return cut_format

    def get_optimized_results(self, n):
        sorted_by_surplus = sort_by_surplus(self.cut_formats)
        final_list = sort_by_leftover(sorted_by_surplus[0:10])
        final_list = filter_by_surplus(final_list, 30)
        # final_list = filter_by_surplus_percentage(final_list, 10)
        for format in final_list:
            format.print_simple()
            if n == 1:
                break
            n = n - 1
        return final_list


def sort_by_surplus(format_list, reverse=False):
    format_list.sort(key=lambda format: format.get_surplus(), reverse=reverse)
    return format_list

def sort_by_leftover(format_list, reverse=False):
    format_list.sort(key=lambda format: format.get_leftover_volume(), reverse=reverse)
    return format_list

def filter_by_surplus(format_list, less_than):
    result_list = list(filter(lambda format: format.get_surplus() < less_than, format_list))
    return result_list

def filter_by_surplus_percentage(format_list, less_than):
    result_list = list(
        filter(lambda format: (format.get_leftover_volume() / format.get_total_volume() * 100) < less_than,
               format_list))
    return result_list

def get_int_set(set):
    if set.is_integer():
        return int(set)
    else:
        return int(set + 1)

def get_width(total_width):
    width = 90
    if total_width == WIDTHS[0]:
        width = 90
    elif total_width == WIDTHS[1]:
        width = 95
    elif total_width == WIDTHS[2]:
        width = 100
    elif total_width == WIDTHS[3]:
        width = 105
    elif total_width == WIDTHS[4]:
        width = 121
    return width

def get_full_width(width):
    full_width = WIDTHS[0]
    if width == 90:
        full_width = WIDTHS[0]
    elif width == 95:
        full_width = WIDTHS[1]
    elif width == 100:
        full_width = WIDTHS[2]
    elif width == 105:
        full_width = WIDTHS[3]
    elif width == 121:
        full_width = WIDTHS[4]
    return full_width