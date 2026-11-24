import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
P = []

# ---------- p-which ----------
def wrow(n, en):
    return ('    <div class="tf"><span>' + str(n) + '.</span><span>' + en +
            '</span><span class="o"></span></div>\n')

P.append(page('p-which', U[6], 'must', 'أي طريقة؟ درّب عينك',
    idea('أهم خطوة: تعرف نوع السؤال من كلماته، وبعدها تطلع البطاقة حقته.') +
    tbl([('في السؤال', 'width:38%'), ('النوع', 'width:17%'), 'أول سطر', ('البطاقة', 'width:10%')], [
        [(lt('Disprove: For every …') + ' أو ' + lt('If …, then …'), 'class="s"'), '1. مثال مضاد', lt(r'Let \(x = \ldots\)'), ref('p-u1')],
        [(lt('Prove: There is no …') + ' أو ' + lt('… is irrational'), 'class="s"'), '2. تناقض', lt('Assume, to the contrary, …'), ref('p-u2')],
        [(lt('Prove … by (a) a direct proof, …'), 'class="s"'), '3. ثلاث طرق', 'حسب الطريقة', ref('p-u3')],
        [(lt('Prove: There exist(s) …'), 'class="s"'), '4. وجود', lt('Let … / Consider …'), ref('p-u4')],
        [(lt('Disprove: There exist(s) …'), 'class="s"'), '5. نفي وجود', lt('We show that if …, then …'), ref('p-u5')]]).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    note('star', lt('Prove or disprove') + '؟', 'جرّب 4 قيم أول. «لكل» وفشلت قيمة: <b>False</b> + مثال مضاد. «يوجد» ولقيت مثال: <b>True</b> + المثال. غير كذا برهن بالطريقة اللي في الجدول.') +
    '  <h3>دورك: اكتب رقم النوع (1 إلى 5) جنب كل جملة، بدون حل</h3>\n' +
    '  <div class="paper" style="--tfp:1.3mm">\n' +
    wrow(1, r'Disprove: For every real number \(x\), \(x^2 \ge x\).') +
    wrow(2, r'Prove that \(\sqrt{7}\) is irrational.') +
    wrow(3, r'Prove that there exist positive integers \(a\) and \(b\) such that \(a^2 + b^2 = 25\).') +
    wrow(4, r'Disprove: There exists an even integer \(n\) such that \(n^2 + 1\) is even.') +
    wrow(5, r'Prove that there is no largest even integer.') +
    wrow(6, r'Disprove: If \(n\) is a prime, then \(n\) is odd.') +
    wrow(7, r'Show that the equation \(x^3 - x - 1 = 0\) has a real number solution between \(x = 1\) and \(x = 2\).') +
    wrow(8, r'Prove that if \(5n + 2\) is odd, then \(n\) is odd, by (a) a direct proof and (b) a proof by contrapositive.') +
    '  </div>\n' +
    '  <p class="small">الأجوبة (غطّها قبل ما تحل). أمثلة: في 1 \\(x = 1/2\\)، وفي 3 \\(a = 3\\) و \\(b = 4\\)، وفي 6 \\(n = 2\\).</p>\n' +
    tbl(['الجملة', '1', '2', '3', '4', '5', '6', '7', '8'], [['النوع', '1', '2', '4', '5', '2', '1', '4', '3']], style='font-size:9.6pt').replace('    <table', '  <table').replace('    </table>', '  </table>'), style='gap:3mm'))

# ---------- p-phr: writing phrases and shortcuts ----------
def prow(en, ar):
    return '    <tr><td class="a">' + ar + '</td><td class="e">' + en + '</td></tr>\n'

