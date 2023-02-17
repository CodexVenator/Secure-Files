from setuptools import find_packages, setup

setup(
    name='SecureFiles',
    version='1.0-beta',
    description='A Python class for encrypting and decrypting files using the AES encryption algorithm.',
    author='CodexVenator',
    url='https://github.com/CodexVenator/SecureFiles',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pycryptodome',  
    ],
    entry_points={
    'console_scripts': [
        'secure=src.main:main'
    ]
}
)