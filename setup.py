from setuptools import setup

setup(
    name='pypollen',
    packages=['pypollen'],
    version='0.1.3',
    description='Provides an API for requesting information from Benadryls Social Pollen Count (https://benadryl.co.uk/social-pollen-count/)',
    author='Kyle Gordon',
    author_email='kyle@glasgownet.com',
    url='https://github.com/kylegordon/pypollen',
    download_url='https://github.com/kylegordon/pypollen/tarball/0.1.3',
    keywords=['weather', 'pollen', 'allergy', 'environment', 'benadryl'],
    install_requires=['requests', 'datetime'],
    classifiers=[],
)
