# Helpers for the chapter 6 booklet (chapter 5 system): question -> think -> write, then a twin exercise ("دورك")
import os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'booklet6') + os.sep
if os.path.basename(os.path.dirname(os.path.abspath(__file__))) == 'gen':
    D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + os.sep

U = {1: 'الوحدة 1 · الترتيب الحسن', 2: 'الوحدة 2 · مبدأ الاستقراء', 3: 'الوحدة 3 · المجاميع',
     4: 'الوحدة 4 · القسمة', 5: 'الوحدة 5 · المتباينات والبداية من m', 6: 'الوحدة 6 · الاستقراء القوي',
     7: 'الوحدة 7 · تدريب الاختبار'}


def hdr(unit_text, lvl):
    lv = {'must': '<span class="lv must">أساسي</span>', 'extra': '<span class="lv extra">إضافي</span>'}.get(lvl, '')
    return '<div class="hdr"><span class="u">' + unit_text + '</span>' + lv + '<span class="pn"></span></div>'


def page(pid, unit_text, lvl, title, body, sol=False, style=''):
    cls = 'page sol' if sol else 'page'
    st = (' style="' + style + '"') if style else ''
    return ('<section class="' + cls + '" id="' + pid + '"' + st + '>\n  ' + hdr(unit_text, lvl) +
            '\n  <h2 class="t">' + title + '</h2>\n' + body + '\n</section>\n')


def tag(kind, t):
    return '<span class="tag ' + kind + '">' + t + '</span>'


def idea(t):
    return '  <div class="idea">' + t + '</div>\n'


def qbox(en, ar, lab='السؤال', cls=''):
    c = 'qbox' + ((' ' + cls) if cls else '')
    out = '  <div class="' + c + '"><div class="lab">' + lab + '</div>\n    <p class="en">' + en + '</p>\n'
    if ar:
        out += '    <p class="ar">بالعربي: ' + ar + '</p>\n'
    return out + '  </div>\n'


def duork(num, en, ar):
    return qbox(en, ar, lab='دورك · تمرين ' + num, cls='ex')


def flow(steps):
    out = '    <div class="flow">\n'
    for i, s in enumerate(steps, 1):
        out += '      <div class="f"><span class="num">' + str(i) + '</span><span>' + s + '</span></div>\n'
    return out + '    </div>\n'


def think(title, steps=None, extra='', before=''):
    out = '  <div class="think">\n    <h3>' + title + '</h3>\n' + before
    if steps:
        out += flow(steps)
    return out + extra + '  </div>\n'


def _lab(num, name):
    if num == '*':
        n = '<b class="n st">★</b>'
    elif num and num.isdigit():
        n = '<b class="n">' + num + '</b>'
    else:
        n = num or ''
    return n + (('<i>' + name + '</i>') if name else '')


def W(rows, title='نكتب', cls='tpl'):
    """rows: (num, name, english_html, arabic_gloss[, size]); english None -> blank writing box."""
    out = ('  <h3>' + title + '</h3>\n') if title else ''
    out += '  <div class="' + cls + '">\n'
    for r in rows:
        num, name, en, ar = r[0], r[1], r[2], r[3]
        size = r[4] if len(r) > 4 else 'b1'
        lab = _lab(num, name)
        if en is None:
            out += '    <div class="r' + (' fill' if size in ('b3', 'b4') else '') + '"><div class="l">' + lab + '</div><div class="v b ' + size + '"></div></div>\n'
        else:
            g = ('<span class="g">' + ar + '</span>') if ar else ''
            extra = (' b ' + size) if len(r) > 4 else ''
            out += '    <div class="r"><div class="l">' + lab + '</div><div class="v' + extra + '">' + en + g + '</div></div>\n'
    return out + '  </div>\n'


def stmt(pairs):
    out = '  <div class="stmt">\n'
    for en, ar in pairs:
        out += '    <p class="en">' + en + '</p>\n'
        if ar:
            out += '    <p class="ar">بالعربي: ' + ar + '</p>\n'
    return out + '  </div>\n'


def note(kind, k, t):
    return '  <div class="note ' + kind + '"><span class="k">' + k + '</span>' + t + '</div>\n'


def box(title, inner, indent='  '):
    return indent + '<div class="box">\n' + indent + '  <h3>' + title + '</h3>\n' + inner + indent + '</div>\n'


def hints(lines):
    return '  <div class="hints">' + ''.join('<p>' + l + '</p>' for l in lines) + '</div>\n'


def ref(pid):
    return '<span class="ref" data-to="' + pid + '"></span>'


def lt(t):
    return '<span class="lt">' + t + '</span>'


def card(title, steps):
    """steps: (name, text_html); name may start with ★"""
    out = '  <div class="card">\n    <h3>' + title + '</h3>\n'
    for i, (nm, tx) in enumerate(steps, 1):
        num = '★' if nm.startswith('★') else str(i)
        nm = nm.lstrip('★ ').strip()
        out += '    <div class="s"><span class="num">' + num + '</span><span class="nm">' + nm + '</span><span>' + tx + '</span></div>\n'
    return out + '  </div>\n'


def recall(t):
    return '  <p class="recall">' + t + '</p>\n'


def tbl(head, rows, ltr=False, style='', cls='t', indent='    '):
    st = []
    if ltr:
        st.append('direction:ltr')
    if style:
        st.append(style)
    out = indent + '<table class="' + cls + '"' + ((' style="' + ';'.join(st) + '"') if st else '') + '>\n'
    if head:
        out += indent + '  <tr>' + ''.join('<th' + ((' style="' + h[1] + '"') if isinstance(h, tuple) else '') + '>' + (h[0] if isinstance(h, tuple) else h) + '</th>' for h in head) + '</tr>\n'
    for r in rows:
        out += indent + '  <tr>' + ''.join('<td' + ((' ' + c[1]) if isinstance(c, tuple) else '') + '>' + (c[0] if isinstance(c, tuple) else c) + '</td>' for c in r) + '</tr>\n'
    return out + indent + '</table>\n'


def chain(items, indent='    '):
    out = indent + '<div class="chain">'
    for i, it in enumerate(items):
        if i:
            out += '<span class="a">←</span>'
        out += '<span class="c">' + it + '</span>'
    return out + '</div>\n'


def wl(n=1):
    return '<div class="wl" style="height:' + ('%.1f' % (8.2 * n)) + 'mm"></div>'


OK = '<span class="ok">✓</span>'
NO = '<span class="no">✗</span>'

# the five lines of every induction proof (+ the "small k" line)
B = ('1', 'الأساس')
A = ('2', 'الفرض')
S = ('3', 'المطلوب')
ST = ('4', 'الخطوة')
C = ('5', 'الختام')
SK = ('*', 'k الصغيرة')


def R(step, en, ar=None, size=None):
    t = (step[0], step[1], en, ar)
    return t + ((size,) if size else ())


def blank(steps_sizes):
    """steps_sizes: [(step, size)] -> blank rows"""
    return [(s[0], s[1], None, None, z) for s, z in steps_sizes]


def save(name, pages, tail=''):
    open(D + name, 'w', encoding='utf-8').write('\n'.join(pages) + tail)
    print(name, 'written:', len(pages), 'pages')
