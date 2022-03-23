#
#   OwOBot Updater
#   Allows updating of OwOBot via Git easily.
#

import requests
import json
import os

version = 0

def checkForUpdate():