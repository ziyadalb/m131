import os
D = os.path.dirname(os.path.abspath(__file__)) + os.sep


def lt(t):
    return '<span class="lt">' + t + '</span>'


def hdr(n):
    return '<div class="hdr"><span class="u">ملخص الفصل 5 · الوجود والبرهان بالتناقض</span><span class="pn"></span></div>'


def chain(items):
    out = '    <div class="chain">'
    for i, it in enumerate(items):
        if i:
            out += '<span class="a">←</span>'
        out += '<span class="c">' + it + '</span>'
    return out + '</div>\n'


def block(num, name, know, steps, body):
    return ('  <div class="tb">\n    <div class="tbh"><span class="tn">' + num + '</span><span class="tt">' + name +
            '</span><span class="tk">تعرفه: ' + know + '</span></div>\n' + (chain(steps) if steps else '') + body + '  </div>\n')


def exq(en, lab='مثال'):
    return '    <div class="exq"><span class="lb2">' + lab + '</span><span class="e2">' + en + '</span></div>\n'


def ans(en, lab='الجواب'):
    return '    <div class="ans"><span class="lb2">' + lab + '</span><span class="e2">' + en + '</span></div>\n'


def p(cls, t):
    return '    <p class="' + cls + '">' + t + '</p>\n'


OK = '<span class="ok">✓</span>'
NO = '<span class="no">✗</span>'

MAP = r'''  <table class="t">
    <tr><th style="width:44%">في السؤال</th><th>النوع</th><th style="width:30%">أول سطر</th></tr>
    <tr><td>''' + lt('Disprove') + ' + ' + lt('For every …') + ''' أو ''' + lt('If …, then …') + r'''</td><td>1. مثال مضاد</td><td>''' + lt(r'For \(n = \ldots\), …') + r'''</td></tr>
    <tr><td>''' + lt('Prove') + ' + ' + lt('There is no …') + ''' أو ''' + lt('irrational') + r'''</td><td>2. تناقض</td><td>''' + lt('Assume, to the contrary, …') + r'''</td></tr>
    <tr><td>''' + lt('by (a) direct, (b) contrapositive, (c) …') + r'''</td><td>3. ثلاث طرق</td><td>جدول النوع 3</td></tr>
    <tr><td>''' + lt('Prove') + ' + ' + lt('There exists …') + r'''</td><td>4. وجود</td><td>''' + lt(r'Let \(x = \ldots\) / Consider …') + r'''</td></tr>
    <tr><td>''' + lt('Disprove') + ' + ' + lt('There exists …') + r'''</td><td>5. نفي وجود</td><td>''' + lt('We show that if …, then …') + r'''</td></tr>
    <tr><td>''' + lt('Prove or disprove') + r'''</td><td colspan="2">جرّب 3 قيم أول، وبعدها قرّر النوع</td></tr>
  </table>
'''

T1 = block('1', 'المثال المضاد', lt('Disprove') + ' + ' + lt('For every'), ['جرّب', 'احسب', 'احكم'],
    exq(r'For every even positive integer \(n\), \(12 \mid (n^2 - 4)\).') +
    p('try', r'جرّب: \(n = 2\) يعطي 0 ' + OK + r' · \(n = 4\) يعطي 12 ' + OK + r' · \(n = 6\) يعطي 32 ' + NO) +
    ans(r'<b>False.</b> For \(n = 6\), \(n^2 - 4 = 32\) and \(12 \nmid 32\). Thus, \(n = 6\) is a counterexample.') +
    p('warn', r'<b>⚠️</b> أول قيمة أو قيمتين ممكن يمشون: جرّب 3 قيم. وفي «إذا… فإن…» المثال المضاد: الشرط صح والنتيجة خطأ.'))

T2 = block('2', 'البرهان بالتناقض', lt('There is no') + ' أو ' + lt('irrational'), ['نعكس', 'نمشي', 'تناقض'],
    exq('There is no smallest positive real number.', 'مثال 1') +
    ans(r'Assume, to the contrary, that there is a smallest positive real number, say \(r\). Since \(0 \lt r/2 \lt r\), \(r/2\) is a positive real number smaller than \(r\). This is a contradiction.') +
    exq(r'Prove that \(\sqrt{2}\) is irrational.', 'مثال 2') +
    ans(r'Assume, to the contrary, that \(\sqrt{2}\) is rational. Then \(\sqrt{2} = a/b\), where \(a, b \in \mathbb{Z}\), \(b \ne 0\), and \(a/b\) is in lowest terms. So \(a^2 = 2b^2\), and \(a\) is even. Let \(a = 2c\). Then \(4c^2 = 2b^2\), so \(b^2 = 2c^2\) and \(b\) is even. Since \(a\) and \(b\) are both even, this contradicts that \(a/b\) is in lowest terms.') +
    p('warn', r'<b>⚠️ العكس:</b> «ما فيه» ← «فيه» · «غير نسبي» ← «نسبي» · «إذا P فإن Q» ← «P صح و Q خطأ» · «و» ← «أو».'))

