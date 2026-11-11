import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
P = []
U3 = U[3] + ' · 5.3'

# ---------- p-u3 ----------
P.append(page('p-u3', U3, 'must', 'ثلاث طرق لنفس الجملة' + tag('sol', 'مثال توأم 5.36'),
    idea('جملة «إذا P فإن Q» تنبرهن بثلاث طرق. الفرق كله في أول سطر: وش تفترض، ووين تبي توصل.') +
    think('الفرق في أول سطر', before=tbl([('الطريقة', 'width:40%'), 'تفترض (أول سطر)', 'توصل لـ'],
        [[('مباشر (' + lt('direct proof') + ')', 'class="s"'), 'P صح', 'Q صح'],
         [('عكس النقيض (' + lt('proof by contrapositive') + ')', 'class="s"'), 'Q خطأ', 'P خطأ'],
         [('تناقض (' + lt('proof by contradiction') + ')', 'class="s"'), 'P صح و Q خطأ', 'شي مستحيل']])) +
    qbox(r'Prove that if \(n\) is an even integer, then \(3n + 7\) is odd.',
         r'اثبت: إذا n زوجي، فإن \(3n + 7\) فردي. هنا P هي «n زوجي»، و Q هي «\(3n + 7\) فردي».') +
    W([('(a)', 'مباشر', r'Assume that \(n\) is even. Then \(n = 2k\) for some integer \(k\). So \(3n + 7 = 6k + 7 = 2(3k + 3) + 1\). Since \(3k + 3\) is an integer, \(3n + 7\) is odd.',
        r'افترضنا P (n زوجي)، ووصلنا لـ Q (\(3n + 7\) فردي).'),
       ('(b)', 'عكس النقيض', r'Assume that \(3n + 7\) is even. Then \(3n + 7 = 2k\) for some integer \(k\). So \(n = (3n + 7) - 2n - 7 = 2k - 2n - 7 = 2(k - n - 4) + 1\). Since \(k - n - 4\) is an integer, \(n\) is odd.',
        r'افترضنا أن Q خطأ (\(3n + 7\) زوجي)، ووصلنا أن P خطأ (n فردي).'),
       ('(c)', 'تناقض', r'Assume, to the contrary, that there exists an even integer \(n\) such that \(3n + 7\) is even. Then \(n = 2x\) and \(3n + 7 = 2y\) for some integers \(x\) and \(y\). Hence \(3(2x) + 7 = 2y\), and so \(7 = 2y - 6x = 2(y - 3x)\). Since \(y - 3x\) is an integer, 7 is even, which is a contradiction.',
        'افترضنا P صح و Q خطأ مع بعض، فطلع أن 7 زوجي. مستحيل.')], title='نكتب: نفس الجملة بثلاث طرق') +
    note('trap', 'انتبه:', 'لا تبدأ بـ «' + lt(r'Assume that \(3n + 7\) is odd') + '»: هذا افتراض للمطلوب نفسه.') +
    note('trick', 'أي طريقة؟', 'لو السؤال حددها التزم فيها. لو ما حدد: جرّب المباشر أول.'), style='gap:3mm'))

# ---------- p-536 ----------
P.append(page('p-536', U[3], 'must', 'تمرين 5.36' + tag('ex', 'دورك'),
    duork('5.36', r'<span class="lb">5.36.</span> Prove that if \(n\) is an odd integer, then \(7n - 5\) is even by (a) a direct proof, (b) a proof by contrapositive and (c) a proof by contradiction.',
          r'اثبت: إذا n فردي، فإن \(7n - 5\) زوجي، بثلاث طرق: (a) مباشر، (b) عكس النقيض، (c) تناقض.') +
    recall('قبل ما تكتب: حدّد P و Q. واكتب أول سطر لكل طريقة من ذاكرتك، وبعدها كمّل.') +
    W([('(a)', 'مباشر', None, None, 'b3'), ('(b)', 'عكس النقيض', None, None, 'b3'), ('(c)', 'تناقض', None, None, 'b3')], title='', cls='tpl grow') +
    hints([r'<b>تلميح (b):</b> من \(7n - 5 = 2k + 1\) طلّع n لوحدها: \(n = (7n - 5) - 6n + 5\).',
           r'<b>تلميح (c):</b> \(n = 2x + 1\) و \(7n - 5 = 2y + 1\). عوّض الأولى في الثانية، وشوف أي عدد يطلع «زوجي» وهو مو زوجي.'])))

