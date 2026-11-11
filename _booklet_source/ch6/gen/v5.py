import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []
U5 = U[5] + ' · 6.2'

# ---------- p-u5 ----------
P.append(page('p-u5', U5, 'must', 'لما البداية مو 1',
    idea('أحياناً الجملة ما تصير صحيحة إلا من عدد معين. نفس القالب، بس الأساس عند هذا العدد (نسميه m).') +
    think(r'نجرب: \(2^n\) و \(n^2\)', before=tbl([r'\(n\)', '0', '1', '2', '3', '4', '5', '6'],
        [[r'\(2^n\)', '1', '2', '4', '8', '16', '32', '64'], [r'\(n^2\)', '0', '1', '4', '9', '16', '25', '36'],
         [r'\(2^n \gt n^2\)؟', OK, OK, NO, NO, NO, OK, OK]], ltr=True),
        extra=r'    <p>تفشل عند 2 و3 و4، ومن 5 وفوق صحيحة. فالكتاب يقول «لكل \(n \ge 5\)»، والأساس \(n = 5\). وهذا الجدول نفسه يعطيك m لأي سؤال.</p>' + '\n') +
    stmt([(r'<span class="lb">Theorem 6.8.</span> For a fixed integer \(m\), let \(S = \{i \in \mathbb{Z} : i \ge m\}\). For each \(n \in S\), let \(P(n)\) be a statement. If (1) \(P(m)\) is true and (2) \(P(k) \Rightarrow P(k+1)\) is true for every \(k \in S\), then \(P(n)\) is true for every \(n \in S\).',
           r'نفس مبدأ الاستقراء، بس الدومينو الأول عند m بدل 1. وهذا مسموح بسبب Theorem 6.7 (الوحدة 1).')]) +
    tbl([('السطر', 'width:22%'), 'البداية من 1', 'البداية من m'], [
        [B[1], r'\(P(1)\)', r'\(P(m)\)'],
        [A[1], lt(r'for a positive integer \(k\)'), lt(r'where \(k \ge m\)')],
        [C[1], lt(r'for every positive integer \(n\)'), lt(r'for every integer \(n \ge m\)')]], indent='  ') +
    card('بطاقة الخطوة 4: المتباينات', [
        ('طبّق الفرض', r'ابدأ من يسار المطلوب، وطلّع منه شكل الفرض: \(2^{k+1} = 2 \cdot 2^k \gt 2k^2\).'),
        ('كبّر', r'استخدم \(k \ge m\) خطوة خطوة لين توصل يمين المطلوب. كل \(\gt\) أو \(\ge\) لازم لها سبب.'),
        ('★ k الصغيرة', 'لو الخطوة احتاجت k أكبر من بداية الفرض، اثبت القيم الصغيرة لوحدها بالأرقام.')]) +
    note('trap', 'فخ ' + lt('Prove or disprove') + ':', r'«\(2^n \gt n^2\) لكل \(n \in \mathbb{N}\)» خاطئة: \(n = 2\) يعطي \(4 \gt 4\)، وهذا خطأ.'),
    style='gap:3mm'))

