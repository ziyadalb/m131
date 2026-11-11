import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []


def tf(n, en):
    return ('    <div class="tf"><span>' + str(n) + '.</span><span>' + en + '</span><span class="o">☐ True &nbsp; ☐ False</span>'
            '<span class="why">النوع: ____ · السبب:</span></div>\n')


TRAPS = [
    r'For every positive integer \(n\), \(2^n \gt n^2\).',
    r'For every positive integer \(n\), \(3^n \gt n^2\).',
    r'For every positive integer \(n\), \(1 + 5 + 9 + \cdots + (4n-3) = 2n^2 + n\).',
    r'For every nonnegative integer \(n\), \(3 \mid (2^{2n} - 1)\).',
    r'For every positive integer \(n\), \(3 \mid (2^n - 1)\).',
    r'The closed interval \([0, 1]\) is well-ordered.',
    r'The set of prime numbers is well-ordered.',
    r'If \(P(k) \Rightarrow P(k+1)\) is true for every positive integer \(k\), then \(P(n)\) is true for every positive integer \(n\).',
    r'If \(a_1 = 1\) and \(a_n = 2a_{n-1}\) for \(n \ge 2\), then \(a_n = 2^n\) for every \(n \in \mathbb{N}\).',
    r'For every \(n \in \mathbb{N}\), the Fibonacci number \(F_n\) is odd whenever \(3 \nmid n\).']

P.append(page('p-traps', U[7], 'must', 'صح أو خطأ؟ ومن أي نوع؟' + tag('ex', 'دورك'),
    idea('مثل ميد 1447: كل فقرة «' + lt('Prove or disprove') + '». لكل عبارة: قرّر صح أو خطأ، واكتب نوعها (رقم الوحدة من 1 إلى 6) والسبب في سطر.') +
    note('star', 'قرّر بسرعة:', r'جرّب \(n = 1, 2, 3\) أول. قيمة فشلت؟ False ومثالها المضاد جاهز. كلها مشت؟ غالباً True.') +
    '  <div class="paper" style="--tfp:1.2mm">\n' + ''.join(tf(i + 1, t) for i, t in enumerate(TRAPS)) + '  </div>\n', style='gap:2.8mm'))

# ---------- p-phr ----------
def prow(en, ar):
    return '    <tr><td class="a">' + ar + '</td><td class="e">' + en + '</td></tr>\n'

SYM = tbl(None, [[r'\(\mathbb{N}\)', ('1، 2، 3، …', 'class="s"')], [r'\(\mathbb{Z}\)', ('الأعداد الصحيحة', 'class="s"')], [r'\(\mathbb{Q}\)', ('النسبية (الكسور)', 'class="s"')],
                 [r'\(x \in A\)', ('x عنصر في A', 'class="s"')], [r'\(A \subseteq B\)', ('A جزء من B', 'class="s"')], [r'\((0, 1)\) و \([0, 1]\)', ('بدون الطرفين / معها', 'class="s"')]], cls='t dict', indent='      ')
SYM2 = tbl(None, [[r'\(a \mid b\)', (r'a يقسم b: \(b = ax\)', 'class="s"')], [r'\(a \nmid b\)', ('a ما يقسم b', 'class="s"')], [r'\(P \Rightarrow Q\)', ('إذا P فإن Q', 'class="s"')],
                  [r'\(\forall\)', ('لكل', 'class="s"')], [r'\(|A|\)', ('عدد عناصر A', 'class="s"')], [r'\(\mathcal{P}(A)\)', ('كل المجموعات الجزئية من A', 'class="s"')]], cls='t dict', indent='      ')

