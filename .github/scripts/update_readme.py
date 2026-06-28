import os

def generate_terminal_content():
    # You can easily extend this function later to fetch live data from 
    # APIs (e.g., LeetCode milestones, GitHub API, or a database)
    content = """```bash
$ python3 -m ai_agent --profile overview

> [Initializing Core Parameters...] Success.
> [Task]: Fetching active developer profile metrics.

📊 Engineering Metrics:
  ├── Core Frameworks  : FastAPI, React, PostgreSQL, MongoDB, Tailwind CSS
  ├── Specialized Focus : Multi-Agent Frameworks, RAG Systems, Adaptive Learning Engines
  └── System State     : Actively building, optimizing, and scaling backend architectures

🤖 Agent Recommendation: Ready for full-stack deployment and intelligent tool integration.
```"""
    return content

def update_readme():
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print("README.md not found!")
        return

    with open(readme_path, "r", encoding="utf-8") as file:
        readme_text = file.read()

    start_tag = "<!-- START_DYNAMIC_SECTION -->"
    end_tag = "<!-- END_DYNAMIC_SECTION -->"

    if start_tag not in readme_text or end_tag not in readme_text:
        print("Marker tags missing from README.md!")
        return

    # Extract text before and after the dynamic section
    before_part = readme_text.split(start_tag)[0]
    after_part = readme_text.split(end_tag)[1]

    # Generate the fresh terminal log
    dynamic_content = generate_terminal_content()

    # Reassemble the file with new data
    new_readme = f"{before_part}{start_tag}\n{dynamic_content}\n{end_tag}{after_part}"

    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(new_readme)
        
    print("README.md successfully updated with latest metrics!")

if __name__ == "__main__":
    update_readme()
