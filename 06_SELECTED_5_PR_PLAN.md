# Agentmail Python - Selected 5 PR Plan

## Quick Fixes Ready to Submit

### PR Candidate 1: Fix Ruff Import Sorting Issues
- **Files**: `src/agentmail/core/query_encoder.py`, `tests/utils/test_query_encoding.py`
- **Issue**: Unsorted imports (ruff I001)
- **Status**: ✅ Already fixed locally
- **Action**: Commit and push to fork, then create PR against upstream

### PR Candidate 2: Add LICENSE file (MIT)
- **Issue**: #5 - pyproject.toml says MIT but no LICENSE file exists
- **Status**: Missing file needs to be created
- **License text**: Standard MIT License
- **Action**: Create LICENSE file and submit PR

## Two-Track Approach

### Track A: Quick Documentation/Quality Fixes (Low Risk)
These are safe, small changes that only touch documentation or lint fixes:

1. **Import sorting fix** - Already applied, just needs commit/push
2. **LICENSE file addition** - Simple file creation
3. **README code block fix** - Verify existing PR or improve

### Track B: Nix Support (Higher Complexity)
- Issues #7 and #8 both request Nix support
- Recommendation: Separate packaging repo (not in-tree)
- Not recommended for this campaign due to complexity

## Action Items

- [ ] 1. Fix import sorting → commit → push → PR
- [ ] 2. Create LICENSE file → commit → push → PR  
- [ ] 3. Verify README code block issue (#2)
- [ ] 4. Update PR candidate docs

## Summary

| Priority | Action | Risk | Effort |
|----------|--------|------|--------|
| High | Fix ruff import sorting | Very Low | 5 min |
| High | Add LICENSE file | Very Low | 5 min |
| Medium | Verify README fix | Low | 10 min |