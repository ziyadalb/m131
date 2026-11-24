import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h6 import *
P = []

def qrow(head, mk):
    return '    <div class="qrow" style="direction:ltr"><span class="en">' + head + '</span><span class="mk">' + mk + '</span></div>\n'

def q(t, sol=None, src=''):
    return ('    <div class="q"><span class="qt">' + t + '</span>' + (('<span class="src">' + src + '</span>') if src else '') +
            (go(sol) if sol else '') + '</div>\n')

def tagrows(rows, ids, home, txt='الورقة'):
    out = []
    for r, i in zip(rows, ids):
        out.append(r + ({'id': i, 'back': [(home, txt)]},) if i else r)
    return out

def score(rows, total):
    out = '  <h3>صحّح نفسك</h3>\n  <table class="t">\n    <tr><th>الفقرة</th><th>النوع</th><th>الدرجة</th><th>لو نقصت، ارجع لـ</th></tr>\n'
    for r in rows:
        out += '    <tr><td>' + r[0] + '</td><td>' + r[1] + '</td><td>' + r[2] + '</td><td>' + ref(r[3]) + '</td></tr>\n'
    return out + '    <tr><th colspan="2">المجموع</th><th>' + total + '</th><th></th></tr>\n  </table>\n'

# ---------- p-phr: the sentences you write ----------
def prow(en, ar):
    return '    <tr><td class="a">' + ar + '</td><td class="e">' + en + '</td></tr>\n'

P.append(page('p-phr', U[6], 'must', 'الجمل اللي تكتبها',
    idea('كل برهان في الفصل مبني من هالجمل. احفظها كقطع جاهزة، وكتابتك تصير أسرع وأوضح للمصحح.') +
    '  <table class="bi">\n    <tr><th>متى تكتبها</th><th>الجملة</th></tr>\n' +
    prow(r'We proceed by induction. Since …, the statement is true for \(n = 1\).', 'الأساس (أو n = 0، أو n = m).') +
    prow(r'Assume that … for an arbitrary positive integer \(k\).', 'الفرض العادي.') +
    prow(r'Assume that … where \(k \ge m\).', 'الفرض لما البداية m.') +
    prow(r'Assume … for all integers \(i\) with \(1 \le i \le k\).', 'الفرض القوي.') +
    prow(r'We show that …', 'المطلوب، قبل الحساب.') +
    prow(r'By the inductive hypothesis, …', 'في السطر اللي تستخدم فيه الفرض (الأزرق في الملزمة).') +
    prow(r'Then … \(= dx\) for some integer \(x\). … Since … is an integer, \(d \mid\) …', 'القسمة: الفرض معادلة، وآخر سطر.') +
    prow(r'If \(k = 1\), then …. Hence, we may assume that \(k \ge 2\).', 'سطر ★ (k الصغيرة لحالها).') +
    prow(r'Since \(k + 1 \ge 3\), …', 'قبل ما تستخدم قانون التكرار.') +
    prow(r'By the (Strong) Principle of Mathematical Induction, …', 'الختام. الاسم كامل، ومعه Strong لو قوي.') +
    '  </table>\n' +
    box('أشياء تنقص درجات', '''    <ul>
      <li>«''' + lt('for every k') + '''» في الفرض. الصح: ''' + lt('for a positive integer k') + '''.</li>
      <li>تكتب المطلوب كأنه صحيح وتشتغل على طرفيه.</li>
      <li>تنسى الأساس، أو سطر ★ في القوي.</li>
      <li>تكتب «>» بدون سبب (اكتب: since k ≥ 5).</li>
      <li>ختام بدون اسم المبدأ.</li>
    </ul>
''')))

# ---------- p-bank: the 10 plan exercises as an exam paper ----------
BANK = [('المبدأ والترتيب الحسن', 'p-wo', [('6.1', 4)]),
        ('المجاميع', 'p-ex1', [('6.4', 4), ('6.5', 3), ('6.11', 4)]),
        ('القسمة', 'p-ex5', [('6.16', 4)]),
        ('المتباينات والبداية من m', 'p-gen', [('6.19', 3), ('6.22', 4), ('6.27', 4)]),
        ('الاستقراء القوي', 'p-strong', [('6.33', 3), ('6.36', 5)])]