P.append(page('p-phr', U[6], 'must', 'جمل الكتابة والاختصارات',
    idea('هذي الجمل تتكرر في كل حلول الفصل. احفظها كقطع جاهزة، وكتابتك بتصير أسرع وأوضح للمصحح.') +
    '  <table class="bi">\n    <tr><th>متى تستخدمها، ومعناها</th><th>الجملة</th></tr>\n' +
    prow('Assume, to the contrary, that …', 'أول سطر في التناقض: نفترض العكس.') +
    prow('This is a contradiction. / …, which is impossible.', 'آخر سطر في التناقض: وهذا تناقض / وهذا مستحيل.') +
    prow(r'Thus, \(x = \ldots\) is a counterexample.', 'آخر سطر في المثال المضاد.') +
    prow(r'Then \(n = 2k + 1\) for some integer \(k\).', 'تحويل «فردي» لمعادلة: لعدد صحيح ما k.') +
    prow('Since … is an integer, … is even.', 'بعد ما تطلّع 2 عامل مشترك.') +
    prow(r'We may assume that \(a/b\) has been reduced to lowest terms.', 'في «غير نسبي»: الكسر في أبسط صورة.') +
    prow('Without loss of generality, assume that …', 'حالتين متشابهتين، تكتب وحدة بس (مثل x و y في 5.33).') +
    prow('We consider two cases. Case 1. … Case 2. …', 'البرهان بالحالات.') +
    prow(r'Let \(x = \ldots\). / Consider …', 'برهان الوجود: تعيّن الشي.') +
    prow('by the Intermediate Value Theorem of Calculus', 'وجود حل بدون ما تعرف قيمته.') +
    prow('We show that if …, then …', 'أول سطر في نفي الوجود.') +
    prow('Hence / Therefore / It follows that …', 'إذن / لذلك / ينتج أن.') +
    '  </table>\n' +
    '  <div class="grid2">\n' +
    box('اختصارات مقبولة', r'''    <ul>
      <li>الرموز: \(\mathbb{Z}\) و \(\mathbb{Q}\) و \(\mathbb{R}\) و \(\in\) و \(\mid\) و \(\nmid\) و \(\Rightarrow\).</li>
      <li>''' + lt('WLOG') + ' بدل ' + lt('Without loss of generality') + r'''.</li>
      <li>''' + lt('iff') + ' بدل ' + lt('if and only if') + r'''.</li>
    </ul>
''').replace('  <div class="box">', '    <div class="box">') +
    box('أشياء تنقص درجات', '''    <ul>
      <li>False بدون مثال محسوب.</li>
      <li>تبدأ البرهان من المطلوب.</li>
      <li>تنسى «''' + lt('lowest terms') + '''».</li>
      <li>«''' + lt('for every k') + '» بدل «' + lt('for some integer k') + '''».</li>
      <li>مثال مضاد من برا المجموعة.</li>
      <li>تنفي «يوجد» بمثال واحد.</li>
      <li>في عكس النقيض تفترض عكس الشرط بدل عكس النتيجة.</li>
    </ul>
''').replace('  <div class="box">', '    <div class="box">') +
    '  </div>\n'))


# ---------- mocks ----------
def qrow(head, mk):
    return '    <div class="qrow" style="direction:ltr"><span class="en">' + head + '</span><span class="mk">' + mk + '</span></div>\n'

def q(t, sol=None, src=''):
    return ('    <div class="q"><span class="qt">' + t + '</span>' + (('<span class="src">' + src + '</span>') if src else '') +
            (go(sol) if sol else '') + '</div>\n')

def tagrows(rows, ids, home, txt='الورقة'):
    """append an anchor + back button to solution rows (None = no anchor)"""
    out = []
    for r, i in zip(rows, ids):
        out.append(r + ({'id': i, 'back': [(home, txt)]},) if i else r)
    return out

AFTER = box('بعد ما تخلص', '''    <ul class="chk">
      <li><span class="cb"></span>كل فقرة في سؤال 1 بدأت بسطر الحكم: True أو False.</li>
      <li><span class="cb"></span>في False كتبت القيمة والحساب، مو بس «خطأ».</li>
      <li><span class="cb"></span>في التناقض بدأت بـ ''' + lt('Assume, to the contrary') + '''.</li>
      <li><span class="cb"></span>في عكس النقيض افترضت عكس النتيجة، مو عكس الشرط.</li>
    </ul>
''')

def score(rows, total):
    out = '  <h3>صحّح نفسك</h3>\n  <table class="t">\n    <tr><th>الفقرة</th><th>النوع</th><th>الدرجة</th><th>لو نقصت، ارجع لـ</th></tr>\n'
    for r in rows:
        out += '    <tr><td>' + r[0] + '</td><td>' + r[1] + '</td><td>' + r[2] + '</td><td>' + ref(r[3]) + '</td></tr>\n'
    return out + '    <tr><th colspan="2">المجموع</th><th>' + total + '</th><th></th></tr>\n  </table>\n'

