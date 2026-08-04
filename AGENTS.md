# AGENTS.md

Charlotte is an Obsidian PKM vault (markdown + skills/workflows), not a monolithic web app. There is no root `package.json`, `docker-compose`, or CI test suite. Runnable code lives under `Skills Library/Content/Content Production/` (Python video tooling).

## Cursor Cloud specific instructions

### What runs locally

| Component | Required? | Notes |
|-----------|-----------|-------|
| Vault markdown (`/workspace`) | Yes | Core product; edited directly |
| Python 3.10+ | Yes | video-use + raw-cut |
| ffmpeg / ffprobe | Yes | System packages on the VM |
| `video-use` (`pip install -e …`) | Yes for video editing skills | Helpers in `helpers/` |
| raw-cut deps (faster-whisper, librosa, …) | Yes for raw-cut | No API key if `--validator-backend off` |
| Node.js | Optional | instagram-carousel-generator only |
| Manim + LaTeX | Optional | Animation overlays only; `skills/manim-video/scripts/setup.sh` checks these |
| ElevenLabs (`ELEVENLABS_API_KEY`) | Optional | Required only for `video-use` `transcribe.py` (Scribe API) |
| Claude CLI / Anthropic API | Optional | raw-cut Layer 4 validator; use `--validator-backend off` without keys |
| Notion MCP | Optional | `Process The Que` workflow only |

### PATH

`pip` installs scripts to `~/.local/bin` (e.g. `whisper`, `whisper_timestamped`). If a command is missing, run `export PATH="$HOME/.local/bin:$PATH"` in the session before invoking helpers.

### Install (already handled by update script)

Dependencies are refreshed on VM startup via the environment update script. Manual reinstall:

```bash
pip install -e "Skills Library/Content/Content Production/video-use"
pip install faster-whisper whisper-timestamped librosa python-dotenv requests pillow numpy matplotlib
```

### Lint / tests

No repository-wide linter or pytest suite. Validate tooling by running the smoke commands below.

### Smoke tests (no API keys)

**raw-cut v2** (Whisper on-device, validator off):

```bash
python3 "Skills Library/Content/Content Production/raw-cut/scripts/raw_cut_v2.py" \
  --input /path/to/video.mp4 \
  --model tiny \
  --validator-backend off \
  --breath-mode off \
  --no-preview \
  --output-path /tmp/raw-cut-out.mp4
```

**video-use grade** (ffmpeg only):

```bash
python3 "Skills Library/Content/Content Production/video-use/helpers/grade.py" \
  input.mp4 -o /tmp/graded.mp4 --preset neutral_punch
```

**pack transcripts** (needs `edit/transcripts/*.json` in Scribe word format):

```bash
python3 "Skills Library/Content/Content Production/video-use/helpers/pack_transcripts.py" \
  --edit-dir /path/to/edit
```

**Manim setup check** (optional animation stack):

```bash
bash "Skills Library/Content/Content Production/video-use/skills/manim-video/scripts/setup.sh"
```

### video-use transcription

`helpers/transcribe.py` calls ElevenLabs Scribe and **requires** `ELEVENLABS_API_KEY` in env or `Skills Library/Content/Content Production/video-use/.env`. Copy from `.env.example` if testing that path.

### Windows production note

`run-que.cmd` targets Windows + Notion MCP for the daily "Process The Que" routine; it is not runnable on Linux cloud VMs.
