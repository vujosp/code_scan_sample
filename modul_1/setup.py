import setuptools

with open('reqirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='sample',
    version='0.0.1',
    package_dir={'': '.'},
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=[requirements],
)
