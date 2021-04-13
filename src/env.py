import toml
import os
import pygame


def load_config(filename: str = os.path.relpath("config.toml")):
    with open(filename, "r") as fh:
        return toml.load(fh)


CONFIG = load_config()
