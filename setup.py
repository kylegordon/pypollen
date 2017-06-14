from setuptools import setup

setup(
    name='pollen',
    packages=['pollen'],
    version='0.1.0',
    description='Provides an API for requesting information from Benadryl's Social Pollen Count (https://benadryl.co.uk/social-pollen-count/)',
    author='Kyle Gordon',
    author_email='kyle@glasgownet.com',
    url='https://github.com/kylegordon/pypollen',
    download_url='https://github.com/kylegordon/pypollen/tarball/0.1.0',
    keywords=['weather', 'pollen', 'allergy', 'environment'],
    install_requires=['requests'],
    classifiers=[],
)
