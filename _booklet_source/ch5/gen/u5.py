import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
P = []
U5 = U[5] + ' · 5.5'

# ---------- p-u5: idea + card + slides Example 14 ----------
P.append(page('p-u5', U5, 'must', 'نفي الوجود: الفكرة' + tag('sol', 'مثال السلايدات 14'),
    idea('جملة «يوجد…» ما تنقض بمثال. لازم تثبت أن الشي ما يتحقق لأي عنصر: «لكل x، الجملة خطأ».') +
    stmt([(r'Since \(\sim (\exists x \in S, R(x)) \equiv \forall x \in S, \sim R(x)\), it follows that the statement \(\exists x \in S, R(x)\) is false if \(R(x)\) is false for every \(x \in S\).',
           r'نفي «يوجد x بحيث \(R(x)\)» هو «لكل x، \(R(x)\) خطأ». فعشان تنفي جملة «يوجد»، تثبت أن \(R(x)\) خطأ لكل x في S.')]) +
    think('لا تخلط بين نوعين من ' + lt('Disprove'), before=tbl(['السؤال', 'تكتب'], [
        [(lt('Disprove: For every x, …'), 'class="s"'), ('مثال واحد يفشل (الوحدة 1)', 'class="s"')],
        [(lt('Disprove: There exists x such that …'), 'class="s"'), ('برهان لكل x: الجملة خطأ عند كل عنصر', 'class="s"')]])) +
    card('بطاقة الخطوات: نفي الوجود', [
        ('اقلب', 'اكتب المطلوب الجديد: العكس لكل x.'),
        ('خذ أي x', lt('Let x be …') + r'، وحوّله لمعادلة لو لزم (مثل \(n = 2k + 1\)).'),
        ('اثبت', 'بالحساب أو بالحالات، أن الجملة خطأ عنده.')]) +
    qbox(r'Disprove the statement: There is a real number \(x\) such that \(x^6 + 2x^4 + x^2 + 2 = 0\).',
         r'انفِ: يوجد عدد حقيقي x بحيث \(x^6 + 2x^4 + x^2 + 2 = 0\). <b>نفكر:</b> كل قوة زوجية لعدد حقيقي أكبر من أو تساوي صفر. فالعبارة أكبر من أو تساوي 2، وما توصل للصفر أبداً.', lab='مثال 14') +
    W([('1', 'خذ أي x', r'Let \(x \in \mathbb{R}\). Since \(x^6\), \(x^4\) and \(x^2\) are all even powers of the real number \(x\), it follows that \(x^6 \ge 0\), \(x^4 \ge 0\) and \(x^2 \ge 0\).',
        r'أي عدد حقيقي (مو قيم نجربها، لأن الأعداد ما تخلص)، وقواه الزوجية كلها \(\ge 0\).'),
       ('2', 'اثبت', r'Therefore, \(x^6 + 2x^4 + x^2 + 2 \ge 0 + 0 + 0 + 2 = 2\) and so \(x^6 + 2x^4 + x^2 + 2 \ne 0\). Hence, the equation \(x^6 + 2x^4 + x^2 + 2 = 0\) has no real number solution.',
        'العبارة أكبر من أو تساوي 2، فما تساوي صفر.')], title='نكتب (حل السلايدات)'),
    style='gap:2.9mm'))

