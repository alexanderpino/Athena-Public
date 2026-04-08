#!/usr/bin/env python3
"""
net_indexer.py - .NET Project Rainbow Indexer
Generates a searchable JSON index of all .NET projects in a given directory (e.g., C:\repos).
Extracts project names, paths, project references, and derives keywords.
"""

import os
import json
import xml.etree.ElementTree as ET
from pathlib import Path

# Target directory to scan
TARGET_DIR = Path("C:/repos")

# Output path for the index
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
OUTPUT_FILE = PROJECT_ROOT / ".context" / "NET_PROJECT_INDEX.json"

def parse_csproj(filepath: Path) -> dict:
    """Parse a .csproj file to extract references and infer keywords."""
    project_name = filepath.stem
    repo_folder = ""
    try:
        # Determine the top-level folder inside C:\repos
        rel_path = filepath.relative_to(TARGET_DIR)
        repo_folder = rel_path.parts[0] if len(rel_path.parts) > 0 else ""
    except ValueError:
        pass

    references = []
    packages = []
    
    try:
        # Parse XML
        tree = ET.parse(filepath)
        root = tree.getroot()
        
        # Handle default namespace if present (often in older .NET Framework projects)
        ns = ''
        if root.tag.startswith('{'):
            ns = root.tag.split('}')[0] + '}'

        # Find ProjectReferences
        for proj_ref in root.findall(f".//{ns}ProjectReference"):
            include_path = proj_ref.attrib.get("Include")
            if include_path:
                ref_name = Path(include_path).stem
                references.append(ref_name)
                
        # Find PackageReferences (NuGet)
        for pkg_ref in root.findall(f".//{ns}PackageReference"):
            include_pkg = pkg_ref.attrib.get("Include")
            if include_pkg:
                packages.append(include_pkg)

    except Exception as e:
        print(f"Warning: Failed to parse {filepath}: {e}")

    # Derive keywords from project name and repo folder
    keywords = set()
    keywords.add(repo_folder.lower())
    
    # Split project name by dots and camel case roughly
    parts = project_name.replace('.', ' ').split()
    for part in parts:
        keywords.add(part.lower())
        
    if "Test" in project_name or "Tests" in project_name:
        keywords.add("testing")
        
    if "Api" in project_name:
        keywords.add("api")
        keywords.add("backend")
        
    if "Mvc" in project_name or "Client" in project_name or "Frontend" in project_name:
        keywords.add("frontend")
        keywords.add("ui")

    return {
        "project_name": project_name,
        "repository": repo_folder,
        "file_path": str(filepath),
        "project_references": sorted(list(set(references))),
        "package_references": sorted(list(set(packages))),
        "keywords": sorted(list(keywords))
    }

def main():
    print(f"🔍 Scanning {TARGET_DIR} for .NET projects (.csproj)...")
    
    if not TARGET_DIR.exists():
        print(f"❌ Target directory {TARGET_DIR} does not exist.")
        return

    projects = []
    for root, _, files in os.walk(TARGET_DIR):
        # Skip common ignored directories
        if any(ignored in root for ignored in [".git", "node_modules", "bin", "obj", "packages", ".venv"]):
            continue
            
        for file in files:
            if file.endswith(".csproj"):
                filepath = Path(root) / file
                project_data = parse_csproj(filepath)
                projects.append(project_data)

    print(f"✅ Found and parsed {len(projects)} projects.")
    
    # Group by repository for easier lookup
    index = {
        "metadata": {
            "total_projects": len(projects),
            "scan_dir": str(TARGET_DIR)
        },
        "projects_by_repo": {}
    }
    
    for p in projects:
        repo = p["repository"]
        if repo not in index["projects_by_repo"]:
            index["projects_by_repo"][repo] = []
        index["projects_by_repo"][repo].append(p)

    # Ensure output directory exists
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
        
    print(f"💾 Saved index to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
