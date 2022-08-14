import typing

import click
from decimal import Decimal, getcontext

from click import INT


class DecimalParamType(click.ParamType):
    name = 'decimal'

    def convert(self, value, param, ctx):
        if isinstance(value, Decimal):
            return value

        try:
            return Decimal(value)
        except ValueError:
            self.fail(f'{value!r} is not a valid integer', param, ctx)


DECIMAL = DecimalParamType()


def get_steps(step_size: Decimal, start: Decimal = Decimal('0'), stop: Decimal = Decimal('1'), precision: int = 5) -> typing.List[str]:
    lines = []
    getcontext().prec = precision
    current = start
    percentage = step_size / (stop - start)
    i = Decimal('0')

    while current <= stop:
        value = percentage * i

        if (step_size + current) > stop:
            # Ensure that our last value is our `stop` value
            value = 1
            current = stop
        elif value == 0:
            value = 0
        elif value == 1:
            value = 1
        
        lines.append(f'       <STEP value="{value}" short="{current}" long="{current}"/>')
        
        current += step_size
        i += Decimal('1')
    
    return lines


@click.group()
def cli():
    pass


@cli.command(name='step-size')
@click.argument('size', type=DECIMAL)
@click.argument('start', type=DECIMAL, default=Decimal('0'))
@click.argument('stop', type=DECIMAL, default=Decimal('1'))
@click.option('--precision', type=INT, default=5, help='Decimal precision')
def step_size(size, start=Decimal('0'), stop=Decimal('1'), precision: int = 5):
    click.echo("\n".join(
        get_steps(size, start, stop, precision)
    ))


@cli.command(name='steps')
@click.argument('total', type=DECIMAL)
@click.argument('start', type=DECIMAL, default=Decimal('0'))
@click.argument('stop', type=DECIMAL, default=Decimal('1'))
@click.option('--precision', type=INT, default=5, help='Decimal precision')
def steps(total, start=Decimal('0'), stop=Decimal('1'), precision: int = 5):
    size = (stop - start) / (total - 1)
    click.echo("\n".join(
        get_steps(size, start, stop, precision)
    ))


if __name__ == '__main__':
    cli()
