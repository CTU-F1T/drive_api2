from setuptools import setup

package_name = 'drive_api2'

setup(
    name=package_name,
    version='0.3.3',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        # (
        #     'share/' + package_name + '/launch',
        #     ['launch/start.launch.py']
        # ),
        (
            'share/' + package_name + '/config',
            ['config/drive_api_node.yaml']
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jaroslav Klapálek',
    maintainer_email='klapajar@fel.cvut.cz',
    description='TODO',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drive_api_node = drive_api2.drive_api_node:main',
        ],
    },
)
