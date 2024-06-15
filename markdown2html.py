#!/usr/bin/python3
"""
markdown2html.py
A script to convert Markdown files to HTML files.
"""

import sys
import os
import re

def parse_markdown(markdown_text):
    """
    Parses the given markdown text and converts it to HTML.

    Args:
        markdown_text (str): The markdown content to be converted.

    Returns:
        str: The HTML representation of the markdown content.
    """
    # Regular expression for detecting **bold text**
    bold_pattern = re.compile(r'\*\*(.*?)\*\*')

    def convert_bold_syntax(match):
        """
        Converts matched bold syntax to HTML <strong> tags.

        Args:
            match (re.Match object): The matched object containing bold text.

        Returns:
            str: HTML representation of bold text.
        """
        return f"<strong>{match.group(1)}</strong>"

    html_lines = []
    lines = markdown_text.split('\n')
    in_ul = False
    in_ol = False
    in_p = False
    paragraph = []

    def close_paragraph():
        nonlocal in_p
        if in_p:
            html_lines.append(f"<p>{' '.join(paragraph)}</p>")
            paragraph.clear()
            in_p = False

    for line in lines:
        stripped_line = line.strip()

        if re.match(r'^# ', stripped_line):
            close_paragraph()
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            html_lines.append(f"<h1>{stripped_line[2:].strip()}</h1>")

        elif re.match(r'^## ', stripped_line):
            close_paragraph()
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            html_lines.append(f"<h2>{stripped_line[3:].strip()}</h2>")

        elif re.match(r'^### ', stripped_line):
            close_paragraph()
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            html_lines.append(f"<h3>{stripped_line[4:].strip()}</h3>")

        elif re.match(r'^#### ', stripped_line):
            close_paragraph()
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            html_lines.append(f"<h4>{stripped_line[5:].strip()}</h4>")

        elif re.match(r'^##### ', stripped_line):
            close_paragraph()
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            html_lines.append(f"<h5>{stripped_line[6:].strip()}</h5>")

        elif re.match(r'^###### ', stripped_line):
            close_paragraph()
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            html_lines.append(f"<h6>{stripped_line[7:].strip()}</h6>")

        elif re.match(r'^- ', stripped_line):
            close_paragraph()
            if not in_ul:
                if in_ol:
                    html_lines.append('</ol>')
                    in_ol = False
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f"<li>{stripped_line[2:].strip()}</li>")

        elif re.match(r'^\d+\. ', stripped_line):
            close_paragraph()
            if not in_ol:
                if in_ul:
                    html_lines.append('</ul>')
                    in_ul = False
                html_lines.append('<ol>')
                in_ol = True
            html_lines.append(f"<li>{stripped_line[stripped_line.find(' ') + 1:].strip()}</li>")

        else:
            if stripped_line:
                # Apply bold syntax conversion using re.sub
                replaced_line = bold_pattern.sub(convert_bold_syntax, stripped_line)
                paragraph.append(replaced_line)
                in_p = True
            else:
                close_paragraph()

    close_paragraph()
    if in_ul:
        html_lines.append('</ul>')
    if in_ol:
        html_lines.append('</ol>')

    return '\n'.join(html_lines)

def main():
    """
    Main function to handle file reading, conversion, and writing.
    """
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(input_file, 'r') as md_file:
            markdown_text = md_file.read()
            html_content = parse_markdown(markdown_text)

        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

        sys.exit(0)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
