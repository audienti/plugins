# Contributing

This repository is a public Codex marketplace, not a dumping ground for future ideas. Keep it accurate, reviewable, and publishable.

## Core rules

- Only add plugins that actually exist in their own upstream repositories.
- Do not add placeholder marketplace entries.
- Keep `.agents/plugins/marketplace.json` valid JSON and structurally correct.
- Use marketplace entries that point to public Git repositories with `source.source: "url"`.
- Use repository URLs in the form `https://... .git`.
- Update `CHANGELOG.md` for repository-visible changes.
- Update `README.md` when repository structure or maintainer workflow changes.

## Before opening a pull request

1. Run `python3 scripts/validate_marketplace.py`.
2. Confirm every catalog entry points to a real upstream plugin repository.
3. Confirm there are no stale or future-facing plugin listings.
4. Confirm docs and changelog changes are included in the same branch.

Use `docs/adding-a-plugin.md` as the operational checklist for plugin additions, updates, and removals.

## Pull request expectations

- Keep changes narrowly scoped.
- Prefer one plugin addition or one repository concern per pull request.
- Explain why the plugin belongs in this marketplace.
- Include any catalog, documentation, and validation changes together.
