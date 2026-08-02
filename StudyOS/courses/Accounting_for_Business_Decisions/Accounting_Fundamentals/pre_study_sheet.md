# Pre-Study Sheet — Accounting for Business Decisions > Accounting_Fundamentals

> Big picture only. Read this before the cluster study sheet.

## What this topic is fundamentally about

**A business is too big to hold in your head, and your bank balance lies to you.** Everything in this
topic is machinery built to solve those two problems.

Your workbook says the first one outright — *"overcoming the limitation of human memory"* (p.6). A man
selling fruit from a cart knows his whole business. Fifty transactions a day across three employees,
and he doesn't. That's the boring half.

**The second half is the real reason, and your workbook never states it.** Watch a bank balance lie
three times:

| Event | What the bank balance says | What is actually true |
|---|---|---|
| Sell Rs 5,00,000 of goods **on credit** | Nothing happened | You are Rs 5,00,000 richer |
| **Borrow** Rs 10,00,000 | You're up Rs 10,00,000 | You are not one rupee richer. You owe every paisa. |
| Buy Rs 3,00,000 of **machinery** | You're down Rs 3,00,000 | You lost nothing. You swapped cash for a machine. |

**Three different questions hide behind that one number:**

1. **What do we own, and who has a claim on it?** → the **Balance Sheet**
2. **Did we get richer by operating?** → the **Income Statement**
3. **Can we pay people on Friday?** → **Cash Flow**

Your bank balance answers question 3 and lies about 1 and 2.

**Accounting is the discipline of separating those three questions so they stop contaminating each
other.** That is the point. "Recording transactions" is the mechanism, not the purpose.

**Why this kills real companies:** profit and cash are different numbers. A *profitable* business can
die of cash starvation — sell hard on credit, the income statement looks superb, and you cannot make
payroll. It is the most common way a growing business goes under.

## How the clusters connect

**One cluster** — `01_Recording_Financial_Transactions` — covering all 73 nodes. Structured as eight
acts, ordered by **when a business actually needs each tool**, not by terminology.

```
   AN EVENT HAPPENS
         │
         ▼
   ┌──────────────────────┐        NO
   │ Is it a transaction? │──────────────► nothing is recorded
   └──────────┬───────────┘                (an order. a promise.
              │ YES                          an intention.)
              ▼
   ╔══════════════════════╗
   ║      JOURNAL         ║   sorted by DATE
   ║   "the day book"     ║   answers: what happened, and when?
   ╚══════════╤═══════════╝
              │  posting
              ▼
   ╔══════════════════════╗
   ║      LEDGER          ║   sorted by ACCOUNT
   ║  "the book that      ║   answers: how much, in total?
   ║   stays put"         ║
   ╚══════════╤═══════════╝
              │  balancing
              ▼
   ╔══════════════════════╗
   ║   TRIAL BALANCE      ║   check: Σ Debits = Σ Credits
   ║   "the checkpoint"   ║   catches: arithmetic
   ╚══════════╤═══════════╝   misses:  truth
              │
      ┌───────┴────────┐
      ▼                ▼
 ╔═════════════╗  ╔═════════════╗
 ║   INCOME    ║  ║  BALANCE    ║
 ║  STATEMENT  ║  ║   SHEET     ║
 ╟─────────────╢  ╟─────────────╢
 ║ did we get  ║  ║ what do we  ║
 ║  richer?    ║  ║ have, and   ║
 ║             ║  ║ who owns it?║
 ║ a PERIOD    ║  ║ an INSTANT  ║
 ║ (a video)   ║  ║ (a photo)   ║
 ╚═════════════╝  ╚═════════════╝
```

**Same money, four views. Each box exists because the box before it cannot answer the next question.**

| Act | The moment | What it forces |
|---|---|---|
| 1 | Money goes in | Where did it come from? → **A = L + E** |
| 2 | Something happened — write it down | Two sides to every event → the **journal** |
| 3 | To write it, name both accounts | A thing, a person, or a reason → the **three account types** |
| 4 | Not everything is cash | **Liabilities** become real. And an **order is not a transaction.** |
| 5 | *"How much do we owe?"* | Time-order can't total → the **ledger** |
| 6 | Did we slip? | The **trial balance** — and what it cannot catch |
| 7 | *"So did we make money?"* | The **statements**. The payoff. |
| 8 | The rules that stop you lying | **Concepts and conventions** — last, because you must see the statement before you can see the lie |

## The single most important concept

**Assets = Liabilities + Equity.**

**Your workbook never states this.** It teaches Dual Aspect (p.6) and the golden rules (p.12) as
separate things you must accept. That is why they feel arbitrary — **as presented, they are.**

**Why it is true:** every rupee of stuff the business controls came from **somewhere**. There are
exactly two somewheres:

- **Someone lent it** → a liability
- **The owner put it in, or the business earned it** → equity

**There is no third source. Nothing appears from nowhere.**

So A = L + E is **not a rule. It is arithmetic.** It is "everything came from somewhere," written
down. It cannot be false.

**The two sides answer two different questions about the same rupees:**

| Left — **Assets** | Right — **Liabilities + Equity** |
|---|---|
| **What we have** | **Where it came from** |
| **Uses** of money | **Sources** of money |
| Cash, machinery, stock, receivables | Lenders' claims + the owner's claim |

**One pile of money. Left says what shape it's in. Right says who supplied it.** They are equal
because they are the same money described twice — **not** two independent quantities that happen to
match.

**This is why the sheet balances at all:** by construction, not by effort.

**Everything else falls out of it:**

- **Double-entry** — if every resource has a source, every event touches both. Two sides, always. Not
  a clever technique someone invented; a consequence of stuff not appearing from nowhere.
- **Debit and credit** — **directions, not meanings.** Debit *is* left. Credit *is* right. Assets
  increase by debit because they **are on the left**.
- **The golden rules** — all three collapse into one question: *which side of the equation does this
  live on?* Your rote-trained peers memorized three rules. You can derive them.

**If you remember nothing else:** *Debit means left. Left is where assets and equity-reductions live.
Everything else is bookkeeping.*
