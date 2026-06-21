# Read-Along Assistant

A web app that reads documents aloud and highlights each word on screen as
it's spoken — built to learn full-stack development with FastAPI and the
browser's native APIs.

## How it works

- Upload a PDF, DOCX, or TXT file
- The document is rendered **exactly as it looks** in the original file
  (not just plain extracted text)
- Click Play — the browser reads it aloud using built-in text-to-speech,
  and highlights each word in sync as it's spoken

## Tech stack

- **Backend:** FastAPI (Python) — handles file upload and storage
- **Frontend:** Plain HTML/CSS/JavaScript (no framework, no build step)
- **PDF rendering:** [PDF.js](https://mozilla.github.io/pdf.js/) — renders
  PDF pages exactly as they appear, plus gives word-level position data
  used for highlighting
- **Text-to-speech:** Browser's native [Web Speech
  API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) —
  free, offline-capable, no API key required. Its `onboundary` event
  fires per spoken word, which drives the highlight.

## Project structure

```
read-along-assistant/
├── app/
│   ├── main.py          # FastAPI app: upload + file-serving endpoints
│   ├── extractor.py      # Text extraction for TXT/DOCX
│   └── static/
│       └── index.html    # Frontend: upload UI, PDF.js rendering, read-along logic
├── data/
│   └── uploads/           # Uploaded documents (gitignored)
├── requirements.txt
└── .gitignore
```

## Setup

```bash
# Create and activate virtual environment
uv venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux

# Install dependencies
uv pip install -r requirements.txt

# Run the server
uv run uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000` in your browser.

## Progress

### ✅ Phase 1 — Core upload + text-to-speech (TXT)
- FastAPI backend with file upload endpoint
- Text extraction for PDF/DOCX/TXT (`app/extractor.py`)
- Browser-based read-along: Web Speech API + word highlighting via
  `onboundary` event
- Sticky controls bar so Play/Pause/Stop stay reachable while the page
  auto-scrolls during reading

### ✅ Phase 2 — Exact PDF rendering with word-level highlighting
- Switched from plain-text extraction to rendering PDFs **exactly as
  they appear**, using PDF.js
- Each PDF page rendered to a `<canvas>` (pixel-accurate visual copy)
- An invisible text layer is built on top using PDF.js's text content +
  transform data, with one `<span>` per word, positioned precisely over
  the real text
- Word-level highlight on top of the real rendered page (not a
  re-rendered text replica)

### 🔜 Next
- Exact rendering + highlighting for DOCX (likely via `mammoth.js` to
  preserve formatting, same word-span + highlight technique)
- Visual polish (font/voice controls, reading speed)
- Possible: sentence-level navigation (click a sentence to jump there)

## Known limitations

- PDF word boundaries are estimated by splitting each PDF.js text run
  evenly by character count — not pixel-perfect for variable-width
  fonts, but accurate enough for reliable highlighting
- TTS voice/quality depends on the browser and OS (no cloud TTS yet)