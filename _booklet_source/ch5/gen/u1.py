import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
import re

def toc_row(u, kind, words, ex, pid):
    return ['<b>' + u + '</b>', (kind, 'class="s"'), (words, 'class="s"'), ex, ref(pid)]

def prow(kind, ex, where, mk, st, pid):
    return ['<b>' + kind + '</b><br><span class="small">' + ex + '</span>', where, mk, st, ref(pid)]

S3 = '<span class="stars">★★★</span>'
S2 = '<span class="stars">★★</span><span class="stars dim">★</span>'
S1 = '<span class="stars">★</span><span class="stars dim">★★</span>'

cover = r'''<section class="page cover" id="p-cover">
  <div class="hdr"><span class="u">131 ريض · الميد الثاني والاختبار البديل</span><span class="pn"></span></div>
  <div>
    <p class="kicker">ملزمة الفصل 5 · الأقسام 5.1 إلى 5.5 · نسخة التدريب</p>
    <h1>الوجود والبرهان بالتناقض</h1>
    <p class="sub">رتّبناها على اللي جا فعلاً في أربع ميدات: ميد 1446، وميد 1447، وميد البنات، وميد نوفمبر 2026. الأسئلة تتكرر، والأرقام بس تتغير.</p>
  </div>
  <div class="box">
    <h3>وش يجي من الفصل 5؟</h3>
''' + tbl([('نوع السؤال، ومثال من الاختبار', 'width:41%'), 'جا في', ('الدرجة', 'width:11%'), ('الأهمية', 'width:11%'), ('الصفحة', 'width:9%')], [
    prow('ثلاث طرق للبرهان', r'إذا n زوجي فإن \(5n + 3\) فردي', 'ميد 1446 · البنات · نوفمبر', '6 إلى 7', S3, 'p-u3'),
    prow('ما فيه أصغر عدد موجب', lt('There is no smallest positive real number.'), 'ميد 1447 · البنات · نوفمبر', '3', S3, 'p-ex5'),
    prow('مثال مضاد فيه فخ', r'لكل n زوجي موجب، 12 يقسم \(n^2 - 4\)', 'ميد 1447 · البنات · نوفمبر', '2 إلى 3', S3, 'p-mid5'),
    prow('غير نسبي', r'\(\sqrt{2}\) غير نسبي، و \(\sqrt[3]{7}\) غير نسبي', 'نوفمبر · نهائي 1446', '3 إلى 4', S2, 'p-rt2a'),
    prow('الوجود ونفي الوجود', lt('There exists …'), 'ما جا ولا مرة', '—', S1, 'p-u4'),
], cls='t toc').replace('    <table', '  <table').replace('    </table>', '  </table>') + r'''  </div>
  <div class="box">
    <h3>كيف تتدرب: كل نوع بأربع مستويات</h3>
    <div class="levels">
      <div class="lvx"><b><span class="num">1</span>شوف</b>مثال محلول سطر بسطر، وتحت كل سطر معناه.</div>
      <div class="lvx"><b><span class="num">2</span>أكمل</b>نفس الحل وفيه فراغات. تعبيها من ذاكرتك.</div>
      <div class="lvx"><b><span class="num">3</span>اكتب لحالك</b>«دورك»: تحل من الصفر، وبعدها تشيّك من الحلول.</div>
      <div class="lvx"><b><span class="num">4</span>اختبر نفسك</b>«قاعة الاختبار»: أوراق بصيغة الاختبار ودرجاته.</div>
    </div>
  </div>
  <div class="grid2">
    <div class="box">
      <h3>خطة المذاكرة</h3>
      <p class="fl3"><b>الجلسة 1 (ساعتين):</b> الوحدتين 1 و2، وركّز على صفحات&nbsp;★.</p>
      <p class="fl3"><b>الجلسة 2 (ساعتين):</b> الوحدة 3 كلها (أهم سؤال)، وبعدها الوحدتين 4 و5 بسرعة.</p>
      <p class="fl3"><b>الجلسة 3 (ساعتين):</b> «قاعة الاختبار» <span class="ref" data-to="p-bank"></span>: البنك، وأوراق الميدات، والاختبارين التجريبيين.</p>
      <p class="fl3"><b>ليلة الاختبار:</b> ورقة ليلة الاختبار <span class="ref" data-to="p-night"></span>.</p>
    </div>
    <div class="box">
      <h3>رموز الصفحات</h3>
      <p class="fl3"><span class="lv top">★ يتكرر في الاختبارات</span> سؤاله جا أكثر من مرة.</p>
      <p class="fl3"><span class="lv top">★ مرشّح للبديل</span> من أمثلة الكتاب اللي ياخذون منها، وما جا للحين. وقتك قليل؟ ذاكر صفحات النجمة بس.</p>
      <p class="fl3"><span class="lv must">أساسي</span> شرح تحتاجه. <span class="lv low">احتمال أقل</span> من الخطة، بس ما جا في الميدات.</p>
      <p class="fl3"><span style="color:var(--acc);font-weight:700">■</span> شرح <span style="color:#2f5fa8;font-weight:700">■</span> دورك <span style="color:#b47a00;font-weight:700">■</span> سؤال اختبار <span style="color:#8a959c;font-weight:700">■</span> حلول</p>
    </div>
  </div>
  <div class="note trick"><span class="k">اضغط وروح:</span>زر <a class="go" href="#p-bank">الحل ص N</a> عند كل سؤال يوديك لحله، وزر <a class="back" href="#p-cover">↩ السؤال</a> يرجعك. وأي «ص N» تنضغط.</div>
  <p class="small">«توأم» في الملزمة يعني: نفس السؤال، بأرقام أو كلمة ثانية. أسئلة الاستقراء (في ميد نوفمبر: فقرة 1.4 وسؤال 3) في ملزمة الفصل 6. علقت بكلمة إنجليزية؟ شوف <span class="ref" data-to="p-phr"></span>.</p>
</section>
'''

