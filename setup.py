from setuptools import setup, find_packages

version = '0.17'

setup(name='Achilterm',
      version=version,
      author='Florent Gallaire',
      author_email='fgallaire@gmail.com',
      url='http://fgallaire.github.io/achilterm',
      license='GNU AGPLv3+',
      keywords='sh shell bash',
      classifiers=[
          "Development Status :: 6 - Mature",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: System :: Shells",
          "Topic :: Terminals :: Terminal Emulators/X Terminals",
          "Programming Language :: Python :: 2.5",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
      ],
      packages=find_packages(exclude=['docs', 'examples', 'tests']),
      py_modules=['achilterm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['webob>=1.0'],
      )
