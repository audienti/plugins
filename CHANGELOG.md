# Changelog

All notable changes to this repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Added the `exo` plugin to the marketplace catalog.
- Added the `signal-prospect-research` plugin to the marketplace catalog.
- Added the `plan-loop-executor` plugin to the marketplace catalog.
- Added proprietary copyright and attribution license notice.
- Added a Claude Code marketplace catalog at `.claude-plugin/marketplace.json` listing `plan-loop-executor` and `signal-prospect-research`.

### Changed

- Updated the `signal-prospect-research` marketplace source URL to `https://github.com/audienti/signal-research.git`.
- Corrected the repository architecture docs to reflect a catalog-only marketplace that points to external plugin repositories.
- Updated marketplace validation to enforce external `source.url` entries instead of local plugin-folder assumptions.
- Added an end-to-end maintainer guide for adding, updating, and removing marketplace plugins.
- Extended marketplace validation to cover the Claude Code catalog and cross-check it against the Codex catalog.
- Documented the dual-catalog (Codex and Claude Code) maintainer workflow.

## [0.1.0] - 2026-06-07

### Added

- Initialized the public `audienti` Codex marketplace repository.
- Added a valid empty marketplace catalog at `.agents/plugins/marketplace.json`.
- Added repository documentation and public-repo maintenance files.
- Added a marketplace validation script and GitHub Actions validation workflow.
