"""
FX Teller SVG Diagram Library
Used by website (as inline SVG), PDF (inline SVG), and PPT (rasterized to PNG).

All diagrams use the brand color palette and a consistent visual language.
"""
import math

# Brand colors (kept in sync with theme/tokens.css)
NAVY      = "#1B1B2F"
GOLD      = "#C5A55A"
CREAM     = "#F5F0E8"
WHITE     = "#FFFFFF"
SAGE      = "#7A9E7E"
SLATE     = "#4A4A6A"
CORAL     = "#C87A6A"
LIGHT     = "#F8F6F2"
DARK      = "#1A1A1A"


def svg_brand_4tier(width=600, height=440):
    """Business Model — 4-tier Revenue Architecture Pyramid."""
    tiers = [
        ("Future Revenue",   "International · Marketplace · AI Subscriptions", CORAL, "Year 3+"),
        ("Strategic Revenue","House · Publishing · Dubai Operations",         SLATE, "Year 2+"),
        ("Premium Revenue",  "Workshops · Roundtables · Coaching",            SAGE,  "Year 2+"),
        ("Primary Revenue",  "Annual + Monthly · Founding Tier",             NAVY,  "Year 1+"),
    ]
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="28" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="16" font-weight="700" fill="{NAVY}">Revenue Architecture</text>')
    svg.append(f'<text x="{width//2}" y="48" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" fill="{SLATE}">Four tiers · Time-sequenced · Philosophy-defended</text>')
    w_base = 380
    center = width // 2
    for i, (name, desc, color, timing) in enumerate(tiers):
        y = 70 + i * 88
        w = w_base - i * 60
        x = center - w // 2
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="68" rx="3" fill="{color}" opacity="0.92"/>')
        svg.append(f'<text x="{center}" y="{y+30}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="white">{name}</text>')
        svg.append(f'<text x="{center}" y="{y+52}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="rgba(255,255,255,0.85)">{desc}</text>')
        svg.append(f'<text x="{x+w+12}" y="{y+38}" text-anchor="start" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" font-weight="700" fill="{color}">{timing}</text>')
        if i < 3:
            svg.append(f'<line x1="{center-15}" y1="{y+68}" x2="{center+15}" y2="{y+88}" stroke="{GOLD}" stroke-width="1.5"/>')
            svg.append(f'<polygon points="{center},{y+88} {center-6},{y+80} {center+6},{y+80}" fill="{GOLD}"/>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_flywheel(width=520, height=520):
    """Value Creation Flywheel."""
    stages = ["Member\nValue", "Trust", "Retention", "Referral", "Brand\nEquity", "Revenue"]
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="30" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="16" font-weight="700" fill="{NAVY}">Value Creation Flywheel</text>')
    cx, cy, r = width//2, 280, 180
    n = len(stages)
    for i, stage in enumerate(stages):
        angle = i * (360/n) - 90
        rad = math.radians(angle)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="42" fill="{GOLD}" opacity="0.15"/>')
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="42" fill="none" stroke="{GOLD}" stroke-width="1.5"/>')
        lines = stage.split('\n')
        for li, line in enumerate(lines):
            yo = y - 2 + li * 11
            svg.append(f'<text x="{x:.1f}" y="{yo:.1f}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="{NAVY}">{line}</text>')
        n_angle = ((i + 1) % n) * (360/n) - 90
        n_rad = math.radians(n_angle)
        nx = cx + r * math.cos(n_rad)
        ny = cy + r * math.sin(n_rad)
        midx = (x + nx) / 2
        midy = (y + ny) / 2
        # Arrow line
        dx = nx - x
        dy = ny - y
        length = math.sqrt(dx*dx + dy*dy)
        ux, uy = dx/length, dy/length
        sx = x + 42*ux
        sy = y + 42*uy
        ex = nx - 42*ux
        ey = ny - 42*uy
        svg.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{GOLD}" stroke-width="1.2" marker-end="url(#arrowGold)"/>')
    svg.append(f'<defs><marker id="arrowGold" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{GOLD}"/></marker></defs>')
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="60" fill="{NAVY}"/>')
    svg.append(f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="white">PHILOSOPHY</text>')
    svg.append(f'<text x="{cx}" y="{cy+10}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="{GOLD}">in motion</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_12_lifecycle(width=820, height=170):
    """12-Stage Member Lifecycle."""
    stages = ["Curiosity", "Application", "Acceptance", "Onboarding",
              "First Floor", "First Win", "Community", "Habit",
              "House", "Ambassador", "Lifetime", "Founder"]
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="22" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="{NAVY}">12-Stage Member Lifecycle</text>')
    n = len(stages)
    spacing = (width - 40) / n
    for i, s in enumerate(stages):
        x = 30 + i * spacing + spacing/2
        phase = 0 if i < 4 else (1 if i < 8 else 2)
        color = [GOLD, SAGE, NAVY][phase]
        phase_label = ["Discovery", "Integration", "Leadership"][phase]
        svg.append(f'<circle cx="{x:.1f}" cy="68" r="20" fill="{color}" opacity="0.9"/>')
        svg.append(f'<text x="{x:.1f}" y="73" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="white">{i+1}</text>')
        svg.append(f'<text x="{x:.1f}" y="105" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="{NAVY}" font-weight="600">{s}</text>')
        if i < n-1:
            svg.append(f'<line x1="{x+22:.1f}" y1="68" x2="{x+spacing-22:.1f}" y2="68" stroke="{SLATE}" stroke-width="0.8" opacity="0.4" marker-end="url(#arrowSlate)"/>')
    # Phase labels
    phase_x = [30 + 1.5*spacing, 30 + 5.5*spacing, 30 + 9.5*spacing]
    for px, label, color in zip(phase_x, ["Discovery", "Integration", "Leadership"], [GOLD, SAGE, NAVY]):
        svg.append(f'<text x="{px:.1f}" y="138" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" font-weight="700" fill="{color}">{label}</text>')
    svg.append(f'<defs><marker id="arrowSlate" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="{SLATE}" opacity="0.4"/></marker></defs>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_24month_roadmap(width=700, height=240):
    """24-Month Roadmap as Gantt-style bars."""
    quarters = [
        ("Q1", "Foundation",         0, 3, NAVY),
        ("Q2", "Founding Cohort",    3, 3, SLATE),
        ("Q3", "Founding Complete",  6, 3, SAGE),
        ("Q4", "Year-1 Validation",  9, 3, GOLD),
        ("Q5", "Year-2 Scale",       12, 3, CORAL),
        ("Q6", "Year-2 Mid",         15, 3, SAGE),
        ("Q7", "Institutionalise",   18, 3, SLATE),
        ("Q8", "Year-2 End",         21, 3, NAVY),
    ]
    milestones = [
        (3, "50 Founding"), (6, "V1 Live"), (12, "Raise Closes"),
        (18, "House Build"), (24, "House Opens"),
    ]
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="20" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="{NAVY}">24-Month Strategic Roadmap</text>')
    bar_w = 600
    bar_x = 30
    for i, (q, label, start, dur, color) in enumerate(quarters):
        y = 40 + i * 20
        sw = dur * (bar_w / 24)
        sx = bar_x + start * (bar_w / 24)
        svg.append(f'<rect x="{sx:.1f}" y="{y}" width="{sw:.1f}" height="14" rx="2" fill="{color}" opacity="0.85"/>')
        svg.append(f'<text x="{sx+sw/2:.1f}" y="{y+10}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="8" font-weight="700" fill="white">{q}</text>')
        svg.append(f'<text x="{bar_x+bar_w+8}" y="{y+10}" text-anchor="start" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="{color}">{label}</text>')
    for m, label in milestones:
        mx = bar_x + m * (bar_w / 24)
        svg.append(f'<line x1="{mx:.1f}" y1="35" x2="{mx:.1f}" y2="205" stroke="{GOLD}" stroke-width="0.5" stroke-dasharray="3,3"/>')
        svg.append(f'<text x="{mx:.1f}" y="220" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="{SLATE}" font-weight="600">{label}</text>')
    for m in range(0, 25, 3):
        mx = bar_x + m * (bar_w / 24)
        svg.append(f'<text x="{mx:.1f}" y="220" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="7" fill="#ccc">|</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_org_chart(width=600, height=320):
    """Team Structure — Cap of 8 in 24 Months."""
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="20" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="{NAVY}">Team Structure — Cap of 8 in 24 Months</text>')
    # Founder
    svg.append(f'<rect x="250" y="35" width="100" height="30" rx="3" fill="{NAVY}"/>')
    svg.append(f'<text x="300" y="55" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="11" font-weight="700" fill="white">Founder</text>')
    # Year 1 (3 roles)
    roles_y1 = [("Host", 80), ("Engineer", 280), ("Writer", 480)]
    for role, x in roles_y1:
        svg.append(f'<line x1="300" y1="65" x2="{x+30}" y2="90" stroke="{SLATE}" stroke-width="1"/>')
        svg.append(f'<rect x="{x}" y="90" width="80" height="26" rx="2" fill="{GOLD}"/>')
        svg.append(f'<text x="{x+40}" y="108" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="white">{role}</text>')
    # Year 2 (5 more)
    roles_y2 = [
        ("Host #2", 30, 80), ("Writer #2", 130, 80), ("Ops", 230, 280),
        ("Engineer #2", 330, 280), ("Community", 430, 280),
    ]
    for role, x, parent_x in roles_y2:
        svg.append(f'<line x1="{parent_x+40}" y1="116" x2="{x+30}" y2="155" stroke="{SLATE}" stroke-width="0.8" opacity="0.6"/>')
        svg.append(f'<rect x="{x}" y="155" width="60" height="24" rx="2" fill="{SAGE}" opacity="0.9"/>')
        svg.append(f'<text x="{x+30}" y="171" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="8" font-weight="700" fill="white">{role}</text>')
    svg.append(f'<text x="{width//2}" y="225" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" fill="{SLATE}" font-weight="600">Year 1: 4 people  ·  Year 2: 8 people max</text>')
    svg.append(f'<text x="{width//2}" y="245" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="#888" font-style="italic">Every hire beyond the third passes a written 5-question philosophy test</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_kpi_dashboard(width=600, height=200):
    """KPI Dashboard — 8 key metrics."""
    kpis = [
        ("MRR",         "₹4.2L",   "Target: ₹25L",     NAVY),
        ("Members",     "42",      "Target: 500",      GOLD),
        ("Retention",   "78%",     "Target: ≥75%",     SAGE),
        ("Apps/week",   "8",       "Target: ≥5",       SLATE),
        ("Uptime",      "99.8%",   "Target: ≥99.5%",   SAGE),
        ("Cost/Member", "₹1,780",  "Target: ₹800",     CORAL),
        ("Writing",     "8h/wk",   "Target: ≥10h/wk",  GOLD),
        ("Subscribers", "850",     "Target: 5,000",    NAVY),
    ]
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="22" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="{NAVY}">Founder Dashboard — Top 8 KPIs</text>')
    for i, (label, value, target, color) in enumerate(kpis):
        x = 12 + (i % 4) * 145
        y = 45 + (i // 4) * 70
        svg.append(f'<rect x="{x}" y="{y}" width="135" height="58" rx="3" fill="{LIGHT}" stroke="#E0DDD5" stroke-width="0.5"/>')
        svg.append(f'<text x="{x+67}" y="{y+25}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="20" font-weight="700" fill="{color}">{value}</text>')
        svg.append(f'<text x="{x+67}" y="{y+42}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="{SLATE}">{label}</text>')
        svg.append(f'<text x="{x+67}" y="{y+53}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="7" fill="#999">{target}</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_growth_curve(width=580, height=280):
    """Membership growth curve — 3 scenarios."""
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="22" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="{NAVY}">Membership Growth — 3 Scenarios</text>')
    # Plot area
    plot_x, plot_y, plot_w, plot_h = 60, 50, 480, 180
    svg.append(f'<line x1="{plot_x}" y1="{plot_y+plot_h}" x2="{plot_x+plot_w}" y2="{plot_y+plot_h}" stroke="#ccc" stroke-width="0.8"/>')
    svg.append(f'<line x1="{plot_x}" y1="{plot_y}" x2="{plot_x}" y2="{plot_y+plot_h}" stroke="#ccc" stroke-width="0.8"/>')
    for v in range(0, 1001, 200):
        vy = plot_y + plot_h - v * (plot_h / 1000)
        svg.append(f'<line x1="{plot_x}" y1="{vy}" x2="{plot_x+plot_w}" y2="{vy}" stroke="#eee" stroke-width="0.3"/>')
        svg.append(f'<text x="{plot_x-6}" y="{vy+3}" text-anchor="end" font-family="Inter,DejaVu Sans,sans-serif" font-size="8" fill="#999">{v}</text>')
    scenarios = [
        ("Conservative", SAGE, [10, 25, 55, 100, 160, 250, 350]),
        ("Expected",     GOLD, [10, 45, 100, 200, 350, 500, 700]),
        ("Optimistic",   NAVY, [12, 65, 170, 290, 450, 650, 900]),
    ]
    months_x = [0, 4, 8, 12, 16, 20, 24]
    for name, color, vals in scenarios:
        pts = []
        for i, v in enumerate(vals):
            x = plot_x + months_x[i] * (plot_w / 24)
            y = plot_y + plot_h - v * (plot_h / 1000)
            pts.append(f"{x:.1f},{y:.1f}")
            svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{color}"/>')
        svg.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="2"/>')
    for m in months_x:
        x = plot_x + m * (plot_w / 24)
        svg.append(f'<text x="{x:.1f}" y="{plot_y+plot_h+15}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="8" fill="#999">M{m}</text>')
    for i, (name, color, _) in enumerate(scenarios):
        lx = 380 + i * 60
        ly = plot_y + plot_h + 35
        svg.append(f'<line x1="{lx}" y1="{ly-3}" x2="{lx+15}" y2="{ly-3}" stroke="{color}" stroke-width="2"/>')
        svg.append(f'<text x="{lx+20}" y="{ly}" text-anchor="start" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="#666">{name}</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_risk_heatmap(width=620, height=520):
    """Risk Heatmap — 5×5 likelihood × impact."""
    risks = [
        ("Founder burnout", 3, 5, "R1"),
        ("Retention <75%",  3, 5, "R2"),
        ("Raise fails",     2, 5, "R3"),
        ("SEBI enforcement",3, 4, "R4"),
        ("Host departure",  2, 4, "R5"),
        ("V1 delay",        3, 3, "R6"),
        ("Low applications",3, 3, "R7"),
        ("Tech outage",     2, 3, "R8"),
        ("Bad hire",        2, 3, "R9"),
        ("Brand drift",     2, 2, "R10"),
    ]
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="22" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="{NAVY}">Risk Heatmap — Top 10 Risks</text>')
    grid_x, grid_y, cell_size = 80, 60, 70
    for i in range(5):
        for j in range(5):
            score = (i + 1) * (j + 1)
            if score >= 15:    color = "#D9534F"
            elif score >= 8:   color = "#F0AD4E"
            else:              color = "#5CB85C"
            alpha = 0.3 + (score / 25) * 0.5
            x = grid_x + j * cell_size
            y = grid_y + (4 - i) * cell_size
            svg.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="{color}" fill-opacity="{alpha}" stroke="white" stroke-width="0.5"/>')
    # Risk markers
    for name, likelihood, impact, _ in risks:
        x = grid_x + (impact - 1) * cell_size + cell_size/2
        y = grid_y + (4 - (likelihood - 1)) * cell_size + cell_size/2
        svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="14" fill="{NAVY}"/>')
        svg.append(f'<text x="{x:.1f}" y="{y+3:.1f}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="8" font-weight="700" fill="white">R</text>')
    # Axis labels
    for j in range(5):
        x = grid_x + j * cell_size + cell_size/2
        svg.append(f'<text x="{x:.1f}" y="{grid_y + 5*cell_size + 18}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="{SLATE}">{"1 Min 2 Min 3 Mod 4 Maj 5 Sev".split()[j]}</text>')
    for i in range(5):
        y = grid_y + (4 - i) * cell_size + cell_size/2
        svg.append(f'<text x="{grid_x - 8}" y="{y+3:.1f}" text-anchor="end" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="{SLATE}">{"5 4 3 2 1".split()[i]}</text>')
    svg.append(f'<text x="{grid_x + 5*cell_size/2}" y="{grid_y + 5*cell_size + 32}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="{NAVY}">Impact →</text>')
    svg.append(f'<text x="20" y="{grid_y + 5*cell_size/2}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="{NAVY}" transform="rotate(-90, 20, {grid_y + 5*cell_size/2})">Likelihood →</text>')
    # Risk list
    risk_y = 460
    svg.append(f'<text x="80" y="{risk_y}" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="{NAVY}">R1: Founder burnout  ·  R2: Retention&lt;75%  ·  R3: Raise fails  ·  R4: SEBI  ·  R5: Host departure</text>')
    svg.append(f'<text x="80" y="{risk_y+15}" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" font-weight="700" fill="{NAVY}">R6: V1 delay  ·  R7: Low apps  ·  R8: Tech outage  ·  R9: Bad hire  ·  R10: Brand drift</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


def svg_brand_pyramid(width=520, height=440):
    """Brand Pyramid — Foundation of identity."""
    levels = [
        ("Voice",      "How the brand speaks",     GOLD,  380),
        ("Positioning","Where the brand sits",     SAGE,  280),
        ("Personality","What the brand feels like",SLATE, 180),
        ("Values",     "What the brand believes",  NAVY,  80),
    ]
    svg = [f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{width}" height="{height}" fill="white"/>')
    svg.append(f'<text x="{width//2}" y="24" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="14" font-weight="700" fill="{NAVY}">Brand Pyramid</text>')
    svg.append(f'<text x="{width//2}" y="42" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="10" fill="{SLATE}">Each level supports the one above</text>')
    center = width // 2
    for i, (level, desc, color, y) in enumerate(levels):
        w = 280 + i * 30
        x = center - w//2
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="50" rx="3" fill="{color}" opacity="0.9"/>')
        svg.append(f'<text x="{center}" y="{y+22}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="12" font-weight="700" fill="white">{level}</text>')
        svg.append(f'<text x="{center}" y="{y+38}" text-anchor="middle" font-family="Inter,DejaVu Sans,sans-serif" font-size="9" fill="rgba(255,255,255,0.85)">{desc}</text>')
    svg.append('</svg>')
    return '\n'.join(svg)


# Map of diagram names to generator functions
DIAGRAMS = {
    "revenue-pyramid": svg_brand_4tier,
    "flywheel": svg_flywheel,
    "lifecycle": svg_12_lifecycle,
    "roadmap": svg_24month_roadmap,
    "org-chart": svg_org_chart,
    "kpi-dashboard": svg_kpi_dashboard,
    "growth-curve": svg_growth_curve,
    "risk-heatmap": svg_risk_heatmap,
    "brand-pyramid": svg_brand_pyramid,
}


def render_diagram(name, **kwargs):
    """Render a named diagram."""
    if name not in DIAGRAMS:
        raise ValueError(f"Unknown diagram: {name}")
    return DIAGRAMS[name](**kwargs)


if __name__ == "__main__":
    # Save all SVGs to disk
    import os
    out = "/mnt/d/FX Teller/publication/diagrams"
    os.makedirs(out, exist_ok=True)
    for name in DIAGRAMS:
        svg = render_diagram(name)
        path = f"{out}/{name}.svg"
        with open(path, "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(svg)
        size = os.path.getsize(path)
        print(f"  {name}.svg: {size} bytes")
