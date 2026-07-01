# Knowledge Management Framework

**Status:** Permanent operating framework. The Office's institutional memory.

> The knowledge base is the company's most-durable non-human asset. The Knowledge Management Framework is the discipline that makes the knowledge base defensible, durable, and re-installable.

---

## Repository Standards

The knowledge base is organised in a numbered folder structure. The folder structure is, in the Office's view, the most-effective single discipline for navigation.

**The folder hierarchy.** The knowledge base is organised as a numbered pipeline. Lower numbers feed higher numbers. The pipeline is, in the Office's view, the discipline that ensures the documents are, in the long run, consistent.

```
00_CONTEXT  →  01_FOUNDATION  →  02_BUSINESS  →  03_PRODUCT
                                                     │
                                                     ▼
                             05_MARKETING  ←  04_BRAND
                                                     │
                                                     ▼
                                              06_OPERATIONS
                                                     │
                                                     ▼
                                              07_EXECUTION
                                                     │
                                                     ▼
                                              08_INVESTOR

09_RESEARCH  (input, read on demand)
10_ARCHIVE   (history, read on demand)
98_STRATEGY_OFFICE  (permanent organisational function)
```

**Folder purpose.** Each folder has a defined purpose. The purpose is recorded in the README of the folder. A document that does not fit any folder's purpose is, in the Office's view, a document that should not be created.

**File naming.** Files use `PascalCase_With_Underscores.md`. Files do not include version numbers in the filename; versioning is in git. Files do not include dates in the filename, except for time-bound artefacts (investor updates, sprint reviews, decision log entries).

**Markdown standard.** All documents are written in CommonMark Markdown. No rich text, no proprietary formats, no embedded HTML beyond what is necessary for tables and code blocks.

The repository standards are, in the Office's view, the discipline that makes the knowledge base navigable.

---

## Versioning

Documents are versioned in git, not in the filename. The version discipline is, in the Office's view, the discipline that ensures the history of the document is preserved.

**Working version.** A working version of a document is the current version. The working version is, in effect, the company's position.

**Previous versions.** Previous versions of a document are preserved in git history. Previous versions are, in effect, the company's memory.

**Superseded versions.** Superseded versions of a document are moved to `10_ARCHIVE/`. Superseded versions are, in effect, the company's record of what the company used to believe.

**Versioning rules.** A new version is created when a document is significantly revised. A minor revision is recorded in the Decision Log. A major revision is recorded in the Decision Log and is, in addition, subject to the full review process.

The versioning discipline is, in the Office's view, the discipline that ensures the documents are, in the long run, auditable.

---

## Cross-References

Documents reference each other through relative paths. The cross-reference discipline is, in the Office's view, the discipline that ensures the knowledge base is, in the long run, navigable.

**Relative paths.** Cross-references use relative paths (`docs/02_BUSINESS/Business_Model.md`), not absolute paths. A document that is moved retains its cross-references.

**Link integrity.** Cross-references must resolve. A cross-reference that does not resolve is, in the Office's view, a broken link, and a broken link is, in the Office's view, a quality failure.

**Cross-reference at creation.** A document is cross-referenced from every relevant existing document at the time of its creation. A document that is not cross-referenced is, in the Office's view, an orphan, and an orphan is, in the Office's view, a quality failure.

**Cross-reference at revision.** A document's cross-references are updated at the time of its revision. A document whose cross-references are stale is, in the Office's view, a document that is, in effect, broken.

The cross-reference discipline is, in the Office's view, the discipline that ensures the knowledge base is, in the long run, navigable.

---

## Decision Logs

The Decision Log is the canonical record of the company's strategic and operational decisions. The Decision Log is, in the Office's view, the most-durable institutional asset.

**The Decision Log is append-only.** Decisions are added, not revised. A reversed decision is recorded as a new decision, not as a revision of the original.

**The Decision Log is in `00_CONTEXT/Decision_Log.md`.** The location is fixed. The location is, in the Office's view, the discipline that ensures the Decision Log is, in the long run, findable.

**The Decision Log is reviewed quarterly.** A Decision Log that is not reviewed is, in the Office's view, a Decision Log that is, in effect, abandoned.

**The Decision Log is the first document a new team member reads.** The Decision Log is, in the Office's view, the institutional memory that makes a new team member's onboarding possible.

The Decision Log discipline is, in the Office's view, the discipline that ensures the company is, in the long run, auditable.

---

## Future AI Usage

The knowledge base is, by design, AI-installable. A future AI agent that joins the company is, by the Office's standing rule, required to read, in order, before producing any output:

1. `docs/00_CONTEXT/FXTeller_Master_Context.md`
2. `docs/00_CONTEXT/AI_Writing_Guidelines.md`
3. `docs/00_CONTEXT/Glossary.md`
4. `docs/00_CONTEXT/Project_Status.md`
5. `docs/00_CONTEXT/Decision_Log.md`
6. The relevant specialist document(s) in `docs/98_STRATEGY_OFFICE/` for the question being asked
7. The relevant folder document(s) in `docs/01_FOUNDATION/` through `docs/10_ARCHIVE/` for the question being asked

The AI's first output is, when relevant, a one-sentence confirmation of what the AI has understood the task to be. The AI's outputs are, in effect, the AI's contribution to the Office, and the Office is, in effect, the AI's operating system.

The future-AI-usage discipline is, in the Office's view, the discipline that ensures the knowledge base is, in the long run, re-installable.

---

## Document Dependencies

Documents depend on each other. The dependency discipline is, in the Office's view, the discipline that ensures the documents are, in the long run, consistent.

**The dependency map.** The dependency map is recorded in the Strategy Office's Collaboration Framework. The map names the upstream documents and the downstream documents for every document in the knowledge base.

**The dependency check.** A document is checked for upstream consistency at the time of its creation and at the time of its revision. A document that contradicts an upstream document is, in the Office's view, a document that has, in effect, broken the knowledge base.

**The dependency update.** A document's downstream references are updated at the time of its revision. A document whose downstream references are stale is, in the Office's view, a document that is, in effect, broken.

The dependency discipline is, in the Office's view, the discipline that ensures the knowledge base is, in the long run, consistent.

---

## Knowledge Governance

The knowledge base is, in the long run, a company asset. The knowledge base has, in effect, owners, reviewers, and a governance discipline.

**Folder owners.** Each folder has a named owner. The owner is responsible for the folder's content, the folder's review cadence, and the folder's evolution.

**Review cadence.** Each folder has a defined review cadence. The review cadence is recorded in the Strategy Office's Collaboration Framework.

**Governance meetings.** The Office's governance meetings (weekly, monthly, quarterly, annual) review the knowledge base for currency, coherence, and completeness. The governance meetings are the discipline that ensures the knowledge base is, in the long run, current.

**Quality bar.** The knowledge base has a quality bar. The quality bar is the test that every document must pass to be, in effect, an active document. The quality bar is, in the Office's view, the discipline that ensures the knowledge base is, in the long run, defensible.

The knowledge governance discipline is, in the Office's view, the discipline that ensures the knowledge base is, in the long run, an institutional asset rather than a personal archive.

---

*End of Knowledge Management Framework.*
