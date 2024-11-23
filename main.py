# This file is the main module which runs init to set everything up, and then boots the server, etc.

import runpy

from starlite import Starlite

from controllers.user import UserController

runpy.run_module("config/init.py")

app = Starlite(route_handlers=[UserController])