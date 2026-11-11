import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []
U6 = U[6] + ' · 6.3'

# ---------- p-strong ----------
P.append(page('p-strong', U6, 'must', 'الاستقراء القوي: نبدأ بأرقام',
    idea('أحياناً عشان تثبت الحالة الجاية تحتاج أكثر من حالة وحدة قبلها. هنا يجي الاستقراء القوي.') +
    think('متتابعة: كل حد يعتمد على الحدين اللي قبله', before=r'''    <p>المتتابعة أعداد مرتبة \(a_1, a_2, a_3, \ldots\). خذ: \(a_1 = 1\)، \(a_2 = 3\) (القيم الابتدائية، ''' + lt('initial values') + r''')، وكل حد بعدها \(a_n = 2a_{n-1} - a_{n-2}\) (القاعدة، ''' + lt('recurrence relation') + r''').</p>
''' + tbl([r'\(a_3\)', r'\(a_4\)', r'\(a_5\)', r'\(a_6\)'], [[r'\(2 \cdot 3 - 1 = 5\)', r'\(2 \cdot 5 - 3 = 7\)', r'\(2 \cdot 7 - 5 = 9\)', r'\(2 \cdot 9 - 7 = 11\)']], ltr=True),
        extra=r'''    <p>الحدود 1، 3، 5، 7، 9، 11: الفردية، فالتخمين \(a_n = 2n - 1\). وعشان تحسب \(a_5\) احتجت \(a_4\) و \(a_3\) الاثنين، فالفرض العادي (حالة k بس) ما يكفي.</p>
''') +
    stmt([(r'<span class="lb">The Strong Principle of Mathematical Induction.</span> For each positive integer \(n\), let \(P(n)\) be a statement. If (1) \(P(1)\) is true and (2) for every positive integer \(k\), if \(P(i)\) is true for every integer \(i\) with \(1 \le i \le k\), then \(P(k+1)\) is true, then \(P(n)\) is true for every positive integer \(n\).',
           r'نفس المبدأ، بس في الخطوة تفترض كل الحالات من 1 إلى k، مو k بس. ومسموح، لأنك لما توصل لـ \(k + 1\) كل اللي قبلها صار مثبت.')]) +
    card('بطاقة الاستقراء القوي: 3 فروق عن القالب العادي', [
        ('الأساس و★', 'كل قيمة ابتدائية تحتاج إثبات: الأساس لأول وحدة، وسطر ★ للباقي.'),
        ('الفرض القوي', lt(r'Assume … for all integers \(i\) with \(1 \le i \le k\).')),
        ('الخطوة', lt(r'Since \(k + 1 \ge 3\), …') + ' عشان يحق لك تستخدم القاعدة، وبعدين عوّض الحدين من الفرض.')]) +
    note('trick', 'عادي أو قوي؟', r'اسأل: الحد الجديد يحتاج كم حد قبله؟ حد واحد (مثل \(a_{k+1} = 2a_k\)): عادي. حدّين أو أكثر: قوي، ومعه سطر ★.'),
    style='gap:2.9mm'))

