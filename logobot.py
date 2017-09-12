
import os
import time
import argparse
from watermark import Watermark

def number_of_files(path):
    for root, dirs, files in os.walk(path):
        return len(files)

def run(input_path, marker, output, size=20, position="right_bottom"):
    n_of_files = number_of_files(input_path)
    while True:
        current_number_of_files = number_of_files(input_path)
        if current_number_of_files > n_of_files:
            watermark = Watermark(input_path, marker, output, size, position)
            watermark.run()
        n_of_files = current_number_of_files
        time.sleep(1)

if __name__ == "__main__":
    # Construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, help="Path to the input folder")
    ap.add_argument("-m", "--marker", required=True, help="Path to the marker file")
    ap.add_argument("-o", "--output", required=True, help="Path to the output folder")
    ap.add_argument("-s", "--size", type=int, default=20, help="Size of the marker in percentage")
    ap.add_argument("-p", "--position", type=str, default="right_bottom", help="Size of the marker in percentage")
    args = vars(ap.parse_args())

    run(args["input"], args["marker"], args["output"], args["size"], args["position"])
