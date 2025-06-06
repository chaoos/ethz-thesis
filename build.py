#! /usr/bin/env python3
"""
TODO
"""

import argparse, re
import boolean, shutil

def uncomment(string):
  return string[1:] if string.startswith("%") else string

def comment(string):
  return string if string.startswith("%") else f"%{string}"

def symbol2str(symbol):
  return repr(symbol.obj)[1:-1]

def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('parts', nargs='*', default=["all"], help='Parts to build.')
  parser.add_argument('-t', '--thesis', nargs='+', default="thesis.tex", help='Main thesis.tex file.')
  parser.add_argument('-l', '--list', action='store_true', help='List all possible parts.')
  args = parser.parse_args()

  # omit these if args.parts == "all"
  omit_in_all = ["deprecated"]

  algebra = boolean.BooleanAlgebra()
  true, false = algebra.TRUE, algebra.FALSE
  pattern = r"\%\ PYTHON\:\ (.+)"
  p = re.compile(pattern)
  linenos = []

  if args.list:
    args.parts = ["all"]

  symbols = set()
  with open(args.thesis, "r+") as fh:
    data = fh.readlines()
    for i, line in enumerate(data):
      if (m := p.search(line)):
        expr = m.group(1)
        try:
          parse = algebra.parse(expr)
          eval_symbols = {s: true if str(s) in args.parts else false for s in parse.symbols}
          result = parse.subs(eval_symbols)
          omit = bool([s for s in omit_in_all if s in map(symbol2str, parse.symbols)])
          linenos.append((i, result.simplify() == true or ("all" in args.parts and not omit)))
          symbols.update(parse.symbols)
        except boolean.ParseError:
          print(f"Parse error at line {i}")
          raise

  if args.list:
    print(f"The list of valid parts is:")
    symbols = ", ".join(sorted(map(symbol2str, symbols)))
    print(symbols)
    return

  for part in args.parts:
    if part not in map(symbol2str, symbols) and part != "all":
      raise ValueError(f"{part = } not found in {args.thesis}. Use --list for a list of valid symbols.")

  for ls, build in linenos:
    le = ls
    while data[le] != "\n":
      le += 1

    for i in range(ls+1, le):
      data[i] = uncomment(data[i]) if build else comment(data[i])

  shutil.copyfile(args.thesis, f"{args.thesis}.bak")

  with open(args.thesis, 'w') as fh:
    for d in data:
      fh.write(d)

if __name__ == '__main__':
  main()

