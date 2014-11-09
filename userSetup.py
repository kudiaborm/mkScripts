import pymel.core as pm
import os

import sys
import pymel.core as pm
import getpass

import mkCore

user = getpass.getuser()
sys.dont_write_bytecode = True

__Red9__ = '/home/{0}/Documents/Red9_StudioPack-1.44'.format(user)
__lib__ = '/home/{0}/maya/scripts/mkCore/lib/site-packages'.format(user)
__plugins__ = '/home/{0}/maya/2015-x64/plug-ins'.format(user)

if __Red9__ not in sys.path:
    sys.path.append(__Red9__)
if __lib__ not in sys.path:
    sys.path.append(__lib__)

if os.environ.get('MAYA_PLUG_IN_PATH').find(__plugins__) == -1:
    os.environ['MAYA_PLUG_IN_PATH'] += "{0}{1}".format(os.pathsep,__plugins__)

import Red9
Red9.start()

