import setuptools

setuptools.setup(
    name='drewsTools',
    packages=setuptools.find_packages(),
    install_requires=[
        'proxmoxer',
        'requests',
        'paramiko',
    ],
)
