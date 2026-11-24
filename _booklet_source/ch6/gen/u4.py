import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []
U4 = U[4] + ' · 6.2'
CONC = 'اسم المبدأ كامل، ومعه البداية الصح.'

# ---------- p-gen: starting at m, example 3 ----------
P.append(page('p-gen', U4, 'cand', 'لما البداية مو 1: مثال 3' + tag('sol', 'مثال 3 في السلايدات'),
    stmt([(r'<span class="lb">The more general principle.</span> For a fixed integer \(m\), let \(S = \{i \in \mathbb{Z} : i \ge m\}\). For each integer \(n \in S\), let \(P(n)\) be a statement. If (1) \(P(m)\) is true and (2) the implication “If \(P(k)\), then \(P(k+1)\).” is true for every integer \(k \in S\), then \(P(n)\) is true for every integer \(n \in S\).',
           'نفس المبدأ، بس البداية m بدل 1: الأساس عند m، والفرض لـ k ≥ m.')]) +
    qbox(r'<span class="lb">Result.</span> For every nonnegative integer \(n\), \(2^n \gt n\).', 'البداية من 0.', lab='مثال 3 في السلايدات') +
    idea(r'<b>حركة الخطوة في المتباينات:</b> ابدأ من الطرف حق k + 1 (\(2^{k+1} = 2 \cdot 2^k\))، واستخدم الفرض، وبعدها خطوة صغيرة توصلك. هنا الخطوة الصغيرة \(k + k \ge k + 1\) تحتاج \(k \ge 1\)، فـ k = 0 نسويها لحالها (سطر ★).') +
    W([('1', 'الأساس', r'We proceed by induction. The inequality holds for \(n = 0\) since \(2^0 \gt 0\).', '\\(2^0 = 1\\)، و 1 > 0.'),
       ('2', 'الفرض', r'Assume that \(2^k \gt k\), where \(k\) is a nonnegative integer.', ''),
       ('3', 'المطلوب', r'We show that \(2^{k+1} \gt k + 1\).', ''),
       ('★', 'k = 0', r'When \(k = 0\), we have \(2^{k+1} = 2 \gt 1 = k + 1\). We therefore assume that \(k \ge 1\).', 'سطر ★: نخلص من k = 0 لحالها.', ST),
       ('4', 'الخطوة', r'Then \(2^{k+1} = 2 \cdot \hyp{2^k} \gt 2\hyp{k} = k + k \ge k + 1\).', r'بدّلنا \(2^k\) بالفرض (أكبر من k)، و \(k \ge 1\) تعطي \(k + k \ge k + 1\).', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(2^n \gt n\) for every nonnegative integer \(n\).', CONC)], title='نكتب (برهان السلايدات)') +
    note('trap', 'انتبه:', 'اقرأ البداية من السؤال: positive من 1، و nonnegative من 0، و n ≥ 5 من 5.')))

# ---------- p-ex4: example 4 ----------
P.append(page('p-ex4', U[4], 'cand', 'متباينة من n ≥ 5: مثال 4' + tag('sol', 'مثال 4 في السلايدات'),
    qbox(r'<span class="lb">Result.</span> For every integer \(n \ge 5\), \(2^n \gt n^2\).', r'البداية 5، لأن \(2^4 = 16\) مو أكبر من \(4^2 = 16\).', lab='مثال 4 في السلايدات (ما انسأل للحين)') +
    idea(r'بالأرقام: n = 4: 16 > 16 ' + NO + r'، و n = 5: 32 > 25 ' + OK + r'. الخطوة: \(2^{k+1} = 2 \cdot 2^k \gt 2k^2\)، وبعدها نستخدم \(k \ge 5\) مرتين: \(k^2 \ge 5k\) و \(3k \ge 15\).') +
    W([('1', 'الأساس', r'We proceed by induction. Since \(2^5 \gt 5^2\), the inequality holds for \(n = 5\).', '32 > 25.'),
       ('2', 'الفرض', r'Assume that \(2^k \gt k^2\) where \(k \ge 5\).', 'ولا تنسَ «where k ≥ 5».'),
       ('3', 'المطلوب', r'We show that \(2^{k+1} \gt (k+1)^2\).', ''),
       ('4', 'الخطوة', r'Observe that \[\begin{aligned} 2^{k+1} = 2 \cdot \hyp{2^k} \gt 2\hyp{k^2} = k^2 + k^2 &\ge k^2 + 5k = k^2 + 2k + 3k \\ &\ge k^2 + 2k + 15 \gt k^2 + 2k + 1 = (k+1)^2. \end{aligned}\] Therefore, \(2^{k+1} \gt (k+1)^2\).',
        r'الفرض (الأزرق)، وبعدها \(k \ge 5\): \(k^2 \ge 5k\) و \(3k \ge 15\). والهدف \(k^2 + 2k + 1\).', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(2^n \gt n^2\) for every integer \(n \ge 5\).', CONC)], title='نكتب (برهان السلايدات)') +
    twins([('q-622', '6.22.', EX['6.22'], 's-622')])))

# ---------- p-627: an inequality with a sum, then 6.27 ----------
P.append(page('p-627', U[4], 'low', 'متباينة فيها مجموع' + tag('sol', 'مثال إضافي'),
    qbox(r'<span class="lb">Result.</span> For every positive integer \(n\), \(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} \le \frac{n+1}{2}\).',
         'مثال إضافي مو من الكتاب، عشان تشوف نوع تمرين 6.27 محلول.', lab='مثال') +
    idea(r'حركة المجاميع والمتباينات مع بعض: افصل آخر حد، وبدّل الباقي بالفرض، وبعدها كبّر آخر حد: \(\frac{1}{k+1} \le \frac{1}{2}\) لأن \(k + 1 \ge 2\).') +
    W([('1', 'الأساس', r'Since \(1 \le \frac{1+1}{2} = 1\), the inequality holds for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(1 + \frac{1}{2} + \cdots + \frac{1}{k} \le \frac{k+1}{2}\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(1 + \frac{1}{2} + \cdots + \frac{1}{k+1} \le \frac{k+2}{2}\).', ''),
       ('4', 'الخطوة', r'Since \(k + 1 \ge 2\), \(\frac{1}{k+1} \le \frac{1}{2}\). By the inductive hypothesis, \(\hyp{1 + \cdots + \frac{1}{k}} + \frac{1}{k+1} \le \hyp{\frac{k+1}{2}} + \frac{1}{k+1} \le \frac{k+1}{2} + \frac{1}{2} = \frac{k+2}{2}.\)', '', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, the inequality holds for every positive integer \(n\).', '')], title='نكتب') +
    twins([('q-627', '6.27.', EX['6.27'], 's-627')])))

# ---------- p-pa: the power set (a theorem in the slides), then 6.19 ----------
P.append(page('p-pa', U[4], 'low', 'استقراء على عدد العناصر' + tag('sol', 'نظرية من السلايدات'),
    qbox(r'<span class="lb">Theorem.</span> If \(A\) is a finite set of cardinality \(n \ge 0\), then the cardinality of its power set \(\mathcal{P}(A)\) is \(2^n\).',
         'لو A فيها n عنصر، فعدد المجموعات الجزئية منها \\(2^n\\). البداية من 0 (المجموعة الفاضية).', lab='نظرية في السلايدات') +
    idea(r'الخطوة: المجموعات الجزئية من C (فيها k + 1 عنصر) نوعين: اللي ما فيها العنصر الأخير (\(2^k\) بالفرض)، واللي فيها (\(2^k\) بعد). المجموع \(2^{k+1}\).') +
    W([('1', 'الأساس', r'We proceed by induction. If \(A\) is a set with \(|A| = 0\), then \(A = \emptyset\). Thus, \(\mathcal{P}(A) = \{\emptyset\}\) and so \(|\mathcal{P}(A)| = 1 = 2^0\). Therefore, the theorem is true for \(n = 0\).', ''),
       ('2', 'الفرض', r'Assume that if \(B\) is any set with \(|B| = k\) for some nonnegative integer \(k\), then \(|\mathcal{P}(B)| = 2^k\).', ''),
       ('3', 'المطلوب', r'We show that if \(C\) is a set with \(|C| = k + 1\), then \(|\mathcal{P}(C)| = 2^{k+1}\). Let \(C = \{c_1, c_2, \ldots, c_{k+1}\}\).', ''),
       ('4', 'الخطوة', r'By the inductive hypothesis, there are \(\hyp{2^k}\) subsets of the set \(\{c_1, c_2, \ldots, c_k\}\), that is, there are \(2^k\) subsets of \(C\) not containing \(c_{k+1}\). Any subset of \(C\) containing \(c_{k+1}\) can be expressed as \(D \cup \{c_{k+1}\}\), where \(D \subseteq \{c_1, c_2, \ldots, c_k\}\). Again, by the inductive hypothesis, there are \(\hyp{2^k}\) such subsets \(D\). Therefore, there are \(2^k + 2^k = 2 \cdot 2^k = 2^{k+1}\) subsets of \(C\).', '', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, it follows for every nonnegative integer \(n\) that if \(|A| = n\), then \(|\mathcal{P}(A)| = 2^n\).', '')], title='نكتب (برهان السلايدات)') +
    twins([('q-619', '6.19.', EX['6.19'], 's-619')])))

# ---------- p-614: the book's result 6.14 ----------
P.append(page('p-614', U[4], 'cand', 'مثال الكتاب 6.14: ' + r'\(x^n\) زوجي' + tag('sol', 'مثال الكتاب 6.14'),
    qbox(r'<span class="lb">Result 6.14.</span> Let \(x \in \mathbb{Z}\). For every integer \(n \ge 2\), \(x^n\) is even if and only if \(x\) is even.',
         r'إذا وفقط إذا: اتجاه بالمباشر، والاتجاه الثاني بالاستقراء من n = 2. وتنفعك في «\(\sqrt[3]{2}\) غير نسبي» في الفصل 5.', lab='مثال من الكتاب في 6.2 (ما انسأل للحين)') +
    idea(r'الاتجاه الصعب: لو \(x^{k+1} = x \cdot x^k\) زوجي، فواحد من الاثنين زوجي (نظرية 3.17). لو x زوجي خلصنا، ولو \(x^k\) زوجي فالفرض يقول x زوجي.') +
    W([('⇐', 'مباشر', r'Assume, first, that \(x\) is even. Then \(x = 2y\) for some integer \(y\). Hence, \(x^n = x \cdot x^{n-1} = (2y)x^{n-1} = 2\left(yx^{n-1}\right)\). Since \(yx^{n-1}\) is an integer, \(x^n\) is even.', 'x زوجي، فـ \\(x^n\\) زوجي.'),
       ('1', 'الأساس', r'We now verify the converse, namely if \(x^n\) is even, where \(n \ge 2\), then \(x\) is even. We proceed by induction. If \(x^2\) is even, then we have already seen that \(x\) is even. Hence, the statement is true for \(n = 2\).', 'البداية من 2، والحالة n = 2 نعرفها من الفصل 3.'),
       ('2', 'الفرض', r'Assume that if \(x^k\) is even for some integer \(k \ge 2\), then \(x\) is even.', ''),
       ('3', 'المطلوب', r'We show that if \(x^{k+1}\) is even, then \(x\) is even.', ''),
       ('4', 'الخطوة', r'Let \(x^{k+1}\) be an even integer. Then \(x \cdot x^k\) is even. By Theorem 3.17, \(x\) or \(x^k\) is even. If \(x\) is even, then the result is proved. On the other hand, if \(\hyp{x^k}\) is even, then, by the induction hypothesis, \(x\) is even as well.', '', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, it follows, for every integer \(n \ge 2\), that if \(x^n\) is even, then \(x\) is even.', '')], title='نكتب (حل الكتاب)')))

# ---------- p-s4: solutions of unit 4 ----------
P.append(page('p-s4', 'حلول الوحدة 4', '', 'الحلول' + tag('sol', 'شيّك'),
    sh('تمرين 6.22', 's-622', SM('622')['back']) +
    W([('1', 'الأساس', r'Since \(3^1 = 3 \gt 1 = 1^2\), the statement is true for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(3^k \gt k^2\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(3^{k+1} \gt (k+1)^2\).', ''),
       ('★', 'k = 1', r'If \(k = 1\), then \(3^{k+1} = 9 \gt 4 = (k+1)^2\). So we may assume that \(k \ge 2\).', r'نحتاج \(k \ge 2\) تحت، فـ k = 1 لحالها.', ST),
       ('4', 'الخطوة', r'By the inductive hypothesis and since \(k \ge 2\), \(3^{k+1} = 3 \cdot \hyp{3^k} \gt 3\hyp{k^2} = k^2 + 2k^2 \ge k^2 + 4k = k^2 + 2k + 2k \ge k^2 + 2k + 4 \gt (k+1)^2.\)', r'\(2k^2 \ge 4k\) و \(2k \ge 4\) لأن \(k \ge 2\).', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(3^n \gt n^2\) for every positive integer \(n\).', '')], title='') +
    sh('تمرين 6.27', 's-627', SM('627')['back']) +
    W([('1', 'الأساس', r'Since \(1 \le 2 - \frac{1}{1} = 1\), the statement is true for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(1 + \frac{1}{4} + \cdots + \frac{1}{k^2} \le 2 - \frac{1}{k}\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(1 + \frac{1}{4} + \cdots + \frac{1}{(k+1)^2} \le 2 - \frac{1}{k+1}\).', ''),
       ('4', 'الخطوة', r'Since \(k(k+1) \lt (k+1)^2\), we have \(\frac{1}{(k+1)^2} \lt \frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}\). Hence, by the inductive hypothesis, \[\hyp{1 + \cdots + \frac{1}{k^2}} + \frac{1}{(k+1)^2} \le \hyp{2 - \frac{1}{k}} + \frac{1}{(k+1)^2} \lt 2 - \frac{1}{k} + \frac{1}{k} - \frac{1}{k+1} = 2 - \frac{1}{k+1}.\]', r'التريك: \(\frac{1}{(k+1)^2} \lt \frac{1}{k} - \frac{1}{k+1}\)، فينحذف \(\frac{1}{k}\).', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, the inequality holds for every positive integer \(n\).', '')], title='') +
    '', sol=True))

P.append(page('p-s4b', 'حلول الوحدة 4', '', 'حل تمرين 6.19' + tag('sol', 'شيّك'),
    sh('تمرين 6.19', 's-619', SM('619')['back']) +
    W([('1', 'الأساس', r'For \(n = 2\): if \(x_1 x_2 = 0\), then \(x_1 = 0\) or \(x_2 = 0\) by the given fact.', 'البداية من 2، والحقيقة المعطاة تكفي.'),
       ('2', 'الفرض', r'Assume for some integer \(k \ge 2\) that whenever \(y_1, \ldots, y_k\) are real numbers with \(y_1 y_2 \cdots y_k = 0\), at least one \(y_i\) is \(0\).', ''),
       ('3', 'المطلوب', r'Let \(x_1, \ldots, x_{k+1}\) be real numbers with \(x_1 x_2 \cdots x_{k+1} = 0\). We show that some \(x_i = 0\).', ''),
       ('4', 'الخطوة', r'Since \((x_1 x_2 \cdots x_k) \cdot x_{k+1} = 0\), the given fact gives \(x_1 \cdots x_k = 0\) or \(x_{k+1} = 0\). If \(x_{k+1} = 0\), we are done. Otherwise \(\hyp{x_1 \cdots x_k = 0}\), and by the inductive hypothesis \(x_i = 0\) for some \(i\) with \(1 \le i \le k\).', 'نعامل أول k أعداد كعدد واحد، ونطبق الحقيقة على عددين.', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, the implication holds for every integer \(n \ge 2\).', '')], title=''), sol=True))

save('e_u4.html', P)
