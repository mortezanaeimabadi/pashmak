#
# test_fread.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

''' The test '''

import random
import os
import tempfile
from TestCore import TestCore

class test_fread(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        rand = str(random.random())
        f = open(tempfile.gettempdir() + '/' + 'pashmak-test-file-' + rand, 'w')
        f.write('hello world')
        f.close()

        self.assert_output(
            self.run_without_error(
                ''' mem "''' + tempfile.gettempdir().replace('\\', '/') + '/' +\
                '''pashmak-test-file-<rand>"; fread ^; out ^; '''.replace('<rand>', rand)
            ),
            'hello world'
        )

        os.remove(tempfile.gettempdir() + '/' + 'pashmak-test-file-' + rand)
