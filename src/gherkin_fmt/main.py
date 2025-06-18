import click

from gherkin_fmt.controllers import format_gherkin, validate_gherkin


@click.group()
def cli():
    """gherkin-fmt: Format and lint Gherkin files."""
    pass


@cli.command()
@click.argument("file", type=click.Path(exists=True))
def lint(file):
    """Validate Gherkin syntax and style rules."""
    issues = validate_gherkin(file)
    if issues:
        for issue in issues:
            click.echo(f"{file}:{issue['line']}: {issue['message']}")
        raise SystemExit(1)
    click.echo("No issues found.")


@cli.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--in-place", is_flag=True, help="Overwrite the input file.")
def fmt(file, in_place):
    """Format Gherkin file."""
    formatted = format_gherkin(file)
    if in_place:
        with open(file, "w") as f:
            f.write(formatted)
    else:
        click.echo(formatted)


if __name__ == "__main__":
    cli()
