import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []
U3 = U[3] + ' · 6.1'

TEMPLATE = card('القالب الذهبي: 5 أسطر في كل برهان استقراء', [
    ('الأساس', r'عوّض \(n = 1\) وبيّن أن الطرفين متساويين: ' + lt(r'Since …, the statement is true for \(n = 1\).')),
    ('الفرض', 'انسخ الجملة وبدّل n بـ k: ' + lt(r'Assume that … for a positive integer \(k\).')),
    ('المطلوب', r'انسخها وبدّل n بـ \(k + 1\)، واكتبها قبل ما تحسب: ' + lt('We show that …')),
    ('الخطوة', 'ابدأ من يسار المطلوب، استخدم الفرض، ووصّل لليمين: ' + lt('By the inductive hypothesis, …')),
    ('الختام', lt(r'By the Principle of Mathematical Induction, … for every positive integer \(n\).'))])

# ---------- p-u3: template + slides Example 1 ----------
P.append(page('p-u3', U3, 'must', 'القالب الذهبي، وأول برهان' + tag('sol', 'مثال السلايدات 1'),
    TEMPLATE +
    qbox(r'Prove that \(1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}\) for every positive integer \(n\).',
         r'مجموع الأعداد من 1 إلى n يساوي \(n(n+1)/2\). <b>نفكر:</b> المجموع إلى \(k+1\) = (المجموع إلى k) + الحد الجديد \(k+1\). بأرقام: \(6 + 4 = 10 = 4 \cdot 5/2\).', lab='مثال 1') +
    W([R(B, r'Since \(1 = \frac{1 \cdot 2}{2}\), the statement is true for \(n = 1\).', 'الطرفين يساوون 1.'),
       R(A, r'Assume that \(1 + 2 + \cdots + k = \frac{k(k+1)}{2}\) for a positive integer \(k\).', 'الجملة عند k.'),
       R(S, r'We show that \(1 + 2 + \cdots + (k+1) = \frac{(k+1)(k+2)}{2}\).', r'الجملة عند \(k + 1\).'),
       R(ST, r'By the inductive hypothesis, \[\begin{aligned} 1 + 2 + \cdots + (k+1) &= (1 + 2 + \cdots + k) + (k+1) = \frac{k(k+1)}{2} + (k+1) \\ &= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}. \end{aligned}\]',
         r'فصلنا آخر حد، وعوّضنا الفرض، وطلّعنا \((k+1)\) عامل مشترك.'),
       R(C, r'By the Principle of Mathematical Induction, \(1 + 2 + \cdots + n = \frac{n(n+1)}{2}\) for every positive integer \(n\).')], title='نكتب (برهان السلايدات)', cls='tpl cmp') +
    note('trick', 'تريك «الفرق»:', r'المطلوب = الفرض + الحد الجديد. فاحسب في المسودة: (يمين المطلوب) − (يمين الفرض)، لازم يطلع الحد الجديد بالضبط. هنا: \(\frac{(k+1)(k+2)}{2} - \frac{k(k+1)}{2} = \frac{(k+1) \cdot 2}{2} = k + 1\) ' + OK + ' وكذا تعرف الخطوة قبل ما تكتبها.'),
    style='gap:2.8mm'))

