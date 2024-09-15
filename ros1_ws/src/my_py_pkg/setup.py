from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asserhanafy',
    maintainer_email='asserhanafy@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_py_pkg.my_first_node:main",
            "draw_circle = my_py_pkg.draw_circle:main",
            "pose_subscriber = my_py_pkg.pose_subscriber:main",
            "turtle_controller = my_py_pkg.turtle_controller:main",
            "ultrasonic_publisher = my_py_pkg.ultrasonic_publisher:main",
            "ultrasonic_subscriber = my_py_pkg.ultrasonic_subscriber:main",
            "RPS = my_py_pkg.main:main",
            "turtle_catch = my_py_pkg.turtle_catch:main"
        ],
    },
)