U1 = U[1] + ' · 5.1'
P = [cover]

# ---------- p-u1 ----------
P.append(page('p-u1', U1, 'must', 'المثال المضاد: الفكرة بالأرقام',
    idea('الجملة اللي تقول «لكل…» تطيح بقيمة وحدة تفشل عندها. هذي القيمة اسمها مثال مضاد.') +
    think('نبدأ بأرقام <span class="cap2">(مثال السلايدات 1)</span>',
          before='    <p>الجملة: «' + lt(r'For every real number \(x\), \((x^2 - 1)^2 \gt 0\)') + r'». يعني: لكل عدد حقيقي x، \((x^2-1)^2\) أكبر من صفر. نجرب:</p>' + '\n' +
          tbl([r'\(x\)', '0', '2', '3', '1'],
              [[r'\((x^2-1)^2\)', r'\((0-1)^2 = 1\)', r'\((4-1)^2 = 9\)', r'\((9-1)^2 = 64\)', r'\((1-1)^2 = 0\)'],
               ['أكبر من 0؟', OK, OK, OK, NO]], ltr=True),
          extra=r'    <p>ثلاث قيم مشت، بس عند \(x = 1\) طلع 0، و0 مو أكبر من 0. قيمة وحدة فشلت، فالجملة «لكل x» خاطئة.</p>' + '\n') +
    W([('1', 'احسب', r'For \(x = 1\), \((x^2 - 1)^2 = (1^2 - 1)^2 = 0\).', 'نكتب القيمة اللي فشلت، والحساب بالأرقام.'),
       ('2', 'احكم', r'Thus, \(x = 1\) is a counterexample.', r'إذن \(x = 1\) مثال مضاد، والجملة خاطئة.')], title='نكتب (حل السلايدات)') +
    stmt([(r'<span class="lb">Definition.</span> If the statement \(\forall x \in S, R(x)\) is false, then there exists some element \(x\) in the set \(S\) for which \(R(x)\) is false. Such an element \(x\) is called a <i>counterexample</i> of the false statement \(\forall x \in S, R(x)\).',
           r'لو الجملة «لكل x في S، \(R(x)\)» خاطئة، فلازم فيه عنصر x في S الجملة عنده خاطئة. هذا العنصر اسمه <b>مثال مضاد</b>.'),
          (r'<span class="lb">Definition.</span> If a statement \(P\) is shown to be false in some manner, then \(P\) is said to be <i>disproved</i>.',
           'لما تثبت أن جملة خاطئة، نقول إنك <b>نفيتها</b>. فكلمة ' + lt('Disprove') + ' في السؤال معناها: اثبت أنها خاطئة.')]) +
    card('بطاقة الخطوات: المثال المضاد', [
        ('جرّب', r'قيم من مجموعة السؤال بالترتيب، لين تلقى وحدة تفشل. جرّب 4 قيم على الأقل.'),
        ('احسب', 'واكتب القيمة والحساب بالأرقام: ' + lt(r'For \(x = \ldots\), …')),
        ('احكم', lt(r'Thus, \(x = \ldots\) is a counterexample.'))]), style='gap:3.1mm'))