def bank_box(i, name, unit, items):
    out = '  <div class="box paper bank">\n    <div class="bh">' + str(i) + ' · ' + name + ' <span class="small">(شرحه من ' + ref(unit) + ')</span></div>\n'
    for k, mk in items:
        out += q('<b>' + k + '.</b> ' + EX[k] + ' <span class="mk">(' + str(mk) + ' marks)</span>', 's-' + k.replace('.', ''))
    return out + '  </div>\n'

P.append(page('p-bank', U[6], 'must', 'بنك تمارين الخطة: كأنك في الاختبار' + tag('ex', '10 أسئلة'),
    idea('تمارين الخطة العشرة بدون أمثلة ولا تلميحات، زي ورقة الاختبار. حل على ورقتك، وبعدها اضغط «الحل»، ومن الحل ارجع بزر «↩ البنك». الدرجات تقريبية.') +
    ''.join(bank_box(i, n, u, it) for i, (n, u, it) in enumerate(BANK, 1)), style='gap:2.6mm'))

# ---------- p-papers: the chapter 6 questions of past midterms ----------
P.append(page('p-papers', U[6], 'top', 'أوراق الميدات السابقة: حلها كأنك في الاختبار' + tag('past', 'بالحرف'),
    idea('نفس أسئلة الفصل 6 اللي جت في الميدات، بنفس الصيغة والدرجات. شغّل مؤقت، وحل على ورقة بدون ما تطالع الشرح. بعدها اضغط «الحل»، وارجع بزر «↩ ورقة الميدات».') +
    '  <div class="box paper">\n' +
    '    <div class="bh">ورقة 1 · ميد نوفمبر 2026، الجزء حق الفصل 6 <span class="small">(9 من 25 درجة · 20 دقيقة)</span></div>\n' +
    q(r'<b>Q1.</b> 4. For every positive integer \(n\), \(1 + 3 + 5 + \cdots + (2n-1) = n^2\). <span class="mk">(4 marks)</span>', 'm-nov4') +
    q(r'<b>Question 3: (1+4)</b> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\), \(a_2 = 3\), and \(a_n = 2a_{n-1} - a_{n-2}\) for \(n \ge 3\). 1. Find \(a_3\) and \(a_4\). 2. Use the Strong Principle of Mathematical Induction to prove that \(a_n = 2n - 1\) for every positive integer \(n\).', 'm-nov3') +
    '  </div>\n  <div class="box paper">\n' +
    '    <div class="bh">ورقة 2 · ميد 1447 وميد البنات <span class="small">(10 درجات · 20 دقيقة)</span></div>\n' +
    q(r'7- A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\), \(a_2 = 3\) and \(a_n = 2a_{n-1} - a_{n-2}\) for \(n \ge 3\). Then \(a_n = 2n - 1\) for all \(n \in \mathbb{N}\). <span class="mk">(4 marks)</span>', 'm-nov3', 'ميد 1447') +
    q(r'8- For each positive integer \(n\), let \(P(n)\) be a statement. If (1) \(P(1)\) is true and (2) the implication: \(P(k) \Rightarrow P(k+1)\), is true for every positive integer \(k\), then \(P(n)\) is true for every positive integer \(n\). <span class="mk">(3 marks)</span>', 'm-pmi', 'ميد 1447') +
    q(r'4- For each positive integer \(n\), \(1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}\). <span class="mk">(3 marks)</span>', 'm-ex1', 'البنات') +
    '  </div>\n' +
    note('star', 'لاحظ:', 'المتتابعة جت مرتين (1447 ونوفمبر)، ومجموع الفرديات جا مرتين (نهائي 1446 ونوفمبر). والاختبارين الجايين فيهم توأم كل هالأسئلة.'), style='gap:3mm'))

# ---------- mocks in the November format ----------
AFTER = box('بعد ما تخلص', '''    <ul>
      <li>كل برهان فيه الخمس أسطر، والختام فيه اسم المبدأ كامل.</li>
      <li>كتبت «المطلوب» قبل الحساب، وبيّنت وين استخدمت الفرض.</li>
      <li>في القوي: الفرض لكل i من 1 إلى k، وسطر ★، وكلمة Strong.</li>
      <li>جرّبت n = 1 و 2 و 3 قبل ما أقرر صح أو خطأ.</li>
    </ul>
''')

