from setuptools import setup, find_packages

files = ["geventdaemon.py"]

setup(name="geventdaemon",
      version="1.0",
      author="Antonin Amand",
      author_email="antonin.amand@gmail.com",
      description="gevent daemonizer",
      packages = ['python-geventdaemon'],
      package_data = {'package' : files },
      zip_safe=False,
      install_requires=[
          'gevent',
          'python-daemon',
        ],
    )