# ---------- p-mid5 ----------
P.append(page('p-mid5', U[1], 'top', 'فخ أول قيمة: سؤال ميد 1447، وبعده دورك' + tag('past', 'ميد 1447 · درجتين'),
    qbox(r'<span class="lb">5.</span> For every odd positive integer \(n\), \(3 \mid (n^2 - 1)\). (2 marks)',
         r'لكل عدد فردي موجب n، العدد 3 يقسم \(n^2 - 1\). السؤال جا تحت «' + lt('Prove or disprove') + '»، يعني أنت تقرر: صح أو خطأ.') +
    think('نفكر', [r'نجرب الأعداد الفردية الموجبة بالترتيب. \(n = 1\): \(1^2 - 1 = 0\)، و3 يقسم 0 (لأن \(0 = 3 \times 0\)) ' + OK,
                   r'\(n = 3\): \(3^2 - 1 = 8\)، و3 ما يقسم 8 ' + NO,
                   r'لقينا قيمة تفشل، فالجملة خاطئة، و \(n = 3\) مثال مضاد.']) +
    W([('1', 'الحكم', 'False.', 'الجملة خاطئة.', dict(BKP, id='m-1447')),
       ('2', 'الحل الرسمي', r'Since \(3 \nmid 8\), so \(3 \nmid (3^2 - 1)\). It follows that \(n = 3\) is a counterexample.', r'3 ما يقسم 8، يعني ما يقسم \(3^2 - 1\). فـ \(n = 3\) مثال مضاد.')], title='نكتب (الحل الرسمي)') +
    note('trap', 'انتبه:', r'أول قيمة مشت! لو وقفت عند \(n = 1\) كان حكمت «صح» وراحت الدرجتين. جرّب 4 قيم على الأقل. والمثال لازم يكون من مجموعة السؤال: هنا فردي وموجب.') +
    duork('5.3', '<span class="lb">5.3.</span> ' + EX['5.3'],
          r'انفِ الجملة: لكل n من 1 إلى 5، العدد 3 يقسم \(2n^2 + 1\). كمّل الجدول، ووقّف عند أول قيمة تفشل.') +
    tbl([r'\(n\)', '1', '2', '3', '4', '5'],
        [[r'\(2n^2 + 1\)', '3', '9', ('', 'style="height:9mm"'), '', ''], ['3 يقسمه؟', OK, OK, ('', 'style="height:9mm"'), '', '']], ltr=True, style='table-layout:fixed').replace('    <table', '  <table').replace('    </table>', '  </table>') +
    W([('', 'الجواب', None, None, 'b2')], title=''), style='gap:3.2mm'))

