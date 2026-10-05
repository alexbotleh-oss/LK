from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "project_diagnostic", ROOT / "scripts" / "project_diagnostic.py"
)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

def test_required_layout():
    for rel in mod.REQUIRED_DIRS:
        assert (ROOT / rel).is_dir(), rel

def test_critical_files():
    for rel in mod.CRITICAL_FILES:
        assert (ROOT / rel).is_file(), rel

def test_stage14_scanner_hooks():
    text = (ROOT / "stage14.html").read_text(encoding="utf-8", errors="replace")
    assert "function openScanner" in text
    assert "function scanSubmit" in text
    assert "Core.findQR" in text
