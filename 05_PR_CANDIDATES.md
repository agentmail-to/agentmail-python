# PR Candidates - agentmail-python

## Open Issues and PRs Summary

| # | Type | Title | Priority | Difficulty | Status |
|---|------|-------|----------|------------|--------|
| 8 | Issue | Add nix package for reproducible builds | Medium | Medium | Needs Review |
| 7 | Issue | feat: add nix support | Medium | Medium | Needs Review |
| 6 | Issue | BUG: Missing contributor with SDK expertise | Low | N/A | Not applicable |
| 5 | Issue | feat: add MIT License | High | Low | Can submit PR |
| 4 | Issue | fix: fix grammar and syntax issues | Low | Low | Can submit PR |
| 2 | Issue | README: Fix broken code block formatting | Medium | Low | Can submit PR |

## Candidate Analysis

### Issue #2 - README: Fix broken code block formatting
- **Type**: Documentation fix (readme only)
- **Difficulty**: Low
- **Risk**: Very low (readme only)
- **Status**: Has PR #2 open already but not merged
- **Action**: Can improve or verify the existing PR

### Issue #4 - fix: fix grammar and syntax issues  
- **Type**: Code quality
- **Difficulty**: Low
- **Risk**: Low (small fixes)
- **Status**: Has PR #4 open but not merged
- **Action**: Review if PR addresses actual issues

### Issue #5 - feat: add MIT License
- **Type**: License compliance
- **Difficulty**: Low
- **Risk**: Low (adding license file)
- **Status**: Has PR #5 open but not merged
- **Note**: pyproject.toml already shows MIT license - may already be resolved
- **Action**: Verify if LICENSE file exists and is correct

### Issue #7/#8 - Nix support
- **Type**: Platform support / packaging
- **Difficulty**: Medium
- **Risk**: Medium (new files)
- **Two approaches**: In-repo flake vs separate packaging repo
- **Recommendation**: Separate repo recommended by issue author (more maintainable)

## Quick Wins (README-only or trivial)

1. **README code block fix** - Verify existing PR #2 is correct
2. **License verification** - Check if LICENSE file actually exists in repo
3. **Grammar fixes** - Review PR #4 contents

## Quality Audit Findings

| Check | Result | Notes |
|-------|--------|-------|
| Tests | ✅ | 27 passed, 1 skipped |
| Type check | ✅ | mypy clean |
| Lint | ⚠️ | 2 fixable ruff issues (import sorting) |
| License | ⚠️ | pyproject.toml says MIT but no LICENSE file found |

## Ruff Issues Found
1. `src/agentmail/core/query_encoder.py` - unsorted imports
2. `tests/utils/test_query_encoding.py` - unsorted imports