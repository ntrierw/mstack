import markdown
import os
import glob
import re
import sys

# Get the list of markdown files in content/ directory
md_files = glob.glob("content/*.md")

# Specify the output directory path
output_dir = "output"

# Loop through each markdown file
for md_file in md_files:
    # Read the markdown file
    with open(md_file, "r") as f:
        md_text = f.read()
    
    # Find the text between the h1 tag in the markdown
    h1_text = re.search(r"# (.*)\n", md_text).group(1)

    # Convert markdown to html
    html = markdown.markdown(md_text)

    # Create the output file name by replacing .md with .html
    output_file = md_file.replace(".md", ".html")

    # Write the output file to the output directory
    with open(os.path.join(output_dir, output_file), "w") as f:
        with open("template/template.html", "r") as g:
            htmlRead = g.read()
            htmlRead = htmlRead.replace("$title$", h1_text)            
        
        htmlRead = htmlRead.replace("$content$", html)
        
        # Read plugin files and execute run function
        sys.path.append('plugin/')
        for file in os.listdir("plugin/"):
            if file.endswith(".py"):
                module = __import__(file[:-3])        
                htmlRead = module.run(htmlRead)
        # Write the converted html
        f.write(htmlRead)
