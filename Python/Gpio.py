import os, time

class Gpio:
    BASE_PATH = '/sys/class/gpio/'

    def __init__(self, gpio_id, direction='in'):
        self.id = str(gpio_id)
        self.path = os.path.join(self.BASE_PATH, 'gpio' + self.id)
        self.direction_file = os.path.join(self.path, 'direction')
        self.value_file = os.path.join(self.path, 'value')
        if not os.path.exists(self.path):
            self.export()
        if not self.direction() == direction:
            self.direction(direction)

    def __read(self, f_name):
        fd = open(f_name, "rt")
        val = fd.read().rstrip()
        fd.close()
        return val

    def __write(self, f_name, value):
        fd = open(f_name, "wt")
        fd.write(str(value).rstrip())
        fd.close()

    def export(self):
        exporter = os.path.join(self.BASE_PATH, 'export')
        self.__write(exporter, str(self.id))

    def unexport(self):
        unexporter = os.path.join(self.BASE_PATH, 'unexport')
        self.__write(unexporter, str(self.id))

    def direction(self, *direction):
        if len(direction) > 0:
            self.__write(self.direction_file, direction)
        return self.__read(self.direction_file)

    def value(self, *value):
        if len(value) > 0:
            self.__write(self.value_file, str(value[0]))
        return int(self.__read(self.value_file).rstrip())

    def set_one(self):
        return self.value(1)

    def set_zero(self):
        return self.value(0)

    def toggle_value(self):
        if self.value():
            return self.set_zero()
        return self.set_one()

if __name__ == "__main__":

    gpio = Gpio(89, 'out')

    try:
        while True:
            print(gpio.toggle_value())
            time.sleep(0.25)
    except KeyboardInterrupt:
        os._exit(0)