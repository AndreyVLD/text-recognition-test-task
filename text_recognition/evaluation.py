from pathlib import Path
from ocr_model import OCRModel
from Levenshtein import distance
import numpy as np
import json


def text_accuracy(src, recognized):
    dist = distance(src, recognized)
    return 1 - dist / max(len(src), len(recognized))


def evaluate_model(model: OCRModel, dataset_path: Path, verbose=0):
    """
    Evaluate a given OCR model on a dataset.

    :param model: The OCRModel object to evaluate.
    :param dataset_path: The path to the dataset directory.
    :param verbose: Level of verbosity. 0 to print nothing, 1 to print only accuracy for each file,
     2 to print both accuracy and predicted/ground truth text. Default is 0.
    :return: The mean accuracy of the model.
    """
    with (dataset_path / 'info.json').open(encoding='utf-8') as f:
        dataset_info = json.load(f)
    accuracies = []
    for file_info in dataset_info:
        predicted_text = model.recognize_text(dataset_path / file_info['path'])
        accuracy = text_accuracy(file_info['text'], predicted_text)
        accuracies.append(accuracy)
        if verbose >= 1:
            print(file_info['path'], accuracy)
        if verbose >= 2:
            print(f'Predicted:\n\n'
                  f'"{predicted_text}"\n'
                  f'Ground truth:\n\n'
                  f'"{file_info["text"]}"\n')
    return np.mean(accuracies)