# ---------- p-sx ----------
P.append(page('p-sx', U[6], 'must', 'سؤال ميد 1447: المتتابعة' + tag('past', 'ميد 1447 · 4 درجات'),
    qbox(r'<span class="lb">7.</span> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\), \(a_2 = 3\) and \(a_n = 2a_{n-1} - a_{n-2}\) for \(n \ge 3\). Then \(a_n = 2n - 1\) for all \(n \in \mathbb{N}\). (4 marks)',
         r'السؤال تحت «' + lt('Prove or disprove') + r'»، وهو مثال 6 في السلايدات بالحرف. <b>نفكر:</b> الحدود 1، 3، 5، 7 تطلع من \(2n - 1\)، فهي صحيحة ونبرهنها. والحد الجديد يحتاج حدّين، فالاستقراء قوي. بأرقام: \(a_5 = 2a_4 - a_3 = 2 \cdot 7 - 5 = 9 = 2 \cdot 5 - 1\) ' + OK) +
    W([R(B, r'Since \(a_1 = 2 \cdot 1 - 1 = 1\) and \(a_2 = 2 \cdot 2 - 1 = 3\), the formula holds for \(n = 1\) and \(n = 2\).', 'الحل الرسمي أثبت القيمتين الابتدائيتين هنا.'),
       R(A, r'Assume for an arbitrary positive integer \(k\) that \(a_i = 2i - 1\) for all integers \(i\) with \(1 \le i \le k\).', 'الفرض القوي: كل الحدود من 1 إلى k.'),
       R(S, r'We show that \(a_{k+1} = 2(k+1) - 1 = 2k + 1\).'),
       R(SK, r'Since \(a_2 = 3\), it follows that \(a_{k+1} = 2k + 1\) when \(k = 1\). Hence, we may assume that \(k \ge 2\).', r'عند \(k = 1\) القاعدة ما تشتغل (\(a_0\) مو موجود)، و \(a_2\) معطى.'),
       R(ST, r'Since \(k + 1 \ge 3\), it follows that \(a_{k+1} = {2a_k - a_{k-1}} = {2(2k - 1) - (2k - 3)} = {2k + 1}\), which is the desired result.', r'الفرض أعطانا \(a_k = 2k - 1\) و \(a_{k-1} = 2(k-1) - 1 = 2k - 3\).'),
       R(C, r'By the Strong Principle of Mathematical Induction, \(a_n = 2n - 1\) for all \(n \in \mathbb{N}\).', 'اسم المبدأ فيه ' + lt('Strong') + '.')], title='نكتب (الحل الرسمي)') +
    note('star', 'ملاحظة:', r'السلايدات كتبت \(n = 1\) بس في الأساس، وتركت \(a_2\) لسطر ★. والحل الرسمي كتب الاثنين في الأساس. الطريقتين صحيحتين، المهم ما تنسى \(a_2\).'),
    style='gap:3mm'))

