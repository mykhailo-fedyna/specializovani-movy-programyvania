def process_tags(tags_string, delimiter=","):
    parts = tags_string.split(delimiter)
    cleaned = []
    for p in parts:
        tag = p.strip(" !-")
        cleaned.append(tag)
    return "  #  ".join(cleaned)


if __name__ == "__main__":
    tags_string = " python, data science! , --machine learning "
    print(process_tags(tags_string))
