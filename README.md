# Logo Bot

A bot that adds a logo to your images. The bot looks for new images in a predefined folder (e.g. input). When it finds a new image, the bot adds a logo in a specific location (e.g. bottom-right) predefined by the user and saves it in an output folder.

## Arguments

The user can set some parameters to the bot when running it:

- **input**: input folder where the images should be put.
- **logo**: path to the logo file.
- **output**: output folder where the images with the logo will be put.
- **size**: the size of the logo. It is defined in percentage and the logo size is calculated based on each image size (default is 30%).
- **position**: position where the logo will be added (default is bottom_right).
- **type**: the type/format of the output images (default is png).

## Command to put the bot running

```
python /Users/kelvinsp/Github/logo-bot/src/logobot.py \
       --input /Users/kelvinsp/Github/logo-bot/tests/input/ \
       --logo /Users/kelvinsp/Github/logo-bot/tests/logo.png \
       --output /Users/kelvinsp/Github/logo-bot/tests/output/ \
       --size 20 \
       --position bottom_right \
       --type png
```

## Example

|                  **Input**                |                   **Logo**                 |                 **Output**                 |
|:-----------------------------------------:|:------------------------------------------:|:------------------------------------------:|
| ![Input](https://i.imgur.com/HHqvE4o.jpg) |  ![Logo](https://i.imgur.com/qn284gD.png)  | ![Output](https://i.imgur.com/tAseG81.jpg) |
| ![Input](https://i.imgur.com/Wq2g7IV.png) |  ![Logo](https://i.imgur.com/qn284gD.png)  | ![Output](https://i.imgur.com/p2kjF87.png) |
| ![Input](https://i.imgur.com/Lk0yqmv.jpg) |  ![Logo](https://i.imgur.com/qn284gD.png)  | ![Output](https://i.imgur.com/JeiEi3Y.png) |
