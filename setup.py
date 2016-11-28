#!/usr/bin/env python3

from setuptools import find_packages, setup


with open('requirements.txt') as requirements:
    requirements = requirements.read().splitlines()

with open('README.md') as readme:
    long_description = readme.read()

if __name__ == '__main__':
    setup(name='wikiphilosophy',
          version='0.3',
          description='See how every wikipedia article leads to Philosophy',
          author='Adhityaa Chandrasekar',
          author_email='c.adhityaa@gmail.com',
          maintainer='Adhityaa Chandrasekar',
          maintainer_email='c.adhityaa@gmail.com',
          platforms='any',
          packages=find_packages(),
          install_requires=requirements,
          license='AGPL-3.0',
          long_description=long_description,
          entry_points={'console_scripts': ['wikiphilosophy = wikiphilosophy:main']},
          classifiers=[
              'Development Status :: 4 - Beta',

              'Environment :: Console',
              'Environment :: MacOS X',
              'Environment :: Win32 (MS Windows)',
              'Environment :: X11 Applications :: Gnome',

              'Intended Audience :: Developers',

              'License :: OSI Approved :: GNU Affero General Public License '
              'v3 or later (AGPLv3+)',

              'Operating System :: OS Independent',

              'Programming Language :: Python :: Implementation :: CPython',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3 :: Only'])
