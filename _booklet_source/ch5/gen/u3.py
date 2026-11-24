import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
P = []
U3 = U[3] + ' · 5.3'

# ---------- p-u3 ----------
P.append(page('p-u3', U3, 'top', 'ثلاث طرق لنفس الجملة' + tag('sol', 'مثال توأم 5.36'),
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
    note('trick', 'ليش عكس النقيض يكفي؟', '«إذا Q خطأ فإن P خطأ» تساوي «إذا P فإن Q» بالضبط، فلو برهنت وحدة انبرهنت الثانية. واسمه «عكس النقيض» لأنك تعكس الجملة وتنفي طرفيها.'), style='gap:2.6mm'))

# ---------- p-tpl3: the November question with the same template ----------
P.append(page('p-tpl3', U[3], 'top', 'سؤال ميد نوفمبر: نفس القالب، أرقام ثانية' + tag('past', 'نوفمبر · 2+2+2'),
    qbox(r'<span class="lb">Question 2:</span> Prove that if \(n\) is an even integer, then \(5n + 3\) is odd by 1. a direct proof. 2. a proof by contrapositive. 3. a proof by contradiction.',
         r'إذا n زوجي، فإن \(5n + 3\) فردي، بثلاث طرق. كل طريقة عليها درجتين.', lab='سؤال ميد نوفمبر · 6 درجات') +
    think(r'نفكر: وش يتغير عن \(3n + 7\)؟', before=tbl([('الطريقة', 'width:22%'), r'في \(3n + 7\) (الصفحة اللي قبل)', r'في \(5n + 3\)'], [
        [('مباشر', 'class="s"'), r'\(6k + 7 = 2(3k + 3) + 1\)', r'\(10k + 3 = 2(5k + 1) + 1\)'],
        [('عكس النقيض', 'class="s"'), r'\(n = (3n + 7) - 2n - 7\)', r'\(n = (5n + 3) - 4n - 3\)'],
        [('تناقض', 'class="s"'), r'\(7 = 2(y - 3x)\)', r'\(3 = 2(y - 5x)\)']]),
        extra='    <p>الجمل الإنجليزية نفسها حرف بحرف. اللي يتغير سطر الحساب بس.</p>\n') +
    W([('1', 'مباشر', r'Assume that \(n\) is even. Then \(n = 2k\) for some integer \(k\). So \(5n + 3 = 10k + 3 = 2(5k + 1) + 1\). Since \(5k + 1\) is an integer, \(5n + 3\) is odd.',
        'افترضنا P (n زوجي)، ووصلنا لـ Q.', dict(BKP, id='m-5n3')),
       ('2', 'عكس النقيض', r'Assume that \(5n + 3\) is even. Then \(5n + 3 = 2k\) for some integer \(k\). So \(n = (5n + 3) - 4n - 3 = 2k - 4n - 3 = 2(k - 2n - 2) + 1\). Since \(k - 2n - 2\) is an integer, \(n\) is odd.',
        r'افترضنا عكس Q (\(5n + 3\) زوجي)، ووصلنا لعكس P (n فردي).'),
       ('3', 'تناقض', r'Assume, to the contrary, that there exists an even integer \(n\) such that \(5n + 3\) is even. Then \(n = 2x\) and \(5n + 3 = 2y\) for some integers \(x\) and \(y\). Hence \(10x + 3 = 2y\), and so \(3 = 2y - 10x = 2(y - 5x)\). Since \(y - 5x\) is an integer, 3 is even, which is a contradiction.',
        'افترضنا P وعكس Q مع بعض، فطلع أن 3 زوجي. مستحيل.')], title='نكتب (كل طريقة درجتين)') +
    note('trap', 'أكثر غلطة:', r'في (2) تفترض «n فردي» وتوصل «\(5n + 3\) زوجي». هذا مو عكس النقيض! عكس النقيض يبدأ من النتيجة: افترض أن \(5n + 3\) زوجي.') +
    note('trick', 'تريك (2):', r'اكتب \(n = (5n + 3) - 4n - 3\). المعامل 5 صار 4، وهو زوجي، فتطلع 2 عامل مشترك بسهولة.'), style='gap:2.6mm'))

