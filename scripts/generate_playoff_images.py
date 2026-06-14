#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_playoff_schedule import MATCHES, Match, to_ufa  # noqa: E402

OUT_DIR = Path("ЧМ 2026/Плей-офф/Картинки")

HEADER_BG = (24, 72, 150)
ROW_BG = (8, 18, 36)
ROW_ALT_BG = (11, 24, 46)
BORDER = (28, 58, 102)
TEXT = (245, 248, 255)

COLUMNS = [
    ("Дата (Уфа)", 108),
    ("Время", 88),
    ("Матч", 430),
    ("Гр.", 72),
    ("Город", 250),
]

STAGE_CODE = {
    "1/16 финала": "1/16",
    "1/8 финала": "1/8",
    "1/4 финала": "1/4",
    "1/2 финала": "1/2",
    "Матч за 3-е место": "3-е",
    "Финал": "Фин",
}

STAGE_IMAGE = {
    "01. 1-16 финала (время Уфа).txt": "01. 1-16 финала (время Уфа).png",
    "02. 1-8 финала (время Уфа).txt": "02. 1-8 финала (время Уфа).png",
    "03. 1-4 финала (время Уфа).txt": "03. 1-4 финала (время Уфа).png",
    "04. 1-2 финала (время Уфа).txt": "04. 1-2 финала (время Уфа).png",
    "05. Матч за 3-е место и финал (время Уфа).txt": "05. Матч за 3-е место и финал (время Уфа).png",
}

CITY_DISPLAY = {
    "Санта-Клара": "Сан-Франциско",
    "Нью-Джерси": "Нью-Йорк/Нью-Джерси",
    "Ист-Разерфорд, Нью-Джерси": "Нью-Йорк/Нью-Джерси",
    "Арлингтон": "Даллас",
}


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def format_side(code: str) -> str:
    if code.startswith("W"):
        return f"Поб. М{code[1:]}"
    if code.startswith("L"):
        return f"Проиг. М{code[1:]}"
    return code


def format_match(pairing: str) -> str:
    left, right = pairing.split(" vs ", 1)
    return f"{format_side(left)} — {format_side(right)}"


def format_city(city: str) -> str:
    return CITY_DISPLAY.get(city, city)


def match_row(match: Match) -> tuple[str, str, str, str, str]:
    ufa = to_ufa(match.kickoff_utc)
    return (
        ufa.strftime("%d.%m"),
        ufa.strftime("%H:%M"),
        format_match(match.pairing),
        STAGE_CODE[match.stage],
        format_city(match.city),
    )


def draw_cell_text(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    h: int,
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    align: str = "center",
) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    if align == "left":
        tx = x + 12
    else:
        tx = x + max(8, (w - tw) // 2)
    ty = y + (h - th) // 2 - 1
    draw.text((tx, ty), text, fill=TEXT, font=font)


def render_table(rows: list[tuple[str, str, str, str, str]], output: Path) -> None:
    row_h = 40
    header_h = 44
    width = sum(col[1] for col in COLUMNS) + 2
    height = header_h + row_h * len(rows) + 2

    image = Image.new("RGB", (width, height), ROW_BG)
    draw = ImageDraw.Draw(image)
    header_font = load_font(18, bold=True)
    body_font = load_font(17)

    x0 = 1
    y = 1
    for idx, (title, col_w) in enumerate(COLUMNS):
        x = x0 + sum(c[1] for c in COLUMNS[:idx])
        draw.rectangle((x, y, x + col_w, y + header_h), fill=HEADER_BG, outline=BORDER, width=1)
        bbox = draw.textbbox((0, 0), title, font=header_font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((x + (col_w - tw) // 2, y + (header_h - th) // 2 - 1), title, fill=TEXT, font=header_font)

    y += header_h
    for row_idx, row in enumerate(rows):
        bg = ROW_BG if row_idx % 2 == 0 else ROW_ALT_BG
        for col_idx, value in enumerate(row):
            x = x0 + sum(c[1] for c in COLUMNS[:col_idx])
            draw.rectangle((x, y, x + COLUMNS[col_idx][1], y + row_h), fill=bg, outline=BORDER, width=1)
            align = "left" if col_idx == 2 else "center"
            draw_cell_text(draw, x, y, COLUMNS[col_idx][1], row_h, value, body_font, align=align)
        y += row_h

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, format="PNG", optimize=True)


def generate_images() -> list[Path]:
    grouped: dict[str, list[Match]] = {}
    for match in MATCHES:
        grouped.setdefault(match.stage_file, []).append(match)

    created: list[Path] = []
    for stage_file, stage_matches in grouped.items():
        stage_matches = sorted(stage_matches, key=lambda match: to_ufa(match.kickoff_utc))
        rows = [match_row(match) for match in stage_matches]
        output = OUT_DIR / STAGE_IMAGE[stage_file]
        render_table(rows, output)
        created.append(output)

    full_rows = [match_row(match) for match in sorted(MATCHES, key=lambda m: to_ufa(m.kickoff_utc))]
    full_output = OUT_DIR / "Расписание плей-офф (полное, время Уфа).png"
    render_table(full_rows, full_output)
    created.append(full_output)
    return created


def main() -> None:
    paths = generate_images()
    print(f"Generated {len(paths)} images in {OUT_DIR}/")
    for path in paths:
        print(f"  - {path}")


if __name__ == "__main__":
    main()
