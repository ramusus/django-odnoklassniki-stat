from setuptools import setup, find_packages

setup(
    name='django-odnoklassniki-stat',
    version='0.1',
    description='Django implementation for odnoklassniki API Stats',
    long_description=open('README.md').read(),
    author='ramusus',
    author_email='ramusus@gmail.com',
    url='https://github.com/ramusus/django-odnoklassniki-stat',
    download_url='http://pypi.python.org/pypi/django-odnoklassniki-stat',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,  # because we're including media that Django needs
    install_requires=[
        'django-odnoklassniki-api>=0.2.3',
        'django-odnoklassniki-groups>=0.0.6',
        'django-odnoklassniki-users>=0.0.6',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)