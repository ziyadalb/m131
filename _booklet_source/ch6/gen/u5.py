import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []
U5 = U[5] + ' · 6.3'
SCONC = 'لازم كلمة Strong في اسم المبدأ.'

# ---------- p-strong: the strong principle and recursive sequences ----------
P.append(page('p-strong', U5, 'top', 'الاستقراء القوي: نبدأ بأرقام' + tag('sol', 'من السلايدات'),
    stmt([(r'<span class="lb">The Strong Principle of Mathematical Induction.</span> For each positive integer \(n\), let \(P(n)\) be a statement. If (a) \(P(1)\) is true and (b) the implication “If \(P(i)\) for every integer \(i\) with \(1 \le i \le k\), then \(P(k+1)\).” is true for every positive integer \(k\), then \(P(n)\) is true for every positive integer \(n\).',
           'الفرق عن العادي: الفرض يغطي كل الأعداد من 1 إلى k، مو k بس.'),
          (r'<span class="lb">Recursively-defined sequence.</span> Only the first term or the first few terms are defined specifically (the initial values); then \(a_n\) is expressed in terms of earlier terms (the recurrence relation).',
           'المتتابعة التكرارية: أول حد أو أول حدّين معطيين، وكل حد بعدها يطلع من اللي قبله بقانون.')]) +
    idea(r'ليش قوي؟ في \(a_n = 2a_{n-1} - a_{n-2}\) كل حد يحتاج <b>حدّين</b> قبله. فالفرض لازم يعطيك \(a_k\) و \(a_{k-1}\) مع بعض، والفرض العادي يعطيك \(a_k\) بس.') +
    '  <h3>بالأرقام (من السلايدات): \\(a_1 = 1\\)، \\(a_2 = 3\\)، و \\(a_n = 2a_{n-1} - a_{n-2}\\)</h3>\n' +
    tbl([r'\(n\)', '1', '2', '3', '4', '5', '6'],
        [[r'\(a_n\)', '1', '3', r'\(2 \cdot 3 - 1 = 5\)', r'\(2 \cdot 5 - 3 = 7\)', '9', '11'],
         [r'\(2n - 1\)', '1', '3', '5', '7', '9', '11']], ltr=True).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    note('star', '«Find a₃ and a₄»:', 'جا في نوفمبر بدرجة. عوّض n = 3 وبعدها n = 4 في قانون التكرار، واكتب الحساب. ومن الجدول تخمّن الصيغة \\(a_n = 2n - 1\\)، وبعدها تبرهنها.')))

