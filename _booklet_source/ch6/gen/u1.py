import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *

S3 = '<span class="stars">★★★</span>'
S2 = '<span class="stars">★★</span><span class="stars dim">★</span>'
S1 = '<span class="stars">★</span><span class="stars dim">★★</span>'

def prow(kind, ex, where, mk, st, pid):
    return ['<b>' + kind + '</b><br><span class="small">' + ex + '</span>', where, mk, st, ref(pid)]

cover = r'''<section class="page cover" id="p-cover">
  <div class="hdr"><span class="u">131 ريض · الميد الثاني والاختبار البديل</span><span class="pn"></span></div>
  <div>
    <p class="kicker">ملزمة الفصل 6 · الأقسام 6.1 و6.2 و6.3 · نسخة التدريب</p>
    <h1>الاستقراء الرياضي</h1>
    <p class="sub">كل برهان استقراء خمس أسطر، أربع منها تنسخها زي ما هي كل مرة. هالملزمة تعلمك السطر الباقي (الخطوة) لكل نوع سؤال جا أو ممكن يجي.</p>
  </div>
  <div class="box">
    <h3>وش يجي من الفصل 6؟ (من أربع ميدات)</h3>
''' + tbl([('نوع السؤال، ومثال من الاختبار', 'width:41%'), 'جا في', ('الدرجة', 'width:11%'), ('الأهمية', 'width:11%'), ('الصفحة', 'width:9%')], [
    prow('مجموع بالاستقراء', r'\(1 + 3 + 5 + \cdots + (2n - 1) = n^2\)', 'البنات · نوفمبر · نهائي 1446', '3 إلى 4', S3, 'p-ex1'),
    prow('متتابعة بالاستقراء القوي', r'\(a_n = 2n - 1\)، و«أوجد \(a_3\) و \(a_4\)»', 'ميد 1447 · نوفمبر', '4 إلى 5', S3, 'p-nov3'),
    prow('برهان مبدأ الاستقراء', lt('Prove the Principle of Mathematical Induction'), 'ميد 1447', '3', S2, 'p-pmi'),
    prow('القسمة والمتباينات', r'\(9 \mid (4^{3n} - 1)\) و \(2^n \gt n^2\)', 'ما جت للحين، بس في السلايدات', '—', S1, 'p-ex5'),
], cls='t toc').replace('    <table', '  <table').replace('    </table>', '  </table>') + r'''    <p class="small" style="margin-top:1.2mm">في ميد نوفمبر كان الفصل 6 عليه 9 من 25 درجة، وكل أسئلته من أمثلة السلايدات أو تمرين 6.4 بالحرف.</p>
  </div>
  <div class="box">
    <h3>كل صفحة بنفس الترتيب</h3>
    <div class="order"><span>① السؤال</span><span>② الفكرة</span><span>③ الحل سطر سطر</span><span>④ انتبه</span><span>⑤ تمرين توأم وزر الحل</span></div>
    <p class="fl3" style="margin-top:1.4mm">التمرين التوأم تحله على ورقتك، وبعدها تضغط «الحل» وتقارن. واللون <span class="hypk">الأزرق</span> في الحلول هو المكان اللي استخدمنا فيه الفرض.</p>
  </div>
  <div class="grid2">
    <div class="box">
      <h3>خطة المذاكرة</h3>
      <p class="fl3"><b>الجلسة 1 (ساعتين):</b> الوحدتين 1 و2.</p>
      <p class="fl3"><b>الجلسة 2 (ساعتين):</b> الوحدة 5 أول لأنها أهم، وبعدها 3 و4 بسرعة.</p>
      <p class="fl3"><b>الجلسة 3 (ساعة ونص):</b> «قاعة الاختبار» <span class="ref" data-to="p-bank"></span>.</p>
      <p class="fl3"><b>ليلة الاختبار:</b> آخر صفحة <span class="ref" data-to="p-night"></span>.</p>
    </div>
    <div class="box">
      <h3>رموز الصفحات</h3>
      <p class="fl3"><span class="lv top">★ يتكرر في الاختبارات</span> سؤاله جا أكثر من مرة.</p>
      <p class="fl3"><span class="lv top">★ مرشّح للبديل</span> من السلايدات أو الكتاب، وما انسأل للحين.</p>
      <p class="fl3"><span class="lv must">أساسي</span> شرح تحتاجه. <span class="lv low">احتمال أقل</span> من الخطة، بس فرصة إنه يجي أقل.</p>
      <p class="fl3"><span class="lv extra">إضافي</span> في السلايدات، بس برا خطة المقرر.</p>
    </div>
  </div>
  <div class="note trick"><span class="k">اضغط وروح:</span>زر <a class="go" href="#p-bank">الحل ص N</a> عند كل تمرين يوديك لحله، وزر <a class="back" href="#p-cover">↩ السؤال</a> يرجعك. وأي رقم صفحة «ص N» تقدر تضغطه.</div>
</section>
'''

