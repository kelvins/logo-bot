# Logo Bot

A bot that automatically adds logos to your images. The bot looks for new images in a predefined folder (e.g. input). When it finds a new image, the bot adds a logo in a specific location (e.g. bottom-right) predefined by the user and saves it in an output folder. You can set up the logo location, the logo size (percentage, based on the image size) and the output type/format (e.g. png, jpg, etc).

This bot is very useful when you have a market place or something like that and needs to always add your logo to your images. You just need a minimal programming knowledge to download the source code and run the bot.

## Arguments

You can set the following parameters to the bot:

- **input**: path to the input folder where the images should be put.
- **logo**: file path and name to the logo file.
- **output**: path to the output folder where the images with the logo will be put.
- **size**: the size of the logo. It is defined in percentage and calculated based on each image size. The default option is 30%. The range should be 1% - 100%.
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
python /Users/kelvinsp/Github/logo-bot/src/logobot.py \
       --input /Users/kelvinsp/Github/logo-bot/tests/input/ \
       --logo /Users/kelvinsp/Github/logo-bot/tests/logo.png \
       --output /Users/kelvinsp/Github/logo-bot/tests/output/ \
       --size 20 \
       --position bottom_right \
       --type png
```

Just change the paths to the project location on your computer.

## Command to run the tests

python -m unittest discover -s /Users/kelvinsp/Github/logo-bot/tests/ -p '*_test.py'

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