# ---------- p-bank: the 16 plan exercises as an exam paper ----------
BANK = [('مثال مضاد', 'p-u1', [('5.2', 2), ('5.3', 2), ('5.4', 2), ('5.5', 2)]),
        ('تناقض', 'p-u2', [('5.12', 3), ('5.18', 3), ('5.21', 4), ('5.33', 3)]),
        ('ثلاث طرق', 'p-u3', [('5.36', 6), ('5.39', 6)]),
        ('وجود', 'p-u4', [('5.42', 2), ('5.46', 4), ('5.51', 4), ('5.53', 3)]),
        ('نفي الوجود', 'p-u5', [('5.55', 3), ('5.57', 3)])]

def bank_score(groups):
    ks = [(k, mk) for _, _, it in groups for k, mk in it]
    out = '  <h3>صحّح نفسك</h3>\n  <table class="t">\n    <tr>' + '<th>التمرين</th><th>الدرجة</th><th>درجتي</th>' * 2 + '</tr>\n'
    for i in range(0, len(ks), 2):
        out += '    <tr>' + ''.join('<td>' + k + '</td><td>' + str(mk) + '</td><td></td>' for k, mk in ks[i:i + 2]) + '</tr>\n'
    return out + '    <tr><th colspan="2">المجموع</th><th>' + str(sum(mk for _, mk in ks)) + '</th><th colspan="3"></th></tr>\n  </table>\n'

def bank_box(i, name, unit, items):
    out = '  <div class="box paper bank">\n    <div class="bh">' + str(i) + ' · ' + name + ' <span class="small">(شرحه من ' + ref(unit) + ')</span></div>\n'
    for k, mk in items:
        out += q('<b>' + k + '.</b> ' + EX[k] + ' <span class="mk">(' + str(mk) + ' marks)</span>', 's-' + k.replace('.', ''))
    return out + '  </div>\n'

P.append(page('p-bank', U[6], 'must', 'بنك تمارين الخطة (1 من 2): كأنك في الاختبار' + tag('ex', '8 أسئلة'),
    idea('تمارين الخطة الـ16 بدون أمثلة ولا تلميحات، زي ورقة الاختبار. حل كل سؤال على ورقة، وبعدها اضغط «الحل»، ومن الحل ارجع بزر «↩ البنك». الدرجات تقريبية على قد الميدات.') +
    ''.join(bank_box(i, n, u, it) for i, (n, u, it) in list(enumerate(BANK, 1))[:2]), style='gap:3mm'))

P.append(page('p-bank2', U[6], 'must', 'بنك تمارين الخطة (2 من 2): كأنك في الاختبار' + tag('ex', '8 أسئلة'),
    idea('نفس الطريقة: حل على ورقة، وبعدها اضغط «الحل». الوجود ونفي الوجود من الخطة، بس ما جت في الميدات.') +
    ''.join(bank_box(i, n, u, it) for i, (n, u, it) in list(enumerate(BANK, 1))[2:]), style='gap:3mm'))

