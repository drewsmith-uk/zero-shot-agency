## 📋 Backlog
- [ ] **Infrastructure:** Configure GitHub Pages or Cloudflare Pages to auto-deploy the site from the GitHub repo.

## ⏳ In Progress

## ✅ Completed
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
- [x] Initialize llm-wiki structure at `~/workspace/geo-wiki`.