P = [cover]
U1 = U[1] + ' · 6.1'

# ---------- p-u1: the idea and the five-line template ----------
P.append(page('p-u1', U1, 'must', 'فكرة الاستقراء: السلّم' + tag('sol', 'من السلايدات'),
    qbox(r'<span class="lb">Theorem (The Principle of Mathematical Induction).</span> For each positive integer \(n\), let \(P(n)\) be a statement. If (1) \(P(1)\) is true and (2) the implication “If \(P(k)\), then \(P(k+1)\).” is true for every positive integer \(k\), then \(P(n)\) is true for every positive integer \(n\).',
         'لو الجملة صحيحة عند 1، وكل ما صحت عند عدد صحت عند اللي بعده، فهي صحيحة لكل الأعداد الطبيعية.', lab='المبدأ') +
    idea('زي السلّم: تقدر توقف على أول درجة (الأساس)، وكل ما وقفت على درجة تقدر تطلع اللي بعدها (الخطوة). يعني توصل لكل الدرجات: \\(P(1)\\) صح، فـ \\(P(2)\\) صح، فـ \\(P(3)\\) صح، وكذا.') +
    W([('1', 'الأساس', r'Since …, the statement \(P(1)\) is true.', 'تعوّض n = 1 وتتأكد إن الطرفين متساويين. اسمه في الكتاب: base step.'),
       ('2', 'الفرض', r'Assume that \(P(k)\) is true for an arbitrary positive integer \(k\), that is, assume that …', 'ثابت: نفس الجملة، بس k بدل n. اسمه: inductive hypothesis.'),
       ('3', 'المطلوب', r'We show that \(P(k+1)\) is true, that is, we show that …', 'ثابت: نفس الجملة بـ k + 1. تكتبه قبل الحساب عشان تعرف وين رايح.'),
       ('4', 'الخطوة', r'… (here we use the hypothesis) …, as desired.', 'هنا الشغل كله: تبدأ من جهة k + 1، وتستخدم الفرض، لين توصل للمطلوب. اسمه: inductive step.', HL),
       ('5', 'الختام', r'By the Principle of Mathematical Induction, \(P(n)\) is true for every positive integer \(n\).', 'ثابت: اسم المبدأ كامل، لا تختصره.')],
      title='القالب: خمس أسطر في كل برهان') +
    note('star', 'الخلاصة:', 'أربع أسطر من الخمسة تنسخها كل مرة. تفكيرك كله في سطر «الخطوة»، وكل وحدة في الملزمة تعلمك حركته لنوع واحد.')))

