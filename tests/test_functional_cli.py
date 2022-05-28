from typer.testing import CliRunner
from discolog.cli import main

runner = CliRunner()


def test_add_album():
    result = runner.invoke(
        main, ["add", "Summer Holiday", "Dreamcatcher", "--year=2021", "--rate=10", "--review=Tudo de lindo"]
    )
    assert result.exit_code == 0
    assert "album added to database" in result.stdout
