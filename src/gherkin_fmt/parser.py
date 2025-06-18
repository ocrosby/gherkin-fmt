from gherkin.parser import Parser
from gherkin.token_scanner import TokenScanner


def parse_gherkin(source: str) -> dict:
    """
    Parses a Gherkin feature file and returns the parsed abstract syntax tree (AST).
    Raises ValueError on parsing errors.
    """
    parser = Parser()
    try:
        return parser.parse(TokenScanner(source))
    except Exception as e:
        raise ValueError(f"Invalid Gherkin syntax: {e}") from e
