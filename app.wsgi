#!/usr/bin/venv python
import sys
import site

site.addsitedir("/var/www/TIEA306_ohjelmointityo/venv/lib/python3.6/site-packages")

sys.path.insert(0, '/var/www/TIEA306_ohjelmointityo')

from application import create_app
application = create_app()

#if __name__ == "__main__":
        #application.run()