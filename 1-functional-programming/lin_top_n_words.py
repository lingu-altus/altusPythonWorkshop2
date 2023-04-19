text = "Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It is a declarative programming paradigm, which means programming is done with expressions or declarations instead of statements."
top_n = 5

print(top_n_words(text, top_n))


def top_n_words(text, top_n):
    #break string into list
    #iterate through list and add count for each word ( to a map)
    #iterate through map keys to get top 5 
