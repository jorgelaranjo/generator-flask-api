#! /usr/bin/env python

import os

from <%= appName %> import create_app


app = create_app(os.getenv('<%= appEnvVar %>_CONFIG', 'default'))


if __name__ == '__main__':
    app.run()
