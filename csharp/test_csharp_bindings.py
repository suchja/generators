#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
C# Bindings Tester
Copyright (C) 2012-2014 Matthias Bolte <matthias@tinkerforge.com>

test_csharp_bindings.py: Tests the C# bindings

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

import sys
import os
import subprocess
import shutil

sys.path.append(os.path.split(os.getcwd())[0])
import common

class CSharpExamplesTester(common.ExamplesTester):
    def __init__(self, path, extra_examples):
        common.ExamplesTester.__init__(self, 'csharp', '.cs', path, extra_examples=extra_examples)

    def test(self, cookie, src, is_extra_example):
        if is_extra_example:
            shutil.copy(src, '/tmp/tester/csharp')
            src = os.path.join('/tmp/tester/csharp', os.path.split(src)[1])

        dest = src[:-3] + '.exe';

        args = ['/usr/bin/gmcs',
                '/warn:4',
                '/optimize',
                '/target:exe',
                '/out:' + dest,
                '/reference:/tmp/tester/csharp/Tinkerforge.dll',
                src]

        self.execute(cookie, args)

def run(path):
    extra_examples = [os.path.join(path, '../../weather-station/button_control/csharp/WeatherStationButton.cs'),
                      os.path.join(path, '../../weather-station/write_to_lcd/csharp/WeatherStation.cs'),
                      os.path.join(path, '../../hardware-hacking/remote_switch/csharp/RemoteSwitch.cs'),
                      os.path.join(path, '../../hardware-hacking/smoke_detector/csharp/SmokeDetector.cs')]

    return CSharpExamplesTester(path, extra_examples).run()

if __name__ == "__main__":
    sys.exit(run(os.getcwd()))
