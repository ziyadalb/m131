import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *


def toc_row(u, kind, how, ex, pid):
    return ['<b>' + u + '</b>', (kind, 'class="s"'), (how, 'class="s"'), ex, ref(pid)]


cover = r'''<section class="page cover" id="p-cover" style="gap:2.6mm">
  <div class="hdr"><span class="u">131 ريض · الميد الثاني</span><span class="pn"></span></div>
  <div>
    <p class="kicker">ملزمة الفصل 6 · الأقسام 6.1 و6.2 و6.3</p>
    <h1>الاستقراء الرياضي</h1>
    <p class="sub">كل برهان استقراء نفس الخمسة أسطر. تتعلم القالب مرة وحدة، وبعدها كل وحدة تعلمك حركة سطر «الخطوة» لنوع واحد: مثال محلول، وبعده تمرين من نفس نوعه.</p>
  </div>
  <div class="box">
    <h3>كيف تستخدمها</h3>
    <ol>
      <li>امشِ بالترتيب. كل وحدة فيها بطاقة خطوات، ونفس أرقام الخطوات تتكرر في المثال والتمرين والحل.</li>
      <li>كل مثال يمشي كذا: السؤال، ثم نفكر بالأرقام، ثم نكتب الجواب وتحت كل سطر معناه.</li>
      <li>بعد المثال يجي «دورك»: غطّ المثال وحل، وبعدها شيّك من الحلول.</li>
      <li>مستعجل؟ امشِ على الصفحات اللي فوقها «أساسي» بس.</li>
    </ol>
  </div>
  <div class="box">
    <h3>خريطة الملزمة: ستة أنواع أسئلة، والسابعة تدريب</h3>
''' + tbl([('الوحدة', 'width:8%'), ('النوع', 'width:20%'), 'كيف يجي في الاختبار', ('تمارين الخطة', 'width:24%'), ('الصفحة', 'width:9%')], [
    toc_row('1', 'الترتيب الحسن', lt('Which sets are well-ordered?'), '<span dir="ltr">6.1</span>', 'p-u1'),
    toc_row('2', 'مبدأ الاستقراء وبرهانه', lt('Prove the Principle of Induction'), 'ميد 1447', 'p-u2'),
    toc_row('3', 'المجاميع', lt(r'Prove \(1 + 3 + \cdots = \ldots\)'), '<span dir="ltr">6.4 · 6.5 · 6.11</span>', 'p-u3'),
    toc_row('4', 'القسمة', lt(r'Prove \(d \mid (\ldots)\)'), '<span dir="ltr">6.16</span>', 'p-u4'),
    toc_row('5', 'المتباينات والبداية من m', lt(r'Prove … \(\gt\) … for \(n \ge m\)'), '<span dir="ltr">6.19 · 6.22 · 6.27</span>', 'p-u5'),
    toc_row('6', 'الاستقراء القوي', lt('A sequence is defined recursively …'), '<span dir="ltr">6.33 · 6.36</span>', 'p-strong'),
    toc_row('7', 'تدريب الاختبار', 'صح أو خطأ · جمل الكتابة · اختبار قصير · ورقة ليلة الاختبار', '—', 'p-traps'),
], cls='t toc') + r'''  </div>
  <div class="grid2">
    <div class="box">
      <h3>أسئلة الاختبارات السابقة</h3>
      <ul class="chk">
        <li><span class="cb"></span>برهان مبدأ الاستقراء · ميد 1447 <span class="pg ref" data-to="p-pmi"></span></li>
        <li><span class="cb"></span>المتتابعة \(a_n = 2n - 1\) · ميد 1447 <span class="pg ref" data-to="p-sx"></span></li>
        <li><span class="cb"></span>مجموع الفرديات · نهائي 1446 <span class="pg ref" data-to="p-64"></span></li>
      </ul>
    </div>
    <div class="box">
      <h3>خطة المذاكرة</h3>
      <p style="font-size:11pt"><b>الجلسة 1:</b> الوحدات 1 إلى 3. تقريباً ساعتين ونص.</p>
      <p style="font-size:11pt"><b>الجلسة 2:</b> الوحدات 4 إلى 6. تقريباً 3 ساعات.</p>
      <p style="font-size:11pt"><b>قبل الاختبار:</b> الوحدة 7. تقريباً ساعة.</p>
    </div>
  </div>
  <div class="box">
    <h3>ألوان الصفحات</h3>
    <p style="font-size:11pt"><span style="color:var(--acc);font-weight:700">■ أخضر:</span> شرح ومثال محلول &nbsp;·&nbsp; <span style="color:#2f5fa8;font-weight:700">■ أزرق:</span> تمرين تحله &nbsp;·&nbsp; <span style="color:#b47a00;font-weight:700">■ ذهبي:</span> سؤال اختبار سابق &nbsp;·&nbsp; <span style="color:#8a959c;font-weight:700">■ رمادي:</span> حلول</p>
  </div>
  <p class="small">ليش هالفصل مهم: في ميد 1447 جا منه 7 درجات من 25، والسؤالين من السلايدات بالحرف. علقت برمز أو كلمة إنجليزية؟ شوف <span class="ref" data-to="p-phr"></span>.</p>
</section>
'''

