
raw_input([prompt])

    If the prompt argument is present, it is written to standard output without
    a trailing newline. The function then reads a line from input, converts it
    to a string (stripping a trailing newline), and returns that. When EOF is
    read, EOFError is raised. Example: >>>

    >>> s = raw_input('--> ')
    --> Monty Python's Flying Circus
    >>> s
    "Monty Python's Flying Circus"

    If the readline module was loaded, then raw_input() will use it to provide
    elaborate line editing and history features.