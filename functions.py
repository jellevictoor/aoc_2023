def clean_lines(input_lines):
    return list(filter(lambda line: (len(line)), input_lines.split("\n")))
