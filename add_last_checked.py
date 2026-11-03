import pathlib

files = ["tutorial/build-your-first-agent.rst"]
files += [str(p) for p in pathlib.Path("how-to").glob("*.rst") if p.name != "index.rst"]

line = "**Last checked:** |last_checked| against Agentplace's public documentation.\n"

for f in files:
    p = pathlib.Path(f)
    lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
    if any("|last_checked|" in l for l in lines):
        continue
    lines[2:2] = ["\n", line]
    p.write_text("".join(lines), encoding="utf-8")
    print("updated", f)
