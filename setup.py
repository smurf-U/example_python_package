from setuptools import setup, find_packages


setup(
    name='examplepythonpypi',
    version='0.1.1',
    license='MIT',
    author="Kaushal Prajapati",
    author_email='kbprajapati@live.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/smurf-U/example_python_package',
    keywords='example python project',
    install_requires=[
          'flask',
      ],

)
