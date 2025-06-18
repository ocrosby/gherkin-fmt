from click.testing import CliRunner

from gherkin_fmt.main import cli


def test_format_empty():
    runner = CliRunner()
    result = runner.invoke(cli, ["fmt"], input="")
    assert result.exit_code == 0