# ---------- p-539 ----------
P.append(page('p-539', U[3], 'extra', 'تمرين 5.39' + tag('ex', 'دورك'),
    duork('5.39', r'<span class="lb">5.39.</span> Let \(x, y \in \mathbb{R}^+\). Prove that if \(x \le y\), then \(x^2 \le y^2\) by (a) a direct proof, (b) a proof by contrapositive and (c) a proof by contradiction.',
          r'x و y عددين حقيقيين موجبين. اثبت: إذا \(x \le y\) فإن \(x^2 \le y^2\)، بثلاث طرق.') +
    think('قبل ما تكتب', [r'بأرقام: \(2 \le 3\) و \(4 \le 9\) ' + OK + r' وشرط «موجبين» مهم: \(-3 \le 2\) لكن \(9 \le 4\) خطأ.',
                          r'حركتين تحتاجهم: لو ضربت متباينة في عدد موجب، اتجاهها ما يتغير. و \(x^2 - y^2 = (x - y)(x + y)\).']) +
    W([('(a)', 'مباشر', None, None, 'b3'), ('(b)', 'عكس النقيض', None, None, 'b3'), ('(c)', 'تناقض', None, None, 'b3')], title='', cls='tpl grow') +
    hints([r'<b>تلميح (a):</b> اضرب \(x \le y\) في x مرة، وفي y مرة.',
           r'<b>تلميح (b) و(c):</b> عكس \(x^2 \le y^2\) هو \(x^2 \gt y^2\)، يعني \((x - y)(x + y) \gt 0\). و \(x + y\) موجب.'])))

# ---------- p-s3 ----------
P.append(page('p-s3', 'حلول الوحدة 3', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>تمرين 5.36</h3>\n' +
    W([('(a)', 'مباشر', r'Assume that \(n\) is odd. Then \(n = 2k + 1\) for some integer \(k\). So \(7n - 5 = 7(2k + 1) - 5 = 14k + 2 = 2(7k + 1)\). Since \(7k + 1\) is an integer, \(7n - 5\) is even.', 'افترضنا P ووصلنا لـ Q.'),
       ('(b)', 'عكس النقيض', r'Assume that \(7n - 5\) is odd. Then \(7n - 5 = 2k + 1\) for some integer \(k\). So \(n = (7n - 5) - 6n + 5 = 2k + 1 - 6n + 5 = 2(k - 3n + 3)\). Since \(k - 3n + 3\) is an integer, \(n\) is even.', 'افترضنا أن Q خطأ، ووصلنا أن P خطأ (n زوجي).'),
       ('(c)', 'تناقض', r'Assume, to the contrary, that there exists an odd integer \(n\) such that \(7n - 5\) is odd. Then \(n = 2x + 1\) and \(7n - 5 = 2y + 1\) for some integers \(x\) and \(y\). Hence \(7(2x + 1) - 5 = 2y + 1\), so \(14x + 2 = 2y + 1\) and \(1 = 2y - 14x = 2(y - 7x)\). Since \(y - 7x\) is an integer, 1 is even, which is a contradiction.', 'افترضنا P صح و Q خطأ، فطلع أن 1 زوجي. مستحيل.')], title='') +
    '  <h3>تمرين 5.39</h3>\n' +
    W([('(a)', 'مباشر', r'Assume that \(x \le y\). Since \(x \gt 0\), multiplying both sides by \(x\) gives \(x^2 \le xy\). Since \(y \gt 0\), multiplying both sides of \(x \le y\) by \(y\) gives \(xy \le y^2\). Therefore \(x^2 \le xy \le y^2\), and so \(x^2 \le y^2\).', 'ضربنا المتباينة في x مرة وفي y مرة، وربطنا النتيجتين.'),
       ('(b)', 'عكس النقيض', r'Assume that \(x^2 \gt y^2\). Then \(x^2 - y^2 \gt 0\), and so \((x - y)(x + y) \gt 0\). Since \(x + y \gt 0\), dividing both sides by \(x + y\) gives \(x - y \gt 0\). Hence \(x \gt y\).', r'افترضنا أن Q خطأ (\(x^2 \gt y^2\))، ووصلنا أن P خطأ (\(x \gt y\)).'),
       ('(c)', 'تناقض', r'Assume, to the contrary, that there exist positive real numbers \(x\) and \(y\) such that \(x \le y\) and \(x^2 \gt y^2\). Then \((x - y)(x + y) = x^2 - y^2 \gt 0\). Since \(x + y \gt 0\), it follows that \(x - y \gt 0\), and so \(x \gt y\). This contradicts \(x \le y\).', r'افترضنا P صح و Q خطأ، فطلع \(x \gt y\) و \(x \le y\) مع بعض. مستحيل.')], title='') +
    box('راجع نفسك (دقيقتين)', '''    <ul class="chk">
      <li><span class="cb"></span>أكتب أول سطر لكل طريقة من الثلاث بدون ما أطالع.</li>
      <li><span class="cb"></span>أعرف وين أوصل في كل طريقة: Q، أو عكس P، أو شي مستحيل.</li>
    </ul>
'''), sol=True))

save('d_u3.html', P)