# ---------- p-trap: the same trap in the girls' exam and the November exam ----------
def drow(n, en):
    return [n, (en, 'class="e"'), '', '']

P.append(page('p-trap', U[1], 'top', 'نفس الفخ في ميد البنات وميد نوفمبر' + tag('past', 'البنات · نوفمبر'),
    qbox(r'<span class="lb">3-</span> For every even positive integer \(n\), \(12 \mid (n^2 - 4)\). (2 marks)',
         r'لكل عدد زوجي موجب n، العدد 12 يقسم \(n^2 - 4\).', lab='سؤال ميد البنات · درجتين') +
    think('نفكر', before=tbl([r'\(n\)', '2', '4', '6'], [[r'\(n^2 - 4\)', '0', '12', '32'], ['12 يقسمه؟', OK, OK, NO]], ltr=True),
          extra='    <p>أول قيمتين مشت، والثالثة فشلت. اللي يوقف عند قيمتين يحكم «صح» ويخسر الدرجتين.</p>\n') +
    W([('', 'الجواب', r'False. For \(n = 6\), \(n^2 - 4 = 32\) and \(12 \nmid 32\). Thus, \(n = 6\) is a counterexample.', '', dict(BKP, id='m-girls'))], title='') +
    qbox(r'<span class="lb">1.</span> If \(n\) is an odd integer, then \(n^2 - n\) is odd.',
         r'إذا n فردي، فإن \(n^2 - n\) فردي. <b>نفكر:</b> المثال لازم يكون فردي (الشرط صح). \(n = 1\) يعطي 0، و \(n = 3\) يعطي 6، والاثنين زوجي ' + NO + r' كل القيم تفشل، لأن \(n^2 - n = n(n - 1)\) عددين ورا بعض، وواحد منهم زوجي. فالفخ هنا عكسي: شكلها «برهن»، وهي خاطئة.', lab='سؤال ميد نوفمبر · 3 درجات') +
    W([('', 'الجواب', r'False. For the odd integer \(n = 1\), the integer \(n^2 - n = 1^2 - 1 = 0\) is even. Thus, \(n = 1\) is a counterexample.', r'هذا حل الكتاب (مثال 5.6). و \(n = 3\) يمشي بعد: \(9 - 3 = 6\) زوجي.', dict(BKP, id='m-nov'))], title='') +
    hq('تدريب سرعة: لقِ أول قيمة تفشل (نفس الفخ بأرقام ثانية)', 'q-drill', 's-drill') +
    tbl([('', 'width:6%'), 'الجملة', ('أول قيمة تفشل', 'width:17%'), ('الحساب', 'width:24%')], [
        drow('1', r'For every odd positive integer \(n\), \(5 \mid (n^2 - 1)\).'),
        drow('2', r'For every even positive integer \(n\), \(8 \mid (n^2 + 4)\).'),
        drow('3', r'For every positive integer \(n\), \(2^n + 1\) is a prime number.'),
        drow('4', r'If \(n\) is an even integer, then \(n^2 + n\) is odd.')], cls='t drill').replace('    <table', '  <table').replace('    </table>', '  </table>') +
    note('trick', 'القاعدة:', 'جرّب 4 قيم على الأقل. ولو كل القيم فشلت (مثل نوفمبر)، اختر أسهل قيمة واكتب حسابها.'), style='gap:2.5mm'))

