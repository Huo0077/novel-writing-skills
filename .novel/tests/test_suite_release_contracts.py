import json
from pathlib import Path
import unittest
import yaml
ROOT=Path(__file__).resolve().parents[2]
class ReleaseContracts(unittest.TestCase):
    def test_router_catalog_matches_actual_skills_and_routes(self):
        router=ROOT/".codex/skills/novel-router"
        catalog=json.loads((router/"references/catalog.json").read_text(encoding="utf-8"))
        actual={p.parent.name for p in (ROOT/".codex/skills").glob("novel-*/SKILL.md")}
        self.assertEqual({x["name"] for x in catalog["skills"]},actual);self.assertEqual(len(actual),31)
        for route in catalog["routes"]:
            self.assertTrue(route["chain"]);self.assertTrue(set(route["chain"])<=actual)
        text=(router/"SKILL.md").read_text(encoding="utf-8")
        for value in ("输入","输出","novel-canon","reader","references/routes.md","references/operations.md"):self.assertIn(value,text)
    def test_seed_resources_match_and_exclude_live_story(self):
        seed=ROOT/".codex/skills/novel-router/assets/project-seed/.novel"
        for name in ("schemas","templates"):
            src=ROOT/".novel"/name
            self.assertEqual({p.name for p in src.glob("*.md")},{p.name for p in (seed/name).glob("*.md")})
            for p in src.glob("*.md"):self.assertEqual(p.read_bytes(),(seed/name/p.name).read_bytes())
        project=yaml.safe_load((seed/"project.yaml").read_text(encoding="utf-8"))
        self.assertEqual(project["title"],"未命名小说");self.assertEqual(project["mode"],"author_assistant")
        self.assertEqual(project["current"]["chapter"],0)
        self.assertFalse(list((seed/"drafts").rglob("*.md")))
        self.assertFalse(list((seed/"proposals").rglob("*.yaml")))
if __name__ == "__main__":unittest.main()
