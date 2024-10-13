import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from _utils.common import test

import typer
app = typer.Typer()

@app.command()
def pipeline():
    test()

@app.command()
def build():
    print('build')

if __name__ == "__main__":
    app()