# ---------- p-ex2 ----------
P.append(page('p-ex2', U[1], 'must', 'مثال: قيمة تخلي الجملة بدون معنى' + tag('sol', 'مثال السلايدات 2') + tag('ex', 'دورك'),
    qbox(r'Disprove the statement: If \(x \in \mathbb{Z}\), then \(\dfrac{x^2 + x}{x^2 - x} = \dfrac{x + 1}{x - 1}\).',
         'انفِ الجملة: لكل عدد صحيح x، الكسرين متساويين.') +
    think('نفكر', [r'قبل ما تجرّب أرقام عشوائية، اسأل: فيه قيمة تخلي مقام صفر؟ المقام \(x^2 - x\) يصير صفر عند \(x = 0\).',
                   r'عند \(x = 0\): الكسر الأيسر ما له قيمة أصلاً (قسمة على صفر)، والأيمن \(\frac{0 + 1}{0 - 1} = -1\). شي ما له قيمة ما يساوي \(-1\).']) +
    W([('1', 'القيمة', r'If \(x = 0\), then \(x^2 - x = 0\) and so \(\frac{x^2 + x}{x^2 - x}\) is not defined.', r'عند \(x = 0\) المقام صفر، فالكسر الأيسر غير معرّف.'),
       ('2', 'احكم', r'On the other hand, if \(x = 0\), then \(\frac{x + 1}{x - 1} = -1\); so the expressions \(\frac{x^2 + x}{x^2 - x}\) and \(\frac{x + 1}{x - 1}\) are certainly not equal when \(x = 0\). Thus, \(x = 0\) is a counterexample to the statement.', r'والكسر الأيمن يساوي \(-1\)، فالطرفين مو متساويين. إذن \(x = 0\) مثال مضاد.')], title='نكتب (حل السلايدات)') +
    duork('5.2', '<span class="lb">5.2.</span> ' + EX['5.2'],
          r'انفِ الجملة: لكل n من 0 إلى 4، هذا العدد أولي (يعني ما يقبل القسمة إلا على 1 ونفسه). كمّل الجدول.') +
    tbl([r'\(n\)', '0', '1', '2', '3', '4'],
        [['القيمة', r'\(1 + 1 + 0 = 2\)', r'\(2 + 3 + 0 = 5\)', ('', 'style="height:9mm"'), '', ''], ['أولي؟', OK, OK, ('', 'style="height:9mm"'), '', '']], ltr=True, style='table-layout:fixed').replace('    <table', '  <table').replace('    </table>', '  </table>') +
    W([('', 'الجواب', None, None, 'b2')], title='') +
    hints(['<b>تلميح:</b> لا توقف عند أول ثلاث قيم. وجرّب تقسم آخر عدد يطلع لك على 11.']), style='gap:3.2mm'))

# ---------- p-ex3 ----------
P.append(page('p-ex3', U[1], 'must', 'مثال: جملة «إذا… فإن…»' + tag('sol', 'مثال السلايدات 3') + tag('ex', 'دورك'),
    qbox(r'Show that the statement “Let \(n \in \mathbb{Z}\). If \(4 \mid (n^2 - 1)\), then \(4 \mid (n - 1)\).” is false.',
         r'اثبت أن الجملة خاطئة: إذا 4 يقسم \(n^2 - 1\)، فإن 4 يقسم \(n - 1\).') +
    think('نفكر', before='    <p>في «إذا… فإن…» المثال المضاد لازم يحقق شيئين مع بعض: <b>الشرط صح، والنتيجة خطأ</b>.</p>\n' +
          tbl([(r'\(n\)', 'width:10%'), r'الشرط: \(4 \mid (n^2-1)\)', r'النتيجة: \(4 \mid (n-1)\)', 'ينفع مثال مضاد؟'],
              [['1', r'\(4 \mid 0\) ' + OK, r'\(4 \mid 0\) ' + OK, 'لا، النتيجة صح'],
               ['2', r'\(4 \nmid 3\) ' + NO, '—', 'لا، الشرط خطأ'],
               ['3', r'\(4 \mid 8\) ' + OK, r'\(4 \nmid 2\) ' + NO, '<b>نعم</b>']])) +
    W([('', 'الجواب', r'Since \(4 \mid (3^2 - 1)\) but \(4 \nmid (3 - 1)\), it follows that \(n = 3\) is a counterexample.',
        r'4 يقسم \(3^2 - 1 = 8\) (الشرط صح)، لكن 4 ما يقسم \(3 - 1 = 2\) (النتيجة خطأ). فـ \(n = 3\) مثال مضاد.')], title='نكتب (حل السلايدات)') +
    note('trap', 'انتبه:', r'القيمة اللي الشرط عندها خطأ (مثل \(n = 2\)) ما تنفع مثال مضاد أبداً، لأن الجملة ما تتكلم عنها.') +
    duork('5.4', '<span class="lb">5.4.</span> ' + EX['5.4'],
          r'انفِ الجملة: إذا \(n(n+1)/2\) فردي، فإن \((n+1)(n+2)/2\) فردي. (n عدد طبيعي: 1، 2، 3، …)') +
    tbl([(r'\(n\)', 'width:10%'), r'الشرط: \(\frac{n(n+1)}{2}\)', 'فردي؟', r'النتيجة: \(\frac{(n+1)(n+2)}{2}\)', 'فردي؟'],
        [['1', '1', OK, '3', OK + ' ما ينفع'], ['2', ('', 'style="height:9mm"'), '', '', ''], ['3', ('', 'style="height:9mm"'), '', '', '']]).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    W([('', 'الجواب', None, None, 'b2')], title='')))

