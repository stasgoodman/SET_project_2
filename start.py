import typer
from tasks.runtests import *

app = typer.Typer(add_completion=False)


@app.command()
def catapi_tests():
    """
    1st
    """
    run_bin_tests()


if __name__ == '__main__':
    app()
