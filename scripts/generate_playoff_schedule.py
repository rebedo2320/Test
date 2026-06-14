#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path

TZ_UFA = "Asia/Yekaterinburg (UTC+5, YEKT)"
ROOT = Path("ЧМ 2026/Плей-офф")

MONTHS_RU = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}


@dataclass(frozen=True)
class Match:
    number: int
    stage: str
    stage_file: str
    pairing: str
    venue: str
    city: str
    kickoff_utc: datetime


MATCHES: list[Match] = [
    # 1/16 финала (Round of 32)
    Match(73, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "2-A vs 2-B", "SoFi Stadium", "Лос-Анджелес", datetime(2026, 6, 28, 19, 0)),
    Match(76, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-C vs 2-F", "NRG Stadium", "Хьюстон", datetime(2026, 6, 29, 17, 0)),
    Match(74, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-E vs 3-ABCDF", "Gillette Stadium", "Бостон", datetime(2026, 6, 29, 20, 30)),
    Match(75, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-F vs 2-C", "Estadio BBVA", "Монтеррей", datetime(2026, 6, 30, 1, 0)),
    Match(78, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "2-E vs 2-I", "AT&T Stadium", "Арлингтон", datetime(2026, 6, 30, 17, 0)),
    Match(77, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-I vs 3-CDFGH", "MetLife Stadium", "Нью-Джерси", datetime(2026, 6, 30, 21, 0)),
    Match(79, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-A vs 3-CEFHI", "Estadio Azteca", "Мехико", datetime(2026, 7, 1, 1, 0)),
    Match(80, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-L vs 3-EHIJK", "Mercedes-Benz Stadium", "Атланта", datetime(2026, 7, 1, 16, 0)),
    Match(82, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-G vs 3-AEHIJ", "Lumen Field", "Сиэтл", datetime(2026, 7, 1, 20, 0)),
    Match(81, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-D vs 3-BEFIJ", "Levi's Stadium", "Санта-Клара", datetime(2026, 7, 2, 0, 0)),
    Match(84, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-H vs 2-J", "SoFi Stadium", "Лос-Анджелес", datetime(2026, 7, 2, 19, 0)),
    Match(83, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "2-K vs 2-L", "BMO Field", "Торонто", datetime(2026, 7, 2, 23, 0)),
    Match(88, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "2-D vs 2-G", "AT&T Stadium", "Арлингтон", datetime(2026, 7, 3, 18, 0)),
    Match(86, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-J vs 2-H", "Hard Rock Stadium", "Майами", datetime(2026, 7, 3, 22, 0)),
    Match(85, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-B vs 3-DFGIJ", "BC Place", "Ванкувер", datetime(2026, 7, 3, 3, 0)),
    Match(87, "1/16 финала", "01. 1-16 финала (время Уфа).txt", "1-K vs 3-DEIJL", "Arrowhead Stadium", "Канзас-Сити", datetime(2026, 7, 4, 1, 30)),
    # 1/8 финала (Round of 16)
    Match(90, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W73 vs W75", "NRG Stadium", "Хьюстон", datetime(2026, 7, 4, 17, 0)),
    Match(89, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W74 vs W77", "Lincoln Financial Field", "Филадельфия", datetime(2026, 7, 4, 21, 0)),
    Match(91, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W76 vs W78", "MetLife Stadium", "Нью-Джерси", datetime(2026, 7, 5, 20, 0)),
    Match(92, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W79 vs W80", "Estadio Azteca", "Мехико", datetime(2026, 7, 6, 0, 0)),
    Match(93, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W83 vs W84", "AT&T Stadium", "Арлингтон", datetime(2026, 7, 6, 19, 0)),
    Match(94, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W81 vs W82", "Lumen Field", "Сиэтл", datetime(2026, 7, 6, 23, 0)),
    Match(95, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W86 vs W88", "Mercedes-Benz Stadium", "Атланта", datetime(2026, 7, 7, 16, 0)),
    Match(96, "1/8 финала", "02. 1-8 финала (время Уфа).txt", "W85 vs W87", "BC Place", "Ванкувер", datetime(2026, 7, 7, 20, 0)),
    # 1/4 финала
    Match(97, "1/4 финала", "03. 1-4 финала (время Уфа).txt", "W89 vs W90", "Gillette Stadium", "Бостон", datetime(2026, 7, 9, 20, 0)),
    Match(98, "1/4 финала", "03. 1-4 финала (время Уфа).txt", "W93 vs W94", "SoFi Stadium", "Лос-Анджелес", datetime(2026, 7, 10, 19, 0)),
    Match(99, "1/4 финала", "03. 1-4 финала (время Уфа).txt", "W91 vs W92", "Hard Rock Stadium", "Майами", datetime(2026, 7, 10, 21, 0)),
    Match(100, "1/4 финала", "03. 1-4 финала (время Уфа).txt", "W95 vs W96", "Arrowhead Stadium", "Канзас-Сити", datetime(2026, 7, 11, 1, 0)),
    # 1/2 финала
    Match(101, "1/2 финала", "04. 1-2 финала (время Уфа).txt", "W97 vs W98", "AT&T Stadium", "Арлингтон", datetime(2026, 7, 14, 19, 0)),
    Match(102, "1/2 финала", "04. 1-2 финала (время Уфа).txt", "W99 vs W100", "Mercedes-Benz Stadium", "Атланта", datetime(2026, 7, 15, 19, 0)),
    # Матч за 3-е место и финал
    Match(103, "Матч за 3-е место", "05. Матч за 3-е место и финал (время Уфа).txt", "L101 vs L102", "Hard Rock Stadium", "Майами", datetime(2026, 7, 18, 21, 0)),
    Match(104, "Финал", "05. Матч за 3-е место и финал (время Уфа).txt", "W101 vs W102", "MetLife Stadium", "Ист-Разерфорд, Нью-Джерси", datetime(2026, 7, 19, 19, 0)),
]

STAGE_HEADERS = {
    "01. 1-16 финала (время Уфа).txt": "1/16 финала (Round of 32) — 28 июня — 4 июля",
    "02. 1-8 финала (время Уфа).txt": "1/8 финала (Round of 16) — 4–7 июля",
    "03. 1-4 финала (время Уфа).txt": "1/4 финала — 9–12 июля",
    "04. 1-2 финала (время Уфа).txt": "1/2 финала — 14–15 июля",
    "05. Матч за 3-е место и финал (время Уфа).txt": "Матч за 3-е место и финал — 18–20 июля",
}


def to_ufa(dt_utc: datetime) -> datetime:
    return dt_utc + timedelta(hours=5)


def format_date_ru(dt: datetime) -> str:
    return f"{dt.day} {MONTHS_RU[dt.month]}"


def format_time(dt: datetime) -> str:
    return dt.strftime("%H:%M")


def format_row(match: Match) -> str:
    ufa = to_ufa(match.kickoff_utc)
    return (
        f"| {format_date_ru(ufa)} | {format_time(ufa)} | "
        f"М{match.number}: {match.pairing} | {match.venue}, {match.city} |"
    )


def stage_intro(stage_file: str) -> str:
    lines = [
        "ЧМ-2026 — плей-офф",
        f"Часовой пояс: {TZ_UFA}",
        "",
        "Обозначения:",
        "  1-A / 2-B — место в группе; 3-ABCDF — лучшая из третьих мест указанных групп",
        "  W73 — победитель матча №73; L101 — проигравший полуфинала №1",
        "",
        STAGE_HEADERS[stage_file],
        "",
        "| Дата (Уфа) | Время (Уфа) | Матч | Стадион, город |",
        "| --- | --- | --- | --- |",
    ]
    return "\n".join(lines)


def write_stage_files() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[Match]] = {}
    for match in MATCHES:
        grouped.setdefault(match.stage_file, []).append(match)

    for stage_file, stage_matches in grouped.items():
        stage_matches = sorted(stage_matches, key=lambda match: to_ufa(match.kickoff_utc))
        content = stage_intro(stage_file) + "\n"
        content += "\n".join(format_row(match) for match in stage_matches)
        content += "\n"
        (ROOT / stage_file).write_text(content, encoding="utf-8")


def write_full_schedule() -> None:
    lines = [
        "ЧМ-2026 — полное расписание плей-офф",
        f"Часовой пояс: {TZ_UFA}",
        "Источник: официальная сетка FIFA / расписание матчей 73–104",
        "",
        "Стадии:",
        "  1/16 финала — 28 июня – 4 июля",
        "  1/8 финала — 4–7 июля",
        "  1/4 финала — 9–12 июля",
        "  1/2 финала — 14–15 июля",
        "  Матч за 3-е место — 19 июля",
        "  Финал — 20 июля (00:00 по Уфе)",
        "",
    ]

    current_stage = ""
    for match in MATCHES:
        if match.stage != current_stage:
            current_stage = match.stage
            lines.extend(["", f"## {current_stage}", ""])
            lines.extend(
                [
                    "| Дата (Уфа) | Время (Уфа) | Матч | Пара | Стадион, город |",
                    "| --- | --- | --- | --- | --- |",
                ]
            )
        ufa = to_ufa(match.kickoff_utc)
        lines.append(
            f"| {format_date_ru(ufa)} | {format_time(ufa)} | М{match.number} | "
            f"{match.pairing} | {match.venue}, {match.city} |"
        )

    (ROOT / "Расписание плей-офф (полное, время Уфа).txt").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def write_csv() -> None:
    lines = ["№;Стадия;Дата (Уфа);Время (Уфа);Пара;Стадион;Город"]
    for match in MATCHES:
        ufa = to_ufa(match.kickoff_utc)
        lines.append(
            f"{match.number};{match.stage};{format_date_ru(ufa)};{format_time(ufa)};"
            f"{match.pairing};{match.venue};{match.city}"
        )
    (ROOT / "Расписание плей-офф (полное, время Уфа).csv").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    write_stage_files()
    write_full_schedule()
    write_csv()
    print(f"Generated {len(MATCHES)} matches in {ROOT}/")


if __name__ == "__main__":
    main()