# ---------- p-64: final 1446 ----------
P.append(page('p-64', U[3], 'must', 'تمرين 6.4' + tag('past', 'نهائي 1446 · 3 درجات'),
    qbox(r'<span class="lb">6.4.</span> Prove that \(1 + 3 + 5 + \cdots + (2n-1) = n^2\) for every positive integer \(n\) (1) by mathematical induction and (2) by adding \(1 + 3 + 5 + \cdots + (2n-1)\) and \((2n-1) + (2n-3) + \cdots + 1\).',
         r'مجموع الفرديات يساوي \(n^2\)، بطريقتين: (1) بالاستقراء، (2) بجمع المجموع مع نفسه مكتوب بالعكس. (في نهائي 1446 انطلب الجزء (1) بس، عليه 3 درجات.)', lab='دورك · تمرين 6.4', cls='ex') +
    '  <h3>(1) بالاستقراء: نفس مثال 1. كمّل الأسطر الفاضية</h3>\n' +
    recall(r'تريك الفرق قبل ما تكتب: \((k+1)^2 - k^2 = 2k + 1\)، وهو نفسه الحد الجديد ' + OK + ' فالخطوة: الفرض + \\(2k+1\\).') +
    W([R(B, r'Since \(1 = 1^2\), the statement is true for \(n = 1\).', r'عند \(n = 1\) الطرفين يساوون 1.'),
       (A[0], A[1], None, None, 'b1'),
       R(S, r'We show that \(1 + 3 + 5 + \cdots + (2k+1) = (k+1)^2\).', r'الحد الأخير عند \(k + 1\): \(2(k+1) - 1 = 2k + 1\).'),
       (ST[0], ST[1], None, None, 'b2'),
       (C[0], C[1], None, None, 'b1')], title='') +
    '  <h3>(2) بالجمع</h3>\n' +
    think('نفكر بأرقام أصغر', extra=r'''    <p>\(1 + 2 + 3 + 4\) واكتبه تحته بالعكس \(4 + 3 + 2 + 1\). اجمع عمود عمود: \(5 + 5 + 5 + 5 = 20\)، وهذا ضعف المجموع، فالمجموع 10. سوّ نفس الشي على الفرديات: كم مجموع كل عمود؟ وكم عمود؟</p>
''') +
    '  <div class="space" data-label="S = 1 + 3 + ⋯ + (2n−1)   و   S = (2n−1) + (2n−3) + ⋯ + 1"></div>\n' +
    hints([r'<b>تلميح (1):</b> افصل آخر حد \((2k+1)\)، وعوّض الباقي بالفرض \(k^2\).', r'<b>تلميح (2):</b> كل عمود مجموعه \(2n\)، وعندك n عمود.']),
    style='gap:3mm'))