# ---------- p-nov3: the November question (= Mid 1447 = example 6) ----------
P.append(page('p-nov3', U[5], 'top', 'المتتابعة: سؤال نوفمبر' + tag('past', 'نوفمبر · 1+4'),
    qbox(r'<span class="lb">Question 3: (1+4)</span> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\), \(a_2 = 3\), and \(a_n = 2a_{n-1} - a_{n-2}\) for \(n \ge 3\). 1. Find \(a_3\) and \(a_4\). 2. Use the Strong Principle of Mathematical Induction to prove that \(a_n = 2n - 1\) for every positive integer \(n\).',
         'جا نفسه في ميد 1447 بس بدون الفقرة 1، وهو مثال 6 في السلايدات بالحرف.', lab='سؤال ميد نوفمبر · وميد 1447') +
    idea(r'<b>حركة القوي:</b> \(a_{k+1}\) من قانون التكرار، والحدّين \(a_k\) و \(a_{k-1}\) من الفرض (الأزرق). والقانون يشتغل لما \(k + 1 \ge 3\) بس، فـ k = 1 نسويها لحالها (سطر ★). وبدون سطر ★ وكلمة Strong البرهان ناقص.') +
    W([('1)', r'\(a_3, a_4\)', r'Letting \(n = 3\), we find that \(a_3 = 2a_2 - a_1 = 2(3) - 1 = 5\); while letting \(n = 4\), we have \(a_4 = 2a_3 - a_2 = 2(5) - 3 = 7\).', 'عوّضنا في القانون بالترتيب. هذي الدرجة الأولى.', dict(BKP, id='m-nov3')),
       ('1', 'الأساس', r'We proceed by induction. Since \(a_1 = 2 \cdot 1 - 1 = 1\), the formula holds for \(n = 1\).', 'في حل ميد 1447 كتبوا الأساس لـ \\(n = 1\\) و \\(n = 2\\) مع بعض، والطريقتين صح.'),
       ('2', 'الفرض', r'Assume for an arbitrary positive integer \(k\) that \(a_i = 2i - 1\) for all integers \(i\) with \(1 \le i \le k\).', 'الفرض القوي: لكل i من 1 إلى k.'),
       ('3', 'المطلوب', r'We show that \(a_{k+1} = 2(k+1) - 1 = 2k + 1\).', ''),
       ('★', 'k = 1', r'If \(k = 1\), then \(a_{k+1} = a_2 = 2 \cdot 1 + 1 = 3\). Since \(a_2 = 3\), it follows that \(a_{k+1} = 2k + 1\) when \(k = 1\). Hence, we may assume that \(k \ge 2\).', r'لما k = 1 ما فيه \(a_{k-1} = a_0\)، فنتأكد من \(a_2\) لحاله.', ST),
       ('4', 'الخطوة', r'Since \(k + 1 \ge 3\), it follows that \(a_{k+1} = 2\hyp{a_k} - \hyp{a_{k-1}} = 2\hyp{(2k - 1)} - \hyp{(2k - 3)} = 2k + 1\), which is the desired result.', r'من الفرض: \(a_k = 2k - 1\) و \(a_{k-1} = 2(k-1) - 1 = 2k - 3\).', HL),
       ('5', 'الختام', r'By the Strong Principle of Mathematical Induction, \(a_n = 2n - 1\) for all \(n \in \mathbb{N}\).', SCONC)], title='نكتب (حل السلايدات)') +
    ''))

# ---------- p-ex7: example 7 (the twin of the exam sequence) ----------
P.append(page('p-ex7', U[5], 'cand', 'توأم المتتابعة: مثال 7' + tag('sol', 'مثال 7 في السلايدات'),
    qbox(r'<span class="lb">Result.</span> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\), \(a_2 = 4\) and \(a_n = 2a_{n-1} - a_{n-2} + 2\) for \(n \ge 3\). Then \(a_n = n^2\) for all \(n \in \mathbb{N}\).',
         'نفس سؤال الاختبار، بس القانون يزيد 2 في آخره، والصيغة \\(n^2\\). أقرب شي ممكن يجي في البديل.', lab='مثال 7 في السلايدات (ما انسأل للحين)') +
    idea(r'بالأرقام: \(a_3 = 2 \cdot 4 - 1 + 2 = 9 = 3^2\) ' + OK + r'. نفس خطوات سؤال نوفمبر حرف بحرف، وتتغير الصيغة بس.') +
    W([('1', 'الأساس', r'We proceed by induction. Since \(a_1 = 1 = 1^2\), the formula holds for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume for an arbitrary positive integer \(k\) that \(a_i = i^2\) for every integer \(i\) with \(1 \le i \le k\).', ''),
       ('3', 'المطلوب', r'We show that \(a_{k+1} = (k+1)^2\).', ''),
       ('★', 'k = 1', r'Since \(a_2 = 4\), it follows that \(a_{k+1} = (k+1)^2\) when \(k = 1\). Thus, we may assume that \(k \ge 2\).', '', ST),
       ('4', 'الخطوة', r'Hence, \(k + 1 \ge 3\) and so \[\begin{aligned} a_{k+1} &= 2\hyp{a_k} - \hyp{a_{k-1}} + 2 = 2\hyp{k^2} - \hyp{(k-1)^2} + 2 \\ &= 2k^2 - (k^2 - 2k + 1) + 2 = k^2 + 2k + 1 = (k+1)^2. \end{aligned}\]', r'من الفرض: \(a_k = k^2\) و \(a_{k-1} = (k-1)^2\).', HL),
       ('5', 'الختام', r'By the Strong Principle of Mathematical Induction, \(a_n = n^2\) for all \(n \in \mathbb{N}\).', SCONC)], title='نكتب (حل السلايدات)') +
    twins([('q-t5', 'توأم.', r'A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 2\), \(a_2 = 4\) and \(a_n = a_{n-1} + 2a_{n-2}\) for \(n \ge 3\). Find \(a_3\) and \(a_4\), and prove that \(a_n = 2^n\) for all \(n \in \mathbb{N}\).', 's-t5')])))

