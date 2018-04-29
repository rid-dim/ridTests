from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

recommended = {
    "cffi": ["cffi>1.11.5"]
}

install_requires = [
    "cffi>=1.11.5"
]

setup(name='ridTests',
      version='0.1',
      description='Python interface to the SAFE binaries',
      long_description=readme(),
      classifiers=[
            'Development Status :: 1 - Dev',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3.6+',
            'Topic :: File Utilities and Management',
      ],
      keywords='safenetwork safenet interface',
      url='https://github.com/rid-dim/ridTests',
      license='MIT',
      packages=['ridTests'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'safeAuth=ridTests:Authenticator', # I just thought it would be cool to have a simple and basic authenticator available in the command line
              'safeConn=ridTests:ConnTest',      # and maybe a connection test as well - rid
          ],}
      )
