"""Contract tests for the bundled minimal-change skill."""

import re
from pathlib import Path

import pytest


SKILL_MD = Path(__file__).resolve().parents[2] / "skills/software-development/minimal-change/SKILL.md"
REQUIRED_SECTIONS = [
    "## When to Use",
    "## Prerequisites",
    "## How to Run",
    "## Quick Reference",
    "## Procedure",
    "## Pitfalls",
    "## Verification",
]


@pytest.fixture(scope="module")
def skill_text() -> str:
    return SKILL_MD.read_text(encoding="utf-8")


def _value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    assert match, f"missing frontmatter field: {key}"
    return match.group(1).strip()


def test_frontmatter_meets_authoring_standard(skill_text: str) -> None:
    assert _value(skill_text, "name") == "minimal-change"
    description = _value(skill_text, "description")
    assert len(description) <= 60
    assert description.endswith(".")
    assert description == "Use only when asked for the smallest sufficient code change."
    assert _value(skill_text, "author").startswith("Joey Farina (josephfarina)")
    assert _value(skill_text, "platforms") == "[linux, macos, windows]"
    assert "    tags: [" in skill_text


def test_body_uses_modern_section_order(skill_text: str) -> None:
    positions = [skill_text.index(section) for section in REQUIRED_SECTIONS]
    assert positions == sorted(positions)


def test_decision_ladder_and_scope_guards_are_documented(skill_text: str) -> None:
    ladder = skill_text.split("## Quick Reference", 1)[1].split("## Procedure", 1)[0]
    for label in (
        "Need",
        "Existing",
        "Stdlib",
        "Native",
        "Installed",
        "Smallest change",
    ):
        assert label in ladder
    for guard in (
        "acceptance criteria",
        "public contracts",
        "trust boundaries",
        "data-loss handling",
        "security",
        "accessibility",
        "targeted tests",
    ):
        assert guard in skill_text
    assert "Do not invent abstractions, dependencies, configuration" in skill_text
    assert "Do not activate this skill automatically" in skill_text
