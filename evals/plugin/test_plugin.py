"""Tests for the AEGIS Claude Code plugin: .claude-plugin/plugin.json and marketplace.json.

Run: python evals/plugin/test_plugin.py
"""
import json
import shutil
import subprocess
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PLUGIN = REPO / ".claude-plugin" / "plugin.json"
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def as_list(value):
    return value if isinstance(value, list) else [value]


class Manifest(unittest.TestCase):
    def test_paths_reuse_the_repos_files(self):
        m = load(PLUGIN)
        self.assertEqual(m["name"], "aegis")
        for rel in as_list(m["skills"]) + as_list(m["agents"]):
            self.assertTrue(rel.startswith("./"), rel)
            self.assertTrue((REPO / rel).exists(), rel)
        self.assertEqual(as_list(m["skills"]), ["./.claude/skills/"])
        self.assertEqual(as_list(m["agents"]), ["./.claude/agents/ux-persona.md"])
        self.assertFalse((REPO / "skills").exists() or (REPO / "agents").exists(), "no copies")

    def test_hooks_match_the_project_settings(self):
        """The same events, matchers and guard modes, run from the plugin's root."""
        def shape(hooks, run):
            return {event: [(g.get("matcher"), [run(h) for h in g["hooks"]]) for g in groups]
                    for event, groups in hooks.items()}

        settings = load(REPO / ".claude" / "settings.json")["hooks"]
        plugin = load(PLUGIN)["hooks"]
        prefix = '"$CLAUDE_PROJECT_DIR/.claude/hooks/aegis-guard.sh" '
        expected = shape(settings, lambda h: ["sh", "${CLAUDE_PLUGIN_ROOT}/.claude/hooks/aegis-guard.sh",
                                              h["command"].split(prefix, 1)[1]])
        self.assertEqual(shape(plugin, lambda h: [h["command"], *h.get("args", [])]), expected)

    def test_marketplace_lists_the_repo_as_the_plugin(self):
        mk = load(MARKETPLACE)
        self.assertEqual(mk["name"], "aegis-core")
        self.assertEqual([(p["name"], p["source"]) for p in mk["plugins"]], [("aegis", ".")])
        self.assertIn("name", mk["owner"])


@unittest.skipUnless(shutil.which("claude"), "claude CLI not installed")
class Validate(unittest.TestCase):
    def test_claude_plugin_validate(self):
        for target in (REPO, MARKETPLACE):
            p = subprocess.run(["claude", "plugin", "validate", str(target)], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", shell=False)
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=1)
