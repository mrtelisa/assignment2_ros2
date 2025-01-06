from setuptools import setup

package_name = 'ass2_ros2'

setup(
    name='ass2_ros2',
    version='0.0.1',
    packages=['ass2_ros2'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + 'ass2_ros2']),
        ('share/' + 'ass2_ros2', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='s6504193@studenti.unige.it',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [  
            'UI_node = ass2_ros2.UI:main',
        ],
    },
)
