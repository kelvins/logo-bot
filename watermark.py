import os
import argparse
from PIL import Image
from progressbar import ProgressBar


class Watermark(object):

    def __init__(self, input, marker, output, size=20, position="right_bottom", type="png"):
        self.input = input
        self.marker = marker
        self.output = output
        self.size = size
        self.position = position
        self.type = type;

    def calc_size(self, width, height):
        if width < height:
            return (self.size * width) / 100.0
        return (self.size * height) / 100.0

    def calc_position(self, width, height, size):
        if self.position == "left_top":
            return 0, 0
        elif self.position == "right_top":
            return width-size, 0
        elif self.position == "left_bottom":
            return 0, height-size
        else:
            return width-size, height-size

    def run(self):
        img_number = 0
        for dirname, dirnames, filenames in os.walk(self.input):

            # Initialize the progress bar
            progress_bar = ProgressBar(len(filenames)-1)
            progress_bar.update(0)

            for filename in filenames:
                ext = filename.split(".")
                ext = ext[len(ext)-1]
                if ext in ["png", "jpg", "jpeg"]:
                    temp_path = os.path.join(dirname, filename)
                    image = Image.open(temp_path)

                    width, height = image.size
                    size = int(self.calc_size(width, height))

                    marker = Image.open(self.marker)

                    marker = marker.resize((size, size), Image.LANCZOS)

                    pos_x, pos_y = self.calc_position(width, height, size)

                    image.paste(marker, (pos_x, pos_y), mask=marker)

                    image.save(self.output + filename + ".jpeg")

                    img_number += 1
                    progress_bar.update(img_number)

if __name__ == "__main__":
    # Construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to the input folder")
    ap.add_argument("-m", "--marker", required=True, help="Path to the marker file")
    ap.add_argument("-o", "--output", required=True, help="Path to the output folder")
    ap.add_argument("-s", "--size", type=int, default=20, help="Size of the marker in percentage")
    ap.add_argument("-p", "--position", type=str, default="right_bottom", help="Size of the marker in percentage")
    ap.add_argument("-t", "--type", type=str, default="png", help="The type of the output images")
    args = vars(ap.parse_args())

    watermark = Watermark(args["input"], args["marker"], args["output"], args["size"], args["position"], args["type"])
    watermark.run()
