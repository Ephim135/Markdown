def extract_title_markdown(markdown):
    lines = markdown.splitlines()
    title = None
    for line in lines:
        line_strip = line.lstrip()
        if line_strip.startswith("#") and not line_strip.startswith("##"):
            if title is not None:
                raise Exception("more than one Title")
            title = line_strip[2:].strip()
    if title is None:
        raise Exception("no Title found")
    return title