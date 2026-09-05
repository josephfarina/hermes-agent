"""Contract tests for the bundled simplify-code skill."""

import re
from pathlib import Path

import pytest


SKILL_MD = Path(__file__).resolve().parents[2] / "skills/software-development/simplify-code/SKILL.md"


@pytest.fixture(scope="module")
def skill_text() -> str:
    return SKILL_MD.read_text(encoding="utf-8")


def _value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    assert match, f"missing frontmatter field: {key}"
    return match.group(1).strip()


def test_frontmatter_preserves_source_credit(skill_text: str) -> None:
    description = _value(skill_text, "description")
    assert len(description) <= 60
    assert description.strip('"').endswith(".")
    author = _value(skill_text, "author")
    assert author.startswith("Joey Farina (josephfarina)")
    assert "Hermes Agent (inspired by Claude Code /simplify)" in author


def test_standard_flow_still_reviews_and_applies(skill_text: str) -> None:
    assert "Launch four reviewers in parallel" in skill_text
    for reviewer in ("Code Reuse", "Code Quality", "Efficiency", "Altitude"):
        assert reviewer in skill_text
    assert "**SAFE first** (auto-apply)" in skill_text
    assert "**CAREFUL next** (apply with verification" in skill_text
    assert "**RISKY last** (flag for review — do NOT auto-apply)" in skill_text
    assert "If the user opted for a dry run" in skill_text


def test_deletion_first_integrates_with_focus_and_fanout(skill_text: str) -> None:
    assert "single narrow reviewer instead of the normal four" in skill_text
    assert "never adds a fifth\n  reviewer" in skill_text
    assert "Only when the user explicitly selects" in skill_text


def test_dry_run_uses_focus_selected_reviewer_set(skill_text: str) -> None:
    modifiers = skill_text.split("Optional modifiers", 1)[1].split("## The Process", 1)[0]
    assert "reviewer set selected by Focus" in modifiers
    assert "four by default" in modifiers
    assert "one read-only\n  reviewer for `deletion-first`" in modifiers
    assert "apply NOTHING" in modifiers

    deletion = skill_text.split("### Deletion-first focus", 1)[1].split(
        "### Phase 3", 1
    )[0]
    assert "Do not wait for four\nreviewers or apply changes" in deletion
    assert "including when dry run is also specified" in deletion


def test_deletion_first_findings_have_required_contract(skill_text: str) -> None:
    deletion = skill_text.split("### Deletion-first focus", 1)[1].split(
        "### Phase 3", 1
    )[0]
    for tag in ("`delete`", "`stdlib`", "`native`", "`yagni`", "`shrink`"):
        assert tag in deletion
    for field in ("evidence", "confidence", "(`SAFE`/`CAREFUL`/`RISKY`)"):
        assert field in deletion
    assert "Chesterton's Fence" in skill_text
    for protected in (
        "real tests",
        "security controls",
        "trust-boundary validation",
        "data-loss safeguards",
        "accessibility behavior",
        "public contracts",
    ):
        assert protected in deletion
    assert "must not edit files or apply suggestions" in deletion
