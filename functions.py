def clean_lines(input_lines):
    return filter(lambda line: (len(line)), input_lines.split("\n"))