P.append(page('p-phr', U[7], 'must', 'جمل الكتابة والرموز والاختصارات',
    '  <div class="grid2">\n    <div>\n' + SYM + '    </div>\n    <div>\n' + SYM2 + '    </div>\n  </div>\n' +
    '  <table class="bi">\n    <tr><th>متى تكتبها</th><th>الجملة</th></tr>\n' +
    prow(r'Since …, the statement is true for \(n = 1\).', 'الأساس.') +
    prow(r'Assume that … for a positive integer \(k\).', 'الفرض. الكتاب يكتبها كذا في أمثلة كثيرة، فهي أقصر صيغة مقبولة.') +
    prow('We show that …', 'المطلوب.') +
    prow('By the inductive hypothesis, …', 'في السطر اللي تعوّض فيه الفرض. المصحح يدوّرها.') +
    prow(r'Then … \(= dx\) for some integer \(x\).', 'القسمة: الفرض كمعادلة.') +
    prow(r'Since … is an integer, \(d \mid\) …', 'ختام خطوة القسمة.') +
    prow(r'Assume that …, where \(k \ge m\).', 'الفرض لما البداية من m.') +
    prow(r'If \(k = 1\), then …. So we may assume that \(k \ge 2\).', 'سطر ★ k الصغيرة.') +
    prow(r'Assume … for all integers \(i\) with \(1 \le i \le k\).', 'الفرض القوي.') +
    prow(r'Since \(k + 1 \ge 3\), …', 'قبل ما تستخدم القاعدة التكرارية.') +
    prow('By the (Strong) Principle of Mathematical Induction, …', 'الختام. اكتب اسم المبدأ كامل، لا تختصره.') +
    '  </table>\n' +
    '  <div class="grid2">\n' +
    box('اختصارات مقبولة', r'''      <ul>
        <li>الرموز: \(\in\) و \(\mathbb{N}\) و \(\mid\) و \(\Rightarrow\).</li>
        <li>''' + lt(r'for a positive integer \(k\)') + r''' بدل الجملة الطويلة.</li>
        <li>تكتب الخطوة سلسلة مساواة وحدة بدل أسطر.</li>
      </ul>
''', indent='    ') +
    box('أشياء تنقص درجات', r'''      <ul>
        <li>''' + lt(r'for every \(k\)') + r''' في الفرض.</li>
        <li>تبدأ الخطوة من المطلوب.</li>
        <li>تنسى الأساس، أو سطر ★.</li>
        <li>\(\gt\) بدون سبب.</li>
      </ul>
''', indent='    ') +
    '  </div>\n', style='gap:3mm'))

# ---------- p-mock ----------
P.append(page('p-mock', U[7], 'must', 'اختبار قصير على الفصل' + tag('ex', '35 دقيقة'),
    idea('نفس صيغة ميد 1447. شغّل مؤقت 35 دقيقة، وحل على ورقة أو صفحات فاضية. لا تفتح الحلول قبل ما يخلص الوقت.') +
    r'''  <div class="box paper">
    <div class="qrow" style="direction:ltr"><span class="en"><b>Q: Prove or disprove the following:</b></span><span class="mk">15 marks</span></div>
    <div class="q">1. For every positive integer \(n\), \(\;1 \cdot 2 + 2 \cdot 3 + \cdots + n(n+1) = \dfrac{n(n+1)(n+2)}{3}\). <span class="mk">(3 marks)</span></div>
    <div class="q">2. For every positive integer \(n\), \(\;5 \mid (6^n - 1)\). <span class="mk">(3 marks)</span></div>
    <div class="q">3. For every positive integer \(n\), \(\;n! \gt 2^n\). <span class="mk">(2 marks)</span></div>
    <div class="q">4. A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 2\), \(a_2 = 4\) and \(a_n = a_{n-1} + 2a_{n-2}\) for \(n \ge 3\). Then \(a_n = 2^n\) for all \(n \in \mathbb{N}\). <span class="mk">(4 marks)</span></div>
    <div class="q">5. For each positive integer \(n\), let \(P(n)\) be a statement. If (1) \(P(1)\) is true and (2) the implication \(P(k) \Rightarrow P(k+1)\) is true for every positive integer \(k\), then \(P(n)\) is true for every positive integer \(n\). <span class="mk">(3 marks)</span></div>
  </div>
''' +
    box('بعد ما تخلص', '''    <ul class="chk">
      <li><span class="cb"></span>كل فقرة بدأت بسطر الحكم: True أو False.</li>
      <li><span class="cb"></span>كل استقراء فيه الخمس أسطر، والختام فيه اسم المبدأ.</li>
      <li><span class="cb"></span>جربت \\(n = 1, 2, 3\\) قبل ما أبدأ أي برهان.</li>
      <li><span class="cb"></span>في المتتابعة كتبت سطر ★.</li>
    </ul>
''') +
    '  <div class="space" data-label="ملاحظات: وش الفقرة اللي أخذت منك وقت أكثر؟"></div>\n'))

