

import click
from code_reader import read_code_from_file, read_code_from_directory

@click.command()
@click.option('--file', help='Path to a single Python file to read.')
@click.option('--directory', help='Path to a directory to read all Python files in it.')
def read_code(file, directory):
    if file:
        code = read_code_from_file(file)
        click.echo(f"Code from {file}:\n\n{code}\n{'='*50}\n")
    elif directory:
        code_dict = read_code_from_directory(directory)
        for file_path, code in code_dict.items():
            click.echo(f"Code from {file_path}:\n\n{code}\n{'='*50}\n")
    else:
        click.echo("Please provide either --file or --directory option.")

if __name__ == '__main__':
    read_code()

