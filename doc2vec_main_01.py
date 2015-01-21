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
	directory_path = '../../Lemmatized_by_Sentence/'
    file_path = 'amazon_music_random_lemmatized_0.pandas'
    df = load_pickled_df(directory_path, file_path)

    # Get the df into desired format
    # NOTE: This assumes set/hard-coded columns and column names in each df
    df = df_columns_reduce(df)
    df = df_title_format(df)
    df = df_review_collapse(df)

    # Run Doc2Vec on the dataset of reviews
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    reviews = LabeledReviewSentence(df)

    # Instantiate the doc2vec model
    # Want to know how long this training takes
    # Need to look into adjustable parameters...
    # --> SEE gensim site
	%time model = gensim.models.Doc2Vec(reviews, workers=4)

	# Look at results
	model.most_similar_cosmul(positive=['hard','rock'], negative=[], topn=10)







