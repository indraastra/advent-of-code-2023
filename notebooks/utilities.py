import functools
import operator
import re
from typing import Iterable

NUMBER_RE = re.compile(r'(\d+)')

def extract_ints(s: str):
  """
  >>> extract_ints('')
  []
  >>> extract_ints('83 86  6 31 17  9 48 53')
  [83, 86, 6, 31, 17, 9, 48, 53]
  """
  return [int(m) for m in NUMBER_RE.findall(s)]


def product_ints(values: Iterable[int]):
  """
  >>> product_ints([6, 13, 20]
  1560
  >>> product_ints([])
  1
  """
  return functools.reduce(operator.mul, values, 1)
