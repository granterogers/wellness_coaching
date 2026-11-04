# Site content

- `en/home.md` — the homepage copy document: frontmatter with `status: draft` or `status: approved`, then one heading per section. Written and approved **before** the build (requirement 1.3).
- `es/home.md` — Spanish, translated after English is approved; `translation_status: draft` until a native speaker reviews it.
- `shared/site.json` — contact details, booking link, credentials, feature flags (created during the build, requirement 3.4).

The build uses this text word for word. Edit wording here, never in code.