# ---------- solutions ----------
ANS = [('False', '5', r'\(n = 2\): \(4 \gt 4\) خطأ. الصحيحة تبدأ من 5.'),
       ('True', '5', 'تمرين 6.22.'),
       ('False', '3', r'\(n = 1\): الأيسر 1 والأيمن 3. الصحيحة \(2n^2 - n\).'),
       ('True', '4', 'مثل مثال القسمة على 9، من \\(n = 0\\).'),
       ('False', '4', r'\(n = 1\): \(2^1 - 1 = 1\) و \(3 \nmid 1\).'),
       ('False', '1', r'\((0, 1)\) جزئية منها بدون أصغر عنصر.'),
       ('True', '1', r'جزء من \(\mathbb{N}\) (تمرين 6.1 d).'),
       ('False', '2', r'بدون أساس ما تثبت شي. مثال: \(P(n): n = n + 1\).'),
       ('False', '6', r'\(a_1 = 1 \ne 2^1\). الصحيحة \(2^{n-1}\).'),
       ('True', '6', r'من 6.36: \(F_n\) زوجي ⟺ \(3 \mid n\).')]
ans_tbl = tbl(['#', 'الحكم', 'النوع', 'السبب'], [[str(i + 1), a, t, (r, 'class="s"')] for i, (a, t, r) in enumerate(ANS)], indent='  ')

P.append(page('p-sm1', 'حلول الوحدة 7', '', 'أجوبة «صح أو خطأ»، وحل السؤال 1' + tag('sol', 'شيّك'),
    ans_tbl +
    '  <h3>1. True</h3>\n' +
    W([R(B, r'Since \(1 \cdot 2 = 2 = \frac{1 \cdot 2 \cdot 3}{3}\), the formula holds for \(n = 1\).'),
       R(A, r'Assume that \(1 \cdot 2 + \cdots + k(k+1) = \frac{k(k+1)(k+2)}{3}\) for a positive integer \(k\).'),
       R(S, r'We show that \(1 \cdot 2 + \cdots + (k+1)(k+2) = \frac{(k+1)(k+2)(k+3)}{3}\).'),
       R(ST, r'By the inductive hypothesis, \({1 \cdot 2 + \cdots + (k+1)(k+2)} = {\frac{k(k+1)(k+2)}{3} + (k+1)(k+2)} = {(k+1)(k+2)\left(\frac{k}{3} + 1\right)} = \frac{(k+1)(k+2)(k+3)}{3}.\)', r'تريك الفرق: \(\frac{(k+1)(k+2)(k+3) - k(k+1)(k+2)}{3} = (k+1)(k+2)\) ✓'),
       R(C, r'By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).')], title='', cls='tpl cmp'),
    sol=True, style='gap:2.8mm'))

