from pathlib import Path

from text_recognition.ocr_model import OCRModel
from text_recognition.evaluation import evaluate_model


def main():
    model = OCRModel()
    data_path = Path(__file__).parent.parent / 'data' / 'public_data'
    accuracy = evaluate_model(model, data_path, verbose=2)
    print(f'Final accuracy is {accuracy:.3f}')


if __name__ == '__main__':
    main()
