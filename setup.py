from setuptools import setup

setup(name='cbpi4-TriacHatActor',
      version='0.0.1',
      description='CraftBeerPi Plugin for controlling actor using Triac HAT for Raspberry Pi',
      author='Netanel Klein',
      author_email='netanel@netanelk.com',
      url='',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'TriacPID': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-TriacHatActor'],
     )
