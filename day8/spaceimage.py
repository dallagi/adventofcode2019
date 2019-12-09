from collections import Counter

class SpaceImage:
    BLACK = 0
    WHITE = 1
    TRANSPARENT = 2

    def __init__(self, layers):
        self.layers = layers

    @classmethod
    def from_pixels(cls, pixels, width, height):
        layers_pixels = cls._chunks(pixels, width * height)

        layers = []
        for layer_pixels in layers_pixels:
            rows = cls._chunks(layer_pixels, width)
            layers.append([''.join(row) for row in rows])

        return cls(layers)

    def layer_with_fewest_zeros(self):
        zeroes_count = lambda layer: Counter(''.join(layer))['0']
        return sorted(self.layers, key=zeroes_count)[0]

    def merged_layers(self):
        merged = []
        for rows in zip(*self.layers):
            new_row = []
            for pixels in zip(*rows):
                visible_pixels = [p for p in pixels if int(p) != self.TRANSPARENT]
                new_row.append(visible_pixels[0])
            merged.append(''.join(new_row))
        return merged

    def show(self):
        return '\n'.join(self.merged_layers())\
                    .replace(str(self.WHITE), '█')\
                    .replace(str(self.BLACK), ' ')

    def checksum(self):
        checksum_layer_pixels = ''.join(self.layer_with_fewest_zeros())
        pixels_count = Counter(checksum_layer_pixels)

        return pixels_count["1"] * pixels_count["2"]
    
    @staticmethod
    def _chunks(lst, size):
        for index in range(0, len(lst), size):
            yield lst[index:index + size]


if __name__ == '__main__':
    pixels = open('input').read().strip()

    image = SpaceImage.from_pixels(pixels, 25, 6)
    print(f"Number of 1 digits multiplied by the number of 2 digits: {image.checksum()}")
    print(f"Image:\n{image.show()}")

