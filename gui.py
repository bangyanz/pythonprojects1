# Start with some imports!

from __future__ import print_function
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


def f(x):
    return x


interact(f, x=5)
