import os
D = os.path.dirname(os.path.abspath(__file__)) + os.sep


def lt(t):
    return '<span class="lt">' + t + '</span>'


HDR = '<div class="hdr"><span class="u">ملخص الفصل 5 · الوجود والبرهان بالتناقض</span><span class="pn"></span></div>'


def block(num, name, when, idea, steps, body):
    st = '    <div class="steps">' + ''.join('<span><span class="n">' + str(i) + '</span>' + s + '</span>' for i, s in enumerate(steps, 1)) + '</div>\n'
    return ('  <div class="tb">\n    <div class="tbh"><span class="tn">' + num + '</span><span class="tt">' + name + '</span></div>\n' +
            '    <p class="meta"><b>متى يجيك:</b> ' + when + '</p>\n' +
            '    <p class="meta"><b>الفكرة:</b> ' + idea + '</p>\n' + st + body + '  </div>\n')


def exq(en, ar, lab='مثال'):
    return ('    <div class="exq"><span class="lb2">' + lab + '</span><span class="bx"><span class="e2">' + en +
            '</span><span class="a2">يعني: ' + ar + '</span></span></div>\n')


def think(t):
    return '    <p class="think2"><b>كيف تفكر:</b> ' + t + '</p>\n'


def ans(en, ar, lab='تكتب'):
    a2 = ('<span class="a2">يعني: ' + ar + '</span>') if ar else ''
    return ('    <div class="ans"><span class="lb2">' + lab + '</span><span class="bx"><span class="e2">' + en +
            '</span>' + a2 + '</span></div>\n')


def warn(t):
    return '    <p class="warn"><b>⚠️ انتبه:</b> ' + t + '</p>\n'


OK = '<span class="ok">✓</span>'
NO = '<span class="no">✗</span>'

MAP = r'''  <h3>كيف تعرف نوع السؤال؟</h3>
  <table class="t">
    <tr><th style="width:43%">لو شفت في السؤال</th><th style="width:22%">فهو</th><th>أول شي تكتبه</th></tr>
    <tr><td>''' + lt('Disprove') + ' + ' + lt('For every') + ' (أو ' + lt('If …, then …') + r''')</td><td>1. مثال مضاد</td><td>''' + lt(r'For \(n = \ldots\), …') + r'''</td></tr>
    <tr><td>''' + lt('Prove') + ' + ' + lt('There is no') + ' (أو ' + lt('irrational') + r''')</td><td>2. تناقض</td><td>''' + lt('Assume, to the contrary, …') + r'''</td></tr>
    <tr><td>''' + lt('by (a) direct, (b) contrapositive, (c) …') + r'''</td><td>3. ثلاث طرق</td><td>حسب الطريقة</td></tr>
    <tr><td>''' + lt('Prove') + ' + ' + lt('There exists') + r'''</td><td>4. وجود</td><td>''' + lt(r'Let \(x = \ldots\)') + r'''</td></tr>
    <tr><td>''' + lt('Disprove') + ' + ' + lt('There exists') + r'''</td><td>5. نفي وجود</td><td>''' + lt('We show that …') + r'''</td></tr>
    <tr><td>''' + lt('Prove or disprove') + r'''</td><td>أنت تقرر</td><td>جرّب ثلاث أرقام أول</td></tr>
  </table>
  <p class="gl">''' + lt('Prove') + ' = اثبت إنها صح · ' + lt('Disprove') + ' = اثبت إنها غلط · ' + lt('For every') + ' = لكل · ' + lt('There exists') + ' = يوجد · ' + lt('There is no') + r''' = ما فيه</p>
'''

