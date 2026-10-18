# Sources and provenance

Research date: 2026-10-19.

## Public references

- [DeepSeek Harness: code review](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/skills/dsh-code-review/SKILL.md)
- [DeepSeek Harness: upgrade guides](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/.agents/skills/dsh-create-upgrade-guide/SKILL.md)

## Design decision

The local comparison stays separate from the agent's semantic interpretation and document editing.

## Distribution

KarmenLoop wrote these instructions, helpers, examples, tests, and packaging. No upstream source tree, model weights, proprietary prompts, logos, or credentials are bundled. Python's standard library is the only runtime dependency.

Links identify research sources, not endorsement or certification. GitHub references are pinned to the revisions reviewed. Meta's Muse announcement describes a product; it does not establish that the personal-agent implementation is available as source.

Any future imported code must record its exact revision, files, copyright, license, and modifications in NOTICE.md.