# ---------- p-ex4 ----------
P.append(page('p-ex4', U[1], 'must', 'مثال: أكثر من متغير' + tag('sol', 'مثال السلايدات 4') + tag('ex', 'دورك'),
    qbox(r'Show that the statement “For positive integers \(a, b, c\), \(a^{b^c} = (a^b)^c\).” is false.',
         r'اثبت أن الجملة خاطئة: لكل أعداد صحيحة موجبة a و b و c، \(a^{b^c} = (a^b)^c\).') +
    think('نفكر', [r'الفرق: في \(a^{b^c}\) تحسب \(b^c\) أول وترفع a له. وفي \((a^b)^c\) تحسب \(a^b\) أول وترفعه لـ c.',
                   r'نجرب \(a = b = c = 2\): \(2^{2^2} = 2^4 = 16\) و \((2^2)^2 = 4^2 = 16\). متساويين، ما نفعت!',
                   r'نغيّر c: \(a = 2,\ b = 2,\ c = 3\): \(2^{2^3} = 2^8 = 256\) و \((2^2)^3 = 4^3 = 64\). مختلفين ' + NO + ' هذا المثال المضاد.']) +
    W([('1', 'احسب', r'Let \(a = 2\), \(b = 2\) and \(c = 3\). Then \(a^{b^c} = 2^{2^3} = 2^8 = 256\), while \((a^b)^c = (2^2)^3 = 4^3 = 64\).', 'نختار القيم، ونحسب كل طرف بالأرقام.'),
       ('2', 'احكم', r'Since \(256 \ne 64\), the positive integers \(a = 2\), \(b = 2\) and \(c = 3\) constitute a counterexample.', 'الطرفين مختلفين، فهذي القيم مثال مضاد.')], title='نكتب (حل السلايدات)') +
    duork('5.5', '<span class="lb">5.5.</span> ' + EX['5.5'],
          'انفِ الجملة: لكل عددين صحيحين موجبين a و b، المساواة صحيحة.') +
    tbl([(r'\((a, b)\)', 'width:14%'), r'الأيسر: \((a+b)^3\)', r'الأيمن: \(a^3 + 2a^2b + 2ab + 2ab^2 + b^3\)', ('متساويين؟', 'width:20%')],
        [[r'\((1, 1)\)', r'\(2^3 = 8\)', r'\(1 + 2 + 2 + 2 + 1 = 8\)', 'نعم، ما نفعت'], [r'\((1, 2)\)', ('', 'style="height:9mm"'), '', '']]).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    W([('', 'الجواب', None, None, 'b2')], title='') +
    hints(['<b>تريك:</b> لو فيه أكثر من متغير، لا تخليهم كلهم 1 ولا كلهم متساويين. القيم «الخاصة» تخبي الخطأ.']), style='gap:3.2mm'))

