from textblob.classifiers import NaiveBayesClassifier

train_data = [('bu urun cok guzel', 'pos'),
              ('cok memnunum', 'pos'),
              ('Cok uygun fiyata cok guzel urun', 'pos'),
              ('Tek kelimeyle harika', 'pos'),
              ('begenmedim', 'neg'),
              ('hic iyi bir urun degil', 'neg'),
              ('almayin bence', 'neg')]

cl = NaiveBayesClassifier(train_data)
print cl.classify('guzel') # pos
print cl.classify('almayin') #neg
