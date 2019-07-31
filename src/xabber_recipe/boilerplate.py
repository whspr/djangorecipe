WSGI_TEMPLATE = """

%(relative_paths_setup)s

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path[0:0] = [
  BASE_DIR + %(path)s,
  BASE_DIR,
  ]
%(initialization)s
import %(module_name)s

application = %(module_name)s.%(attrs)s(%(arguments)s)
"""
