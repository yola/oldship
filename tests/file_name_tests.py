from datetime import datetime
from os import listdir
from os.path import dirname, isfile, join, realpath
from unittest import TestCase

PROOF_DIR = realpath(join(dirname(__file__), '../proof'))


class ProofFileNames(TestCase):
    def setUp(self):
        self.proof_files = [
            f for f in listdir(PROOF_DIR) if isfile(join(PROOF_DIR, f))]

    def assert_valid_file_name(self, name):
        """Raise AssertionError if name doesn't match YYYMMDD.ext format"""
        date = name.rpartition('.')[0]
        try:
            datetime.strptime(date, "%Y%m%d")
        except ValueError:
            self.fail("%s doesn't match required YYYMMDD.ext format" % name)

    def test_have_the_proper_format(self):
        [self.assert_valid_file_name(x) for x in self.proof_files]
