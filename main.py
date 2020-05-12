from Styrofoam import Styrofoam
from ProduceFoam import ProduceFoam

def main():
    # optimize_cut(350,185,30,396)
    # optimize_cut(310,260,40,548)
    # optimize_cut(330,140,30,544)
    # optimize_cut(295,140,60,660)
    # optimize_cut(325,105,55,1920)
    optimize_cut(200,200,55,640)

def optimize_cut(x, y, z, n):
    s = Styrofoam(x, y, z)
    p = ProduceFoam(s, n)
    p.get_optimized_results(20)


if __name__ == '__main__':
    main()