# ---------- p-555: slides Example 13 + 5.55 ----------
P.append(page('p-555', U[5], 'must', 'مثال: نفي الوجود بالتعويض' + tag('sol', 'مثال السلايدات 13') + tag('ex', 'دورك'),
    qbox(r'Disprove the statement: There exists an odd integer \(n\) such that \(n^2 + 2n + 3\) is odd.',
         r'انفِ: يوجد عدد فردي n بحيث \(n^2 + 2n + 3\) فردي. <b>نفكر:</b> \(n = 1, 3, 5\) يعطون 6 و18 و38، كلها زوجية! فنثبت أنها زوجية لكل n فردي.', lab='مثال 13') +
    W([('1', 'اقلب', r'We show that if \(n\) is an odd integer, then \(n^2 + 2n + 3\) is even.', 'نقلب «يوجد… فردي» إلى «لكل… زوجي».'),
       ('2', 'خذ أي n', r'Let \(n\) be an odd integer. Then \(n = 2k + 1\) for some integer \(k\).', 'أي عدد فردي، مو عدد معين.'),
       ('3', 'اثبت', r'Thus, \[\begin{aligned} n^2 + 2n + 3 &= (2k + 1)^2 + 2(2k + 1) + 3 = 4k^2 + 4k + 1 + 4k + 2 + 3 \\ &= 4k^2 + 8k + 6 = 2(2k^2 + 4k + 3). \end{aligned}\] Since \(2k^2 + 4k + 3\) is an integer, \(n^2 + 2n + 3\) is even.',
        'نعوّض ونفك، ونطلّع 2 عامل مشترك.')], title='نكتب (حل السلايدات)') +
    duork('5.55', r'<span class="lb">5.55.</span> Disprove the statement: There exist odd integers \(a\) and \(b\) such that \(4 \mid (3a^2 + 7b^2)\).',
          r'انفِ: يوجد عددين فرديين a و b بحيث 4 يقسم \(3a^2 + 7b^2\). جرّب: \(a = b = 1\) يعطي 10، و \(a = 1, b = 3\) يعطي 66. وش الباقي لما تقسمهم على 4؟') +
    recall(r'بعد التعويض اكتب العبارة على شكل \(4m + 2\)، وكمّل بحركة مثال 7 في التناقض: لو 4 يقسمها، يطلع 4 يقسم 2.') +
    W([('1', 'اقلب', None, None, 'b1'), ('2', 'خذ أي a و b', None, None, 'b1'), ('3', 'اثبت', None, None, 'b3')], title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> \((2x + 1)^2 = 4x^2 + 4x + 1\)، والعبارة بعد الفك \(12x^2 + 12x + 28y^2 + 28y + 10\).']),
    style='gap:2.6mm'))

# ---------- p-ex15: slides Example 15 + 5.57 ----------
P.append(page('p-ex15', U[5], 'must', 'مثال: نفي الوجود بالحالات' + tag('sol', 'مثال السلايدات 15') + tag('ex', 'دورك'),
    qbox(r'Disprove the statement: There exists an integer \(n\) such that \(n^3 - n + 1\) is even.',
         r'انفِ: يوجد عدد صحيح n بحيث \(n^3 - n + 1\) زوجي. <b>نفكر:</b> \(n = 0, 1, 2, 3\) يعطون 1 و1 و7 و25، كلها فردية. وما فيه شرط على n، فنقسم: زوجي أو فردي.', lab='مثال 15') +
    W([('1', 'حالة 1', r'Let \(n \in \mathbb{Z}\). We consider two cases. <i>Case 1.</i> \(n\) is even. Then \(n = 2a\), where \(a \in \mathbb{Z}\). So \(n^3 - n + 1 = (2a)^3 - (2a) + 1 = 8a^3 - 2a + 1 = 2(4a^3 - a) + 1\). Since \(4a^3 - a\) is an integer, \(n^3 - n + 1\) is odd and so it is not even.',
        r'n زوجي: نعوّض ونكتبها \(2(\ldots) + 1\)، يعني فردية.'),
       ('2', 'حالة 2', r'<i>Case 2.</i> \(n\) is odd. Then \(n = 2b + 1\), where \(b \in \mathbb{Z}\). Hence, \[\begin{aligned} n^3 - n + 1 &= (2b + 1)^3 - (2b + 1) + 1 = 8b^3 + 12b^2 + 6b + 1 - 2b - 1 + 1 \\ &= 8b^3 + 12b^2 + 4b + 1 = 2(4b^3 + 6b^2 + 2b) + 1. \end{aligned}\] Since \(4b^3 + 6b^2 + 2b\) is an integer, \(n^3 - n + 1\) is odd and so it is not even.',
        r'n فردي: نفس الشي. و \((2b + 1)^3 = 8b^3 + 12b^2 + 6b + 1\).')], title='نكتب (حل السلايدات)') +
    duork('5.57', r'<span class="lb">5.57.</span> Disprove the statement: There is an integer \(n\) such that \(n^4 + n^3 + n^2 + n\) is odd.',
          r'انفِ: يوجد عدد صحيح n بحيث \(n^4 + n^3 + n^2 + n\) فردي. جرّب: \(n = 1\) يعطي 4، و \(n = 2\) يعطي 30. وش تلاحظ؟') +
    W([('1', 'حالة 1', None, None, 'b2'), ('2', 'حالة 2', None, None, 'b3')], title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> \((2k + 1)^4 = 16k^4 + 32k^3 + 24k^2 + 8k + 1\). وطريق أسرع للحالة 2: لو n فردي، كل القوى فردية، وفردي + فردي + فردي + فردي = زوجي.']),
    style='gap:3.1mm'))

# ---------- solutions ----------
P.append(page('p-s5', 'حلول الوحدة 5', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>تمرين 5.55</h3>\n' +
    W([('1', 'اقلب', r'We show that if \(a\) and \(b\) are odd integers, then \(4 \nmid (3a^2 + 7b^2)\).', 'نقلب «يوجد… 4 يقسم» إلى «لكل… 4 ما يقسم».'),
       ('2', 'خذ أي a و b', r'Let \(a\) and \(b\) be odd integers. Then \(a = 2x + 1\) and \(b = 2y + 1\) for some integers \(x\) and \(y\).', 'أي عددين فرديين.'),
       ('3', 'اثبت', r'Thus, \[\begin{aligned} 3a^2 + 7b^2 &= 3(4x^2 + 4x + 1) + 7(4y^2 + 4y + 1) = 12x^2 + 12x + 28y^2 + 28y + 10 \\ &= 4(3x^2 + 3x + 7y^2 + 7y + 2) + 2 = 4m + 2, \end{aligned}\] where \(m = 3x^2 + 3x + 7y^2 + 7y + 2 \in \mathbb{Z}\). If \(4 \mid (3a^2 + 7b^2)\), then \(4m + 2 = 4t\) for some integer \(t\), and so \(2 = 4(t - m)\), that is, \(4 \mid 2\), which is impossible. Hence \(4 \nmid (3a^2 + 7b^2)\).',
        r'العبارة = \(4m + 2\)، يعني باقيها 2 لما تنقسم على 4. ولو 4 يقسمها يطلع 4 يقسم 2: مستحيل (نفس مثال 7).')], title='') +
    '  <h3>تمرين 5.57</h3>\n' +
    W([('1', 'حالة 1', r'Let \(n \in \mathbb{Z}\). We show that \(n^4 + n^3 + n^2 + n\) is even. <i>Case 1.</i> \(n\) is even. Then \(n = 2k\) for some \(k \in \mathbb{Z}\). So \(n^4 + n^3 + n^2 + n = 16k^4 + 8k^3 + 4k^2 + 2k = 2(8k^4 + 4k^3 + 2k^2 + k)\), which is even.',
        'n زوجي: كل حد زوجي، ونطلّع 2.'),
       ('2', 'حالة 2', r'<i>Case 2.</i> \(n\) is odd. Then \(n = 2k + 1\) for some \(k \in \mathbb{Z}\). So \[\begin{aligned} n^4 + n^3 + n^2 + n &= (16k^4 + 32k^3 + 24k^2 + 8k + 1) + (8k^3 + 12k^2 + 6k + 1) \\ &\quad + (4k^2 + 4k + 1) + (2k + 1) \\ &= 16k^4 + 40k^3 + 40k^2 + 20k + 4 = 2(8k^4 + 20k^3 + 20k^2 + 10k + 2), \end{aligned}\] which is even. Hence there is no integer \(n\) such that \(n^4 + n^3 + n^2 + n\) is odd.',
        'n فردي: نفك كل قوة ونجمع، ونطلّع 2.')], title='') +
    note('trick', 'تريك أسرع:', r'\(n^4 + n^3 + n^2 + n = n(n + 1)(n^2 + 1)\)، و \(n(n + 1)\) حاصل ضرب عددين متتاليين، فهو زوجي دائماً. فالعبارة زوجية لكل n.') +
    box('راجع نفسك (دقيقتين)', '''    <ul class="chk">
      <li><span class="cb"></span>أقول خطوات نفي الوجود من ذاكرتي: اقلب، خذ أي x، اثبت.</li>
      <li><span class="cb"></span>أعرف ليش مثال واحد يكفي لـ «لكل»، وما يكفي لـ «يوجد».</li>
    </ul>
'''), sol=True))

save('f_u5.html', P)
