import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='django-geoexplorer',
    version='4.0.2', # actually based on my fork, should we base the git hash of it?
    author='Ariel Nunez',
    author_email='ingenieroariel@gmail.com',
    url='https://github.com/GeoNode/django-geoexplorer',
    download_url = "http://pypi.python.org/pypi/django-geoexplorer/",
    description="Use GeoExplorer in your django projects",
    long_description=open(os.path.join(here, 'README.rst')).read() + '\n\n' +
                     open(os.path.join(here, 'CHANGES')).read(),
    license='LGPL, see LICENSE file.',
    install_requires=['Django==1.5.5'],
    packages=find_packages(),
    include_package_data = True,
    zip_safe = False,
    classifiers  = ['Topic :: Utilities',
                    'Natural Language :: English',
                    'Operating System :: OS Independent',
                    'Intended Audience :: Developers',
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Development Status :: 5 - Production/Stable',
                    'Programming Language :: Python :: 2.7'],
)
