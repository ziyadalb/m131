import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
P = []

# ---------- p-which ----------
def wrow(n, en):
    return ('    <div class="tf"><span>' + str(n) + '.</span><span>' + en +
            '</span><span class="o">النوع: <span class="blank s"></span></span></div>\n')

P.append(page('p-which', U[6], 'must', 'أي طريقة؟ درّب عينك',
    idea('أهم خطوة: تعرف نوع السؤال من كلماته، وبعدها تطلع البطاقة حقته.') +
    tbl([('في السؤال', 'width:38%'), ('النوع', 'width:17%'), 'أول سطر', ('البطاقة', 'width:10%')], [
        [(lt('Disprove: For every …') + ' أو ' + lt('If …, then …'), 'class="s"'), '1. مثال مضاد', lt(r'Let \(x = \ldots\)'), ref('p-u1')],
        [(lt('Prove: There is no …') + ' أو ' + lt('… is irrational'), 'class="s"'), '2. تناقض', lt('Assume, to the contrary, …'), ref('p-u2')],
        [(lt('Prove … by (a) a direct proof, …'), 'class="s"'), '3. ثلاث طرق', 'حسب الطريقة', ref('p-u3')],
        [(lt('Prove: There exist(s) …'), 'class="s"'), '4. وجود', lt('Let … / Consider …'), ref('p-u4')],
        [(lt('Disprove: There exist(s) …'), 'class="s"'), '5. نفي وجود', lt('We show that if …, then …'), ref('p-u5')]]).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    note('star', lt('Prove or disprove') + '؟', 'جرّب ثلاث قيم أول. «لكل» وفشلت قيمة: <b>False</b> + مثال مضاد. «يوجد» ولقيت مثال: <b>True</b> + المثال. غير كذا برهن بالطريقة اللي في الجدول.') +
    '  <h3>دورك: اكتب رقم النوع (1 إلى 5) جنب كل جملة، بدون حل</h3>\n' +
    '  <div class="paper" style="--tfp:1.3mm">\n' +
    wrow(1, r'Disprove: For every real number \(x\), \(x^2 \ge x\).') +
    wrow(2, r'Prove that \(\sqrt{7}\) is irrational.') +
    wrow(3, r'Prove that there exist positive integers \(a\) and \(b\) such that \(a^2 + b^2 = 25\).') +
    wrow(4, r'Disprove: There exists an even integer \(n\) such that \(n^2 + 1\) is even.') +
    wrow(5, r'Prove that there is no largest even integer.') +
    wrow(6, r'Disprove: If \(n\) is a prime, then \(n\) is odd.') +
    wrow(7, r'Show that the equation \(x^3 - x - 1 = 0\) has a real number solution between \(x = 1\) and \(x = 2\).') +
    wrow(8, r'Prove that if \(5n + 2\) is odd, then \(n\) is odd, by (a) a direct proof and (b) a proof by contrapositive.') +
    '  </div>\n' +
    '  <p class="small">الأجوبة (غطّها قبل ما تحل). أمثلة: في 1 \\(x = 1/2\\)، وفي 3 \\(a = 3\\) و \\(b = 4\\)، وفي 6 \\(n = 2\\).</p>\n' +
    tbl(['الجملة', '1', '2', '3', '4', '5', '6', '7', '8'], [['النوع', '1', '2', '4', '5', '2', '1', '4', '3']], style='font-size:9.6pt').replace('    <table', '  <table').replace('    </table>', '  </table>'), style='gap:3mm'))

# ---------- p-phr: writing phrases and shortcuts ----------
def prow(en, ar):
    return '    <tr><td class="a">' + ar + '</td><td class="e">' + en + '</td></tr>\n'

