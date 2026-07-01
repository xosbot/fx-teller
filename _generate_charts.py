"""Generate 8 infographics for the FX Teller Strategic Blueprint PDF."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import os

OUT_DIR = "/mnt/d/FX Teller/docs/assets"
os.makedirs(OUT_DIR, exist_ok=True)

# Brand palette
NAVY = "#1B1B2F"
GOLD = "#C5A55A"
CREAM = "#F5F0E8"
WHITE = "#FFFFFF"
SAGE = "#7A9E7E"
SLATE = "#4A4A6A"
CORAL = "#C87A6A"
LIGHT_NAVY = "#2D2D4A"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.facecolor": WHITE,
    "figure.facecolor": WHITE,
})

def save(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", pad_inches=0.3,
                facecolor=WHITE, edgecolor="none")
    plt.close(fig)
    print(f"  Saved: {path} ({os.path.getsize(path)//1024} KB)")


def chart_1_timeline():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    phases = {
        "Foundation":      (1, 3, NAVY),
        "Founding Cohort": (4, 6, GOLD),
        "Year-1 Scale":    (7, 12, SAGE),
        "Year-2 Scale":    (13, 18, SLATE),
        "Institutional":   (19, 24, CORAL),
    }
    milestones = {
        1:  "V1 spec done",
        3:  "25-50 Founding",
        4:  "Second Host in",
        6:  "V1 ships public",
        9:  "House scoping",
        12: "Raise closes",
        18: "House building",
        21: "AI production",
        24: "House opens",
    }
    for i, (name, (s, e, c)) in enumerate(phases.items()):
        ax.barh(5 - i, e - s + 1, left=s, height=0.6, color=c, alpha=0.85,
                label=f"{name} (M{s}-M{e})", edgecolor=WHITE, linewidth=0.5)
    for m, label in milestones.items():
        ax.annotate(label, (m, 5.5), fontsize=7, ha="center", va="bottom",
                    color=NAVY, fontweight="bold", rotation=25)
    ax.set_xlim(0, 25.5)
    ax.set_ylim(-0.5, 6.5)
    ax.set_yticks([])
    ax.set_xticks(np.arange(1, 25))
    ax.set_xticklabels([f"M{m}" for m in range(1, 25)], fontsize=6, rotation=45)
    ax.set_xlabel("Month", fontsize=8, color=SLATE)
    ax.set_title("24-Month Execution Timeline", fontsize=14, color=NAVY, fontweight="bold", pad=12)
    ax.legend(loc="upper right", fontsize=7, framealpha=0.9, edgecolor=CREAM)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    fig.tight_layout()
    save(fig, "chart_01_timeline.png")


def chart_2_growth():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    months = np.arange(0, 25)
    conservative = [10, 15, 25, 35, 45, 55, 65, 75, 85, 100,
                    110, 120, 130, 145, 160, 175, 190, 210, 230, 250,
                    270, 290, 310, 330, 350]
    expected = [10, 18, 30, 45, 60, 80, 100, 120, 145, 170,
                200, 230, 260, 290, 320, 350, 380, 410, 440, 470,
                500, 550, 600, 650, 700]
    optimistic = [12, 25, 45, 65, 90, 115, 145, 175, 210, 250,
                  290, 330, 370, 410, 450, 490, 530, 570, 610, 660,
                  700, 750, 800, 850, 900]
    ax.plot(months, conservative, color=SAGE, linewidth=2.2, label="Conservative",
            marker="o", markersize=3, alpha=0.85)
    ax.plot(months, expected, color=GOLD, linewidth=3, label="Expected",
            marker="s", markersize=3.5, alpha=0.9)
    ax.plot(months, optimistic, color=NAVY, linewidth=2.2, label="Optimistic",
            marker="^", markersize=3, alpha=0.85)
    ax.annotate("50 Founding", (6, 80), fontsize=7.5, color=NAVY, fontweight="bold", ha="center",
                arrowprops=dict(arrowstyle="->", color=GOLD, lw=1.2))
    ax.annotate("Raise gate\n>=75% retention", (12, 200), fontsize=7, color=SLATE, ha="center", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=1))
    ax.annotate("House opens", (24, expected[24]), fontsize=7.5, color=GOLD, fontweight="bold", ha="center",
                arrowprops=dict(arrowstyle="->", color=GOLD, lw=1.2))
    ax.set_xlim(0, 24)
    ax.set_ylim(0, 950)
    ax.set_xlabel("Month", fontsize=9, color=SLATE)
    ax.set_ylabel("Active Members", fontsize=9, color=SLATE)
    ax.set_title("Membership Growth Projection (3 Scenarios)", fontsize=13, color=NAVY, fontweight="bold", pad=10)
    ax.legend(fontsize=8, framealpha=0.9, edgecolor=CREAM)
    ax.grid(axis="y", alpha=0.2, color=SLATE)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    save(fig, "chart_02_growth.png")


def chart_3_revenue_pyramid():
    fig, ax = plt.subplots(figsize=(7, 5))
    tiers = [
        ("Future Revenue", "International / Marketplace / AI Subscriptions", 250, CORAL, "Year 3+"),
        ("Strategic Revenue", "House of Traders / Publishing / Dubai Ops", 400, SLATE, "Year 2+"),
        ("Premium Revenue", "Workshops / Roundtables / Coaching", 600, SAGE, "Year 2+"),
        ("Primary Revenue", "Annual + Monthly Membership / Founding Tier", 900, NAVY, "Year 1+"),
    ]
    for i, (name, desc, width, color, timing) in enumerate(tiers):
        y = i * 1.1
        hw = width / 200
        rect = FancyBboxPatch((5 - hw, y), 2 * hw, 0.9, boxstyle="round,pad=0.08",
                              facecolor=color, edgecolor=WHITE, linewidth=1.5, alpha=0.9)
        ax.add_patch(rect)
        ax.text(5, y + 0.55, name, fontsize=10, color=WHITE, fontweight="bold", ha="center", va="center")
        ax.text(5, y + 0.25, desc, fontsize=6.5, color=WHITE, ha="center", va="center", alpha=0.85)
        ax.text(5 + hw + 1.2, y + 0.45, timing, fontsize=7, color=color, fontweight="bold", va="center")
    ax.set_xlim(0, 10)
    ax.set_ylim(-0.3, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Revenue Architecture - 4 Tiers", fontsize=14, color=NAVY, fontweight="bold", pad=10)
    fig.tight_layout()
    save(fig, "chart_03_revenue_pyramid.png")


def chart_4_moats():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    moats = ["Brand Philosophy", "Member Trust", "Community",
             "Host Quality", "House of Traders", "Operating System"]
    scores = [9.5, 8.5, 7.5, 7.0, 6.5, 6.0]
    colors = [NAVY, GOLD, SAGE, SLATE, CORAL, LIGHT_NAVY]
    bars = ax.barh(moats, scores, color=colors, height=0.55, edgecolor=WHITE, linewidth=0.8, alpha=0.9)
    for bar, score in zip(bars, scores):
        ax.text(bar.get_width() + 0.15, bar.get_y() + bar.get_height()/2,
                f"{score}/10", fontsize=9, color=NAVY, fontweight="bold", va="center")
    ax.set_xlim(0, 11)
    ax.set_xlabel("Durability Score", fontsize=9, color=SLATE)
    ax.set_title("The 6 Moats - Ordered by Durability", fontsize=13, color=NAVY, fontweight="bold", pad=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(axis="y", labelsize=9)
    fig.tight_layout()
    save(fig, "chart_04_moats.png")


def chart_5_lifecycle():
    fig, ax = plt.subplots(figsize=(10, 4.5))
    stages = ["Curiosity", "Application", "Acceptance", "Onboarding",
              "First Floor", "First Win", "Community", "Habit",
              "House", "Ambassador", "Lifetime", "Founder-tier"]
    n = len(stages)
    xs = np.linspace(0, n - 1, n)
    for i, (stage, x) in enumerate(zip(stages, xs)):
        color = GOLD if i < 4 else (SAGE if i < 8 else NAVY)
        circle = plt.Circle((x, 0), 0.38, color=color, alpha=0.85, ec=WHITE, lw=1.5)
        ax.add_patch(circle)
        ax.text(x, 0, str(i + 1), fontsize=9, color=WHITE, fontweight="bold", ha="center", va="center")
        ax.text(x, -0.72, stage, fontsize=7.5, ha="center", color=NAVY, fontweight="bold")
    for i in range(n - 1):
        ax.annotate("", xy=(xs[i + 1] - 0.42, 0), xytext=(xs[i] + 0.42, 0),
                    arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.2, alpha=0.5))
    ax.text(1.5, 0.65, "Discovery", fontsize=8, ha="center", color=NAVY, fontweight="bold", style="italic")
    ax.text(6.5, 0.65, "Integration", fontsize=8, ha="center", color=SAGE, fontweight="bold", style="italic")
    ax.text(10.5, 0.65, "Leadership", fontsize=8, ha="center", color=CORAL, fontweight="bold", style="italic")
    ax.set_xlim(-0.8, n - 1 + 0.8)
    ax.set_ylim(-1.1, 0.95)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("12-Stage Member Lifecycle", fontsize=14, color=NAVY, fontweight="bold", pad=8)
    fig.tight_layout()
    save(fig, "chart_05_lifecycle.png")


def chart_6_risk_heatmap():
    fig, ax = plt.subplots(figsize=(7, 5.5))
    risks = [
        ("Founder burnout", 3, 5), ("Retention <75%", 3, 5),
        ("Raise fails", 2, 5), ("SEBI enforcement", 3, 4),
        ("Host departure", 2, 4), ("V1 delay", 3, 3),
        ("Low applications", 3, 3), ("Tech outage", 2, 3),
        ("Bad hire", 2, 3), ("Brand drift", 2, 2),
    ]
    for i in range(5):
        for j in range(5):
            score = (i + 1) * (j + 1)
            if score >= 15:       color = "#D9534F"
            elif score >= 8:      color = "#F0AD4E"
            else:                 color = "#5CB85C"
            alpha = 0.3 + (score / 25) * 0.5
            ax.add_patch(plt.Rectangle((j, 4 - i), 1, 1, color=color, alpha=alpha, ec=WHITE, lw=0.5))
    for name, likelihood, impact in risks:
        x = impact - 1 + 0.5
        y = 4 - (likelihood - 1) + 0.5
        ax.plot(x, y, "o", color=NAVY, markersize=9, zorder=5)
        ax.annotate(name, (x, y), fontsize=6.5, ha="center", va="center", color=WHITE, fontweight="bold", zorder=6)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_xticks(np.arange(5) + 0.5)
    ax.set_yticks(np.arange(5) + 0.5)
    ax.set_xticklabels(["1 Minimal", "2 Minor", "3 Moderate", "4 Major", "5 Severe"], fontsize=7)
    ax.set_yticklabels(["5 Almost\nCertain", "4 Likely", "3 Possible", "2 Unlikely", "1 Rare"], fontsize=7)
    ax.set_xlabel("Impact", fontsize=9, color=SLATE, labelpad=8)
    ax.set_ylabel("Likelihood", fontsize=9, color=SLATE, labelpad=8)
    ax.set_title("Risk Heatmap - Top 10 Risks", fontsize=13, color=NAVY, fontweight="bold", pad=10)
    fig.tight_layout()
    save(fig, "chart_06_risk_heatmap.png")


def chart_7_kpi_dashboard():
    fig, axes = plt.subplots(2, 4, figsize=(10, 4.5))
    axes = axes.flatten()
    kpis = [
        ("MRR", "Rs 4.2L", GOLD, "Target: Rs 25L at M24"),
        ("Active Members", "42", NAVY, "Target: 500 at M24"),
        ("12-mo Retention", "78%", SAGE, "Target: >=75%"),
        ("Weekly Apps", "8", SLATE, "Target: >=5"),
        ("Floor Uptime", "99.8%", SAGE, "Target: >=99.5%"),
        ("Cost/Member", "Rs 1,780", CORAL, "Target: Rs 800 at M24"),
        ("Writing Hours", "8h/wk", GOLD, "Target: >=10h/wk"),
        ("Substack Subs", "850", NAVY, "Target: 5,000 at M24"),
    ]
    for ax, (name, value, color, note) in zip(axes, kpis):
        ax.text(0.5, 0.75, value, fontsize=16, color=color, fontweight="bold", ha="center", va="center", transform=ax.transAxes)
        ax.text(0.5, 0.40, name, fontsize=8, color=SLATE, ha="center", va="center", transform=ax.transAxes, fontweight="bold")
        ax.text(0.5, 0.15, note, fontsize=5.5, color=SLATE, ha="center", va="center", transform=ax.transAxes, alpha=0.7)
        ax.set_facecolor(CREAM)
        for spine in ax.spines.values():
            spine.set_color(CREAM)
            spine.set_linewidth(0.5)
    fig.suptitle("Founder Dashboard - Top 8 KPIs", fontsize=14, color=NAVY, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "chart_07_kpi_dashboard.png")


def chart_8_service_catalogue():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    layers = ["Trading Floor", "Library", "Community", "Process Journal", "Mentor Pool"]
    v1_counts = [5, 2, 3, 1, 2]
    future_counts = [3, 6, 8, 2, 4]
    x = np.arange(len(layers))
    width = 0.35
    bars1 = ax.bar(x - width/2, v1_counts, width, color=NAVY, alpha=0.9, label="V1 Services (13)", edgecolor=WHITE, linewidth=0.5)
    bars2 = ax.bar(x + width/2, future_counts, width, color=GOLD, alpha=0.7, label="Future Services (35)", edgecolor=WHITE, linewidth=0.5)
    for bar, count in zip(bars1, v1_counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, str(count), fontsize=8, color=NAVY, ha="center", fontweight="bold")
    for bar, count in zip(bars2, future_counts):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, str(count), fontsize=8, color=GOLD, ha="center", fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(layers, fontsize=8)
    ax.set_ylabel("Number of Services", fontsize=9, color=SLATE)
    ax.set_title("Service Catalogue - V1 vs Future, by Layer", fontsize=13, color=NAVY, fontweight="bold", pad=10)
    ax.legend(fontsize=8, framealpha=0.9, edgecolor=CREAM)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_ylim(0, 15)
    fig.tight_layout()
    save(fig, "chart_08_service_catalogue.png")


if __name__ == "__main__":
    print("Generating 8 infographics...")
    chart_1_timeline()
    chart_2_growth()
    chart_3_revenue_pyramid()
    chart_4_moats()
    chart_5_lifecycle()
    chart_6_risk_heatmap()
    chart_7_kpi_dashboard()
    chart_8_service_catalogue()
    print("All charts generated successfully.")
