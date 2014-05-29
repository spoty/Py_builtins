import timeit

x = range(10)

print timeit.timeit('[i for i in reversed(x)]', setup='x = range(10)')

print timeit.timeit('x[::-1]', setup='x = range(10)')
