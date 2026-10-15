"""Portable source layout and distribution resource regression tests."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile
SCRIPT=Path(__file__).resolve().parents[1]/"scripts/suite.py"
spec=importlib.util.spec_from_file_location("portable_suite",SCRIPT)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
from test_suite import fixture
class PortableSuiteTests(unittest.TestCase):
    def test_agents_layout_validation(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);fixture(root);(root/'.agents').mkdir();shutil.move(str(root/'.codex/skills'),str(root/'.agents/skills'))
            self.assertEqual(mod.validate_suite(root)['errors'],[])
    def test_alternative_layout_packages_canonical_skill_paths(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'source';fixture(root);(root/'.agents').mkdir();shutil.move(str(root/'.codex/skills'),str(root/'.agents/skills'))
            output=Path(d)/'bundle.zip';mod.build_bundle(root,output)
            with zipfile.ZipFile(output) as z:self.assertIn('.codex/skills/novel-router/SKILL.md',z.namelist())
    def test_installer_and_license_are_in_bundle(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'source';skill=fixture(root)
            (skill/'scripts').mkdir();(skill/'scripts/init-project.mjs').write_text('export {};')
            (root/'LICENSE').write_text('MIT');(root/'README.en.md').write_text('English')
            output=Path(d)/'bundle.zip';mod.build_bundle(root,output)
            with zipfile.ZipFile(output) as z:
                for name in ('.codex/skills/novel-router/scripts/init-project.mjs','LICENSE','README.en.md'):self.assertIn(name,z.namelist())
if __name__=='__main__':unittest.main()