P = [cover]
U1 = U[1] + ' · 6.1'

# ---------------- UNIT 1 ----------------
P.append(page('p-u1', U1, 'must', 'أصغر عنصر، والترتيب الحسن',
    idea('فكرتين بس: «أصغر عنصر» في المجموعة، و«مرتبة ترتيباً حسناً» يعني كل قطعة منها لها أصغر عنصر. وعليها ينبني الاستقراء كله.') +
    think('نبدأ بأرقام', before=tbl([('المجموعة', 'width:27%'), ('أصغر عنصر؟', 'width:31%'), 'مرتبة ترتيباً حسناً؟'], [
        [r'\(\{3, 5, 9\}\)', '3', ('نعم: منتهية', 'class="s"')],
        [r'\(\mathbb{N} = \{1, 2, 3, \ldots\}\)', '1', ('نعم: هذي المسلّمة', 'class="s"')],
        [r'\(\{-3, -2, -1, 0, \ldots\}\)', r'\(-3\)', ('نعم: صحيحة من m وفوق', 'class="s"')],
        [r'\([0, 1]\)', '0', (r'<b>لا</b>: القطعة \((0, 1)\) ما لها أصغر عنصر', 'class="s"')],
        [r'\((0, 1)\)', 'ما فيه: نص أي عدد أصغر منه', ('لا', 'class="s"')],
        [r'\(\mathbb{Z}\)', r'ما فيه: \(r - 1\) أصغر من r', ('لا', 'class="s"')]]),
        extra=r'    <p>شوف \([0, 1]\): لها أصغر عنصر، ومع كذا مو مرتبة. لأن الشرط على كل قطعة منها، مو عليها هي بس.</p>' + '\n') +
    stmt([(r'<span class="lb">Definition.</span> A number \(m\) in a nonempty set \(A \subseteq \mathbb{R}\) is called a <i>least element</i> of \(A\) if \(x \ge m\) for every \(x \in A\).',
           r'm <b>أصغر عنصر</b> في A إذا: m داخل A، وكل عنصر x في A أكبر من أو يساوي m.'),
          (r'<span class="lb">Definition.</span> A nonempty set \(S\) of real numbers is <i>well-ordered</i> if every nonempty subset of \(S\) has a least element.',
           'S <b>مرتبة ترتيباً حسناً</b> إذا كل قطعة غير خالية منها (' + lt('subset') + ') لها أصغر عنصر.'),
          (r'<span class="lb">The Well-Ordering Principle.</span> The set \(\mathbb{N}\) of positive integers is well-ordered.',
           'أي مجموعة غير خالية من 1، 2، 3، … لها أصغر عدد. الكتاب يقبلها بدون برهان (' + lt('axiom') + ' = مسلّمة).'),
          (r'<span class="lb">Theorem 6.7.</span> For each integer \(m\), the set \(S = \{i \in \mathbb{Z} : i \ge m\}\) is well-ordered.',
           'الأعداد الصحيحة من m وفوق مرتبة ترتيباً حسناً. وهي اللي تسمح نبدأ الاستقراء من أي m (الوحدة 5).')]) +
    card('بطاقة الخطوات: مرتبة ترتيباً حسناً؟', [
        ('صنّف', r'منتهية؟ جزء من \(\mathbb{N}\)؟ صحيحة من m وفوق؟ إذا إيه، الجواب <b>نعم</b>.'),
        ('ابنِ قطعة', r'غير كذا: قطعة غير خالية ما لها أصغر عنصر، بحركة «نص العدد» أو «ناقص 1». الجواب <b>لا</b>.'),
        ('اكتب', 'جملة الجواب الجاهزة ' + ref('p-wo') + '.')]), style='gap:3.2mm'))