T1 = block('1', 'المثال المضاد',
    'لما يقول لك اثبت إن الجملة غلط (' + lt('Disprove') + ')، والجملة تقول «لكل…».',
    'جملة «لكل» تطيح برقم واحد بس يخالفها.',
    ['جرّب أرقام من المجموعة اللي في السؤال، لين تلقى رقم يخرّبها.', 'اكتب الحساب بالأرقام.', 'قل إن هذا الرقم مثال مضاد.'],
    exq(r'For every even positive integer \(n\), \(12 \mid (n^2 - 4)\).', r'لكل عدد زوجي موجب n، الـ 12 تقسم \(n^2 - 4\).') +
    think(r'نجرب الأعداد الزوجية بالترتيب: \(n = 2\) يطلع 0، و12 تقسمه ' + OK + r'. \(n = 4\) يطلع 12 ' + OK + r'. \(n = 6\) يطلع 32، و12 ما تقسمه ' + NO + '. لقينا الرقم.') +
    ans(r'<b>False.</b> For \(n = 6\), \(n^2 - 4 = 32\) and \(12 \nmid 32\). Thus, \(n = 6\) is a counterexample.',
        'الجملة غلط. لما n = 6 يطلع 32، و12 ما تقسم 32. إذن 6 مثال مضاد.') +
    warn('أول رقم أو رقمين ممكن يمشون، فجرّب ثلاثة على الأقل. ولو الجملة «إذا… فإن…»، دوّر رقم يخلي الشرط صح والنتيجة غلط.'))

T2 = block('2', 'البرهان بالتناقض',
    'لما يقول «' + lt('There is no') + '» (ما فيه…) أو «' + lt('irrational') + '» (غير نسبي).',
    'تفترض عكس المطلوب، وتمشي بخطوات صحيحة لين توصل لشي مستحيل. معناها افتراضك غلط، والجملة صح.',
    ['اكتب العكس: ' + lt('Assume, to the contrary, that …'), 'امشِ بخطوات صحيحة: تعريف وحساب.', 'وصّل لشي مستحيل واكتب ' + lt('This is a contradiction.')],
    exq('There is no smallest positive real number.', 'ما فيه أصغر عدد حقيقي موجب.', 'مثال 1') +
    think('أي عدد موجب تختاره، نصّه أصغر منه وبعده موجب. فما فيه «أصغر واحد».') +
    ans(r'Assume, to the contrary, that there is a smallest positive real number, say \(r\). Since \(0 \lt r/2 \lt r\), \(r/2\) is a positive real number smaller than \(r\). This is a contradiction.',
        'نفترض فيه أصغر عدد موجب، ونسميه r. بس نص r موجب وأصغر منه، وهذا يناقض إن r هو الأصغر.') +
    exq(r'Prove that \(\sqrt{2}\) is irrational.', r'اثبت إن \(\sqrt{2}\) ما ينكتب ككسر.', 'مثال 2') +
    think(r'نفترض \(\sqrt{2} = a/b\)، كسر مبسّط لآخر حد. نربّع الطرفين، فيطلع إن a و b الاثنين زوجيين، يعني الكسر ينبسط بعد. تناقض!') +
    ans(r'Assume, to the contrary, that \(\sqrt{2}\) is rational. Then \(\sqrt{2} = a/b\), where \(a, b \in \mathbb{Z}\), \(b \ne 0\), and \(a/b\) is in lowest terms. So \(a^2 = 2b^2\), and \(a\) is even. Let \(a = 2c\). Then \(4c^2 = 2b^2\), so \(b^2 = 2c^2\) and \(b\) is even. Since \(a\) and \(b\) are both even, this contradicts that \(a/b\) is in lowest terms.',
        r'\(a^2 = 2b^2\) فـ a زوجي. نكتبه 2c ونعوّض، فيطلع b زوجي بعد. والكسر المبسّط ما يكون بسطه ومقامه الاثنين زوجيين.') +
    warn('كيف تكتب العكس: «ما فيه» يصير «فيه». «غير نسبي» يصير «نسبي». «إذا P فإن Q» يصير «P صح و Q غلط». و«و» تصير «أو».'))

