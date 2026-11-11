import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
P = []
U2 = U[2] + ' · 5.2'

# ---------- p-u2 ----------
P.append(page('p-u2', U2, 'must', 'البرهان بالتناقض: الفكرة' + tag('sol', 'مثال السلايدات 6'),
    idea('تبي تثبت أن شي صحيح؟ افترض أنه غلط، وامشِ بخطوات صحيحة. لو وصلت لشي مستحيل، فافتراضك هو الغلط، والشي صحيح.') +
    qbox('<span class="lb">Result.</span> No odd integer can be expressed as the sum of three even integers.',
         'ما فيه عدد فردي ينكتب كمجموع ثلاث أعداد زوجية.') +
    think('نفكر', [r'نجرب: \(2 + 4 + 6 = 12\)، و \(2 + 2 + 2 = 6\)، و \(10 + 4 + 8 = 22\). كلها زوجية. بس التجربة ما تكفي، لأن الأعداد ما تخلص.',
                   '<b>نعكس:</b> نفترض أن فيه عدد فردي n يساوي مجموع ثلاث أعداد زوجية.',
                   r'<b>نمشي:</b> كل عدد زوجي يساوي 2 في عدد صحيح. فالمجموع \(2a + 2b + 2c = 2(a + b + c)\)، يعني n زوجي.',
                   '<b>تناقض:</b> n فردي (هذا افتراضنا) وزوجي (هذا اللي طلع) في نفس الوقت. مستحيل! إذن الافتراض غلط، وما فيه عدد كذا.']) +
    W([('1', 'نعكس', r'Assume, to the contrary, that there exists an odd integer \(n\) which can be expressed as the sum of three even integers \(x\), \(y\) and \(z\).', 'نفترض العكس: فيه عدد فردي n يساوي مجموع ثلاث أعداد زوجية x و y و z.'),
       ('2', 'نمشي', r'Then \(x = 2a\), \(y = 2b\) and \(z = 2c\) with \(a, b, c \in \mathbb{Z}\). Therefore, \(n = x + y + z = 2a + 2b + 2c = 2(a + b + c)\).', 'نكتب كل زوجي كـ 2 في عدد صحيح، نجمع، ونطلّع 2 عامل مشترك.'),
       ('3', 'تناقض', r'Since \(a + b + c\) is an integer, \(n\) is even. This is a contradiction.', 'n طلع زوجي، وهو فردي. تناقض، فالجملة الأصلية صحيحة.')], title='نكتب (برهان السلايدات)') +
    card('بطاقة الخطوات: البرهان بالتناقض', [
        ('نعكس', 'أول سطر: ' + lt('Assume, to the contrary, that …') + ' وبعدها عكس المطلوب.'),
        ('نمشي', 'خطوات صحيحة: تعاريف وحساب.'),
        ('تناقض', 'توصل لشي مستحيل، وتكتب: ' + lt('This is a contradiction.'))]), style='gap:3.2mm'))

# ---------- p-neg ----------
neg_tbl = ('  <table class="bi2">\n    <tr><th>المطلوب تثبته</th><th>تكتب بعد <span class="lt">Assume, to the contrary, that</span></th></tr>\n' +
    '    <tr><td>There is no smallest positive real number.</td><td>there <b>is</b> a smallest positive real number.</td></tr>\n' +
    r'    <tr><td>\(\sqrt{2}\) is irrational.</td><td>\(\sqrt{2}\) is <b>rational</b>.</td></tr>' + '\n' +
    '    <tr><td>No odd integer can be expressed as …</td><td><b>there exists</b> an odd integer which can be expressed as …</td></tr>\n' +
    r'    <tr><td>If \(a\) is an even integer and \(b\) is an odd integer, then \(4 \nmid (a^2 + 2b^2)\).</td><td>there exist an even integer \(a\) and an odd integer \(b\) such that \(4 \mid (a^2 + 2b^2)\).</td></tr>' + '\n  </table>\n')
