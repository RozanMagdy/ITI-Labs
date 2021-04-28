from setuptools import setup

package_name = 'second_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
        'py_node_one=second_pkg.node1:main',
        'py_node_two=second_pkg.node2:main',
        'py_node_three=second_pkg.node3:main'
        ],
    },
)