# ---------- p-fill3: two exam questions to solve on paper, and spot the error ----------
P.append(page('p-fill3', U[3], 'top', 'دورك: سؤالين من الميدات' + tag('past', 'البنات · ميد 1446') + tag('ex', 'دورك'),
    idea('حل السؤالين على ورقتك بنفس قالب سؤال نوفمبر، بدون ما تطالع الصفحة اللي قبل. بعدها اضغط «الحل» وقارن.') +
    qbox(r'<span class="lb">1-</span> “If \(n\) is an even integer, then \(5n + 1\) is odd” using three ways: direct proof, proof by contrapositive and proof by contradiction. (6 marks)',
         r'نفس سؤال نوفمبر، بس \(+1\) بدل \(+3\).', lab='دورك · سؤال ميد البنات', cls='ex', qid='q-girls', sol='s-girls') +
    duork('5.36', '<span class="lb">5.36.</span> ' + EX['5.36'],
          r'جا بالحرف في ميد 1446 (7 درجات). هنا الشرط «n فردي»: \(n = 2k + 1\)، والنتيجة «زوجي».') +
    hq('لقِ الغلط: طالب كتب هذا في (2) لسؤال البنات', 'q-err', 's-err', txt='الجواب') +
    '  <div class="err"><p class="en">' + r'Assume that \(n\) is odd. Then \(n = 2k + 1\) for some integer \(k\). So \(5n + 1 = 10k + 6 = 2(5k + 3)\). Since \(5k + 3\) is an integer, \(5n + 1\) is even.' + '</p></div>\n' +
    '  <p class="recall">الحساب صح، بس البرهان نفسه غلط. ليش؟ وش لازم يكون أول سطر؟</p>\n', style='gap:3mm'))

# ---------- p-ineq: three ways with an inequality (the book's example in 5.3) ----------
P.append(page('p-ineq', U[3], 'low', 'ثلاث طرق مع متباينة' + tag('sol', 'مثال الكتاب في 5.3'),
    qbox(r'<span class="lb">Result.</span> Let \(x\) be a nonzero real number. If \(x + \frac{1}{x} \lt 2\), then \(x \lt 0\).',
         r'x عدد حقيقي مو صفر. إذا \(x + 1/x \lt 2\) فإن x سالب. نفس الثلاث طرق، بس الحساب متباينات بدل زوجي وفردي.', lab='مثال الكتاب في 5.3') +
    think('ثلاث حركات بس', [r'لو ضربت أو قسمت متباينة على عدد موجب (مثل x لما \(x \gt 0\)، أو \(x^2\))، اتجاهها ما يتغير.',
                            r'أي مربع ما يصير سالب: \((x - 1)^2 = x^2 - 2x + 1 \ge 0\).',
                            r'عكس «\(x \lt 0\)» هو «\(x \ge 0\)». ولأن x مو صفر، يصير \(x \gt 0\).']) +
    W([('(a)', 'مباشر', r'Assume that \(x + \frac{1}{x} \lt 2\). Since \(x^2 \gt 0\), multiplying both sides by \(x^2\) gives \(x^3 + x \lt 2x^2\), and so \(x^3 - 2x^2 + x \lt 0\), that is, \(x(x - 1)^2 \lt 0\). Since \((x - 1)^2 \ge 0\) and \(x(x - 1)^2 \ne 0\), it follows that \((x - 1)^2 \gt 0\), and so \(x \lt 0\).',
        r'نضرب في \(x^2\) (موجب دايماً)، ونجمع كل شي في طرف، ونحلل. المربع ما يصير سالب، فالسالب جا من x.'),
       ('(b)', 'عكس النقيض', r'Assume that \(x \ge 0\). Since \(x \ne 0\), it follows that \(x \gt 0\). Because \((x - 1)^2 \ge 0\), we have \((x - 1)^2 = x^2 - 2x + 1 \ge 0\). Adding \(2x\) to both sides of this inequality, we obtain \(x^2 + 1 \ge 2x\). Dividing both sides of the inequality \(x^2 + 1 \ge 2x\) by the positive number \(x\), we obtain \(x + \frac{1}{x} \ge 2\), as desired.',
        r'عكس النتيجة: x موجب. نبدأ من مربع \(\ge 0\) ونمشي لين نوصل \(x + 1/x \ge 2\)، يعني الشرط خطأ.'),
       ('(c)', 'تناقض', r'Assume, to the contrary, that there exists a nonzero real number \(x\) such that \(x + \frac{1}{x} \lt 2\) and \(x \ge 0\). Since \(x \ne 0\), it follows that \(x \gt 0\). Multiplying both sides of the inequality \(x + \frac{1}{x} \lt 2\) by \(x\), we obtain \(x^2 + 1 \lt 2x\). Subtracting \(2x\) from both sides, we have \(x^2 - 2x + 1 \lt 0\). It then follows that \((x - 1)^2 \lt 0\), which is a contradiction.',
        'الشرط صح والنتيجة خطأ مع بعض. نضرب في x الموجب، فيطلع مربع سالب. مستحيل.')], title='نكتب ((b) و(c) من الكتاب بالحرف)') +
    duork('5.39', '<span class="lb">5.39.</span> ' + EX['5.39'],
          r'x و y موجبين. نفس حركات المثال: الضرب في عدد موجب، و \(x^2 - y^2 = (x - y)(x + y)\).'), style='gap:3mm'))