# ---------- p-ex7 ----------
P.append(page('p-ex7', U[6], 'must', 'توأم سؤال الميد' + tag('ex', 'دورك'),
    qbox(r'<span class="lb">Example 7 (slides).</span> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\), \(a_2 = 4\) and \(a_n = 2a_{n-1} - a_{n-2} + 2\) for \(n \ge 3\). Then \(a_n = n^2\) for all \(n \in \mathbb{N}\).',
         r'اثبت أن \(a_n = n^2\). نفس سؤال الميد بالضبط، بس القاعدة فيها \(+2\). احتمال يجي هو هالسنة.', lab='دورك · مثال 7 من السلايدات', cls='ex') +
    recall(r'قبل ما تكتب: احسب \(a_3\) و \(a_4\) من القاعدة، وتأكد أنهم 9 و16. وبعدين: وش يعطيك الفرض القوي عن \(a_k\) و \(a_{k-1}\)؟') +
    W([R(B, r'Since \(a_1 = 1 = 1^2\), the formula holds for \(n = 1\).'),
       (A[0], A[1], None, None, 'b2'),
       R(S, r'We show that \(a_{k+1} = (k+1)^2\).'),
       (SK[0], SK[1], None, None, 'b1'),
       (ST[0], ST[1], None, None, 'b3'),
       (C[0], C[1], None, None, 'b1')], title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> بالفرض \(a_k = k^2\) و \(a_{k-1} = (k-1)^2\). عوّض في القاعدة، وفك \((k-1)^2 = k^2 - 2k + 1\).'])))

# ---------- p-633 ----------
P.append(page('p-633', U[6], 'extra', 'مثال: خمّن وأثبت، ودورك 6.33' + tag('sol', 'مثال إضافي') + tag('ex', 'دورك'),
    qbox(r'A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 2\) and \(a_n = a_{n-1} + 3\) for \(n \ge 2\). Conjecture a formula for \(a_n\) and verify that your conjecture is correct.',
         r'<b>نفكر:</b> الحدود 2، 5، 8، 11، فالتخمين \(a_n = 3n - 1\). والحد الجديد يحتاج حد واحد قبله، فالعادي يكفي. (مثال إضافي.)', lab='مثال') +
    W([R(B, r'Since \(a_1 = 2 = 3 \cdot 1 - 1\), the formula holds for \(n = 1\).'),
       R(A, r'Assume that \(a_k = 3k - 1\) for a positive integer \(k\).'),
       R(S, r'We show that \(a_{k+1} = 3(k+1) - 1 = 3k + 2\).'),
       R(ST, r'Since \(k + 1 \ge 2\), \(a_{k+1} = a_k + 3 = (3k - 1) + 3 = 3k + 2\).', r'«\(k + 1 \ge 2\)» لأن القاعدة تبدأ من \(n = 2\).'),
       R(C, r'By the Principle of Mathematical Induction, \(a_n = 3n - 1\) for every \(n \in \mathbb{N}\).')], title='', cls='tpl cmp') +
    duork('6.33', r'<span class="lb">6.33.</span> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\) and \(a_n = 2a_{n-1}\) for \(n \ge 2\). Conjecture a formula for \(a_n\) and verify that your conjecture is correct.',
          r'احسب أول الحدود، وخمّن الصيغة، وبرهنها بنفس خطوات المثال.') +
    W([('', 'احسب وخمّن', r'\(a_2 = \) <span class="blank s"></span>, \(a_3 = \) <span class="blank s"></span>, \(a_4 = \) <span class="blank s"></span>, \(a_5 = \) <span class="blank s"></span>. Conjecture: \(a_n = \) <span class="blank"></span>', None)] + blank([(B, 'b1'), (A, 'b1'), (S, 'b1'), (ST, 'b1'), (C, 'b1')]), title='', cls='tpl grow'),
    style='gap:2.6mm'))

# ---------- p-ex8 ----------
P.append(page('p-ex8', U[6], 'extra', r'مثال: كل عدد من 8 وفوق يُكتب \(3a + 5b\)' + tag('sol', 'مثال السلايدات 8'),
    qbox(r'For each integer \(n \ge 8\), there are nonnegative integers \(a\) and \(b\) such that \(n = 3a + 5b\).',
         r'كل عدد صحيح من 8 وفوق ينكتب \(3a + 5b\). (نفس تمرين 5.51 في ملزمة الفصل 5: هناك بالحالات، وهنا بالاستقراء القوي.)', lab='مثال 8') +
    think('نفكر', before=tbl([r'\(n\)', '8', '9', '10', '11', '12', '13'], [[r'\(3a + 5b\)', r'\(3 + 5\)', r'\(3 \cdot 3\)', r'\(5 \cdot 2\)', r'\(8 + 3\)', r'\(9 + 3\)', r'\(10 + 3\)']], ltr=True),
          extra=r'''    <p>من 11 وفوق: كل عدد = العدد اللي قبله بثلاث خانات + 3. فالخطوة ترجع 3 خانات، والفرض القوي يغطيها. و9 و10 لو رجعنا منهم 3 نوصل 6 و7 (تحت 8)، فنثبتهم بالأرقام في سطر ★.</p>
''') +
    W([R(B, r'Since \(8 = 3 \cdot 1 + 5 \cdot 1\), the statement is true for \(n = 8\).'),
       R(A, r'Assume for each integer \(i\) with \(8 \le i \le k\), where \(k \ge 8\), that there are nonnegative integers \(s\) and \(t\) such that \(i = 3s + 5t\).', 'فرض قوي يبدأ من 8.'),
       R(S, r'We show that \(k + 1 = 3x + 5y\) for some nonnegative integers \(x\) and \(y\).'),
       R(SK, r'Since \(9 = 3 \cdot 3 + 5 \cdot 0\) and \(10 = 3 \cdot 0 + 5 \cdot 2\), this is true if \(k + 1 = 9\) or \(k + 1 = 10\). So we may assume that \(k + 1 \ge 11\).'),
       R(ST, r'Then \(8 \le (k+1) - 3 \lt k\). By the induction hypothesis, there are nonnegative integers \(a\) and \(b\) such that \((k+1) - 3 = 3a + 5b\), and so \(k + 1 = 3(a+1) + 5b\). Letting \(x = a + 1\) and \(y = b\) gives the result.', r'رجعنا 3 خانات، والفرض كتبه \(3a + 5b\)، وزدنا 3.'),
       R(C, r'By the Strong Principle of Mathematical Induction, the statement holds for every integer \(n \ge 8\).')], title='', cls='tpl cmp') +
    note('trick', 'قاعدة عدد الأساسات:', r'= مقدار القفزة. هنا نطرح 3، فنحتاج 8 و9 و10. وفي المتتابعات: = عدد القيم الابتدائية.'),
    style='gap:2.8mm'))

# ---------- p-636 ----------
P.append(page('p-636', U[6], 'extra', 'تمرين 6.36: أعداد فيبوناتشي' + tag('ex', 'دورك'),
    duork('6.36', r'<span class="lb">6.36.</span> Consider the sequence \(F_1, F_2, F_3, \ldots\), where \(F_1 = 1\), \(F_2 = 1\), \(F_3 = 2\), \(F_4 = 3\), \(F_5 = 5\) and \(F_6 = 8\). The terms of this sequence are called <i>Fibonacci numbers</i>. (a) Define the sequence of Fibonacci numbers by means of a recurrence relation. (b) Prove that \(2 \mid F_n\) if and only if \(3 \mid n\).',
          r'المتتابعة 1، 1، 2، 3، 5، 8، … (a) اكتب قاعدتها. (b) اثبت أن \(F_n\) زوجي إذا وفقط إذا n يقبل القسمة على 3.') +
    think('نفكر: لاحظ النمط', before=tbl([r'\(n\)', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        [[r'\(F_n\)', '1', '1', '2', '3', '5', '8', '13', '21', '34'], ['زوجي؟', 'لا', 'لا', 'نعم', 'لا', 'لا', 'نعم', 'لا', 'لا', 'نعم']], ltr=True),
        extra=r'''    <p>كل حد = مجموع الحدين قبله، والزوجي يجي عند 3 و6 و9. فالاستقراء قوي (حدّين).</p>
''') +
    box('حقيقتين تحتاجهم', r'''    <ol>
      <li>فردي + فردي = زوجي، وفردي + زوجي = فردي.</li>
      <li>من أي ثلاث أعداد متتالية \(k-1, k, k+1\)، واحد بالضبط يقبل القسمة على 3.</li>
    </ol>
''') +
    '  <div class="space" data-label="(a) اكتب العلاقة التكرارية مع القيم الابتدائية" style="flex:1 1 24mm"></div>\n' +
    note('trick', '«إذا وفقط إذا» بدون تعب:', 'ما تحتاج اتجاهين منفصلين. في الخطوة حالتين: حالة الطرفين فيها صح، وحالة الطرفين فيها خطأ. البرهان في الصفحة الجاية.')))

P.append(page('p-636b', U[6], 'extra', 'تمرين 6.36 (b): البرهان' + tag('ex', 'دورك'),
    qbox(r'<span class="lb">(b)</span> Prove that \(2 \mid F_n\) if and only if \(3 \mid n\). &nbsp; Let \(P(n)\): \(F_n\) is even if and only if \(3 \mid n\).',
         r'اثبت أن \(F_n\) زوجي إذا وفقط إذا n يقبل القسمة على 3.', lab='دورك · تمرين 6.36 (b)', cls='ex') +
    recall(r'نفس بطاقة الاستقراء القوي: الأساس \(n = 1\)، وسطر ★ لـ \(F_2\)، والخطوة بعد ' + lt(r'Since \(k + 1 \ge 3\)') + r' فيها \(F_{k+1} = F_k + F_{k-1}\).') +
    W(blank([(B, 'b1'), (A, 'b2'), (SK, 'b1')]) +
      [(ST[0], 'حالة 1', r'Case 1. \(3 \mid (k+1)\).', None), ('', '', None, None, 'b3'),
       (ST[0], 'حالة 2', r'Case 2. \(3 \nmid (k+1)\).', None), ('', '', None, None, 'b3')] +
      blank([(C, 'b1')]), title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> إذا \(3 \mid (k+1)\) فإن \(3 \nmid k\) و \(3 \nmid (k-1)\)، فـ \(F_k\) و \(F_{k-1}\) فرديين بالفرض. وإذا \(3 \nmid (k+1)\) فواحد بالضبط من k و \(k-1\) يقبل القسمة على 3.'])))

# ---------- solutions ----------
P.append(page('p-s6a', 'حلول الوحدة 6', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>توأم سؤال الميد (Example 7)</h3>\n' +
    W([R(A, r'Assume for an arbitrary positive integer \(k\) that \(a_i = i^2\) for every integer \(i\) with \(1 \le i \le k\).', 'الفرض القوي.'),
       R(SK, r'Since \(a_2 = 4 = 2^2\), the formula holds when \(k = 1\). So we may assume that \(k \ge 2\).', r'\(a_2\) معطى.'),
       R(ST, r'Since \(k + 1 \ge 3\), and \(a_k = k^2\) and \(a_{k-1} = (k-1)^2\) by the inductive hypothesis, \[a_{k+1} = 2a_k - a_{k-1} + 2 = 2k^2 - (k^2 - 2k + 1) + 2 = k^2 + 2k + 1 = (k+1)^2.\]', 'عوّضنا الحدين من الفرض، وفكّينا.'),
       R(C, r'By the Strong Principle of Mathematical Induction, \(a_n = n^2\) for all \(n \in \mathbb{N}\).')], title='') +
    '  <h3>تمرين 6.33</h3>\n' +
    r'''  <p>الحدود: \(a_1 = 1,\ a_2 = 2,\ a_3 = 4,\ a_4 = 8,\ a_5 = 16\)، فالتخمين \(a_n = 2^{n-1}\).</p>
''' +
    W([R(B, r'Since \(a_1 = 1 = 2^0\), the formula holds for \(n = 1\).'),
       R(A, r'Assume that \(a_k = 2^{k-1}\) for a positive integer \(k\).'),
       R(S, r'We show that \(a_{k+1} = 2^k\).'),
       R(ST, r'Since \(k + 1 \ge 2\), \(\;a_{k+1} = 2a_k = 2 \cdot 2^{k-1} = 2^k\).', 'القاعدة، ثم الفرض.'),
       R(C, r'By the Principle of Mathematical Induction, \(a_n = 2^{n-1}\) for every \(n \in \mathbb{N}\).')], title='') +
    note('trap', 'فخ محتمل:', r'لو جت «\(a_n = 2^n\)» في ' + lt('Prove or disprove') + r'، جوابها False: \(a_1 = 1 \ne 2^1\).') +
    box('راجع نفسك (دقيقتين)', '''    <ul class="chk">
      <li><span class="cb"></span>أعرف متى أستخدم القوي بدل العادي (الحد الجديد يحتاج كم حد؟).</li>
      <li><span class="cb"></span>أكتب سطر ★ لكل قيمة ابتدائية بعد الأولى، و''' + lt(r'Since \(k + 1 \ge 3\)') + ''' قبل القاعدة.</li>
    </ul>
'''), sol=True, style='gap:2.8mm'))

P.append(page('p-s6b', 'حلول الوحدة 6', '', 'حل تمرين 6.36' + tag('sol', 'شيّك'),
    '  <h3>(a)</h3>\n' +
    W([('', 'الجواب', r'\(F_1 = F_2 = 1\) and \(F_n = F_{n-1} + F_{n-2}\) for every integer \(n \ge 3\).', 'أول حدين 1، وكل حد بعدهم = مجموع الحدين قبله.')], title='') +
    '  <h3>(b)</h3>\n' +
    W([('', 'الجملة', r'For each \(n \in \mathbb{N}\), let \(P(n)\): \(F_n\) is even if and only if \(3 \mid n\). We use the Strong Principle of Mathematical Induction.', None),
       R(B, r'\(F_1 = 1\) is odd and \(3 \nmid 1\), so \(P(1)\) is true.', 'الطرفين خطأ، فالـ «إذا وفقط إذا» صحيحة.'),
       R(A, r'Assume for an arbitrary positive integer \(k\) that \(P(i)\) is true for every integer \(i\) with \(1 \le i \le k\).'),
       R(S, r'We show that \(P(k+1)\) is true, that is, \(F_{k+1}\) is even if and only if \(3 \mid (k+1)\).'),
       R(SK, r'If \(k = 1\), then \(F_{k+1} = F_2 = 1\) is odd and \(3 \nmid 2\), so \(P(2)\) is true. So we may assume that \(k \ge 2\).'),
       R(ST, r'Since \(k + 1 \ge 3\), \(F_{k+1} = F_k + F_{k-1}\). Exactly one of \(k-1\), \(k\), \(k+1\) is divisible by 3.<br><i>Case 1.</i> \(3 \mid (k+1)\). Then \(3 \nmid k\) and \(3 \nmid (k-1)\), so \(F_k\) and \(F_{k-1}\) are odd by the hypothesis. Hence \(F_{k+1}\) is even.<br><i>Case 2.</i> \(3 \nmid (k+1)\). Then exactly one of \(k\) and \(k-1\) is divisible by 3, so exactly one of \(F_k\) and \(F_{k-1}\) is even. Hence \(F_{k+1}\) is odd.<br>Therefore \(F_{k+1}\) is even if and only if \(3 \mid (k+1)\).',
         'حالة 1: فردي + فردي = زوجي. حالة 2: زوجي + فردي = فردي.'),
       R(C, r'By the Strong Principle of Mathematical Induction, \(2 \mid F_n\) if and only if \(3 \mid n\), for every \(n \in \mathbb{N}\).')], title=''),
    sol=True))

save('f_u6.html', P)
