from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-TriacHatActor',
      version='0.0.4',
      description='CraftBeerPi Plugin for controlling actor using Waveshare\'s 2CH Triac HAT for Raspberry Pi',
      author='Netanel Klein',
      author_email='netanel@netanelk.com',
      url='https://github.com/netanelklein/cbpi4-TriacHatActor',
      licence='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-TriacHatActor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-TriacHatActor', 'TriacHat_2CH_Driver'],
      install_requires=['cbpi>=4.0.0.56', 'RPi.GPIO', 'pyserial', 'smbus'],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
