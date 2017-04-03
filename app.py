#!/usr/bin/env python

import os

from bottle import abort, get, redirect, run

directory = os.path.join(os.path.dirname(__file__), 'links')


@get('/<path:path>')
def get_path(path):
    try:
        with open(os.path.join(directory, path)) as f:
            redirect(f.read().strip())
    except FileNotFoundError:
        abort(404, 'Not found: %r' % path)


if __name__ == "__main__":
    run()
