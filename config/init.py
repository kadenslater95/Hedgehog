
import runpy
from dotenv import dotenv_values

ENV = dotenv_values(".env.local")

runpy.run_module("config/init.py")