P.append(page('p-u1b', U[1], 'must', 'مثال: أصغر عنصر واحد بس' + tag('sol', 'من السلايدات') + tag('ex', 'دورك'),
    qbox(r'Prove: If a set \(A\) of real numbers has a least element, then \(A\) has a unique least element.',
         r'لو المجموعة لها أصغر عنصر، فهو واحد بس (' + lt('unique') + r' = وحيد). <b>نفكر:</b> لو 3 و5 الاثنين أصغر عنصر، لازم \(5 \ge 3\) ' + OK + r' و \(3 \ge 5\) ' + NO + '. ما يصير إلا لو نفس العدد.') +
    W([('1', 'نفرض', r'Let \(m_1\) and \(m_2\) be least elements of \(A\).', r'نفرض أن \(m_1\) و \(m_2\) الاثنين أصغر عنصر.'),
       ('2', 'مرة', r'Since \(m_1\) is a least element and \(m_2 \in A\), we have \(m_2 \ge m_1\).', r'\(m_1\) أصغر عنصر، و \(m_2\) داخل A.'),
       ('3', 'بالعكس', r'Since \(m_2\) is a least element and \(m_1 \in A\), we have \(m_1 \ge m_2\).', 'نفس الجملة، بس نبدّل الاثنين.'),
       ('4', 'النتيجة', r'Therefore, \(m_1 = m_2\).', 'كل واحد أكبر من أو يساوي الثاني، إذن متساويين.')], title='نكتب (برهان السلايدات)') +
    qbox(r'A number \(M\) in a set \(A \subseteq \mathbb{R}\) is a <i>largest element</i> of \(A\) if \(x \le M\) for every \(x \in A\). Prove that if \(A\) has a largest element, then \(A\) has a unique largest element.',
         r'نفس البرهان بالضبط، بس «أكبر» بدل «أصغر»، و \(\le\) بدل \(\ge\). اكتبه بدون ما تطالع.', lab='دورك · تدريب (مو من الكتاب)', cls='ex') +
    W([('1', 'نفرض', None, None, 'b1'), ('2', 'مرة', None, None, 'b1'), ('3', 'بالعكس', None, None, 'b1'), ('4', 'النتيجة', None, None, 'b1')], title='') +
    note('star', 'البرهان كله:', 'تعريف أصغر عنصر مرتين، مرة على كل واحد. قصير وممكن ينطلب.'),
    style='gap:2.9mm'))

def yes_row(name, en, ar):
    return ('', name, en, ar)

P.append(page('p-wo', U[1], 'must', 'كيف تجاوب: نعم أو لا' + tag('sol', 'أمثلة محلولة'),
    qbox(r'Is \(S = \{x \in \mathbb{R} : 0 \le x \le 2\}\) well-ordered?',
         r'S هي الأعداد من 0 إلى 2. <b>1 صنّف:</b> مو منتهية، ومو جزء من \(\mathbb{N}\)، ومو صحيحة. فنروح للخطوة 2. <b>2 ابنِ قطعة:</b> T = من 0 إلى 2 بدون الصفر. 0.1؟ لا، 0.05 أصغر. أي عدد فيها نصّه أصغر منه وداخلها.', lab='مثال 1 · الجواب «لا»') +
    W([('2', 'ابنِ قطعة', r'The subset \(T = \{x \in \mathbb{R} : 0 \lt x \le 2\}\) of \(S\) is nonempty and has no least element, since if \(r \in T\), then \(r/2 \in T\) and \(r/2 \lt r\).',
        'القطعة T، والسبب: نص أي عدد فيها أصغر منه وداخلها.'),
       ('3', 'اكتب', r'Hence \(S\) is not well-ordered.', 'إذن S مو مرتبة ترتيباً حسناً.')], title='') +
    note('trap', 'انتبه:', 'S نفسها لها أصغر عنصر (0)، ومع كذا الجواب «لا».') +
    '  <h3>مثال 2 · الجواب «نعم»: ثلاث حالات، لكل وحدة جملة</h3>\n' +
    W([yes_row('منتهية', r'\(S = \{3, 7, 20\}\) is a nonempty finite set, so every nonempty subset of \(S\) is finite and has a least element. Hence \(S\) is well-ordered.', 'أي قطعة منها فيها أعداد قليلة، فلها أصغر عدد.'),
       yes_row(r'جزء من \(\mathbb{N}\)', r'\(S = \{2, 4, 6, \ldots\} \subseteq \mathbb{N}\), so every nonempty subset of \(S\) is a nonempty subset of \(\mathbb{N}\), which has a least element by the Well-Ordering Principle. Hence \(S\) is well-ordered.', 'أي قطعة منها قطعة من ℕ، ولها أصغر عنصر بالمسلّمة.'),
       yes_row('من m وفوق', r'\(S = \{x \in \mathbb{Z} : x \ge -5\} = \{i \in \mathbb{Z} : i \ge m\}\) with \(m = -5\), so \(S\) is well-ordered by Theorem 6.7.', r'صحيحة من \(-5\) وفوق: Theorem 6.7.')], title='') +
    note('trick', 'تريك «لا»:', r'دايماً بحركة من اثنين: «نص العدد» للفترات والأعداد النسبية، و«ناقص 1» للأعداد الصحيحة اللي ما لها بداية، مثل \(\{\ldots, -2, -1, 0\}\).'),
    style='gap:3.1mm'))

