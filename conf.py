project = "Agentplace Beginner Guide (independent)"
author = "Mumpe Cydrone"
copyright = "2026, Mumpe Cydrone"
extensions = ["sphinx_copybutton"]
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
exclude_patterns = ["_build", "venv", ".venv", "Thumbs.db", ".DS_Store"]

rst_prolog = """
.. |last_checked| replace:: 3 November 2026
"""

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#1f4adc",
        "color-brand-content": "#1f4adc",
        "color-link--hover": "#153bb5",
        "color-foreground-primary": "#172036",
        "color-foreground-secondary": "#59647a",
        "color-background-border": "#dbe0e9",
        "font-stack": 'Inter, system-ui, -apple-system, "Segoe UI", Arial, sans-serif',
        "font-stack--headings": '"Funnel Display", Inter, system-ui, Arial, sans-serif',
    },
    "dark_css_variables": {
        "color-brand-primary": "#7f9bff",
        "color-brand-content": "#7f9bff",
        "color-link--hover": "#a9bcff",
        "color-background-border": "#2a3347",
        "font-stack": 'Inter, system-ui, -apple-system, "Segoe UI", Arial, sans-serif',
        "font-stack--headings": '"Funnel Display", Inter, system-ui, Arial, sans-serif',
    },
}
