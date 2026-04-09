import os

folder = "/Users/sarvanan-16306/Documents/Xascom/presentation"

def icon(name):
    return '<i data-lucide="' + name + '" class="ico"></i>'

emoji_map = {
    '\U0001F4CB': icon('clipboard-list'),
    '\U0001F4D1': icon('file-text'),
    '\U0001F50D': icon('search'),
    '\U0001F3D7\uFE0F': icon('building-2'),
    '\U0001F3D7': icon('building-2'),
    '\u2699\uFE0F': icon('settings'),
    '\u2699': icon('settings'),
    '\U0001F4C5': icon('calendar'),
    '\U0001F91D': icon('handshake'),
    '\U0001F4CA': icon('bar-chart-3'),
    '\U0001F5BC\uFE0F': icon('image'),
    '\U0001F5BC': icon('image'),
    '\U0001F4DD': icon('pen-line'),
    '\u2139\uFE0F': icon('info'),
    '\u2139': icon('info'),
    '\U0001F4AC': icon('message-circle'),
    '\U0001F4C4': icon('file-text'),
    '\U0001F4DE': icon('phone'),
    '\U0001F58B\uFE0F': icon('pen-tool'),
    '\U0001F58B': icon('pen-tool'),
    '\U0001F3E2': icon('building'),
    '\U0001F6A8': icon('alert-triangle'),
    '\U0001F534': icon('circle-dot'),
    '\U0001F7E0': icon('circle-dot'),
    '\U0001F7E1': icon('circle-dot'),
    '\U0001F7E2': icon('circle-dot'),
    '\U0001F310': icon('globe'),
    '\U0001F6AB': icon('x-circle'),
    '\U0001F4A1': icon('lightbulb'),
    '\U0001F4BB': icon('monitor'),
    '\U0001F527': icon('wrench'),
    '\u2728': icon('sparkles'),
    '\U0001F9EE': icon('calculator'),
    '\U0001F4EC': icon('mail-open'),
    '\U0001F4F2': icon('smartphone'),
    '\U0001F6E0\uFE0F': icon('settings-2'),
    '\U0001F6E0': icon('settings-2'),
    '\u26A1': icon('zap'),
    '\U0001F36A': icon('cookie'),
    '\U0001F4F0': icon('newspaper'),
    '\U0001F512': icon('lock'),
    '\U0001F4E7': icon('mail'),
    '\U0001F5FA\uFE0F': icon('map-pin'),
    '\U0001F5FA': icon('map-pin'),
    '\u2696\uFE0F': icon('scale'),
    '\u2696': icon('scale'),
    '\U0001F510': icon('shield-check'),
    '\U0001F4B0': icon('banknote'),
    '\u26A0\uFE0F': icon('alert-triangle'),
    '\u26A0': icon('alert-triangle'),
    '\u267F': icon('accessibility'),
    '\U0001F4E6': icon('package'),
    '\U0001F680': icon('rocket'),
    '\U0001F4D0': icon('ruler'),
    '\U0001F3E0': icon('home'),
    '\U0001F3E5': icon('heart-pulse'),
    '\U0001F6E1\uFE0F': icon('shield'),
    '\U0001F6E1': icon('shield'),
    '\U0001F4DC': icon('scroll-text'),
    '\U0001F3A8': icon('palette'),
    '\U0001F5A5\uFE0F': icon('monitor'),
    '\U0001F5A5': icon('monitor'),
    '\U0001F41B': icon('bug'),
    '\U0001F4BE': icon('hard-drive'),
    '\U0001F4BC': icon('briefcase'),
    '\u274C': icon('x'),
    '\u2705': icon('check'),
    '\u2753': icon('help-circle'),
    '\u2B50': icon('star'),
    '\U0001F4F1': icon('smartphone'),
    '\U0001F4CD': icon('map-pin'),
    '\U0001F4F8': icon('camera'),
    '\U0001F465': icon('users'),
    '\U0001F511': icon('key'),
    '\U0001F517': icon('link'),
    '\U0001F4DA': icon('book-open'),
    '\U0001F4B5': icon('banknote'),
    '\U0001F4B2': icon('dollar-sign'),
    '\u2714': icon('check'),
    '\u2714\uFE0F': icon('check'),
    '\u2718': icon('x'),
    '\u2713': icon('check'),
    '\u2717': icon('x'),
    '\U0001F4CC': icon('pin'),
    '\U0001F4CE': icon('paperclip'),
    '\U0001F4E9': icon('inbox'),
    '1\uFE0F\u20E3': '<span class="step-num">1</span>',
    '2\uFE0F\u20E3': '<span class="step-num">2</span>',
    '3\uFE0F\u20E3': '<span class="step-num">3</span>',
    '4\uFE0F\u20E3': '<span class="step-num">4</span>',
}

lucide_head = (
    '  <link rel="stylesheet" href="styles.css">\n'
    '  <script src="https://unpkg.com/lucide@0.460.0/dist/umd/lucide.min.js"></script>\n'
    '  <style>\n'
    '    .ico { display: inline-block; width: 16px; height: 16px; vertical-align: -2px; }\n'
    '    .card-icon .ico, .feature-icon .ico, .page-icon .ico, .nav-card .icon .ico { width: 24px; height: 24px; vertical-align: middle; }\n'
    '    .audit-score-card .ico { width: 28px; height: 28px; display: block; margin: 0 auto 4px; }\n'
    '    .legal-card .ico { width: 32px; height: 32px; display: block; margin: 0 auto 4px; }\n'
    '    .step-num { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; background: var(--blue); color: white; font-size: .8rem; font-weight: 800; }\n'
    '  </style>'
)

for fname in ["index.html", "audit.html", "proposal.html", "features.html", "timeline.html"]:
    fpath = os.path.join(folder, fname)
    with open(fpath, 'r') as f:
        content = f.read()

    content = content.replace(
        '  <link rel="stylesheet" href="styles.css">',
        lucide_head,
        1
    )

    content = content.replace(
        '</body>',
        '<script>lucide.createIcons();</script>\n</body>'
    )

    for emoji in sorted(emoji_map.keys(), key=len, reverse=True):
        content = content.replace(emoji, emoji_map[emoji])

    with open(fpath, 'w') as f:
        f.write(content)

    print("Done:", fname)

print("\nAll files updated!")