PH = r'''  <div class="box">
    <h3>5 جمل تحفظها</h3>
    <ul class="notes" style="direction:ltr; text-align:left; font-family:var(--en); columns:2; column-gap:8mm">
      <li>Thus, \(n = \ldots\) is a counterexample.</li><li>Assume, to the contrary, that …</li><li>This is a contradiction.</li>
      <li>… has the desired property.</li><li>We show that if …, then …</li>
    </ul>
  </div>
'''

T3 = block('3', 'ثلاث طرق', lt('by (a) direct, (b) contrapositive, (c) contradiction'), None,
    r'''    <div class="fl"><div class="h">مباشر</div><div class="h">عكس النقيض</div><div class="h">تناقض</div>
      <div>افترض P ← وصّل لـ Q</div><div>افترض عكس Q ← وصّل لعكس P</div><div>افترض P وعكس Q ← مستحيل</div></div>
''' +
    exq(r'If \(n\) is an even integer, then \(5n + 1\) is odd.') +
    ans(r'Assume that \(n\) is even. Then \(n = 2k\) for some integer \(k\). So \(5n + 1 = 10k + 1 = 2(5k) + 1\), which is odd.', '(a) مباشر') +
    ans(r'Assume that \(5n + 1\) is even. Then \(5n + 1 = 2k\) for some integer \(k\). So \(n = (5n + 1) - 4n - 1 = 2(k - 2n - 1) + 1\), which is odd.', '(b) عكس النقيض') +
    ans(r'Assume, to the contrary, that there is an even integer \(n\) such that \(5n + 1\) is even. Then \(n = 2x\) and \(5n + 1 = 2y\) for some integers \(x, y\). So \(10x + 1 = 2y\) and \(1 = 2(y - 5x)\). Thus 1 is even, which is a contradiction.', '(c) تناقض') +
    p('warn', r'<b>⚠️</b> لا تبدأ أبداً بافتراض Q (أن \(5n + 1\) فردي). هذا افتراض للمطلوب.'))

T4 = block('4', 'الوجود', lt('Prove') + ' + ' + lt('There exists'), ['اختر', 'تحقق', 'اختم'],
    exq('There exists an integer whose cube equals its square.', 'مثال 1') +
    ans(r'Since \(1^3 = 1^2 = 1\), the integer 1 has the desired property.') +
    exq(r'The equation \(x^5 + 2x - 5 = 0\) has a unique real solution between \(x = 1\) and \(x = 2\).', 'مثال 2') +
    ans(r'<b>Existence.</b> Let \(f(x) = x^5 + 2x - 5\). Since \(f\) is a polynomial, it is continuous on \([1, 2]\). Since \(f(1) = -2 \lt 0 \lt 31 = f(2)\), by the Intermediate Value Theorem there is \(c \in (1, 2)\) with \(f(c) = 0\).<br><b>Uniqueness.</b> Assume, to the contrary, that there are two solutions \(a \lt b\) in \((1, 2)\). Then \(a^5 + 2a - 5 \lt b^5 + 2b - 5\), so \(0 \lt 0\), a contradiction.') +
    p('warn', r'<b>⚠️</b> «حل وحيد» = جزأين: الوجود بالقيمة الوسطى، والوحدانية بالتناقض.'))

T5 = block('5', 'نفي الوجود', lt('Disprove') + ' + ' + lt('There exists'), ['اقلب', 'خذ أي x', 'اثبت'],
    exq(r'Disprove: There exists an integer \(n\) such that \(n^3 - n + 1\) is even.') +
    ans(r'We show that \(n^3 - n + 1\) is odd for every \(n \in \mathbb{Z}\).<br><i>Case 1.</i> \(n = 2a\): \(n^3 - n + 1 = 8a^3 - 2a + 1 = 2(4a^3 - a) + 1\), which is odd.<br><i>Case 2.</i> \(n = 2b + 1\): \(n^3 - n + 1 = 8b^3 + 12b^2 + 4b + 1 = 2(4b^3 + 6b^2 + 2b) + 1\), which is odd.') +
    p('warn', r'<b>⚠️</b> هنا مثال واحد ما يكفي: لازم تثبت «لكل n».'))

pages = [
    '<section class="page" id="p-s1" style="gap:2.4mm">\n  ' + hdr(1) + '\n  <h2 class="t">ملخص الفصل 5: خمس أنواع أسئلة</h2>\n' + MAP + T1 + T2 + PH + '</section>\n',
    '<section class="page" id="p-s2" style="gap:2.4mm">\n  ' + hdr(2) + '\n' + T3 + T4 + T5 + '</section>\n',
]
open(D + 'b_sum.html', 'w', encoding='utf-8').write('\n'.join(pages))
print('written', len(pages))
