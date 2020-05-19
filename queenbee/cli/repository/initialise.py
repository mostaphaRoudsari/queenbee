import os
from ...repository.index import RepositoryIndex

try:
    import click
    from click_plugins import with_plugins
except ImportError:
    raise ImportError(
        'click modules not installed. Try `pip install queenbee[cli]` command.'
    )

MODULE_PATH = os.path.abspath(os.path.dirname(__file__))

@click.command('init')
@click.argument('path', type=click.Path(exists=False))
def initialise(path):
    """initialise an empty repository

    Use this command to create a new repository folder.
    """

    path = os.path.abspath(path)

    os.makedirs(os.path.join(path, 'workflows'))
    os.makedirs(os.path.join(path, 'recipes'))

    index = RepositoryIndex.from_folder(path)

    index.to_json(os.path.join(path, 'index.json'), indent=2)

    click.echo(f'Created new repository at {path}')

    