# ---------- p-papers: the chapter 5 questions of past midterms, word for word ----------
P.append(page('p-papers', U[6], 'top', 'أوراق الميدات السابقة: حلها كأنك في الاختبار' + tag('past', 'بالحرف'),
    idea('نفس أسئلة الفصل 5 اللي جت في الميدات، بنفس الصيغة والدرجات. شغّل مؤقت، وحل على ورقة بدون ما تطالع الشرح. بعدها اضغط «الحل» عند كل سؤال، وارجع بزر «↩ ورقة الميدات».') +
    '  <div class="box paper">\n' +
    '    <div class="bh">ورقة 1 · ميد نوفمبر 2026، الجزء حق الفصل 5 <span class="small">(16 من 25 درجة · 35 دقيقة)</span></div>\n' +
    qrow('<b>Question 1: (3+3+4)</b> Prove or disprove the following:', '10 marks') +
    q(r'1. If \(n\) is an odd integer, then \(n^2 - n\) is odd.', 'm-nov') +
    q('2. There is no smallest positive real number.', 'm-small') +
    q(r'3. The real number \(\sqrt{2}\) is irrational.', 'm-rt2') +
    qrow(r'<b>Question 2: (2+2+2)</b> Prove that if \(n\) is an even integer, then \(5n + 3\) is odd by', '6 marks') +
    q('1. a direct proof. &nbsp; 2. a proof by contrapositive. &nbsp; 3. a proof by contradiction.', 'm-5n3') +
    '  </div>\n  <div class="box paper">\n' +
    '    <div class="bh">ورقة 2 · من ميد 1446 وميد 1447 وميد البنات ونهائي 1446 <span class="small">(14 درجة · 30 دقيقة)</span></div>\n' +
    q(r'1. For every odd positive integer \(n\), \(3 \mid (n^2 - 1)\). <span class="mk">(2 marks)</span>', 'm-1447', 'ميد 1447') +
    q(r'2. For every even positive integer \(n\), \(12 \mid (n^2 - 4)\). <span class="mk">(2 marks)</span>', 'm-girls', 'البنات') +
    q(r'3. Use a proof by contradiction to prove that \(\sqrt[3]{7}\) is irrational. <span class="mk">(3 marks)</span>', 's-cbrt7', 'نهائي 1446') +
    q(r'4. Prove that if \(n\) is an odd integer, then \(7n - 5\) is even by (a) a direct proof, (b) a proof by contrapositive and (c) a proof by contradiction. <span class="mk">(7 marks)</span>', 's-536', 'ميد 1446') +
    '  </div>\n' +
    note('star', 'بعدها:', 'الاختبارين التجريبيين الجايين فيهم توأم كل هذي الأسئلة بأرقام ثانية، يعني أقرب شي للبديل.'), style='gap:3mm'))


# ---------- p-mockA ----------
P.append(page('p-mockA', U[6], 'top', 'اختبار تجريبي 1: بصيغة ميد نوفمبر' + tag('ex', '35 دقيقة'),
    idea('هذا جزء الفصل 5 من ميد نوفمبر (16 درجة)، بأسئلة توأم. شغّل مؤقت 35 دقيقة، وحل على ورقة. لا تفتح الحلول قبل ما يخلص الوقت.') +
    '  <div class="box paper">\n' +
    qrow('<b>Question 1: (3+3+4)</b> Prove or disprove the following:', '10 marks') +
    q(r'1. For every positive integer \(n\), \(n^2 + n + 1\) is a prime number.', 's-mA11') +
    q('2. There is no largest negative real number.', 's-mA12') +
    q(r'3. The real number \(\sqrt{5}\) is irrational. [You may use: for an integer \(a\), if \(5 \mid a^2\), then \(5 \mid a\).]', 's-mA13') +
    '  </div>\n  <div class="box paper">\n' +
    qrow(r'<b>Question 2: (2+2+2)</b> Prove that if \(n\) is an even integer, then \(7n + 3\) is odd by', '6 marks') +
    q('1. a direct proof. &nbsp; 2. a proof by contrapositive. &nbsp; 3. a proof by contradiction.', 's-mA2') +
    '  </div>\n' + AFTER +
    ''))

