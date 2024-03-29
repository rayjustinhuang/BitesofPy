import os
from pathlib import Path
import string
import sys
from urllib.request import urlretrieve
from zipfile import ZipFile

import pandas as pd

TMP = Path(os.getenv("TMP", "/tmp"))
S3 = "https://bites-data.s3.us-east-2.amazonaws.com"


def _setup():
    data_zipfile = '311-data.zip'
    urlretrieve(f'{S3}/{data_zipfile}', TMP / data_zipfile)
    ZipFile(TMP / data_zipfile).extractall(TMP)
    sys.path.append(TMP)

_setup()

from stop_words import stop_words
from tf_idf import TFIDF


def load_data():
    # Load the text and populate a Pandas Dataframe
    # The order of the sample text strings should not be changed
    # Return the Dataframe with the index and 'text' column
    return pd.read_csv('/tmp/samples.txt')
    pass


def strip_url_email(x_df):
    # Strip all URLs (http://...) and Emails (somename@email.address)
    # The 'text' column should be modified to remove
    #   all URls and Emails
    df = pd.DataFrame(x_df['text'].str.replace(r"[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)", ''))
    df = pd.DataFrame(df['text'].str.replace(r'\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', ''))
    return df
    pass


def to_lowercase(x_df):
    # Convert the contents of the 'text' column to lower case
    # Return the Dataframe with the 'text' as lower case
    df = pd.DataFrame(x_df['text'].str.lower())
    return df
    pass


def strip_stopwords(x_df):
    # Drop all stop words from the 'text' column
    # Return the Dataframe with the 'text' stripped of stop words
    df = pd.DataFrame(x_df['text'].apply(lambda x: " ".join([word for word in x.split() if word not in stop_words])))
    return df
    pass


def strip_non_ascii(x_df):
    # Remove all non-ascii characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of non-ascii characters
    df = pd.DataFrame(x_df['text'].str.encode('ascii', 'ignore').str.decode('ascii'))
    return df
    pass


def strip_digits_punctuation(x_df):
    # Remove all digits and punctuation characters from the 'text' column
    # Return the Dataframe with the 'text' column
    #   stripped of all digit and punctuation characters
    df = pd.DataFrame(x_df['text'].str.replace('\d+', ""))
    table = str.maketrans(dict.fromkeys(string.punctuation))
    df = pd.DataFrame(df['text'].str.translate(table))
    return df
    pass


def calculate_tfidf(x_df):
    # Calculate the 'tf-idf' matrix of the 'text' column
    # Return the 'tf-idf' Dataframe
    tfidf_obj = TFIDF(x_df['text'])
    return tfidf_obj()


def sort_columns(x_df):
    # Depending on how the earlier functions are implemented
    #   it's possible that the order of the columns may be different
    # Sort the 'tf-idf' Dataframe columns
    #   This ensure the tests are compatible
    df = pd.DataFrame(x_df.sort_index(axis=1).copy())
    return df
    pass


def get_tdidf():
    # Pandas’ pipeline feature allows you to string together
    #   Python functions in order to build a pipeline of data processing.
    # Complete the functions above in order to produce a 'tf-idf' Dataframe
    # Return the 'tf-idf' Dataframe
    df = (
        load_data()
        .pipe(strip_url_email)
        .pipe(to_lowercase)
        .pipe(strip_stopwords)
        .pipe(strip_non_ascii)
        .pipe(strip_digits_punctuation)
        .pipe(calculate_tfidf)
        .pipe(sort_columns)
    )
    return df