P.append(page('p-61', U[1], 'must', 'تمرين 6.1' + tag('ex', 'دورك'),
    duork('6.1', r'<span class="lb">6.1.</span> Which of the following sets are well-ordered?<br>(a) \(S = \{x \in \mathbb{Q} : x \ge -10\}\) &nbsp;&nbsp; (b) \(S = \{-2, -1, 0, 1, 2\}\)<br>(c) \(S = \{x \in \mathbb{Q} : -1 \le x \le 1\}\) &nbsp;&nbsp; (d) \(S = \{p : p \text{ is a prime}\} = \{2, 3, 5, 7, 11, 13, 17, \ldots\}\)',
          r'أي من هذي المجموعات مرتبة ترتيباً حسناً؟ (a) الأعداد النسبية من \(-10\) وفوق. (b) \(\{-2, -1, 0, 1, 2\}\). (c) الأعداد النسبية من \(-1\) إلى 1. (d) الأعداد الأولية.') +
    recall('غطّ البطاقة ' + ref('p-u1') + ' واكتب خطواتها الثلاث من ذاكرتك. بعدين لكل مجموعة: صنّف أول، وإذا ما انطبقت ولا حالة ابنِ قطعة.') +
    W([('(a)', '☐ نعم ☐ لا', None, None, 'b2'), ('(b)', '☐ نعم ☐ لا', None, None, 'b2'),
       ('(c)', '☐ نعم ☐ لا', None, None, 'b2'), ('(d)', '☐ نعم ☐ لا', None, None, 'b2')], title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> \(\mathbb{Q}\) هي الأعداد النسبية (الكسور). لو r نسبي موجب، فإن \(r/2\) نسبي موجب وأصغر منه.',
           '<b>تلميح:</b> (b) و(d) جوابهم من الخطوة 1: صنّف.'])))