# ---------- p-mockAs ----------
P.append(page('p-mockAs', 'حلول الوحدة 6', '', 'حلول الاختبار التجريبي 1' + tag('sol', 'شيّك'),
    W(tagrows([('1.1 False', '', r'Let \(n = 4\). Then \(n^2 + n + 1 = 16 + 4 + 1 = 21 = 3 \cdot 7\), which is not a prime number. Thus, \(n = 4\) is a counterexample.',
        r'أول ثلاث قيم تعطي 3 و7 و13، وكلها أولية. الفخ: لازم توصل لـ \(n = 4\).'),
       ('1.2 True', '', r'Assume, to the contrary, that there is a largest negative real number, say \(r\). Since \(r \lt r/2 \lt 0\), it follows that \(r/2\) is a negative real number that is larger than \(r\). This is a contradiction.',
        'توأم «ما فيه أصغر عدد موجب»: «أصغر» صارت «أكبر»، و«موجب» صارت «سالب».'),
       ('1.3 True', '', r'Assume, to the contrary, that \(\sqrt{5}\) is rational. Then \(\sqrt{5} = a/b\), where \(a, b \in \mathbb{Z}\), \(b \ne 0\) and \(a/b\) has been reduced to lowest terms. Then \(a^2 = 5b^2\). Thus \(5 \mid a^2\), and so \(5 \mid a\). So \(a = 5c\) for some \(c \in \mathbb{Z}\), and \(25c^2 = 5b^2\), that is, \(b^2 = 5c^2\). Thus \(5 \mid b^2\), and so \(5 \mid b\). Since \(5 \mid a\) and \(5 \mid b\), this is a contradiction since \(a/b\) has been reduced to lowest terms.',
        r'قالب \(\sqrt{2}\) نفسه، و«زوجي» صارت «يقبل القسمة على 5».'),
       ('2 (1)', 'مباشر', r'Assume that \(n\) is even. Then \(n = 2k\) for some integer \(k\). So \(7n + 3 = 14k + 3 = 2(7k + 1) + 1\). Since \(7k + 1\) is an integer, \(7n + 3\) is odd.', ''),
       ('2 (2)', 'عكس النقيض', r'Assume that \(7n + 3\) is even. Then \(7n + 3 = 2k\) for some integer \(k\). So \(n = (7n + 3) - 6n - 3 = 2k - 6n - 3 = 2(k - 3n - 2) + 1\). Since \(k - 3n - 2\) is an integer, \(n\) is odd.', ''),
       ('2 (3)', 'تناقض', r'Assume, to the contrary, that there exists an even integer \(n\) such that \(7n + 3\) is even. Then \(n = 2x\) and \(7n + 3 = 2y\) for some integers \(x\) and \(y\). Hence \(14x + 3 = 2y\), and so \(3 = 2y - 14x = 2(y - 7x)\). Since \(y - 7x\) is an integer, 3 is even, which is a contradiction.', '')], ['s-mA11', 's-mA12', 's-mA13', 's-mA2', None, None], 'p-mockA'), title='') +
    score([('1.1', 'مثال مضاد فيه فخ', '3', 'p-trap'), ('1.2', 'ما فيه أكبر ولا أصغر', '3', 'p-ex5'),
           ('1.3', 'غير نسبي', '4', 'p-rt2b'), ('2', 'ثلاث طرق', '6', 'p-tpl3')], '16') +
    note('star', 'كل فقرة توأم سؤال من ميد نوفمبر:', r'1.1 توأم «\(n^2 - n\) فردي»، و1.2 توأم «ما فيه أصغر عدد موجب»، و1.3 توأم \(\sqrt{2}\)، وسؤال 2 توأم \(5n + 3\). يعني لو حليت هذا، أنت جاهز لنسخة البديل.'), sol=True))

# ---------- p-mockB ----------
P.append(page('p-mockB', U[6], 'top', 'اختبار تجريبي 2: بعد ما تصحح الأول' + tag('ex', '40 دقيقة'),
    idea('سوّه بعد ما تصحح الاختبار الأول وترجع للي نقصت فيه. فيه فقرة وجود (1.4) احتياط، لو جا سؤال من الوحدة 4. شغّل مؤقت 40 دقيقة.') +
    '  <div class="box paper">\n' +
    qrow('<b>Question 1: (2+3+4+3)</b> Prove or disprove the following:', '12 marks') +
    q(r'1. For every odd positive integer \(n\), \(3 \mid (n^2 + 2)\).', 's-mB11') +
    q('2. There is no smallest positive rational number.', 's-mB12') +
    q(r'3. The real number \(\sqrt[3]{2}\) is irrational. [You may use: for an integer \(a\), if \(a^3\) is even, then \(a\) is even.]', 's-mB13') +
    q(r'4. The equation \(x^3 + x - 1 = 0\) has a real number solution between \(x = 0\) and \(x = 1\).', 's-mB14') +
    '  </div>\n  <div class="box paper">\n' +
    qrow(r'<b>Question 2: (2+2+2)</b> Prove that if \(n\) is an odd integer, then \(5n - 3\) is even by', '6 marks') +
    q('1. a direct proof. &nbsp; 2. a proof by contrapositive. &nbsp; 3. a proof by contradiction.', 's-mB2') +
    '  </div>\n' + AFTER +
    ''))