T3 = block('3', 'ثلاث طرق',
    'لما يطلب نفس الجملة بثلاث طرق: ' + lt('direct') + ' و ' + lt('contrapositive') + ' و ' + lt('contradiction') + '.',
    'الجملة «إذا P فإن Q». الفرق بين الطرق بس في وش تفترض بأول سطر، ووين توصل.',
    ['<b>مباشر:</b> تفترض P، وتوصل لـ Q.', '<b>عكس النقيض:</b> تفترض إن Q غلط، وتوصل إن P غلط.', '<b>تناقض:</b> تفترض P صح و Q غلط مع بعض، وتوصل لشي مستحيل.'],
    exq(r'If \(n\) is an even integer, then \(5n + 1\) is odd.', r'لو n زوجي، فـ \(5n + 1\) فردي. هنا P = «n زوجي»، و Q = «\(5n + 1\) فردي».') +
    ans(r'Assume that \(n\) is even. Then \(n = 2k\) for some integer \(k\). So \(5n + 1 = 10k + 1 = 2(5k) + 1\), which is odd.',
        r'n زوجي فنكتبه 2k، ونعوّض. يطلع \(5n + 1\) على شكل \(2(\ldots) + 1\)، يعني فردي.', '(a) مباشر') +
    ans(r'Assume that \(5n + 1\) is even. Then \(5n + 1 = 2k\) for some integer \(k\). So \(n = (5n + 1) - 4n - 1 = 2(k - 2n - 1) + 1\), which is odd.',
        r'نفترض \(5n + 1\) زوجي (عكس Q)، ونطلّع n منها. يطلع n فردي (عكس P).', '(b) عكس النقيض') +
    ans(r'Assume, to the contrary, that there is an even integer \(n\) such that \(5n + 1\) is even. Then \(n = 2x\) and \(5n + 1 = 2y\) for some integers \(x, y\). So \(10x + 1 = 2y\) and \(1 = 2(y - 5x)\). Thus 1 is even, which is a contradiction.',
        r'نفترض n زوجي و \(5n + 1\) زوجي مع بعض. يطلع إن 1 زوجي، وهذا مستحيل.', '(c) تناقض') +
    warn(r'لا تبدأ أبداً بإنك تفترض Q (إن \(5n + 1\) فردي)، لأن هذا هو اللي مطلوب منك تثبته.'))

T4 = block('4', 'الوجود',
    'لما يقول «' + lt('Prove: There exists …') + '» (اثبت إنه يوجد…).',
    'يكفي تجيب مثال واحد يحقق الشرط، وتتحقق منه بالأرقام.',
    ['اختر الشي: رقم أو أرقام.', 'تحقق إنه يمشي مع كل شروط السؤال.', 'قل إنه هو المطلوب.'],
    exq('There exists an integer whose cube equals its square.', 'فيه عدد صحيح مكعبه يساوي مربعه.', 'مثال 1') +
    ans(r'Since \(1^3 = 1^2 = 1\), the integer 1 has the desired property.', None) +
    exq(r'The equation \(x^5 + 2x - 5 = 0\) has a unique real solution between \(x = 1\) and \(x = 2\).', 'المعادلة لها حل واحد بس بين 1 و2.', 'مثال 2') +
    think(r'عند 1 الدالة سالبة (\(-2\))، وعند 2 موجبة (31)، فلازم تقطع الصفر بينهم. ولو فيه حلين، يطلع \(0 \lt 0\). مستحيل.') +
    ans(r'<b>Existence.</b> Let \(f(x) = x^5 + 2x - 5\). Since \(f\) is a polynomial, it is continuous on \([1, 2]\). Since \(f(1) = -2 \lt 0 \lt 31 = f(2)\), by the Intermediate Value Theorem there is \(c \in (1, 2)\) with \(f(c) = 0\).<br><b>Uniqueness.</b> Assume, to the contrary, that there are two solutions \(a \lt b\) in \((1, 2)\). Then \(a^5 + 2a - 5 \lt b^5 + 2b - 5\), so \(0 \lt 0\), a contradiction.',
        '«حل وحيد» (' + lt('unique') + ') جزأين: إنه موجود (بالقيمة الوسطى)، وإنه واحد بس (بالتناقض).'))

