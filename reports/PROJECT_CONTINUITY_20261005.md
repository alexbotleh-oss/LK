# B77 Project Continuity & Context Incident Report

Date: 2026-10-05
Repository: `alexbotleh-oss/LK`
Default branch: `main`
Project: **Б77**
Primary source of truth: ChatGPT Project **Б77**, including chat **«Б77 часть 3»** and project documents/history.
GitHub role: technical stack, debugging, history, verification and project reports; it is not the replacement for the ChatGPT Project source of truth.

## 1. Incident

During transition into a new ChatGPT chat, the assistant failed to use the already established project context from **«Б77 часть 3»** and incorrectly attempted to rediscover the repository from scratch.

Observed incorrect behavior:
- treated the repository as unknown;
- attempted a generic repository search;
- did not immediately use the repository already connected to the project;
- asked the user to provide the repository URL again;
- this contradicted the established project rule that the user must not be forced to repeat project data already present in the project context.

This is an **assistant context-continuity failure**, not a project-code failure.

## 2. Correct project context restored

The connected repository has been verified as:

`alexbotleh-oss/LK`

Current working project contour:
- HTML / PWA baseline: `stage14.html`
- project baseline identified in the project history as **HTML-poligon / core35**;
- verified Stage14 baseline commit: `e1eaf7cd20b1265f35a023c8c87db8b1994044f0`;
- GitHub Pages entrypoint was set to the verified Stage14;
- current `main` contains the later mobile scanner camera work;
- current latest relevant scanner commit: `e29c156544357ae998041d5f46c8571ffffba00f`;
- immutable pre-camera backup: `7e911a97dd95df6d08efb24b2eb39846efa0ce1c`;
- immutable WP backup: `6d9038eb0b37f53698074be7ea1a0dc3b1eb77eb`.

Frozen components:
- **Fix6/Flet — frozen, do not touch.**
- **Stage14-WP — frozen as working reference; do not replace with an unverified candidate.**
- **Core/business logic — do not rewrite.**

## 3. Scanner continuity rule

The verified camera implementation must feed the existing scanner/business chain:

`openScanner(context) → scanSubmit() → Core.findQR() → existing Products/Shopping/QR handler`

Rules:
- no second/new Core;
- no parallel business-result path;
- camera layer is an input layer only;
- preserve existing QR/EAN result handling;
- stop the camera stream correctly;
- preserve permission/error diagnostics.

The mobile camera patch is isolated to `stage14.html`: comparison of the pre-camera backup `7e911a97dd95df6d08efb24b2eb39846efa0ce1c` with `e29c156544357ae998041d5f46c8571ffffba00f` shows exactly one changed file, `stage14.html`, with 74 additions and 7 deletions.

## 4. Current repository evidence

Recent commits establish the project sequence:
- `e1eaf7cd20b1265f35a023c8c87db8b1994044f0` — Complete verified Stage14 HTML baseline.
- `108e373bc523f396626d3441635045c54ee757c0` — Set Pages entrypoint to verified Stage14.
- `bd346c3f81e728624a82182446c1284af3721e9b` — Audit mobile PWA v1.7.7.
- `7e911a97dd95df6d08efb24b2eb39846efa0ce1c` — immutable main backup before mobile scanner camera change.
- `e29c156544357ae998041d5f46c8571ffffba00f` — Add verified mobile scanner camera layer.

## 5. Required behavior for future chat transitions

When continuing B77 in a new ChatGPT chat, the assistant must:

1. First restore the project context from the ChatGPT Project **Б77**, especially the latest relevant chat/history and project documents.
2. Treat the established project context as the primary source of truth.
3. Use the already connected GitHub repository without asking the user to repeat its URL/name.
4. Use GitHub only to verify the technical state, files, commits, diffs and reports.
5. Continue from the latest verified checkpoint rather than restarting discovery.
6. Preserve frozen components and existing business logic.
7. If a required project detail is genuinely unavailable, state exactly which detail is missing; do not guess and do not ask for data that is already available in the project context.
8. Before any code change, identify the working baseline, backup/SHA, change boundary and regression checkpoints.
9. After a change, perform reverse-diff and regression verification and record the result in the project reports.

## 6. Status

**Incident recorded. Project context restored. Repository identified and verified.**

No application rollback is required because the incident concerned assistant behavior/context handling, not the B77 application code.
