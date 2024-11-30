#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing necessary packages to execute functions

# In[2]:


import os
import docx 
import spacy
import nltk
import json
import pdfplumber
from transformers import pipeline
import pathlib

# In[3]:


nltk.download('punkt')

# In[4]:


#setting the spacy to en_core_web_sm for english language

# In[5]:


nlp = spacy.load("en_core_web_sm")

# In[6]:


#Load transformer-based summarization model


summarizer = pipeline("summarization")

# In[7]:


# Load labels from JSON file
file_json="D:/vishwanathan/Doclens_AI/Backend/legal_docs.json"
def load_labels_from_json(file_json):
    with open(file_json, 'r') as file:
        return json.load(file)

# In[8]:


#function that reads a word document

# In[9]:


def read_word_document(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# In[10]:


#function to read a pdf document

# In[11]:


def read_pdf_document(file_path):
    full_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            full_text.append(page.extract_text())
    return '\n'.join(full_text)

# In[12]:


#summarizing document using NLP

# In[13]:


# Function to summarize the document using NLP
def summarize_document(content, max_length=500):
    # Limit the input size for the model to handle
    if len(content.split()) > 512:
        content = ' '.join(content.split()[:512])  # Trim the content if it's too long
    # Summarize using the transformers model
    summary = summarizer(content, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# In[14]:


#function to classify the type of document

# In[15]:


# Function to classify the document using labels from JSON
def classify_document(content, labels):
    # Lowercase the content for case insensitive comparison
    content_lower = content.lower()
    
    for entry in labels:
        clause_text = entry.get('clause_text', None)  # Safely get clause_text
        if clause_text and clause_text.lower() in content_lower:  # Check if clause_text is not None
            return entry['clause_type']
    
    return "Unknown Document Type"


# In[16]:


#function to return the file type
def get_file_extension(file_path):
    # Get the file extension and remove the leading dot
    _, extension = os.path.splitext(file_path)
    return extension[1:] # Slice to remove the dot


# # Main function to process the document

# In[17]:


def process_legal_document(uploaded_file,labels_file):
    # Load labels from JSON
    labels_file = 'D:/vishwanathan/Doclens_AI/Backend/legal_docs.json'
    labels = load_labels_from_json(labels_file)

    if uploaded_file.name.endswith('.docx'):
        content = read_word_document(uploaded_file)
    elif uploaded_file.endswith('.pdf'):
        content = read_pdf_document(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please provide a .docx or .pdf file.")

    # Summarize the document
    summary = summarize_document(content)

    # Classify the document using JSON labels
    document_type = classify_document(content, labels)
    
    #classify the file type
    extension = get_file_extension(content)
    
    #debug
    print("Document Summary:")
    print(summary)
    print("\nDocument Type:")
    print(document_type)
    print("\nFile Type:")
    print(extension)    
    print("Document verified successfully")
    
    return {
        "document_type": document_type,
       "extension":extension,
       "summary":summary
    }
    
    

# In[20]:



# Replace with the path to your Word document and JSON file
#file_path = 'E:/AIDocAnalyzer/legal_document_testpdf1.pdf'
#labels_file = 'E:/AIDocAnalyzer/Backend/legal_docs.json'
    
# Process the document
#report = process_legal_document(file_path, labels_file)
    
# Output the results
#print("Document Summary:")
#print(report["summary"])
#print("\nDocument Type:")
#print(report["document_type"])
#print("\nFile Type:")
#print(report["extension"])