# ---------- p-s3 ----------
P.append(page('p-s3', 'حلول الوحدة 3', '', 'الحلول' + tag('sol', 'شيّك'),
    sh('سؤال البنات', 's-girls', [('q-girls', 'السؤال')]) +
    W([('(1)', 'مباشر', r'Assume that \(n\) is even. Then \(n = 2k\) for some integer \(k\). So \(5n + 1 = 10k + 1 = 2(5k) + 1\). Since \(5k\) is an integer, \(5n + 1\) is odd.', ''),
       ('(2)', 'عكس النقيض', r'Assume that \(5n + 1\) is even. Then \(5n + 1 = 2k\) for some integer \(k\). So \(n = (5n + 1) - 4n - 1 = 2k - 4n - 1 = 2(k - 2n - 1) + 1\). Since \(k - 2n - 1\) is an integer, \(n\) is odd.', ''),
       ('(3)', 'تناقض', r'Assume, to the contrary, that there exists an even integer \(n\) such that \(5n + 1\) is even. Then \(n = 2x\) and \(5n + 1 = 2y\) for some integers \(x\) and \(y\). Hence \(10x + 1 = 2y\), and so \(1 = 2y - 10x = 2(y - 5x)\). Since \(y - 5x\) is an integer, 1 is even, which is a contradiction.', '')], title='') +
    note('trap', 'لقِ الغلط:', r'الطالب افترض «n فردي» ووصّل «\(5n + 1\) زوجي». هذا يثبت جملة ثانية (عكس P يعطي عكس Q)، مو عكس النقيض. الصح: ' + lt(r'Assume that \(5n + 1\) is even.') + ' ويوصّل أن n فردي. ' + back('q-err')).replace('<div class="note trap">', '<div class="note trap" id="s-err">') +
    sh('تمرين 5.36 (ميد 1446)', 's-536', SM('536', [('p-papers', 'ورقة الميدات')])['back']) +
    W([('(a)', 'مباشر', r'Assume that \(n\) is odd. Then \(n = 2k + 1\) for some integer \(k\). So \(7n - 5 = 7(2k + 1) - 5 = 14k + 2 = 2(7k + 1)\). Since \(7k + 1\) is an integer, \(7n - 5\) is even.', ''),
       ('(b)', 'عكس النقيض', r'Assume that \(7n - 5\) is odd. Then \(7n - 5 = 2k + 1\) for some integer \(k\). So \(n = (7n - 5) - 6n + 5 = 2k + 1 - 6n + 5 = 2(k - 3n + 3)\). Since \(k - 3n + 3\) is an integer, \(n\) is even.', ''),
       ('(c)', 'تناقض', r'Assume, to the contrary, that there exists an odd integer \(n\) such that \(7n - 5\) is odd. Then \(n = 2x + 1\) and \(7n - 5 = 2y + 1\) for some integers \(x\) and \(y\). Hence \(7(2x + 1) - 5 = 2y + 1\), so \(14x + 2 = 2y + 1\) and \(1 = 2y - 14x = 2(y - 7x)\). Since \(y - 7x\) is an integer, 1 is even, which is a contradiction.', '')], title='') +
    '', sol=True))

P.append(page('p-s3b', 'حلول الوحدة 3', '', 'حل تمرين 5.39' + tag('sol', 'شيّك'),
    sh('تمرين 5.39', 's-539', SM('539')['back']) +
    W([('(a)', 'مباشر', r'Assume that \(x \le y\). Since \(x \gt 0\), multiplying both sides by \(x\) gives \(x^2 \le xy\). Since \(y \gt 0\), multiplying both sides of \(x \le y\) by \(y\) gives \(xy \le y^2\). Therefore \(x^2 \le xy \le y^2\), and so \(x^2 \le y^2\).', 'ضربنا المتباينة في x مرة وفي y مرة، وربطنا النتيجتين.'),
       ('(b)', 'عكس النقيض', r'Assume that \(x^2 \gt y^2\). Then \(x^2 - y^2 \gt 0\), and so \((x - y)(x + y) \gt 0\). Since \(x + y \gt 0\), dividing both sides by \(x + y\) gives \(x - y \gt 0\). Hence \(x \gt y\).', r'افترضنا أن Q خطأ (\(x^2 \gt y^2\))، ووصلنا أن P خطأ (\(x \gt y\)).'),
       ('(c)', 'تناقض', r'Assume, to the contrary, that there exist positive real numbers \(x\) and \(y\) such that \(x \le y\) and \(x^2 \gt y^2\). Then \((x - y)(x + y) = x^2 - y^2 \gt 0\). Since \(x + y \gt 0\), it follows that \(x - y \gt 0\), and so \(x \gt y\). This contradicts \(x \le y\).', r'افترضنا P صح و Q خطأ، فطلع \(x \gt y\) و \(x \le y\) مع بعض. مستحيل.')], title=''), sol=True))

save('d_u3.html', P)
