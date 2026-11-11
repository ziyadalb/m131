import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h5 import *
P = []
U4 = U[4] + ' · 5.4'

# ---------- p-u4: idea + card + slides Examples 8, 9 ----------
P.append(page('p-u4', U4, 'must', 'براهين الوجود: الفكرة' + tag('sol', 'مثالا السلايدات 8 و9'),
    idea('جملة «يوجد…» (' + lt('There exists') + ') يكفيها مثال واحد صحيح: تختاره، وتتحقق منه بالأرقام. (عكس «لكل»: هذي تنقضها بمثال واحد.)') +
    stmt([(r'<span class="lb">Definition.</span> An <i>existence theorem</i> is expressed as \(\exists x \in S, R(x)\): There exists \(x \in S\) such that \(R(x)\). Such a statement is true if \(R(x)\) is true for some \(x \in S\). Its proof is called an <i>existence proof</i>.',
           r'نظرية الوجود تقول إن فيه شي له خاصية معينة: «يوجد x في S بحيث \(R(x)\)». وتكون صحيحة لو \(R(x)\) صحيحة لعنصر واحد على الأقل. وبرهانها اسمه <b>برهان وجود</b>.')]) +
    qbox(r'<span class="lb">Result.</span> There exists an integer whose cube equals its square.',
         r'يوجد عدد صحيح مكعبه يساوي مربعه. <b>نفكر:</b> نجرب 2: مكعبه 8 ومربعه 4 ' + NO + r'. نجرب 1: مكعبه 1 ومربعه 1 ' + OK, lab='مثال 8') +
    W([('', 'نكتب', r'Since \(1^3 = 1^2 = 1\), the integer 1 has the desired property.', 'مكعب 1 ومربعه يساوون 1، فهو العدد المطلوب. سطر واحد يكفي.')], title='') +
    qbox(r'<span class="lb">Result.</span> There exist real numbers \(a\) and \(b\) such that \((a + b)^2 = a^2 + b^2\).',
         r'يوجد عددين حقيقيين a و b بحيث \((a + b)^2 = a^2 + b^2\). <b>نفكر (في المسودة):</b> نفك الأيسر: \(a^2 + 2ab + b^2 = a^2 + b^2\)، يعني \(2ab = 0\). فيكفي واحد منهم صفر: \(a = 1\) و \(b = 0\).', lab='مثال 9') +
    W([('1', 'اختر', r'Let \(a = 1\) and \(b = 0\).', 'نعيّن القيم.'),
       ('2', 'تحقق', r'Then \((a + b)^2 = (1 + 0)^2 = 1^2 = 1^2 + 0^2 = a^2 + b^2\).', 'نتحقق بالأرقام أن الطرفين متساويين.')], title='') +
    card('بطاقة الخطوات: برهان الوجود', [
        ('اختر', 'عيّن الشي بالأرقام: ' + lt(r'Let \(x = \ldots\)') + ' أو ' + lt('Consider …')),
        ('تحقق', 'من كل شرط في السؤال، بالأرقام.'),
        ('اختم', lt('Thus, … has the desired property.'))]),
    style='gap:3mm'))

# ---------- p-ex10: slides Example 10 + 5.42 ----------
P.append(page('p-ex10', U[4], 'must', 'مثال: وجود بحالتين' + tag('sol', 'مثال السلايدات 10') + tag('ex', 'دورك'),
    qbox(r'<span class="lb">Result.</span> There exist irrational numbers \(a\) and \(b\) such that \(a^b\) is rational.',
         r'يوجد عددين غير نسبيين a و b بحيث \(a^b\) نسبي. <b>نفكر:</b> المرشح \(\sqrt{2}^{\sqrt{2}}\). ما نعرف هو نسبي أو لا، والحلو أننا ما نحتاج نعرف: لو نسبي خلصنا، ولو غير نسبي نرفعه للأس \(\sqrt{2}\) فيطلع 2. في الحالتين لقينا a و b.') +
    W([('1', 'حالة 1', r'Consider the number \(\sqrt{2}^{\sqrt{2}}\). Of course, this number is either rational or irrational. <i>Case 1.</i> \(\sqrt{2}^{\sqrt{2}}\) is rational. Then we can take \(a = b = \sqrt{2}\) and we have the desired result.',
        r'العدد يا نسبي يا غير نسبي. لو نسبي، \(a = b = \sqrt{2}\) تكفي.'),
       ('2', 'حالة 2', r'<i>Case 2.</i> \(\sqrt{2}^{\sqrt{2}}\) is irrational. In this case, consider \(a^b\), where \(a = \sqrt{2}^{\sqrt{2}}\) and \(b = \sqrt{2}\). Observe that \[a^b = \left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}} = \sqrt{2}^{\sqrt{2} \cdot \sqrt{2}} = \sqrt{2}^{\,2} = 2,\] which is rational.',
        r'لو غير نسبي، نأخذه هو a، و \(b = \sqrt{2}\).')], title='نكتب (برهان السلايدات)') +
    duork('5.42', r'<span class="lb">5.42.</span> Show that there exist a rational number \(a\) and an irrational number \(b\) such that \(a^b\) is rational.',
          r'اثبت أنه يوجد عدد نسبي a وعدد غير نسبي b بحيث \(a^b\) نسبي. أسهل من المثال: فكّر في عدد نسبي أي أس تحطه له يطلع نفس العدد.') +
    W([('1', 'اختر', None, None, 'b1'), ('2', 'تحقق', None, None, 'b2'), ('3', 'اختم', None, None, 'b1')], title=''), style='gap:3mm'))

