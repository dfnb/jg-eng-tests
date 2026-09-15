from pathlib import Path
x=(Path(__file__).parents[1]/"compose.yaml").read_text()
assert all(name+":" in x for name in ("db","redis","api","worker"))
print("Public tests passed")