P.append(page('p-sm2', 'حلول الوحدة 7', '', 'حلول الاختبار القصير' + tag('sol', '2 إلى 4'),
    '  <h3>2. True</h3>\n' +
    W([R(B, r'When \(n = 1\), \(6^1 - 1 = 5\) and \(5 \mid 5\).'),
       R(A, r'Assume that \(5 \mid (6^k - 1)\) for a positive integer \(k\). Then \(6^k - 1 = 5x\) for some integer \(x\), so \(6^k = 5x + 1\).', 'اعزل.'),
       R(ST, r'\(6^{k+1} - 1 = 6 \cdot 6^k - 1 = 6(5x + 1) - 1 = 30x + 5 = 5(6x + 1)\). Since \(6x + 1\) is an integer, \(5 \mid (6^{k+1} - 1)\).', 'عوّض، واختم.'),
       R(C, r'By the Principle of Mathematical Induction, \(5 \mid (6^n - 1)\) for every positive integer \(n\).')], title='') +
    '  <h3>3. False</h3>\n' +
    W([('', 'الجواب', r'Let \(n = 1\). Then \(1! = 1\) and \(2^1 = 2\), so \(n! \gt 2^n\) is false. Hence \(n = 1\) is a counterexample.', r'مثال واحد محسوب يكفي. (الصحيحة من \(n \ge 4\).)')], title='') +
    '  <h3>4. True</h3>\n' +
    W([R(B, r'Since \(a_1 = 2 = 2^1\), the formula holds for \(n = 1\).'),
       R(A, r'Assume for an arbitrary positive integer \(k\) that \(a_i = 2^i\) for every integer \(i\) with \(1 \le i \le k\).', 'فرض قوي.'),
       R(S, r'We show that \(a_{k+1} = 2^{k+1}\).'),
       R(SK, r'If \(k = 1\), then \(a_{k+1} = a_2 = 4 = 2^2\). So we may assume that \(k \ge 2\).'),
       R(ST, r'Since \(k + 1 \ge 3\), by the inductive hypothesis \(a_{k+1} = a_k + 2a_{k-1} = 2^k + 2 \cdot 2^{k-1} = 2^k + 2^k = 2^{k+1}\).'),
       R(C, r'By the Strong Principle of Mathematical Induction, \(a_n = 2^n\) for all \(n \in \mathbb{N}\).')], title='', cls='tpl cmp'),
    sol=True, style='gap:2.6mm'))

P.append(page('p-sm3', 'حلول الوحدة 7', '', 'حل السؤال 5، وصحّح نفسك' + tag('sol', 'شيّك'),
    '  <h3>5. True</h3>\n' +
    '  <p>هذا مبدأ الاستقراء نفسه. صحّح برهانك من ' + ref('p-pmi') + ' جملة بجملة: نعكس، أصغر فاشل s، \\(s \\ge 2\\)، \\(P(s - 1)\\) صحيحة، تناقض.</p>\n' +
    r'''  <h3>صحّح نفسك</h3>
  <table class="t">
    <tr><th>السؤال</th><th>النوع</th><th>الدرجة</th><th>درجتي</th><th>لو نقصت، ارجع لـ</th></tr>
    <tr><td>1</td><td>مجموع</td><td>3</td><td></td><td>القالب ومثال 1 <span class="ref" data-to="p-u3"></span></td></tr>
    <tr><td>2</td><td>قسمة</td><td>3</td><td></td><td>مثال القسمة <span class="ref" data-to="p-ex5"></span></td></tr>
    <tr><td>3</td><td>عبارة خاطئة</td><td>2</td><td></td><td>صح أو خطأ <span class="ref" data-to="p-traps"></span></td></tr>
    <tr><td>4</td><td>متتابعة</td><td>4</td><td></td><td>سؤال الميد <span class="ref" data-to="p-sx"></span></td></tr>
    <tr><td>5</td><td>برهان المبدأ</td><td>3</td><td></td><td>برهان المبدأ <span class="ref" data-to="p-pmi"></span></td></tr>
    <tr><th colspan="2">المجموع</th><th>15</th><th></th><th></th></tr>
  </table>
''' + note('star', 'كيف تصحح:', '12 وفوق: جاهز. أقل: ارجع للمثال المحلول حق السؤال اللي نقصت فيه، وبعدها حل تمرين من نفس الوحدة بدون تلميحات.'),
    sol=True))

