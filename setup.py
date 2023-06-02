from setuptools import setup
import os
from glob import glob

package_name = 'pyvoyis_ros2'
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Miquel Massot',
    maintainer_email='miquel.massot@gmail.com',
    description='ROS2 wrapper for pyvoyis driver',
    license='GPLv3',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)