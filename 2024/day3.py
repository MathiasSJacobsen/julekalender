import re


def extract_mul_instructions(text):
    
    pattern = r"mul\(([-+]?\d+),([-+]?\d+)\)"
    
    matches = re.findall(pattern, text)
    instructions = []
    for x_str, y_str in matches:
        x = int(x_str)
        y = int(y_str)
        instructions.append((x, y))
    return instructions

def multiply_all_instructions(text):
    instructions = extract_mul_instructions(text)
    return sum([x * y for (x, y) in instructions])

def parse_and_execute_instructions(text):
    """
    Parse the text for do(), don't(), and mul(X,Y) instructions.
    - At the start, mul is enabled.
    - do() re-enables mul instructions.
    - don't() disables mul instructions.
    - mul(X,Y) is only executed (multiplied) if mul is currently enabled.
    
    Returns a list of integer results from each enabled mul(X,Y).
    """

    # This regex will match any of the three patterns in the order they appear
    pattern = re.compile(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")

    # Find all occurrences of these instructions in order
    instructions = pattern.findall(text)

    results = []
    enabled = True  # mul instructions are enabled at the beginning

    for instr in instructions:
        if instr == "do()":
            enabled = True
        elif instr == "don't()":
            enabled = False
        else:
            match = re.match(r"mul\((\d+),(\d+)\)", instr)
            if match:
                x_str, y_str = match.groups()
                x, y = int(x_str), int(y_str)
                if enabled:
                    results.append(x * y)

    return sum(results)

if __name__ == "__main__":
    with open("2024/day3.txt") as f:
        data = f.read()
    # result = multiply_all_instructions(data)
    result = parse_and_execute_instructions(data)
    print(result)