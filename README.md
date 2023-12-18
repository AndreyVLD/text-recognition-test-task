# Instructions

- Your goal is to implement a model using any python library
that will recognize the text from the picture as accurate as possible.

- The dataset contained in `data/public_data` consist of images with English/Chinese texts
and `info.json` file with all ground truth texts.

- You should implement class located in `ocr_model.py`. Feel free to write any code you want,
but keep in mind that the model should match `OCRModel` interface, so I will be able to easily test it.
You can check your recognition quality on public data with `main.py` script.

- Your grade would depend on both the accuracy of your model
and the quality of your code.

  -  To measure your accuracy I will download your fork and 
run your model on the secret version of dataset (with another, but conceptually similar screenshots).