# ---------- p-ex4 ----------
P.append(page('p-ex4', U[5], 'must', r'مثال: \(2^n \gt n^2\)' + tag('sol', 'مثال السلايدات 4'),
    qbox(r'Prove that \(2^n \gt n^2\) for every integer \(n \ge 5\).',
         r'لكل عدد صحيح n من 5 وفوق. <b>نفكر:</b> الحركة 1 تعطي \(2^{k+1} \gt 2k^2\)، وباقي نثبت \(2k^2 \gt (k+1)^2\). بالأرقام:', lab='مثال 4') +
    tbl([r'\(k\)', r'\(2^{k+1}\)', r'\(2k^2\)', r'\((k+1)^2\)'], [['5', '64', '50', '36'], ['6', '128', '72', '49'], ['7', '256', '98', '64']], ltr=True, style='table-layout:fixed', indent='  ') +
    '  <p class="small">في كل سطر: الأول أكبر من الثاني (بسبب الفرض)، والثاني أكبر من الثالث (بسبب \\(k \\ge 5\\)). هذي هي السلسلة.</p>\n' +
    W([R(B, r'Since \(2^5 = 32 \gt 25 = 5^2\), the inequality holds for \(n = 5\).', r'الأساس عند \(m = 5\).'),
       R(A, r'Assume that \(2^k \gt k^2\), where \(k \ge 5\).', r'الفرض فيه \(k \ge 5\): هذا اللي بنستخدمه في التكبير.'),
       R(S, r'We show that \(2^{k+1} \gt (k+1)^2\).'),
       R(ST, r'\[\begin{aligned} 2^{k+1} = 2 \cdot 2^k \gt 2k^2 = k^2 + k^2 &\ge k^2 + 5k = k^2 + 2k + 3k \\ &\ge k^2 + 2k + 15 \gt k^2 + 2k + 1 = (k+1)^2. \end{aligned}\]',
         r'سبب كل علامة: \(\gt 2k^2\) الفرض. \(k^2 \ge 5k\) و \(3k \ge 15\) لأن \(k \ge 5\). وآخر وحدة لأن \(15 \gt 1\).'),
       R(C, r'By the Principle of Mathematical Induction, \(2^n \gt n^2\) for every integer \(n \ge 5\).')], title='نكتب (برهان السلايدات)') +
    note('trick', 'تريك التكبير:', r'عشان تكبّر \(k^2\)، حط m مكان واحد من الـ k: \(k^2 = k \cdot k \ge 5k\). وكذا أي \(ak \ge am\).') +
    box('3 أخطاء تنقص درجات', r'''    <ol class="notes">
      <li>تبدأ من المطلوب \(2^{k+1} \gt (k+1)^2\) وتشتغل على الطرفين. هذا افتراض للمطلوب.</li>
      <li>تكتب \(\ge\) أو \(\gt\) بدون سبب تقدر تقوله.</li>
      <li>تستخدم \(k \ge 5\) وأنت ما كتبته في الفرض.</li>
    </ol>
'''), style='gap:2.6mm'))

# ---------- p-ex3 ----------
P.append(page('p-ex3', U[5], 'must', 'مثال: لما k الصغيرة تخرب الخطوة' + tag('sol', 'مثال السلايدات 3'),
    qbox(r'Prove that \(2^n \gt n\) for every nonnegative integer \(n\).',
         r'لكل عدد صحيح غير سالب n (0، 1، 2، …)، \(2^n \gt n\).', lab='مثال 3') +
    think('نفكر', [r'الخطوة: \(2^{k+1} = 2 \cdot 2^k \gt 2k\)، وباقي نحتاج \(2k \ge k + 1\)، يعني \(k \ge 1\).',
                   r'بس الفرض يبدأ من \(k = 0\)! وعند \(k = 0\): \(2k = 0\) و \(k + 1 = 1\)، و \(0 \ge 1\) خطأ. فنثبت \(k = 0\) بالأرقام لوحدها (سطر ★)، ونكمل الخطوة لـ \(k \ge 1\).']) +
    W([R(B, r'The inequality holds for \(n = 0\) since \(2^0 = 1 \gt 0\).'),
       R(A, r'Assume that \(2^k \gt k\), where \(k\) is a nonnegative integer.'),
       R(S, r'We show that \(2^{k+1} \gt k + 1\).'),
       R(SK, r'When \(k = 0\), we have \(2^{k+1} = 2 \gt 1 = k + 1\). We therefore assume that \(k \ge 1\).', r'سطر ★: يثبت \(P(1)\) بالأرقام، وبعدها \(k \ge 1\).'),
       R(ST, r'Then \(2^{k+1} = 2 \cdot 2^k \gt 2k = k + k \ge k + 1\).', r'الفرض أعطى \(\gt 2k\)، و \(k \ge 1\) أعطت \(k + k \ge k + 1\).'),
       R(C, r'By the Principle of Mathematical Induction, \(2^n \gt n\) for every nonnegative integer \(n\).')], title='نكتب (برهان السلايدات)') +
    box('كيف تعرف إنك تحتاج سطر ★؟ 3 أسئلة في المسودة', r'''    <ol>
      <li>وش شرط k اللي استخدمته في الخطوة؟ (هنا \(k \ge 1\))</li>
      <li>من وين يبدأ الفرض؟ (هنا \(k \ge 0\))</li>
      <li>القيم اللي بينهم (هنا \(k = 0\)) تثبتها لوحدها في سطر ★: تحسب \(P(k+1)\) بالأرقام.</li>
    </ol>
'''), style='gap:2.9mm'))

