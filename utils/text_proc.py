def words_yield(fileobj):
    for line in fileobj:
        for word in line.split():
            yield word
