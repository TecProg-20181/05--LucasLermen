import unittest
import StringIO
import os
import subprocess
import re
import sys
from diskspace import diskspace

class DiskspaceTest(unittest.TestCase):

    def setUp(self):
        self.path = '/home/TecProg/Test'
        self.total_size = 6
        self.file_tree_node = {'print_size': '100.00Kb',
                               'children': [], 'size': self.total_size}
        self.file_tree = {self.path: self.file_tree_node}
        self.largest_size = 8

    def testOutputForCommand(self):
        command = 'ls'
        checkReturn = subprocess.check_output(command)
        self.assertEqual(diskspace.subprocess_check_output(command), checkReturn)

    def testBytesToReadable(self):
        blocksBytes = 0
        readable = diskspace.bytes_to_readable(blocksBytes)
        self.assertEqual(readable, '0.00B')

        blocksBytes = 1
        readable = diskspace.bytes_to_readable(blocksBytes)
        self.assertEqual(readable, '512.00B')

        blocksBytes = 200
        readable = diskspace.bytes_to_readable(blocksBytes)
        self.assertEqual(readable, '100.00Kb')

        blocksBytes = 491510
        readable = diskspace.bytes_to_readable(blocksBytes)
        self.assertEqual(readable, '240.00Mb')

    def testPrintTree(self):
        captured = StringIO.StringIO()
        sys.stdout = captured

        diskspace.print_tree(self.file_tree, self.file_tree_node, self.path,
                             self.largest_size, self.total_size)
        result = "100.00Kb  100%  {}\n".format(self.path)
        sys.stdout = sys.__stdout__
        self.assertEqual(result, captured.getvalue())



if __name__ == '__main__':
    unittest.main()