# ---------- p-mockBs ----------
P.append(page('p-mockBs', 'حلول الوحدة 6', '', 'حلول الاختبار التجريبي 2' + tag('sol', 'شيّك'),
    W(tagrows([('1.1 False', '', r'Let \(n = 3\). Then \(n^2 + 2 = 11\) and \(3 \nmid 11\). Thus, \(n = 3\) is a counterexample.',
        ''),
       ('1.2 True', '', r'Assume, to the contrary, that there is a smallest positive rational number, say \(r\). Then \(r = a/b\) for some integers \(a\) and \(b\) with \(b \ne 0\), and so \(r/2 = a/(2b)\) is a positive rational number. Since \(0 \lt r/2 \lt r\), this is a contradiction.', ''),
       ('1.3 True', '', r'Assume, to the contrary, that \(\sqrt[3]{2}\) is rational. Then \(\sqrt[3]{2} = a/b\), where \(a, b \in \mathbb{Z}\), \(b \ne 0\) and \(a/b\) has been reduced to lowest terms. Then \(a^3 = 2b^3\), so \(a^3\) is even, and so \(a\) is even. So \(a = 2c\) for some \(c \in \mathbb{Z}\), and \(8c^3 = 2b^3\), that is, \(b^3 = 4c^3 = 2(2c^3)\). Thus \(b^3\) is even, and so \(b\) is even. Since \(a\) and \(b\) are even, this is a contradiction since \(a/b\) has been reduced to lowest terms.',
        ''),
       ('1.4 True', '', r'Let \(f(x) = x^3 + x - 1\). Since \(f\) is a polynomial function, it is continuous on \([0, 1]\). Now \(f(0) = -1\) and \(f(1) = 1\). Since 0 is between \(f(0)\) and \(f(1)\), it follows by the Intermediate Value Theorem of Calculus that there is a number \(c\) between 0 and 1 such that \(f(c) = 0\). Hence \(c\) is a solution.',
        ''),
       ('2 (1)', 'مباشر', r'Assume that \(n\) is odd. Then \(n = 2k + 1\) for some integer \(k\). So \(5n - 3 = 10k + 2 = 2(5k + 1)\). Since \(5k + 1\) is an integer, \(5n - 3\) is even.', ''),
       ('2 (2)', 'عكس النقيض', r'Assume that \(5n - 3\) is odd. Then \(5n - 3 = 2k + 1\) for some integer \(k\). So \(n = (5n - 3) - 4n + 3 = 2k - 4n + 4 = 2(k - 2n + 2)\). Since \(k - 2n + 2\) is an integer, \(n\) is even.', ''),
       ('2 (3)', 'تناقض', r'Assume, to the contrary, that there exists an odd integer \(n\) such that \(5n - 3\) is odd. Then \(n = 2x + 1\) and \(5n - 3 = 2y + 1\) for some integers \(x\) and \(y\). Hence \(10x + 2 = 2y + 1\), and so \(1 = 2y - 10x = 2(y - 5x)\). Since \(y - 5x\) is an integer, 1 is even, which is a contradiction.', '')], ['s-mB11', 's-mB12', 's-mB13', 's-mB14', 's-mB2', None, None], 'p-mockB'), title='') +
    score([('1.1', 'مثال مضاد فيه فخ', '2', 'p-trap'), ('1.2', 'ما فيه أصغر', '3', 'p-fam'), ('1.3', 'غير نسبي', '4', 'p-rt2b'),
           ('1.4', 'وجود', '3', 'p-ivt'), ('2', 'ثلاث طرق', '6', 'p-fill3')], '18'), sol=True))

# ---------- p-night ----------
def nb(title, inner):
    return box(title, inner).replace('  <div class="box">', '    <div class="box">')

