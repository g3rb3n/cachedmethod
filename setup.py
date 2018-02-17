from setuptools import setup

long_description = ''
setup(name='cachedmethod',
    version='0.1.0',
    description='',
    long_description=long_description,
    url='http://github.com/g3rb3n/cachedmethod',
    author='Gerben van Eerten',
    author_email='gerben@eerten.com',
    license='MIT',
    packages=['cachedmethod'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='development',
    python_requires='>=3'
)
