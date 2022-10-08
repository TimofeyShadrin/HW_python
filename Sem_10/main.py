import Road as r
import TrafficLight as tl


def main():
    light = tl.TrafficLight()
    light.running(7, 2, 8)

    mass = r.Road(20, 5000)
    mass.calc_mass(5)


if __name__ == '__main__':
    main()
