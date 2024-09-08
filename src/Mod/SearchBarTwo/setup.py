from setuptools import setup
import os

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            "freecad", "search_bar_two", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.search_bar_two',
      version=str(__version__),
      packages=['freecad',
                'freecad.search_bar_two'],
      maintainer="me",
      maintainer_email="me@foobar.com",
      url="https://foobar.com/me/coolWB",
      description="SearchBarTwo does something cool.",
      install_requires=['numpy',],
      include_package_data=True)