# ---------- p-ivt: IVT + slides Example 11 ----------
P.append(page('p-ivt', U[4], 'must', 'القيمة الوسطى: وجود حل بدون ما تلقاه' + tag('sol', 'مثال السلايدات 11'),
    idea('أحياناً ما نقدر نحسب الحل. بس نقدر نثبت أنه موجود: لو الدالة سالبة عند طرف وموجبة عند الثاني، فلازم تمر بالصفر بينهم.') +
    stmt([(r'<span class="lb">The Intermediate Value Theorem of Calculus.</span> If \(f\) is a function that is continuous on the closed interval \([a, b]\) and \(k\) is a number between \(f(a)\) and \(f(b)\), then there exists a number \(c \in (a, b)\) such that \(f(c) = k\).',
           r'لو f متصلة على \([a, b]\)، و k عدد بين \(f(a)\) و \(f(b)\)، فيوجد c بين a و b بحيث \(f(c) = k\). وفي أسئلتنا \(k = 0\).')]) +
    qbox(r'<span class="lb">Result.</span> The equation \(x^5 + 2x - 5 = 0\) has a real number solution between \(x = 1\) and \(x = 2\).',
         'المعادلة لها حل حقيقي بين 1 و2.', lab='مثال 11') +
    think(r'نفكر بأرقام: \(f(x) = x^5 + 2x - 5\)', before=tbl([r'\(x\)', '1', '1.2', '1.25', '1.5', '2'],
              [[r'\(f(x)\)', r'\(-2\)', r'\(\approx -0.11\)', r'\(\approx 0.55\)', r'\(\approx 5.59\)', '31']], ltr=True),
          extra=r'    <p>الإشارة تقلب من سالب لموجب بين 1.2 و1.25، فالحل هناك (تقريباً 1.21). والبرهان ما يحتاج هالحساب: يكفي الطرفين.</p>' + '\n') +
    W([('1', 'الدالة', r'Let \(f(x) = x^5 + 2x - 5\). Since \(f\) is a polynomial function, it is continuous on the set of all real numbers and so \(f\) is continuous on the interval \([1, 2]\).',
        'كثيرة حدود، فهي متصلة. هذا شرط النظرية، لا تنساه.'),
       ('2', 'الطرفين', r'Now, \(f(1) = -2\) and \(f(2) = 31\). Since 0 is between \(f(1)\) and \(f(2)\), it follows by the Intermediate Value Theorem of Calculus that there is a number \(c\) between 1 and 2 such that \(f(c) = c^5 + 2c - 5 = 0\). Hence, \(c\) is a solution.',
        r'نحسب الطرفين: \(-2\) و31. والصفر بينهم، فالنظرية تعطينا c.')], title='نكتب (برهان السلايدات)') +
    recall('الخطوات الثلاث: الدالة متصلة ← الطرفين بإشارتين مختلفتين ← النظرية تعطي c.')))

