import pytest

from workouts import print_workout_days

@pytest.mark.parametrize("test_input,expected", [("upper body #4", "No matching workout\n"), ("upper body #1", 'Mon\n'), ("30 min cardio", 'Wed\n'), ('lower body #1, 30 min cardio', 'No matching workout\n'), ("upper body #2", 'Thu\n'),("lower body #2", 'Fri\n'),("lower body #1", 'Tue\n'),("", 'Mon, Tue, Wed, Thu, Fri\n'),])
def test_print_workout_days(test_input, expected, capsys):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected
    pass