# ---------- p-65 ----------
P.append(page('p-65', U[3], 'extra', 'تمرين 6.5' + tag('ex', 'دورك'),
    duork('6.5', r'<span class="lb">6.5.</span> Use mathematical induction to prove that \(1 + 5 + 9 + \cdots + (4n-3) = 2n^2 - n\) for every positive integer \(n\).',
          r'استخدم الاستقراء عشان تثبت أن \(1 + 5 + 9 + \cdots + (4n-3) = 2n^2 - n\)، لكل عدد صحيح موجب n.') +
    think('قبل ما تكتب: تريك الفرق في المسودة', [
        r'الحد الجديد: بدّل n بـ \(k+1\) في \(4n - 3\): يطلع \(4k + 1\).',
        r'احسب \(\left[2(k+1)^2 - (k+1)\right] - \left[2k^2 - k\right]\). لازم يطلع \(4k + 1\). طلع؟ إذن الخطوة بتمشي.',
        r'وتحقق سريع عند \(n = 2\): \(1 + 5 = 6\) و \(2 \cdot 4 - 2 = 6\) ' + OK]) +
    W(blank([(B, 'b1'), (A, 'b2'), (S, 'b2'), (ST, 'b3'), (C, 'b1')]), title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> الهدف بعد الفك: \(2(k+1)^2 - (k+1) = 2k^2 + 3k + 1\).'])))

# ---------- p-ex2: slides Example 2 ----------
P.append(page('p-ex2', U[3], 'extra', 'مثال: مجموع كسور' + tag('sol', 'مثال السلايدات 2'),
    qbox(r'Prove that \(\frac{1}{2\cdot 3} + \frac{1}{3\cdot 4} + \cdots + \frac{1}{(n+1)(n+2)} = \frac{n}{2n+4}\) for every positive integer \(n\).',
         r'مجموع هذي الكسور يساوي \(n/(2n+4)\). <b>نفكر:</b> نفس القالب. الحد الجديد عند \(k+1\): \(\frac{1}{(k+2)(k+3)}\). والهدف \(\frac{k+1}{2k+6}\) ما فيه \((k+2)\)، فلازم \((k+2)\) يختصر من البسط.', lab='مثال 2') +
    W([R(B, r'Since \(\frac{1}{2\cdot 3} = \frac{1}{6} = \frac{1}{2\cdot 1 + 4}\), the formula holds for \(n = 1\).', r'الطرفين يساوون \(1/6\).'),
       R(A, r'Assume that \(\frac{1}{2\cdot 3} + \cdots + \frac{1}{(k+1)(k+2)} = \frac{k}{2k+4}\) for a positive integer \(k\).', 'الجملة عند k.'),
       R(S, r'We show that \(\frac{1}{2\cdot 3} + \cdots + \frac{1}{(k+2)(k+3)} = \frac{k+1}{2k+6}\).', r'الجملة عند \(k + 1\).'),
       R(ST, r'By the inductive hypothesis, \[\begin{aligned} \frac{1}{2\cdot 3} + \cdots + \frac{1}{(k+2)(k+3)} &= \frac{k}{2(k+2)} + \frac{1}{(k+2)(k+3)} = \frac{k(k+3) + 2}{2(k+2)(k+3)} \\ &= \frac{(k+1)(k+2)}{2(k+2)(k+3)} = \frac{k+1}{2k+6}. \end{aligned}\]',
         r'عوّضنا الفرض، ووحّدنا المقام، وحلّلنا البسط، واختصرنا \((k+2)\).'),
       R(C, r'By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).')], title='نكتب (برهان السلايدات)') +
    box('3 قواعد للكسور', r'''    <ol>
      <li>اكتب المقام مضروب: \(2k + 4 = 2(k + 2)\). كذا يبان المقام المشترك.</li>
      <li>لا تفك المقام المشترك. خله مضروب عشان تشوف وش يختصر.</li>
      <li>الهدف يقول لك وش يختصر: العامل اللي مو في الهدف، دوّره في البسط.</li>
    </ol>
''')))

# ---------- p-611 ----------
P.append(page('p-611', U[3], 'extra', 'تمرين 6.11' + tag('ex', 'دورك'),
    duork('6.11', r'<span class="lb">6.11.</span> Prove that \(\frac{1}{3\cdot 4} + \frac{1}{4\cdot 5} + \cdots + \frac{1}{(n+2)(n+3)} = \frac{n}{3n+9}\) for every positive integer \(n\).',
          r'اثبت أن هذا المجموع يساوي \(n/(3n+9)\)، لكل عدد صحيح موجب n. توأم مثال 2.') +
    think('قبل ما تكتب: سخّن', extra=r'''    <p>جهّز الحركتين اللي بتحتاجها:</p>
    <p class="en">\(k^2 + 4k + 3 = (\) <span class="blank"></span> \()(\) <span class="blank"></span> \()\) &nbsp;&nbsp;&nbsp;&nbsp; \(3k + 9 = 3(\) <span class="blank"></span> \()\)</p>
    <p>وتريك الفرق: \(\frac{k+1}{3(k+4)} - \frac{k}{3(k+3)}\) لازم يساوي الحد الجديد \(\frac{1}{(k+3)(k+4)}\).</p>
''') +
    W(blank([(B, 'b1'), (A, 'b2'), (S, 'b2'), (ST, 'b3'), (C, 'b1')]), title='', cls='tpl grow') +
    hints([r'<b>تلميح 1:</b> \(3k + 9 = 3(k + 3)\)، فالمقام المشترك \(3(k+3)(k+4)\).', r'<b>تلميح 2:</b> البسط \(k(k+4) + 3 = (k+1)(k+3)\).',
           r'<b>تلميح 3:</b> الهدف \(\frac{k+1}{3(k+1)+9} = \frac{k+1}{3(k+4)}\).'])))

# ---------- solutions ----------
P.append(page('p-s3', 'حلول الوحدة 3', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>تمرين 6.4 (1)</h3>\n' +
    W([R(A, r'Assume that \(1 + 3 + 5 + \cdots + (2k-1) = k^2\) for a positive integer \(k\).', 'الجملة عند k.'),
       R(ST, r'By the inductive hypothesis, \({1 + 3 + \cdots + (2k-1) + (2k+1)} = {k^2 + (2k+1)} = {(k+1)^2}.\)', r'فصلنا آخر حد \((2k+1)\)، وعوّضنا الباقي بـ \(k^2\).'),
       R(C, r'By the Principle of Mathematical Induction, \(1 + 3 + 5 + \cdots + (2n-1) = n^2\) for every positive integer \(n\).')], title='') +
    '  <h3>تمرين 6.4 (2)</h3>\n' +
    W([('', 'البرهان', r'Let \(S = 1 + 3 + \cdots + (2n-1)\). Writing the terms in reverse order, \(S = (2n-1) + (2n-3) + \cdots + 1\). Adding the two expressions term by term, each of the \(n\) pairs has sum \(2n\), so \(2S = n(2n) = 2n^2\). Hence \(S = n^2\).',
        r'كل عمود مجموعه \(2n\)، وعندنا n عمود. فـ \(2S = 2n^2\).')], title='') +
    '  <h3>تمرين 6.5</h3>\n' +
    W([R(B, r'Since \(1 = 2 \cdot 1^2 - 1\), the statement is true for \(n = 1\).'),
       R(A, r'Assume that \(1 + 5 + \cdots + (4k-3) = 2k^2 - k\) for a positive integer \(k\).'),
       R(S, r'We show that \(1 + 5 + \cdots + (4k+1) = 2(k+1)^2 - (k+1)\).', r'الحد الأخير \(4(k+1) - 3 = 4k + 1\).'),
       R(ST, r'By the inductive hypothesis, \({1 + 5 + \cdots + (4k-3) + (4k+1)} = {(2k^2 - k) + (4k + 1)} = {2k^2 + 3k + 1} = {2(k+1)^2 - (k+1)}.\)', r'تريك الفرق قال لنا الجواب: \(2k^2 - k\) + \(4k + 1\).'),
       R(C, r'By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).')], title=''),
    sol=True))

P.append(page('p-s3b', 'حلول الوحدة 3', '', 'حل تمرين 6.11' + tag('sol', 'شيّك'),
    W([R(B, r'Since \(\frac{1}{3\cdot 4} = \frac{1}{12} = \frac{1}{3\cdot 1 + 9}\), the formula holds for \(n = 1\).', r'الطرفين \(1/12\).'),
       R(A, r'Assume that \(\frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+2)(k+3)} = \frac{k}{3k+9}\) for a positive integer \(k\).'),
       R(S, r'We show that \(\frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+3)(k+4)} = \frac{k+1}{3k+12}\).', r'الحد الجديد \(\frac{1}{(k+3)(k+4)}\).'),
       R(ST, r'By the inductive hypothesis, \[\begin{aligned} \frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+3)(k+4)} &= \frac{k}{3(k+3)} + \frac{1}{(k+3)(k+4)} = \frac{k(k+4) + 3}{3(k+3)(k+4)} \\ &= \frac{(k+1)(k+3)}{3(k+3)(k+4)} = \frac{k+1}{3(k+4)} = \frac{k+1}{3k+12}. \end{aligned}\]',
         r'نفس قواعد الكسور: الفرض، مقام مشترك بدون فك، تحليل البسط، نختصر \((k+3)\).'),
       R(C, r'By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).')], title='') +
    r'''  <p class="small">أجوبة التسخين: \(k^2+4k+3 = (k+1)(k+3)\) و \(3k+9 = 3(k+3)\). وتريك الفرق: \(\frac{(k+1)(k+3) - k(k+4)}{3(k+3)(k+4)} = \frac{3}{3(k+3)(k+4)} = \frac{1}{(k+3)(k+4)}\) ✓</p>
''' + box('راجع نفسك (3 دقائق)', '''    <ul class="chk">
      <li><span class="cb"></span>أكتب القالب الذهبي (5 أسطر) بدون ما أطالع.</li>
      <li><span class="cb"></span>أحسب تريك الفرق قبل ما أكتب الخطوة.</li>
      <li><span class="cb"></span>أفصل آخر حد، وأكتب ''' + lt('By the inductive hypothesis') + ''' في السطر اللي أعوّض فيه.</li>
    </ul>
'''), sol=True))

save('c_u3.html', P)