# ---------- p-book: the remaining examples of the book's section 5.1 ----------
P.append(page('p-book', U[1], 'cand', 'أمثلة الكتاب الباقية: مرشّحة للبديل' + tag('sol', 'أمثلة الكتاب 5.2 و5.5 و5.9'),
    idea('الميدات أخذت مثالين من أمثلة الكتاب في 5.1 بالحرف: 5.4 (ميد 1447) و5.6 (نوفمبر). هذي الثلاثة الباقية، وكل واحد على فكرة شفتها قبل. غطِّ «حل الكتاب»، حاول، وبعدها قارن.') +
    qbox(r'<span class="lb">Example 5.5.</span> Disprove the statement: Let \(n \in \mathbb{Z}\). If \(n^2 + 3n\) is even, then \(n\) is odd.',
         r'إذا \(n^2 + 3n\) زوجي، فإن n فردي. <b>الفكرة</b> ' + ref('p-ex3') + r': «إذا… فإن…»، فنبي الشرط صح والنتيجة خطأ، يعني n زوجي و \(n^2 + 3n\) زوجي. جرّب \(n = 2\).', lab='مثال الكتاب 5.5') +
    W([('', 'حل الكتاب', r'If \(n = 2\), then \(n^2 + 3n = 2^2 + 3 \cdot 2 = 10\) is even and 2 is even. Thus, \(n = 2\) is a counterexample.', 'الشرط صح (10 زوجي) والنتيجة خطأ (2 مو فردي). وأي عدد زوجي يمشي.')], title='') +
    qbox(r'<span class="lb">Example 5.2.</span> Disprove the statement: If \(x\) is a real number, then \(\tan^2 x + 1 = \sec^2 x\).',
         r'لكل عدد حقيقي x، \(\tan^2 x + 1 = \sec^2 x\). <b>الفكرة</b> ' + ref('p-ex2') + r': قيمة تخلي الطرفين بدون معنى. \(\tan x\) و \(\sec x\) غير معرّفين لما \(\cos x = 0\)، مثل \(x = \pi/2\).', lab='مثال الكتاب 5.2') +
    W([('', 'حل الكتاب', r'Since \(\tan x\) and \(\sec x\) are not defined when \(x = \pi/2\), it follows that \(\tan^2 x + 1\) and \(\sec^2 x\) have no numerical value when \(x = \pi/2\) and, consequently, \(\tan^2 x + 1\) and \(\sec^2 x\) are not equal when \(x = \pi/2\). That is, \(x = \pi/2\) is a counterexample to the statement.', '')], title='') +
    qbox(r'<span class="lb">Example 5.9.</span> Show that the statement: Let \(a\) and \(b\) be nonzero real numbers. If \(x, y \in \mathbb{R}^+\), then \(\dfrac{a^2}{2b^2}x^2 + \dfrac{b^2}{2a^2}y^2 \gt xy\) is false.',
         r'a و b حقيقيين مو صفر، و x و y موجبين. <b>الفكرة</b> ' + ref('p-ex4') + r': أكثر من متغير، فاختر قيم «ذكية» تخلي الحدين متساويين. لو \(x = b^2\) و \(y = a^2\)، كل حد يصير \(a^2b^2/2\)، والمجموع يساوي xy بالضبط، مو أكبر.', lab='مثال الكتاب 5.9') +
    W([('', 'حل الكتاب', r'Let \(x = b^2\) and \(y = a^2\). Then \(\frac{a^2}{2b^2}x^2 + \frac{b^2}{2a^2}y^2 = \frac{a^2b^2}{2} + \frac{a^2b^2}{2} = a^2b^2 = xy\). Thus, \(x = b^2\) and \(y = a^2\) is a counterexample and so the inequality is false.', '')], title=''), style='gap:2.8mm'))

