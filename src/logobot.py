
import os
import time
import argparse
from threading import Thread
from logo import Logo


class LogoBot(Thread):

    def __init__(self, logo_object):
        Thread.__init__(self)
        self.logo_object = logo_object
        self.stopped = False

    def stop(self):
        self.stopped = True

    def run(self):
        n_of_files = len(os.listdir(self.logo_object.input_folder))
        self.logo_object.add()

        while True:
            current_number_of_files = len(os.listdir(self.logo_object.input_folder))
            if current_number_of_files > n_of_files:
                self.logo_object.add()
            n_of_files = current_number_of_files
            time.sleep(1)

            # If the stopped flag is true, break it
            if self.stopped:
                break

if __name__ == "__main__":
    # Construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", type=str, default="./input/", help="Path to the input folder")
    ap.add_argument("-l", "--logo", type=str, default="./logo.png", help="Path to the logo file")
    ap.add_argument("-o", "--output", type=str, default="./output/", help="Path to the output folder")
    ap.add_argument("-s", "--size", type=int, default=20, help="Size of the marker in percentage")
    ap.add_argument("-p", "--position", type=str, default="bottom_right", help="Size of the marker in percentage")
    ap.add_argument("-t", "--type", type=str, default="png", help="The type of the output images")
    args = vars(ap.parse_args())

    logo = Logo(args["input"], args["logo"], args["output"], args["size"], args["position"], args["type"])
    logo_bot = LogoBot(logo)
    logo_bot.start()

    print("I'm watching the input folder...")

    while True:
        print("If you type q or quit and press Enter/Return I will stop")
        op = raw_input()
        if op == "q" or op == "quit":
            print("Please wait, I'm turning off...")
            logo_bot.stop()
            break

    print("Bye Bye")

