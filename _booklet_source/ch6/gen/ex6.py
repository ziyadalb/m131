# Exact book texts of the 10 plan exercises of chapter 6 (taken from the checked booklet)
EX = {
    '6.1': r'''Which of the following sets are well-ordered?<br>(a) \(S = \{x \in \mathbb{Q} : x \ge -10\}\) &nbsp;&nbsp; (b) \(S = \{-2, -1, 0, 1, 2\}\)<br>(c) \(S = \{x \in \mathbb{Q} : -1 \le x \le 1\}\) &nbsp;&nbsp; (d) \(S = \{p : p \text{ is a prime}\} = \{2, 3, 5, 7, 11, 13, 17, \ldots\}\)''',
    '6.4': r'''Prove that \(1 + 3 + 5 + \cdots + (2n-1) = n^2\) for every positive integer \(n\) (1) by mathematical induction and (2) by adding \(1 + 3 + 5 + \cdots + (2n-1)\) and \((2n-1) + (2n-3) + \cdots + 1\).''',
    '6.5': r'''Use mathematical induction to prove that \(1 + 5 + 9 + \cdots + (4n-3) = 2n^2 - n\) for every positive integer \(n\).''',
    '6.11': r'''Prove that \(\frac{1}{3\cdot 4} + \frac{1}{4\cdot 5} + \cdots + \frac{1}{(n+2)(n+3)} = \frac{n}{3n+9}\) for every positive integer \(n\).''',
    '6.16': r'''Prove that \(7 \mid \left[3^{4n+1} - 5^{2n-1}\right]\) for every positive integer \(n\).''',
    '6.19': r'''Prove the following implication for every integer \(n \ge 2\): If \(x_1, x_2, \ldots, x_n\) are any \(n\) real numbers such that \(x_1 \cdot x_2 \cdots x_n = 0\), then at least one of the numbers \(x_1, x_2, \ldots, x_n\) is \(0\). (Use the fact that if the product of two real numbers is \(0\), then at least one of the numbers is \(0\).)''',
    '6.22': r'''Prove that \(3^n \gt n^2\) for every positive integer \(n\).''',
    '6.27': r'''Prove that \(1 + \frac{1}{4} + \frac{1}{9} + \cdots + \frac{1}{n^2} \le 2 - \frac{1}{n}\) for every positive integer \(n\).''',
    '6.33': r'''A sequence \(\{a_n\}\) is defined recursively by \(a_1 = 1\) and \(a_n = 2a_{n-1}\) for \(n \ge 2\). Conjecture a formula for \(a_n\) and verify that your conjecture is correct.''',
    '6.36': r'''Consider the sequence \(F_1, F_2, F_3, \ldots\), where \(F_1 = 1\), \(F_2 = 1\), \(F_3 = 2\), \(F_4 = 3\), \(F_5 = 5\) and \(F_6 = 8\). The terms of this sequence are called <i>Fibonacci numbers</i>. (a) Define the sequence of Fibonacci numbers by means of a recurrence relation. (b) Prove that \(2 \mid F_n\) if and only if \(3 \mid n\).''',
}
