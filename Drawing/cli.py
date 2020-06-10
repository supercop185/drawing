from Drawing import *

import click

@click.command()
@click.option("-m", '--func', help='Introduza shapes ou oval"', required=True)


def main(func):
    if func=="color":
        red()
    elif func=="shapes":
        oval()
    else:
        print("Introduza shapes ou oval")

if __name__ == '__main__':
    main()