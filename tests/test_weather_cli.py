import pytest
from click.testing import CliRunner
from tools.weather_cli import weather


def test_non_city():
    runner = CliRunner()
    prompt_inputs = 'Shabalaba123'
    result = runner.invoke(weather, input=prompt_inputs)

    expected_output = '\n'.join([
        'City Name: Shabalaba123',
        'OpenWeather does not have information for this location.',
        ''
    ])

    assert result.output == expected_output


def test_city():
    runner = CliRunner()
    prompt_inputs = 'Dansoman'
    result = runner.invoke(weather, input=prompt_inputs)

    expected_output = '\n'.join([
        'City Name: Dansoman',
        'It is currently 89% humid',
        ''
    ])

    assert result.output == expected_output

