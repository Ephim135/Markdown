import re

# Sample text
text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"

# Regex pattern to match everything up to the first comma
pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# Using re.search() to find the pattern in the text
match = re.findall(pattern, text)

input_text = text
for x in match:
    img_text, url = x
    sections = input_text.split(f"![{img_text}]({url})", 1)
    print(sections)
    if sections[0] != "":
        answer.append(TextNode(sections[0], TextType.TEXT))
    if sections[0]
    input_text = sections[1]

# Check if there's a match and print it
if match:
    print(match)  # Output: "Hello"
