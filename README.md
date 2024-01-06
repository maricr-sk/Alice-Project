# Alice Project

Create n-grams given a specific text. Also finds the number of occurrences.

Directions: 

An n-gram is a contiguous sequence of n words in the given text. An n-gram of size 1 is referred to as a unigram, size 2 is a bigram, and size 3 is a trigram. For example, for the sentence "Columbia University is great" the unigrams would be
[('columbia',), ('university',), ('is',), ('great',)], 
the bigrams would be
[('columbia','university'), ('university','is'), ('is','great')], 
and the trigrams would be 
[('columbia','university','is'), ('university','is','great')]

N-grams are frequently used in natural language processing (NLP) applications such as language modeling to identify a text's genre or author, or in machine translation to judge the quality of the translation output (if the output includes very unlikely n-grams, it's probably not good).
