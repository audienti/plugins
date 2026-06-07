# Adding a Plugin

This guide explains how to add a new plugin to the `audienti` marketplace when the plugin itself lives in a separate Git repository.

## What belongs here

This repository only owns the marketplace catalog and curation rules.

- Add plugin entries to `.agents/plugins/marketplace.json`.
- Do not copy plugin source code into this repository.
- Do not add speculative entries for plugins that are not ready yet.

## Before you add a plugin

Confirm the upstream plugin repository is actually ready to be listed.

Minimum bar:

- The repository already exists and is reachable as a public `https://...git` URL.
- The repository is the real source of truth for the plugin.
- The plugin is installable from that repository, not just planned.
- The repository contains the plugin manifest at `.codex-plugin/plugin.json`.
- Manifest metadata is real, not placeholder text.
- Any referenced skills, MCP config, app config, assets, and documentation are committed in that plugin repo.
- The plugin name in the upstream manifest matches the marketplace entry you plan to add.

If any of those are false, the plugin is not ready for this marketplace yet.

## Marketplace entry template

Add a new object to the `plugins` array in `.agents/plugins/marketplace.json`:

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

Required rules:

- `name` must be a non-empty string.
- `source.source` must be `"url"`.
- `source.url` must be an absolute `https://` Git repository URL ending in `.git`.
- `policy.installation` must be one of `NOT_AVAILABLE`, `AVAILABLE`, or `INSTALLED_BY_DEFAULT`.
- `policy.authentication` must be one of `ON_INSTALL` or `ON_USE`.
- `category` must be a non-empty string.

## How to add a plugin

1. Verify the upstream plugin repo is ready using the checklist above.
2. Open `.agents/plugins/marketplace.json`.
3. Append the new plugin entry to the `plugins` array.
4. Keep the entry honest and minimal. Do not add fields that the marketplace does not use.
5. Run `python3 scripts/validate_marketplace.py`.
6. Update `CHANGELOG.md` with the marketplace change.
7. If the addition changes workflow or curation rules, update `README.md` or other docs in the same branch.
8. Open a pull request with the catalog change, docs change, and changelog entry together.

## Worked example

If the marketplace is currently empty:

```json
{
  "name": "audienti",
  "interface": {
    "displayName": "Audienti"
  },
  "plugins": []
}
```

Then adding one plugin should look like:

```json
{
  "name": "audienti",
  "interface": {
    "displayName": "Audienti"
  },
  "plugins": [
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
  ]
}
```

## Choosing policy values

Use the policy fields deliberately.

### `policy.installation`

- `AVAILABLE`: Normal default. Use this for standard marketplace plugins that users may install.
- `INSTALLED_BY_DEFAULT`: Use only for a deliberately preinstalled core plugin. This should be rare.
- `NOT_AVAILABLE`: Use only when you intentionally want the entry present but not installable. In most cases, removal is cleaner than leaving a dead listing.

### `policy.authentication`

- `ON_INSTALL`: Default choice. Use when setup should happen as part of installation.
- `ON_USE`: Use when authentication can wait until the first real action.

## Choosing a category

Categories are curation labels, not marketing copy.

- Prefer reusing existing categories before inventing new ones.
- Use `Engineering` for developer tooling, code workflows, CI, debugging, or technical automation.
- Use `Productivity` for operational workflows, communication, task execution, or general business utility.
- Use `Research` for investigation, synthesis, analysis, or information-gathering tools.
- Use `Sales` for prospecting, pipeline, account research, buyer research, and go-to-market execution.

If a plugin does not fit any current category, add a new category intentionally and keep the label plain.

## Updating an existing plugin entry

Update an existing entry when the plugin remains in the marketplace but its metadata changed.

Typical reasons:

- The repository moved to a new URL.
- The category needs correction.
- Installation or authentication policy changed.
- The plugin name in the marketplace needs to match the upstream manifest.

Procedure:

1. Edit the existing object in `.agents/plugins/marketplace.json`.
2. Confirm the new `source.url` resolves to the correct upstream repository.
3. Run `python3 scripts/validate_marketplace.py`.
4. Record the change in `CHANGELOG.md`.
5. Include a short explanation in the pull request for why the metadata changed.

## Removing a plugin

Remove a plugin entry when it should no longer be discoverable through this marketplace.

Typical reasons:

- The plugin repository is gone or no longer public.
- The plugin is deprecated and should not be offered anymore.
- Ownership changed and the plugin no longer belongs in this marketplace.
- The listing was added too early and should be rolled back.

Procedure:

1. Delete the plugin object from `.agents/plugins/marketplace.json`.
2. Run `python3 scripts/validate_marketplace.py`.
3. Record the removal in `CHANGELOG.md`.
4. Explain the removal briefly in the pull request.

## Review checklist

Before merging a plugin catalog change, confirm all of the following:

- The plugin is real and installable from its upstream repository.
- The marketplace entry name matches the upstream plugin name.
- The `source.url` is public, correct, and ends in `.git`.
- The chosen `policy` values are intentional.
- The chosen `category` is sensible and consistent.
- `python3 scripts/validate_marketplace.py` passes.
- `CHANGELOG.md` is updated.
- Any related docs updates are included in the same branch.
