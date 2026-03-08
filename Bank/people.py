from dataclasses import dataclass
from accounts import *

@dataclass
class People:
    age : int
    name : str

@dataclass
class Client(People):
    account : Account | None = None
