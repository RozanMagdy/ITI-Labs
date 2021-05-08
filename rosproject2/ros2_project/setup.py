from setuptools import setup
import os
from glob import glob

package_name = 'ros2_project'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rouzan',
    maintainer_email='rozanabdelmawla@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'py_node_one=ros2_project.control_node:main',
        'py_node_two=ros2_project.Spawn_node:main',
        ],
    },
)
