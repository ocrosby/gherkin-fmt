from gherkin.parser import Parser

def validate_gherkin(source: str):
    issues = []
    parser = Parser()

    try:
        parser.parse(source)
    except Exception as e:
        issues.append({"line": 0, "message": str(e)})

    # TODO: Add rule checks here
    return issues