# ---------------- UNIT 2 ----------------
U2 = U[2] + ' · 6.1'
P.append(page('p-u2', U2, 'must', 'فكرة الاستقراء، والمبدأ',
    idea('الاستقراء يثبت أن جملة صحيحة لكل n = 1، 2، 3، … بدون ما تجربها كلها.') +
    think(r'نبدأ بأرقام: \(1 + 2 + \cdots + n = n(n+1)/2\)', before=tbl([r'\(n\)', '1', '2', '3', '4'],
        [[r'\(1 + \cdots + n\)', '1', '3', '6', '10'], [r'\(n(n+1)/2\)', '1', '3', '6', '10']], ltr=True),
        extra='    <p>صحيحة للأربعة. بس الأعداد ما تخلص، فنحتاج طريقة ثانية.</p>\n') +
    think('الفكرة: الدومينو', before=r'''    <div class="dom"><span class="d f">1</span><span class="ar">→</span><span class="d">2</span><span class="ar">→</span><span class="d">3</span><span class="ar">→</span><span class="d">4</span><span class="ar">→</span><span>\(\cdots\)</span></div>
    <p>لو (1) أول قطعة تطيح، و(2) كل قطعة تطيح تطيّح اللي بعدها، فكلها بتطيح. وبالرياضيات: (1) الجملة صحيحة عند \(n = 1\). (2) <b>لو</b> صحيحة عند k، فهي صحيحة عند \(k + 1\).</p>
''') +
    stmt([(r'<span class="lb">Theorem 6.2 (The Principle of Mathematical Induction).</span> For each positive integer \(n\), let \(P(n)\) be a statement.', r'لكل عدد صحيح موجب n عندنا جملة \(P(n)\).'),
          (r'If (1) \(P(1)\) is true and', r'إذا كان (1) \(P(1)\) صحيحة، و'),
          (r'(2) the implication “If \(P(k)\), then \(P(k+1)\)” is true for every positive integer \(k\),', r'(2) «إذا \(P(k)\) فإن \(P(k+1)\)» صحيحة لكل عدد صحيح موجب k،'),
          (r'then \(P(n)\) is true for every positive integer \(n\).', r'فإن \(P(n)\) صحيحة لكل n.')]) +
    note('trick', r'وش يعني \(P(n)\)؟', r'الجملة عند العدد n. مثلاً \(P(3)\) هي \(1 + 2 + 3 = 3 \cdot 4/2\). و \(P(k)\) عند عدد اسمه k، و \(P(k+1)\) عند اللي بعده.') +
    note('star', r'ليش مسموح نفترض \(P(k)\)؟', r'الشرط (2) ما يقول إن \(P(k)\) صحيحة. يقول «لو» صحيحة، اللي بعدها صحيحة. مثل: لو طاحت القطعة k، بتطيّح اللي بعدها.') +
    '  <p class="small">الشرط (1) اسمه الأساس (' + lt('base step') + ')، والشرط (2) الخطوة (' + lt('inductive step') + ')، و \\(P(k)\\) فرض الاستقراء (' + lt('inductive hypothesis') + ').</p>\n',
    style='gap:2.8mm'))

P.append(page('p-pmi', U[2], 'must', 'برهان مبدأ الاستقراء' + tag('past', 'ميد 1447 · 3 درجات'),
    qbox(r'For each positive integer \(n\), let \(P(n)\) be a statement. If (1) \(P(1)\) is true and (2) the implication \(P(k) \Rightarrow P(k+1)\) is true for every positive integer \(k\), then \(P(n)\) is true for every positive integer \(n\). (3 marks)',
         'برهن مبدأ الاستقراء نفسه. الطريقة: بالتناقض، ونستخدم الترتيب الحسن من الوحدة 1.') +
    r'''  <div class="think">
    <h3>نفكر: تخيّل أن أصغر عدد تفشل عنده الجملة هو 5</h3>
    <div class="nl">
      <div class="c"><div class="dot">1</div><div class="cap">صحيحة</div></div>
      <div class="c"><div class="dot">2</div><div class="cap">صحيحة</div></div>
      <div class="c"><div class="dot">3</div><div class="cap">صحيحة</div></div>
      <div class="c"><div class="dot">4</div><div class="cap">s − 1<br>صحيحة</div></div>
      <div class="c s"><div class="dot">5</div><div class="cap">s<br>أصغر فاشل</div></div>
      <div class="c x"><div class="dot">6</div><div class="cap">؟</div></div>
      <div class="c x"><div class="dot">7</div><div class="cap">؟</div></div>
    </div>
    <p style="font-size:11.2pt">5 أصغر فاشل، فـ 4 صحيحة. والشرط (2) يقول: 4 صحيحة تجرّ 5. يعني 5 صحيحة وفاشلة. مستحيل! البرهان نفس الكلام بالحرف s.</p>
  </div>
''' +
    W([('1', 'نعكس', r'Assume, to the contrary, that the theorem is false. Then conditions (1) and (2) are satisfied but there exist some positive integers \(n\) for which \(P(n)\) is a false statement.', 'نفترض العكس: الشرطين متحققين، بس فيه أعداد الجملة عندها خاطئة.'),
       ('2', 'أصغر فاشل', r'Let \(S = \{n \in \mathbb{N} : P(n) \text{ is false}\}\). Since \(S\) is a nonempty subset of \(\mathbb{N}\), it follows by the Well-Ordering Principle that \(S\) contains a least element \(s\).', 'S = الأعداد الفاشلة. غير خالية ومن ℕ، فلها أصغر عنصر s.'),
       ('3', r'\(s \ge 2\)', r'Since \(P(1)\) is true, \(1 \notin S\). Thus \(s \ge 2\) and \(s - 1 \in \mathbb{N}\).', 'الشرط (1): 1 مو فاشل.'),
       ('4', r'\(s - 1\)', r'Therefore, \(s - 1 \notin S\) and so \(P(s-1)\) is a true statement.', r'\(s - 1\) أصغر من أصغر فاشل، فهو صحيح.'),
       ('5', 'تناقض', r'By condition (2), \(P(s)\) is also true and so \(s \notin S\). This, however, contradicts our assumption that \(s \in S\).', 'الشرط (2) ينقل الصحة إلى s، و s فاشل. تناقض.')], title='نكتب (الحل الرسمي: خمس جمل)') +
    note('star', 'في الاختبار:', 'الخمس جمل بنفس الترتيب. الشرط (1) في الجملة 3، والشرط (2) في الجملة 5. لو برهانك ما استخدم الشرطين، فيه شي ناقص.'),
    style='gap:2.7mm'))