T5 = block('5', 'نفي الوجود',
    'لما يقول «' + lt('Disprove: There exists …') + '» (اثبت إنه ما يوجد…).',
    'هنا مثال واحد ما يكفي. لازم تثبت إن الشي غلط مع كل الأرقام.',
    ['اقلب السؤال: بدل «فيه رقم كذا»، تثبت إن كل الأرقام عكس كذا.', 'خذ رقم عام (مو رقم معيّن) واكتبه بالرموز.', 'اثبت بالحساب، أو بحالتين: زوجي وفردي.'],
    exq(r'Disprove: There exists an integer \(n\) such that \(n^3 - n + 1\) is even.', r'اثبت إنه ما فيه عدد صحيح يخلي \(n^3 - n + 1\) زوجي.') +
    think('نجرب 0، 1، 2، 3: يطلع 1، 1، 7، 25، كلها فردية. فنثبت إنها فردية دايماً: مرة n زوجي، ومرة n فردي.') +
    ans(r'We show that \(n^3 - n + 1\) is odd for every \(n \in \mathbb{Z}\).<br><i>Case 1.</i> \(n = 2a\): \(n^3 - n + 1 = 8a^3 - 2a + 1 = 2(4a^3 - a) + 1\), which is odd.<br><i>Case 2.</i> \(n = 2b + 1\): \(n^3 - n + 1 = 8b^3 + 12b^2 + 4b + 1 = 2(4b^3 + 6b^2 + 2b) + 1\), which is odd.',
        r'في الحالتين يطلع الناتج على شكل \(2(\ldots) + 1\)، يعني فردي دايماً.') +
    warn('لا تخلط: «' + lt('Disprove: For every') + '» يكفيها مثال واحد. أما «' + lt('Disprove: There exists') + '» فلازم برهان لكل الأرقام.'))


def prow(en, ar):
    return '    <tr><td class="a">' + ar + '</td><td class="e">' + en + '</td></tr>\n'


PH = ('  <div class="box">\n    <h3>خمس جمل احفظها بالإنجليزي</h3>\n  <table class="bi">\n' +
      prow(r'Thus, \(n = \ldots\) is a counterexample.', 'إذن هذا الرقم مثال مضاد.') +
      prow('Assume, to the contrary, that …', 'نفترض العكس إن …') +
      prow('This is a contradiction.', 'وهذا تناقض.') +
      prow('… has the desired property.', 'وهذا يحقق المطلوب.') +
      prow('We show that …', 'نثبت إن …') +
      '  </table>\n  </div>\n')

INTRO = ('  <div class="idea">الفصل كله خمس أنواع أسئلة. أول شي اعرف نوع السؤال من كلماته (الجدول تحت)، وبعدين امشِ على خطوات النوع. '
         'الأجوبة مكتوبة بالإنجليزي مثل ما تكتبها في الاختبار، وتحت كل جواب معناه بالعربي.</div>\n')


def page(pid, body, title=None):
    t = ('\n  <h2 class="t">' + title + '</h2>\n') if title else '\n'
    return '<section class="page" id="' + pid + '" style="gap:' + ('1.6mm' if pid == 'p-s3' else '2.6mm') + '">\n  ' + HDR + t + body + '</section>\n'


pages = [
    page('p-s1', INTRO + MAP + T1, 'ملخص الفصل 5: خمس أنواع أسئلة'),
    page('p-s2', T2),
    page('p-s3', T3 + T4),
    page('p-s4', T5 + PH),
]
open(D + 'b_sum.html', 'w', encoding='utf-8').write('\n'.join(pages))
print('written', len(pages))
