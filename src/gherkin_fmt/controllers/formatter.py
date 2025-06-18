def format_gherkin(source: str) -> str:
    lines = source.splitlines()

    # TODO: Apply formatting rules here
    formatted = "\n".join(lines).strip() + "\n"
    return formatted
