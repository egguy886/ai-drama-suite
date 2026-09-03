#!/usr/bin/env python3
"""
Install Skills for supported Agent platforms:
- codex: ~/.codex/skills/
- claude-code: ~/.claude/skills/
- trae / antigravity: .agents/skills/
"""

import os
import sys
import shutil
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
EXP_ROOT = ROOT / "experimental"

def get_target_path(platform: str) -> Path:
    home = Path.home()
    if platform == "codex":
        return home / ".codex" / "skills"
    elif platform == "claude-code":
        return home / ".claude" / "skills"
    elif platform in ["trae", "antigravity", "generic"]:
        return Path.cwd() / ".agents" / "skills"
    else:
        raise ValueError(f"Unknown platform: {platform}")

def list_skills():
    print("Available Skills:")
    for base in [SKILLS_ROOT, EXP_ROOT]:
        if base.exists():
            for child in sorted(base.iterdir()):
                if child.is_dir() and (child / "SKILL.md").exists():
                    status = "experimental" if base == EXP_ROOT else "stable"
                    print(f"  - {child.name} [{status}]")

def install(skill_name: str, platform: str):
    source = SKILLS_ROOT / skill_name
    if not source.exists():
        source = EXP_ROOT / skill_name
    if not source.exists():
        print(f"[ERROR] Skill '{skill_name}' not found!")
        sys.exit(1)
        
    target_dir = get_target_path(platform)
    target_dir.mkdir(parents=True, exist_ok=True)
    dest = target_dir / skill_name
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(source, dest)
    print(f"[SUCCESS] Installed {skill_name} -> {dest}")

def main():
    parser = argparse.ArgumentParser(description="Install AI Film Skills")
    parser.add_argument("skill", nargs="?", help="Skill directory name")
    parser.add_argument("--list", action="store_true", help="List available skills")
    parser.add_argument("--platform", default="trae", choices=["codex", "claude-code", "trae", "antigravity", "generic"])
    args = parser.parse_args()
    
    if args.list or not args.skill:
        list_skills()
        return
        
    install(args.skill, args.platform)

if __name__ == "__main__":
    main()
