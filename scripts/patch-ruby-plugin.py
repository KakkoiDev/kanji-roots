"""
patch-ruby-plugin.py — Fix mkdocs-ruby-plugin's overly broad single-char regex.

The original regex `(.)\((.+?)\)` matches ANY character before `(reading)`,
which causes false positives on English text. This patch restricts the
match to CJK kanji characters only.
"""

import os
import mkdocs_ruby_plugin.plugin as plugin_mod

OLD = r"rf'(.)\{self.config.inter_begin}(.+?)\{self.config.inter_end}'"
NEW = r"rf'([\u4e00-\u9fff\u3400-\u4dbf])\{self.config.inter_begin}(.+?)\{self.config.inter_end}'"

path = plugin_mod.__file__
with open(path) as f:
    src = f.read()

if OLD in src:
    src = src.replace(OLD, NEW)
    with open(path, 'w') as f:
        f.write(src)
    print(f"Patched: {path}")
else:
    if NEW in src:
        print(f"Already patched: {path}")
    else:
        print(f"WARNING: Pattern not found in {path}")
