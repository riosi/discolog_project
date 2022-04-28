from typer.testing import CliRunner
from beerlog.cli import main

runner = CliRunner()


def test_add_beer():
    result = runner.invoke(
        main, ["add", "Skol", "KornIPA", "--flavor=1", "--image=2", "--cost=3"]
    )
    assert result.exit_code == 0
    assert "beer added to database" in result.stdout
