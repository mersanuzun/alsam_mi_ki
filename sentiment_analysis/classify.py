#!/usr/bin/python
# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier
import codecs

train_data = [("bu ürün çok güzel".decode('utf8'), 'pos'),
              ('çok memnunum'.decode('utf8'), 'pos'),
              ('Çok uygun fiyata çok güzel ürün'.decode('utf8'), 'pos'),
              ('Tek kelimeyle harika', 'pos'),
              ('beğenmedim'.decode('utf-8'), 'neg'),
              ('hiç iyi bir ürün değil'.decode('utf8'), 'neg'),
              ('almayın bence'.decode('utf-8'), 'neg')]

reviews = []
with open('../scraping_reviews/pos.txt') as file: 
   for line in file:
       reviews.append((line.decode('utf8'), "pos"))
with open('../scraping_reviews/neg.txt') as file:
   for line in file:
       reviews.append((line.decode('utf8'), 'neg'))
print reviews[len(reviews) - 2]

cl = NaiveBayesClassifier(reviews)
print cl.classify('ürünü gerçekten beğenmedim'.decode('utf8'))

