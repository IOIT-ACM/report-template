# ACM Student Chapter Event & Annual Report LaTeX System

---

## 1. Purpose

The objective is to design a LaTeX-based reporting system for the student chapter that supports:

- **Independent authoring and compilation of individual event reports**
- **Seamless aggregation of all event reports into a single annual report PDF**

The system must ensure correctness, consistency, scalability, and ease of use for contributors, while strictly preserving institutional formatting rules.

---

## 2. Core Requirement

Each **event report must exist as a single self-contained LaTeX file** that can operate correctly in **two compilation contexts**:

1. **Standalone compilation (individual event report)**
2. **Embedded compilation (as part of the annual report)**

The behavior of the same `.tex` file must automatically adapt based on the compilation context, without requiring content duplication or manual modification by contributors.

---

## 3. Requirements for Individual Event Reports (Standalone Mode)

When an event report is compiled on its own:

1. The report **must generate a complete, submission-ready PDF**, including:

   - A dedicated title page
   - A table of contents
   - A list of figures
   - A list of tables
   - All required report sections as defined by the template

2. **Page numbering must be local to the event report**:

   - Page numbers must start at page 1
   - Roman/Arabic numbering (if used) must apply only to that report
   - Headers and footers must reflect the event report’s own layout

3. **Indexing scope must be local**:

   - The table of contents must list only the sections of that event
   - The list of figures and tables must include only figures and tables from that event
   - Page references in all indices must correspond to the event report’s own page numbers

4. The file must remain:

   - Fully compilable in isolation
   - Easy for contributors to edit
   - Compliant with all institutional non-negotiable formatting rules

---

## 4. Requirements for Annual Report Compilation (Embedded Mode)

When the same event report file is included in the annual report:

1. **The event report must not render its own front matter**, including:

   - Title page
   - Table of contents
   - List of figures
   - List of tables

2. **The event report must not control or reset page numbering**:

   - No page number resets
   - No standalone page counters
   - No standalone headers or footers

3. **All page numbers must be governed exclusively by the annual report template**:

   - Continuous pagination across all events
   - Page numbers referenced in the annual report TOC must reflect the annual report’s page sequence
   - Event reports must inherit the annual report’s headers and footers

4. **Indexing must be global, not local**:

   - Event sections must appear in the annual report’s table of contents
   - Individual event TOCs, lists of figures, and lists of tables must not be rendered
   - Figures and tables from events must contribute to the annual report’s global lists (if enabled)

5. Each event report must appear as a **logical structural unit** (e.g., a section or chapter-like block) within the annual report, without visual duplication or layout conflicts.

---

## 5. Annual Report Template Responsibilities

The annual report template must be the **single source of truth** for:

1. Document class and page geometry
2. Global page numbering and counters
3. Headers and footers
4. Global table of contents
5. Global list of figures and tables
6. Overall document structure and ordering of events

The annual report must include event reports only via `\input{}` or equivalent mechanisms and must not require modification of event content files.

---

## 6. Contributor Workflow Requirements

1. Contributors must:

   - Edit only one `.tex` file per event
   - Never need to remove, comment out, or alter structural elements for annual compilation
   - Be able to compile and verify their event report independently

2. Contributors must not be required to:

   - Understand the annual report architecture
   - Manage page numbering or indexing logic
   - Maintain multiple versions of the same report

---

## 7. Maintainability and Scalability Requirements

1. The system must support:

   - Any number of events without structural changes
   - Easy addition or removal of event reports in the annual document
   - Reuse across academic years

2. The solution must not rely on:

   - Manual PDF merging
   - Post-compilation editing
   - External tooling outside LaTeX

---

## 8. Explicit Non-Goals (Out of Scope)

The system must **not**:

- Maintain separate “standalone” and “annual” versions of the same event report
- Require contributors to manually toggle content blocks
- Duplicate report content across files
- Break institutional formatting constraints defined in the template

---

## 9. One-Paragraph Summary

The system must allow each event report to function as a fully independent document with its own correct pagination and indices when compiled alone, while automatically suppressing all local front matter and pagination when embedded into an annual report, so that the annual report maintains a single, continuous page numbering and global indices—without requiring duplicate files or manual intervention.
