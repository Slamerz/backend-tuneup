#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Jacob Walker"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    # https://docs.python.org/2/library/profile.html
    def deco(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sort_by = 'cumulative'
        ps = pstats.Stats(pr).sort_stats(sort_by)
        ps.print_stats(10)
        return result
    return deco


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    formatted_movies = []
    seen = {}
    results = []

    for movie in movies:
        formatted_movies.append(movie.split('\t')[1])

    for movie in formatted_movies:
        if movie in seen:
            seen[movie] += 1
            results.append(movie)
        else:
            seen[movie] = 1
    print('Found {} duplicate movies:{}'.format(len(results), results))


@profile
def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    setup = 'from __main__ import find_duplicate_movies'
    """Computes a list of duplicate movie entries"""
    t = timeit.Timer("find_duplicate_movies('movies.txt')", setup)
    repeat_num = 3
    run_num = 3
    result = t.repeat(repeat=repeat_num, number=run_num)
    result = [number / float(run_num) for number in result]
    print('Best time of {} runs:'.format(repeat_num * run_num))
    return min(result)


def main():
    timeit_helper()


if __name__ == '__main__':
    main()