P.append(page('p-phr', U[6], 'must', 'جمل الكتابة والاختصارات',
    idea('هذي الجمل تتكرر في كل حلول الفصل. احفظها كقطع جاهزة، وكتابتك بتصير أسرع وأوضح للمصحح.') +
    '  <table class="bi">\n    <tr><th>متى تستخدمها، ومعناها</th><th>الجملة</th></tr>\n' +
    prow('Assume, to the contrary, that …', 'أول سطر في التناقض: نفترض العكس.') +
    prow('This is a contradiction. / …, which is impossible.', 'آخر سطر في التناقض: وهذا تناقض / وهذا مستحيل.') +
    prow(r'Thus, \(x = \ldots\) is a counterexample.', 'آخر سطر في المثال المضاد.') +
    prow(r'Then \(n = 2k + 1\) for some integer \(k\).', 'تحويل «فردي» لمعادلة: لعدد صحيح ما k.') +
    prow('Since … is an integer, … is even.', 'بعد ما تطلّع 2 عامل مشترك.') +
    prow(r'We may assume that \(a/b\) has been reduced to lowest terms.', 'في «غير نسبي»: الكسر في أبسط صورة.') +
    prow('Without loss of generality, assume that …', 'حالتين متشابهتين، تكتب وحدة بس (مثل x و y في 5.33).') +
    prow('We consider two cases. Case 1. … Case 2. …', 'البرهان بالحالات.') +
    prow(r'Let \(x = \ldots\). / Consider …', 'برهان الوجود: تعيّن الشي.') +
    prow('by the Intermediate Value Theorem of Calculus', 'وجود حل بدون ما تعرف قيمته.') +
    prow('We show that if …, then …', 'أول سطر في نفي الوجود.') +
    prow('Hence / Therefore / It follows that …', 'إذن / لذلك / ينتج أن.') +
    '  </table>\n' +
    '  <div class="grid2">\n' +
    box('اختصارات مقبولة', r'''    <ul>
      <li>الرموز: \(\mathbb{Z}\) و \(\mathbb{Q}\) و \(\mathbb{R}\) و \(\in\) و \(\mid\) و \(\nmid\) و \(\Rightarrow\).</li>
      <li>''' + lt('WLOG') + ' بدل ' + lt('Without loss of generality') + r'''.</li>
      <li>''' + lt('iff') + ' بدل ' + lt('if and only if') + r'''.</li>
    </ul>
''').replace('  <div class="box">', '    <div class="box">') +
    box('أشياء تنقص درجات', '''    <ul>
      <li>False بدون مثال محسوب.</li>
      <li>تبدأ البرهان من المطلوب.</li>
      <li>تنسى «''' + lt('lowest terms') + '''».</li>
      <li>«''' + lt('for every k') + '» بدل «' + lt('for some integer k') + '''».</li>
      <li>مثال مضاد من برا المجموعة.</li>
      <li>تنفي «يوجد» بمثال واحد.</li>
    </ul>
''').replace('  <div class="box">', '    <div class="box">') +
    '  </div>\n'))

# ---------- p-mock ----------
P.append(page('p-mock', U[6], 'must', 'اختبار قصير على الفصل' + tag('ex', '30 دقيقة'),
    idea('نفس صيغة ميد 1447. شغّل مؤقت 30 دقيقة، وحل على ورقة أو صفحات فاضية. لا تفتح الحلول قبل ما يخلص الوقت.') +
    r'''  <div class="box paper">
    <div class="qrow" style="direction:ltr"><span class="en"><b>Q: Prove or disprove the following:</b></span><span class="mk">15 marks</span></div>
    <div class="q">1. For every positive integer \(n\), \(2^n + 1\) is a prime number. <span class="mk">(2 marks)</span></div>
    <div class="q">2. There is no smallest positive rational number. <span class="mk">(3 marks)</span></div>
    <div class="q">3. The real number \(\sqrt{5}\) is irrational. <span class="mk">(3 marks)</span></div>
    <div class="q">4. There exists an integer \(n\) such that \(n^2 + n + 1\) is even. <span class="mk">(3 marks)</span></div>
    <div class="q">5. The equation \(x^3 + x - 1 = 0\) has a unique real number solution between \(x = 0\) and \(x = 1\). <span class="mk">(4 marks)</span></div>
  </div>
''' +
    box('بعد ما تخلص', '''    <ul class="chk">
      <li><span class="cb"></span>كل فقرة بدأت بسطر الحكم: True أو False.</li>
      <li><span class="cb"></span>في False كتبت القيمة والحساب، أو برهان لكل n (لو الجملة «يوجد»).</li>
      <li><span class="cb"></span>في التناقض بدأت بـ ''' + lt('Assume, to the contrary') + '''.</li>
      <li><span class="cb"></span>في «حل وحيد» كتبت الوجود والوحدانية.</li>
    </ul>
''') +
    '  <div class="space" data-label="ملاحظات: وش الفقرة اللي أخذت منك وقت أكثر؟"></div>\n'))

