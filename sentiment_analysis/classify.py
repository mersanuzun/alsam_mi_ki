#!/usr/bin/python
# -*- coding: utf-8 -*-
from textblob.classifiers import NaiveBayesClassifier

train_data = [("bu ürün çok güzel".decode('utf8'), 'pos'),
              ('çok memnunum'.decode('utf8'), 'pos'),
              ('Çok uygun fiyata çok güzel ürün'.decode('utf8'), 'pos'),
              ('Tek kelimeyle harika', 'pos'),
              ('beğenmedim'.decode('utf-8'), 'neg'),
              ('hiç iyi bir ürün değil'.decode('utf8'), 'neg'),
              ('almayın bence'.decode('utf-8'), 'neg')]

cl = NaiveBayesClassifier(train_data)
print cl.classify('bu ürün çok güzel') # pos
print cl.classify('almayın') #neg
print cl.classify('çok memnunum') #pos
print cl.classify('beğenmedim') #neg
print cl.classify('Tek kelimeyle memnunum') #pos