import re
old = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mem.html'), encoding='utf-8').read()
mem = re.search(r'<section class="page" id="p-mem">.*?</section>', old, re.S).group(0)
mem = mem.replace('<li>غطِّ الصفحة اللي قبل، واملأ الفراغات.</li>', '<li>غطِّ الصفحة اللي قبل، واملأ الفراغات تحت.</li>')
assert 'lv must' in mem and 'blank' in mem
P.append(mem + '\n')

P.append(page('p-s12', 'حلول الوحدتين 1 و2', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>تمرين 6.1</h3>\n' +
    W([('(a) لا', '', r'The subset \(T = \{x \in \mathbb{Q} : x \gt 0\}\) of \(S\) is nonempty and has no least element, since if \(r \in T\), then \(r/2 \in T\) and \(r/2 \lt r\). Hence \(S\) is not well-ordered.', 'القطعة: النسبية الموجبة، بحركة «نص العدد».'),
       ('(b) نعم', '', r'\(S\) is a nonempty finite set, so every nonempty subset of \(S\) is finite and has a least element. Hence \(S\) is well-ordered.', 'منتهية.'),
       ('(c) لا', '', r'The subset \(T = \{x \in \mathbb{Q} : 0 \lt x \le 1\}\) of \(S\) is nonempty and has no least element, since if \(r \in T\), then \(r/2 \in T\) and \(r/2 \lt r\). Hence \(S\) is not well-ordered.', 'القطعة: النسبية من 0 إلى 1 بدون الصفر.'),
       ('(d) نعم', '', r'\(S \subseteq \mathbb{N}\), so every nonempty subset of \(S\) is a nonempty subset of \(\mathbb{N}\), which has a least element by the Well-Ordering Principle. Hence \(S\) is well-ordered.', 'جزء من ℕ.')], title='') +
    note('trap', 'انتبه:', 'في (a) المجموعة نفسها لها أصغر عنصر (−10)، بس هذا ما يكفي.') +
    '  <h3>تدريب أكبر عنصر</h3>\n' +
    W([('', '', r'Let \(M_1\) and \(M_2\) be largest elements of \(A\). Since \(M_1\) is a largest element and \(M_2 \in A\), we have \(M_2 \le M_1\). Since \(M_2\) is a largest element and \(M_1 \in A\), we have \(M_1 \le M_2\). Therefore, \(M_1 = M_2\).', None)], title='') +
    r'''  <h3>فراغات برهان المبدأ بالترتيب</h3>
  <ol class="notes" style="direction:ltr; text-align:left; font-family:var(--en); columns:2; column-gap:8mm">
    <li>the theorem is false</li><li>\(P(n)\) is false</li><li>Well-Ordering Principle</li><li>\(P(1)\) is true</li><li>\(2\)</li>
    <li>\(\notin\)</li><li>true</li><li>(2)</li><li>\(\notin\)</li><li>our assumption that \(s \in S\)</li>
  </ol>
''' + box('راجع نفسك (دقيقتين)', '''    <ul class="chk">
      <li><span class="cb"></span>أقول خطوات «مرتبة ترتيباً حسناً؟» من ذاكرتي: صنّف، ابنِ قطعة، اكتب.</li>
      <li><span class="cb"></span>أكتب برهان المبدأ بالجمل الخمس بدون ما أطالع.</li>
    </ul>
'''), sol=True, style='gap:2.8mm'))

save('b_u12.html', P)