P.append(page('p-mockA', U[6], 'top', 'اختبار تجريبي 1: بصيغة ميد نوفمبر' + tag('ex', '25 دقيقة'),
    idea('جزء الفصل 6 من ميد نوفمبر، بأسئلة توأم، ومعه فقرة قسمة احتياط. شغّل مؤقت 25 دقيقة، وحل على ورقة. لا تفتح الحلول قبل ما يخلص الوقت.') +
    '  <div class="box paper">\n' +
    qrow('<b>Question 1: (4+3)</b> Prove or disprove the following:', '7 marks') +
    q(r'1. For every positive integer \(n\), \(1 + 4 + 7 + \cdots + (3n-2) = \frac{n(3n-1)}{2}\).', 's-mA11') +
    q(r'2. For every nonnegative integer \(n\), \(4 \mid (5^n - 1)\).', 's-mA12') +
    '  </div>\n  <div class="box paper">\n' +
    qrow(r'<b>Question 2: (1+4)</b> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 2\), \(a_2 = 5\), and \(a_n = 2a_{n-1} - a_{n-2}\) for \(n \ge 3\).', '5 marks') +
    q(r'1. Find \(a_3\) and \(a_4\). &nbsp; 2. Use the Strong Principle of Mathematical Induction to prove that \(a_n = 3n - 1\) for every positive integer \(n\).', 's-mA2') +
    '  </div>\n' + AFTER))

P.append(page('p-mockAs', 'حلول الوحدة 6', '', 'حلول الاختبار التجريبي 1' + tag('sol', 'شيّك'),
    W(tagrows([
        ('1.1 True', '', r'Since \(1 = \frac{1 \cdot 2}{2}\), the statement is true for \(n = 1\). Assume that \(1 + 4 + \cdots + (3k-2) = \frac{k(3k-1)}{2}\) for a positive integer \(k\). We show that \(1 + 4 + \cdots + (3k+1) = \frac{(k+1)(3k+2)}{2}\). By the inductive hypothesis, \(1 + 4 + \cdots + (3k+1) = \hyp{\frac{k(3k-1)}{2}} + (3k+1) = \frac{3k^2 + 5k + 2}{2} = \frac{(k+1)(3k+2)}{2}\). By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).',
         r'آخر حد: \(3(k+1) - 2 = 3k + 1\). و \(3k^2 + 5k + 2 = (k+1)(3k+2)\).'),
        ('1.2 True', '', r'When \(n = 0\), \(5^0 - 1 = 0\) and \(4 \mid 0\). Assume that \(4 \mid (5^k - 1)\), where \(k\) is a nonnegative integer. Then \(5^k - 1 = 4x\) for some integer \(x\), so \(5^k = 4x + 1\). We show that \(4 \mid (5^{k+1} - 1)\). Now, \(5^{k+1} - 1 = 5 \cdot \hyp{5^k} - 1 = 5\hyp{(4x + 1)} - 1 = 20x + 4 = 4(5x + 1)\). Since \(5x + 1\) is an integer, \(4 \mid (5^{k+1} - 1)\). By the Principle of Mathematical Induction, \(4 \mid (5^n - 1)\) for every nonnegative integer \(n\).',
         'نفس حركة مثال 5. والبداية من 0.'),
        ('2 (1)', '', r'\(a_3 = 2a_2 - a_1 = 2(5) - 2 = 8\) and \(a_4 = 2a_3 - a_2 = 2(8) - 5 = 11\).', ''),
        ('2 (2)', '', r'We proceed by induction. Since \(a_1 = 3 \cdot 1 - 1 = 2\), the formula holds for \(n = 1\). Assume for an arbitrary positive integer \(k\) that \(a_i = 3i - 1\) for all integers \(i\) with \(1 \le i \le k\). We show that \(a_{k+1} = 3(k+1) - 1 = 3k + 2\). If \(k = 1\), then \(a_{k+1} = a_2 = 5 = 3 \cdot 1 + 2\). Hence, we may assume that \(k \ge 2\). Since \(k + 1 \ge 3\), \(a_{k+1} = 2\hyp{a_k} - \hyp{a_{k-1}} = 2\hyp{(3k - 1)} - \hyp{(3k - 4)} = 3k + 2\). By the Strong Principle of Mathematical Induction, \(a_n = 3n - 1\) for all \(n \in \mathbb{N}\).',
         r'من الفرض: \(a_{k-1} = 3(k-1) - 1 = 3k - 4\).')], ['s-mA11', 's-mA12', 's-mA2', None], 'p-mockA'), title='') +
    score([('1.1', 'مجموع', '4', 'p-nov4'), ('1.2', 'قسمة', '3', 'p-ex5'), ('2', 'متتابعة (قوي)', '5', 'p-nov3')], '12') +
    note('star', 'كل فقرة توأم:', '1.1 توأم مجموع الفرديات، و1.2 توأم مثال 5، وسؤال 2 توأم متتابعة نوفمبر بأرقام ثانية.'), sol=True))