# ---------- p-mocks ----------
P.append(page('p-mocks', 'حلول الوحدة 6', '', 'حلول الاختبار القصير' + tag('sol', 'شيّك'),
    W([('1. False', '', r'Let \(n = 3\). Then \(2^3 + 1 = 9 = 3 \cdot 3\), which is not a prime. Thus, \(n = 3\) is a counterexample.',
        r'\(n = 1\) و \(n = 2\) يعطون 3 و5 (أوليين). أول قيمة تفشل \(n = 3\).'),
       ('2. True', '', r'Assume, to the contrary, that there is a smallest positive rational number, say \(r\). Then \(r = a/b\) for some integers \(a\) and \(b\) with \(b \ne 0\), and so \(r/2 = a/(2b)\) is a positive rational number. Since \(0 \lt r/2 \lt r\), this is a contradiction.',
        'نفس سؤال ميد 1447، ومعه سطر «ليش r/2 نسبي».'),
       ('3. True', '', r'Assume, to the contrary, that \(\sqrt{5}\) is rational. Then \(\sqrt{5} = a/b\), where \(a, b \in \mathbb{Z}\), \(b \ne 0\) and \(a/b\) has been reduced to lowest terms. Then \(a^2 = 5b^2\). Thus \(5 \mid a^2\), and since 5 is a prime, \(5 \mid a\). So \(a = 5c\) for some \(c \in \mathbb{Z}\), and \(25c^2 = 5b^2\), that is, \(b^2 = 5c^2\). Thus \(5 \mid b^2\), and so \(5 \mid b\). Since \(5 \mid a\) and \(5 \mid b\), this is a contradiction since \(a/b\) has been reduced to lowest terms.',
        r'قالب \(\sqrt{2}\) نفسه، و«زوجي» صارت «يقبل القسمة على 5».'),
       ('4. False', '', r'We show that if \(n \in \mathbb{Z}\), then \(n^2 + n + 1\) is odd. <i>Case 1.</i> \(n = 2k\) for some \(k \in \mathbb{Z}\). Then \(n^2 + n + 1 = 4k^2 + 2k + 1 = 2(2k^2 + k) + 1\), which is odd. <i>Case 2.</i> \(n = 2k + 1\) for some \(k \in \mathbb{Z}\). Then \(n^2 + n + 1 = 4k^2 + 6k + 3 = 2(2k^2 + 3k + 1) + 1\), which is odd. Hence there is no integer \(n\) such that \(n^2 + n + 1\) is even.',
        'نفي وجود بالحالات، مثل مثال 15.'),
       ('5. True', '', r'Let \(f(x) = x^3 + x - 1\). Since \(f\) is a polynomial, it is continuous on \([0, 1]\). Since \(f(0) = -1\) and \(f(1) = 1\), it follows by the Intermediate Value Theorem of Calculus that there is \(c \in (0, 1)\) with \(f(c) = 0\). For uniqueness, assume, to the contrary, that there are two solutions \(a\) and \(b\) with \(0 \lt a \lt b \lt 1\). Then \(a^3 \lt b^3\) and \(a \lt b\), so \(0 = a^3 + a - 1 \lt b^3 + b - 1 = 0\), which is a contradiction.',
        'الوجود بالقيمة الوسطى، والوحدانية بالتناقض، مثل مثالي 11 و12.')], title='') +
    r'''  <h3>صحّح نفسك</h3>
  <table class="t">
    <tr><th>السؤال</th><th>النوع</th><th>الدرجة</th><th>درجتي</th><th>لو نقصت، ارجع لـ</th></tr>
    <tr><td>1</td><td>مثال مضاد</td><td>2</td><td></td><td>سؤال الميد <span class="ref" data-to="p-mid5"></span></td></tr>
    <tr><td>2</td><td>تناقض</td><td>3</td><td></td><td>سؤال الميد <span class="ref" data-to="p-ex5"></span></td></tr>
    <tr><td>3</td><td>غير نسبي</td><td>3</td><td></td><td>\(\sqrt{2}\) <span class="ref" data-to="p-rt2b"></span></td></tr>
    <tr><td>4</td><td>نفي وجود</td><td>3</td><td></td><td>مثال 15 <span class="ref" data-to="p-ex15"></span></td></tr>
    <tr><td>5</td><td>وجود ووحدانية</td><td>4</td><td></td><td>مثالا 11 و12 <span class="ref" data-to="p-ivt"></span></td></tr>
    <tr><th colspan="2">المجموع</th><th>15</th><th></th><th></th></tr>
  </table>
''', sol=True))