P.append(page('p-neg', U[2], 'must', 'أهم سطر: كيف تكتب العكس؟',
    idea('السطر الأول هو نص البرهان. لو كتبت العكس غلط، البرهان كله يروح. شوف كيف انقلبت كل جملة:') +
    neg_tbl +
    box('قواعد العكس', r'''    <ul>
      <li>«ما فيه…» تنقلب «فيه…». و«غير نسبي» تنقلب «نسبي».</li>
      <li>«إذا P فإن Q» عكسها «P صح <b>و</b> Q خطأ». مو «إذا P فإن مو Q».</li>
      <li>«و» تنقلب «أو»، و«أو» تنقلب «و». مثلاً عكس «\(5 \nmid x\) و \(5 \nmid y\)» هو «\(5 \mid x\) أو \(5 \mid y\)».</li>
      <li>\(\nmid\) تنقلب \(\mid\)، و \(\lt\) تنقلب \(\ge\)، و \(\le\) تنقلب \(\gt\).</li>
    </ul>
''') +
    note('star', 'من السلايدات:', 'البرهان بالتناقض يبدأ بـ «' + lt('Suppose that …') + '» أو «' + lt('Assume, to the contrary, that …') + '». والثانية هي اللي في الحلول الرسمية، فاستخدمها.') +
    '  <h3>دورك: اكتب أول سطر بس</h3>\n' +
    W([('1', '', 'Prove that there is no largest negative rational number.' + wl(1.2), None),
       ('2', '', r'Prove that \(\sqrt{3}\) is irrational.' + wl(1.2), None),
       ('3', '', r'Prove that if \(n\) is an odd integer, then \(7n - 5\) is even.' + wl(1.2), None)], title='') +
    '  <p class="small">تتأكد من أجوبتك من أول سطر في حلول 5.12 ' + ref('p-s2a') + ' و5.21 ' + ref('p-rt3') + ' و5.36 (c) ' + ref('p-s3') + '.</p>\n'))

# ---------- p-ex5 ----------
P.append(page('p-ex5', U[2], 'must', 'سؤال ميد 1447، وبعده دورك' + tag('past', 'ميد 1447 · 3 درجات'),
    qbox('<span class="lb">4.</span> There is no smallest positive real number. (3 marks)',
         'ما فيه أصغر عدد حقيقي موجب. جا تحت «' + lt('Prove or disprove') + '»، وهو مثال 5 في السلايدات بالحرف.') +
    think('نفكر', [r'نجرب: هل 1 أصغر عدد موجب؟ لا، \(0.5\) أصغر. هل \(0.5\)؟ لا، \(0.25\) أصغر. أي عدد تختاره، نصّه أصغر منه وموجب.',
                   'فالجملة صحيحة، ونبرهنها بالتناقض. <b>نعكس:</b> نفترض فيه أصغر عدد موجب، ونسميه r.',
                   r'<b>نمشي:</b> نصّه \(r/2\) موجب وأصغر من r. <b>تناقض:</b> لقينا عدد موجب أصغر من «الأصغر».']) +
    W([('1', 'نعكس', r'Assume, to the contrary, that there is a smallest positive real number, say \(r\).', 'نفترض العكس: فيه أصغر عدد حقيقي موجب، ونسميه r.'),
       ('2', 'نمشي', r'Since \(0 \lt r/2 \lt r\), it follows that \(r/2\) is a positive real number that is smaller than \(r\).', 'نص r موجب، وأصغر من r.'),
       ('3', 'تناقض', 'This, however, is a contradiction.', 'وهذا يناقض أن r هو الأصغر.')], title='نكتب (الحل الرسمي: ثلاث جمل عليها 3 درجات)') +
    duork('5.12', '<span class="lb">5.12.</span> Prove that there is no largest negative rational number.',
          r'اثبت أنه ما فيه أكبر عدد نسبي سالب. (النسبي: ينكتب \(a/b\) حيث a و b أعداد صحيحة و \(b \ne 0\).)') +
    W([('1', 'نعكس', None, None, 'b2'), ('2', 'نمشي', None, None, 'b2'), ('3', 'تناقض', None, None, 'b1')], title='') +
    hints([r'<b>تلميح:</b> نص \(-1\) هو \(-0.5\)، وهو أكبر منه. فلو r سالب فإن \(r \lt r/2 \lt 0\). وقل ليش \(r/2\) نسبي: لو \(r = a/b\) فإن \(r/2 = a/(2b)\).']), style='gap:3.1mm'))

