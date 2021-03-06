# Logo Bot

[![Build Status](https://travis-ci.org/kelvins/logo-bot.svg)](https://travis-ci.org/kelvins/logo-bot)
[![Coverage Status](https://coveralls.io/repos/github/kelvins/logo-bot/badge.svg?branch=master)](https://coveralls.io/github/kelvins/logo-bot?branch=master)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-green.svg)](https://www.python.org/dev/peps/pep-0008/)

A bot that automatically adds logos to your images. The bot looks for new images in a predefined folder (e.g. input). When it finds a new image, the bot adds a logo in a specific location (e.g. bottom-right) predefined by the user and saves it in an output folder. You can set up the logo location, the logo size (percentage, based on the image size) and the output type/format (e.g. png, jpg, etc).

This bot is very useful when you have a market place or something like that and needs to always add your logo to your images. You just need a minimal programming knowledge to download the source code and run the bot.

## Arguments

You can set the following parameters to the bot:

- **input**: path to the input folder where the images should be put. The default options is "./input/".
- **logo**: file path and name to the logo file. The default options is "./logo.png".
- **output**: path to the output folder where the images with the logo will be put. The default options is "./output/".
- **size**: the size of the logo. It is defined in percentage and calculated based on each image size. The default option is 20%. The range should be 1% - 100%.
- **position**: position where the logo will be added. The default option is **bottom_right**. You can use the following options:
	- **top_left**: Top left corner.
	- **top_center**: Top center.
	- **top_right**: Top right corner.
	- **center_right**: Center right.
	- **bottom_right**: Bottom right corner.
	- **bottom_center**: Bottom center.
	- **bottom_left**: Bottom left corner.
	- **center_left**: Center left.
	- **center**: Center.
- **type**: the type/format of the output images. The default option is **png**. Available options are: **png**, **jpeg** and **bmp**.

## Command to turn the bot on

You can use the following command to turn the bot on:

```
python logobot.py \
       --input ../input/ \
       --logo ../logo.png \
       --output ../output/ \
       --size 20 \
       --position bottom_right \
       --type png
```

The `logobot.py` file is inside the `src` directory.

To stop the bot just type 'q' or 'quit' and press Enter/Return.

## Example

|                  **Input**                |                   **Logo**                 |                 **Output**                 |
|:-----------------------------------------:|:------------------------------------------:|:------------------------------------------:|
| ![Input](https://i.imgur.com/HHqvE4o.jpg) |  ![Logo](https://i.imgur.com/qn284gD.png)  | ![Output](https://i.imgur.com/tAseG81.jpg) |
| ![Input](https://i.imgur.com/Wq2g7IV.png) |  ![Logo](https://i.imgur.com/qn284gD.png)  | ![Output](https://i.imgur.com/p2kjF87.png) |
| ![Input](https://i.imgur.com/Lk0yqmv.jpg) |  ![Logo](https://i.imgur.com/qn284gD.png)  | ![Output](https://i.imgur.com/JeiEi3Y.png) |

## Contributing

This project was created under the [MIT license][1].
Feel free to contribute by commenting, suggesting, creating issues or sending pull requests.

 [1]: LICENSE