# ---------- p-uniq: slides Example 12 + 5.46 ----------
P.append(page('p-uniq', U[4], 'must', 'مثال: الحل وحيد' + tag('sol', 'مثال السلايدات 12') + tag('ex', 'دورك'),
    qbox(r'<span class="lb">Result.</span> The equation \(x^5 + 2x - 5 = 0\) has a unique real number solution between \(x = 1\) and \(x = 2\).',
         r'نفس المعادلة، والحل <b>وحيد</b> (' + lt('unique') + r'). <b>نفكر:</b> الوجود ثبت في مثال 11. للوحدانية نفترض حلين \(a \lt b\). بس الدالة متزايدة: \(a^5 \lt b^5\) و \(2a \lt 2b\)، فيطلع \(0 \lt 0\). تناقض!', lab='مثال 12') +
    W([('1', 'نعكس', r'Assume, to the contrary, that the equation \(x^5 + 2x - 5 = 0\) has two distinct real number solutions \(a\) and \(b\) between \(x = 1\) and \(x = 2\). We may assume that \(a \lt b\).',
        'نفترض فيه حلين مختلفين، ونسمي الأصغر a.'),
       ('2', 'نمشي', r'Since \(1 \lt a \lt b \lt 2\), it follows that \(a^5 + 2a - 5 \lt b^5 + 2b - 5\). On the other hand, \(a^5 + 2a - 5 = 0\) and \(b^5 + 2b - 5 = 0\).',
        'الدالة متزايدة، و a و b حلول (يعني قيمتها عندهم صفر).'),
       ('3', 'تناقض', r'Thus, \(0 = a^5 + 2a - 5 \lt b^5 + 2b - 5 = 0\), which produces a contradiction.', 'طلع أن صفر أصغر من صفر.')], title='نكتب (برهان السلايدات)') +
    duork('5.46', r'<span class="lb">5.46.</span> Prove that there exists a unique real number solution to the equation \(x^3 + x^2 - 1 = 0\) between \(x = 2/3\) and \(x = 1\).',
          r'اثبت أن للمعادلة حل حقيقي واحد بس بين \(2/3\) و1. جزأين: الوجود (مثال 11)، ثم الوحدانية (مثال 12).') +
    recall(r'قبل ما تكتب: احسب \(f(2/3)\) و \(f(1)\) في المسودة، وفكّر ليش f متزايدة بين \(2/3\) و1.') +
    W([('1', 'الوجود', None, None, 'b3'), ('2', 'الوحدانية', None, None, 'b3')], title='', cls='tpl grow') +
    hints([r'<b>تلميح:</b> \((2/3)^3 = 8/27\) و \((2/3)^2 = 4/9 = 12/27\).']),
    style='gap:2.6mm'))

# ---------- p-cases: book proof (n >= 7, 2a + 3b) + 5.51 ----------
P.append(page('p-cases', U[4], 'must', 'مثال: وجود «لكل n» بالحالات' + tag('sol', 'برهان من الكتاب') + tag('ex', 'دورك'),
    qbox(r'<span class="lb">Result.</span> For every integer \(n \ge 7\), there exist positive integers \(a\) and \(b\) such that \(n = 2a + 3b\).',
         r'كل عدد صحيح من 7 وفوق ينكتب \(2a + 3b\)، حيث a و b موجبين. <b>نفكر:</b> \(7 = 2 \cdot 2 + 3 \cdot 1\) و \(8 = 2 \cdot 1 + 3 \cdot 2\). بس الجملة «لكل n»، فنقسم n لزوجي وفردي، ونعيّن a و b بدلالة q.') +
    W([('1', 'الحالات', r'Let \(n\) be an integer such that \(n \ge 7\). Since \(n\) is even or odd, either \(n = 2q\) or \(n = 2q + 1\) for some integer \(q\). We consider these two cases.', 'n يا زوجي يا فردي.'),
       ('2', 'حالة 1', r'<i>Case 1.</i> \(n = 2q\). Since \(n \ge 7\), it follows that \(q \ge 4\). Thus, \(n = 2q = 2(q - 3) + 6 = 2(q - 3) + 3 \cdot 2\). Since \(q \ge 4\), it follows that \(q - 3 \in \mathbb{N}\).',
        r'نأخذ ستة من n: \(a = q - 3\) و \(b = 2\). و \(q \ge 4\) لأن \(2q \ge 7\)، وهذا اللي يخلي a موجب.'),
       ('3', 'حالة 2', r'<i>Case 2.</i> \(n = 2q + 1\). Since \(n \ge 7\), it follows that \(q \ge 3\). Thus, \(n = 2q + 1 = 2(q - 1) + 2 + 1 = 2(q - 1) + 3 \cdot 1\). Since \(q \ge 3\), it follows that \(q - 1 \in \mathbb{N}\).',
        r'نأخذ ثلاثة من n: \(a = q - 1\) و \(b = 1\).')], title='نكتب (برهان الكتاب)') +
    duork('5.51', r'<span class="lb">5.51.</span> Prove for every integer \(n \ge 8\) that there exist nonnegative integers \(a\) and \(b\) such that \(n = 3a + 5b\).',
          r'كل عدد صحيح من 8 وفوق ينكتب \(3a + 5b\)، حيث a و b أعداد صحيحة غير سالبة. (نفس مثال 8 في ملزمة الفصل 6، بس هنا بالحالات.)') +
    W([('1', 'حالة 1', None, None, 'b1'), ('2', 'حالة 2', None, None, 'b2'), ('3', 'حالة 3', None, None, 'b2')], title='') +
    hints([r'<b>تلميح:</b> اقسم حسب الباقي على 3: \(n = 3q\) أو \(3q + 1\) أو \(3q + 2\). في \(3q + 1\) خذ عشرة (\(5 \cdot 2\))، وفي \(3q + 2\) خذ خمسة. وشرط q في كل حالة.']),
    style='gap:2.8mm'))

