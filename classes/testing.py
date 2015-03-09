"""
Configuration and requirements testing


Released under the MIT license
Copyright (c) 2012, Jason Millward

@category   misc
@version    $Id: 1.7-testing, 2015-03-09 21:25:58 ACDT $;
@author     Jason Millward <jason@jcode.me>
@license    http://opensource.org/licenses/MIT
"""

import sys
import os
import subprocess


def perform_testing(config):

    requirements = {
        "MakeMKV":   "makemkvcon",
        "Filebot":   "filebot",
        "HandBrake": "HandBrakeCLI",
        "FFmpeg (optional)": "ffmpeg"
    }

    print "= Checking directory permissions"
    print canwrite(config['makemkv']['savePath']), "MakeMKV savePath"

    print ""
    print "= Checking requirements"
    for req in requirements:
        print checkcommand(requirements[req]), req

    sys.exit(0)


def canwrite(path):
    try:
        ret = booltostatus(os.access(path, os.W_OK | os.X_OK))
    except:
        ret = False
    finally:
        return ret


def booltostatus(inbool):
    if inbool:
        return "[  OK  ]"
    else:
        return "[ FAIL ]"


def checkcommand(com):
    proc = subprocess.Popen(
        [
            'which',
            str(com)
        ],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE
    )
    return booltostatus(len(proc.stdout.read()) > 0)