import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *

def toc_row(u, kind, words, ex, pid):
    return ['<b>' + u + '</b>', (kind, 'class="s"'), (words, 'class="s"'), ex, ref(pid)]

cover = r'''<section class="page cover" id="p-cover">
  <div class="hdr"><span class="u">131 ريض · الميد الثاني</span><span class="pn"></span></div>
  <div>
    <p class="kicker">ملزمة الفصل 5 · الأقسام 5.1 إلى 5.5</p>
    <h1>الوجود والبرهان بالتناقض</h1>
    <p class="sub">الفصل كله خمس أنواع أسئلة. لكل نوع: بطاقة خطوات، وأمثلة محلولة سطر بسطر، وبعد كل مثال تمرين من نفس نوعه تحله بنفس الخطوات.</p>
  </div>
  <div class="box">
    <h3>كيف تستخدمها</h3>
    <ol>
      <li>امشِ بالترتيب. كل وحدة تبدأ بـ«بطاقة خطوات» فيها ثلاث خطوات تحفظها.</li>
      <li>كل مثال يمشي كذا: السؤال، ثم نفكر بالأرقام، ثم نكتب الجواب وتحت كل سطر معناه.</li>
      <li>بعد المثال يجي «دورك»: تمرين من نفس النوع. غطِّ المثال وحلّه، وبعدها شيّك من الحلول.</li>
      <li>مستعجل؟ امشِ على الصفحات اللي فوقها «أساسي» بس.</li>
    </ol>
  </div>
  <div class="box">
    <h3>خريطة الملزمة: خمس أنواع أسئلة</h3>
''' + tbl([('الوحدة', 'width:9%'), ('نوع السؤال', 'width:19%'), 'كيف يجي في الاختبار', ('تمارين الخطة', 'width:21%'), ('الصفحة', 'width:9%')], [
    toc_row('1', 'مثال مضاد', lt('Disprove: For every …') + ' أو ' + lt('If …, then …'), '5.2 · 5.3 · 5.4 · 5.5', 'p-u1'),
    toc_row('2', 'برهان بالتناقض', lt('Prove: There is no …') + ' أو ' + lt('… is irrational'), '5.12 · 5.18 · 5.21 · 5.33', 'p-u2'),
    toc_row('3', 'ثلاث طرق للبرهان', lt('Prove … by a direct proof, …'), '5.36 · 5.39', 'p-u3'),
    toc_row('4', 'برهان الوجود', lt('Prove: There exists …'), '5.42 · 5.46 · 5.51 · 5.53', 'p-u4'),
    toc_row('5', 'نفي الوجود', lt('Disprove: There exists …'), '5.55 · 5.57', 'p-u5'),
    toc_row('6', 'تدريب الاختبار', 'أي طريقة؟ · جمل الكتابة · اختبار قصير · ورقة ليلة الاختبار', '—', 'p-which'),
], cls='t toc') + r'''  </div>
  <div class="grid2">
    <div class="box">
      <h3>أسئلة الاختبارات السابقة</h3>
      <ul class="chk">
        <li><span class="cb"></span>ما فيه أصغر عدد موجب · ميد 1447 <span class="pg ref" data-to="p-ex5"></span></li>
        <li><span class="cb"></span>مثال مضاد · ميد 1447 <span class="pg ref" data-to="p-mid5"></span></li>
        <li><span class="cb"></span>\(\sqrt[3]{7}\) غير نسبي · نهائي 1446 <span class="pg ref" data-to="p-rt3"></span></li>
      </ul>
    </div>
    <div class="box">
      <h3>خطة المذاكرة</h3>
      <p style="font-size:11pt"><b>الجلسة 1:</b> الوحدتين 1 و2. تقريباً ساعتين وربع.</p>
      <p style="font-size:11pt"><b>الجلسة 2:</b> الوحدات 3 و4 و5. تقريباً ساعتين ونص.</p>
      <p style="font-size:11pt"><b>قبل الاختبار:</b> الوحدة 6. تقريباً ساعة.</p>
    </div>
  </div>
  <div class="box">
    <h3>ألوان الصفحات</h3>
    <p style="font-size:11pt"><span style="color:var(--acc);font-weight:700">■ أخضر:</span> شرح ومثال محلول &nbsp;·&nbsp; <span style="color:#2f5fa8;font-weight:700">■ أزرق:</span> مثال وبعده تمرين تحله &nbsp;·&nbsp; <span style="color:#b47a00;font-weight:700">■ ذهبي:</span> سؤال اختبار سابق &nbsp;·&nbsp; <span style="color:#8a959c;font-weight:700">■ رمادي:</span> حلول</p>
  </div>
  <p class="small">ليش هالفصل مهم: في ميد 1447 جا منه سؤالين (5 درجات من 25)، والاثنين من أمثلة الكتاب بالحرف. علقت بكلمة إنجليزية؟ شوف <span class="ref" data-to="p-phr"></span>.</p>
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
        ('جرّب', r'قيم من المجموعة اللي في السؤال، لين تلقى وحدة تفشل. ابدأ بـ 0 و1 و\(-1\) و2.'),
        ('احسب', 'واكتب القيمة والحساب بالأرقام: ' + lt(r'For \(x = \ldots\), …')),
        ('احكم', lt(r'Thus, \(x = \ldots\) is a counterexample.'))]), style='gap:3.1mm'))

# ---------- p-mid5 ----------
P.append(page('p-mid5', U[1], 'must', 'سؤال ميد 1447، وبعده دورك' + tag('past', 'ميد 1447 · درجتين'),
    qbox(r'<span class="lb">5.</span> For every odd positive integer \(n\), \(3 \mid (n^2 - 1)\). (2 marks)',
         r'لكل عدد فردي موجب n، العدد 3 يقسم \(n^2 - 1\). السؤال جا تحت «' + lt('Prove or disprove') + '»، يعني أنت تقرر: صح أو خطأ.') +
    think('نفكر', [r'نجرب الأعداد الفردية الموجبة بالترتيب. \(n = 1\): \(1^2 - 1 = 0\)، و3 يقسم 0 (لأن \(0 = 3 \times 0\)) ' + OK,
                   r'\(n = 3\): \(3^2 - 1 = 8\)، و3 ما يقسم 8 ' + NO,
                   r'لقينا قيمة تفشل، فالجملة خاطئة، و \(n = 3\) مثال مضاد.']) +
    W([('1', 'الحكم', 'False.', 'الجملة خاطئة.'),
       ('2', 'الحل الرسمي', r'Since \(3 \nmid 8\), so \(3 \nmid (3^2 - 1)\). It follows that \(n = 3\) is a counterexample.', r'3 ما يقسم 8، يعني ما يقسم \(3^2 - 1\). فـ \(n = 3\) مثال مضاد.')], title='نكتب (الحل الرسمي)') +
    note('trap', 'انتبه:', r'أول قيمة مشت! لو وقفت عند \(n = 1\) كان حكمت «صح» وراحت الدرجتين. جرّب ثلاث قيم على الأقل. والمثال لازم يكون من مجموعة السؤال: هنا فردي وموجب.') +
    duork('5.3', r'<span class="lb">5.3.</span> Disprove the statement: If \(n \in \{1, 2, 3, 4, 5\}\), then \(3 \mid (2n^2 + 1)\).',
          r'انفِ الجملة: لكل n من 1 إلى 5، العدد 3 يقسم \(2n^2 + 1\). كمّل الجدول، ووقّف عند أول قيمة تفشل.') +
    tbl([r'\(n\)', '1', '2', '3', '4', '5'],
        [[r'\(2n^2 + 1\)', '3', '9', ('', 'style="height:9mm"'), '', ''], ['3 يقسمه؟', OK, OK, ('', 'style="height:9mm"'), '', '']], ltr=True, style='table-layout:fixed').replace('    <table', '  <table').replace('    </table>', '  </table>') +
    W([('', 'الجواب', None, None, 'b2')], title=''), style='gap:3.2mm'))

# ---------- p-ex2 ----------
P.append(page('p-ex2', U[1], 'must', 'مثال: قيمة تخلي الجملة بدون معنى' + tag('sol', 'مثال السلايدات 2') + tag('ex', 'دورك'),
    qbox(r'Disprove the statement: If \(x \in \mathbb{Z}\), then \(\dfrac{x^2 + x}{x^2 - x} = \dfrac{x + 1}{x - 1}\).',
         'انفِ الجملة: لكل عدد صحيح x، الكسرين متساويين.') +
    think('نفكر', [r'قبل ما تجرّب أرقام عشوائية، اسأل: فيه قيمة تخلي مقام صفر؟ المقام \(x^2 - x\) يصير صفر عند \(x = 0\).',
                   r'عند \(x = 0\): الكسر الأيسر ما له قيمة أصلاً (قسمة على صفر)، والأيمن \(\frac{0 + 1}{0 - 1} = -1\). شي ما له قيمة ما يساوي \(-1\).']) +
    W([('1', 'القيمة', r'If \(x = 0\), then \(x^2 - x = 0\) and so \(\frac{x^2 + x}{x^2 - x}\) is not defined.', r'عند \(x = 0\) المقام صفر، فالكسر الأيسر غير معرّف.'),
       ('2', 'احكم', r'On the other hand, if \(x = 0\), then \(\frac{x + 1}{x - 1} = -1\); so the expressions \(\frac{x^2 + x}{x^2 - x}\) and \(\frac{x + 1}{x - 1}\) are certainly not equal when \(x = 0\). Thus, \(x = 0\) is a counterexample to the statement.', r'والكسر الأيمن يساوي \(-1\)، فالطرفين مو متساويين. إذن \(x = 0\) مثال مضاد.')], title='نكتب (حل السلايدات)') +
    duork('5.2', r'<span class="lb">5.2.</span> Disprove the statement: If \(n \in \{0, 1, 2, 3, 4\}\), then \(2^n + 3^n + n(n-1)(n-2)\) is a prime number.',
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
    duork('5.4', r'<span class="lb">5.4.</span> Disprove the statement: Let \(n \in \mathbb{N}\). If \(\frac{n(n+1)}{2}\) is odd, then \(\frac{(n+1)(n+2)}{2}\) is odd.',
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
    duork('5.5', r'<span class="lb">5.5.</span> Disprove the statement: For every two positive integers \(a\) and \(b\), \((a + b)^3 = a^3 + 2a^2b + 2ab + 2ab^2 + b^3\).',
          'انفِ الجملة: لكل عددين صحيحين موجبين a و b، المساواة صحيحة.') +
    tbl([(r'\((a, b)\)', 'width:14%'), r'الأيسر: \((a+b)^3\)', r'الأيمن: \(a^3 + 2a^2b + 2ab + 2ab^2 + b^3\)', ('متساويين؟', 'width:20%')],
        [[r'\((1, 1)\)', r'\(2^3 = 8\)', r'\(1 + 2 + 2 + 2 + 1 = 8\)', 'نعم، ما نفعت'], [r'\((1, 2)\)', ('', 'style="height:9mm"'), '', '']]).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    W([('', 'الجواب', None, None, 'b2')], title='') +
    hints(['<b>تريك:</b> لو فيه أكثر من متغير، لا تخليهم كلهم 1 ولا كلهم متساويين. القيم «الخاصة» تخبي الخطأ.']), style='gap:3.2mm'))

# ---------- p-s1 ----------
P.append(page('p-s1', 'حلول الوحدة 1', '', 'الحلول' + tag('sol', 'شيّك'),
    W([('5.3', '', r'Let \(n = 3\). Then \(2n^2 + 1 = 2 \cdot 9 + 1 = 19\) and \(3 \nmid 19\). Thus, \(n = 3\) is a counterexample.',
        'القيم بالترتيب: 3، 9، 19، 33، 51. كلها تقبل القسمة على 3 إلا 19.'),
       ('5.2', '', r'Let \(n = 4\). Then \(2^4 + 3^4 + 4 \cdot 3 \cdot 2 = 16 + 81 + 24 = 121 = 11 \cdot 11\), which is not a prime number. Thus, \(n = 4\) is a counterexample.',
        r'القيم من 0 إلى 3 تعطي 2 و5 و13 و41، وكلها أولية. بس عند \(n = 4\) يطلع 121، وهو \(11 \times 11\).'),
       ('5.4', '', r'Let \(n = 2\). Then \(\frac{n(n+1)}{2} = 3\) is odd, but \(\frac{(n+1)(n+2)}{2} = 6\) is even. Thus, \(n = 2\) is a counterexample.',
        r'عند \(n = 2\) الشرط صح (3 فردي) والنتيجة خطأ (6 زوجي). أما \(n = 3\) فالشرط عندها خطأ (6 زوجي)، فما تنفع.'),
       ('5.5', '', r'Let \(a = 1\) and \(b = 2\). Then \((a + b)^3 = 3^3 = 27\), while \(a^3 + 2a^2b + 2ab + 2ab^2 + b^3 = 1 + 4 + 4 + 8 + 8 = 25\). Since \(27 \ne 25\), \(a = 1\) and \(b = 2\) constitute a counterexample.',
        r'الأيسر 27 والأيمن 25. (\(a = b = 1\) ما تنفع، لأن الطرفين 8.)')], title='') +
    box('خمس تريكات للمثال المضاد', r'''    <ol>
      <li>ابدأ بالقيم السهلة: 0، 1، \(-1\)، 2، 3. أغلب الأمثلة المضادة في الكتاب منها.</li>
      <li>دوّر قيمة تخلي مقام صفر، يعني تخلي الجملة بدون معنى.</li>
      <li>في «إذا… فإن…»: الشرط صح والنتيجة خطأ. جهّز جدول فيه عمود لكل واحد.</li>
      <li>لو فيه أكثر من متغير، لا تخليهم متساويين.</li>
      <li>لا تكتب «الجملة خاطئة» وتسكت. اكتب القيمة، والحساب، وكلمة ''' + lt('counterexample') + r'''.</li>
    </ol>
''') +
    box('راجع نفسك (دقيقتين)', '''    <ul class="chk">
      <li><span class="cb"></span>أقول الخطوات الثلاث من ذاكرتي: جرّب، احسب، احكم.</li>
      <li><span class="cb"></span>أعرف الشرطين في مثال مضاد لجملة «إذا… فإن…».</li>
      <li><span class="cb"></span>أكتب جملة الحكم بالإنجليزي بدون ما أطالع.</li>
    </ul>
'''), sol=True))

save('b_u1.html', P)
