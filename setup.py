from setuptools import setup

setup(name='pandasbox',
      version='0.1',
      description='Read csv into pandas directly from box',
      url='http://github.com/alexandercbooth/pandasbox',
      author='Alexander Booth',
      author_email='alexander.c.booth@gmail.com',
      license='Apache',
      tests_require=['pytest'],
      test_suite='pytest',
      packages=['pandasbox'],
      zip_safe=False)