# ---------- p-night ----------
P.append(page('p-night', 'ورقة ليلة الاختبار', 'must', 'الفصل كله في صفحة',
    '  <div class="grid2">\n' +
    box('البطاقات الخمس', r'''    <ol>
      <li><b>مثال مضاد:</b> جرّب ← احسب ← احكم.</li>
      <li><b>تناقض:</b> نعكس ← نمشي ← تناقض.</li>
      <li><b>ثلاث طرق:</b> مباشر: افترض P ووصّل لـ Q. عكس النقيض: افترض عكس Q ووصّل لعكس P. تناقض: افترض P وعكس Q ووصّل لمستحيل.</li>
      <li><b>وجود:</b> اختر ← تحقق ← اختم.</li>
      <li><b>نفي وجود:</b> اقلب ← خذ أي x ← اثبت.</li>
    </ol>
''').replace('  <div class="box">', '    <div class="box">') +
    box('خريطة القرار', r'''    <ul>
      <li>''' + lt('Disprove + For every') + r''' ← 1</li>
      <li>''' + lt('Prove + There is no / irrational') + r''' ← 2</li>
      <li>''' + lt('Prove … by (a), (b), (c)') + r''' ← 3</li>
      <li>''' + lt('Prove + There exists') + r''' ← 4</li>
      <li>''' + lt('Disprove + There exists') + r''' ← 5</li>
      <li>''' + lt('Prove or disprove') + r''': جرّب ثلاث قيم أول.</li>
    </ul>
''').replace('  <div class="box">', '    <div class="box">') +
    '  </div>\n' +
    box(r'قالب «غير نسبي» (\(\sqrt{2}\) و \(\sqrt{3}\) و \(\sqrt[3]{7}\))', chain([r'\(a/b\) في أبسط صورة', 'ربّع (أو كعّب)', 'p يقسم a', r'\(a = pc\) وعوّض', 'p يقسم b', 'تناقض مع أبسط صورة'])) +
    '  <div class="grid2">\n' +
    box('الفخاخ', r'''    <ul>
      <li>أول قيمة ممكن تمشي. جرّب ثلاث.</li>
      <li>في «إذا… فإن…»: المثال المضاد الشرط فيه صح والنتيجة خطأ.</li>
      <li>عكس «و» هو «أو».</li>
      <li>لا تنسَ «''' + lt('lowest terms') + r'''».</li>
      <li>«يوجد» ما تنقض بمثال.</li>
      <li>«حل وحيد» = وجود + وحدانية.</li>
    </ul>
''').replace('  <div class="box">', '    <div class="box">') +
    box('أسئلة الاختبارات السابقة', r'''    <ul class="chk">
      <li><span class="cb"></span>ما فيه أصغر عدد موجب · ميد 1447 <span class="pg ref" data-to="p-ex5"></span></li>
      <li><span class="cb"></span>مثال مضاد لـ \(3 \mid (n^2 - 1)\) · ميد 1447 <span class="pg ref" data-to="p-mid5"></span></li>
      <li><span class="cb"></span>\(\sqrt[3]{7}\) غير نسبي · نهائي 1446 <span class="pg ref" data-to="p-rt3"></span></li>
    </ul>
    <p class="small">جهّز نفسك لـ: توأم واحد من هذي، و«حل وحيد» بالقيمة الوسطى، ونفي وجود بالحالات.</p>
''').replace('  <div class="box">', '    <div class="box">') +
    '  </div>\n'))

save('g_u6.html', P)
