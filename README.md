# How to run the project
## 1. Clone this repository
## 2. Install the dependencies
### On Linux
```
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev   
```
### On Mac
```
brew install tesseract
```
### On Windows
Download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add \
```pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'``` to your script.
(Replace the path of tesseract binary if necessary). Check line 13 from ocr_model and change the path there to match 
your tesseract binary path. 

## 3. Download the chinese language data
For the Simplified Chinese language data, download the train data from 
https://github.com/tesseract-ocr/tessdata/blob/main/chi_sim.traineddata and place this file in the tessdata folder 
in your Tesseract-OCR directory.

## 4. Run the project
Open the project in your IDE and run the main.py file. 
The accuracy achieved by this model is 0.94 on the public data.
