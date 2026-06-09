from onboarding_agent import (
    GAP_TAXONOMY,
    build_measurement_row,
    classify_gap,
    load_prompt_batch,
    scrub_private_content,
)


def test_load_prompt_batch_from_csv_with_required_metadata(tmp_path):
    prompts_path = tmp_path / "prompts.csv"
    prompts_path.write_text(
        "prompt,intent,target_entity_page,priority,source,date_collected\n"
        "What is GEO?,informational,docs/concepts/generative-engine-optimization.md,1,strategy,2026-05-10\n",
        encoding="utf-8",
    )

    prompts = load_prompt_batch(prompts_path)

    assert prompts == [
        {
            "prompt": "What is GEO?",
            "intent": "informational",
            "target_entity_page": "docs/concepts/generative-engine-optimization.md",
            "priority": "1",
            "source": "strategy",
            "date_collected": "2026-05-10",
        }
    ]


def test_scrub_private_content_removes_tracking_emails_credentials_and_client_references():
    raw = (
        "Contact drew@example.com about Acme Corp private client audit at "
        "https://example.com/page?utm_source=x&sessionid=abc&ok=1 "
        "with api_key=test-redacted-token and password=hunter2."
    )

    scrubbed = scrub_private_content(raw)

    assert "drew@example.com" not in scrubbed
    assert "Acme Corp" not in scrubbed
    assert "private client" not in scrubbed.lower()
    assert "utm_source" not in scrubbed
    assert "sessionid" not in scrubbed
    assert "api_key" not in scrubbed
    assert "password" not in scrubbed
    assert "https://example.com/page" in scrubbed


def test_build_measurement_row_has_pending_review_shape():
    row = build_measurement_row(
        prompt={"prompt": "best GEO agency", "intent": "buyer", "source": "duckduckgo"},
        evidence={
            "zsa_present": True,
            "zsa_position": 3,
            "zsa_cited_url": "https://zero-shot.agency/strategy/?utm_source=test",
            "competitor_cited_urls": ["https://competitor.example/a?ref=tracker"],
        },
        gap_cluster="missing proof/statistic",
        recommended_artifact="Add proof-backed comparison brief",
        notes="Needs Drew review before publication",
        date="2026-05-10",
    )

    assert list(row) == [
        "date",
        "prompt",
        "intent",
        "engine/source",
        "zsa_present",
        "zsa_position",
        "zsa_cited_url",
        "competitor_cited_urls",
        "gap_cluster",
        "recommended_artifact",
        "review_status",
        "published_path",
        "notes",
    ]
    assert row["review_status"] == "pending"
    assert row["published_path"] == ""
    assert row["zsa_cited_url"] == "https://zero-shot.agency/strategy/"
    assert row["competitor_cited_urls"] == "https://competitor.example/a"


def test_classify_gap_detects_missing_citation_path():
    classification = classify_gap(
        prompt={"intent": "informational"},
        competitor_terms=["citation", "source", "statistic"],
        zsa_terms=["definition", "overview"],
    )

    assert classification in GAP_TAXONOMY
    assert classification == "missing citation"
