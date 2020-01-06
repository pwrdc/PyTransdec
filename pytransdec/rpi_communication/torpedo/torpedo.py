import time

from rpi_communication.depth.IDepthSensor import IDepthSensor
from rpi_communication.base_communication import BaseCommunication

class DepthSensor(BaseCommunication, IDepthSensor):
    def __init__(self, port, is_log, log_file_name, log_directory):
        super(DepthSensor, self).__init__(port, is_log, log_file_name, log_directory)

    def send_depth(self, depth):
        self.client.send_data(depth)

    def log(self, msg, logtype='info'):
        if self.logger:
            self.logger.log(msg, logtype=logtype)

if __name__ == '__main__':
    depth_sensor = DepthSensor()
    while True:
        self.client.send_data(depth)