#!/usr/bin/env python

from flask_script import Manager

from liedown import create_app


manager = Manager(create_app)


if __name__ == '__main__':
    manager.run()
