#!/usr/bin/env python
from os import getcwd, listdir, path
from re import subn, DOTALL, MULTILINE

def get_pieces(site_dir):
    pieces = {}
    contents = listdir(site_dir)
    for filename in filter(lambda n: n.endswith('.html'), contents):
        name = filename.split('.html')[0]
        with open(path.join(site_dir, filename)) as f:
            content = f.read().strip()
            pieces[name] = content
    return pieces

def indent(text, spacer):
    spaced = text.replace('\n', '\n{}'.format(spacer))
    return '{}{}'.format(spacer, spaced)

def inject(file_path, pieces):
    parts_injected = []
    def replacer(match):
        original = match.group()
        parts = match.groupdict()
        name = parts['name']
        spacing = parts['spacing']
        try:
            site_content = pieces[name]
        except KeyError:
            from sys import stderr
            stderr.write('Warning: no template: "{}" ({})\n'.format(name, file_path))
            return original
        updated = indent('<!--site:{0}-->\n{1}\n<!--/site:{0}-->'.format(name, site_content), spacing)
        if updated != original:
            parts_injected.append(name)
        return updated
    with open(file_path, 'r') as f:
        content = f.read()
    (injected, n) = subn(r'(?P<spacing>[ \t]*)<!--site\:(?P<name>.*?)-->\n(?P<old_content>.*?)\s*<!--/site\:(?P=name)-->', replacer, content, 0, MULTILINE | DOTALL)
    if n == 0 or len(parts_injected) == 0:  # no content injected
        return
    with open(file_path, 'w') as f:
        f.write(injected)
    print('{}: {}'.format(file_path, ', '.join(parts_injected)))

def inject_files(pieces, dirname, fnames):
    to_exclude = filter(lambda n: n.startswith('.') or n.startswith('_'), fnames);
    for name in to_exclude:
        fnames.remove(name)
    for name in filter(lambda n: n.endswith('.html'), fnames):
        inject(path.join(dirname, name), pieces)

if __name__ == '__main__':
    here = getcwd()
    pieces = get_pieces(path.join(here, '_site'))
    path.walk(here, inject_files, pieces)
