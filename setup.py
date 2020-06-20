from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cana-algorithms',
    version='0.1.0',
    description='Algorithms\' implementations from CANA course.',
    long_description=readme,
    author='Thais Amorim',
    url='https://github.com/thasmarinho/cana-algorithms',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
