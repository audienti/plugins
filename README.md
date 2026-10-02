# Audienti Codex Marketplace

This repository is the public source for the `audienti` Codex marketplace catalog.

The marketplace is intentionally small and catalog-only:

- The catalog at `.agents/plugins/marketplace.json` is the source of truth for published plugin listings.
- This repository does not contain plugin implementation code.
- Each marketplace entry should point at a real upstream plugin repository.

## Repository layout

- `.agents/plugins/marketplace.json` defines the marketplace metadata and plugin catalog.
- `docs/marketplace-architecture.md` explains how this marketplace points to plugin repos hosted elsewhere.
- `docs/adding-a-plugin.md` explains how to add, update, and remove marketplace entries.
- `scripts/validate_marketplace.py` validates the marketplace catalog and external source contract.
- `.github/workflows/validate-marketplace.yml` runs the validator on pushes and pull requests.
- `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` define public repo hygiene.

## Install

Add the marketplace once, then install any plugin listed below by name.

### Claude Code

In a Claude Code session:

```text
/plugin marketplace add audienti/plugins
/plugin install reddit-pain-finder@audienti
```

Or from your terminal:

```bash
claude plugin marketplace add audienti/plugins
claude plugin install reddit-pain-finder@audienti
```

Swap `reddit-pain-finder` for any plugin name below. Run `/plugin` with no
name to browse everything in the marketplace. If the install says to check your
access rights, run it again with `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` set. That
makes Claude Code download over HTTPS instead of SSH.

### Codex

From your terminal:

```bash
codex plugin marketplace add audienti/plugins
codex plugin add reddit-pain-finder@audienti
```

Swap `reddit-pain-finder` for any plugin name below, or type `/plugins` inside
Codex to browse and install from the `audienti` marketplace.

Each plugin runs on your own Claude or Codex account. Some plugins work better
with outside tools (for example Apify for live Reddit search). Each plugin's
README lists what you'll need.

## Current status

The marketplace publishes ten plugins for Codex. Nine of them are also listed
for Claude Code.

| Plugin | What it does | Source | Claude Code | Codex |
|---|---|---|---|---|
| `reddit-pain-finder` | Finds Reddit threads where your buyers are describing the problem you solve, and drafts a helpful reply. | [audienti/reddit-pain-finder](https://github.com/audienti/reddit-pain-finder) | Yes | Yes |
| `signal-prospect-research` | Turns what you sell into a ranked list of companies showing the problem now, plus who to talk to at each. | [audienti/signal-research](https://github.com/audienti/signal-research) | Yes | Yes |
| `linkedin-pain-finder` | Finds LinkedIn posts where buyers are talking about the problem, worth engaging now. | [audienti/linkedin-pain-finder](https://github.com/audienti/linkedin-pain-finder) | Yes | Yes |
| `twitter-signal-finder` | Finds posts on X (Twitter) worth engaging now. | [audienti/twitter-signal-finder](https://github.com/audienti/twitter-signal-finder) | Yes | Yes |
| `instagram-comment-finder` | Finds Instagram posts and comments worth engaging now. | [audienti/instagram-comment-finder](https://github.com/audienti/instagram-comment-finder) | Yes | Yes |
| `facebook-comment-finder` | Finds Facebook posts and comments worth engaging now. | [audienti/facebook-comment-finder](https://github.com/audienti/facebook-comment-finder) | Yes | Yes |
| `tiktok-comment-finder` | Finds TikTok videos and comments worth engaging now. | [audienti/tiktok-comment-finder](https://github.com/audienti/tiktok-comment-finder) | Yes | Yes |
| `sales-sheet-builder` | Builds a short, clear one-page sales sheet for an offer, plus a separate research workbook. | [audienti/sales-sheet-builder](https://github.com/audienti/sales-sheet-builder) | Yes | Yes |
| `exo` | Runs go-to-market plays from inside Codex. | [audienti/exo](https://github.com/audienti/exo) | No (the repo has no Claude Code manifest yet) | Yes |
| `plan-loop-executor` | Works through a written build plan one tested step at a time (for engineering). | [audienti/plan-loop-executor](https://github.com/audienti/plan-loop-executor) | Yes | Yes |

Add plugins only when they are ready to be represented honestly in the marketplace catalog.

## Architecture

This repository is a catalog, not a monorepo for plugin source.

- Marketplace entries belong in `.agents/plugins/marketplace.json`.
- Each plugin entry should point to a separate public Git repository using `source.url`.
- Each plugin repository owns its own plugin manifest, skills, MCP/app config, assets, and release cadence.
- This repository should not accumulate plugin code under a local `plugins/` tree.

## Maintainer workflow

1. Prepare the real plugin in its own public Git repository.
2. Add the matching marketplace entry to `.agents/plugins/marketplace.json`.
3. Run `python3 scripts/validate_marketplace.py`.
4. Update `CHANGELOG.md` for any user-visible repository or catalog change.
5. Open a pull request with the relevant docs updates.

For the full procedure, see `docs/adding-a-plugin.md`.

## Repository standards

- Keep the marketplace honest. Do not add placeholder plugins, future entries, or marketing-only listings.
- Keep plugin implementation code in the upstream plugin repository, not in this repo.
- Use public `https://...git` repository URLs in marketplace entries.
- Treat documentation and changelog updates as part of the change, not follow-up work.

## License

Copyright (c) 2026 OMALab, Inc. All rights reserved.

This marketplace catalog is not open source. Wholesale copying, redistribution,
resale, or publication of substantial portions requires prior written
permission. Fair use, short quotations, references, summaries, links, and
commentary are not limited; attribution to OMALab, Inc. and a link to this
repository are requested when quoting or referencing the work.
