#!/usr/bin/python3
"""
markdown2html.py: A script to convert Markdown files to HTML.

Usage:
    ./markdown2html.py README.md README.html

This script takes two arguments:
1. The name of the Markdown file to be converted.
2. The name of the output HTML file.

Requirements:
- If the number of arguments is less than 2: 
  print in STDERR "Usage: ./markdown2html.py README.md README.html" and exit with status 1.
- If the Markdown file doesn’t exist: 
  print in STDERR "Missing <filename>" and exit with status 1.
- Otherwise, print nothing and exit with status 0.
"""
import sys
import os
import markdown

def main():
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
            html_content = markdown.markdown(markdown_text)
        
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)
        
        sys.exit(0)
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
