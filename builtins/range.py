""" range(start,stop[,step])

    This is a versatile function to create lists containing arithmetic
    progressions. It is most often used in for loops. The arguments must be
    plain integers. If the step argument is omitted, it defaults to 1. If the
    start argument is omitted, it defaults to 0. The full form returns a list of
    plain integers [start, start + step, start + 2 * step, ...]. If step is
    positive, the last element is the largest start + i * step less than stop;
    if step is negative, the last element is the smallest start + i * step
    greater than stop. step must not be zero (or else ValueError is raised).
"""
