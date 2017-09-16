
import os
import sys
from PIL import Image
from progressbar import ProgressBar


class Logo(object):

    __valid_positions = ["top_left", "top_center", "top_right",
                         "center_right", "bottom_right", "bottom_center",
                         "bottom_left", "center_left", "center"]

    __valid_image_types = ["png", "jpg", "jpeg", "bmp"]

    def __init__(self, input_folder, logo_filename, output_folder, size, position, output_type):
        """
        The init function from the Logo class is used only to get the arguments.
        :param input_folder: path to the input folder
        :param logo_filename: path and filename to the logo file
        :param output_folder: path to the output folder
        :param size: size of the logo (percentage)
        :param position: position in the image
        :param output_type: type of the output image
        """

        if os.path.exists(input_folder):
            self.input_folder = input_folder
        else:
            sys.exit("Invalid input path")

        if os.path.exists(logo_filename):
            self.logo_filename = logo_filename
        else:
            sys.exit("Invalid logo path")

        if os.path.exists(output_folder):
            self.output_folder = output_folder
        else:
            sys.exit("Invalid output path")

        if size <= 0:
            self.size = 1
        elif size > 100:
            self.size = 100
        else:
            self.size = size

        if position in self.__valid_positions:
            self.position = position
        else:
            self.position = "right_bottom"

        if output_type in self.__valid_image_types:
            self.output_type = output_type
        else:
            self.output_type = "png"

    def calc_size(self, image_size, logo_size):
        """
        Calculates the logo size based on the image size.
        :param image_size: The size (width and height) of the image.
        :param logo_size: The size of the logo (width and height).
        :return: The new size (width and height).
        """

        image_width, image_height = image_size
        logo_width, logo_height = logo_size

        if image_width <= 0 or image_height <= 0:
            return 0, 0
        if logo_width <= 0 or logo_height <= 0:
            return 0, 0

        if logo_width < logo_height:
            new_height = int(image_height * self.size / 100.0)
            percentage = (logo_width * 100.0) / logo_height
            new_width = int(new_height * percentage / 100.0)
        else:
            new_width = int(image_width * self.size / 100.0)
            percentage = (logo_height * 100.0) / logo_width
            new_height = int(new_width * percentage / 100.0)

        return new_width, new_height

    def calc_position(self, image_size, logo_size):
        """
        Calculates the position where the logo must be add.
        :param image_size: The size (width and height) of the image.
        :param logo_size: The size of the logo (width and height).
        :return: The position (x and y) where the logo must be add.
        """

        image_width, image_height = image_size
        logo_width, logo_height = logo_size

        if image_width <= 0 or image_height <= 0:
            return 0, 0
        if logo_width <= 0 or logo_height <= 0:
            return 0, 0

        # Bottom right
        pos_x = image_width - logo_width
        pos_y = image_height - logo_height

        if self.position == "top_left":
            pos_x = 0
            pos_y = 0
        elif self.position == "top_center":
            pos_x = (image_width/2) - (logo_width/2)
            pos_y = 0
        elif self.position == "top_right":
            pos_x = image_width - logo_width
            pos_y = 0
        elif self.position == "center_right":
            pos_x = image_width - logo_width
            pos_y = (image_height/2) - (logo_height/2)
        elif self.position == "bottom_center":
            pos_x = (image_width/2) - (logo_width/2)
            pos_y = image_height - logo_height
        elif self.position == "bottom_left":
            pos_x = 0
            pos_y = image_height - logo_height
        elif self.position == "center_left":
            pos_x = 0
            pos_y = (image_height/2) - (logo_height/2)
        elif self.position == "center":
            pos_x = (image_width/2) - (logo_width/2)
            pos_y = (image_height/2) - (logo_height/2)

        return pos_x, pos_y

    def add(self):

        img_number = 0

        # Load the original logo image
        original_logo = Image.open(self.logo_filename)

        for dirname, dirnames, filenames in os.walk(self.input_folder):

            total = len(filenames)-1

            # Initialize the progress bar
            progress_bar = ProgressBar(total)
            progress_bar.update(0)

            for filename in filenames:
                # Extract the image type/format
                image_type = filename.split(".")
                image_type = image_type[len(image_type)-1]

                if image_type in self.__valid_image_types:
                    # Load the image
                    temp_path = os.path.join(dirname, filename)
                    image = Image.open(temp_path)

                    # Get a copy of the original logo
                    logo = original_logo

                    # Calculate the new logo size
                    width, height = self.calc_size(image.size, logo.size)

                    logo = logo.resize((width, height), Image.LANCZOS)

                    pos_x, pos_y = self.calc_position(image.size, logo.size)

                    image.paste(logo, (pos_x, pos_y), mask=logo)

                    # Creates a new filename removing the old image format
                    new_filename = filename.split(".")
                    new_filename = "".join(new_filename[:len(new_filename)-1])
                    image.save(self.output_folder + new_filename + "." + self.output_type)

                    img_number += 1
                    progress_bar.update(img_number)

            # Set the progress bar to 100% and break the loop
            progress_bar.update(total)
            break
