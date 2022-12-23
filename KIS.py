import random
import csv, os
import numpy as np
from pathlib import Path
from numpy.linalg import norm
from matplotlib import pyplot as plt

class Embedding:
    def __init__(self, img, data, text=None, score=None):
        self.data = data
        self.score = score
        self.ID = str(Path(img).parts[-3:])
        self.img = img
        self.text = text

def Compare(q1, q2):
    return np.sum(np.dot(q1.data, q2.data) / (norm(q1.data) * norm(q2.data)))

def KISExperiment(CLIPimg, CLIPtxt, is_random=False):
    #set number of queries
    if is_random:
        numSample = 100
        sampleQueries = random.sample(CLIPtxt, numSample)
    else:
        numSample = len(CLIPtxt)
        sampleQueries = CLIPtxt
    ranking = []

    for i in range(0, numSample):
        q = sampleQueries[i]

        for img in CLIPimg:
            img.score = Compare(img, q)

        result = sorted(CLIPimg, key=lambda x: x.score, reverse=True)

        for k in range(len(result)):
            if result[k].ID == q.ID:
                ranking.append(k)
                break
    return ranking

def Parse_expert_Data(path):
    manual_text = []
    with open(path, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        #skip header
        next(reader, None)

        for row in reader:
            img = row[0]
            text = np.fromstring(row[1], sep=';')
            manual_text.append(Embedding(img, None, text))

    return manual_text

def Parse_Manual_Data(path, novice):
    img_embeddings = []
    manual_text_embeddings = []
    ClipCapText_embeddings = []
    with open(path, newline='') as f:
        reader = csv.reader(f, delimiter=';')
        #skip header
        next(reader, None)

        if novice:
            for row in reader:
                img = row[0]
                CLIP_img = np.fromstring(row[1], sep='|')
                ClipCap_text = row[2]
                CLIP_ClipCap = np.fromstring(row[3], sep='|')
                text = row[4]
                CLIP_text = np.fromstring(row[5], sep='|')

                img_embeddings.append(Embedding(img, CLIP_img))
                manual_text_embeddings.append(Embedding(img, CLIP_text, text))
                ClipCapText_embeddings.append(Embedding(img, CLIP_ClipCap, ClipCap_text))
            return img_embeddings, ClipCapText_embeddings, manual_text_embeddings
        else:
            for row in reader:
                img = row[0]
                text = row[1]
                CLIP_text = np.fromstring(row[2], sep='|')
                manual_text_embeddings.append(Embedding(img, CLIP_text, text))
            return manual_text_embeddings


def Parse_Dataset(path):
    img_embeddings = []
    text_embeddings = []
    folder_dirs = [os.path.join(path, folder) for folder in os.listdir(path)]
    for folder_dir in folder_dirs:
        dir = Path(folder_dir)

        for csv_dir in list(sorted(dir.glob("*.csv"))):
            with open(csv_dir, newline='') as f:
                reader = csv.reader(f, delimiter=';')
                # skip header
                next(reader, None)

                for row in reader:
                    img = row[0]
                    ClipCap_text = row[1]
                    CLIP_ClipCap = np.fromstring(row[2], sep='|')
                    CLIP_img = np.fromstring(row[3], sep='|')
                    img_embeddings.append(Embedding(img, CLIP_img))
                    text_embeddings.append(Embedding(img, CLIP_ClipCap, ClipCap_text))
    return img_embeddings, text_embeddings

if __name__ == '__main__':
    # load data
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    expert_descriptions = Parse_expert_Data(ROOT_DIR + "/data/manual_vs_ClipCap/100_expert_descriptions.csv")
    novice_img_embeddings, novice_ClipCapText_embeddings, novice_manual_embeddings = Parse_Manual_Data(ROOT_DIR + "/data/manual_vs_ClipCap/100_samples.csv", True)
    expert_manual_embeddings = Parse_Manual_Data(ROOT_DIR + "/data/manual_vs_ClipCap/expertQueriesCLIPfeatures.csv", False)

    img_dataset_embeddings, text_dataset_embeddings = Parse_Dataset(ROOT_DIR + "/data/extracted_low_res_images_v2")

    ClipCap_ranking = KISExperiment(img_dataset_embeddings, novice_ClipCapText_embeddings)
    novice_manual_ranking = KISExperiment(img_dataset_embeddings, novice_manual_embeddings)
    expert_manual_ranking = KISExperiment(img_dataset_embeddings, expert_manual_embeddings)

    #plot 2d
    plt.scatter(ClipCap_ranking, expert_manual_ranking)
    plt.xlabel("Rank for ClipCap query")
    plt.ylabel("Rank for manual novice query")
    plt.show()