# ---------- p-wo: least element and well-ordering ----------
P.append(page('p-wo', U[1], 'low', 'أصغر عنصر، والترتيب الحسن' + tag('sol', 'من السلايدات'),
    stmt([(r'<span class="lb">Definition.</span> A number \(m\) in a (nonempty) set \(A \subseteq \mathbb{R}\) is called a least (or minimum or smallest) element of \(A\) if \(x \ge m\) for every \(x \in A\).',
           'm أصغر عنصر في A، لو كل عنصر في A أكبر منه أو يساويه.'),
          (r'<span class="lb">Definition.</span> A nonempty set \(S\) of real numbers is said to be well-ordered if every nonempty subset of \(S\) has a least element.',
           'المجموعة «مرتبة ترتيب حسن» لو كل جزء منها (مو فاضي) له أصغر عنصر.'),
          (r'<span class="lb">The Well-Ordering Principle.</span> The set \(\mathbb{N}\) of positive integers is well-ordered.',
           'ℕ مرتبة ترتيب حسن. هذي مسلّمة (axiom)، ما تنبرهن.')]) +
    idea(r'أمثلة السلايدات: \(\mathbb{N}\) أصغر عنصر فيها 1، و \([0, 1]\) أصغر عنصر فيها 0، و \((0, 1)\) و \(\{\frac{1}{n} : n \in \mathbb{N}\}\) ما لهم أصغر عنصر، لأن أي عدد تاخذه فيه أصغر منه. وعشان كذا \([0, 1]\) مو مرتبة ترتيب حسن: \((0, 1)\) جزء منها بدون أصغر عنصر.') +
    '  <h3>كيف تجاوب «Is S well-ordered?»</h3>\n' +
    tbl([('المجموعة', 'width:30%'), ('الجواب', 'width:12%'), 'وش تكتب'], [
        [('منتهية، زي \\(\\{2, 3, 6, 10\\}\\)', 'class="s"'), 'نعم', (lt('Every nonempty finite set of real numbers is well-ordered.'), 'class="s"')],
        [('جزء من \\(\\mathbb{N}\\)', 'class="s"'), 'نعم', (lt('by the Well-Ordering Principle'), 'class="s"')],
        [('\\(\\{i \\in \\mathbb{Z} : i \\ge m\\}\\)', 'class="s"'), 'نعم', ('نظرية في السلايدات: هذي المجموعة مرتبة ترتيب حسن لكل m', 'class="s"')],
        [('فيها كسور أو فترة', 'class="s"'), 'غالباً لا', ('اكتب جزء منها ما له أصغر عنصر، بحركة «نص العدد»', 'class="s"')]]).replace('    <table', '  <table').replace('    </table>', '  </table>') +
    twins([('q-61', '6.1.', EX['6.1'], 's-61')])))

# ---------- p-least: the least element is unique ----------
P.append(page('p-least', U[1], 'low', 'أصغر عنصر وحيد' + tag('sol', 'نظرية من السلايدات'),
    qbox(r'<span class="lb">Theorem.</span> If a set \(A\) of real numbers has a least element, then \(A\) has a unique least element.',
         'لو المجموعة لها أصغر عنصر، فهو واحد بس.', lab='النظرية') +
    idea('«وحيد» (unique) تنبرهن كذا: افترض فيه اثنين، وطلّع إنهم متساويين.') +
    W([('1', 'اثنين', r'Proof. Let \(m_1\) and \(m_2\) be least elements of \(A\).', 'نسمي الاثنين \\(m_1\\) و \\(m_2\\).'),
       ('2', 'الأول', r'Since \(m_1\) is a least element, \(m_2 \ge m_1\).', '\\(m_1\\) أصغر عنصر، و \\(m_2\\) من A، فـ \\(m_2\\) أكبر منه أو يساويه.'),
       ('3', 'الثاني', r'Also, since \(m_2\) is a least element, \(m_1 \ge m_2\).', 'ونفس الكلام بالعكس.'),
       ('4', 'الختام', r'Therefore, \(m_1 = m_2\).', 'كل واحد أكبر من الثاني أو يساويه، فهم متساويين.')], title='نكتب (برهان السلايدات)') +
    twins([('q-max', '', r'A number \(M\) in a set \(A \subseteq \mathbb{R}\) is a largest element of \(A\) if \(x \le M\) for every \(x \in A\). Prove that if \(A\) has a largest element, then \(A\) has a unique largest element.', 's-max')])))