# ---------- p-633: guess a formula, then prove it ----------
P.append(page('p-633', U[5], 'low', 'خمّن الصيغة وبرهنها' + tag('sol', 'مثال إضافي'),
    qbox(r'<span class="lb">Example.</span> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 2\) and \(a_n = a_{n-1} + 3\) for \(n \ge 2\). Conjecture a formula for \(a_n\) and verify that your conjecture is correct.',
         'مثال إضافي، عشان تشوف نوع تمرين 6.33 محلول.', lab='مثال') +
    idea(r'خمّن بالأرقام: 2، 5، 8، 11. كل مرة نزيد 3، فالصيغة \(a_n = 3n - 1\). وكل حد يحتاج حد واحد قبله، فالاستقراء العادي يكفي.') +
    W([('1', 'الأساس', r'Since \(a_1 = 2 = 3 \cdot 1 - 1\), the formula holds for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(a_k = 3k - 1\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(a_{k+1} = 3(k+1) - 1 = 3k + 2\).', ''),
       ('4', 'الخطوة', r'Since \(k + 1 \ge 2\), \(a_{k+1} = \hyp{a_k} + 3 = \hyp{(3k - 1)} + 3 = 3k + 2\).', '', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(a_n = 3n - 1\) for every \(n \in \mathbb{N}\).', '')], title='نكتب') +
    twins([('q-633', '6.33.', EX['6.33'], 's-633'), ('q-636', '6.36.', EX['6.36'], 's-636')], lab='تمارين الخطة: حلها على ورقتك، وبعدها اضغط «الحل»')))

# ---------- p-ex8: example 8 ----------
P.append(page('p-ex8', U[5], 'low', 'قوي بدون متتابعة: مثال 8' + tag('sol', 'مثال 8 في السلايدات'),
    qbox(r'<span class="lb">Result.</span> For each integer \(n \ge 8\), there are nonnegative integers \(a\) and \(b\) such that \(n = 3a + 5b\).',
         'كل عدد من 8 وفوق ينكتب \\(3a + 5b\\). (هو نفسه تمرين 5.51 في الفصل 5، بس هنا بالاستقراء القوي.)', lab='مثال 8 في السلايدات') +
    idea(r'\(k + 1 = (k - 2) + 3\). العدد \(k - 2\) أصغر من \(k + 1\)، فالفرض القوي يقول إنه ينكتب \(3a + 5b\)، ونزيد عليه 3. بس لازم \(k - 2 \ge 8\)، فـ 9 و 10 نسويهم لحالهم.') +
    W([('1', 'الأساس', r'We proceed by induction. Since \(8 = 3 \cdot 1 + 5 \cdot 1\), the statement is true for \(n = 8\).', ''),
       ('2', 'الفرض', r'Assume for each integer \(i\) with \(8 \le i \le k\), where \(k \ge 8\) is an arbitrary integer, that there are nonnegative integers \(s\) and \(t\) such that \(i = 3s + 5t\).', 'الفرض القوي يبدأ من 8.'),
       ('3', 'المطلوب', r'Consider the integer \(k + 1\). We show that there are nonnegative integers \(x\) and \(y\) such that \(k + 1 = 3x + 5y\).', ''),
       ('★', '9 و 10', r'Since \(9 = 3 \cdot 3 + 5 \cdot 0\) and \(10 = 3 \cdot 0 + 5 \cdot 2\), this is true if \(k + 1 = 9\) and \(k + 1 = 10\). Hence, we may assume that \(k + 1 \ge 11\). Thus, \(8 \le (k+1) - 3 \lt k\).', '', ST),
       ('4', 'الخطوة', r'By the induction hypothesis, there are nonnegative integers \(a\) and \(b\) such that \(\hyp{(k+1) - 3 = 3a + 5b}\) and so \(k + 1 = 3(a+1) + 5b\). Letting \(x = a + 1\) and \(y = b\), we have the desired conclusion.', '', HL),
       ('5', 'الختام', r'By the Strong Principle of Mathematical Induction, for every integer \(n \ge 8\), there are nonnegative integers \(a\) and \(b\) such that \(n = 3a + 5b\).', '')], title='نكتب (حل السلايدات)')))

# ---------- p-623: the book's result 6.23 (strong, no sequence) ----------
P.append(page('p-623', U[5], 'low', 'قوي بدون متتابعة: مثال الكتاب 6.23' + tag('sol', 'مثال الكتاب 6.23'),
    qbox(r'<span class="lb">Result 6.23.</span> If \(r\) is a nonzero real number such that \(r + \frac{1}{r}\) is an integer, then \(r^n + \frac{1}{r^n}\) is an integer for every positive integer \(n\).',
         r'لو \(r + \frac{1}{r}\) عدد صحيح، فكل \(r^n + \frac{1}{r^n}\) عدد صحيح. مثلاً \(r = \frac{3 + \sqrt{5}}{2}\) يعطي \(r + \frac{1}{r} = 3\).', lab='مثال من الكتاب في 6.3 (ما انسأل للحين)') +
    idea(r'<b>التريك:</b> \(\left(r^k + \frac{1}{r^k}\right)\left(r + \frac{1}{r}\right) = \left(r^{k+1} + \frac{1}{r^{k+1}}\right) + \left(r^{k-1} + \frac{1}{r^{k-1}}\right)\). يعني الحد الجديد يطلع من الحد k والحد k − 1 مع بعض، فنحتاج الاستقراء القوي.') +
    W([('1', 'الأساس', r'We use the Strong Principle of Mathematical Induction. Since \(r + \frac{1}{r} = r^1 + \frac{1}{r^1}\) is an integer, the statement is true for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume for an arbitrary integer \(k \ge 1\) that \(m_i = r^i + \frac{1}{r^i}\) is an integer for every integer \(i\) with \(1 \le i \le k\).', ''),
       ('3', 'المطلوب', r'We show that \(r^{k+1} + \frac{1}{r^{k+1}}\) is an integer.', ''),
       ('★', 'k = 1', r'If \(k = 1\), then \(r^{k+1} + \frac{1}{r^{k+1}} = r^2 + \frac{1}{r^2} = \left(r + \frac{1}{r}\right)^2 - 2\) is an integer. So we may assume that \(k \ge 2\).', r'الخطوة تحتاج \(m_{k-1}\)، ولما k = 1 يصير \(m_0\) وهو برا الفرض.', ST),
       ('4', 'الخطوة', r'Observe that \[r^{k+1} + \frac{1}{r^{k+1}} = \hyp{\left(r^k + \frac{1}{r^k}\right)}\left(r + \frac{1}{r}\right) - \hyp{\left(r^{k-1} + \frac{1}{r^{k-1}}\right)} = m_k m_1 - m_{k-1},\] which is an integer by the inductive hypothesis.', '', HL),
       ('5', 'الختام', r'By the Strong Principle of Mathematical Induction, \(r^n + \frac{1}{r^n}\) is an integer for every positive integer \(n\).', '')], title='نكتب (حل الكتاب، ومعه سطر ★)') +
    twins([('q-xy', 'توأم.', r'Let \(x\) and \(y\) be real numbers such that \(x + y\) and \(xy\) are integers. Prove that \(x^n + y^n\) is an integer for every positive integer \(n\).', 's-xy')])))

# ---------- p-minc: proof by minimum counterexample (slides; book section 6.4, outside the plan) ----------
P.append(page('p-minc', U[5] + ' · 6.4', 'extra', 'برهان أصغر مثال مضاد: مثال 9' + tag('sol', 'مثال 9 في السلايدات'),
    qbox(r'<span class="lb">Result.</span> For every positive integer \(n\), \(6 \mid (n^3 - n)\).',
         'من القسم 6.4: برا خطة المقرر، بس موجود في السلايدات. اقرأه بعد ما تخلص الباقي.', lab='مثال 9 في السلايدات') +
    idea(r'نفرض العكس، وأصغر عدد تكون الجملة غلط عنده نسميه m (الترتيب الحسن يضمن وجوده)، واسمه <i>minimum counterexample</i>. كل عدد أصغر من m الجملة صحيحة عنده، وهذا يلعب دور الفرض. نثبتها عند m بعد، فيطلع تناقض.') +
    W([('1', 'نعكس', r'Assume, to the contrary, that there are positive integers \(n\) such that \(6 \nmid (n^3 - n)\). Then there is a smallest positive integer \(n\) such that \(6 \nmid (n^3 - n)\). Let \(m\) be this integer.', ''),
       ('2', 'الصغار', r'If \(n = 1\), then \(n^3 - n = 0\); while if \(n = 2\), then \(n^3 - n = 6\). Since \(6 \mid 0\) and \(6 \mid 6\), it follows that \(6 \mid (n^3 - n)\) for \(n = 1\) and \(n = 2\). Therefore \(m \ge 3\). So, we can write \(m = k + 2\), where \(1 \le k \lt m\).', ''),
       ('3', 'الحساب', r'Observe that \[\begin{aligned} m^3 - m &= (k+2)^3 - (k+2) = (k^3 + 6k^2 + 12k + 8) - (k + 2) \\ &= (k^3 - k) + (6k^2 + 12k + 6). \end{aligned}\] Since \(k \lt m\), it follows that \(6 \mid (k^3 - k)\). Hence, \(\hyp{k^3 - k = 6x}\) for some integer \(x\). So, we have \(m^3 - m = 6x + 6(k^2 + 2k + 1) = 6(x + k^2 + 2k + 1)\).', r'ليش k + 2؟ عشان يطلع \(k^3 - k\) (صحيح لأن k أصغر من m)، والباقي مضاعف 6 على طول.', HL),
       ('4', 'التناقض', r'Since \(x + k^2 + 2k + 1\) is an integer, \(6 \mid (m^3 - m)\), which produces a contradiction.', '')], title='نكتب (حل السلايدات)') +
    note('trap', 'انتبه:', 'لو السؤال قال «by minimum counterexample» لازم هالطريقة، مو الاستقراء.') +
    twins([('q-mc10', 'مثال 10 في السلايدات.', r'Use a proof by minimum counterexample to prove that \(3 \mid (2^{2n} - 1)\) for every nonnegative integer \(n\).', 's-mc10')])))

# ---------- p-s5a / p-s5b: solutions of unit 5 ----------
P.append(page('p-s5a', 'حلول الوحدة 5', '', 'الحلول' + tag('sol', 'شيّك'),
    sh('توأم المتتابعة', 's-t5', [('q-t5', 'السؤال')]) +
    W([('أولاً', '', r'\(a_3 = a_2 + 2a_1 = 4 + 4 = 8\) and \(a_4 = a_3 + 2a_2 = 8 + 8 = 16\).', ''),
       ('1', 'الأساس', r'Since \(a_1 = 2 = 2^1\), the formula holds for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume for an arbitrary positive integer \(k\) that \(a_i = 2^i\) for every integer \(i\) with \(1 \le i \le k\).', ''),
       ('3', 'المطلوب', r'We show that \(a_{k+1} = 2^{k+1}\).', ''),
       ('★', 'k = 1', r'If \(k = 1\), then \(a_{k+1} = a_2 = 4 = 2^2\). So we may assume that \(k \ge 2\).', '', ST),
       ('4', 'الخطوة', r'Since \(k + 1 \ge 3\), by the inductive hypothesis \(a_{k+1} = \hyp{a_k} + 2\hyp{a_{k-1}} = \hyp{2^k} + 2 \cdot \hyp{2^{k-1}} = 2^k + 2^k = 2^{k+1}\).', '', HL),
       ('5', 'الختام', r'By the Strong Principle of Mathematical Induction, \(a_n = 2^n\) for all \(n \in \mathbb{N}\).', '')], title='') +
    sh('تمرين 6.33', 's-633', SM('633')['back']) +
    W([('تخمين', '', r'\(a_2 = 2\), \(a_3 = 4\), \(a_4 = 8\), \(a_5 = 16\). Conjecture: \(a_n = 2^{n-1}\).', 'كل حد ضعف اللي قبله.'),
       ('1', 'الأساس', r'Since \(a_1 = 1 = 2^0\), the formula holds for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(a_k = 2^{k-1}\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(a_{k+1} = 2^k\).', ''),
       ('4', 'الخطوة', r'Since \(k + 1 \ge 2\), \(a_{k+1} = 2\hyp{a_k} = 2 \cdot \hyp{2^{k-1}} = 2^k\).', '', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(a_n = 2^{n-1}\) for every \(n \in \mathbb{N}\).', '')], title=''), sol=True))

P.append(page('p-s5b', 'حلول الوحدة 5', '', 'حل تمرين 6.36' + tag('sol', 'شيّك'),
    sh('تمرين 6.36', 's-636', SM('636')['back']) +
    W([('(a)', '', r'\(F_1 = F_2 = 1\) and \(F_n = F_{n-1} + F_{n-2}\) for every integer \(n \ge 3\).', 'كل حد = مجموع الحدّين اللي قبله.'),
       ('(b)', '', r'For each \(n \in \mathbb{N}\), let \(P(n)\): \(F_n\) is even if and only if \(3 \mid n\). We use the Strong Principle of Mathematical Induction.', ''),
       ('1', 'الأساس', r'\(F_1 = 1\) is odd and \(3 \nmid 1\), so \(P(1)\) is true.', ''),
       ('2', 'الفرض', r'Assume for an arbitrary positive integer \(k\) that \(P(i)\) is true for every integer \(i\) with \(1 \le i \le k\).', ''),
       ('3', 'المطلوب', r'We show that \(P(k+1)\) is true, that is, \(F_{k+1}\) is even if and only if \(3 \mid (k+1)\).', ''),
       ('★', 'k = 1', r'If \(k = 1\), then \(F_{k+1} = F_2 = 1\) is odd and \(3 \nmid 2\), so \(P(2)\) is true. So we may assume that \(k \ge 2\).', '', ST),
       ('4', 'الخطوة', r'Since \(k + 1 \ge 3\), \(F_{k+1} = F_k + F_{k-1}\). Exactly one of \(k-1\), \(k\), \(k+1\) is divisible by 3. <i>Case 1.</i> \(3 \mid (k+1)\). Then \(3 \nmid k\) and \(3 \nmid (k-1)\), so \(\hyp{F_k}\) and \(\hyp{F_{k-1}}\) are odd by the hypothesis. Hence \(F_{k+1}\) is even. <i>Case 2.</i> \(3 \nmid (k+1)\). Then exactly one of \(k\) and \(k-1\) is divisible by 3, so exactly one of \(\hyp{F_k}\) and \(\hyp{F_{k-1}}\) is even. Hence \(F_{k+1}\) is odd. Therefore \(F_{k+1}\) is even if and only if \(3 \mid (k+1)\).',
        'فردي + فردي = زوجي، وزوجي + فردي = فردي.', HL),
       ('5', 'الختام', r'By the Strong Principle of Mathematical Induction, \(2 \mid F_n\) if and only if \(3 \mid n\), for every \(n \in \mathbb{N}\).', '')], title=''), sol=True))

P.append(page('p-s5c', 'حلول الوحدة 5', '', 'حل توأم 6.23، ومثال 10' + tag('sol', 'شيّك'),
    sh('توأم مثال الكتاب 6.23', 's-xy', [('q-xy', 'السؤال')]) +
    W([('1', 'الأساس', r'Since \(x^1 + y^1 = x + y\) is an integer, the statement is true for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume for an arbitrary positive integer \(k\) that \(x^i + y^i\) is an integer for every integer \(i\) with \(1 \le i \le k\).', ''),
       ('3', 'المطلوب', r'We show that \(x^{k+1} + y^{k+1}\) is an integer.', ''),
       ('★', 'k = 1', r'If \(k = 1\), then \(x^2 + y^2 = (x + y)^2 - 2xy\) is an integer. So we may assume that \(k \ge 2\).', '', ST),
       ('4', 'الخطوة', r'Observe that \(x^{k+1} + y^{k+1} = \hyp{(x^k + y^k)}(x + y) - xy\hyp{(x^{k-1} + y^{k-1})}\). Since \(x + y\) and \(xy\) are integers, this is an integer by the inductive hypothesis.', 'ومثال 6.23 حالة خاصة منه: y = 1/r، فـ xy = 1.', HL),
       ('5', 'الختام', r'By the Strong Principle of Mathematical Induction, \(x^n + y^n\) is an integer for every positive integer \(n\).', '')], title='') +
    sh('مثال 10 في السلايدات', 's-mc10', [('q-mc10', 'السؤال')]) +
    W([('1', 'نعكس', r'Assume, to the contrary, that there are nonnegative integers \(n\) for which \(3 \nmid (2^{2n} - 1)\). By a theorem in this chapter, there is a smallest nonnegative integer \(n\) such that \(3 \nmid (2^{2n} - 1)\). Denote this integer by \(m\). Thus \(3 \nmid (2^{2m} - 1)\) and \(3 \mid (2^{2n} - 1)\) for all nonnegative integers \(n\) for which \(0 \le n \lt m\).', r'النظرية: \(\{i \in \mathbb{Z} : i \ge 0\}\) مرتبة ترتيب حسن.'),
       ('2', 'الصغار', r'Since \(3 \mid (2^{2n} - 1)\) when \(n = 0\), it follows that \(m \ge 1\). Hence, \(m\) can be expressed by \(m = k + 1\), where \(0 \le k \lt m\).', r'\(2^0 - 1 = 0\)، و 3 تقسم 0.'),
       ('3', 'الحساب', r'Thus, \(3 \mid (2^{2k} - 1)\), which implies that \(\hyp{2^{2k} - 1 = 3x}\) for some integer \(x\). Consequently, \(2^{2k} = 3x + 1\). Observe that \[\begin{aligned} 2^{2m} - 1 &= 2^{2(k+1)} - 1 = 2^{2k+2} - 1 = 2^2 \cdot 2^{2k} - 1 \\ &= 4(3x + 1) - 1 = 12x + 3 = 3(4x + 1). \end{aligned}\]', 'k أصغر من m، فالجملة صحيحة عند k (الأزرق).', HL),
       ('4', 'التناقض', r'Since \(4x + 1\) is an integer, \(3 \mid (2^{2m} - 1)\), which produces a contradiction.', '')], title=''), sol=True))

save('f_u5.html', P)
