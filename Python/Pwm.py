import os, time

class Pwm:
    PWM_PATH = '/sys/class/pwm'

    def __init__(self, chip_id, pwm_id):
        self.chip_id = chip_id
        self.pwm_id = pwm_id
        self.path = os.path.join(self.PWM_PATH, 'pwmchip' + str(self.chip_id), 'pwm' + str(self.pwm_id))
        self.period_file = os.path.join(self.path, 'period')
        self.duty_cycle_file = os.path.join(self.path, 'duty_cycle')
        self.enable_file = os.path.join(self.path, 'enable')
        if not self.exported():
            self.export()

    def exported(self):
        if os.path.exists(self.path):
            return True
        return False

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
        exporter = os.path.join(self.PWM_PATH, 'pwmchip' + str(self.chip_id), 'export')
        self.__write(exporter, self.pwm_id)

    def enable(self):
        self.__write(self.enable_file, '1')

    def disable(self):
        self.__write(self.enable_file, '0')

    def period(self, *new_period):
        if len(new_period) > 0:
            self.__write(self.period_file, new_period[0])
        return self.__read(self.period_file)

    def duty_cycle(self, *new_duty_cycle):
        if len(new_duty_cycle) > 0:
            self.__write(self.duty_cycle_file, new_duty_cycle[0])
        return self.__read(self.duty_cycle_file)

if __name__ == "__main__":

    pwm0 = Pwm(0,0)
    print(pwm0.period(1000000))
    print(pwm0.period())
    print(pwm0.duty_cycle(250000))
    print(pwm0.duty_cycle())