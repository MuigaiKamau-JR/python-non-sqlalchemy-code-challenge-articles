#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Sample data for debugging
    author_1 = Author("Carry Bradshaw")
    magazine_1 = Magazine("Vogue", "Fashion")
    article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
    
    print(magazine_1.articles())
    print(author_1.articles())

    # don't remove this line, ni ya debugging!
    ipdb.set_trace()
