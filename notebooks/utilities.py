import re

NUMBER_RE = re.compile(r'(\d+)')

def extract_ints(s: str):
  return [int(m) for m in NUMBER_RE.findall(s)]
