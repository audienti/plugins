# Marketplace Architecture

The `audienti` marketplace repository is a catalog of plugins, not the place where plugin source code lives.

## Model

- This repository owns marketplace metadata and curation.
- Each plugin lives in its own upstream Git repository.
- Marketplace entries point to those repositories with `source.source: "url"` and `source.url`.
- Plugin manifests, skills, hooks, MCP config, apps, assets, tests, and release work stay with the plugin repo.

## Why

- Plugin repositories can evolve independently.
- Ownership stays with the team that maintains the plugin.
- Marketplace changes stay small and reviewable.
- The catalog remains honest: it lists installable plugins instead of half-scaffolded local folders.

## Expected entry shape

Future plugin entries in `.agents/plugins/marketplace.json` should follow this pattern:

```json
{
  "name": "example-plugin",
  "source": {
    "source": "url",
    "url": "https://github.com/example/example-plugin.git"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

## Rules for adding a plugin

- The upstream repository must already exist.
- The repository URL should be a public `https://` Git URL ending in `.git`.
- Do not add placeholder, speculative, or pre-announcement entries.
- Update marketplace docs and changelog in the same pull request as the catalog change.
