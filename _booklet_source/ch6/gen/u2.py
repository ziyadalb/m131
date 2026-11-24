import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []
U2 = U[2] + ' · 6.1'
CONC = 'اسم المبدأ كامل.'

# ---------- p-ex1: example 1 = the girls' exam question ----------
P.append(page('p-ex1', U2, 'top', 'أول مجموع: مثال 1' + tag('past', 'البنات · 3 درجات'),
    qbox(r'<span class="lb">4-</span> For each positive integer \(n\), \(1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}\). (3 marks)',
         'مجموع الأعداد من 1 إلى n يساوي n(n + 1)/2.', lab='سؤال ميد البنات · ومثال 1 في السلايدات') +
    idea(r'بالأرقام: n = 3: 1 + 2 + 3 = 6، و \(\frac{3 \cdot 4}{2} = 6\) ' + OK + r'. <b>حركة الخطوة في المجاميع:</b> مجموع k + 1 = (مجموع k) + آخر حد. مجموع k تبدّله بالفرض، وبعدها تبسّط لين يطلع المطلوب.') +
    W([('1', 'الأساس', r'We employ induction. Let \(P(n): 1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}\). Since \(1 = \frac{1 \cdot 2}{2}\), the statement \(P(1)\) is true.', 'سمّينا الجملة P(n) زي السلايدات، وعوّضنا n = 1: الطرفين 1.', dict(BKP, id='m-ex1')),
       ('2', 'الفرض', r'Assume that \(P(k)\) is true for an arbitrary positive integer \(k\), that is, assume that \(1 + 2 + 3 + \cdots + k = \frac{k(k+1)}{2}\).', 'نفس الجملة، بس k بدل n.'),
       ('3', 'المطلوب', r'We show that \(P(k+1)\) is true, that is, we show that \(1 + 2 + 3 + \cdots + (k+1) = \frac{(k+1)(k+2)}{2}\).', 'نفس الجملة بـ k + 1. هذا الهدف.'),
       ('4', 'الخطوة', r'Thus, \[\begin{aligned} 1 + 2 + 3 + \cdots + (k+1) &= \hyp{(1 + 2 + 3 + \cdots + k)} + (k+1) = \hyp{\frac{k(k+1)}{2}} + (k+1) \\ &= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}, \end{aligned}\] as desired.',
        'فصلنا آخر حد (k + 1). الباقي بالأزرق هو مجموع k، فبدّلناه بالفرض. بعدها مقام مشترك، و (k + 1) عامل مشترك.', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(P(n)\) is true for every positive integer \(n\).', CONC)], title='نكتب (برهان السلايدات)') +
    note('trap', 'انتبه:', 'لا تكتب المطلوب كأنه صحيح وتشتغل على طرفيه. ابدأ من طرف واحد (المجموع)، وامشِ لين توصل للطرف الثاني.')))

# ---------- p-nov4: the November question (exercise 6.4) ----------
P.append(page('p-nov4', U[2], 'top', 'مجموع الفرديات: سؤال نوفمبر' + tag('past', 'نوفمبر · 4 درجات'),
    qbox(r'<span class="lb">4.</span> For every positive integer \(n\), \(1 + 3 + 5 + \cdots + (2n - 1) = n^2\).',
         'مجموع أول n أعداد فردية يساوي n². وهو تمرين 6.4 في الخطة، وجا بعد في نهائي 1446.', lab='سؤال ميد نوفمبر') +
    idea(r'بالأرقام: 1 + 3 + 5 = 9 = 3² ' + OK + r'. نفس حركة مثال 1. الفرق الوحيد: آخر حد عند k + 1 هو \(2(k+1) - 1 = 2k + 1\).') +
    W([('1', 'الأساس', r'Since \(1 = 1^2\), the statement is true for \(n = 1\).', 'عوّضنا n = 1.', dict(BKP, id='m-nov4')),
       ('2', 'الفرض', r'Assume that \(1 + 3 + 5 + \cdots + (2k-1) = k^2\) for an arbitrary positive integer \(k\).', 'نفس الجملة بـ k.'),
       ('3', 'المطلوب', r'We show that \(1 + 3 + 5 + \cdots + (2k+1) = (k+1)^2\).', 'آخر حد صار 2k + 1، والأيمن (k + 1)².'),
       ('4', 'الخطوة', r'Thus, \(1 + 3 + \cdots + (2k+1) = \hyp{[1 + 3 + \cdots + (2k-1)]} + (2k+1) = \hyp{k^2} + 2k + 1 = (k+1)^2\), as desired.',
        'فصلنا آخر حد، وبدّلنا الأزرق بـ k² من الفرض. و k² + 2k + 1 مربع كامل.', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(1 + 3 + 5 + \cdots + (2n-1) = n^2\) for every positive integer \(n\).', CONC)], title='نكتب') +
    note('trap', 'انتبه:', r'آخر حد في المطلوب: عوّض n = k + 1 في (2n − 1)، يطلع 2k + 1. لا تكتبه (2k − 1) + 1.') +
    twins([('q-65', '6.5.', EX['6.5'], 's-65')])))

# ---------- p-ex2: example 2 (sum of fractions) ----------
P.append(page('p-ex2', U[2], 'cand', 'مجموع كسور: مثال 2' + tag('sol', 'مثال 2 في السلايدات'),
    qbox(r'<span class="lb">Result.</span> For every positive integer \(n\), \(\frac{1}{2\cdot 3} + \frac{1}{3\cdot 4} + \cdots + \frac{1}{(n+1)(n+2)} = \frac{n}{2n+4}\).',
         'مجموع كسور. نفس القالب، بس الخطوة فيها مقام مشترك.', lab='مثال 2 في السلايدات (ما انسأل للحين)') +
    idea(r'بالأرقام: n = 2: \(\frac{1}{6} + \frac{1}{12} = \frac{1}{4}\)، و \(\frac{2}{8} = \frac{1}{4}\) ' + OK + r'. <b>تريك:</b> لا تفك المقامات. المطلوب \(\frac{k+1}{2(k+3)}\) يقول لك إن \((k + 2)\) لازم ينحذف، فخلّه عامل مشترك.') +
    W([('1', 'الأساس', r'We use induction. Since \(\frac{1}{2\cdot 3} = \frac{1}{2\cdot 1 + 4} = \frac{1}{6}\), the formula holds for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(\frac{1}{2\cdot 3} + \frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+1)(k+2)} = \frac{k}{2k+4}\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(\frac{1}{2\cdot 3} + \frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+2)(k+3)} = \frac{k+1}{2(k+1)+4} = \frac{k+1}{2k+6}\).', r'آخر حد صار \(\frac{1}{(k+2)(k+3)}\).'),
       ('4', 'الخطوة', r'Observe that \[\begin{aligned} \frac{1}{2\cdot 3} + \cdots + \frac{1}{(k+2)(k+3)} &= \hyp{\left[\frac{1}{2\cdot 3} + \cdots + \frac{1}{(k+1)(k+2)}\right]} + \frac{1}{(k+2)(k+3)} \\ &= \hyp{\frac{k}{2k+4}} + \frac{1}{(k+2)(k+3)} \\ &= \frac{k}{2(k+2)} + \frac{1}{(k+2)(k+3)} \\ &= \frac{k(k+3) + 2}{2(k+2)(k+3)} = \frac{k^2 + 3k + 2}{2(k+2)(k+3)} \\ &= \frac{(k+1)(k+2)}{2(k+2)(k+3)} = \frac{k+1}{2(k+3)} = \frac{k+1}{2k+6}, \end{aligned}\] giving us the desired result.',
        r'بدّلنا الأزرق بالفرض، ووحّدنا المقام \(2(k+2)(k+3)\)، وحلّلنا \(k^2 + 3k + 2\)، فانحذف \((k + 2)\).', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(\frac{1}{2\cdot 3} + \cdots + \frac{1}{(n+1)(n+2)} = \frac{n}{2n+4}\) for every positive integer \(n\).', '')], title='نكتب (برهان السلايدات)') +
    twins([('q-611', '6.11.', EX['6.11'], 's-611')]), style='gap:3mm'))

# ---------- p-sums: twin sums to practise ----------
P.append(page('p-sums', U[2], 'top', 'تدريب: مجاميع توأم' + tag('ex', 'حلها على ورقتك'),
    idea('كلها بنفس حركة مثال 1: افصل آخر حد، وبدّل الباقي بالفرض، وبسّط لين يطلع المطلوب. حل كل سؤال على ورقتك، وبعدها اضغط «الحل».') +
    twins([('q-t1', '1.', r'For every positive integer \(n\), \(2 + 4 + 6 + \cdots + 2n = n(n+1)\).', 's-t1'),
           ('q-t2', '2.', r'For every positive integer \(n\), \(1^2 + 2^2 + 3^2 + \cdots + n^2 = \frac{n(n+1)(2n+1)}{6}\).', 's-t2'),
           ('q-t3', '3.', r'For every positive integer \(n\), \(1 \cdot 2 + 2 \cdot 3 + \cdots + n(n+1) = \frac{n(n+1)(n+2)}{3}\).', 's-t3'),
           ('q-64', '6.4.', EX['6.4'], 's-64')],
          lab='تمارين توأم') +
    twins([('q-613', 'Result 6.13.', r'For every positive integer \(n\), \(1 \cdot 3 \cdot 5 \cdots (2n-1) = \frac{(2n)!}{2^n \cdot n!}\).', 's-613')],
          lab='مثال الكتاب 6.13: ضرب بدل جمع (احتمال أقل)') +
    note('trick', 'تريك قبل ما تبدأ:', 'عوّض n = 1 و n = 2 في الصيغة. لو طلعت صح، تأكدت إنك نسخت السؤال صح، وعرفت شكل آخر حد.')))

# ---------- p-s2a / p-s2b: solutions of unit 2 ----------
P.append(page('p-s2a', 'حلول الوحدة 2', '', 'الحلول' + tag('sol', 'شيّك'),
    sh('تمرين 6.5', 's-65', SM('65')['back']) +
    W([('1', 'الأساس', r'Since \(1 = 2 \cdot 1^2 - 1\), the statement is true for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(1 + 5 + 9 + \cdots + (4k-3) = 2k^2 - k\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(1 + 5 + 9 + \cdots + (4k+1) = 2(k+1)^2 - (k+1)\).', 'آخر حد: 4(k + 1) − 3 = 4k + 1.'),
       ('4', 'الخطوة', r'By the inductive hypothesis, \(1 + 5 + \cdots + (4k+1) = \hyp{(2k^2 - k)} + (4k + 1) = 2k^2 + 3k + 1 = 2(k+1)^2 - (k+1)\).', 'فك المطلوب في المسودة: 2k² + 4k + 2 − k − 1 = 2k² + 3k + 1.', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(1 + 5 + 9 + \cdots + (4n-3) = 2n^2 - n\) for every positive integer \(n\).', '')], title='') +
    sh('تمرين 6.11', 's-611', SM('611')['back']) +
    W([('1', 'الأساس', r'Since \(\frac{1}{3\cdot 4} = \frac{1}{12} = \frac{1}{3\cdot 1 + 9}\), the formula holds for \(n = 1\).', ''),
       ('2', 'الفرض', r'Assume that \(\frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+2)(k+3)} = \frac{k}{3k+9}\) for a positive integer \(k\).', ''),
       ('3', 'المطلوب', r'We show that \(\frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+3)(k+4)} = \frac{k+1}{3k+12}\).', ''),
       ('4', 'الخطوة', r'By the inductive hypothesis, \[\begin{aligned} \frac{1}{3\cdot 4} + \cdots + \frac{1}{(k+3)(k+4)} &= \hyp{\frac{k}{3(k+3)}} + \frac{1}{(k+3)(k+4)} = \frac{k(k+4) + 3}{3(k+3)(k+4)} \\ &= \frac{(k+1)(k+3)}{3(k+3)(k+4)} = \frac{k+1}{3(k+4)} = \frac{k+1}{3k+12}. \end{aligned}\]', r'نفس مثال 2: \(k^2 + 4k + 3 = (k+1)(k+3)\)، فانحذف \((k + 3)\).', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).', '')], title=''), sol=True))

P.append(page('p-s2b', 'حلول الوحدة 2', '', 'حلول المجاميع التوأم' + tag('sol', 'شيّك'),
    sh('تمرين 6.4', 's-64', [('q-64', 'السؤال'), ('p-bank', 'البنك')]) +
    W([('(1)', '', r'By mathematical induction, exactly as in the November question.', 'نفس حل سؤال نوفمبر ' + ref('p-nov4') + '.'),
       ('(2)', '', r'Let \(S = 1 + 3 + \cdots + (2n-1)\). Writing the terms in reverse order, \(S = (2n-1) + (2n-3) + \cdots + 1\). Adding the two expressions term by term, each of the \(n\) pairs has sum \(2n\), so \(2S = n(2n) = 2n^2\). Hence \(S = n^2\).', 'نكتب المجموع مرتين، مرة بالعكس، ونجمع: كل زوج مجموعه 2n.')], title='') +
    sh('توأم 1', 's-t1', [('q-t1', 'السؤال')]) +
    W([('', 'الحل', r'Since \(2 = 1 \cdot 2\), the statement is true for \(n = 1\). Assume that \(2 + 4 + \cdots + 2k = k(k+1)\) for a positive integer \(k\). We show that \(2 + 4 + \cdots + 2(k+1) = (k+1)(k+2)\). By the inductive hypothesis, \(2 + 4 + \cdots + 2(k+1) = \hyp{k(k+1)} + 2(k+1) = (k+1)(k+2)\). By the Principle of Mathematical Induction, \(2 + 4 + \cdots + 2n = n(n+1)\) for every positive integer \(n\).', '')], title='') +
    sh('توأم 2', 's-t2', [('q-t2', 'السؤال')]) +
    W([('', 'الحل', r'Since \(1^2 = \frac{1 \cdot 2 \cdot 3}{6}\), the statement is true for \(n = 1\). Assume that \(1^2 + \cdots + k^2 = \frac{k(k+1)(2k+1)}{6}\) for a positive integer \(k\). We show that \(1^2 + \cdots + (k+1)^2 = \frac{(k+1)(k+2)(2k+3)}{6}\). By the inductive hypothesis, \[\begin{aligned} 1^2 + \cdots + (k+1)^2 &= \hyp{\frac{k(k+1)(2k+1)}{6}} + (k+1)^2 = \frac{(k+1)\left[k(2k+1) + 6(k+1)\right]}{6} \\ &= \frac{(k+1)(2k^2 + 7k + 6)}{6} = \frac{(k+1)(k+2)(2k+3)}{6}. \end{aligned}\] By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).',
        r'التريك: طلّع (k + 1) عامل مشترك قبل ما تفك، وبعدها \(2k^2 + 7k + 6 = (k+2)(2k+3)\).')], title='') +
    '', sol=True))

P.append(page('p-s2c', 'حلول الوحدة 2', '', 'حلول المجاميع التوأم (تكملة)' + tag('sol', 'شيّك'),
    sh('توأم 3', 's-t3', [('q-t3', 'السؤال')]) +
    W([('', 'الحل', r'Since \(1 \cdot 2 = 2 = \frac{1 \cdot 2 \cdot 3}{3}\), the formula holds for \(n = 1\). Assume that \(1 \cdot 2 + \cdots + k(k+1) = \frac{k(k+1)(k+2)}{3}\) for a positive integer \(k\). We show that \(1 \cdot 2 + \cdots + (k+1)(k+2) = \frac{(k+1)(k+2)(k+3)}{3}\). By the inductive hypothesis, \(1 \cdot 2 + \cdots + (k+1)(k+2) = \hyp{\frac{k(k+1)(k+2)}{3}} + (k+1)(k+2) = (k+1)(k+2)\left(\frac{k}{3} + 1\right) = \frac{(k+1)(k+2)(k+3)}{3}\). By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).', '')], title='') +
    sh('مثال الكتاب 6.13', 's-613', [('q-613', 'السؤال')]) +
    W([('', 'حل الكتاب', r'We proceed by induction. Since \(1 = \frac{(2 \cdot 1)!}{2^1 \cdot 1!} = \frac{2}{2}\), the statement is true for \(n = 1\). Assume, for a positive integer \(k\), that \(1 \cdot 3 \cdot 5 \cdots (2k-1) = \frac{(2k)!}{2^k \cdot k!}\). We show that \(1 \cdot 3 \cdot 5 \cdots (2k+1) = \frac{(2k+2)!}{2^{k+1} \cdot (k+1)!}\). Observe that \[\begin{aligned} \frac{(2k+2)!}{2^{k+1} \cdot (k+1)!} &= \frac{(2k+2)(2k+1)}{2 \cdot (k+1)} \cdot \hyp{\frac{(2k)!}{2^k \cdot (k)!}} = (2k+1)\hyp{[1 \cdot 3 \cdot 5 \cdots (2k-1)]} \\ &= 1 \cdot 3 \cdot 5 \cdots (2k+1). \end{aligned}\] By the Principle of Mathematical Induction, \(1 \cdot 3 \cdot 5 \cdots (2n-1) = \frac{(2n)!}{2^n \cdot n!}\) for every positive integer \(n\).',
        r'الكتاب بدأ من الطرف الأيمن حق k + 1، وفصل منه جزء الفرض (الأزرق). و \(\frac{2k+2}{2(k+1)} = 1\).')], title=''), sol=True))

save('c_u2.html', P)