# ---------- p-553: extra twin + 5.53 ----------
P.append(page('p-553', U[4], 'must', 'مثال: عيّن الشي، وتحقق من كل شرط' + tag('sol', 'مثال إضافي') + tag('ex', 'دورك'),
    qbox(r'Prove that there exist three distinct primes whose sum is also a prime.',
         'اثبت أنه يوجد ثلاث أعداد أولية مختلفة مجموعها عدد أولي. (مثال إضافي مو من الكتاب، عشان تشوف نوع 5.53 محلول.)') +
    think('نفكر', ['لو 2 واحد منهم، فالمجموع = 2 + عددين فرديين = عدد زوجي أكبر من 2، يعني مو أولي. فـ 2 ممنوع، ونختار أعداد أولية فردية.',
                   r'نجرب: \(3 + 5 + 7 = 15 = 3 \cdot 5\) ' + NO + r' و \(3 + 5 + 11 = 19\)، و19 أولي ' + OK]) +
    W([('1', 'اختر', r'Let \(p = 3\), \(q = 5\) and \(r = 11\). These are three distinct primes.', 'نعيّن الأعداد، ونتأكد أنها أولية ومختلفة.'),
       ('2', 'تحقق', r'Since \(p + q + r = 3 + 5 + 11 = 19\) and 19 is a prime, the primes 3, 5 and 11 have the desired property.', 'نحسب المجموع ونتأكد أنه أولي.')], title='نكتب') +
    duork('5.53', r'<span class="lb">5.53.</span> Prove that there exists a set \(S\) of four distinct primes such that the sum of every three elements of \(S\) is also a prime.',
          'اثبت أنه يوجد مجموعة S فيها أربع أعداد أولية مختلفة، ومجموع أي ثلاثة منها عدد أولي.') +
    recall('قبل ما تكتب: ليش 2 ممنوع هنا بعد؟ وكم مجموع ثلاثي لازم تتحقق منه؟') +
    W([('1', 'اختر', None, None, 'b1'), ('2', 'تحقق', None, None, 'b3')], title='', cls='tpl grow') +
    hints(['<b>تلميح:</b> جرّب أعداد بين 5 و23. والأعداد الأولية تحت 50: 2، 3، 5، 7، 11، 13، 17، 19، 23، 29، 31، 37، 41، 43، 47.'])))