# ---------- p-pmi: proof of the principle (Mid 1447) ----------
P.append(page('p-pmi', U[1], 'top', 'برهان مبدأ الاستقراء' + tag('past', 'ميد 1447 · 3 درجات'),
    qbox(r'<span class="lb">8-</span> For each positive integer \(n\), let \(P(n)\) be a statement. If (1) \(P(1)\) is true and (2) the implication: \(P(k) \Rightarrow P(k+1)\), is true for every positive integer \(k\), then \(P(n)\) is true for every positive integer \(n\). (3 marks)',
         'برهن مبدأ الاستقراء نفسه. جا بالحرف في ميد 1447، وبرهانه في السلايدات.', lab='سؤال ميد 1447') +
    idea('تناقض + الترتيب الحسن: لو فيه أعداد الجملة غلط عندها، خذ أصغرها وسمّه s. العدد اللي قبله \\(s - 1\\) الجملة صحيحة عنده لأنه أصغر من s، والشرط (2) ينقلك من \\(s - 1\\) لـ s، فالجملة صحيحة عند s بعد. تناقض.') +
    W([('1', 'نعكس', r'Proof. Assume, to the contrary, that the theorem is false. Then conditions (1) and (2) are satisfied but there exist some positive integers \(n\) for which \(P(n)\) is a false statement.',
        'نفترض المبدأ غلط: الشرطين صح، بس فيه أعداد الجملة عندها غلط.', dict(BKP, id='m-pmi')),
       ('2', 'أصغر عنصر', r'Let \(S = \{n \in \mathbb{N} : P(n) \text{ is false}\}\). Since \(S\) is a nonempty subset of \(\mathbb{N}\), it follows by the Well-Ordering Principle that \(S\) contains a least element \(s\).',
        'S هي الأعداد اللي الجملة عندها غلط. مو فاضية، فلها أصغر عنصر s (الترتيب الحسن).'),
       ('3', r'\(s \ge 2\)', r'Since \(P(1)\) is true, \(1 \notin S\). Thus, \(s \ge 2\) and \(s - 1 \in \mathbb{N}\).',
        'الجملة صحيحة عند 1، فـ s مو 1. يعني \\(s - 1\\) عدد طبيعي.'),
       ('4', 's − 1', r'Therefore, \(s - 1 \notin S\) and so \(P(s-1)\) is a true statement.',
        '\\(s - 1\\) أصغر من أصغر عنصر، فهو مو في S، يعني الجملة عنده صحيحة.'),
       ('5', 'تناقض', r'By condition (2), \(P(s)\) is also true and so \(s \notin S\). This, however, contradicts our assumption that \(s \in S\).',
        'الشرط (2) ينقلنا من \\(s - 1\\) لـ s، فـ s مو في S، مع إنه في S. تناقض.', HL)], title='نكتب (برهان السلايدات بالحرف)') +
    note('trap', 'انتبه:', 'سطر \\(s \\ge 2\\) هو اللي يخلي \\(s - 1\\) عدد طبيعي، لا تنساه. ولازم تكتب الجمل الخمس كلها، لأن عليها 3 درجات.')))

# ---------- p-s1: solutions of unit 1 ----------
P.append(page('p-s1', 'حلول الوحدة 1', '', 'الحلول' + tag('sol', 'شيّك'),
    sh('تمرين 6.1', 's-61', SM('61')['back']) +
    W([('(a) لا', '', r'The subset \(T = \{x \in \mathbb{Q} : x \gt 0\}\) of \(S\) is nonempty and has no least element, since if \(r \in T\), then \(r/2 \in T\) and \(r/2 \lt r\). Hence \(S\) is not well-ordered.', 'الكسور الموجبة ما لها أصغر عنصر: نص أي واحد أصغر منه.'),
       ('(b) نعم', '', r'\(S\) is a nonempty finite set, so every nonempty subset of \(S\) is finite and has a least element. Hence \(S\) is well-ordered.', 'مجموعة منتهية.'),
       ('(c) لا', '', r'The subset \(T = \{x \in \mathbb{Q} : 0 \lt x \le 1\}\) of \(S\) is nonempty and has no least element, since if \(r \in T\), then \(r/2 \in T\) and \(r/2 \lt r\). Hence \(S\) is not well-ordered.', 'نفس فكرة (a).'),
       ('(d) نعم', '', r'\(S \subseteq \mathbb{N}\), so every nonempty subset of \(S\) is a nonempty subset of \(\mathbb{N}\), which has a least element by the Well-Ordering Principle. Hence \(S\) is well-ordered.', 'جزء من ℕ.')], title='') +
    sh('التوأم: أكبر عنصر وحيد', 's-max', [('q-max', 'السؤال')]) +
    W([('', 'الحل', r'Let \(M_1\) and \(M_2\) be largest elements of \(A\). Since \(M_1\) is a largest element and \(M_2 \in A\), we have \(M_2 \le M_1\). Since \(M_2\) is a largest element and \(M_1 \in A\), we have \(M_1 \le M_2\). Therefore, \(M_1 = M_2\).',
        'نفس برهان أصغر عنصر، بس الإشارة بالعكس.')], title=''), sol=True))

save('b_u1.html', P)
