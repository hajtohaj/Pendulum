import socket
import struct
import time
import os


class Can:
    CAN_FRAME_FMT = "=IB3x8s"

    def __init__(self, can_itf):
        self.can_socket = socket.socket(socket.AF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.can_socket.bind((can_itf,))

    def build_can_frame(self, can_id, data):
           can_dlc = len(data)
           data = data.ljust(8, b'\x00')
           return struct.pack(self.CAN_FRAME_FMT, can_id, can_dlc, data)

    def dissect_can_frame(self, frame):
           can_id, can_dlc, data = struct.unpack(self.CAN_FRAME_FMT, frame)
           return (can_id, can_dlc, data[:can_dlc])

    def send_frame(self, frame):
        self.can_socket.send(frame)
        return self.can_socket.recvfrom(16)


if __name__ == "__main__":

    CAN_ITF = 'can0'
    CAN_ID = 0x67F
    CAN_DATA = b'\x40\x62\x37\x00\x00\x00\x00\x00'

    can = Can(CAN_ITF)

    frame_get_position = can.build_can_frame(CAN_ID, CAN_DATA)

    sleep_interval = 0.5
    iterations = 0
    try:
        while True:
            iterations += 1
            can.send(frame_get_position)
            cf, addr = can.send.recvfrom(16)
            print('Received: can_id=%x, can_dlc=%x, data=%s' % can.send.dissect_can_frame(cf))
            time.sleep(sleep_interval)
    except KeyboardInterrupt:
        print('Iterations: {}'.format(iterations))
        os._exit(0)