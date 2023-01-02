import unittest
import os
import shutil
from naverLand import utils, config


class Test_1_utils(unittest.TestCase):

    def tearDown(self) -> None:
        shutil.rmtree(config.dir_gu)

    def test_1_make_dir(self):
        utils.make_dir(config.dir_gu)
        self.assertEqual(os.path.exists(config.dir_gu), True)

if __name__ == '__main__':
    unittest.main()


