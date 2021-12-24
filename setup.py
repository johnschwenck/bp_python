from setuptools import setup

setup(name='bp',
      version='0.1',
      description='The Python equivalent of the bp R package. A comprehensive package to aid in the analysis of blood pressure data of all forms by providing both descriptive and visualization tools for researchers.',
      url='https://github.com/johnschwenck/bp_python',
      author='John Schwenck',
      author_email='jschwenck12@gmail.com',
      license='GPL-3',
      packages=['bp_python'],
      install_requires=[
          'pandas'
      ],
      zip_safe=False)