# Guess the Purpose

Before diving into the details, can you guess the purpose of the epsilon-delta definition of a limit?

In mathematical analysis, the \(\epsilon\)-\(\delta\) definition of a limit is used to formally define the limit of a function at a point. Specifically, the definition states:

Let \( f(x) \) be a function defined on an open interval containing \( c \) (except possibly at \( c \) itself). We say that the limit of \( f(x) \) as \( x \) approaches \( c \) is \( L \), and we write

\[ \lim_{x \to c} f(x) = L \]

if for every \(\epsilon > 0\) there exists a \(\delta > 0\) such that

\[ 0 < |x - c| < \delta \implies |f(x) - L| < \epsilon. \]

Let’s consider an example problem to illustrate this concept. We will approximate \(\delta\) for given \(\epsilon\) in a simple \(\epsilon\)-\(\delta\) problem.

### Example Problem

Consider the function \( f(x) = 2x \). We want to show that

\[ \lim_{x \to 3} 2x = 6. \]

### Solution

1. **Start with the \(\epsilon\)-\(\delta\) definition:**

   For every \(\epsilon > 0\), we must find a \(\delta > 0\) such that if \(0 < |x - 3| < \delta\), then \(|2x - 6| < \epsilon\).

2. **Simplify the condition \(|2x - 6| < \epsilon\):**

   \[ |2x - 6| = 2|x - 3|. \]

   We want:

   \[ 2|x - 3| < \epsilon. \]

3. **Solve for \(|x - 3|\):**

   \[ |x - 3| < \frac{\epsilon}{2}. \]

4. **Choose \(\delta\) to satisfy this condition:**

   \[ \delta = \frac{\epsilon}{2}. \]

Therefore, for the given \(\epsilon > 0\), we can choose \(\delta = \frac{\epsilon}{2}\) to satisfy the \(\epsilon\)-\(\delta\) definition of the limit.

### Summary

We have shown that for the function \( f(x) = 2x \) and the point \( c = 3 \), the limit is \( L = 6 \). For any \(\epsilon > 0\), we can choose \(\delta = \frac{\epsilon}{2}\) so that \( 0 < |x - 3| < \delta \) implies \(|2x - 6| < \epsilon\).

This example demonstrates the process of finding an appropriate \(\delta\) for a given \(\epsilon\) in the context of the \(\epsilon\)-\(\delta\) definition of a limit.
