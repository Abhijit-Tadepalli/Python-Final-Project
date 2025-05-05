from setuptools import setup

package_name = 'ur5_human_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_dir={'': '.'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your@email.com',
    description='Natural language control of UR5 using MoveIt',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ur5_moveit_control = ur5_human_control.ur5_moveit_control:main',
        ],
    },
)

