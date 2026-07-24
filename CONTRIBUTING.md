# Contributing to Antigravity Hardened Ruleset Suite

Thank you for your interest in contributing! We welcome technical contributions, rule optimizations, and bug reports.

## 🛠️ Development Guidelines

1. **Ruleset Quality & Structure**: 
   - All rulesets must be written in clean, semantic Markdown.
   - Prompts must maintain character integrity and enforce step-by-step reasoning without introducing unnecessary boilerplate text that causes prompt drift.

2. **Switcher Engine Integration**:
   - If you add or modify a ruleset file in `.agents/`, update `set-rules.py`'s `RULES_MAP` and `ORDERED_MODELS`.
   - Maintain cross-platform path resolution using dynamic environment variables and `os.path`.

## 🧪 Testing Guidelines

Before submitting a Pull Request, please test your changes:
1. Run `python set-rules.py all` to verify that the unified `AGENTS.md` is generated cleanly.
2. Run `set-rules.bat` in a command shell to ensure menu options `[1-8]` function as expected.
3. Verify that active rules load under Antigravity GUI/TUI without configuration syntax errors.

---

## 🔒 Security Policy

For security vulnerability reporting, please see [SECURITY.md](SECURITY.md).