# ---------- p-622 ----------
P.append(page('p-622', U[5], 'must', 'تمرين 6.22' + tag('ex', 'دورك'),
    duork('6.22', r'<span class="lb">6.22.</span> Prove that \(3^n \gt n^2\) for every positive integer \(n\).', r'اثبت أن \(3^n \gt n^2\)، لكل عدد صحيح موجب n.') +
    think('قبل ما تكتب: الأسئلة الثلاث في المسودة', [
        r'الخطوة: \(3^{k+1} = 3 \cdot 3^k \gt 3k^2\)، وتحتاج \(3k^2 \ge (k+1)^2\). جرّبها عند \(k = 1\): 3 مقابل 4. وش لاحظت؟',
        r'وعند \(k = 2\): 12 مقابل 9 ' + OK + ' فمن وين يبدأ شرط الخطوة؟ ومن وين يبدأ الفرض؟',
        'اللي بينهم يروح لسطر ★.']) +
    W(blank([(B, 'b1'), (A, 'b1'), (S, 'b1'), (SK, 'b1'), (ST, 'b3'), (C, 'b1')]), title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> لـ \(k \ge 2\): \(3k^2 = k^2 + 2k^2 \ge k^2 + 4k = k^2 + 2k + 2k \ge k^2 + 2k + 4\).'])))

# ---------- p-627: extra example + 6.27 ----------
P.append(page('p-627', U[5], 'extra', 'متباينة فيها مجموع، ودورك 6.27' + tag('sol', 'مثال إضافي') + tag('ex', 'دورك'),
    qbox(r'Prove that \(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} \le \frac{n+1}{2}\) for every positive integer \(n\).',
         r'<b>نفكر:</b> بعد الفرض: المجموع \(\le \frac{k+1}{2} + \frac{1}{k+1}\). والمطلوب \(\frac{k+2}{2} = \frac{k+1}{2} + \frac{1}{2}\). فيكفي \(\frac{1}{k+1} \le \frac{1}{2}\)، وهذي صحيحة لأن \(k + 1 \ge 2\). (مثال إضافي مو من الكتاب، نوع 6.27.)', lab='مثال إضافي') +
    W([R(B, r'Since \(1 \le \frac{1+1}{2} = 1\), the inequality holds for \(n = 1\).'),
       R(A, r'Assume that \(1 + \frac{1}{2} + \cdots + \frac{1}{k} \le \frac{k+1}{2}\) for a positive integer \(k\).'),
       R(S, r'We show that \(1 + \frac{1}{2} + \cdots + \frac{1}{k+1} \le \frac{k+2}{2}\).'),
       R(ST, r'Since \(k + 1 \ge 2\), \(\frac{1}{k+1} \le \frac{1}{2}\). By the inductive hypothesis, \(1 + \cdots + \frac{1}{k} + \frac{1}{k+1} \le \frac{k+1}{2} + \frac{1}{k+1} \le \frac{k+1}{2} + \frac{1}{2} = \frac{k+2}{2}.\)', 'افصل الحد الجديد، طبّق الفرض، وكبّر الحد الجديد إلى 1/2.'),
       R(C, r'By the Principle of Mathematical Induction, the inequality holds for every positive integer \(n\).')], title='', cls='tpl cmp') +
    duork('6.27', r'<span class="lb">6.27.</span> Prove that \(1 + \frac{1}{4} + \frac{1}{9} + \cdots + \frac{1}{n^2} \le 2 - \frac{1}{n}\) for every positive integer \(n\).',
          r'نفس الهيكل. بعد الفرض، وش يكفيك تثبت عن الحد الجديد \(1/(k+1)^2\)؟') +
    W(blank([(B, 'b1'), (A, 'b1'), (S, 'b1'), (ST, 'b2'), (C, 'b1')]), title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> يكفي \(\frac{1}{(k+1)^2} \le \frac{1}{k} - \frac{1}{k+1} = \frac{1}{k(k+1)}\)، وهذا صحيح لأن \(k(k+1) \lt (k+1)^2\).']),
    style='gap:2.6mm'))

# ---------- p-pa: power set (slides) ----------
P.append(page('p-pa', U[5], 'extra', 'مثال: الاستقراء على عدد العناصر' + tag('sol', 'من السلايدات'),
    qbox(r'<span class="lb">Theorem 6.16.</span> If \(A\) is a finite set of cardinality \(n \ge 0\), then the cardinality of its power set \(\mathcal{P}(A)\) is \(2^n\).',
         'لو A فيها n عنصر، فعدد مجموعاتها الجزئية \\(2^n\\). (' + lt('cardinality') + ' = عدد العناصر \\(|A|\\)، و' + lt('power set') + ' = كل المجموعات الجزئية.) <b>نفكر:</b> كل ما زاد عنصر يتضاعف العدد. شوف \\(\\{1, 2, 3\\}\\):', lab='مثال') +
    tbl(['ما فيها 3: الجزئية من \\(\\{1, 2\\}\\)', 'فيها 3: نفسها + 3'], [[r'\(\emptyset,\ \{1\},\ \{2\},\ \{1, 2\}\)', r'\(\{3\},\ \{1, 3\},\ \{2, 3\},\ \{1, 2, 3\}\)'], ['4', '4، والمجموع \\(8 = 2^3\\)']], indent='  ') +
    W([R(B, r'If \(A\) is a set with \(|A| = 0\), then \(A = \emptyset\). Thus, \(\mathcal{P}(A) = \{\emptyset\}\) and so \(|\mathcal{P}(A)| = 1 = 2^0\). Therefore, the theorem is true for \(n = 0\).', r'الفاضية لها مجموعة جزئية وحدة: نفسها.'),
       R(A, r'Assume that if \(B\) is any set with \(|B| = k\) for some nonnegative integer \(k\), then \(|\mathcal{P}(B)| = 2^k\).', 'الفرض عن <b>أي</b> مجموعة B فيها k عنصر.'),
       R(S, r'We show that if \(C\) is a set with \(|C| = k + 1\), then \(|\mathcal{P}(C)| = 2^{k+1}\). Let \(C = \{c_1, c_2, \ldots, c_{k+1}\}\).', 'مجموعة جديدة C فيها \\(k + 1\\).'),
       R(ST, r'By the inductive hypothesis, there are \(2^k\) subsets of the set \(\{c_1, c_2, \ldots, c_k\}\), that is, there are \(2^k\) subsets of \(C\) not containing \(c_{k+1}\). Any subset of \(C\) containing \(c_{k+1}\) can be expressed as \(D \cup \{c_{k+1}\}\), where \(D \subseteq \{c_1, c_2, \ldots, c_k\}\). Again, by the inductive hypothesis, there are \(2^k\) such subsets \(D\). Therefore, there are \(2^k + 2^k = 2 \cdot 2^k = 2^{k+1}\) subsets of \(C\).',
         r'اللي ما فيها آخر عنصر: \(2^k\). واللي فيها: نفس العدد. المجموع \(2^{k+1}\).'),
       R(C, r'By the Principle of Mathematical Induction, it follows for every nonnegative integer \(n\) that if \(|A| = n\), then \(|\mathcal{P}(A)| = 2^n\).')], title='', cls='tpl cmp') +
    note('trick', 'لاحظ الأسماء:', 'الفرض عن «أي مجموعة B»، والخطوة عن C جديدة. عشان تقدر تطبّق الفرض على \\(\\{c_1, \\ldots, c_k\\}\\). نفس الشي في 6.19: الفرض عن أي أعداد \\(y_1, \\ldots, y_k\\).'),
    style='gap:2.8mm'))

# ---------- p-619 ----------
P.append(page('p-619', U[5], 'extra', 'تمرين 6.19' + tag('ex', 'دورك'),
    duork('6.19', r'<span class="lb">6.19.</span> Prove the following implication for every integer \(n \ge 2\): If \(x_1, x_2, \ldots, x_n\) are any \(n\) real numbers such that \(x_1 \cdot x_2 \cdots x_n = 0\), then at least one of the numbers \(x_1, x_2, \ldots, x_n\) is \(0\). (Use the fact that if the product of two real numbers is \(0\), then at least one of the numbers is \(0\).)',
          r'لكل \(n \ge 2\): لو حاصل ضرب n أعداد حقيقية صفر، فواحد منها على الأقل صفر. (استخدم الحقيقة: لو حاصل ضرب عددين صفر، فواحد منهم صفر.)') +
    think('قبل ما تكتب', [r'الأساس \(n = 2\): هو نفس الحقيقة المعطاة.',
                          r'الفرض عن <b>أي</b> k أعداد، بأسماء جديدة \(y_1, \ldots, y_k\) (مثل B في المثال اللي قبل).',
                          r'الخطوة: \(x_1 \cdots x_{k+1} = (x_1 \cdots x_k) \cdot x_{k+1}\). طبّق الحقيقة على العددين، وبتطلع حالتين.']) +
    W(blank([(B, 'b1'), (A, 'b2'), (S, 'b1'), (ST, 'b3'), (C, 'b1')]), title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> يا \(x_{k+1} = 0\) وخلصنا، يا \(x_1 \cdots x_k = 0\) وهنا تطبّق الفرض.'])))

# ---------- solutions ----------
P.append(page('p-s5', 'حلول الوحدة 5', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>تمرين 6.22</h3>\n' +
    W([R(B, r'Since \(3^1 = 3 \gt 1 = 1^2\), the statement is true for \(n = 1\).'),
       R(A, r'Assume that \(3^k \gt k^2\) for a positive integer \(k\).'),
       R(S, r'We show that \(3^{k+1} \gt (k+1)^2\).'),
       R(SK, r'If \(k = 1\), then \(3^{k+1} = 9 \gt 4 = (k+1)^2\). So we may assume that \(k \ge 2\).', r'الخطوة تحتاج \(k \ge 2\)، فـ \(k = 1\) بالأرقام.'),
       R(ST, r'By the inductive hypothesis and since \(k \ge 2\), \(3^{k+1} = {3 \cdot 3^k} \gt {3k^2} = {k^2 + 2k^2} \ge {k^2 + 4k} = {k^2 + 2k + 2k} \ge {k^2 + 2k + 4} \gt {(k+1)^2}.\)',
         r'\(\gt 3k^2\) الفرض. \(2k^2 \ge 4k\) و \(2k \ge 4\) لأن \(k \ge 2\).'),
       R(C, r'By the Principle of Mathematical Induction, \(3^n \gt n^2\) for every positive integer \(n\).')], title='') +
    '  <h3>تمرين 6.27</h3>\n' +
    W([R(B, r'Since \(1 \le 2 - \frac{1}{1} = 1\), the statement is true for \(n = 1\).'),
       R(A, r'Assume that \(1 + \frac{1}{4} + \cdots + \frac{1}{k^2} \le 2 - \frac{1}{k}\) for a positive integer \(k\).'),
       R(S, r'We show that \(1 + \frac{1}{4} + \cdots + \frac{1}{(k+1)^2} \le 2 - \frac{1}{k+1}\).'),
       R(ST, r'Since \(k(k+1) \lt (k+1)^2\), we have \(\frac{1}{(k+1)^2} \lt \frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}\). Hence, by the inductive hypothesis, \[1 + \cdots + \frac{1}{k^2} + \frac{1}{(k+1)^2} \le 2 - \frac{1}{k} + \frac{1}{(k+1)^2} \lt 2 - \frac{1}{k} + \frac{1}{k} - \frac{1}{k+1} = 2 - \frac{1}{k+1}.\]',
         r'كبّرنا الحد الجديد إلى \(\frac{1}{k} - \frac{1}{k+1}\)، فراحت \(-\frac{1}{k}\) مع \(+\frac{1}{k}\).'),
       R(C, r'By the Principle of Mathematical Induction, the inequality holds for every positive integer \(n\).')], title=''),
    sol=True, style='gap:2.8mm'))

P.append(page('p-s5b', 'حلول الوحدة 5', '', 'حل تمرين 6.19' + tag('sol', 'شيّك'),
    W([R(B, r'For \(n = 2\): if \(x_1 x_2 = 0\), then \(x_1 = 0\) or \(x_2 = 0\) by the given fact.', 'الحقيقة المعطاة نفسها.'),
       R(A, r'Assume for some integer \(k \ge 2\) that whenever \(y_1, \ldots, y_k\) are real numbers with \(y_1 y_2 \cdots y_k = 0\), at least one \(y_i\) is \(0\).', 'عن أي k أعداد، بأسماء جديدة.'),
       R(S, r'Let \(x_1, \ldots, x_{k+1}\) be real numbers with \(x_1 x_2 \cdots x_{k+1} = 0\). We show that some \(x_i = 0\).'),
       R(ST, r'Since \((x_1 x_2 \cdots x_k) \cdot x_{k+1} = 0\), the given fact gives \(x_1 \cdots x_k = 0\) or \(x_{k+1} = 0\). If \(x_{k+1} = 0\), we are done. Otherwise \(x_1 \cdots x_k = 0\), and by the inductive hypothesis \(x_i = 0\) for some \(i\) with \(1 \le i \le k\).',
         'جمّعنا أول k في عدد واحد، وطبّقنا حقيقة العددين، وطلعت حالتين.'),
       R(C, r'By the Principle of Mathematical Induction, the implication holds for every integer \(n \ge 2\).')], title='') +
    box('راجع نفسك (3 دقائق)', '''    <ul class="chk">
      <li><span class="cb"></span>أعرف وش يتغير لما البداية m: الأساس، والفرض، والختام.</li>
      <li><span class="cb"></span>أقول حركات المتباينات من ذاكرتي: طبّق الفرض، كبّر، ★ k الصغيرة.</li>
      <li><span class="cb"></span>أكتب سبب كل علامة \\(\\gt\\) أو \\(\\ge\\).</li>
    </ul>
'''), sol=True))

save('e_u5.html', P)
