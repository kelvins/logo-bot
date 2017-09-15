
import os
import time
import argparse
from logo import Logo


class LogoBot(object):

    def __init__(self, logo_object):
        self.logo_object = logo_object

    @staticmethod
    def number_of_files(path):
        for root, dirs, files in os.walk(path):
            return len(files)
        return 0

    def run(self):
        n_of_files = self.number_of_files(self.logo_object.input_folder)
        while True:
            current_number_of_files = self.number_of_files(self.logo_object.input_folder)
            if current_number_of_files > n_of_files:
                self.logo_object.add()
            n_of_files = current_number_of_files
            time.sleep(1)

if __name__ == "__main__":
    # Construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to the input folder")
    ap.add_argument("-l", "--logo", required=True, help="Path to the logo file")
    ap.add_argument("-o", "--output", required=True, help="Path to the output folder")
    ap.add_argument("-s", "--size", type=int, default=20, help="Size of the marker in percentage")
    ap.add_argument("-p", "--position", type=str, default="right_bottom", help="Size of the marker in percentage")
    ap.add_argument("-t", "--type", type=str, default="png", help="The type of the output images")
    args = vars(ap.parse_args())

    logo = Logo(args["input"], args["logo"], args["output"], args["size"], args["position"], args["type"])
    logo_bot = LogoBot(logo)
    logo_bot.run()
