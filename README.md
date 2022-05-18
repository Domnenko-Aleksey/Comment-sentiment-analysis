# Sentiment analysis model for online reputation management system (ORM)

## Data
### Getting data
Data (reviews, names of banks, rating) are obtained from the website of reviews about banks.  Using parsing in 3 stages:

1. The data was obtained by parsing pages with reviews. We parse pages to get data in the format: id, link, bank, rating. Parsing is carried out in parts. We combine individual files and get the final data set **list.csv**

2. Links are taken from a previously generated dataset. We parse pages to get data in the format: 'id', 'text', 'bank', 'rating'. Parsing is carried out in parts.

3. Connect separate files and get the final dataset **data.csv**

Result: **list.csv**, **data.csv**

### **Data analysis**

We check your data for gaps, look at statistics and balance classes. Save a balanced dataset **data_balanced**

## **Models**

### **Classification**

To categorize reviews (by class: negative, neutral, positive), BERT fine tuning was used to perform a sentiment analysis of the dataset

As a basis for creating the code, a guide was taken from the official TensorFlow website "classify_text_with_bert"

* The preprocessing model: **bert_multi_cased_preprocess/3**

Text inputs need to be transformed to numeric token ids and arranged in several Tensors before being input to BERT. TensorFlow Hub provides a matching preprocessing model for each of the BERT models discussed above, which implements this transformation using TF ops from the TF.text library. It is not necessary to run pure Python code outside your TensorFlow model to preprocess text

* BERT model: **bert_multi_cased_L-12_H-768_A-12/4**

Use the model "pooled_output" after which add our layers for classification

## **Result**

The result folder contains a report on the result of the work in PDF format
