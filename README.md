# Audienti Codex Marketplace

This repository is the public source for the `audienti` Codex marketplace.

The marketplace starts empty on purpose:

- The catalog at `.agents/plugins/marketplace.json` is valid and public-ready.
- The `plugins/` directory is present but intentionally contains no plugins yet.
- `exo` is not scaffolded or listed here yet.

## Repository layout

- `.agents/plugins/marketplace.json` defines the marketplace metadata and plugin catalog.
- `plugins/` is where future marketplace plugins will live.
- `scripts/validate_marketplace.py` validates the marketplace catalog and plugin-path integrity.
- `.github/workflows/validate-marketplace.yml` runs the validator on pushes and pull requests.
- `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md`, and `CODE_OF_CONDUCT.md` define public repo hygiene.

## Current status

There are no published plugins in this repository yet. Add plugins only when they are ready to be represented honestly in the marketplace catalog.

## Maintainer workflow

1. Add a real plugin under `plugins/<plugin-name>/`.
2. Add the matching entry to `.agents/plugins/marketplace.json`.
3. Run `python3 scripts/validate_marketplace.py`.
4. Update `CHANGELOG.md` for any user-visible repository or catalog change.
5. Open a pull request with the relevant docs updates.

## Repository standards

- Keep the marketplace honest. Do not add placeholder plugins, future entries, or marketing-only listings.
- Keep each plugin folder name aligned with the marketplace entry name.
- Use relative local paths in the catalog as `./plugins/<plugin-name>`.
- Treat documentation and changelog updates as part of the change, not follow-up work.

## License

This repository does not yet include a `LICENSE` file. That decision should be made explicitly by the repository owner before public publication.
