import unittest
from spaceimage import SpaceImage

class TestSpaceImage(unittest.TestCase):
    def test_image_from_pixels(self):
        pixels = '123456789012'
        
        image = SpaceImage.from_pixels(pixels, 3, 2)
        self.assertEqual(image.layers, [['123', '456'], ['789', '012']])

    def test_layer_with_fewer_zeroes(self):
        pixels = '123456789002'

        image = SpaceImage.from_pixels(pixels, 3, 2)
        self.assertEqual(image.layer_with_fewest_zeros(), ['123', '456'])

    def test_checksum(self):
        pixels = '112223'

        image = SpaceImage.from_pixels(pixels, 3, 2)
        self.assertEqual(image.checksum(), 2 * 3)

    def test_merged_layers(self):
        pixels = '0222112222120000'

        image = SpaceImage.from_pixels(pixels, 2, 2)
        self.assertEqual(image.merged_layers(), ['01', '10'])

if __name__ == '__main__':
    unittest.main()
