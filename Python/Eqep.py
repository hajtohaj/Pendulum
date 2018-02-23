import os, time

class Eqep:

    def __init__(self, eqep_path):
        self.base_path = eqep_path
        self.enabled_file = os.path.join(self.base_path, 'enabled')
        self.position_file = os.path.join(self.base_path, 'position')

    def __read(self, f_name):
        fd = open(f_name, "rt")
        val = fd.read().rstrip()
        fd.close()
        return val

    def __write(self, f_name, value):
        fd = open(f_name, "rt")
        fd.seek(0)
        fd.write(str(value).rstrip())
        fd.close()

    def position(self, *new_position):
        if len(new_position) > 0:
            self.__write(self.position_file, str(new_position[0]))
        return self.__read(self.position_file)

    def reset_position(self):
        self.position('0')
        return 0

    def enable(self):
        self.__write(self.enabled_file, '1')

    def disable(self):
        self.__write(self.enabled_file, '0')

    def enabled(self):
         return self.__read(self.enabled_file)

if __name__ == "__main__":

    EQEP2_PATH = '/sys/bus/platform/drivers/eqep/48304180.eqep'

    eqep2 = Eqep(EQEP2_PATH)

    try:
        while True:
            print(eqep2.position())
            time.sleep(0.1)
    except KeyboardInterrupt:
        os._exit(0)