# ---------- p-ex7 ----------
P.append(page('p-ex7', U[2], 'must', 'مثال: «إذا… فإن…» بالتناقض' + tag('sol', 'مثال السلايدات 7') + tag('ex', 'دورك'),
    qbox(r'<span class="lb">Result.</span> If \(a\) is an even integer and \(b\) is an odd integer, then \(4 \nmid (a^2 + 2b^2)\).',
         r'إذا a زوجي و b فردي، فإن 4 ما يقسم \(a^2 + 2b^2\). <b>نفكر:</b> العكس هو «الشرط صح والنتيجة خطأ» (شف ' + ref('p-neg') + '). وبعدها نحوّل كل كلمة لمعادلة ونعوّض.') +
    W([('1', 'نعكس', r'Assume, to the contrary, that there exist an even integer \(a\) and an odd integer \(b\) such that \(4 \mid (a^2 + 2b^2)\).', 'الشرط صح (a زوجي و b فردي)، والنتيجة خطأ (4 يقسم).'),
       ('2', 'نمشي', r'Thus, \(a = 2x\), \(b = 2y + 1\) and \(a^2 + 2b^2 = 4z\) for some integers \(x\), \(y\) and \(z\). Hence, \(a^2 + 2b^2 = (2x)^2 + 2(2y + 1)^2 = 4z\). Simplifying, we obtain \(4x^2 + 8y^2 + 8y + 2 = 4z\) or, equivalently, \[2 = 4z - 4x^2 - 8y^2 - 8y = 4(z - x^2 - 2y^2 - 2y).\]', 'نكتب الزوجي والفردي والقسمة كمعادلات، نعوّض، ونخلي 2 لوحدها في طرف.'),
       ('3', 'تناقض', r'Since \(z - x^2 - 2y^2 - 2y\) is an integer, \(4 \mid 2\), which is impossible.', 'طلع أن 4 يقسم 2، وهذا مستحيل.')], title='نكتب (برهان السلايدات)') +
    duork('5.33', r'<span class="lb">5.33.</span> Use a proof by contradiction to prove the following. Let \(x, y \in \mathbb{Z}\). If \(5 \nmid xy\), then \(5 \nmid x\) and \(5 \nmid y\).',
          'استخدم التناقض: إذا 5 ما يقسم xy، فإن 5 ما يقسم x و5 ما يقسم y.') +
    W([('1', 'نعكس', None, None, 'b2'), ('2', 'نمشي', None, None, 'b2'), ('3', 'تناقض', None, None, 'b1')], title='') +
    hints([r'<b>تلميح:</b> العكس فيه «أو» (شف القواعد في ' + ref('p-neg') + r'). ولو \(5 \mid x\) فإن \(x = 5k\)، فـ \(xy = 5(ky)\).']), style='gap:3.1mm'))

