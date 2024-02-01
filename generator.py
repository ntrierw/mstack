import markdown
import os
import glob

# Get the list of markdown files in content/ directory
md_files = glob.glob("content/*.md")

# Get the list of html files in template/ directory
html_files = sorted(glob.glob("template/*.html"))

# Find the index of m.html in the list
m_index = html_files.index("template/m.html")

# Split the list into two parts: before and after m.html
before_m = html_files[:m_index]
after_m = html_files[m_index+1:]

# Specify the output directory path
output_dir = "output"

# Loop through each markdown file
for md_file in md_files:
    # Read the markdown file
    with open(md_file, "r") as f:
        md_text = f.read()

    # Convert markdown to html
    html = markdown.markdown(md_text)

    # Create the output file name by replacing .md with .html
    output_file = md_file.replace(".md", ".html")

    # Write the output file to the output directory
    with open(os.path.join(output_dir, output_file), "w") as f:
        # Prepend the html files before m.html
        for file in before_m:
            with open(file, "r") as g:
                f.write(g.read())

        # Write the converted html
        f.write(html)

        # Append the html files after m.html
        for file in after_m:
            with open(file, "r") as g:
                f.write(g.read())
