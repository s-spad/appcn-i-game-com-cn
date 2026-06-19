from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    url: str
    note: str
    timestamp: Optional[str] = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formatted_output(self, index: int = 0) -> str:
        lines = []
        lines.append(f"--- 笔记 #{index + 1} ---")
        lines.append(f"关键词 : {self.keyword}")
        lines.append(f"相关URL: {self.url}")
        lines.append(f"备注   : {self.note}")
        lines.append(f"记录时间: {self.timestamp}")
        lines.append("")
        return "\n".join(lines)


def batch_format_notes(notes: List[KeywordNote]) -> str:
    result_parts = []
    for i, note in enumerate(notes):
        result_parts.append(note.formatted_output(index=i))
    return "\n".join(result_parts)


def add_note(notes: List[KeywordNote], keyword: str, url: str, note: str) -> None:
    new_note = KeywordNote(
        keyword=keyword,
        url=url,
        note=note
    )
    notes.append(new_note)


def find_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    return [note for note in notes if note.keyword == keyword]


def show_summary(notes: List[KeywordNote]) -> str:
    if not notes:
        return "当前没有任何笔记。"
    unique_keywords = set(n.keyword for n in notes)
    lines = [f"总笔记数: {len(notes)}", f"不同关键词数: {len(unique_keywords)}"]
    for kw in sorted(unique_keywords):
        count = sum(1 for n in notes if n.keyword == kw)
        lines.append(f"  - {kw}: {count} 条")
    return "\n".join(lines)


def run_demo() -> None:
    sample_notes: List[KeywordNote] = []

    add_note(sample_notes, "爱游戏", "https://appcn-i-game.com.cn", "爱游戏官方平台，提供多种游戏下载与资讯")
    add_note(sample_notes, "爱游戏", "https://appcn-i-game.com.cn/news", "爱游戏新闻中心，最新游戏动态")
    add_note(sample_notes, "游戏攻略", "https://appcn-i-game.com.cn/guide", "包含热门游戏详细攻略")
    add_note(sample_notes, "玩家社区", "https://appcn-i-game.com.cn/community", "爱游戏玩家交流社区")

    print("===== 格式化输出全部笔记 =====")
    print(batch_format_notes(sample_notes))

    print("===== 按关键词查找 '爱游戏' =====")
    matched = find_notes_by_keyword(sample_notes, "爱游戏")
    if matched:
        for idx, note in enumerate(matched):
            print(note.formatted_output(index=idx))

    print("===== 总结统计 =====")
    print(show_summary(sample_notes))


if __name__ == "__main__":
    run_demo()