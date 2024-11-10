from markdown_blocks import markdown_to_html_node
from extract_title import extract_title_markdown
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()

    title = extract_title_markdown(markdown)
    content = markdown_to_html_node(markdown).to_html()        

    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)

    # Extract the directory path from the file path
    dir_path = os.path.dirname(dest_path)
    
    # Create missing directories if necessary
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)  # `exist_ok=True` ignores existing directories
    

    with open(dest_path, 'w', encoding='utf-8') as file:
        file.write(html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print("start")
    for root, dirs, files in os.walk(dir_path_content):
        print(f"{root}, {dirs}, {files}")
        for file in files:
            print(f"{file}")
            if file.endswith(".md"):
                # Get the relative path of the markdown file
                relative_path = os.path.relpath(root, dir_path_content)
                
                # Construct the input markdown path and the destination HTML path
                markdown_path = os.path.join(root, file)
                html_path = os.path.join(dest_dir_path, relative_path, file.replace('.md', '.html'))

                print(f"copy file: {file} markdown_path: {markdown_path} html_path: {html_path}")
                
                # Generate the page from markdown to HTML
                generate_page(markdown_path, template_path, html_path)