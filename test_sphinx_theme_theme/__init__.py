"""
Seriously?
"""
import os

__version__ = "0.0.1"

def setup(app):
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme("test_sphinx_theme_theme", theme_path)
    # app.connect("html-page-context", update_context)
    # return {"version": __version__, "parallel_read_safe": True}
