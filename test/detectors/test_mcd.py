import unittest
from test.helpers import ClassificationModel, SegmentationModel

import torch

from pytorch_ood.detector import MCD


class TestMCD(unittest.TestCase):
    """
    Tests for Monte Carlo Dropout
    """

    def test_something(self):
        model = ClassificationModel()
        mcd = MCD(model)

        x = torch.zeros(size=(1, 10))
        y = mcd.predict(x)
        self.assertIsNotNone(y)

    def test_segmentation(self):
        model = SegmentationModel()
        mcd = MCD(model)

        x = torch.zeros(size=(4, 3, 32, 32))
        y = mcd.predict(x)
        self.assertIsNotNone(y)
        self.assertEqual(y.shape, (4, 32, 32))
