"""
Main function to implement Doc2Vec.

Part of Project for Insight Data Science - Silicon Valley 2015a

David L. Hochstetler
1/20/15

Much thanks to Matt P. and Ben E. for the dataframe and Doc2Vec help!
"""

import doc2vec_methods
import doc2vec_classses




if __name__ == '__main__':
	# Set the path to the pickled file
    directory_path = '../amazon_music_reviews/'
    file_path = 'amazon_music_random_lemmatized_0.pandas'

    df = load_pickled_df(directory_path, file_path)