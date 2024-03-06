import setuptools

setuptools.setup(
    name='sample-module',
    version='0.0.1',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=['numpy', 'torch'],
)
