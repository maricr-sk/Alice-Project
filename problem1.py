from collections import defaultdict
import string


def count_ngrams(filename, n=2):
    try:
        f = open(filename, "r")
        long_str = ""
        new_str =""
        words = []
        punc = string.punctuation
        dic = defaultdict()
        for l in f:
            long_str += " " + l.strip("\n").replace('-',' ')
        for letter in long_str:
            if letter not in punc:
                new_str += letter
        words = new_str.lower().split()
        for i in range(len(words)-n+1):
            n_gram = tuple(words[i:i+n])
            if dic.get(n_gram) is None:
                dic[n_gram] = 1
            else:
                dic[n_gram] += 1
        return dic
    except FileNotFoundError as e:
        print("This file does not exist. Please use a valid filename next time.")
        exit(0)


def single_occurences(ngram_count_dict):
    li = []
    for i in ngram_count_dict:
        if ngram_count_dict[i] == 1:
            li.append(i)
    return li


def most_frequent(ngram_count_dict, num=5):
    li = []
    for entry in ngram_count_dict:
        li.append((ngram_count_dict[entry], entry))
    li.sort()
    final = []

    if num > len(li):
        num = len(li)
    for i in range(1, num+1):
        final.append(li[-i][1])
    return final


def main(filename, n, most_frequent_k):
    ngram_counts = count_ngrams(filename, n)

    print(f'{n}-grams that occur only once:')
    print(single_occurences(ngram_counts))

    print(f'{most_frequent_k} most frequent {n}-grams:')
    print(most_frequent(ngram_counts, most_frequent_k))


if __name__ == '__main__':
  main("alice.txt", 2, 5)
