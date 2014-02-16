import os
from setuptools import setup
import xenon


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as fobj:
    readme = fobj.read()

setup(name='xenon',
      version=xenon.__version__,
      author='Michele Lacchia',
      author_email='michelelacchia@gmail.com',
      url='https://xenon.readthedocs.org/',
      download_url='https://pypi.python.org/xenon/',
      license='MIT',
      description='Monitor code metrics for Python on your CI server',
      platforms='any',
      long_description=readme,
      py_modules=['xenon'],
      tests_require=['tox'],
      install_requires=['radon'],
      entry_points={'console_scripts': ['xenon = xenon:main']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Utilities',
      ]
)