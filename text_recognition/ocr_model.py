from pathlib import Path
import cv2
import numpy as np
import pytesseract
import os

# Try to get the Tesseract path from the environment variable
tesseract_path = os.getenv('TESSERACT_PATH')

# Set the path to the tesseract executable, if necessary, change it to your path
# Follow this format: pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
if not tesseract_path:
    tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = tesseract_path


class OCRModel:

    def preprocess_image(self, image: Path) -> np.ndarray:
        """
        Preprocess the input image by converting it to grayscale and applying thresholding.

        :param image: Path to the input image file.
        :return: Preprocessed image as a NumPy array.
        """
        # Loading the image from the file path
        img = cv2.imread(str(image))

        # Convert the image to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Apply thresholding
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # Apply Gaussian blur and equalize histogram
        img = cv2.GaussianBlur(img, (3, 3), 0)
        img = cv2.equalizeHist(img)

        return img

    def recognize_text(self, image: Path) -> str:
        """
        Recognize text from the input image using Tesseract OCR.

        :param image: Path to the input image file.
        :return: The recognized text.
        """

        # Preprocess the image
        preprocessed_image = self.preprocess_image(image)

        # Use tesseract to recognize text
        my_config = r'--oem 3 --psm 6 -l eng+chi_sim -c preserve_interword_spaces=1'
        extracted_text = pytesseract.image_to_string(preprocessed_image, config=my_config)
        return extracted_text.strip()
