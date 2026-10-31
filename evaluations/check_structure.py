"""Static package and fixture checks; not a model-behavior evaluation."""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def check():
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
    assert match, "Missing or malformed frontmatter"
    meta = yaml.safe_load(match.group(1))
    assert set(meta) == {"name", "description"}, "Unexpected frontmatter fields"
    assert meta["name"] == "better-report"
    assert isinstance(meta["description"], str) and 0 < len(meta["description"]) <= 1024
    assert len(skill.splitlines()) < 500, "Core skill exceeds suggested size"
    ui = yaml.safe_load((ROOT / "agents/openai.yaml").read_text(encoding="utf-8"))
    assert 25 <= len(ui["interface"]["short_description"]) <= 64
    assert "$better-report" in ui["interface"]["default_prompt"]
    assert ui["policy"]["allow_implicit_invocation"] is True

    for doc in ROOT.rglob("*.md"):
        if ".git" in doc.parts:
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            assert (doc.parent / target).exists(), f"Broken local link in {doc}: {target}"

    rubric = json.loads((ROOT / "evaluations/rubric.json").read_text(encoding="utf-8"))
    cases = {p.parent.name for p in (ROOT / "evaluations/cases").glob("*/request.md")}
    assert cases == set(rubric), "Cases and rubric identifiers differ"
    assert len(cases) >= 8
    assert all(isinstance(items, list) and items and all(isinstance(x, str) and x for x in items)
               for items in rubric.values())
    assert "archive/" not in skill, "Historical specialist guidance must not be auto-loaded"
    assert "survival-reporting.md" not in skill
    print(f"PASS: package metadata, local links, and {len(cases)} evaluation cases")


if __name__ == "__main__":
    check()