P.append(page('p-mockB', U[6], 'top', 'اختبار تجريبي 2: بعد ما تصحح الأول' + tag('ex', '30 دقيقة'),
    idea('سوّه بعد ما تصحح الأول وترجع للي نقصت فيه. فيه فقرة خطأ لازم تكتشفها، وفقرة متباينة من n ≥ 4. شغّل مؤقت 30 دقيقة.') +
    '  <div class="box paper">\n' +
    qrow('<b>Question 1: (4+3+2)</b> Prove or disprove the following:', '9 marks') +
    q(r'1. For every positive integer \(n\), \(1 \cdot 1! + 2 \cdot 2! + \cdots + n \cdot n! = (n+1)! - 1\).', 's-mB11') +
    q(r'2. For every integer \(n \ge 4\), \(n! \gt 2^n\).', 's-mB12') +
    q(r'3. For every positive integer \(n\), \(3 \mid (2^n - 1)\).', 's-mB13') +
    '  </div>\n  <div class="box paper">\n' +
    qrow(r'<b>Question 2: (1+4)</b> A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 3\), \(a_2 = 5\), and \(a_n = 3a_{n-1} - 2a_{n-2}\) for \(n \ge 3\).', '5 marks') +
    q(r'1. Find \(a_3\) and \(a_4\). &nbsp; 2. Use the Strong Principle of Mathematical Induction to prove that \(a_n = 2^n + 1\) for every positive integer \(n\).', 's-mB2') +
    '  </div>\n' + AFTER))

P.append(page('p-mockBs', 'حلول الوحدة 6', '', 'حلول الاختبار التجريبي 2' + tag('sol', 'شيّك'),
    W(tagrows([
        ('1.1 True', '', r'Since \(1 \cdot 1! = 1 = 2! - 1\), the statement is true for \(n = 1\). Assume that \(1 \cdot 1! + \cdots + k \cdot k! = (k+1)! - 1\) for a positive integer \(k\). We show that \(1 \cdot 1! + \cdots + (k+1)(k+1)! = (k+2)! - 1\). By the inductive hypothesis, \(1 \cdot 1! + \cdots + (k+1)(k+1)! = \hyp{(k+1)! - 1} + (k+1)(k+1)! = (k+1)!\,(1 + k + 1) - 1 = (k+2)! - 1\). By the Principle of Mathematical Induction, the formula holds for every positive integer \(n\).',
         r'التريك: \((k+1)!\) عامل مشترك، و \((k+2)(k+1)! = (k+2)!\).'),
        ('1.2 True', '', r'Since \(4! = 24 \gt 16 = 2^4\), the inequality holds for \(n = 4\). Assume that \(k! \gt 2^k\) where \(k \ge 4\). We show that \((k+1)! \gt 2^{k+1}\). Observe that \((k+1)! = (k+1) \cdot \hyp{k!} \gt (k+1)\hyp{2^k} \ge 2 \cdot 2^k = 2^{k+1}\), since \(k + 1 \ge 2\). By the Principle of Mathematical Induction, \(n! \gt 2^n\) for every integer \(n \ge 4\).',
         'البداية 4: لما n = 3، 6 > 8 خطأ.'),
        ('1.3 False', '', r'Let \(n = 1\). Then \(2^1 - 1 = 1\) and \(3 \nmid 1\). Thus, \(n = 1\) is a counterexample.',
         r'جرّب قبل ما تبرهن: \(2^2 - 1 = 3\) يمشي، بس \(n = 1\) يفشل.'),
        ('2 (1)', '', r'\(a_3 = 3a_2 - 2a_1 = 15 - 6 = 9\) and \(a_4 = 3a_3 - 2a_2 = 27 - 10 = 17\).', ''),
        ('2 (2)', '', r'We proceed by induction. Since \(a_1 = 2^1 + 1 = 3\), the formula holds for \(n = 1\). Assume for an arbitrary positive integer \(k\) that \(a_i = 2^i + 1\) for all integers \(i\) with \(1 \le i \le k\). We show that \(a_{k+1} = 2^{k+1} + 1\). If \(k = 1\), then \(a_{k+1} = a_2 = 5 = 2^2 + 1\). Hence, we may assume that \(k \ge 2\). Since \(k + 1 \ge 3\), \(a_{k+1} = 3\hyp{a_k} - 2\hyp{a_{k-1}} = 3\hyp{(2^k + 1)} - 2\hyp{(2^{k-1} + 1)} = 3 \cdot 2^k - 2^k + 1 = 2^{k+1} + 1\). By the Strong Principle of Mathematical Induction, \(a_n = 2^n + 1\) for all \(n \in \mathbb{N}\).',
         r'\(2 \cdot 2^{k-1} = 2^k\)، و \(3 \cdot 2^k - 2^k = 2 \cdot 2^k\).')], ['s-mB11', 's-mB12', 's-mB13', 's-mB2', None], 'p-mockB'), title='') +
    score([('1.1', 'مجموع', '4', 'p-ex1'), ('1.2', 'متباينة من m', '3', 'p-ex4'), ('1.3', 'خطأ (مثال مضاد)', '2', 'p-gen'), ('2', 'متتابعة (قوي)', '5', 'p-nov3')], '14'), sol=True))

