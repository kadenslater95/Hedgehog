# This file is for running whatever initialization is needed, e.g. database setup, etc.

import runpy

runpy.run_module("config/database.py")