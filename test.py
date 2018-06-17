import unittest

#from diskspace.diskspace import diskspace

class SubprocessCheckOutputTest(unittest.TestCase):

    def testOutputForCommand(self):
        command = 'output test'
        output = diskspace.subprocess_check_output(command)
        self.assertEqual('test\n', output)

suite = unittest.TestLoader().loadTestsFromTestCase(SubprocessCheckOutputTest)
unittest.TextTestRunner(verbosity=3).run(suite)
