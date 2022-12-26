from setuptools import setup

package_name = 'myRobot'

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
    maintainer='ali-x86',
    maintainer_email='aasgharansari@yahoo.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robotPublisher=myRobot.robotPublisher:main',
            'pubKey=myRobot.pubKey:main',
            'webcam_sub=myRobot.webcam_sub:main',
            'webcam_pub=myRobot.webcam_pub:main'
        ],
    },
)
