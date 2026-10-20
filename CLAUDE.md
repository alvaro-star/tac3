# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

`tac7` is the newest snapshot of the TAC pygame course engine (git history v0.0.1 → v0.1.0). It continues `tac6` (OpenGL rendering, animated player, sparse-matrix tile map) and adds a **level editor** (`source/modules/maker/`). The parent `../CLAUDE.md` describes the shared engine. This file covers what differs in tac7.

Code comments and identifiers mix Portuguese and English. Match the surrounding file.

## Running

Run everything from the `tac7/` root. Asset and data paths (`assets/...`, `source/data/...`) are relative to the CWD.

```bash
source .venv/bin/activate        # Python 3.14 venv (uv)
pip install -r requirements.txt  # file is UTF-16 LE encoded (pip handles it; use iconv to read it)
python main.py                   # fullscreen; ESC quits
python source/docs/generate.py   # UML via pyreverse -> docs/ (needs pylint + graphviz)
```

- Main dependencies: `pygame-ce` (not classic pygame), `PyOpenGL`, `numpy`, `scipy`, `cx_Freeze`.
- No tests, linter or `setup.py` exist in this folder. `docs/comandos.txt` still mentions `python setup.py build`.
- `exemplos/` holds standalone teaching scripts plus pygame's official examples (`exemplos/official/`). They are not imported by the game.

## Entry point: editor vs. game

`main.py` currently calls `editor.run()`. `engine.run()` (the game) is commented out. Switch between them there.

Importing `source.modules.engine` has side effects. `engine = GameEngine()` runs at import time and calls `display.create_display()`, loads sounds and calls `game.init_assets()`. `main.py` imports it even in editor mode, so the window is created twice (once by the engine import, once by `Editor.run()`). Also, `pygame.mixer.init()` runs when `config/sounds.py` is imported.

## Level data model

- `TileMap.load_sprite_maps()` (`entities/tiles.py`) cuts 16×16 crops from `assets/image/bg-1-1.png` into `codes`. **The list index is the tile id** stored in the map file. Index 0 is `None` (empty), and each entry is `(id, surface, desc)`. Adding a tile type means appending to `codes`. Reordering it breaks saved maps.
- `Level1` (`ui/levels.py`) keeps `self.tiles` as a dense 2D list, `tiles[lin][col]`, with `Tile` or `None`, sized `TILE_MAP_LEVEL1 = (500 cols, 100 rows)` from `constants.py`. Each `Tile` is scaled to 32×32 and positioned at `(col*TILE_SIZE, lin*TILE_SIZE)` in world space.
- Persistence: `source/data/level1.json` holds Tiled-like metadata. `source/data/lv1.npz` is a SciPy CSR matrix of tile ids. `Level1.save()` writes the npz from `self.tiles`.
- `Level1.load()` returns `False` if a file is missing. In that case it has already regenerated the default map with `create_first_map()`, and callers load a second time. The debug call to `create_first_map()` at the top of `load()` is now commented out, so editor saves persist. Uncommenting it wipes `lv1.npz` on every run.
- Every `Tile` creates its own GL texture in `__init__`, so building tiles is not free.

## Editor (`source/modules/maker/`)

`Editor` has its own loop (`handle_events` → `update` → `draw`) and its own event handling. It does not use `events/io.py` or the `game` singleton. Components:

- `Grid`: viewport onto the level. It shows `x_tiles × y_tiles` cells starting at `grid.anchor = [col, row]`, the scroll offset in tiles. Each viewport cell is a placeholder `Tile` whose `desc` is `"col,lin"`. Clicks translate viewport cell + anchor to map coordinates. Left click places the selected palette tile (always a **new** `Tile`, so rects aren't shared). Right click clears the cell.
- `Pallet`: lists `tile_map.codes[1:]`. `pallet.select` is the chosen `Tile`. Tile rects are local to the palette surface, so hit-testing adds `pallet.rect.topleft`.
- `Info`: FPS, grid size, map size and anchor overlay.
- `Button` (`buttons.py`): arrow buttons move the anchor, and "SALVAR" calls `level1.save()`. Arrow keys also move the anchor (once per frame while held).
- **Change notification** (`notify.py`): components subclass `Interested`. A `Notify(listeners, event_id)` pushes one of the int ids `Anchor`/`Select`/`Fill` into each listener's queue via `.event()`. Each component drains its queue in `update()` with `events_get()` and re-renders its surface only then. Trigger the matching `Notify` after mutating shared state (anchor, selection, level tiles), or nothing redraws.

## Rendering conventions (shared with tac6)

- Draw only via `utils.draw_textured_quad(texture_id, x, y, w, h)`. Nothing is blitted to the screen surface. Components compose a pygame `Surface` and upload it.
- Prefer `utils.update_texture(texture_id, surface)` to re-upload into an existing texture. `utils.surface_to_texture` allocates a new GL texture each call and never frees the old one (`Panel` and `Background.add_cenario` still leak this way).
- `glOrtho` uses logical `WIDTH×HEIGHT` (1920×1080), but the editor lays out UI with `display.size` (the monitor's real resolution). Both match only on a 1080p display.
- The game loop in `engine.run()` swallows exceptions (`print(e)` + exit). The editor loop has its try/except commented out, so its tracebacks surface normally.