# ---------- p-rt2a ----------
P.append(page('p-rt2a', U[2], 'must', r'\(\sqrt{2}\) غير نسبي: نفكر' + tag('sol', 'نظرية من السلايدات'),
    qbox(r'<span class="lb">Theorem.</span> The real number \(\sqrt{2}\) is irrational.',
         r'العدد \(\sqrt{2}\) غير نسبي، يعني ما ينكتب ككسر \(a/b\) من أعداد صحيحة.', lab='النظرية') +
    think('ثلاث أشياء تحتاجها قبل البرهان', [
        '<b>نسبي</b> (' + lt('rational') + r'): ينكتب \(a/b\) حيث a و b أعداد صحيحة و \(b \ne 0\). مثل \(0.75 = 3/4\). و<b>غير نسبي</b> (' + lt('irrational') + '): ما ينكتب كذا.',
        '<b>أبسط صورة</b> (' + lt('lowest terms') + r'): ما فيه عدد غير 1 يقسم البسط والمقام مع بعض. مثل \(3/2\). أما \(6/4\) فمو أبسط صورة، لأن 2 يقسم الاثنين. وأي كسر نقدر نبسّطه لين يوصل أبسط صورة.',
        r'لو \(a^2\) زوجي فإن a زوجي، لأن حاصل ضرب فرديين فردي. (نظرية من الفصل 3.)']) +
    think('نجرب بأرقام: ليش ما نلقى الكسر؟',
          before=tbl(['الكسر', r'\(7/5\)', r'\(17/12\)', r'\(99/70\)'], [['مربعه', r'\(49/25 = 1.96\)', r'\(289/144 \approx 2.007\)', r'\(9801/4900 \approx 2.0002\)']], ltr=True),
          extra='    <p>نقرّب من 2، بس ولا كسر مربعه 2 بالضبط. والبرهان يثبت أن هذا مستحيل، مو بس أننا ما لقينا.</p>\n') +
    think('خطة البرهان (بالتناقض)',
          before=chain([r'نفترض \(\sqrt{2} = a/b\) في أبسط صورة', r'نربّع: \(a^2 = 2b^2\)', 'a زوجي', r'نكتب \(a = 2c\) ونعوّض: \(b^2 = 2c^2\)', 'b زوجي', '2 يقسم a و b', 'تناقض مع «أبسط صورة»']),
          extra='    <p class="small">اقرأ السلسلة من اليمين. كل محطة تطلع من اللي قبلها. في الصفحة الجاية نكتبها بالإنجليزي.</p>\n') +
    note('star', 'ليش مهمة؟', r'السلايدات تقول إنها من أشهر البراهين بالتناقض. وجا مثلها في نهائي 1446: \(\sqrt[3]{7}\) غير نسبي (3 درجات).') +
    '  <div class="space" data-label="دورك: غطِّ السلسلة، واكتب المحطات السبع من ذاكرتك" style="min-height:34mm"></div>\n'))

# ---------- p-rt2b ----------
P.append(page('p-rt2b', U[2], 'must', r'\(\sqrt{2}\) غير نسبي: نكتب' + tag('sol', 'نظرية من السلايدات'),
    W([('1', 'نعكس', r'Assume, to the contrary, that \(\sqrt{2}\) is rational. Then \(\sqrt{2} = a/b\), where \(a, b \in \mathbb{Z}\) and \(b \ne 0\). We may further assume that \(a/b\) has been expressed in (or reduced to) lowest terms.', r'نفترض \(\sqrt{2}\) نسبي: كسر \(a/b\). ونفترض أن الكسر في أبسط صورة.'),
       ('2', 'نربّع', r'Then \(2 = a^2/b^2\); so \(a^2 = 2b^2\). Since \(b^2\) is an integer, \(a^2\) is even. Then \(a\) is even.', r'نربّع الطرفين. \(a^2\) يساوي 2 في عدد صحيح، يعني زوجي. فـ a زوجي.'),
       ('3', 'نعوّض', r'So, \(a = 2c\), where \(c \in \mathbb{Z}\). Thus, \((2c)^2 = 2b^2\) and so \(4c^2 = 2b^2\). Therefore, \(b^2 = 2c^2\). Because \(c^2\) is an integer, \(b^2\) is even, which implies that \(b\) is even.', r'نكتب \(a = 2c\) ونعوّض. يطلع \(b^2 = 2c^2\)، فـ b زوجي بعد.'),
       ('4', 'تناقض', r'Since \(a\) and \(b\) are even, each has 2 as a divisor, which is a contradiction since \(a/b\) has been reduced to lowest terms.', 'a و b الاثنين يقبلون القسمة على 2، وهذا يناقض أن الكسر في أبسط صورة.')], title='') +
    note('trap', 'انتبه:', 'لا تنسَ جملة «أبسط صورة» (' + lt('lowest terms') + ') في المحطة 1. بدونها ما فيه تناقض في المحطة 4.') +
    note('trick', 'نفس القالب لغيره:', r'يشتغل لـ \(\sqrt{3}\) و \(\sqrt{5}\) و \(\sqrt[3]{7}\). بدّل «زوجي» بـ «يقبل القسمة على 3» (أو 5 أو 7)، والباقي نفسه.') +
    '  <div class="why2"><h3>اسأل نفسك</h3><div class="qa">\n    <div class="qq">وين استخدمنا أن الكسر في أبسط صورة؟</div>\n    <div class="aa">في آخر سطر بس. طلع أن 2 يقسم a و b، والكسر اللي في أبسط صورة ما يصير بسطه ومقامه الاثنين زوجيين. هذا هو التناقض.</div>\n  </div></div>\n' +
    box('استراحة: لغز السجناء الثلاثة (من السلايدات، إضافي)', '''    <p style="font-size:11pt">السجّان غطّى عيون ثلاثة سجناء، وحط على جبين كل واحد نقطة حمراء أو زرقاء. بعدين شال الغطاء وقال: اللي يشوف نقطة حمراء على واحد من الاثنين الباقين يرفع يده، وأول واحد يعرف لون نقطته يطلع. هو حط حمراء للثلاثة، فكلهم رفعوا يدهم. بعد مدة قال واحد: «نقطتي حمراء!». كيف عرف؟</p>
    <p style="font-size:11pt"><b>الحل (تناقض):</b> قال في نفسه: «نفترض أن نقطتي زرقاء. الثاني يشوف الثالث رافع يده، والثالث ما يشوف حمراء عندي، فلازم يشوفها عند الثاني. يعني الثاني بيعرف على طول أن نقطته حمراء. بس مر وقت ومحد تكلم. تناقض! إذن نقطتي حمراء.»</p>
''')))

