import unittest

from  BeautifulReport import  BeautifulReport

from script.test_login import TestLogin

test_suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
