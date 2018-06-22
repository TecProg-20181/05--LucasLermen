import unittest
import os
import subprocess
import re
from diskspace import diskspace

class DiskspaceTest(unittest.TestCase):

    def setUp(self):
        self.command = 'ls'

    def testOutputForCommand(self):
        checkReturn = subprocess.check_output(self.command)
        self.assertEqual(diskspace.subprocess_check_output(self.command), checkReturn)

    def testBytesToReadable(self):
        blocksBytes= 1
        self.assertEqual(diskspace.bytes_to_readable(blocksBytes), '512.00B')



if __name__ == '__main__':
    unittest.main()