AR = 'font-family:var(--ar);direction:rtl;text-align:right'
P.append(page('p-night', 'ورقة ليلة الاختبار', 'top', 'الفصل كله في صفحة',
    '  <div class="grid2">\n' +
    nb('البطاقات الخمس', '''    <ol>
      <li><b>مثال مضاد:</b> جرّب ← احسب ← احكم.</li>
      <li><b>تناقض:</b> نعكس ← نمشي ← تناقض.</li>
      <li><b>ثلاث طرق:</b> الفرق في أول سطر (تحت).</li>
      <li><b>وجود:</b> اختر ← تحقق ← اختم.</li>
      <li><b>نفي وجود:</b> اقلب ← خذ أي x ← اثبت.</li>
    </ol>
''') +
    nb('خريطة القرار', '''    <ul>
      <li>''' + lt('Disprove + For every') + ''' ← 1</li>
      <li>''' + lt('Prove + There is no / irrational') + ''' ← 2</li>
      <li>''' + lt('Prove … by (a), (b), (c)') + ''' ← 3</li>
      <li>''' + lt('Prove + There exists') + ''' ← 4</li>
      <li>''' + lt('Disprove + There exists') + ''' ← 5</li>
      <li>''' + lt('Prove or disprove') + ''': جرّب 4 قيم أول.</li>
    </ul>
''') +
    '  </div>\n' +
    r'  <h3>ثلاث طرق: أول سطر لكل طريقة (مثال: n زوجي، و \(5n + 3\) فردي)</h3>' + '\n' +
    W([('1', 'مباشر', r'Assume that \(n\) is even.', ''),
       ('2', 'عكس النقيض', r'Assume that \(5n + 3\) is even. Then \(n = (5n + 3) - 4n - 3 = \ldots\)', ''),
       ('3', 'تناقض', r'Assume, to the contrary, that there exists an even integer \(n\) such that \(5n + 3\) is even.', '')], title='') +
    '  <div class="grid2">\n' +
    nb('ما فيه أصغر عدد موجب', chain(['نفترض r الأصغر', r'\(0 \lt r/2 \lt r\)', 'تناقض']) +
       '    <p class="small">سالب؟ \\(r \\lt r/2 \\lt 0\\). نسبي؟ زد سطر: \\(r/2 = a/(2b)\\).</p>\n') +
    nb('قالب «غير نسبي»', chain([r'\(a/b\) أبسط صورة', 'ربّع أو كعّب', 'p يقسم a', r'\(a = pc\)', 'p يقسم b', 'تناقض'])) +
    '  </div>\n' +
    '  <div class="grid2">\n' +
    nb('الفخاخ', '''    <ul>
      <li>أول قيمة أو قيمتين تمشي. جرّب 4.</li>
      <li>في (2) ابدأ بعكس النتيجة، مو بعكس الشرط.</li>
      <li>عكس «و» هو «أو».</li>
      <li>لا تنسَ «''' + lt('lowest terms') + '''».</li>
      <li>«يوجد» ما تنقضها بمثال.</li>
    </ul>
''') +
    nb('أسئلة الاختبارات السابقة', r'''    <ul class="chk">
      <li><span class="cb"></span>ثلاث طرق: \(5n + 3\) و \(5n + 1\) و \(7n - 5\) <span class="pg ref" data-to="p-tpl3"></span></li>
      <li><span class="cb"></span>ما فيه أصغر عدد موجب <span class="pg ref" data-to="p-ex5"></span></li>
      <li><span class="cb"></span>فخاخ: \(3 \mid (n^2 - 1)\) و \(12 \mid (n^2 - 4)\) و \(n^2 - n\) <span class="pg ref" data-to="p-trap"></span></li>
      <li><span class="cb"></span>\(\sqrt{2}\) و \(\sqrt[3]{7}\) غير نسبي <span class="pg ref" data-to="p-rt2b"></span></li>
    </ul>
''') +
    '  </div>\n' +
    note('star', 'توقّع البديل:', r'نفس الأنواع الأربعة بأرقام ثانية: ثلاث طرق بعدد ثاني، و«ما فيه أكبر أو أصغر» بكلمة ثانية، وجذر ثاني (\(\sqrt{3}\) أو \(\sqrt{5}\) أو \(\sqrt[3]{7}\))، ومثال مضاد جديد (يمكن من أمثلة الكتاب 5.2 و5.5 و5.9).')))

save('g_u6.html', P)
