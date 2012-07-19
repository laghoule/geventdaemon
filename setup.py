from setuptools import setup

setup(name="geventdaemon",
      version="1.0",
      author="Antonin Amand",
      author_email="antonin.amand@gmail.com",
      description="gevent daemonizer",
      py_modules=['geventdaemon'],
      zip_safe=False,
      install_requires=[
          'gevent',
          'python-daemon',
        ],
    )

