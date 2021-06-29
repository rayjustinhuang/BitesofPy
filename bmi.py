import argparse


def calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


def create_parser():
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object"""
       
    parser = agrparse.ArgumentParser(description='Calculate your BMI')
    parser.add_argument('weight', metavar='-w', type=int, nargs=1, help='Your weight in kg')
    partser.add_argument('length', metavar='-l', type=int, nargs=1, help='Your length in cm')
    pass


def handle_args(args=None):
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    if args is None:
        parser = create_parser()
        args = parser.parse_args()

    if args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    else:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        raise SystemExit


if __name__ == '__main__':
    handle_args()