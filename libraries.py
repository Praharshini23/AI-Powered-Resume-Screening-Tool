import streamlit as st
import re
import string
import spacy
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import io
from nltk.corpus import stopwords
