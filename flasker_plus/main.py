
import click
import os


TEMPLATE_URL = 'https://github.com/XzavierDunn/restPlus.git'


@click.group()
def main():
    pass


@main.command()
def start():
    project_name = click.prompt('Enter project Name: ')

    path = os.getcwd()

    install_path = f'{path}/{project_name}'

    os.system('git clone %s %s' % (TEMPLATE_URL, install_path))

    print('Install Complete, check the readme at
            https://github.com/connormullett/flasker_plus')

