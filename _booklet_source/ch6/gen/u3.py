import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []
U3 = U[3] + ' · 6.2'

# ---------- p-ex5: divisibility, example 5 ----------
P.append(page('p-ex5', U3, 'cand', 'القسمة: مثال 5' + tag('sol', 'مثال 5 في السلايدات'),
    qbox(r'<span class="lb">Result.</span> For every nonnegative integer \(n\), \(9 \mid (4^{3n} - 1)\).',
         '9 يقسم \\(4^{3n} - 1\\) لكل n من 0 وفوق. كلمة nonnegative تعني إن البداية من 0.', lab='مثال 5 في السلايدات (ما انسأل للحين)') +
    idea(r'بالأرقام: n = 1: 63 = 9 × 7 ' + OK + r'. <b>حركة القسمة:</b> الفرض معادلة (\(4^{3k} = 9x + 1\))، وحد k + 1 من حد k (\(4^{3k+3} = 4^3 \cdot 4^{3k}\))، وعوّض، وطلّع 9 عامل مشترك.') +
    W([('1', 'الأساس', r'We proceed by induction. When \(n = 0\), \(4^{3n} - 1 = 0\). Since \(9 \mid 0\), the statement is true when \(n = 0\).', 'البداية من 0، و 0 = 9 × 0.'),
       ('2', 'الفرض', r'Assume that \(9 \mid (4^{3k} - 1)\), where \(k\) is a nonnegative integer.', ''),
       ('3', 'المطلوب', r'We now show that \(9 \mid (4^{3k+3} - 1)\).', r'عوّضنا n = k + 1: \(4^{3(k+1)} = 4^{3k+3}\).'),
       ('4', 'الخطوة', r'Since \(9 \mid (4^{3k} - 1)\), it follows that \(4^{3k} - 1 = 9x\) for some integer \(x\). Hence, \(4^{3k} = 9x + 1\). Now, observe that \[\begin{aligned} 4^{3k+3} - 1 &= 4^3 \cdot \hyp{4^{3k}} - 1 = 64\hyp{(9x + 1)} - 1 \\ &= 64 \cdot 9x + 64 - 1 = 64 \cdot 9x + 63 = 9(64x + 7). \end{aligned}\] Since \(64x + 7\) is an integer, \(9 \mid (4^{3k+3} - 1)\).',
        r'عوّضنا \(4^{3k}\) نفسه (الأزرق)، مو العبارة كلها. و 63 = 9 × 7، فطلع 9 عامل مشترك.', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(9 \mid (4^{3n} - 1)\) for every nonnegative integer \(n\).', 'اسم المبدأ كامل.')], title='نكتب (برهان السلايدات)') +
    twins([('q-611b', 'Result 6.11.', r'For every nonnegative integer \(n\), \(3 \mid (2^{2n} - 1)\).', 's-611b'),
           ('q-616', '6.16.', EX['6.16'], 's-616'),
           ('q-t4', 'توأم.', r'For every positive integer \(n\), \(5 \mid (6^n - 1)\).', 's-t4')],
          lab='تمارين توأم: حلها على ورقتك (الأول مثال من الكتاب)')))

# ---------- p-s3: solutions of unit 3 ----------
P.append(page('p-s3', 'حلول الوحدة 3', '', 'الحلول' + tag('sol', 'شيّك'),
    sh('مثال الكتاب 6.11', 's-611b', [('q-611b', 'السؤال')]) +
    W([('', 'حل الكتاب', r'We proceed by induction. The result is true when \(n = 0\) since in this case \(2^{2n} - 1 = 0\) and \(3 \mid 0\). Assume that \(3 \mid (2^{2k} - 1)\), where \(k\) is a nonnegative integer. We show that \(3 \mid (2^{2k+2} - 1)\). Since \(3 \mid (2^{2k} - 1)\), there exists an integer \(x\) such that \(2^{2k} - 1 = 3x\) and so \(2^{2k} = 3x + 1\). Now, \[2^{2k+2} - 1 = 4 \cdot \hyp{2^{2k}} - 1 = 4\hyp{(3x + 1)} - 1 = 12x + 3 = 3(4x + 1).\] Since \(4x + 1\) is an integer, \(3 \mid (2^{2k+2} - 1)\). By the Principle of Mathematical Induction, \(3 \mid (2^{2n} - 1)\) for every nonnegative integer \(n\).',
        r'نفس حركة مثال 5 بالضبط: \(2^{2k+2} = 4 \cdot 2^{2k}\).')], title='') +
    sh('تمرين 6.16', 's-616', SM('616')['back']) +
    W([('1', 'الأساس', r'When \(n = 1\), \(3^{4n+1} - 5^{2n-1} = 3^5 - 5 = 238 = 7 \cdot 34\), so \(7 \mid 238\).', ''),
       ('2', 'الفرض', r'Assume that \(7 \mid (3^{4k+1} - 5^{2k-1})\) for a positive integer \(k\). Then \(3^{4k+1} - 5^{2k-1} = 7x\) for some integer \(x\), so \(3^{4k+1} = 7x + 5^{2k-1}\).', 'نكتب الفرض معادلة، ونعزل الحد اللي فيه 3.'),
       ('3', 'المطلوب', r'We show that \(7 \mid (3^{4k+5} - 5^{2k+1})\).', ''),
       ('4', 'الخطوة', r'\[\begin{aligned} 3^{4k+5} - 5^{2k+1} &= 81 \cdot \hyp{3^{4k+1}} - 25 \cdot 5^{2k-1} = 81\hyp{\left(7x + 5^{2k-1}\right)} - 25 \cdot 5^{2k-1} \\ &= 567x + 56 \cdot 5^{2k-1} = 7\left(81x + 8 \cdot 5^{2k-1}\right). \end{aligned}\] Since \(81x + 8 \cdot 5^{2k-1}\) is an integer, \(7 \mid (3^{4k+5} - 5^{2k+1})\).', r'\(3^{4k+5} = 3^4 \cdot 3^{4k+1}\) و \(5^{2k+1} = 5^2 \cdot 5^{2k-1}\). و 567 = 7 × 81، و 56 = 7 × 8.', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(7 \mid (3^{4n+1} - 5^{2n-1})\) for every positive integer \(n\).', '')], title='') +
    sh('توأم: 5 يقسم \\(6^n - 1\\)', 's-t4', [('q-t4', 'السؤال')]) +
    W([('', 'الحل', r'When \(n = 1\), \(6^1 - 1 = 5\) and \(5 \mid 5\). Assume that \(5 \mid (6^k - 1)\) for a positive integer \(k\). Then \(6^k - 1 = 5x\) for some integer \(x\), so \(6^k = 5x + 1\). We show that \(5 \mid (6^{k+1} - 1)\). Now, \(6^{k+1} - 1 = 6 \cdot \hyp{6^k} - 1 = 6\hyp{(5x + 1)} - 1 = 30x + 5 = 5(6x + 1)\). Since \(6x + 1\) is an integer, \(5 \mid (6^{k+1} - 1)\). By the Principle of Mathematical Induction, \(5 \mid (6^n - 1)\) for every positive integer \(n\).', '')], title=''), sol=True))

save('d_u3.html', P)
