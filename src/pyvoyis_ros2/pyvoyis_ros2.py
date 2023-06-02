from pathlib import Path

import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
from rcl_interfaces.msg import ParameterDescriptor
from ament_index_python.packages import get_package_share_directory, PackageNotFoundError
# may raise PackageNotFoundError


from pyvoyis import VoyisAPI, Configuration

class VoyisROS2(Node):
    def __init__(self):
        super().__init__("voyis_ros2")

        # Get default configuration file
        try:
            node_dir = get_package_share_directory('pyvoyis_ros2')
            default_config_file = Path(node_dir) / 'config' / 'pyvoyis_ros2.yaml'
            if not default_config_file.is_file():
                self.get_logger().error("Default configuration file not found")
                self.get_logger().error("Please create a configuration file in {}".format(default_config_file))
                return
        except PackageNotFoundError as e:
            self.get_logger().error("Error getting package directory: {}".format(e))
            return

        config_file_desc = ParameterDescriptor(description='Configuration file for pyvoyis')
        self.declare_parameter('config_file', str(default_config_file), config_file_desc)

        self.config_file = self.get_parameter('config_file').get_parameter_value().string_value

        self.config = Configuration(self.config_file)

        self.api = VoyisAPI(self.config)

        # Offer start_acquisition service
        self.srv = self.create_service(Empty, 'start_acquisition', self.start_acquisition_srv_cb)
        # Offer stop_acquisition service
        self.srv = self.create_service(Empty, 'stop_acquisition', self.stop_acquisition_srv_cb)

        # Run VoyisAPI
        self.api.run()

        self.get_logger().info("VoyisROS2 node started")

    def start_acquisition_srv_cb(self, req):
        self.api.request_acquisition()
        return True

    def stop_acquisition_srv_cb(self, req):
        self.api.request_stop()
        return True


def main(args=None):
    rclpy.init(args=args)
    node = VoyisROS2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()