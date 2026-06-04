#!/usr/bin/env python3

# Copy an SVG, replacing hex color substrings, to inject the `accent` build
# option into the rendered PNG assets without mutating the source SVG.
# Usage: recolor-svg.py <input.svg> <output.svg> old=new [old=new ...]

import sys


def main():
    src, dst, *pairs = sys.argv[1:]
    text = open(src, encoding='utf-8').read()
    for pair in pairs:
        old, new = pair.split('=', 1)
        text = text.replace(old, new)
    with open(dst, 'w', encoding='utf-8') as out:
        out.write(text)


main()
