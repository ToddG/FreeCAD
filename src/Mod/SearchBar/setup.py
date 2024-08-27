from setuptools import setup

from freecad.search_bar.version import __version__

setup(
    name="freecad.search_bar",
    version=str(__version__),
    packages=["freecad", "freecad.search_bar"],
    maintainer="TODO",
    maintainer_email="TODO@foobar.com",
    url="https://foobar.com/me/coolWB",
    description="SearchBar does something cool.",
    install_requires=[],
    include_package_data=True,
)
