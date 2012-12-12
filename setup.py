from distutils.core import setup

version = '1.0.3a'

setup(name='pyactiveresource',
      version=version,
      description='ActiveResource for Python',
      author='Jared Kuolt, Brandon Schlueter',
      author_email='me@superjared.com, bs@bschlueter.com',
      url='https://github.com/bluSch/pyactiveresource',
      packages=['pyactiveresource'],
      package_dir={'pyactiveresource':'src'},
      license='MIT License',
      platforms=['any'],
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers', 
                   'License :: OSI Approved :: MIT License', 
                   'Operating System :: OS Independent', 
                   'Programming Language :: Python', 
                   'Topic :: Software Development', 
                   'Topic :: Software Development :: Libraries', 
                   'Topic :: Software Development :: Libraries :: Python Modules']
      
    )