# ---------- p-rt3 ----------
P.append(page('p-rt3', U[2], 'must', 'دورك: توأم النظرية، ثم سؤال النهائي' + tag('past', 'نهائي 1446 · 3 درجات'),
    duork('5.21', r'<span class="lb">5.21.</span> Prove that \(\sqrt{3}\) is irrational. [Hint: By Result 4.8, for an integer \(a\), \(3 \mid a^2\) if and only if \(3 \mid a\).]',
          r'اثبت أن \(\sqrt{3}\) غير نسبي. (تلميح الكتاب: 3 يقسم \(a^2\) إذا وفقط إذا 3 يقسم a.) كمّل الفراغات من ذاكرتك.') +
    r'''  <div class="stmt" style="line-height:2.15">
    <p class="en" style="line-height:2.15">Assume, to the contrary, that \(\sqrt{3}\) is <span class="blank"></span>. Then \(\sqrt{3} = a/b\), where \(a, b \in \mathbb{Z}\) and \(b \ne 0\). We may further assume that \(a/b\) has been reduced to <span class="blank w"></span>. Then \(3 = a^2/b^2\); so \(a^2 =\) <span class="blank s"></span>. Thus \(3 \mid a^2\), and so \(3 \mid\) <span class="blank s"></span>. So, \(a = 3c\), where \(c \in \mathbb{Z}\). Thus, \((3c)^2 = 3b^2\) and so \(9c^2 = 3b^2\). Therefore, \(b^2 =\) <span class="blank s"></span>. Thus \(3 \mid b^2\), which implies that \(3 \mid\) <span class="blank s"></span>. Since \(3 \mid a\) and \(3 \mid b\), this is a <span class="blank w"></span> since \(a/b\) has been reduced to lowest terms.</p>
  </div>
''' +
    qbox(r'Use a proof by contradiction to prove that \(\sqrt[3]{7}\) is irrational.',
         'النص الأصلي (الاختبار كان بالعربي): «مستخدماً طريقة الوقوع في تناقض، أثبت أن الجذر التكعيبي للعدد سبعة هو عدد غير نسبي.» اكتبه كامل بدون ما تطالع.',
         lab='دورك · سؤال نهائي 1446 (3 درجات)', cls='ex') +
    W([('1', 'نعكس', None, None, 'b2'), ('2', 'نمشي', None, None, 'b4'), ('3', 'تناقض', None, None, 'b2')], title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> نفس محطات \(\sqrt{2}\)، بس تكعّب بدل ما تربّع: \(a^3 = 7b^3\). والحل الرسمي يقول: 7 عدد أولي، فلو 7 يقسم \(a^3\) فهو يقسم a.'])))

# ---------- p-518 ----------
P.append(page('p-518', U[2], 'extra', 'مثال: نسبي + غير نسبي' + tag('sol', 'مثال إضافي') + tag('ex', 'دورك'),
    qbox('<span class="lb">Result.</span> The sum of a rational number and an irrational number is irrational.',
         r'مجموع عدد نسبي وعدد غير نسبي هو عدد غير نسبي. (مثال إضافي مو في السلايدات.) <b>نفكر:</b> لو \(1 + \sqrt{2}\) نسبي، كان \(\sqrt{2} = (1 + \sqrt{2}) - 1\) يساوي نسبي ناقص نسبي، يعني نسبي. وهذا غلط. فالحركة: اطرح النسبي.') +
    W([('1', 'نعكس', r'Assume, to the contrary, that there exist a rational number \(x\) and an irrational number \(y\) whose sum is a rational number \(z\).', 'نفترض العكس: نسبي + غير نسبي = نسبي.'),
       ('2', 'نمشي', r'Thus, \(x + y = z\), where \(x = a/b\) and \(z = c/d\) for some integers \(a, b, c, d\) with \(b, d \ne 0\). This implies that \(y = \frac{c}{d} - \frac{a}{b} = \frac{bc - ad}{bd}\).', 'نكتب النسبيين ككسور، ونطرح: y يطلع كسر.'),
       ('3', 'تناقض', r'Since \(bc - ad\) and \(bd\) are integers and \(bd \ne 0\), it follows that \(y\) is rational, which is a contradiction.', 'y طلع نسبي، وهو غير نسبي. تناقض.')]) +
    duork('5.18', '<span class="lb">5.18.</span> Prove that the product of an irrational number and a nonzero rational number is irrational.',
          'اثبت أن حاصل ضرب عدد غير نسبي في عدد نسبي غير الصفر هو عدد غير نسبي.') +
    W([('1', 'نعكس', None, None, 'b2'), ('2', 'نمشي', None, None, 'b2'), ('3', 'تناقض', None, None, 'b1')], title='') +
    hints([r'<b>تلميح:</b> سمِّ غير النسبي a والنسبي b. لو \(ab\) نسبي فإن \(a = (ab) \div b\)، وقسمة كسرين تعطي كسر.']), style='gap:3.1mm'))

# ---------- p-s2a ----------
P.append(page('p-s2a', 'حلول الوحدة 2', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>تمرين 5.12</h3>\n' +
    W([('1', 'نعكس', r'Assume, to the contrary, that there is a largest negative rational number, say \(r\).', 'نفترض فيه أكبر عدد نسبي سالب r.'),
       ('2', 'نمشي', r'Then \(r = a/b\) for some integers \(a\) and \(b\) with \(b \ne 0\), and so \(r/2 = a/(2b)\) is a rational number. Since \(r \lt 0\), it follows that \(r \lt r/2 \lt 0\).', r'نص r نسبي بعد، وهو سالب وأكبر من r. (مثل: نص \(-1\) هو \(-0.5\)، وهو أكبر من \(-1\).)'),
       ('3', 'تناقض', r'Thus \(r/2\) is a negative rational number that is larger than \(r\). This is a contradiction.', 'لقينا نسبي سالب أكبر من «الأكبر».')], title='') +
    '  <h3>تمرين 5.33</h3>\n' +
    W([('1', 'نعكس', r'Assume, to the contrary, that there exist integers \(x\) and \(y\) such that \(5 \nmid xy\) and either \(5 \mid x\) or \(5 \mid y\).', 'الشرط صح (5 ما يقسم xy)، والنتيجة خطأ («و» انقلبت «أو»).'),
       ('2', 'نمشي', r'Without loss of generality, assume that \(5 \mid x\). Then \(x = 5k\) for some integer \(k\). So \(xy = (5k)y = 5(ky)\).', 'x و y لهم نفس الدور، فنكتب حالة وحدة (' + lt('Without loss of generality') + '). وتقدر تكتب الحالتين.'),
       ('3', 'تناقض', r'Since \(ky\) is an integer, \(5 \mid xy\), which is a contradiction.', '5 يقسم xy، وافتراضنا أنه ما يقسمه.')], title='') +
    '  <h3>تمرين 5.21: الفراغات بالترتيب</h3>\n' +
    r'''  <ol class="notes" style="direction:ltr; text-align:left; font-family:var(--en); columns:4; column-gap:6mm">
    <li>rational</li><li>lowest terms</li><li>\(3b^2\)</li><li>\(a\)</li><li>\(3c^2\)</li><li>\(b\)</li><li>contradiction</li>
  </ol>
''' +
    note('trick', 'قارن:', r'حط برهان \(\sqrt{3}\) جنب برهان \(\sqrt{2}\) ' + ref('p-rt2b') + '. الفرق الوحيد: «يقبل القسمة على 3» بدل «زوجي».'), sol=True))

# ---------- p-s2b ----------
P.append(page('p-s2b', 'حلول الوحدة 2', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>سؤال نهائي 1446</h3>\n' +
    W([('1', 'نعكس', r'Assume, to the contrary, that \(\sqrt[3]{7}\) is rational. Then \(\sqrt[3]{7} = a/b\), where \(a, b \in \mathbb{Z}\) and \(b \ne 0\). We may further assume that \(a/b\) has been reduced to lowest terms.', 'نفترض أنه نسبي: كسر في أبسط صورة.'),
       ('2', 'نمشي', r'Then \(7 = a^3/b^3\); so \(a^3 = 7b^3\). Thus \(7 \mid a^3\). Since 7 is a prime, \(7 \mid a\). So \(a = 7c\), where \(c \in \mathbb{Z}\). Thus \((7c)^3 = 7b^3\) and so \(343c^3 = 7b^3\). Therefore \(b^3 = 49c^3 = 7(7c^3)\). Thus \(7 \mid b^3\) and so \(7 \mid b\).', r'نكعّب الطرفين. 7 يقسم \(a^3\) فيقسم a (لأن 7 أولي، مثل ما في الحل الرسمي). نعوّض \(a = 7c\)، فيطلع أن 7 يقسم b بعد.'),
       ('3', 'تناقض', r'Since \(7 \mid a\) and \(7 \mid b\), this is a contradiction since \(a/b\) has been reduced to lowest terms.', '7 يقسم الاثنين، والكسر في أبسط صورة. تناقض.')], title='') +
    '  <p class="small">الحل الرسمي مكتوب بالعربي وبنفس المحطات: كسر في أبسط صورة، نكعّب، 7 يقسم a، نعوّض، 7 يقسم b، تناقض مع أن القاسم المشترك الأكبر 1.</p>\n' +
    '  <h3>تمرين 5.18</h3>\n' +
    W([('1', 'نعكس', r'Assume, to the contrary, that there exist an irrational number \(a\) and a nonzero rational number \(b\) such that \(ab\) is rational.', 'نفترض العكس: غير نسبي في نسبي يعطي نسبي.'),
       ('2', 'نمشي', r'Then \(b = p/q\) and \(ab = r/s\), where \(p, q, r, s \in \mathbb{Z}\) and \(p, q, s \ne 0\). Hence \(a = \frac{ab}{b} = \frac{r}{s} \cdot \frac{q}{p} = \frac{rq}{sp}\).', r'نكتب النسبيين ككسور (\(p \ne 0\) لأن b مو صفر)، ونقسم: a يطلع كسر.'),
       ('3', 'تناقض', r'Since \(rq\) and \(sp\) are integers and \(sp \ne 0\), the number \(a\) is rational, which is a contradiction.', 'a طلع نسبي، وهو غير نسبي.')], title='') +
    box('راجع نفسك (3 دقائق)', '''    <ul class="chk">
      <li><span class="cb"></span>أقول الخطوات الثلاث من ذاكرتي: نعكس، نمشي، تناقض.</li>
      <li><span class="cb"></span>أكتب برهان «ما فيه أصغر عدد موجب» بدون ما أطالع (ثلاث جمل).</li>
      <li><span class="cb"></span>أكتب برهان \\(\\sqrt{2}\\) بمحطاته الأربع بدون ما أطالع.</li>
    </ul>
'''), sol=True))

save('c_u2.html', P)
