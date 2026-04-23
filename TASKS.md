     ## 📋 Backlog
     
## ⏳ In Progress
     
## ✅ Completed
- [x] **Development:** The `geo_tracker.py` tool needs an automated Cron testing suite. Create a shell script wrapper that runs the tracker every day at 8:00 AM, saves the CSV output to `raw/tracker_history/`, and automatically commits the results to the repo. This builds our open-source, empirical data trail.
- [x] **Content:** Draft the "Daily Blog: Day 3" post. We successfully established a developer-grade "Drafts via Pull Request" publishing workflow. Explain how this architecture prevents "AI hallucination leaks" into production while maintaining full automation. Submit this as a Pull Request via GitHub CLI so Drew can review it before it merges.
- [x] **Development:** Enhance `geo_tracker.py`. Upgrade the script to hit the actual OpenAI and Anthropic APIs. It needs to run mock-queries to check for "Zero-Shot Agency" brand citations and output the results to a CSV file. (Note: Ralph is authorized to loop continuously on this task until the tool is fully robust and operational).
- [x] **Documentation:** Update the `docs/tools/index.md` file to include comprehensive documentation and usage instructions for the internal tools (currently `geo_tracker.py` and `llms-txt-generator.py`).
- [x] **Content:** Draft the "Daily Blog: Day 2" post. Focus on our tech stack architecture and our strategic decisions today (MkDocs, Material theme, Cloudflare Pages, Semantic HTML, LLM-native assets). Do not focus on the minor deployment hiccups.
- [x] **Bugfix:** Fix the `[[wikilinks]]` across the site documentation. Update either the markdown files or the MkDocs configuration so that internal links render properly as hyperlinks instead of literal bracket text.
- [x] **Infrastructure:** Build the fallback Direct Deployment Script. Since mobile GitHub auth is failing, write a script that uses the Cloudflare Wrangler CLI in the terminal to directly deploy the `zero-shot-agency` static site to Cloudflare Pages, bypassing the mobile browser loop entirely.
- [x] **Infrastructure:** Configure GitHub Pages or Cloudflare Pages to auto-deploy the site from the GitHub repo.
- [x] **Infrastructure:** Set up a lightweight static site generator (like Hugo or MkDocs) in the repo to serve the drafted homepage copy (`zero-shot-homepage-copy.md`) and the `llms.txt` file directly to the newly purchased `zeroshotagency.com` domain.
- [x] **Content:** Review and approve the Day 1 draft so the pipeline can publish it.
- [x] **Infrastructure:** Build the "Daily Publisher Pipeline". A script that takes an approved markdown draft and automatically pushes it to GitHub, posts it as a thread on X/Twitter (using `x-cli`), and emails it to Substack.
- [x] **Development:** Build the `llms-txt-generator.py` lead-magnet tool (a script that crawls a domain and generates a perfect `llms.txt` file) and place it in the tools/ directory.
- [x] **Infrastructure:** Configure the Ralph Loop bash script to automatically commit and push to the GitHub repository at the end of every successful task execution (so we build a verifiable public commit history of an AI agent working autonomously).
- [x] **Infrastructure:** Initialize a new public GitHub repository for "Zero-Shot Agency" to host our open-source tools and markdown blog posts.
- [x] **Content:** Draft the actual homepage copy using the semantic structure in `geo-semantic-structure.md`, for the brand **"Zero-Shot Agency"**.
- [x] **Content:** Setup the "Daily Collaboration Blog" format in the wiki, and draft the Day 1 post ("An AI and a Human start a GEO Agency").
- [x] **Strategy:** Defined core mission and narrative (The Human + AI Collaboration).
- [x] **Research:** Ingest and summarize the Princeton GEO paper into `raw/papers/` and extract tactics into `concepts/geo-tactics.md`.
- [x] **Research:** Analyze Perplexity/SearchGPT citation mechanics and create `concepts/citation-mechanics.md`.
- [x] **Content:** Draft the `llms.txt` standard template for the new website.
- [x] **Content:** Outline the H1/H2 semantic structure for the #1 GEO ranking website.
- [x] **Development:** Build the baseline GEO ranking tracker script to run against GPT-4o, Claude 3.5, and Gemini.
- [x] Initialize llm-wiki structure at `~/workspace/zero-shot-agency`.