# ---------- solutions ----------
P.append(page('p-s4', 'حلول الوحدة 4', '', 'الحلول' + tag('sol', 'شيّك'),
    '  <h3>تمرين 5.42</h3>\n' +
    W([('', 'الجواب', r'Let \(a = 1\) and \(b = \sqrt{2}\). Then \(a\) is rational and \(b\) is irrational. Since \(a^b = 1^{\sqrt{2}} = 1\) and 1 is rational, the numbers \(a\) and \(b\) have the desired property.',
        r'1 أس أي عدد يساوي 1. (\(\sqrt{2}\) غير نسبي من الوحدة 2.)')], title='') +
    '  <h3>تمرين 5.46</h3>\n' +
    W([('1', 'الوجود', r'Let \(f(x) = x^3 + x^2 - 1\). Since \(f\) is a polynomial function, it is continuous on \([2/3, 1]\). Now, \(f(2/3) = \frac{8}{27} + \frac{12}{27} - \frac{27}{27} = -\frac{7}{27}\) and \(f(1) = 1\). Since 0 is between \(f(2/3)\) and \(f(1)\), it follows by the Intermediate Value Theorem of Calculus that there is a number \(c\) between \(2/3\) and 1 such that \(f(c) = 0\).',
        r'\(f(2/3)\) سالب و \(f(1)\) موجب، فالنظرية تعطي حل بينهم.'),
       ('2', 'الوحدانية', r'Assume, to the contrary, that the equation has two distinct real number solutions \(a\) and \(b\) between \(x = 2/3\) and \(x = 1\). We may assume that \(a \lt b\). Since \(0 \lt a \lt b\), it follows that \(a^3 \lt b^3\) and \(a^2 \lt b^2\), and so \(a^3 + a^2 - 1 \lt b^3 + b^2 - 1\). Thus, \(0 = a^3 + a^2 - 1 \lt b^3 + b^2 - 1 = 0\), which is a contradiction.',
        r'نفس مثال 12: الدالة متزايدة، فحلين يعطون \(0 \lt 0\).')], title='') +
    '  <h3>تمرين 5.53</h3>\n' +
    W([('', 'الجواب', r'Let \(S = \{5, 7, 17, 19\}\). The elements of \(S\) are four distinct primes, and \(5 + 7 + 17 = 29\), \(5 + 7 + 19 = 31\), \(5 + 17 + 19 = 41\) and \(7 + 17 + 19 = 43\) are all primes. Thus \(S\) has the desired property.',
        r'أربع مجاميع ثلاثية، كلها أولية. وفيه أجوبة ثانية صحيحة، مثل \(\{7, 11, 13, 23\}\): مجاميعها 31 و41 و43 و47.')], title=''),
    sol=True))

P.append(page('p-s4b', 'حلول الوحدة 4', '', 'حل تمرين 5.51' + tag('sol', 'شيّك'),
    W([('1', 'الحالات', r'Let \(n\) be an integer such that \(n \ge 8\). Then \(n = 3q\), \(n = 3q + 1\) or \(n = 3q + 2\) for some integer \(q\). We consider these three cases.', 'الباقي لما نقسم على 3: يا 0 يا 1 يا 2.'),
       ('2', 'حالة 1', r'<i>Case 1.</i> \(n = 3q\). Since \(n \ge 8\), it follows that \(q \ge 3\). Thus, \(n = 3q + 5 \cdot 0\). Let \(a = q\) and \(b = 0\).', r'مثل \(9 = 3 \cdot 3 + 5 \cdot 0\).'),
       ('3', 'حالة 2', r'<i>Case 2.</i> \(n = 3q + 1\). Since \(n \ge 8\), it follows that \(q \ge 3\). Thus, \(n = 3q + 1 = 3(q - 3) + 10 = 3(q - 3) + 5 \cdot 2\). Let \(a = q - 3\) and \(b = 2\). Since \(q \ge 3\), \(a \ge 0\).',
        r'نأخذ عشرة من n. مثل \(10 = 3 \cdot 0 + 5 \cdot 2\) و \(13 = 3 \cdot 1 + 5 \cdot 2\).'),
       ('4', 'حالة 3', r'<i>Case 3.</i> \(n = 3q + 2\). Since \(n \ge 8\), it follows that \(q \ge 2\). Thus, \(n = 3q + 2 = 3(q - 1) + 5 \cdot 1\). Let \(a = q - 1\) and \(b = 1\). Since \(q \ge 2\), \(a \ge 1\).',
        r'نأخذ خمسة من n. مثل \(8 = 3 \cdot 1 + 5 \cdot 1\) و \(11 = 3 \cdot 2 + 5 \cdot 1\).'),
       ('5', 'الختام', r'In each case, \(a\) and \(b\) are nonnegative integers such that \(n = 3a + 5b\).', 'في كل حالة لقينا a و b غير سالبين.')], title='') +
    note('trick', 'ليش \\(q \\ge 3\\) في حالة 2؟', r'لأن \(3q + 1 \ge 8\) يعني \(q \ge 7/3\)، و q عدد صحيح، فـ \(q \ge 3\). وهذا اللي يخلي \(a = q - 3\) غير سالب.') +
    box('راجع نفسك (دقيقتين)', '''    <ul class="chk">
      <li><span class="cb"></span>أقول خطوات الوجود من ذاكرتي: اختر، تحقق، اختم.</li>
      <li><span class="cb"></span>أعرف متى أحتاج حالات (لما الجملة «لكل n يوجد…»).</li>
      <li><span class="cb"></span>أكتب «حل وحيد» بجزأيه: القيمة الوسطى، ثم التناقض.</li>
    </ul>
'''), sol=True))

save('e_u4.html', P)