# ---------- p-s1 ----------
P.append(page('p-s1', 'حلول الوحدة 1', '', 'الحلول' + tag('sol', 'شيّك'),
    W([('5.2', '', r'Let \(n = 4\). Then \(2^4 + 3^4 + 4 \cdot 3 \cdot 2 = 16 + 81 + 24 = 121 = 11 \cdot 11\), which is not a prime number. Thus, \(n = 4\) is a counterexample.',
        r'القيم من 0 إلى 3 تعطي 2 و5 و13 و41، وكلها أولية. بس عند \(n = 4\) يطلع 121، وهو \(11 \times 11\).', SM('52')),
       ('5.4', '', r'Let \(n = 2\). Then \(\frac{n(n+1)}{2} = 3\) is odd, but \(\frac{(n+1)(n+2)}{2} = 6\) is even. Thus, \(n = 2\) is a counterexample.',
        r'عند \(n = 2\) الشرط صح (3 فردي) والنتيجة خطأ (6 زوجي). أما \(n = 3\) فالشرط عندها خطأ (6 زوجي)، فما تنفع.', SM('54')),
       ('5.5', '', r'Let \(a = 1\) and \(b = 2\). Then \((a + b)^3 = 3^3 = 27\), while \(a^3 + 2a^2b + 2ab + 2ab^2 + b^3 = 1 + 4 + 4 + 8 + 8 = 25\). Since \(27 \ne 25\), \(a = 1\) and \(b = 2\) constitute a counterexample.',
        r'الأيسر 27 والأيمن 25. (\(a = b = 1\) ما تنفع، لأن الطرفين 8.)', SM('55')),
       ('5.3', '', r'Let \(n = 3\). Then \(2n^2 + 1 = 2 \cdot 9 + 1 = 19\) and \(3 \nmid 19\). Thus, \(n = 3\) is a counterexample.',
        'القيم بالترتيب: 3، 9، 19، 33، 51. كلها تقبل القسمة على 3 إلا 19.', SM('53'))], title='') +
    sh('تدريب السرعة: الأجوبة', 's-drill', [('q-drill', 'السؤال')]) +
    tbl(['', 'أول قيمة تفشل', 'الحساب'], [
        ['1', r'\(n = 3\)', r'\(3^2 - 1 = 8\)، و5 ما يقسم 8'],
        ['2', r'\(n = 4\)', r'\(16 + 4 = 20\)، و8 ما يقسم 20'],
        ['3', r'\(n = 3\)', r'\(2^3 + 1 = 9 = 3 \times 3\)، مو أولي'],
        ['4', r'\(n = 2\)', r'\(4 + 2 = 6\) زوجي. أي زوجي يمشي']]).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    box('خمس تريكات للمثال المضاد', r'''    <ol>
      <li>ابدأ بالقيم السهلة: 0، 1، \(-1\)، 2، 3، وجرّب 4 قيم على الأقل. في الاختبارات أول قيمة أو قيمتين ممكن يمشون.</li>
      <li>دوّر قيمة تخلي مقام صفر، يعني تخلي الجملة بدون معنى.</li>
      <li>في «إذا… فإن…»: الشرط صح والنتيجة خطأ. جهّز جدول فيه عمود لكل واحد.</li>
      <li>لو فيه أكثر من متغير، لا تخليهم متساويين.</li>
      <li>لا تكتب «الجملة خاطئة» وتسكت. اكتب القيمة، والحساب، وكلمة ''' + lt('counterexample') + r'''.</li>
    </ol>
'''), sol=True))

ORDER = ['p-cover', 'p-u1', 'p-ex2', 'p-ex3', 'p-ex4', 'p-mid5', 'p-trap', 'p-book', 'p-s1']
P.sort(key=lambda h: ORDER.index(re.search(r'id="([^"]+)"', h).group(1)))
save('b_u1.html', P)
