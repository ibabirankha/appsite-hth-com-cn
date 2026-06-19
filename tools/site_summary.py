import json
import sys


SITE_RECORDS = [
    {
        "title": "华体会官方入口",
        "url": "https://appsite-hth.com.cn",
        "keywords": ["体育", "电竞", "真人", "华体会"],
        "tags": ["首页", "综合娱乐", "官方站点"],
        "description": "华体会综合娱乐平台，提供体育赛事、电子竞技及真人娱乐服务。"
    },
    {
        "title": "华体会体育专区",
        "url": "https://appsite-hth.com.cn/sports",
        "keywords": ["华体会", "足球", "篮球", "网球", "体育投注"],
        "tags": ["体育", "投注", "赛事"],
        "description": "涵盖足球、篮球、网球等主流体育赛事的实时投注与比分服务。"
    },
    {
        "title": "华体会电竞版块",
        "url": "https://appsite-hth.com.cn/esports",
        "keywords": ["华体会", "DOTA2", "LOL", "CSGO", "电竞投注"],
        "tags": ["电竞", "赛事", "投注"],
        "description": "专注电子竞技赛事，支持DOTA2、英雄联盟、CSGO等热门游戏的竞猜。"
    },
    {
        "title": "华体会真人娱乐",
        "url": "https://appsite-hth.com.cn/live",
        "keywords": ["华体会", "真人", "百家乐", "轮盘", "视讯"],
        "tags": ["真人", "视讯", "娱乐"],
        "description": "高清视讯真人荷官，提供百家乐、轮盘等传统娱乐项目。"
    }
]


def build_summary_entry(record):
    """Convert a single site record into a structured summary line."""
    kw_list = record.get("keywords", [])
    tag_list = record.get("tags", [])
    kw_str = ", ".join(kw_list)
    tag_str = ", ".join(tag_list)
    return {
        "name": record["title"],
        "url": record["url"],
        "keywords": kw_str,
        "tags": tag_str,
        "description": record["description"]
    }


def generate_summary(records):
    """Generate a full structured summary from a list of site records."""
    if not records:
        return {"total": 0, "items": []}
    items = [build_summary_entry(r) for r in records]
    return {
        "total": len(items),
        "items": items
    }


def format_summary_text(summary_data):
    """Convert summary dict to a human-readable text block."""
    lines = []
    lines.append(f"站点资料摘要（共 {summary_data['total']} 条）")
    lines.append("=" * 40)
    for idx, item in enumerate(summary_data["items"], start=1):
        lines.append(f"\n--- 条目 {idx} ---")
        lines.append(f"名称：{item['name']}")
        lines.append(f"URL ：{item['url']}")
        lines.append(f"关键词：{item['keywords']}")
        lines.append(f"标签：{item['tags']}")
        lines.append(f"说明：{item['description']}")
    lines.append("\n" + "=" * 40)
    lines.append("摘要生成完毕。")
    return "\n".join(lines)


def export_summary_json(summary_data, filepath=None):
    """Export summary data as JSON, optionally to a file."""
    json_str = json.dumps(summary_data, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(json_str)
        return f"已导出 JSON 至 {filepath}"
    return json_str


def main():
    """Main entry: generate summary and print to stdout."""
    summary = generate_summary(SITE_RECORDS)
    text = format_summary_text(summary)
    print(text)
    # Uncomment next line to also export JSON to a file:
    # export_summary_json(summary, "site_summary.json")


if __name__ == "__main__":
    main()