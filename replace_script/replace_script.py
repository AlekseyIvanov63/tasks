import sys
import re


def load_config(config_fil):
    """Converts configuration file data into a dictionary."""
    replacements = {}
    with open(config_fil, 'r') as f:
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=')
                replacements[key] = value
    return replacements


def replace_values(text, replacements):
    """Replace values 1 with values 2 from the configuration file in a text file."""
    changed_lines = []
    for line in text.splitlines():
        all_count = 0
        for key, value in replacements.items():
            line, count = re.subn(key, value, line)
            all_count += count
        changed_lines.append((line, all_count))
    return changed_lines


def sort_lines(lines):
    """Sort strings by largest replacements."""
    return sorted(lines, key=lambda x: x[1], reverse=True)


def main(config_fil, text_fil):
    """Function replaces values and sorts."""
    replacements = load_config(config_fil)

    with open(text_fil, 'r') as f:
        text = f.read()

    changed_lines = replace_values(text, replacements)
    sorted_changed_lines = sort_lines(changed_lines)

    for line, count in sorted_changed_lines:
        print(f"{line} ({count})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Use script: python script.py <config_file> <text_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    text_file = sys.argv[2]
    main(config_file, text_file)
