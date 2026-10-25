import sqlite3
import html
from string.templatelib import Interpolation


def render(template):
    parts = []
    for part in template:
        if isinstance(part, Interpolation):
            parts.append(format(part.value, part.format_spec))
        else:
            parts.append(part)
    return "".join(parts)


def render_html(template):
    parts = []
    for part in template:
        if isinstance(part, Interpolation):
            parts.append(html.escape(format(part.value, part.format_spec)))
        else:
            parts.append(part)
    return "".join(parts)


description = "<script>alert(1)</script>"
print(f"<p>{description}</p>")
print(render_html(t"<p>{description}</p>"))


def to_sql(template):
    sql, params = [], []
    for part in template:
        if isinstance(part, Interpolation):
            sql.append("?")
            params.append(part.value)
        else:
            sql.append(part)
    return "".join(sql), params

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE tx (date TEXT, description TEXT, amount REAL)")
when, who, amount = "2026-10-01", "O'Brien's Pub", -32.0
conn.execute(*to_sql(t"INSERT INTO tx VALUES ({when}, {who}, {amount})"))
print(conn.execute("SELECT * FROM tx").fetchall())
