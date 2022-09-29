from gensim.utils import simple_preprocess
from gensim import corpora
from smart_open import smart_open
import os
from collections import defaultdict, Counter
from tqdm import tqdm
import pandas as pd

if __name__ == "__main__":

    bel_letters = [
        "а",
        "б",
        "в",
        "г",
        "д",
        "е",
        "ё",
        "ж",
        "з",
        "і",
        "й",
        "к",
        "л",
        "м",
        "н",
        "о",
        "п",
        "р",
        "с",
        "т",
        "у",
        "ў",
        "ф",
        "х",
        "ц",
        "ч",
        "ш",
        "ы",
        "ь",
        "э",
        "ю",
        "я",
    ]
    if os.path.isfile("dictionary.dict"):
        print("Loading a gensim dictionary...")
        dictionary = corpora.Dictionary.load("dictionary.dict")
    else:
        print("Creating a gensim dictionary...")
        dictionary = corpora.Dictionary(
            simple_preprocess(line, deacc=False)
            for line in tqdm(open("wiki_bel.txt", encoding="utf-8"))
        )
        dictionary.save("dictionary.dict")
    print("Calculating stats...")
    a_dict = defaultdict(list, {k: [] for k in bel_letters})
    for key in tqdm(dictionary.token2id):
        for i, c in enumerate(key):
            if c in a_dict:
                a_dict[c].append(i)

a_dict_compressed = {}
for key in a_dict.keys():
    a_dict_compressed[key] = Counter(a_dict[key])
df = pd.DataFrame.from_dict(a_dict_compressed)
df.to_csv("bel_letters.csv")
