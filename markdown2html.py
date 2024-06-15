#!/usr/bin/python3
"""
markdown2html.py
A script to convert Markdown files to HTML files.
"""

import sys
import os

def parse_markdown(markdown_text):
    """
    Parses the given markdown text and converts it to HTML.
    
    Args:
        markdown_text (str): The markdown content to be converted.
    
    Returns:
        str: The HTML representation of the markdown content.
    """
    html_lines = []
    lines = markdown_text.split('\n')
    
    for line in lines:
        if line.startswith('# '):
            html_lines.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith('## '):
            html_lines.append(f"<h2>{line[3:].strip()}</h2>")
        elif line.startswith('### '):
            html_lines.append(f"<h3>{line[4:].strip()}</h3>")
        elif line.startswith('#### '):
            html_lines.append(f"<h4>{line[5:].strip()}</h4>")
        elif line.startswith('##### '):
            html_lines.append(f"<h5>{line[6:].strip()}</h5>")
        elif line.startswith('###### '):
            html_lines.append(f"<h6>{line[7:].strip()}</h6>")
        else:
            html_lines.append(f"<p>{line.strip()}</p>")
    
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