# ---------- p-night ----------
P.append(page('p-night', 'ورقة ليلة الاختبار', 'must', 'الفصل كله في صفحة',
    box('القالب الذهبي', r'''    <p class="en">Base → Assume (for a positive integer \(k\)) → Show (\(n = k + 1\)) → Step (By the inductive hypothesis) → By the Principle of Mathematical Induction</p>
    <p><b>من m:</b> الأساس \(P(m)\)، والفرض ''' + lt(r'where \(k \ge m\)') + r'''. <b>قوي:</b> الفرض لكل i من 1 إلى k، وسطر ★، و''' + lt(r'Since \(k + 1 \ge 3\)') + r'''، والختام فيه ''' + lt('Strong') + r'''.</p>
''') +
    '  <div class="grid2">\n' +
    box('حركة الخطوة لكل نوع', r'''      <ul>
        <li><b>مجموع:</b> افصل آخر حد وعوّض الفرض. وتريك الفرق في المسودة.</li>
        <li><b>كسور:</b> مقام مشترك بدون فك، والهدف يقول وش يختصر.</li>
        <li><b>قسمة:</b> اعزل وعوّض، أو اجمع واطرح.</li>
        <li><b>متباينة:</b> طبّق الفرض، كبّر بـ \(k \ge m\)، وسطر ★ لو لزم.</li>
        <li><b>قوي:</b> كل القيم الابتدائية، والحدين من الفرض.</li>
      </ul>
''', indent='    ') +
    box('الترتيب الحسن', r'''      <ul>
        <li>منتهية، أو جزء من \(\mathbb{N}\)، أو صحيحة من m وفوق: نعم.</li>
        <li>غير كذا: قطعة بدون أصغر عنصر بحركة «نص العدد» أو «ناقص 1».</li>
        <li>\([0, 1]\) لها أصغر عنصر، ومع كذا مو مرتبة.</li>
      </ul>
''', indent='    ') +
    '  </div>\n' +
    box('برهان مبدأ الاستقراء (3 درجات)', chain(['نعكس', 'S الفاشلين لها أصغر s (الترتيب الحسن)', r'\(s \ge 2\) (الشرط 1)', r'\(P(s - 1)\) صحيحة', 'الشرط (2): \\(P(s)\\) صحيحة', 'تناقض'])) +
    '  <div class="grid2">\n' +
    box('الفخاخ', r'''      <ul>
        <li>جرّب \(n = 1, 2, 3\) قبل أي برهان.</li>
        <li>اقرأ البداية: positive من 1، nonnegative من 0.</li>
        <li>\(4 \cdot 2^{2k} - 1 \ne 4(2^{2k} - 1)\).</li>
        <li>«''' + lt(r'for every \(k\)') + r'''» في الفرض غلط.</li>
        <li>الخطوة بدون أساس ما تثبت شي.</li>
      </ul>
''', indent='    ') +
    box('أسئلة الاختبارات السابقة', r'''      <ul class="chk">
        <li><span class="cb"></span>برهان المبدأ · ميد 1447 <span class="pg ref" data-to="p-pmi"></span></li>
        <li><span class="cb"></span>المتتابعة \(2n - 1\) · ميد 1447 <span class="pg ref" data-to="p-sx"></span></li>
        <li><span class="cb"></span>مجموع الفرديات · نهائي 1446 <span class="pg ref" data-to="p-64"></span></li>
      </ul>
      <p class="small">جهّز نفسك لـ: توأم المتتابعة (\(a_n = n^2\))، ومجموع أو قسمة أو متباينة، وعبارة محرّفة تحتاج مثال مضاد.</p>
''', indent='    ') +
    '  </div>\n'))

save('g_u7.html', P)
