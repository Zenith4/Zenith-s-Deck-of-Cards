import pathlib
from setuptools import setup
HERE = pathlib.Path(__file__).parent
setup(
    name="zenith_deck_of_cards",
    version="1.0.1",
    description="Deck and card classes",
    packages=["zenith_deck"],
)