# ---------- p-night ----------
def nb(title, inner):
    return box(title, inner).replace('  <div class="box">', '    <div class="box">')

P.append(page('p-night', 'ورقة ليلة الاختبار', 'top', 'الفصل كله في صفحة',
    '  <h3>القالب (خمس أسطر في كل برهان)</h3>\n' +
    W([('1', 'الأساس', r'Since …, the statement is true for \(n = 1\) (or \(0\), or \(m\)).', ''),
       ('2', 'الفرض', r'Assume that … for an arbitrary positive integer \(k\).  [strong: for all \(i\) with \(1 \le i \le k\)]', ''),
       ('3', 'المطلوب', r'We show that … (the statement with \(k + 1\)).', ''),
       ('4', 'الخطوة', r'By the inductive hypothesis, … , as desired.', '', HL),
       ('5', 'الختام', r'By the (Strong) Principle of Mathematical Induction, …', '')], title='') +
    '  <div class="grid2">\n' +
    nb('حركة الخطوة لكل نوع', '''    <ul>
      <li><b>مجموع:</b> افصل آخر حد، وبدّل الباقي بالفرض.</li>
      <li><b>قسمة:</b> الفرض معادلة، وطلّع حد k + 1 من حد k، وعوّض.</li>
      <li><b>متباينة:</b> ابدأ من طرف k + 1، والفرض، وخطوة «أكبر من» بسبب.</li>
      <li><b>قوي:</b> قانون التكرار، والحدّين من الفرض، وسطر&nbsp;★.</li>
      <li><b>n أعداد أو مجموعات (6.19):</b> أول k منها اعتبرها شي واحد، وطبّق حقيقة الاثنين.</li>
    </ul>
''') +
    nb('الفخاخ', '''    <ul>
      <li>اقرأ البداية: positive من 1، nonnegative من 0.</li>
      <li>آخر حد عند k + 1: عوّض n = k + 1 فيه.</li>
      <li>«''' + lt('for every k') + '''» في الفرض غلط.</li>
      <li>القوي بدون سطر ★ ناقص.</li>
      <li>جرّب n = 1، 2، 3 قبل أي برهان.</li>
    </ul>
''') +
    '  </div>\n' +
    '  <div class="grid2">\n' +
    nb('برهان المبدأ (3 درجات)', chain(['نعكس', 'S لها أصغر عنصر s', r'\(s \ge 2\)', r'\(P(s-1)\) صح', r'\(P(s)\) صح', 'تناقض'])) +
    nb('أسئلة الاختبارات السابقة', r'''    <ul>
      <li>مجموع الفرديات (نوفمبر، ونهائي 1446) <span class="pg ref" data-to="p-nov4"></span></li>
      <li>المتتابعة \(2n - 1\)، وأوجد \(a_3\) و \(a_4\) (1447، ونوفمبر) <span class="pg ref" data-to="p-nov3"></span></li>
      <li>برهان المبدأ (1447) <span class="pg ref" data-to="p-pmi"></span></li>
      <li>مجموع 1 إلى n (البنات) <span class="pg ref" data-to="p-ex1"></span></li>
    </ul>
''') +
    '  </div>\n' +
    '  <p class="small"><b>توقّع البديل:</b> مجموع ثاني، ومتتابعة ثانية (مثل مثال 7)، ويمكن قسمة أو متباينة.</p>\n'))

save('g_u6.html', P)
