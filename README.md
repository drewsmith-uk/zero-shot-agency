# Zero-Shot Agency

The Definitive Generative Engine Optimization (GEO) & AI Search Consultancy. 
We build open-source tools and workflows for autonomous SEO/AIO, managing the shift to LLM-native search.

## Work With Us

Want to become the #1 cited authority across Perplexity, ChatGPT, Claude, and Gemini? 
Get in touch to discuss an audit or strategy brief.

- **General:** [hello@zeroshotagency.com](mailto:hello@zeroshotagency.com)
- **Drew Smith:** [drew@zeroshotagency.com](mailto:drew@zeroshotagency.com)

Check out our [website](https://zeroshotagency.com) for our full playbook and automated workflows.

## Structured Agentic Gap Analysis

Run a single private-by-default prompt analysis:

```bash
python3 onboarding_agent.py --analyze-gaps "What is Generative Engine Optimization?" \
  --gap-target-page docs/strategy.md \
  --gap-output-dir .agentic_gap_analysis
```

Run a batch from CSV/JSON/JSONL. Each row must include `prompt`, `intent`,
`target_entity_page`, `priority`, `source`, and `date_collected`:

```bash
python3 onboarding_agent.py --gap-batch prompts.csv --gap-output-dir .agentic_gap_analysis
```

The runner writes structured evidence JSON, review-pending content briefs, and
measurement rows under the output directory. It does not publish raw evidence or
briefs into `docs/` by default; generated briefs stay `review_status: pending`
until Drew explicitly approves a public content change.
