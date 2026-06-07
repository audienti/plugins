# Audienti Codex Marketplace

This repository is the public source for the `audienti` Codex marketplace catalog.

The marketplace starts empty on purpose:

- The catalog at `.agents/plugins/marketplace.json` is valid and public-ready.
- This repository does not contain plugin implementation code.
- `exo` is not scaffolded or listed here yet.

## Repository layout

- `.agents/plugins/marketplace.json` defines the marketplace metadata and plugin catalog.
- `docs/marketplace-architecture.md` explains how this marketplace points to plugin repos hosted elsewhere.
- `scripts/validate_marketplace.py` validates the marketplace catalog and external source contract.
- `.github/workflows/validate-marketplace.yml` runs the validator on pushes and pull requests.
- `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` define public repo hygiene.

## Current status

There are no published plugins in this repository yet. Add plugins only when they are ready to be represented honestly in the marketplace catalog.

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

## Repository standards

- Keep the marketplace honest. Do not add placeholder plugins, future entries, or marketing-only listings.
- Keep plugin implementation code in the upstream plugin repository, not in this repo.
- Use public `https://...git` repository URLs in marketplace entries.
- Treat documentation and changelog updates as part of the change, not follow-up work.

## License

This repository does not yet include a `LICENSE` file. That decision should be made explicitly by the repository owner before public publication.
