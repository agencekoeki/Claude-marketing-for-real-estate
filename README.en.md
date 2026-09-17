# AI toolkit for real-estate agents

**Five skills for Claude, written in French for French real-estate agents: set up the agent's profile, work on client types and the client journey, write property listings, prepare social media posts and carousels, and separate what is known from what is assumed.**

> Built by **Sébastien Grillot** for his AI training for real-estate agents, with **Boost Academy**.
> Independent project: Claude is a trademark of Anthropic; this project is neither affiliated with nor endorsed by Anthropic.

## Install

- **Claude Desktop or claude.ai** — Customize › **Plugins** tab (not Connectors) › **Add** › **Add marketplace** › **Add from a repository**, paste `https://github.com/agencekoeki/Claude-marketing-for-real-estate` and confirm to sync, then click **Add** next to **Mallette immo**: it should list 5 skills.
- **claude.ai** — download the five files — `.zip` or `.skill`, same content — from the [latest release](https://github.com/agencekoeki/Claude-marketing-for-real-estate/releases/latest) and upload them one by one under Customize › Skills.
- **Claude Code** — `/plugin marketplace add agencekoeki/Claude-marketing-for-real-estate`, then `/plugin install mallette-immo@sebastien-grillot`. The scripts need Python 3; carousels also need reportlab, Pillow and pypdf.

A paid Claude plan and code execution are required. The skills, their outputs and the documentation are in French.

## Author

**Sébastien Grillot** — SEO & AI consultant, trainer, founder of Koeki.
[About](https://sebastiengrillot.com/a-propos/) · [LinkedIn](https://www.linkedin.com/in/consultant-seo-ia-automatisation/) · [Boost Academy](https://boostacademy.ai/)

## License

GPL 3.0 — see [LICENSE](LICENSE). The bundled Liberation Sans font remains under the SIL Open Font License 1.1.

[Lire en français](README.md)
