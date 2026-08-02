# Study Sheet — Accounting for Business Decisions > Accounting_Fundamentals > 01_Recording_Financial_Transactions

> **WARNING: No held-out validation possible — built on your workbook alone (research declined).
> Ground truth will be your first real assessment attempt. Recalibrate on first mismatch.**
> (`spec.md` §5. This is a claim about *what you'll be assessed on* — not about whether the
> accounting below is correct. See `course_guide.md` §7.)

**Scope:** `bridge_course_workbook_draft.pdf`, sessions 1–5. Session 6 is blank in the DRAFT.
**Covers all 81 nodes** of `topic_guide.md` §1 — the convergence checklist.

---

## How to read this

**Every node carries a tag. Check it before you trust it.**

| Tag | Means |
|---|---|
| `[SOURCED p.N]` | Traceable to that page of **your workbook**. Your facilitators will back this. |
| `[EXT — not in your workbook]` | **Not in your material.** Standard accounting, checkable from first principles — but your facilitators may not teach it, and a rote answer key may not reward it. |

**About one third of this sheet is `[EXT]`.** That is not padding — it is the measured distance
between what your workbook contains and what your objective requires. Three examples of what's
missing from your material:

- **The accounting equation is never stated.** Dual Aspect is asserted (p.6); the equation under it
  is not.
- **The ledger and trial-balance formats are asked for and never shown.** p.9 says *"Draw the Format
  of a Ledger"*; p.10 says *"Draw the Format of Trial Balance"*. Neither appears anywhere in the
  workbook's 20 pages.
- **The financial statements are never built.** Named once as vocabulary on p.2, then abandoned. The
  workbook stops at the trial balance — one step before the payoff.

**Per node you get:** Definition · why the format looks like that · the format · a worked example ·
where it bites (only where a real confusion exists) · 2 questions.

**Every question is self-contained.** It restates every figure it needs. You never have to scroll
anywhere to answer it — if you do, the question is broken and I want to know.

**The answer sits directly under each question, collapsed:**

<details><summary>Answer</summary>

Like this. Final answer only, no working — so you compare your result, not your route.

**Open it in VS Code's markdown preview** (`Ctrl+Shift+V`) and these stay shut until you click.
In the raw file they're open, so cover the screen or use the preview.

</details>

**A match with different reasoning is not a match.** A right answer reached by pattern-match counts
as FRAGILE at best (`spec.md` §4) — guessing right is not mastery. If your route differed, say so
when you submit.

---

## The map

Everything below is one chain. Each box exists because the box before it cannot answer the next
question.

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

**The one idea underneath all 81 nodes:**

**Assets = Liabilities + Equity.** Not a rule — arithmetic. Every rupee of stuff came from
**somewhere**, and there are exactly two somewheres: an outsider lent it, or the owner supplied or
earned it. **There is no third source.**

| Left — **Assets** | Right — **Liabilities + Equity** |
|---|---|
| **What we have** | **Where it came from** |
| **Uses** | **Sources** |

**Same rupees, described twice.** That is why it balances — by construction, not by effort.

---

## The worked example running through every act

All figures below trace to **p.15 of your workbook** (`[SOURCED]`) — a business's first seven days.
Its solution page (p.16) is **blank**, so the workbook never works this. Every act narrates the same
verified books:

| Day | Event | Amount |
|---|---|---|
| 1 | Started business with cash | 20,00,000 |
| 2 | Purchased goods | 4,00,000 |
| 3 | Sold goods | 4,60,000 |
| 4 | Purchased machinery **from Arjun & Co.** (credit) | 3,00,000 |
| 5 | **Placed an order** with Saksham | 3,00,000 → **NO ENTRY** |
| 6 | Paid to Arjun & Co. | 1,00,000 |
| 7 | Commission paid | 50,000 |

**Verified:** journal 28,10,000 = 28,10,000 · trial balance **26,60,000** both sides · net profit
**10,000** · balance sheet **22,10,000** both sides (2,00,000 liabilities + 20,10,000 equity).

> **`[INFERRED]` assumption, stated rather than slipped past you:** the workbook gives **no closing
> stock**, so the Income Statement assumes **all goods purchased were sold**. Real businesses almost
> never look like this. Flagged again where it bites, in Act 7.


---

# ACT 1 — Money goes in. Where did it come from?

## C1 — Assets = Liabilities + Equity     [EXT — not in your workbook]

**Definition**

Everything a business controls had to come from somewhere. Somebody handed it over. There are only two kinds of somebody:

- **Outsiders** who must be paid back → **Liabilities**
- **The owner**, whose stake is whatever is left over → **Equity**

So the identity is not a rule someone invented. It is a counting fact:

> **Assets = Liabilities + Equity**

**Assets** = the total of what we have.
**Liabilities + Equity** = the total of where all of it came from.

Both sides count the **same rupees**. The left counts them by *form*. The right counts them by *origin*. A pile of money cannot exist without having arrived from somewhere, so the two counts can never disagree.

**Why "= L + E" and not "= E + L"?** Order is convention only. The equation is often rearranged:

| Arrangement | Reads as |
|---|---|
| A = L + E | What we have = where it all came from |
| E = A − L | Owner's stake = what's left after outsiders are paid |
| L = A − E | Outsiders' claim = what we have that isn't the owner's |

All three are the same statement. Nothing is added or removed by moving a term.

**In action**

The business's balance sheet at 30 June 2024:

| Where it came from | Amount | What we have | Amount |
|---|---|---|---|
| Arjun & Co. (creditor) | 2,00,000 | Cash | 19,10,000 |
| Capital 20,00,000 + Net Profit 10,000 | 20,10,000 | Machinery | 3,00,000 |
| **TOTAL** | **22,10,000** | **TOTAL** | **22,10,000** |

The check:

```
      22,10,000     =     2,00,000    +    20,10,000
          A                   L                E
    what we have         outsiders         owner
```

**Where it bites**

**Wrong:** "The two sides came out equal — lucky, the arithmetic worked."
**Right:** They were never able to disagree. 22,10,000 of assets exist **because** 2,00,000 arrived from a supplier and 20,10,000 belongs to the owner. Equality is not the result of the arithmetic. It is the reason the arithmetic works.

**Your turn**

1. A business applies for a loan. Its books at 30 June show everything it controls: cash of Rs 19,10,000 and machinery of Rs 3,00,000. It owes a supplier Rs 2,00,000 for that machinery, and owes nobody else. The equity line has been left blank on the form. Without it, state what the owner's stake must be, and explain why no other figure is possible.

<details><summary>Answer</summary>

Equity is Rs 20,10,000. Assets total Rs 22,10,000, and every rupee of that came from one of exactly two places — an outsider (Rs 2,00,000) or the owner. The remainder is forced: E = A − L = 22,10,000 − 2,00,000.

</details>

2. The same owner tells the lender: *"The business holds Rs 22,10,000, so that's my stake — and on top of that we owe a supplier Rs 2,00,000."* Name which side of the equation this breaks, and by exactly how much.

<details><summary>Answer</summary>

The right side. It would total Rs 24,10,000 against assets of Rs 22,10,000 — overstated by Rs 2,00,000. The supplier's Rs 2,00,000 is being counted twice: once as a debt and again inside the owner's stake, when equity is only what remains **after** outsiders' claims. The true stake is Rs 20,10,000.

</details>

---

## A3 — Assets     [SOURCED p.2]

**Definition**

An **asset** is a resource the business **controls right now** and expects to get future benefit from.

Three tests, all of which must pass:

- **Control now** — not promised, not ordered, not hoped for. Held.
- **Future benefit** — it can be used, sold, or turned into cash later.
- **Arose from something that already happened** — a past transaction, not a future plan.

Assets sit on the **left**. They answer *"what have we got?"* — never *"where did it come from?"*

**In action**

Assets at 30 June 2024, taken from the closing balances:

| Asset | Amount | Why it qualifies |
|---|---|---|
| Cash | 19,10,000 | Held. Spendable. |
| Machinery | 3,00,000 | Controlled since Day 4, still controlled |

**Day 5 is the test case.** An order for goods of 3,00,000 was placed. No entry was made.

```
  Order placed  ──►  nothing received
                ──►  nothing controlled
                ──►  NOT an asset
```

The amount, 3,00,000, is identical to Day 4's machinery. The amount is not what makes an asset. **Control** is.

**Where it bites**

**Wrong:** "3,00,000 of goods are coming, so record 3,00,000 of stock."
**Right:** Nothing was received, given, owed or paid. Bites at the word *coming* — an asset is present control, not a future arrival.

**Your turn**

1. A business places a firm order with a supplier for goods worth Rs 3,00,000. The supplier confirms it and will deliver next week. Nothing has been received, nothing has been paid, and nothing is yet owed. The owner wants stock of Rs 3,00,000 shown on the assets side now, arguing the goods are genuinely on their way. Explain why no asset is recorded.

<details><summary>Answer</summary>

An asset requires **present control** arising from something that has already happened. Nothing was received, given, owed or paid — the order is an agreement about the future, not a past transaction. The size of the figure is irrelevant; control is what makes an asset.

</details>

2. At 30 June a business holds cash of Rs 19,10,000 and machinery of Rs 3,00,000. During the month it also bought goods for Rs 4,00,000 in cash and sold them all — no stock remains. The owner says goods costing Rs 4,00,000 were bought too, so they belong on the assets side. Name the figures that actually sit there and explain why the Rs 4,00,000 does not.

<details><summary>Answer</summary>

Cash Rs 19,10,000 and Machinery Rs 3,00,000. The Rs 4,00,000 of goods was consumed — with all of it sold and no closing stock, nothing is controlled any more, so the value appears as cost of goods sold, not as an asset. Buying something does not make it an asset; still holding it does.

</details>

---

## A4 — Liabilities     [SOURCED p.2]

**Definition**

A **liability** is an amount the business **owes to an outsider** because of something that has already happened.

Key traits:

- **An outsider's claim** — a supplier, a lender, a landlord. Not the owner.
- **A source, not a thing.** A liability is never the goods you bought. It is the *funder* of what you bought.
- **Must be settled.** It has a claim on assets ahead of the owner.

Liabilities sit on the **right**, because the right side answers *"where did it come from?"* A liability's answer is: *"from someone we haven't paid yet."*

**In action**

| Day | Event | Effect |
|---|---|---|
| 4 | Machinery 3,00,000 taken on credit from Arjun & Co. | Asset up 3,00,000 · Liability up 3,00,000 |
| 6 | Paid Arjun & Co. 1,00,000 | Cash down 1,00,000 · Liability down 1,00,000 |

The ledger closes **Arjun & Co. at 2,00,000 credit** — still owed. That is the only liability on the balance sheet at 30 June.

```
  Day 4:  Arjun & Co. funded 3,00,000 of machinery
  Day 6:  1,00,000 of that funding was repaid with cash
  Day 30: 2,00,000 of it is still outstanding
```

**Where it bites**

**Wrong:** "The machinery of 3,00,000 is our liability."
**Right:** The machinery is the **asset** — we control it, it's on the left. The **liability** is the 3,00,000 claim Arjun & Co. holds against us, on the right. The same 3,00,000 appears twice: once as a thing, once as its source. Bites the moment the object gets confused with its funder.

**Your turn**

1. A business takes delivery of machinery worth Rs 3,00,000 from a supplier on credit — not a rupee is paid, and the machine is installed and running. Asked what the Rs 3,00,000 on the right side of the books represents, the owner answers *"the machinery."* State what actually appears on the right side, and explain why it is a liability and not equity.

<details><summary>Answer</summary>

The supplier's claim of Rs 3,00,000 appears on the right. The machinery itself is the **asset**, on the left; the liability is the source that funded it. It is not equity because a supplier is an outsider whose claim must be settled ahead of the owner — equity is only the residual left after such claims.

</details>

2. That business owes the supplier Rs 3,00,000 for machinery already delivered. It now pays the supplier Rs 1,00,000 in cash. State the effect on total assets, on the liability, and on equity, and explain why the equation still holds.

<details><summary>Answer</summary>

Total assets fall by Rs 1,00,000 (cash out); the liability falls from Rs 3,00,000 to Rs 2,00,000; equity is unmoved. Both sides shrink by exactly Rs 1,00,000, so A = L + E holds. Repaying a source of funds is not an expense — nothing was consumed.

</details>

---

## A5 — Equity / Capital     [SOURCED p.2]

**Definition**

**Equity** (also called **Capital**) is the owner's claim on the business.

- It is a **source of funds**, exactly like a liability — the owner is just a different kind of funder.
- It is **residual**: outsiders get paid first, the owner gets what remains. Hence **E = A − L**.
- The word *capital* comes from the fund the owner puts **in**, at the head of the business. It is money the business **owes back** to the owner.

That last point is why Capital carries a **credit** balance in the business's own books. The business did not receive a gift. It received a loan-like contribution from a person who now has a claim on it.

**In action**

| Point | Figure | Source |
|---|---|---|
| Capital introduced, Day 1 | 20,00,000 | Capital A/C closing balance, credit |
| Net profit earned in June | 10,000 | Income statement |
| **Equity at 30 June** | **20,10,000** | Balance sheet |

Profit belongs to the owner, so profit **increases equity**. That is the entire reason net profit is added to capital on the balance sheet rather than parked somewhere else.

**Where it bites**

**Wrong:** "Cash is 19,10,000 so the owner's stake is 19,10,000."
**Right:** Equity is **20,10,000**. Cash is one asset among two; equity is a claim over *all* assets minus *all* debts. Bites at the assumption that the owner's stake lives in the cash box. It does not live anywhere on the left side at all.

**Your turn**

1. An owner started a business by putting in Rs 20,00,000 of cash and has taken nothing out; the Capital account still stands at Rs 20,00,000 credit. The business earned a net profit of Rs 10,000 over the month. The balance sheet reports equity of Rs 20,10,000, and the owner — seeing cash of Rs 19,10,000 in the box — asks where the Rs 20,10,000 comes from. Account for the difference and explain why it belongs to the owner.

<details><summary>Answer</summary>

The Rs 10,000 is the month's net profit, which is value the business earned and therefore belongs to the owner: Rs 20,00,000 + Rs 10,000 = Rs 20,10,000. Cash of Rs 19,10,000 is irrelevant to it — equity is a claim over all assets minus all debts, not the contents of the cash box.

</details>

2. An owner hands over Rs 20,00,000 in cash to start a business and is puzzled to see the books show that Rs 20,00,000 as a **credit** — "the business received it, so surely it's the business's." Explain why it sits as a credit.

<details><summary>Answer</summary>

The books are the business's, and from inside the business the owner is an outsider who supplied funds the business owes back. Receiving the cash is the left-side aspect (Cash Dr. Rs 20,00,000); the owner's claim on the business is the right-side aspect (Capital Cr. Rs 20,00,000). Capital is a source of funds, and sources are credits.

</details>

---

## B2 — Business Entity Concept     [SOURCED p.6]

**Definition**

The business is treated as a **person separate from whoever funded it**. The books are the *business's* books, kept from the *business's* point of view.

Consequences, all forced by that one idea:

- The owner is an **outsider** to the business.
- Money the owner puts in is money the business **owes back** → Capital, a credit.
- The owner's personal cash, house and spending are **not** in these books.
- Money the owner takes out reduces what the business owes back → Drawings.

Without this concept, "Capital" makes no sense. You cannot owe money to yourself. You *can* owe it to an entity you happen to own.

**In action**

Day 1: the business is started with cash of 20,00,000.

```
   OWNER  ────── hands over 20,00,000 ──────►  BUSINESS
                                                  │
   The business's view:                           │
      Cash A/C          Dr.  20,00,000   ◄── a thing it now controls
          To Capital A/C     20,00,000   ◄── a claim the owner holds over it
```

The business does not record "I got lucky." It records **an asset and a matching obligation to its funder**. Both lines are written from inside the business, looking out.

**Where it bites**

**Wrong:** "It's the owner's own money, so it isn't really owed to anyone."
**Right:** Ownership of the business is irrelevant to the entity. From inside, that 20,00,000 arrived from an outside party with a claim. Bites at the word *own* — the concept exists precisely to stop the owner and the business from being the same wallet.

**Your turn**

1. A sole owner funds a new business with Rs 20,00,000 of her own savings and says: *"It's my own money — the business doesn't owe it to anyone."* The books nevertheless record the Rs 20,00,000 as a claim against the business. Explain why the business records a claim against itself instead of treating the money as simply belonging to it.

<details><summary>Answer</summary>

The books are kept from the business's own point of view, and the business is a person separate from whoever funded it. From inside, the owner is an outsider who handed over funds and now holds a claim the business must eventually honour. Ownership of the business is irrelevant to the entity — "the business's money" and "the owner's money" are different things, and Capital is the account that records the difference.

</details>

2. A business's trial balance shows cash of Rs 19,10,000. The owner has been paying for household groceries out of the business cash box, and the bookkeeper has been entering those payments in the business's books. Name the trial balance figure that stops meaning what it claims to mean, and explain why.

<details><summary>Answer</summary>

Cash Rs 19,10,000. It no longer reports the business's cash, because personal spending has been mixed into it. Once the owner's wallet and the business's are treated as one, no figure in the books reports business position or performance, and Capital — which only makes sense if the business is a separate person — becomes incoherent.

</details>

---

## C2 — Dual Aspect     [EXT — not in your workbook]

**Definition**

**Dual aspect** — the workbook's *"two-fold aspect"* (p.6) — says every transaction has **two sides**, always.

The workbook states it as a property of transactions. Stated precisely, it **is the accounting equation**:

> Every transaction affects at least two accounts, in a way that keeps **A = L + E** true.

These are not two separate ideas to memorise. Dual aspect is *why* the equation never breaks; the equation is *what* dual aspect protects. One is the mechanism, the other is the result.

**The format**

Every transaction resolves into exactly one of these four shapes:

| Shape | Left side | Right side | Example from the first week |
|---|---|---|---|
| 1 | Asset ↑ | Source ↑ | Day 1: Cash ↑ 20,00,000 · Capital ↑ 20,00,000 |
| 2 | Asset ↓ | Source ↓ | Day 6: Cash ↓ 1,00,000 · Arjun & Co. ↓ 1,00,000 |
| 3 | Asset ↑ **and** Asset ↓ | unmoved | Day 2: Goods ↑ 4,00,000 · Cash ↓ 4,00,000 |
| 4 | unmoved | Source ↑ **and** Source ↓ | (no example this week) |

There is no fifth shape. That is the whole of double entry.

**In action**

Day 3 — goods sold for 4,60,000:

```
  Aspect 1 (left)   Cash              ↑  4,60,000     an asset we now control
  Aspect 2 (right)  Sales → Equity    ↑  4,60,000     value the business earned, owner's stake

  Shape 1.  Both sides rise by 4,60,000.  A = L + E survives.
```

Day 5 — an order placed for 3,00,000:

```
  Aspect 1   ──   nothing
  Aspect 2   ──   nothing

  No aspects, no transaction, NO ENTRY.
```

**Where it bites**

**Wrong:** "Day 5 has two parties, so it has two aspects — record it."
**Right:** Two *parties* is not two *aspects*. Nothing was received, given, owed or paid, so no account moved. Bites at the point where an agreement gets mistaken for an exchange.

**Your turn**

1. A business sells goods over the counter for Rs 4,60,000 and the customer pays cash on the spot. Name both aspects of this transaction, classify it as one of the four shapes (asset ↑ / source ↑; asset ↓ / source ↓; asset ↑ and asset ↓; source ↑ and source ↓), and show the equation surviving.

<details><summary>Answer</summary>

Aspect 1: Cash (asset) up Rs 4,60,000. Aspect 2: Sales — revenue, which raises equity — up Rs 4,60,000. Shape: asset ↑ / source ↑. Left rises Rs 4,60,000, right rises Rs 4,60,000, so A = L + E survives.

</details>

2. A business and a supplier sign off on an order for goods worth Rs 3,00,000, to be delivered and paid for later. Nothing has been received, given, owed or paid. The owner argues that two parties agreed, so there are two aspects and an entry is due. Explain why no entry is made, using the phrase "two-fold aspect" in your reasoning.

<details><summary>Answer</summary>

No two-fold aspect exists. Two *parties* is not two *aspects* — an aspect is an account that moved, and nothing was received, given, owed or paid, so not one account moved, let alone two. An order is an agreement about the future, not an exchange; no aspects means no entry.

</details>

---

## C8 — Sources vs Uses     [EXT — not in your workbook]

**Definition**

This is the load-bearing idea of the whole equation. Read it slowly.

The balance sheet has two columns, and they ask **two different questions about the same rupees**:

- **LEFT — Uses.** *What do we have right now?* What form did the money take?
- **RIGHT — Sources.** *Where did every rupee come from?* Who supplied it?

The same money is counted **twice**, from two angles. Not two piles of money. **One pile, two questions.**

```
   ┌─────────────────────────┬─────────────────────────┐
   │      LEFT  =  USES      │    RIGHT  =  SOURCES    │
   ├─────────────────────────┼─────────────────────────┤
   │  "What we have"         │  "Where it came from"   │
   │  the FORM it took       │  the ORIGIN it had      │
   │                         │                         │
   │  Cash, Machinery, Goods │  Capital  (the owner)   │
   │                         │  Liabilities (outsiders)│
   └─────────────────────────┴─────────────────────────┘
              same rupees ──────────► counted twice
```

**Spending money is a LEFT-side event.** It changes the *form* of what we have. It cannot change where the money came from, because **the past cannot be edited**. Money that arrived from the owner arrived from the owner, forever, no matter what you later buy with it.

**In action — the demonstration that settles it**

**Day 1.** Started business with cash 20,00,000.

```
   LEFT (uses)                    RIGHT (sources)
   Cash          20,00,000        Capital       20,00,000
   ─────────────────────────      ─────────────────────────
   TOTAL         20,00,000        TOTAL         20,00,000
```

**Day 2.** Purchased goods 4,00,000, paying cash. Watch **only the right side**:

```
   LEFT (uses)                    RIGHT (sources)
   Cash            ↓ 4,00,000     Capital       20,00,000   ◄── did not move
   Goods           ↑ 4,00,000     
   ─────────────────────────      ─────────────────────────
   TOTAL         20,00,000        TOTAL         20,00,000   ◄── did not move
```

**The right side did not move. Not by one rupee.**

Cash fell by 4,00,000. Goods rose by 4,00,000. The left total is still 20,00,000. The right total is still 20,00,000. All that happened is that **20,00,000 of owner-supplied money changed shape** — part of it stopped being cash and started being goods.

> **Spending money never changes where money came from.**
> Spending is a **use**. It reshuffles the left column. The right column records history, and history is closed.

**Where it bites**

This is the exact inversion to kill.

**Wrong:** *"Liabilities are the things we've spent the money on."*
So the Day 2 goods of 4,00,000 would be a liability, and the Day 7 commission of 50,000 would be a liability, and the right side would swell every time cash left the building.

**Right:** **Liabilities are one of the two places money came FROM.** Spending is a use, and uses live on the **left** — or get consumed and vanish. They never appear on the right.

Name the exact point it bites: at the word **"on."** *"Spent the money on goods"* describes what the money **turned into** — a left-side fact. The right side never answers *what did we buy*; it only answers *who supplied the funds*.

Run the check against the first week's own figures:

| At 30 June | Liabilities under the wrong belief | Actual liabilities |
|---|---|---|
| Goods purchased (Day 2) | 4,00,000 ✗ | not a liability — a **use** of funds |
| Commission paid (Day 7) | 50,000 ✗ | not a liability — **consumed**, gone |
| Arjun & Co. (Days 4 & 6) | *often forgotten* | **2,00,000** ✓ — the only liability |

The wrong belief lists the two items that are **not** liabilities and omits the one that **is**. It is not a small slip. It is the right-hand side read upside down.

**The one-line test:** a liability is money someone **gave** the business. It is never a thing the business **bought**.

**Your turn**

1. An owner drafting the year's first balance sheet writes: *"Our liabilities are the Rs 4,00,000 of goods we bought and the Rs 50,000 of commission we paid — that's what we spent our money on."* The books also show a supplier still owed Rs 2,00,000 for machinery delivered on credit. State the correct liability figure, and name the exact word in that sentence where the reasoning inverts.

<details><summary>Answer</summary>

Liabilities are Rs 2,00,000 — the supplier's claim, the only one. The inversion is at the word **"on."** "Spent the money *on* goods" describes what the money turned into, which is a left-side, use-of-funds fact; the right side never answers what was bought, only who supplied the funds. The owner's list names the two items that are not liabilities and omits the one that is.

</details>

2. A business is started with Rs 20,00,000 of the owner's cash — the only money it has ever received from anyone. It then buys goods for Rs 4,00,000, paying cash. State the total of the right side (sources) immediately before that purchase and immediately after it, and explain in one sentence of principle why they are identical.

<details><summary>Answer</summary>

Rs 20,00,000 before, Rs 20,00,000 after — unchanged. Spending is a use of funds: it changes the form of what is held (cash becomes goods) but cannot change where the money came from, because the right side records history and history cannot be edited.

</details>

---

## C9 — Asset vs Expense Boundary     [EXT — not in your workbook]

**Definition**

Money going out looks the same from the cash box. It is not the same. Every payment is one of two things:

- **Asset** — the money bought a resource you **still control** afterwards. Value changed *form*.
- **Expense** — the money bought something **consumed** in the act. Value is *gone*.

**The one test:**

> **After the payment ends, do you still control a resource?**
> Yes → **Asset.** Equity unmoved.
> No → **Expense.** Equity down.

**Why the test works.** Equity is a residual — it only moves when total value moves. Swap 3,00,000 of cash for 3,00,000 of machinery and total value is untouched, so equity cannot move. Burn 50,000 on a service that's finished and total value fell by 50,000, so equity must fall by 50,000. The test is not a rule of thumb. It is the equation being obeyed.

**In action**

**Day 4 — machinery 3,00,000, from Arjun & Co.**

```
   Test: after the transaction, do we control a resource?
   YES — machinery, sitting there, 3,00,000.

   Asset ↑ 3,00,000  (Machinery)
   Right ↑ 3,00,000  (Arjun & Co. — a source, the supplier funded it)
   EQUITY:  UNMOVED
```

**Day 7 — commission paid 50,000.**

```
   Test: after the transaction, do we control a resource?
   NO — the service is over. Nothing is left to point at.

   Asset ↓ 50,000    (Cash)
   EQUITY: ↓ 50,000  — value left the business permanently
```

Now look at what the two statements do with them:

| Item | Amount | Income statement | Balance sheet |
|---|---|---|---|
| Machinery | 3,00,000 | **absent** — not consumed, acquired | **present**, assets side |
| Commission | 50,000 | **present** — deducted, gross profit 60,000 → net profit 10,000 | **absent** — nothing left to show |

**Where it bites**

**Wrong:** "Machinery cost 3,00,000, so it's an expense of the month — deduct it and the business made a loss."
**Right:** Net profit is **10,000**. Machinery is deducted from **nothing**, because it was never consumed. It is still standing there, 3,00,000 of it, on the balance sheet.

Name the exact point it bites: at the assumption that **paying out = expense**. Both Day 4 and Day 7 are money leaving in ordinary language. Only Day 7 leaves nothing behind. The control test separates them in one question; the cash box cannot separate them at all.

**Your turn**

1. In one month a business acquires machinery worth Rs 3,00,000 from a supplier on credit, and separately pays Rs 50,000 in cash as commission for a service that is now finished. Both are "money out" in ordinary speech. Apply the control test to each and state the effect of each on equity.

<details><summary>Answer</summary>

Machinery: a resource worth Rs 3,00,000 is still controlled afterwards → asset → equity **unmoved** (asset up Rs 3,00,000, source up Rs 3,00,000). Commission: the service is over and nothing is controlled → expense → equity **down Rs 50,000**.

</details>

2. A business's month shows sales of Rs 4,60,000, goods sold costing Rs 4,00,000 (gross profit Rs 60,000), and commission paid of Rs 50,000, giving a net profit of Rs 10,000. It also acquired machinery for Rs 3,00,000, which is still installed and running. The owner insists the Rs 3,00,000 must be deducted too, making the month a heavy loss. Explain why the machinery is absent from the income statement while the commission appears in it, referring to what the income statement measures.

<details><summary>Answer</summary>

The income statement measures value **consumed to earn revenue** over the period. The machinery was acquired, not consumed — it is still controlled, so it sits on the balance sheet at Rs 3,00,000 and is deducted from nothing. The commission was consumed entirely, so it is deducted, taking gross profit Rs 60,000 down to net profit Rs 10,000, and leaves nothing on the balance sheet. Net profit is Rs 10,000; there is no loss.

</details>

---

## C10 — Forced vs Arbitrary     [EXT — not in your workbook]

**Definition**

Two very different things get taught in the same breath, and students memorise both as if they were equally deep. They are not.

- **FORCED — which side an account lives on.** This is dictated by the equation. There is no choice. Cash is a use, so it sits with the uses. Capital is a source, so it sits with the sources. Change it and A = L + E collapses.
- **ARBITRARY — what the two columns are called.** "Debit" for the left and "credit" for the right are **names**. From Latin *debere* (to owe) and *credere* (to entrust). Historical labels. Nothing more.

> The **logic** is forced. The **vocabulary** is a naming convention.
> Rename the columns tomorrow and every balance stays exactly where it is.

**The format**

```
   ┌──────────────────────────────────────────────────────┐
   │  FORCED                    │  ARBITRARY              │
   ├────────────────────────────┼─────────────────────────┤
   │  Cash is a USE   → left    │  We call the left       │
   │  Capital is a SOURCE→right │  column "debit"         │
   │                            │                         │
   │  Break it and the          │  Break it and…          │
   │  equation breaks           │  nothing breaks.        │
   │                            │  Only the label changed │
   └────────────────────────────┴──────────────────────────┘
```

**In action**

The trial balance at 30 June:

| Account | Debit | Credit | Which part is forced? |
|---|---|---|---|
| Cash | 19,10,000 | | **Forced** — a use, must sit left |
| Purchases | 4,00,000 | | **Forced** — value consumed, reduces equity |
| Machinery | 3,00,000 | | **Forced** — a use, must sit left |
| Commission | 50,000 | | **Forced** — value consumed, reduces equity |
| Capital | | 20,00,000 | **Forced** — a source, must sit right |
| Sales | | 4,60,000 | **Forced** — value earned, increases equity |
| Arjun & Co. | | 2,00,000 | **Forced** — a source, must sit right |
| **TOTAL** | **26,60,000** | **26,60,000** | |

The words **"Debit"** and **"Credit"** at the tops of those two columns are the only arbitrary thing on the page. Every figure underneath them is forced.

**Where it bites**

**Wrong:** "Cash increases go on the debit side because that's the rule for asset accounts — I memorised the four rules."
**Right:** Cash increases go on the left because **cash is a use of funds and uses are counted on the left**. The rule you memorised is a *description* of that fact, written in the arbitrary vocabulary. Bites when a transaction doesn't match a memorised rule — the rule-memoriser stalls; the equation-user just asks *"is this a use or a source?"* and the answer is already there.

**Your turn**

1. A business's books close the month with cash of Rs 19,10,000 on the debit side and capital of Rs 20,00,000 on the credit side. A new employee asks why, and is told "because that's the rule for asset and capital accounts — memorise it." For each of the two balances, separate what is genuinely forced from what is only naming convention.

<details><summary>Answer</summary>

Forced: cash is a use of funds, so the Rs 19,10,000 must sit on the left; capital is a source of funds, so the Rs 20,00,000 must sit on the right — put either on the other side and A = L + E collapses. Arbitrary: calling the left column "debit" and the right "credit." The memorised rule is a description of the forced fact, written in the arbitrary vocabulary.

</details>

2. A software vendor ships an accounting package that, by a historical quirk, prints "Credit" over the left column and "Debit" over the right. A business runs its month-end trial balance through it: cash Rs 19,10,000, purchases Rs 4,00,000, machinery Rs 3,00,000, commission Rs 50,000, capital Rs 20,00,000, sales Rs 4,60,000, supplier owed Rs 2,00,000. State which figures would change, and justify your answer.

<details><summary>Answer</summary>

Not one figure changes. Cash stays Rs 19,10,000 on the uses side, capital stays Rs 20,00,000 on the sources side, and the totals stay Rs 26,60,000 = Rs 26,60,000. Only the two words at the tops of the columns swapped. The sides are forced by the equation; the vocabulary is a label.

</details>

---

## C6 — The Expanded Equation     [EXT — not in your workbook]

**Definition**

**A = L + E** is true but blunt. Equity is not one lump — it is built from four separate forces, two that raise it and two that lower it. Expand it and every account in the books gets a home:

> **Equity = Capital + Revenue − Expenses − Drawings**

Substituting into the identity:

> **Assets = Liabilities + Capital + Revenue − Expenses − Drawings**

**Why each sign is what it is:**

| Term | Sign | Reason |
|---|---|---|
| **Capital** | **+** | Owner puts value in → owner's claim grows |
| **Revenue** | **+** | Business earns value → it belongs to the owner → claim grows |
| **Expenses** | **−** | Value consumed to earn → gone → claim shrinks |
| **Drawings** | **−** | Owner takes value out → owner's claim on the business shrinks |

The signs are not arbitrary. Every term asks the same question — *did the owner's stake grow or shrink?* — and answers it.

**The format**

```
                            EQUITY
                              │
        ┌───────────┬─────────┴────────┬────────────┐
        │           │                  │            │
    Capital     Revenue           Expenses     Drawings
      (+)         (+)                (−)          (−)
   put in by   earned by         consumed to   taken out by
    owner      business            earn          owner
        │           │                  │            │
        └── raises ─┘                  └── lowers ──┘
```

**In action**

Assemble the first week's equity from the components:

| Term | Account | Amount |
|---|---|---|
| Capital | Capital A/C | + 20,00,000 |
| Revenue | Sales A/C | + 4,60,000 |
| Expense | Purchases A/C (goods consumed) | − 4,00,000 |
| Expense | Commission A/C | − 50,000 |
| Drawings | *none in the seven events* | − 0 |
| | **EQUITY at 30 June** | **20,10,000** |

Cross-check against the balance sheet: Capital 20,00,000 **+** Net Profit 10,000 = **20,10,000**. Identical.

Those are two routes to one number, and that is the point. "Capital + Profit" is just "Capital + Revenue − Expenses" with the middle two collapsed into one word.

> **`[INFERRED]` assumption in play:** Purchases 4,00,000 is treated as fully consumed because the workbook gives **no closing stock**, so all goods purchased are assumed sold. Real businesses almost never look like this. If stock remained, part of that 4,00,000 would still be an **asset** on the left, not an expense.

**Where it bites**

**Wrong:** "Equity is 20,00,000 — that's what the owner put in."
**Right:** Equity is **20,10,000**. Capital is only the *first* of four terms. The business then earned 4,60,000 and consumed 4,00,000 and 50,000 — and every rupee of that net movement lands on the owner. Bites at treating Capital and Equity as synonyms. Capital is an input; equity is the running total.

**Your turn**

1. A business closes its first month with these balances: Capital Rs 20,00,000 credit, Sales Rs 4,60,000 credit, Purchases Rs 4,00,000 debit (all goods sold, no closing stock), Commission Rs 50,000 debit, and no drawings. The owner says equity is Rs 20,00,000, "because that's what I put in." Assemble equity from those balances through the expanded equation, and state the figure it must agree with on the balance sheet.

<details><summary>Answer</summary>

20,00,000 + 4,60,000 − 4,00,000 − 50,000 − 0 = **Rs 20,10,000**. It must agree with the balance sheet's Capital Rs 20,00,000 + Net Profit Rs 10,000 = Rs 20,10,000. Capital is only the first of four terms — it is an input; equity is the running total.

</details>

2. In the same month, the business earns Rs 4,60,000 of revenue from customers, and in a different month the owner takes Rs 50,000 out of the till for personal use. Both move value across the boundary between the business and the outside world, yet revenue carries a plus in the expanded equation and drawings a minus. Explain why the signs differ.

<details><summary>Answer</summary>

Both terms answer one question: did the owner's stake grow or shrink? Revenue is value the business earned, and it belongs to the owner, so the stake grows (+). Drawings is the owner removing value, so the business owes the owner less and the stake shrinks (−). Neither sign is a convention; each is the direction of the claim.

</details>

---

## A13 — Drawings     [SOURCED p.4]

**Definition**

**Drawings** are value the **owner takes out** of the business for personal use — cash, goods, anything.

What drawings are:

- The **reverse of capital.** Capital is the owner putting value in; drawings is the owner pulling it back out.
- A **reduction of equity.** The business owes the owner less than it did.
- **Only possible because of the business entity concept.** The owner can "take" from the business precisely because the business is a separate person holding the value.

What drawings are **not**:

- **Not an expense.** Nothing was consumed to earn revenue. Value simply moved from the business's side of the line to the owner's side.
- **Never on the income statement.** Profit measures how the *business* performed. What the owner then removes has nothing to do with performance.

**The format**

```
        CAPITAL  ──────  owner puts value IN   ──────►  equity ↑
       DRAWINGS  ──────  owner takes value OUT ──────►  equity ↓

        Both run between OWNER and BUSINESS.
        Neither has anything to do with earning.
```

**In action**

**The seven events contain no drawings at all.** That absence is itself evidence, and it is readable straight off the ledger:

| Account | Closing balance | What it proves |
|---|---|---|
| Capital A/C | 20,00,000 credit | Introduced 20,00,000, reduced by nothing |

Every rupee that left the business in the first week left for a **business** reason:

| Day | Money out | Reason | Kind |
|---|---|---|---|
| 2 | 4,00,000 | Goods for the business | Use of funds |
| 6 | 1,00,000 | Settling a supplier | Repaying a source |
| 7 | 50,000 | Commission to earn revenue | Expense |

None of these is the owner taking value home. So Capital stands at its full 20,00,000, and equity closes at 20,10,000 — capital untouched, plus profit.

**Where it bites**

**Wrong:** "Money left the business, so it's an expense — Day 7's commission of 50,000 and an owner's 50,000 withdrawal are the same event."
**Right:** They are opposite in kind.

| | Commission 50,000 | A withdrawal of 50,000 |
|---|---|---|
| Cash | ↓ 50,000 | ↓ 50,000 |
| Equity | ↓ 50,000 | ↓ 50,000 |
| **Why** | **Consumed** to earn revenue | **Removed** by the owner |
| Income statement | Appears — deducted | **Never appears** |
| Net profit | Reduces it (60,000 → 10,000) | Leaves it at **10,000** |

Name the exact point it bites: at **"money left, so it's an expense."** Both hit cash and equity identically, so cash cannot tell them apart. Only the *reason* separates them — consumed **by the business** versus taken **by the owner** — and only one of those is a fact about how the business performed.

**Your turn**

1. A business has sales of Rs 4,60,000 and goods sold costing Rs 4,00,000, giving a gross profit of Rs 60,000. Consider two separate Rs 50,000 cash payments: commission paid to earn revenue, and the owner taking Rs 50,000 out for personal use. Each cuts cash by Rs 50,000 and equity by Rs 50,000. State what happens to net profit under each, and explain why they differ.

<details><summary>Answer</summary>

Commission: net profit is Rs 10,000 (gross profit Rs 60,000 less Rs 50,000) — value was consumed to earn revenue, a fact about business performance. Withdrawal: net profit stays at Rs 60,000, because drawings never touch the income statement — the owner removing value says nothing about how the business performed. Cash and equity move identically in both, which is exactly why cash cannot classify a transaction; only the reason can.

</details>

2. A business is started with the owner's cash of Rs 20,00,000. Over the month cash leaves three times: Rs 4,00,000 for goods, Rs 1,00,000 to settle a supplier, and Rs 50,000 as commission. At month end the Capital account stands at Rs 20,00,000 credit. A lender asks whether the owner has been taking money out for personal use. State what the Capital balance proves, and the reasoning that gets you there.

<details><summary>Answer</summary>

Drawings were zero. Any withdrawal would have reduced the owner's claim on the business and shown as a debit against Capital, pulling the closing balance below Rs 20,00,000. It stands unreduced at the full Rs 20,00,000, so nothing was taken out — every rupee that left did so for a business reason.

</details>

---

# ACT 2 — Something happened. Write it down.

## B5 — Dual Aspect                                            [SOURCED p.6]

**Definition**

The workbook calls Dual Aspect **"the basic concept"** — not one concept among many, the one the rest stand on.

It says: **every transaction gives a benefit and receives a benefit.** Both halves, always. Never one alone.

The logic under it is almost boringly physical:

- Nothing appears from nowhere.
- Nothing vanishes into nowhere.
- So if something arrived, it arrived **from** somewhere.
- And if something left, it went **to** somewhere.

A transaction is therefore never a single fact. It is always a **pair** of facts about the same event.

```
        ONE EVENT
             |
     +-------+-------+
     |               |
 RECEIVED         GIVEN
 (what came       (what it
  in / what        came from /
  we now have)     what left)
     |               |
     +-------+-------+
             |
    both recorded, always
```

**In action**

Day 2 of the spine. The business purchased goods for Rs 4,00,000.

| Question | Answer |
|---|---|
| What did the business receive? | Goods worth Rs 4,00,000 |
| What did the business give? | Cash of Rs 4,00,000 |

Two facts. One event. Neither is optional.

Now Day 1, the same test:

| Question | Answer |
|---|---|
| What did the business receive? | Cash of Rs 20,00,000 |
| What did the business give? | A claim — the owner's capital of Rs 20,00,000 |

The second half is easy to miss because nothing physical left. But the business now **owes** the owner Rs 20,00,000. The claim is the benefit given.

**Where it bites**

The confusion: *"Day 1 only has one side. Cash just came in. Nobody gave anything."*

**Wrong:** Cash came in, so record cash Rs 20,00,000 and stop. Nothing went out.

**Right:** Cash came in **from** the owner. The business received Rs 20,00,000 and gave back a claim of Rs 20,00,000 against itself. Cash A/C Dr. 20,00,000 · To Capital A/C 20,00,000.

**The exact point it bites:** "gave a benefit" is read as "something physical left." It doesn't mean that. It means **a source was used up** — and an owner's willingness to fund the business is a source.

**Your turn**

1. A business owes a machinery supplier Rs 3,00,000 for equipment bought on credit. It decides to pay Rs 1,00,000 of that off early to keep the supplier willing to extend credit again. Cash of Rs 1,00,000 leaves the business — that is plainly the "given" half. Nothing physical arrives in return, so it is tempting to say this event has only one side. Name the "received" half, and state what the business has after the payment that it did not have before.

<details><summary>Answer</summary>

The received half is the discharge of Rs 1,00,000 of the debt. What the business now has is a smaller obligation — the supplier's claim against it drops from Rs 3,00,000 to Rs 2,00,000. Freedom from a claim is a benefit received even though nothing physical came in.

</details>

2. A business telephones a supplier and places an order for goods worth Rs 3,00,000, to be delivered next month. The supplier confirms the order. The owner assumes this is a Rs 3,00,000 transaction because a firm commitment now exists. Apply the "every transaction gives a benefit and receives a benefit" test: state what was received and what was given, and use that to explain why the books record nothing at all.

<details><summary>Answer</summary>

Nothing was received and nothing was given — no goods arrived, no cash left, no debt arose. Both halves are empty, so there is nothing for Dual Aspect to record: no entry is made. A commitment to transact is not itself a transaction.

</details>

---

## D1 — Double-Entry Defined                                   [SOURCED p.8]

**Definition**

Double-entry is Dual Aspect turned into a **rule for writing things down**.

The definition, exactly:

> **Every transaction affects at least two accounts — one is debited, one is credited.**

Read the parts:

- **Every transaction** — no exceptions, no small ones that don't count.
- **At least two accounts** — two is the minimum, not the maximum. A transaction can touch three or four; it can never touch one.
- **One debited, one credited** — the two entries go on **opposite sides**.

Double-entry is not a technique somebody cleverly invented. It is what you are **forced** into once you accept that stuff does not appear from nowhere. B5 says every event has two halves. D1 says: then write both.

```
   B5 Dual Aspect            D1 Double Entry
   (the fact)         -->    (the recording rule)

   every event has           so every event gets
   two halves                two entries
```

**A one-line historical note.** Double-entry spread among Renaissance Italian merchants who had agents in distant cities. Its virtue was that a dishonest agent now needed **two consistent lies** instead of one — falsify the cash and the other side no longer fits. It was built as an anti-theft device.

**In action**

Day 1, counted out:

| Test | Day 1 |
|---|---|
| Is it a transaction? | Yes — Rs 20,00,000 cash actually moved in |
| How many accounts? | Two: Cash A/C, Capital A/C |
| Which is debited? | Cash A/C — Rs 20,00,000 |
| Which is credited? | Capital A/C — Rs 20,00,000 |

Day 2, same count:

| Test | Day 2 |
|---|---|
| Is it a transaction? | Yes — goods in, Rs 4,00,000 out |
| How many accounts? | Two: Purchases A/C, Cash A/C |
| Which is debited? | Purchases A/C — Rs 4,00,000 |
| Which is credited? | Cash A/C — Rs 4,00,000 |

**Your turn**

1. In its first month a business records five transactions involving cash: cash of Rs 20,00,000 put in by the owner (Cash debited), cash of Rs 4,60,000 taken in from selling goods (Cash debited), cash of Rs 4,00,000 paid for goods (Cash credited), cash of Rs 1,00,000 paid to a supplier (Cash credited), and cash of Rs 50,000 paid as commission (Cash credited). A reviewer objects that Cash has been debited twice and credited three times, so the rule "every transaction affects at least two accounts — one is debited, one is credited" has clearly been broken five times over. Explain why the reviewer is wrong, and state what the rule is actually counting.

<details><summary>Answer</summary>

The rule counts accounts per transaction, not appearances per account. Each of the five transactions had exactly one debit and one credit; Cash simply happened to be one leg of five different transactions. An account may appear in either column any number of times across the book.

</details>

2. A business pays Rs 50,000 of commission to an agent who brought in a customer. The bookkeeper writes *Commission A/C Dr. 50,000* and stops there, arguing "the money is simply gone — there's nobody on the other side to record." Identify the account left out, and state which part of the rule "every transaction affects at least two accounts — one debited, one credited" was broken.

<details><summary>Answer</summary>

Cash A/C, credited Rs 50,000, was left out — the money went somewhere, namely out of cash. The part broken is "at least two accounts" (and with it, "one debited, one credited": the entry has a debit and no credit).

</details>

---

## D2 — The Three Attributes of Double-Entry                    [SOURCED p.8]

**Definition**

D1 says two entries. D2 says **which** two, **where** they go, and **how big** they are. Three attributes, and all three must hold at once.

| # | Attribute | What it forbids |
|---|---|---|
| 1 | **All aspects of a transaction are recorded** | Recording only the half you noticed |
| 2 | **The entries are made on opposite sides** | Debiting both accounts, or crediting both |
| 3 | **The same amount, at the same time** | Rs 4,00,000 out and Rs 3,90,000 in; or one half today and the other next week |

Attribute 3 is the one doing the invisible work. **Same amount + same time** is why the journal's debit column and credit column can be totalled and compared at all. Break it and the two columns drift apart forever.

```
   Attribute 1        Attribute 2         Attribute 3
   both halves        opposite sides      same amount,
   recorded                               same moment
        |                  |                   |
        +------------------+-------------------+
                           |
              Σ debits = Σ credits, always
```

**In action**

Day 2 against all three attributes:

| Attribute | Day 2: goods purchased for cash, Rs 4,00,000 | Holds? |
|---|---|---|
| All aspects recorded | Goods in (Purchases) **and** cash out (Cash) — both written | Yes |
| Opposite sides | Purchases **debited**, Cash **credited** | Yes |
| Same amount, same time | Rs 4,00,000 both sides, both on Jun 2 | Yes |

The spine's journal total is the proof at scale: **Debit 28,10,000 = Credit 28,10,000.** That equality is not luck. Attribute 3 makes it unavoidable — every single line added the same number to both columns.

**Where it bites**

The confusion: *"Attribute 3 means the totals must match, so if my totals match, my books are right."*

**Wrong:** Journal totals Rs 28,10,000 = Rs 28,10,000, therefore nothing is wrong.

**Right:** The totals match because **each entry** put equal amounts on both sides. If a whole transaction is never written, both columns lose the same amount and the totals **still** match.

**The exact point it bites:** equal totals prove that *what you wrote* obeyed attribute 3. They say nothing about *what you didn't write*. Attribute 1 (all aspects recorded) has no arithmetic guard at all — only your care. (Act 5 shows exactly what this costs.)

**Your turn**

1. On Jun 4 a business takes delivery of machinery worth Rs 3,00,000 bought on credit from a supplier, and records *Machinery A/C Dr. 3,00,000* that same day. The supplier's invoice only reaches the office on Jun 6, so the bookkeeper waits and records the matching *To Supplier A/C 3,00,000* on Jun 6 — "the debit and credit are both there in the end, and the amount is identical, so nothing is lost." Given that double-entry requires all aspects recorded, on opposite sides, in the same amount **and at the same time**, name the attribute this breaks and state one question the books could not answer on Jun 5.

<details><summary>Answer</summary>

It breaks attribute 3 — specifically the "same time" half; the amount and the sides are fine. On Jun 5 the debit column exceeds the credit column by Rs 3,00,000, so the books cannot answer "what does the business owe?" or produce a balanced position at that date: machinery of Rs 3,00,000 exists with no recorded source.

</details>

2. A business sells goods for Rs 4,60,000 cash. The goods had cost it Rs 4,00,000. The bookkeeper debits Cash A/C Rs 4,60,000 — the amount actually received — but credits Sales A/C only Rs 4,00,000, reasoning "the goods were only worth Rs 4,00,000 to us, so that's the real figure." Name the attribute broken and state what happens to the journal's two column totals.

<details><summary>Answer</summary>

Attribute 3 — same amount. The debit column exceeds the credit column by Rs 60,000, and no later entry corrects it: once the two columns drift apart they stay apart, so the journal's totals can never agree again.

</details>

---

## C3 — Debit and Credit: Directions, Not Meanings   [EXT — not in your workbook]

**Definition**

This is the single most important sentence in the whole subject:

> **Debit means LEFT. Credit means RIGHT. That is all they mean.**

They are not words about money. They are words about **which column**.

- **Debit** ← from Latin *debere*. **Left column.**
- **Credit** ← from Latin *credere*. **Right column.**

The Latin roots once meant "he owes" and "he trusts." **That meaning is dead.** It survived only as a position. Trying to read the old meaning into a modern entry is how students wreck themselves for a whole term.

**Debit does not mean increase.** Debit does not mean money-in, or good, or ours, or expense. It means left.

**So why do assets increase by debit?**

Because of where they sit in the accounting equation — nothing more:

```
        A          =        L        +        E
     ASSETS               LIABILITIES      EQUITY
        |                      |               |
    LEFT SIDE             RIGHT SIDE      RIGHT SIDE
        |                      |               |
   grows on the           grow on the     grows on the
       LEFT                  RIGHT           RIGHT
     = DEBIT                = CREDIT       = CREDIT
```

An asset grows **by debit** because an asset **is** a left-side item, and a thing grows on its own side. That is the entire explanation. There is no deeper rule and no meaning to memorise.

**In action**

Day 1 and Day 2 read as pure directions — no meanings anywhere.

**Day 1** — Cash A/C Dr. 20,00,000 · To Capital A/C 20,00,000

| Account | Which side of A = L + E? | Growing or shrinking? | So which column? |
|---|---|---|---|
| Cash (asset) | Left | Growing | **Left = Debit** 20,00,000 |
| Capital (equity) | Right | Growing | **Right = Credit** 20,00,000 |

Both accounts **increased**. One is a debit and one is a credit. If debit meant "increase," this entry would be impossible.

**Day 2** — Purchases A/C Dr. 4,00,000 · To Cash A/C 4,00,000

| Account | Which side? | Growing or shrinking? | So which column? |
|---|---|---|---|
| Purchases (reduces equity) | Equity is right, so a reduction goes **left** | Equity shrinking | **Left = Debit** 4,00,000 |
| Cash (asset) | Left | Shrinking | Shrink **against** its own side → **Right = Credit** 4,00,000 |

Cash was **credited** while cash **went down**. Credit did not mean "money in." It meant right.

**Where it bites**

The confusion — the classic wreck: *"Debit = increase, credit = decrease."*

Test it on Day 1:

**Wrong:** Both Cash and Capital went up on Day 1. Debit = increase. So debit Cash 20,00,000 **and** debit Capital 20,00,000.
→ Debit column 40,00,000, credit column nil. The journal cannot even be totalled. D1 broken, D2 attribute 2 broken.

**Right:** Cash is an asset, assets live on the left, it grew → **debit**. Capital is equity, equity lives on the right, it grew → **credit**. Both grew; opposite columns; Rs 20,00,000 each.

**The exact point it bites:** the moment a transaction makes **two accounts increase at once** — which is most of them. "Debit = increase" gives you two debits and no credit, and the whole system stops. The rule that never fails: *find the account's home side, then ask whether it's growing (own side) or shrinking (other side).*

**Your turn**

1. A business owes a supplier Rs 3,00,000 and pays Rs 1,00,000 of it in cash. Two things go **down**: the debt owed to the supplier, and the cash held. The entry is *Supplier A/C Dr. 1,00,000 · To Cash A/C 1,00,000* — one debit, one credit, even though both accounts decreased. Using home-side reasoning only (find the account's home side in A = L + E, then ask whether it is growing or shrinking) — and never "debit = decrease" — explain why one of the two is a debit and the other a credit.

<details><summary>Answer</summary>

The supplier account is a liability, home side right; it is shrinking, so it is recorded against its home side, on the left = debit Rs 1,00,000. Cash is an asset, home side left; it is shrinking, so it is recorded against its home side, on the right = credit Rs 1,00,000. Both fell; the columns differ only because the home sides differ.

</details>

2. A business makes two entries in the same week. Selling goods for cash brings Rs 4,60,000 **in**, and Sales A/C is credited Rs 4,60,000. Buying goods for cash sends Rs 4,00,000 **out**, and Cash A/C is credited Rs 4,00,000. One credit sits alongside money arriving, the other alongside money leaving — so "credit" cannot be describing the money's direction. State what these two entries genuinely have in common.

<details><summary>Answer</summary>

Only their position: both amounts sit in the right-hand column. Credit means right and nothing else — it makes no claim about whether money came in or went out.

</details>

---

## E1 — The Journal                                            [SOURCED p.8]

**Definition**

**Journal** comes from the French ***jour*** — **day**. The name is the definition. It is a **day-book**: a **diary of the business**.

Two properties follow from the name:

- **Chronological.** Entries go in **date order**, as events happen. Jun 1, then Jun 2, then Jun 3. Never regrouped, never re-sorted.
- **Book of original entry.** Every transaction is written **here first**. Nothing enters the books anywhere else. The journal is the front door.

The one question it answers:

> **"What happened on June 4th?"**

Look at Jun 4, read the line, done: machinery Rs 3,00,000 bought from Arjun & Co. on credit.

And that is the **only** question it answers. Ask it "how much do we still owe Arjun & Co.?" and it makes you hunt Jun 4, then Jun 6, then add. A diary is organised by **when**, not by **what**. That limit is the reason another book has to exist later.

**In action**

The spine's journal, read as a diary, day by day:

| Ask the diary | It answers instantly |
|---|---|
| What happened Jun 1? | Capital introduced in cash — Rs 20,00,000 |
| What happened Jun 2? | Goods purchased for cash — Rs 4,00,000 |
| What happened Jun 5? | **Nothing.** An order was placed; no entry |
| What happened Jun 7? | Commission paid — Rs 50,000 |

Jun 5 is worth pausing on. The diary records **events that changed the books** — not everything that occupied the day. An order placed is activity, not a transaction.

**Your turn**

1. A business's journal for June is complete and totals Rs 28,10,000 on each side. Cash appears in five separate entries scattered through it: in on Jun 1 (Rs 20,00,000 from the owner), out on Jun 2 (Rs 4,00,000 for goods), in on Jun 3 (Rs 4,60,000 from sales), out on Jun 6 (Rs 1,00,000 to a supplier) and out on Jun 7 (Rs 50,000 of commission). The owner is asked by a bank how much cash the business is holding and expects to read it off the journal. Using the fact that a journal is a diary — ordered by date, as events happen — explain why no line in it answers that question.

<details><summary>Answer</summary>

The journal is ordered by date, not by account, so Cash's five appearances are scattered across five dates and each records only a movement, never a running total. A diary answers "what happened when," so no single line in it can show the cash held — that requires a book organised by account.

</details>

2. On Jun 7 a business must tell a supplier how much of its bill is still outstanding. Its journal shows machinery bought on credit from that supplier for Rs 3,00,000 on Jun 4, and a payment of Rs 1,00,000 to the same supplier on Jun 6 — with three unrelated entries in between. Name the journal dates the reader must find, state what must be done with the figures, and explain why this work gets harder as the business does more business.

<details><summary>Answer</summary>

Jun 4 (Rs 3,00,000 credited to the supplier) and Jun 6 (Rs 1,00,000 debited) must be hunted down, and Rs 1,00,000 subtracted from Rs 3,00,000 to get Rs 2,00,000 still owed. The work grows because every further dealing with that supplier adds another date to search for and another figure to combine, and the search runs over the whole book — so its cost rises with the book's length.

</details>

---

## E2 — The Journal Format                                     [SOURCED p.15]

**Why the format looks like this**

The columns are not a style choice. Each one exists because a specific question would otherwise be unanswerable.

| Column | Exists because someone will ask |
|---|---|
| **Date** | "When did this happen?" — and the book is chronological, so this is the sort key |
| **Particulars** | "Which accounts, and which side?" — the debit line and the credit line |
| **L.F** | "Where did this end up in the ledger?" — the trace (see E12) |
| **Debit** | "How much on the left?" |
| **Credit** | "How much on the right?" |
| **Narration** | "What *was* this?" — the plain-language fact (see F3) |

Two amount columns, because Dual Aspect (B5) says there are two halves and D2 says they sit on **opposite sides**. One column could not express "opposite." Two can, by position alone.

**The format**

```
 +--------+----------------------------+-------+-------------+-------------+
 |  DATE  |        PARTICULARS         |  L.F  |    DEBIT    |   CREDIT    |
 +--------+----------------------------+-------+-------------+-------------+
 |        |  Name A/C            Dr.   |       |   xx,xx,xxx |             |  <- debit line: flush left
 |        |      To Name A/C           |       |             |   xx,xx,xxx |  <- credit line: INDENTED, "To"
 |        |  (Being ................)  |       |             |             |  <- narration, in brackets
 +--------+----------------------------+-------+-------------+-------------+
```

Three conventions carry meaning — they are not decoration:

- **`Dr.`** after the debited account name. Marks the left-hand half.
- **`To`** before the credited account name, and the line is **indented**. The indent is visual: the credited account is physically pushed to the right of the debited one, so the page itself shows the two halves on opposite sides.
- **Narration in brackets**, starting *"Being…"*, on its own line under the entry.

**In action**

The spine's first two entries, drawn out in full:

```
 +--------+----------------------------------+-------+-------------+-------------+
 |  DATE  |          PARTICULARS             |  L.F  |    DEBIT    |   CREDIT    |
 +--------+----------------------------------+-------+-------------+-------------+
 | Jun 1  |  Cash A/C                  Dr.   |       |  20,00,000  |             |
 |        |      To Capital A/C              |       |             |  20,00,000  |
 |        |  (Being capital introduced       |       |             |             |
 |        |   in cash)                       |       |             |             |
 +--------+----------------------------------+-------+-------------+-------------+
 | Jun 2  |  Purchases A/C             Dr.   |       |   4,00,000  |             |
 |        |      To Cash A/C                 |       |             |   4,00,000  |
 |        |  (Being goods purchased          |       |             |             |
 |        |   for cash)                      |       |             |             |
 +--------+----------------------------------+-------+-------------+-------------+
```

Same thing in table form — how it will look in an exam answer:

| Date | Particulars | L.F | Debit | Credit |
|---|---|---|---|---|
| Jun 1 | Cash A/C **Dr.** | | 20,00,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Capital A/C | | | 20,00,000 |
| | *(Being capital introduced in cash)* | | | |
| Jun 2 | Purchases A/C **Dr.** | | 4,00,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Cash A/C | | | 4,00,000 |
| | *(Being goods purchased for cash)* | | | |

Notice Cash: **debited** on Jun 1, **credited** on Jun 2. Same account, both columns, two days apart. The format tracks position, not the account's character.

**Where it bites**

The confusion: *"`To` means 'paid to' or 'given to' someone."*

Test it on Day 1.

**Wrong:** "To Capital A/C" means cash was paid **to** capital. Day 2's "To Cash A/C" means goods were paid **to** cash. Neither sentence means anything.

**Right:** `To` is a **format marker**. It flags the credit line — the right-hand half — and nothing else. On Jun 1 it marks Capital as the credited account. On Jun 2 it marks Cash as the credited account. Read it as "and on the right:".

**The exact point it bites:** on Jun 1, "To Capital" would have to mean paying money to the owner — the exact opposite of what happened (the owner paid **in**). The English word is a false friend, exactly like *debit*.

**Your turn**

1. On Jun 3 a business sells goods for Rs 4,60,000 cash: Cash A/C is debited Rs 4,60,000 and Sales A/C is credited Rs 4,60,000. Write this entry out in the full journal format — Date, Particulars, L.F, Debit, Credit — with its narration. Then state which single **visual** feature, not the wording, tells a reader that Sales was the credited account. (Note that "To" is a word, so it does not count as the answer.)

<details><summary>Answer</summary>

| Date | Particulars | L.F | Debit | Credit |
|---|---|---|---|---|
| Jun 3 | Cash A/C **Dr.** | | 4,60,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Sales A/C | | | 4,60,000 |
| | *(Being goods sold for cash)* | | | |

The visual feature is position: the Sales line is indented to the right and its amount sits in the right-hand (Credit) column. The page shows which half is which before a single word is read.

</details>

2. A business's journal contains two entries with the same shape. On Jun 2 it buys goods for Rs 4,00,000 cash: *Purchases A/C Dr. 4,00,000 · To Cash A/C 4,00,000*. On Jun 6 it pays Rs 1,00,000 to a machinery supplier it owes: *Supplier A/C Dr. 1,00,000 · To Cash A/C 1,00,000*. Both credit Cash, and a reader who takes "To Cash" to mean "money paid to Cash" sees the same sentence twice. Explain what actually distinguishes these two entries for a reader scanning the page, and connect that to the journal being chronological.

<details><summary>Answer</summary>

Structurally they are identical — an account debited, Cash credited — so only the Date column and the amounts tell them apart. "To" is just a marker of the credit line, not a description of where money went, so it distinguishes nothing. Because the journal is chronological, the date is an entry's address: it is how an entry is located and how two structurally alike events stay separate.

</details>

---

## E12 — The L.F Column                              [EXT — not in your workbook]

**Definition**

**L.F = Ledger Folio.** *Folio* means **page number**.

It holds the **page number in the ledger** where this journal entry got posted.

**Be told this honestly: your workbook prints the L.F column in the journal format on p.15 and never once says what it is, what goes in it, or why it's there.** It is drawn as an empty box and left as one. It is not a decorative gap.

What it actually is: **a link.**

```
    JOURNAL (by DATE)                    LEDGER (by ACCOUNT)
    +--------------------+               +--------------------+
    | Jun 2  Purchases   |   L.F = 7 --> | page 7:            |
    |        A/C   Dr.   |               | PURCHASES A/C      |
    |          To Cash   |   L.F = 3 --> | page 3:            |
    +--------------------+               | CASH A/C           |
             ^                           +--------------------+
             |                                     |
             +---------- J.F points back ----------+
```

- The journal's **L.F** points **forward**: *this line went to ledger page 7.*
- The ledger's **J.F** (Journal Folio — see the spine's ledger columns) points **back**: *this figure came from journal page 2.*

Together they make every figure in the books **traceable in both directions**. Pick any number anywhere and you can walk to the original event, and from the original event to every place it landed.

**Why that matters — and it's the same reason double-entry exists at all.** A number with no trace is a number nobody can challenge. L.F is what turns "the books balance" into "show me where this Rs 4,00,000 came from" — and gets an answer. The anti-theft device again: the merchant's agent must now not only lie twice consistently, but leave a trail that survives being followed.

**A working rule:** L.F is filled in **when the entry is posted to the ledger**, not when it is journalised. So a blank L.F in a real set of books is meaningful — it means **this entry has not been posted yet.** The column doubles as a posting checklist.

**In action**

The spine's journal leaves L.F blank throughout — the ledger page numbers are not given anywhere in the spine, so no figure can be invented for them. What the column would carry is structural, and can be shown without inventing page numbers:

| Journal line (Jun 2) | L.F would hold | Meaning |
|---|---|---|
| Purchases A/C Dr. 4,00,000 | the ledger page of **Purchases A/C** | this debit landed there |
| To Cash A/C 4,00,000 | the ledger page of **Cash A/C** | this credit landed there |

One entry, **two** L.F values — one per line, because the two halves go to two different ledger pages. The spine's Stage 2 confirms exactly this: Rs 4,00,000 appears on the debit side of Purchases A/C **and** on the credit side of Cash A/C.

Trace the Rs 4,00,000 the whole way:

```
  Jun 2 event  -->  JOURNAL (Jun 2)  -->  L.F  -->  LEDGER: Purchases A/C debit 4,00,000
                                       -->  L.F  -->  LEDGER: Cash A/C credit 4,00,000
```

**Your turn**

1. A business keeps a journal whose entries each carry an **L.F** column (the ledger page a line was posted to, filled in at the moment of posting) and a ledger whose accounts each carry a **J.F** column (the journal page a figure came from). To save time, the owner tells the bookkeeper to stop filling the journal's L.F column, arguing "the ledger's J.F already links the two books, so the trail survives." State what would still be verifiable and what would stop being verifiable.

<details><summary>Answer</summary>

Still verifiable: from any figure in the ledger you can walk back to the journal entry that produced it, because J.F points backwards. Lost: from a journal entry you can no longer confirm it was posted or find where it landed — so an entry that was never posted becomes invisible, and the blank-L.F posting checklist disappears.

</details>

2. A business's journal has all its June entries written and totals Rs 28,10,000 on both sides. Every entry's L.F cells are filled except the Jun 7 entry — commission of Rs 50,000 paid in cash — whose two L.F cells are blank. Given that L.F is filled in when an entry is posted to the ledger, state what the blank tells you has not happened, and name the ledger account whose closing balance is most obviously wrong as a result.

<details><summary>Answer</summary>

The blank says the Jun 7 entry was journalised but never posted to the ledger. Commission A/C is the account most obviously wrong — it would show no balance at all instead of a Rs 50,000 debit (Cash A/C is also overstated by Rs 50,000).

</details>

---

## F1 — The Four Steps in Journalising                          [SOURCED p.15]

**Definition**

Journalising is turning an **event** into an **entry**. Four steps, in this order. The order is the point — step 3 is unanswerable before step 2, and step 2 is unanswerable before step 1.

| Step | What you do | The question you are answering |
|---|---|---|
| **1** | **Identify the accounts involved** | Which accounts does this event touch? |
| **2** | **Determine the nature of each account** | Is each one an asset, liability, capital, income or expense? |
| **3** | **Apply the rules of debit and credit** | Which one goes left, which goes right? |
| **4** | **Record the entry with its narration** | Write it in journal format, with the "Being…" line |

```
  EVENT
    |
    v
  [1] which accounts?  ---------> at least two (D1)
    |
    v
  [2] nature of each?  ---------> asset / liability / capital / income / expense
    |
    v
  [3] which side?      ---------> home side + growing or shrinking (C3)
    |
    v
  [4] write it         ---------> Date · Particulars · L.F · Dr · Cr · Narration
    |
    v
  ENTRY
```

Step 3 is where C3 does its work. **You cannot ask "debit or credit?" before you know what kind of account it is** — because the answer comes from the account's home side in A = L + E, not from the transaction feeling like an increase.

**In action**

**Day 1** — the business started with cash of Rs 20,00,000.

| Step | Working |
|---|---|
| 1 · Accounts | Cash A/C · Capital A/C |
| 2 · Nature | Cash = **asset** · Capital = **capital/equity** |
| 3 · Rules | Cash: asset, home side **left**, growing → **Debit** 20,00,000<br>Capital: equity, home side **right**, growing → **Credit** 20,00,000 |
| 4 · Record | Cash A/C Dr. 20,00,000 · To Capital A/C 20,00,000<br>*(Being capital introduced in cash)* |

**Day 2** — goods purchased for Rs 4,00,000.

| Step | Working |
|---|---|
| 1 · Accounts | Purchases A/C · Cash A/C |
| 2 · Nature | Purchases = **expense** · Cash = **asset** |
| 3 · Rules | Purchases: expense reduces equity (right), so it sits **left** → **Debit** 4,00,000<br>Cash: asset, home side **left**, shrinking → **Credit** 4,00,000 |
| 4 · Record | Purchases A/C Dr. 4,00,000 · To Cash A/C 4,00,000<br>*(Being goods purchased for cash)* |

**Where it bites**

The confusion: skipping step 2 and going straight from step 1 to step 3.

Try it on Day 2.

**Wrong:** Accounts are Purchases and Cash (step 1). Straight to step 3: "we bought goods, we got something, getting = debit; cash went out, out = credit." Right answer by luck. Now try Day 1 the same way: "cash came in = debit; capital… came in too? = debit." **Two debits. Dead.**

**Right:** Step 2 first. Capital is **capital** — home side right. Only then step 3: growing on its home side → credit. Cash is an **asset** — home side left, growing → debit.

**The exact point it bites:** the shortcut works on cash-out transactions and fails the instant both accounts increase. Step 2 is not a formality; it is the step that supplies the *only* information step 3 can use.

**Your turn**

1. A business buys machinery worth Rs 3,00,000 from a supplier on credit — the machinery is delivered now, the money is due later. Journalise this using all four steps explicitly (identify the accounts, determine the nature of each, apply the rules of debit and credit, record the entry with narration). Separately, the same business earlier received Rs 20,00,000 of cash from its owner as capital, and that entry credited Capital A/C. A supplier and an owner are very different people, yet both were credited. Compare what step 2 finds for each, and explain why both are credited.

<details><summary>Answer</summary>

Step 1: Machinery A/C and the supplier's A/C. Step 2: Machinery = asset; supplier = liability (creditor). Step 3: Machinery — asset, home side left, growing → Debit Rs 3,00,000; supplier — liability, home side right, growing → Credit Rs 3,00,000. Step 4: *Machinery A/C Dr. 3,00,000 · To Supplier A/C 3,00,000 (Being machinery purchased on credit)*. Both the supplier (a liability) and Capital (equity) sit on the **right** of A = L + E, and both are growing — a right-side item growing is recorded on its home side, i.e. credited. Both are sources of funds; only the source differs, a supplier rather than the owner.

</details>

2. A business phones a supplier and places an order for goods worth Rs 3,00,000 for delivery next month; the supplier confirms it. The bookkeeper starts the four-step journalising process — identify the accounts, determine their nature, apply the debit and credit rules, record the entry — and gets stuck immediately. State what step 1 returns here, and explain why steps 2, 3 and 4 are never reached.

<details><summary>Answer</summary>

Step 1 returns no accounts at all — nothing was received, given, owed or paid, so no account is touched. Steps 2, 3 and 4 each take an account as their input, so with zero accounts there is nothing to classify, no side to assign and nothing to record. The process ends at step 1, which is exactly what "no entry" means.

</details>

---

## F3 — Narration                                              [SOURCED p.15]

**Definition**

The **narration** is the one-line plain-language statement written **in brackets under every entry**, beginning ***"Being…"***.

It records what the accounts cannot: **what actually happened.**

Why it must exist:

- **Accounts are ambiguous; events are not.** *Cash A/C Dr. 4,60,000 · To Sales A/C 4,60,000* is a shape. *"Being goods sold for cash"* is a fact.
- **It is the only evidence of intent** left in the books. The debit and credit prove the entry balances. They never prove it was the **right** entry.
- **It is read by someone who wasn't there.** An auditor, a partner, the same person eleven months later. Every one of them is a stranger to the event.
- **It survives when memory doesn't.** Six months on, the numbers are still legible and the reason is gone — unless it was written down.

**A narration and a trace do different jobs, and you need both:**

| | Answers | Node |
|---|---|---|
| **L.F** | *Where did this figure go?* | E12 |
| **Narration** | *Why does this figure exist?* | F3 |

**In action**

Day 2 and Day 6 both credit Cash. Strip the narrations and read only the accounts:

| Date | Entry without narration | Can you tell what happened? |
|---|---|---|
| Jun 2 | Purchases A/C Dr. 4,00,000 · To Cash A/C 4,00,000 | Goods were bought — but for cash? on credit later settled? |
| Jun 6 | Arjun & Co. A/C Dr. 1,00,000 · To Cash A/C 1,00,000 | Money went to Arjun & Co. — a payment? a loan? in full? |

Put them back:

| Date | Narration | Now settled |
|---|---|---|
| Jun 2 | *(Being goods purchased for cash)* | **for cash** — that's why Cash, not a supplier, is credited |
| Jun 6 | *(Being part payment to Arjun & Co.)* | **part** payment — Rs 1,00,000 of the Rs 3,00,000 owed |

Jun 6's narration carries a fact the two accounts genuinely cannot: the word ***part***. Without it, Rs 1,00,000 against a Rs 3,00,000 debt looks like an error rather than a deliberate instalment. The spine's ledger confirms it — Arjun & Co. closes at **Rs 2,00,000 credit**, still owed.

The best narration in the spine is the one attached to **no entry at all**:

| Date | Entry | Narration |
|---|---|---|
| Jun 5 | **NO ENTRY** | *(An order placed is not a transaction — nothing received, given, owed or paid)* |

Nothing was recorded, so a reader would otherwise see only a gap between Jun 4 and Jun 6 — and could not tell **"nothing happened"** apart from **"someone forgot."** The narration states which. A narration on an absence is still evidence.

**Where it bites**

The confusion: *"Narration is a formality — the marks are for the debit and credit."*

**Wrong:** Write *Purchases A/C Dr. 4,00,000 · To Cash A/C 4,00,000* and move on. It balances. The maths is right.

**Right:** It balances **and** it is unverifiable. Nobody reading it can confirm the goods were paid for in cash rather than bought on credit — and if they were bought on credit, the entry is wrong while still balancing perfectly.

**The exact point it bites:** balancing is not the same as being correct. A wrong entry balances just as neatly as a right one. The narration is the only line in the entry an outsider can check **against the real world** — and checkability is the whole reason the system was built.

**Your turn**

1. A business sells goods for Rs 4,60,000 and records *Cash A/C Dr. 4,60,000 · To Sales A/C 4,60,000*, with the narration *(Being goods sold for cash)*. A month later it makes a sale of exactly the same goods for exactly Rs 4,60,000, but this time lets the customer pay in thirty days. Write the entry now required, state which account replaces which, and use the difference to explain why the narration is not decoration — given that the original entry balanced perfectly either way.

<details><summary>Answer</summary>

The entry becomes *Customer (Debtor) A/C Dr. 4,60,000 · To Sales A/C 4,60,000* — the customer's account replaces Cash as the debit; the credit to Sales is unchanged. The same amount and the same credit produce a different debit, and both versions balance, so only the narration says which one is correct. It is not decoration: it is the real-world fact the entry claims to represent, and the only line an outsider can check against reality.

</details>

2. A business places an order for goods worth Rs 3,00,000 on Jun 5. Nothing is recorded, because an order is not a transaction — but the journal still carries a Jun 5 line reading **NO ENTRY**, with the note *(An order placed is not a transaction — nothing received, given, owed or paid)*. A reviewer calls this pointless: no amounts, no accounts, so the totals are identical with or without it. State precisely what a reader would conclude if that line were deleted, and name the type of error they could not rule out.

<details><summary>Answer</summary>

They would see an unexplained gap between Jun 4 and Jun 6 and could not tell "nothing happened on Jun 5" apart from "an entry was left out." The error they could not rule out is an error of omission — and no arithmetic check would flag it, since the totals balance either way.

</details>

---

# ACT 3 — To write it, you must name both accounts.

﻿# Act 3 — To write the entry, you must NAME both accounts

## D3 — Classification: Personal / Real / Nominal      [SOURCED p.12]

**Definition**

Every transaction has two sides. Before you can journalise, you must decide what to *call* each side. That single need is what produces account types.

Ask one question of any side of any transaction:

> **"Who or what is on the other side of this?"**

There are exactly three possible answers. That is why there are exactly three types — not because someone chose three buckets.

```
        "Who or what is on the other side?"
                      |
      +---------------+---------------+
      |               |               |
    A THING        A PERSON        A REASON
      |               |               |
    REAL          PERSONAL         NOMINAL
  Machinery      Arjun & Co.      Commission
  Cash           Capital          Sales
```

**The names encode their nature.** Learn the names and you have already learned half the rule.

| Type | Name comes from | What it means | Survives 30 June? |
|---|---|---|---|
| **Real** | *real* = **persisting**, actually there | You could point at it or hold the claim | **Yes** — carried into next period |
| **Personal** | *persona* = **person** | A party, natural or artificial | **Yes** — the debt is still owed |
| **Nominal** | Latin *nomen* = **name** | Exists **in name only** — no physical existence | **No** — closed off at period end |

- **Real** — the machinery is still standing there in April. That is what "real" means here. Not "important". **Persisting.**
- **Nominal** — Commission A/C is not a thing. You cannot walk into the godown and find the commission. It is a **label for a reason** money moved.
- **Personal** — a party you can owe, or who can owe you.

**In action**

All seven accounts in the business's first week, classified:

| Account | Other side is a… | Type | Test |
|---|---|---|---|
| Cash A/C | thing | **Real** | Rs 19,10,000 is still in hand on 30 June |
| Machinery A/C | thing | **Real** | Rs 3,00,000 of machine still there in April |
| Arjun & Co. A/C | person (a firm) | **Personal** | Rs 2,00,000 still owed to it |
| Capital A/C | person (the owner) | **Personal** | Rs 20,00,000 still owed to the owner |
| Purchases A/C | reason | **Nominal** | Rs 4,00,000 — a *reason* cash left |
| Sales A/C | reason | **Nominal** | Rs 4,60,000 — a *reason* cash arrived |
| Commission A/C | reason | **Nominal** | Rs 50,000 — a *reason* cash left |

**Where it bites**

*Purchases A/C — goods are things you can touch, so surely Real?*

**Wrong:** "Day 2, goods worth Rs 4,00,000 came in. Goods are physical. Purchases A/C is Real."

**Right:** **Purchases A/C is Nominal.** It bites here: you are not naming *the goods*, you are naming *the act of buying*. "Purchases" is not an inventory of crates — it is a running label for money spent on stock during the period. Apply the persistence test: on 30 June, Purchases A/C of Rs 4,00,000 is closed off into the income statement as cost of goods sold. Machinery A/C of Rs 3,00,000 is **not** — it walks into the balance sheet.

> **The tell:** if the account name is a *verb-ish activity* (Purchas**es**, Sal**es**, Wag**es**, Rent), it is naming an act, not a thing. Nominal.

**Your turn**

1. A trading business telephones a supplier firm and places a firm order for goods worth Rs 3,00,000. No goods have moved, nothing has been paid, and nothing is yet owed. The bookkeeper wants to open an account in the supplier's name and asks you to classify it. State the type that account *would* have been, and then state why classification never gets to run on this event at all.

<details><summary>Answer</summary>

It would have been **Personal** — a supplier firm is an artificial person. But no account is opened: an order placed is not a transaction (nothing received, given, owed or paid), so there is **no entry** and nothing to classify.

</details>

2. A business holds Rs 19,10,000 of cash at 30 June. Separately, during June it spent Rs 4,00,000 on goods for resale, all of which were sold within June. Both Cash A/C and Purchases A/C carry debit balances. Using **only** the persistence test, show that they are different account types.

<details><summary>Answer</summary>

Cash A/C survives 30 June with its Rs 19,10,000 debit balance and walks into the balance sheet → **Real**. Purchases A/C of Rs 4,00,000 dies at 30 June, closed off into the income statement as cost of goods sold → **Nominal**.

</details>

---

## D4 — Golden rule, Real: debit what comes in, credit what goes out      [SOURCED p.12]

**Definition**

- **Debit what comes IN** to the business.
- **Credit what goes OUT** of the business.

The rule ranges over **things**, not over people or reasons. "In" and "out" mean *across the boundary of the business* — the business is a container, and you record which way the thing crossed.

```
        +---------------------------+
  IN -->|      THE BUSINESS         |--> OUT
 DEBIT  |  (Cash, Machinery, Stock) |  CREDIT
        +---------------------------+
```

**In action**

**Day 4 — machinery purchased on credit, Rs 3,00,000.**

- A machine **came in**. Machinery A/C is Real. → **Debit Machinery A/C 3,00,000.**

**Day 6 — paid Arjun & Co. Rs 1,00,000.**

- Cash **went out**. Cash A/C is Real. → **Credit Cash A/C 1,00,000.**

Every Real-account line in the week, read by direction:

| Day | Real account | Direction | Side | Amount |
|---|---|---|---|---|
| 1 | Cash | in | Debit | 20,00,000 |
| 2 | Cash | out | Credit | 4,00,000 |
| 3 | Cash | in | Debit | 4,60,000 |
| 4 | Machinery | in | Debit | 3,00,000 |
| 6 | Cash | out | Credit | 1,00,000 |
| 7 | Cash | out | Credit | 50,000 |

Cash A/C debits 20,00,000 + 4,60,000 = 24,60,000; credits 4,00,000 + 1,00,000 + 50,000 = 5,50,000. **Closing balance 19,10,000 debit** — exactly what the ledger shows.

**Where it bites**

*Day 3 — goods went out. So credit Goods?*

**Wrong:** "Sold goods Rs 4,60,000. Cash came in — debit Cash. Goods went out — credit Goods A/C."

**Right:**
```
Cash A/C            Dr.    4,60,000
    To Sales A/C                    4,60,000
```
It bites at the word "out". The **Real** rule only fires for an account you are actually keeping as a thing. This business keeps no Goods A/C — the outward movement of stock is captured by the *reason* it left: **Sales A/C, a Nominal account** (D6). Two different rules run on the two sides of the same entry, and that is normal.

> One entry may use **two different golden rules**. Day 4 uses Real (Machinery in) *and* Personal (Arjun & Co. the giver).

**Your turn**

1. In one month a business pays Rs 4,00,000 in cash for goods it intends to resell, and separately pays Rs 1,00,000 in cash to a machinery supplier it already owed money to. Cash A/C is credited Rs 4,00,000 and Rs 1,00,000 respectively. Name the account type of the *other* side of each entry, and state which golden rule fired there.

<details><summary>Answer</summary>

Rs 4,00,000: **Purchases A/C, Nominal** — the Nominal rule (debit all expenses). Rs 1,00,000: the **supplier's A/C, Personal** — the Personal rule (debit the receiver). Two different rules run against the same Cash credit.

</details>

2. An owner starts a business by handing it Rs 20,00,000 of his own cash. The Real rule says "debit what comes in", so Cash A/C is debited Rs 20,00,000. Explain why the **credit** side is not governed by the Real rule, and name the account and rule that do govern it.

<details><summary>Answer</summary>

The credit is **Capital A/C, a Personal account**, governed by "credit the giver" — the owner gave the cash. The Real rule ranges only over the *thing* that crossed the boundary (the cash), never over the party who supplied it.

</details>

---

## D5 — Golden rule, Personal: debit the receiver, credit the giver      [SOURCED p.12]

**Definition**

- **Debit the RECEIVER** — the party who received value from the business.
- **Credit the GIVER** — the party who gave value to the business.

The rule ranges over the **other party**, never over the business itself. The business is the camera; it is not in the photograph.

**Why it works:** a party who received from you now **owes** you → that is a claim → an asset. A party who gave to you is owed **by** you → that is a liability. (C5 makes this exact.)

**In action**

**Day 4 — machinery purchased from Arjun & Co., Rs 3,00,000.**

- Arjun & Co. **gave** the machine and took nothing yet. It is the **giver**. → **Credit Arjun & Co. A/C 3,00,000.**

**Day 6 — paid Arjun & Co. Rs 1,00,000.**

- Arjun & Co. **received** the cash. It is the **receiver**. → **Debit Arjun & Co. A/C 1,00,000.**

The same account, both sides, one week apart:

```
                    Arjun & Co. A/C
      +---------------------------+---------------------------+
Jun 6 | To Cash        1,00,000   | Jun 4  By Machinery  3,00,000
      |   (it RECEIVED)           |          (it GAVE)
Jun 30| To Balance c/d 2,00,000   |
      +---------------------------+---------------------------+
      |                3,00,000   |                    3,00,000
```
**Closing: 2,00,000 credit — still owed.**

**Where it bites**

*"The business received the machine, so debit the receiver."*

**Wrong:** "Day 4 — we received the machinery. We are the receiver. Debit us… debit Arjun & Co.?" — and the entry inverts.

**Right:** **Credit Arjun & Co. A/C 3,00,000.** It bites at "the receiver". There is no account called "us". The Personal rule is always asked about **the named outside party only**. Arjun & Co. handed over a machine and got nothing on Day 4 — it gave. Credit it.

> **Sanity check that never fails:** if you credit Arjun & Co., its balance grows *credit* — meaning **you owe it more**. Rs 3,00,000 owed after Day 4, Rs 2,00,000 after the Day 6 part payment. Does that match reality? Yes. The entry is right.

**Your turn**

1. A business buys machinery on credit for Rs 3,00,000 from a supplier firm, then a few days later pays that firm Rs 1,00,000 in part settlement. The firm's account has therefore been credited Rs 3,00,000 and debited Rs 1,00,000, and stands at Rs 2,00,000 credit. Using **only** the receiver/giver rule, state what a *further* Rs 2,00,000 debit to that account would mean has happened in the real world.

<details><summary>Answer</summary>

The firm received a further Rs 2,00,000 of value from the business — i.e. the remaining debt was paid off in full. The account closes to nil: nothing more is owed.

</details>

2. A business owes a machinery supplier Rs 3,00,000 and hands over Rs 1,00,000 in cash to reduce that debt. The business itself received nothing that day. Show why "debit the receiver" and "credit what goes out" produce one debit and one credit, rather than two debits.

<details><summary>Answer</summary>

Two rules fire on two different sides. The supplier received the Rs 1,00,000, so it is **debited** (Personal). The cash left the business, so **Cash A/C is credited** Rs 1,00,000 (Real). The Personal rule is only ever asked about the named outside party — there is no account called "us" — so the business being the payer never generates a second debit.

</details>

---

## D6 — Golden rule, Nominal: debit expenses/losses, credit incomes/gains      [SOURCED p.12]

**Definition**

- **Debit all EXPENSES and LOSSES.**
- **Credit all INCOMES and GAINS.**

Nominal accounts name **reasons**, not things and not parties. The reason is either money leaving for value consumed (expense/loss) or value arriving as earnings (income/gain).

**In action**

**Day 7 — commission paid, Rs 50,000.**

- Commission is a **reason** cash left. It is an **expense**. → **Debit Commission A/C 50,000.**
- Cash went out → **Credit Cash A/C 50,000.**

**Day 3 — goods sold, Rs 4,60,000.**

- Sales is a **reason** cash arrived. It is an **income**. → **Credit Sales A/C 4,60,000.**
- Cash came in → **Debit Cash A/C 4,60,000.**

All three nominal accounts in the week:

| Nominal A/C | Reason type | Side | Amount | Lands in |
|---|---|---|---|---|
| Purchases | expense (cost of goods sold) | Debit | 4,00,000 | Income statement |
| Sales | income | Credit | 4,60,000 | Income statement |
| Commission | expense | Debit | 50,000 | Income statement |

Sales 4,60,000 − Purchases 4,00,000 = **Gross Profit 60,000**; less Commission 50,000 = **Net Profit 10,000**. Every nominal account, and only the nominal accounts, is consumed by that statement.

> `[INFERRED]` The income statement above treats all Rs 4,00,000 of purchases as sold, because the workbook gives **no closing stock**. Real businesses almost never look like this.

**Where it bites**

*Machinery cost Rs 3,00,000 and cash left. Isn't that an expense too?*

**Wrong:** "Debit Machinery — an expense of Rs 3,00,000 — put it in the income statement alongside the Rs 50,000 commission."

**Right:** **Machinery A/C is Real, not Nominal.** It bites on the word "paid". Both Day 4 and Day 7 involve Rs leaving; only one is an expense.

> **The test:** *after the transaction, do you still control a resource?*
> - Day 4, Rs 3,00,000 → **yes**, a machine. Real. Balance sheet. Equity unmoved — an asset swap.
> - Day 7, Rs 50,000 → **no**, nothing left. Nominal. Income statement. Equity down.

Machinery is absent from the income statement for exactly this reason: **it was not consumed, it was acquired.**

**Your turn**

1. In one month a business pays out Rs 50,000 of commission and separately earns Rs 4,60,000 by selling goods. Commission A/C is debited Rs 50,000; Sales A/C is credited Rs 4,60,000. Both are Nominal accounts. Explain why the same account type takes opposite sides.

<details><summary>Answer</summary>

Nominal accounts name *reasons* money moved, and there are two directions of reason. Commission is an expense — value consumed, equity down — so it is debited. Sales is an income — value earned, equity up — so it is credited. The type fixes that it is a reason; the direction of equity fixes the side.

</details>

2. A business's June shows sales of Rs 4,60,000, cost of goods sold of Rs 4,00,000 and commission paid of Rs 50,000, giving a net profit of Rs 10,000. It also holds machinery that cost Rs 3,00,000. Suppose the Rs 50,000 had instead been spent on more machinery rather than on commission. State the new net profit and the new machinery figure.

<details><summary>Answer</summary>

Machinery becomes **Rs 3,50,000**; net profit becomes **Rs 60,000** — equal to gross profit, since no expense would remain below it. The Rs 50,000 buys a resource still controlled, so it never touches the income statement.

</details>

---

## D7 — Personal accounts include ARTIFICIAL persons — a sports club, a Bank A/C      [SOURCED p.13]

**Definition**

"Personal" does **not** mean "a human being with a face". It means **a party that can hold a claim**. Law recognises two kinds:

| Kind | Meaning | Examples |
|---|---|---|
| **Natural person** | A human being | a sole supplier, a customer, the owner |
| **Artificial person** | An entity law treats *as if* a person — it can owe, be owed, sue and be sued | **Arjun & Co.**, a company, a **sports club**, a **Bank A/C**, a school, a trust |

The test is not "does it breathe?" The test is **"can it owe or be owed?"**

```
   Can this party OWE you, or can you OWE it?
                    |
          +---------+---------+
         YES                  NO
          |                    |
      PERSONAL          Real or Nominal
```

**In action**

**Arjun & Co. A/C — Rs 3,00,000 credited on Day 4, Rs 1,00,000 debited on Day 6.**

- Arjun & Co. is a firm. Nobody named "Arjun & Co." walks the earth.
- Yet it **gave** a machine and it is **owed Rs 2,00,000** on 30 June.
- It can owe and be owed → **artificial person → Personal account.**
- That Rs 2,00,000 appears on the balance sheet under **Liabilities**, because a person is owed.

**Where it bites**

*"Bank A/C holds money. Money is a thing. Bank A/C must be Real, like Cash A/C."*

**Wrong:** Bank A/C = Real, because it feels like Cash A/C.

**Right:** **Bank A/C is a PERSONAL account** — an artificial person. It bites because Cash and Bank *look* like twins.

| | Cash A/C | Bank A/C |
|---|---|---|
| What you hold | the notes themselves | a **claim against the bank** |
| Other side is | a thing | a party |
| Type | **Real** | **Personal** |
| Rule that fires | debit what comes in | debit the receiver |
| If it vanished tonight | the notes are gone | **the bank still owes you** |

The business's Rs 19,10,000 sits in Cash A/C — a Real account, physically held. Had the same Rs 19,10,000 been deposited, it would be a Personal account: an amount the bank **owes back**.

> A sports club is the same shape. It is not a person, it is not a thing, it is not a reason — it is a body that can be owed a subscription. **Personal.**

**Your turn**

1. A supplier firm — a partnership, not a human being — hands over machinery worth Rs 3,00,000 to a business on credit and receives nothing at the time. Its account is **credited** Rs 3,00,000, not debited. A student objects that a firm is not a person and "has no hands to give with". Justify the credit using the receiver/giver rule.

<details><summary>Answer</summary>

The firm gave the machine and got nothing back, so the business owes it Rs 3,00,000 → credit the giver. An artificial person can owe and be owed, and it gives through the people acting for it; the rule tests the **flow of value**, not the presence of hands.

</details>

2. A business owes a machinery supplier Rs 3,00,000 and settles Rs 1,00,000 of it by cheque drawn on its bank account, rather than in notes. Name both accounts in the resulting entry and the type of each.

<details><summary>Answer</summary>

**Dr the supplier's A/C (Personal) Rs 1,00,000; Cr Bank A/C (Personal — an artificial person) Rs 1,00,000.** Both sides are Personal: Bank A/C is not Real, because what you hold is a claim against the bank, not the notes themselves.

</details>

---

## D8 — Nominal identification: the workbook tests the NEGATIVE      [SOURCED p.14 Q4]

**Definition**

The workbook does not ask "which is nominal?" It asks **"which of the following is NOT a nominal account?"**

That inversion changes the work you must do:

- **Positive question** — find **one** match. You can stop at the first hit.
- **Negative question** — you must **classify all four** and find the single misfit. There is no early exit.

Students who memorised a list of nominal examples answer positive questions and fail negative ones, because a list tells you what *is* on it, never what *is not*.

**The format**

Run the same three-way question on **every** option, then invert:

```
For each option:  "Who or what is on the other side?"
     thing  -> Real      -+
     person -> Personal   +-> these are the ANSWER to a NOT-nominal question
     reason -> Nominal   -+-> these are eliminated
```

**In action**

Take the seven accounts in the books as a four-option question. *Which is NOT a nominal account?*

| Option | Other side | Type | Nominal? |
|---|---|---|---|
| (a) Purchases A/C | reason | Nominal | yes → eliminate |
| (b) Sales A/C | reason | Nominal | yes → eliminate |
| (c) Commission A/C | reason | Nominal | yes → eliminate |
| (d) **Machinery A/C** | thing | **Real** | **no → ANSWER** |

**Answer: (d) Machinery A/C.**

The confirmation is arithmetic, not memory. Options (a), (b), (c) — Rs 4,00,000, Rs 4,60,000 and Rs 50,000 — are all consumed by the income statement and leave nothing behind. Option (d) — Rs 3,00,000 — stands on the balance sheet on 30 June. **Only the misfit persists.**

**Where it bites**

*Reading speed.*

**Wrong:** eyes land on "Commission A/C", brain fires "expense — nominal — that's the one", and circles (c). The classification was **correct**; the answer is wrong.

**Right:** **(d) Machinery A/C.** It bites at the word **NOT**, which the eye skips because it is short. The defence is mechanical: **write the type beside all four options before choosing anything.** Three will agree; circle the one that disagrees.

> Every account in these books passes the persistence test the same way: Cash 19,10,000, Machinery 3,00,000, Capital 20,00,000 and Arjun & Co. 2,00,000 survive 30 June. Purchases, Sales and Commission do not. **Survivors are never nominal.**

**Your turn**

1. A business's June books contain exactly seven accounts: Cash Rs 19,10,000, Machinery Rs 3,00,000, a machinery supplier owed Rs 2,00,000, Capital Rs 20,00,000, Purchases Rs 4,00,000, Sales Rs 4,60,000 and Commission Rs 50,000. Using only these seven, build a four-option *"which of the following is NOT a nominal account?"* question whose correct answer is a **Personal** account. State your answer.

<details><summary>Answer</summary>

Three nominal accounts plus one personal one — e.g. (a) Purchases A/C (b) Sales A/C (c) Commission A/C (d) Capital A/C. **Answer: (d) Capital A/C** — it is Personal: it names the owner, a party the business owes. The supplier's A/C works equally well as the misfit.

</details>

2. A question reads: *"Which of the following is NOT a nominal account? (a) Purchases A/C Rs 4,00,000 (b) Sales A/C Rs 4,60,000 (c) Commission A/C Rs 50,000 (d) Machinery A/C Rs 3,00,000."* A student circles (c), reasoning correctly that commission paid is an expense and therefore nominal. The correct answer is (d). Explain precisely which step failed.

<details><summary>Answer</summary>

The classification step succeeded — Commission genuinely is nominal. The **question-reading step** failed: the student answered the positive question ("which IS nominal?") and skipped the word **NOT**, so a correct classification produced a wrong selection. The defence is to write the type beside all four options first and circle the one that disagrees.

</details>

---

## D9 — Capital A/C is a PERSONAL account — and why      [SOURCED p.13 item 10]

**Definition**

Capital A/C is **Personal**. Not Real (Rs 20,00,000 of "capital" is not a thing you can point at) and not Nominal (it does not close off on 30 June — it persists).

It is Personal because of the **Business Entity concept**:

> The business and the owner are **two separate persons**. Money the owner puts in is money the **business owes back**.

```
   +-----------+   gives Rs 20,00,000 cash    +--------------+
   |   OWNER   | ---------------------------> |   BUSINESS   |
   | (a person)| <--------------------------- | (the entity) |
   +-----------+     owes it back  = CAPITAL  +--------------+
```

- The owner is the **giver** on Day 1 → **credit the giver** → Capital A/C credited.
- Same rule that credited Arjun & Co. **Capital is a payable to the owner.** The only differences are that the owner is last in the queue and never sends a reminder.

**In action**

**Day 1 — started business with cash Rs 20,00,000.**

```
Cash A/C            Dr.   20,00,000        <- Real: what came IN
    To Capital A/C              20,00,000  <- Personal: the GIVER
```

On 30 June:

- **Capital A/C closing: 20,00,000 credit.** It persists — so it is not nominal.
- Balance sheet: Capital 20,00,000 *add* Net Profit 10,000 = **20,10,000**, sitting on the **Liabilities & Equity** side, one column across from Arjun & Co.'s Rs 2,00,000.
- **A = L + E:** 22,10,000 = 2,00,000 + 20,10,000. Capital sits where a person's claim sits, because it **is** one.

**Where it bites**

*"The Rs 20,00,000 is the owner's own money. How can the business owe him his own money?"*

**Wrong:** treat Capital as belonging to the owner, so nothing is owed, so no credit is needed — and Day 1 has no second side.

**Right:** It bites the moment Business Entity is dropped. **Drop the concept and the entry is unwritable.** Without a separate entity there is no boundary for cash to come "in" across, no party to have "given", and no credit to pair with the Rs 20,00,000 debit.

The proof is in the profit figure:

| | Amount |
|---|---|
| Net profit for June | **10,000** |
| Cash in hand on 30 June | **19,10,000** |

Neither number explains the other. Cash is high because **Rs 20,00,000 was supplied by the owner, not earned by the business**. Capital A/C is the account that keeps those two facts from being confused — a *source*, not a performance.

**Your turn**

1. At 30 June a business's Capital A/C closes at Rs 20,00,000 credit, and the account of a firm that supplied it machinery on credit closes at Rs 2,00,000 credit. The owner insists his capital is "his own money" and nothing at all like a supplier's unpaid bill, yet both sit in the same column of the balance sheet, totalling Rs 22,10,000 with the profit added. Name the one economic feature they share that puts them there.

<details><summary>Answer</summary>

Both are **amounts the business owes to an outside party** — a person's claim against the business. Under the Business Entity concept the owner is as separate from the business as the supplier is, so both are credit balances and both sit on the Liabilities & Equity side.

</details>

2. An owner introduced Rs 20,00,000 of cash into his business, which then earned a net profit of Rs 10,000 for June. The closing balance sheet shows Capital of Rs 20,10,000, not Rs 20,00,000. Explain what the Rs 10,000 addition is doing to the owner's claim, and why it is credited rather than debited.

<details><summary>Answer</summary>

The Rs 10,000 was earned by the business on the owner's behalf, so the amount the business owes him grows from Rs 20,00,000 to Rs 20,10,000. Equity lives on the right of A = L + E, and right-side items grow by credit — so the increase is credited.

</details>

---

## D10 — Significance of the golden rules      [SOURCED p.14]

**Definition**

The golden rules do four jobs. Each one is a job nothing else in the system does at this stage.

| # | What the rules do | What it prevents |
|---|---|---|
| 1 | **Force a two-sided entry.** Naming a debit forces you to hunt for its credit. | One-sided entries; unbalanced books |
| 2 | **Make the treatment uniform.** The same transaction gets the same entry in any set of books, by anyone. | Books that only their author can read |
| 3 | **Give a decision procedure.** Classify, then apply — no judgement call, no taste. | Guessing the side |
| 4 | **Guarantee Σ debits = Σ credits mechanically.** Every rule pairs a debit with a credit. | Arithmetic drift |

**They are a SHORTCUT, not the foundation.** The foundation is A = L + E (see **C5**). The rules are the equation pre-solved for the cases you meet daily, so you do not re-derive the equation seven times a week.

**In action**

The rules ran seven times in the first week and produced this:

| | Debit | Credit |
|---|---|---|
| **Journal totals** | **28,10,000** | **28,10,000** |
| **Trial balance totals** | **26,60,000** | **26,60,000** |

Both sides agree, and **nobody added them up hoping**. Each of the six entries was forced into balance at the moment it was written, by a rule. Balance is a *consequence* of the rules, not a target you aim at.

> **Job 4 in one line:** Day 4 debits Machinery 3,00,000 (Real: came in) and credits Arjun & Co. 3,00,000 (Personal: the giver). Two rules, one amount, automatic balance.

**Where it bites**

*Believing the rules also make the books CORRECT.*

**Wrong:** "The trial balance totals Rs 26,60,000 on both sides. The golden rules were followed. The books are right."

**Right:** The rules guarantee **balance**, never **truth**. Now omit Day 7 entirely — never journalise the Rs 50,000 commission at all:

| | Full books | Day 7 omitted |
|---|---|---|
| Cash | 19,10,000 | **19,60,000** *(the 50,000 never left)* |
| Purchases | 4,00,000 | 4,00,000 |
| Machinery | 3,00,000 | 3,00,000 |
| Commission | 50,000 | **— gone —** |
| **Debit total** | **26,60,000** | **26,60,000** |
| **Credit total** | **26,60,000** | **26,60,000** |

**The total does not change. Not by one rupee.** The Rs 50,000 simply moves out of Commission and stays in Cash. It bites here: the rules police the *form* of each entry, and an entry never written has no form to police. **The rules cannot see an absence.**

**Your turn**

1. A business's June journal totals Rs 28,10,000 on each side, while its trial balance for the same month totals Rs 26,60,000 on each side. Cash featured in five of the six entries, but appears once in the trial balance, at Rs 19,10,000. Both statements are "balanced". An auditor claims the difference between the two totals proves an entry was mis-posted. Explain what each total measures, and why the difference is not an error.

<details><summary>Answer</summary>

The journal total of Rs 28,10,000 measures **movements** — every debit and credit as it happened, so Cash is counted five times. The trial balance total of Rs 26,60,000 measures **balances** — each account once, Cash netted to Rs 19,10,000. Different quantities, so they are not meant to agree; the auditor is wrong.

</details>

2. The golden rules do four jobs: (1) force a two-sided entry, (2) make the treatment uniform across anyone's books, (3) give a decision procedure for choosing the side, and (4) guarantee Σ debits = Σ credits mechanically. A bookkeeper writes up a whole month with every entry's debit and credit **systematically swapped** — cash received is credited, cash paid is debited, and so on throughout. The trial balance still agrees. State which of the four jobs are still done and which fail.

<details><summary>Answer</summary>

**Jobs 1 and 4 still hold** — every entry is still two-sided and the totals still agree, which is exactly why the trial balance notices nothing. **Jobs 2 and 3 fail**: the treatment no longer matches anyone else's books, and the decision procedure has been inverted, so every balance reports the wrong direction. Balance is not truth.

</details>

---

## A6 — Revenue      [SOURCED p.2]

**Definition**

**Revenue** is value the business **earns** from its normal activity — the inflow that arises from doing the thing the business exists to do.

- It is **not** "cash received". Cash received from the owner is not revenue. Cash received from a lender is not revenue.
- It is **earned**, not supplied. The test: **did the business give up goods or services to get it?**

**Revenue is not a separate species. It is EQUITY IN MOTION — upward.** Earnings grow the owner's stake, so revenue behaves exactly like equity: **credit**.

**In action**

**Day 3 — sold goods Rs 4,60,000.** Revenue. The business handed over goods and earned the inflow. → **Credit Sales A/C 4,60,000.**

**Day 1 — Rs 20,00,000 cash in.** **NOT revenue.** Nothing was given up; the owner supplied it. → **Credit Capital A/C 20,00,000.**

Two inflows of cash, one week apart, and only one is revenue:

| Day | Cash in | Did the business give up goods/services? | Revenue? | Credit goes to |
|---|---|---|---|---|
| 1 | 20,00,000 | **No** — the owner supplied it | **No** | Capital A/C (Personal) |
| 3 | 4,60,000 | **Yes** — goods went out | **Yes** | Sales A/C (Nominal) |

Sales of Rs 4,60,000 is the **only** revenue in the week — and it is the top line of the income statement.

**Where it bites**

*The biggest inflow is not the revenue.*

**Wrong:** "Rs 20,00,000 came in on Day 1 and Rs 4,60,000 on Day 3. Revenue for June = Rs 24,60,000."

**Right:** **Revenue = Rs 4,60,000.** It bites because Rs 20,00,000 is four times larger and arrives first, so it feels like the main event. It is a **source of funds**, not an earning. Put it in revenue and net profit stops being Rs 10,000 and starts being fiction.

**Your turn**

1. An owner started a business in June by paying in Rs 20,00,000 of his own cash. During the same month the business sold goods for Rs 4,60,000 cash and paid out Rs 5,50,000 of cash for various purposes, ending 30 June with Rs 19,10,000 in hand. Its revenue for June is only Rs 4,60,000. A friend looks at the cash and says the business "must have taken in Rs 24,60,000". Explain the gap between the Rs 19,10,000 of cash and the Rs 4,60,000 of revenue **without using the word "profit"**.

<details><summary>Answer</summary>

The Rs 19,10,000 is mostly the owner's Rs 20,00,000 — a **source of funds**, not an earning, because the business gave up nothing to get it. Only the Rs 4,60,000 was earned by handing over goods. The rest of the movement is the Rs 5,50,000 of cash that went back out. Cash measures a stock of money; revenue measures what was earned.

</details>

2. A **customer** telephones a business and places a firm, signed order for Rs 3,00,000 of goods, to be delivered next month. The customer is reliable and has never missed a payment. Nothing has shipped and nothing has been paid. The owner tells the bookkeeper: *"That's Rs 3,00,000 of sales — book it, we've earned it."* State whether revenue arises, and name the exact condition in the revenue definition that decides it.

<details><summary>Answer</summary>

**No revenue arises.** The condition is that the business must have **given up goods or services**. Nothing has been handed over, so nothing has been earned — the customer's reliability is irrelevant, because it speaks to whether payment will *eventually* come, not to whether anything has been *earned yet*. A signed order is a promise about the future; revenue records the past.

</details>

---

## A7 — Expenses      [SOURCED p.2]

**Definition**

An **expense** is value the business **consumes** to earn revenue. It is gone. Nothing is left that you control.

- It is **not** "cash paid". Paying a supplier what you already owe is not an expense.
- It is **not** "buying something". Buying a machine gives you a machine.

**The test:** *after the transaction, do you still control a resource?*
- **No** → **expense** → income statement.
- **Yes** → **asset** → balance sheet.

**Expenses are EQUITY IN MOTION — downward.** They shrink the owner's stake, so they take the side opposite to equity: **debit**.

**In action**

**Day 7 — commission paid Rs 50,000.** After paying, the business controls nothing. **Expense.** → **Debit Commission A/C 50,000.** Equity down.

**Day 4 — machinery Rs 3,00,000.** After the purchase, the business controls a machine. **Asset.** → **Debit Machinery A/C 3,00,000.** Equity unmoved — an **asset swap**.

**Day 6 — paid Arjun & Co. Rs 1,00,000.** Cash left. **Not an expense** — a debt shrank. Assets down 1,00,000, liabilities down 1,00,000. Equity unmoved.

| Day | Amount | Resource left afterwards? | Verdict | Effect on equity |
|---|---|---|---|---|
| 2 | 4,00,000 | goods — but sold within the period | **Expense** (COGS) | **Down** |
| 4 | 3,00,000 | **yes** — a machine | **Asset** | **Unmoved** |
| 6 | 1,00,000 | **no** — but no value consumed either | **Debt settlement** | **Unmoved** |
| 7 | 50,000 | **no** | **Expense** | **Down** |

Only Days 2 and 7 reach the income statement: 4,00,000 + 50,000 against Sales 4,60,000 → **Net Profit 10,000**.

**Where it bites**

*Three payments of cash. Only two are expenses. Only one is obvious.*

**Wrong:** "Cash left on Days 2, 4, 6 and 7 — Rs 4,00,000 + Rs 3,00,000 + Rs 1,00,000 + Rs 50,000. That is Rs 8,50,000 of expenses. The business lost Rs 3,90,000 in its first week."

**Right:** **Expenses = Rs 4,50,000. Net profit = Rs 10,000.** It bites at "cash left", which is not a test of anything.

- Day 4's Rs 3,00,000 bought a **machine you still have** → asset, not expense.
- Day 6's Rs 1,00,000 **settled a debt already recorded** on Day 4 → recording it again as an expense counts the machinery twice.

> **Machinery is absent from the income statement.** It was **not consumed, it was acquired.**

**Your turn**

1. In one month a business buys a machine for Rs 3,00,000, which it still owns and uses at month end, and separately pays Rs 50,000 of commission for a service already rendered. Both amounts are debited. The owner wants both listed as costs of the month. Apply the resource test to each and state which statement each amount lands in.

<details><summary>Answer</summary>

Machinery Rs 3,00,000: a resource is **still controlled** afterwards → **asset → balance sheet**, equity unmoved (an asset swap). Commission Rs 50,000: **nothing is controlled** afterwards → **expense → income statement**, equity down. The owner is wrong about the machine — it was not consumed, it was acquired.

</details>

2. A business bought machinery on credit for Rs 3,00,000, owing the supplier firm that amount. It later pays the firm Rs 1,00,000 in cash, consuming nothing; the firm appears on the closing balance sheet at Rs 2,00,000. Show what that Rs 1,00,000 payment did to the supplier's claim rather than to profit.

<details><summary>Answer</summary>

It cut the supplier's claim from Rs 3,00,000 to the Rs 2,00,000 shown on the balance sheet. Assets fell Rs 1,00,000 and liabilities fell Rs 1,00,000 — equity, and therefore profit, was untouched. Treating it as an expense would count the machinery's cost a second time.

</details>

---

## C4 — Why assets + expenses share a normal DEBIT balance, and liabilities + equity + revenue share CREDIT      [EXT — not in your workbook]

**Definition**

Not a convention to be memorised. It falls out of the equation's geometry.

```
        A        =        L        +        E
   +---------+        +---------------------------+
   |  LEFT   |        |          RIGHT            |
   |  DEBIT  |        |          CREDIT           |
   +---------+        +---------------------------+
   Assets              Liabilities      Equity
```

**Rule of the geometry:** an account **grows on the side of the equation it lives on**.

Now expand equity — because revenue and expenses are not extra species, they are **equity in motion**:

> **Equity = Capital + Revenue − Expenses − Drawings**

- **Revenue** carries a **plus** inside equity → equity lives right → revenue grows **right** → **credit**.
- **Expenses** carry a **minus** inside equity → a *reduction* of a right-side item grows **left** → **debit**.

That is the whole derivation. Five families, one line each:

| Family | Lives / acts on | Grows by | Normal balance | From the books |
|---|---|---|---|---|
| **Assets** | Left of A = L + E | Debit | **Debit** | Cash 19,10,000 Dr · Machinery 3,00,000 Dr |
| **Expenses** | Minus inside right-side E | Debit | **Debit** | Purchases 4,00,000 Dr · Commission 50,000 Dr |
| **Liabilities** | Right | Credit | **Credit** | Arjun & Co. 2,00,000 Cr |
| **Equity** | Right | Credit | **Credit** | Capital 20,00,000 Cr |
| **Revenue** | Plus inside right-side E | Credit | **Credit** | Sales 4,60,000 Cr |

**In action**

The trial balance is this table, sorted:

| Account | Family | Debit | Credit |
|---|---|---|---|
| Cash A/C | Asset | 19,10,000 | |
| Purchases A/C | Expense | 4,00,000 | |
| Machinery A/C | Asset | 3,00,000 | |
| Commission A/C | Expense | 50,000 | |
| Capital A/C | Equity | | 20,00,000 |
| Sales A/C | Revenue | | 4,60,000 |
| Arjun & Co. A/C | Liability | | 2,00,000 |
| **TOTAL** | | **26,60,000** | **26,60,000** |

**Read the debit column:** assets and expenses. Nothing else. **Read the credit column:** liabilities, equity and revenue. Nothing else. Not one exception in seven accounts — because the equation has no exceptions.

**Where it bites**

*"Assets and expenses are both debits — so an expense must be a kind of asset."*

**Wrong:** Machinery Rs 3,00,000 and Commission Rs 50,000 both sit in the debit column, so treat both as things the business has.

**Right:** They share a **side**, not a **nature**. It bites because the trial balance column hides the reason.

| | Machinery 3,00,000 | Commission 50,000 |
|---|---|---|
| Why it is a debit | it **is** a left-side item (an asset) | it **reduces** a right-side item (equity) |
| Effect on equity | **none** — asset swap | **down 50,000** |
| Where it goes on 30 June | Balance sheet | Income statement |
| Alive on 1 July | **yes** | **no** |

**Same column. Opposite lives.**

**Your turn**

1. At 30 June a business's Sales A/C stands at Rs 4,60,000 credit, and the account of a firm that supplied it machinery on credit stands at Rs 2,00,000 credit. Sitting in the same trial balance column, they look like the same kind of thing. Derive each credit **separately** from A = L + E, and state why they end on the same side for different reasons.

<details><summary>Answer</summary>

Sales Rs 4,60,000 is revenue — a **plus inside equity**, and equity is on the right of A = L + E, so it grows by credit. The supplier's Rs 2,00,000 is a **liability** — itself a right-side item, so it grows by credit. Same side, two different routes: one is equity in motion, the other is L itself.

</details>

2. A business's owner introduced Rs 20,00,000 of capital. During June it earned sales of Rs 4,60,000, incurred cost of goods sold of Rs 4,00,000 and commission of Rs 50,000, and the owner withdrew nothing. Its balance sheet shows equity of Rs 20,10,000. A student assumes that Rs 20,10,000 is a separately calculated figure. Using Equity = Capital + Revenue − Expenses − Drawings and only these figures, show that it is the equation's output.

<details><summary>Answer</summary>

20,00,000 + 4,60,000 − (4,00,000 + 50,000) − nil = **Rs 20,10,000** — identical to Capital 20,00,000 + Net Profit 10,000 on the balance sheet. It is the equation restated, not a fresh number.

</details>

---

## C5 — Deriving each golden rule from A = L + E: the rules as SHORTCUT, not foundation      [EXT — not in your workbook]

**Definition**

There are not three rules. There is **one question**, asked three times:

> **"Which side of A = L + E does this account live on?"**

Left → debit to grow. Right → credit to grow. That is all. The three golden rules are that single question, **pre-answered** for the three kinds of account — so you can journalise at speed instead of re-deriving the equation for every line.

**The derivation table — this is the payload**

| Golden rule | The account is really… | Equation side | Grows on | Therefore the rule reads | ✓ |
|---|---|---|---|---|---|
| **Real:** debit what comes in | a **thing** = an **asset** | **LEFT** (A) | Debit | something coming in grows an asset → **debit it** | ✓ |
| **Real:** credit what goes out | an **asset** leaving | LEFT (A) | shrinks Credit | an asset falling is the opposite of growth → **credit it** | ✓ |
| **Personal:** debit the receiver | a party who received now **owes you** = a **receivable** = an **asset** | **LEFT** (A) | Debit | the receiver's debt to you grew → **debit it** | ✓ |
| **Personal:** credit the giver | a party who gave is **owed by you** = a **liability** | **RIGHT** (L) | Credit | your debt to it grew → **credit it** | ✓ |
| **Nominal:** debit all expenses | a **reduction of equity** | equity is **RIGHT**, so its reduction is **LEFT** | Debit | equity shrank → **debit it** | ✓ |
| **Nominal:** credit all incomes | an **increase of equity** | **RIGHT** (E) | Credit | equity grew → **credit it** | ✓ |

**All six lines are one line.** Left grows by debit; right grows by credit. Everything else is vocabulary.

```
   A = L + E
   |         \
   LEFT       RIGHT
   |             \
   assets         liabilities, equity
   |                 \
   "comes in"         "the giver"        <- Real / Personal vocabulary
   "the receiver"     "incomes"          <- Personal / Nominal vocabulary
   "expenses"                            <- (reduction of a RIGHT item = LEFT)
```

**In action**

Derive Day 4 (Rs 3,00,000, machinery from Arjun & Co.) **without using any golden rule at all**:

1. A machine arrives → **assets up 3,00,000** → assets are LEFT → **debit Machinery 3,00,000**.
2. Nothing was paid → the business now **owes** Arjun & Co. → **liabilities up 3,00,000** → liabilities are RIGHT → **credit Arjun & Co. 3,00,000**.
3. Equity untouched. **A up 3,00,000 = L up 3,00,000 + E unmoved.** ✓

Now the golden-rule route: *Machinery came in → debit. Arjun & Co. gave → credit.* **Identical entry. One-tenth the words.** That is what a shortcut is.

Derive Day 7 (commission Rs 50,000) the same way:

1. Cash leaves → **assets down 50,000** → LEFT item falling → **credit Cash 50,000**.
2. Nothing acquired → value consumed → **equity down 50,000** → equity is RIGHT, so its fall is **debit Commission 50,000**.
3. **A down 50,000 = L unmoved + E down 50,000.** ✓ — and the balance sheet confirms it: Capital 20,00,000 + Net Profit 10,000 = 20,10,000, where that Rs 10,000 already has the Rs 50,000 subtracted.

**Where it bites**

*Treating the rules as the foundation.*

**Wrong:** "Debit the receiver" — memorised, whole, from nowhere. So when a novel account arrives that is neither a thing nor a person nor an obvious reason, there is nothing to fall back on and the student guesses.

**Right:** The rules are **derived**, so they are **re-derivable**. It bites at exactly the moment the workbook's ten examples run out.

- **Memorised rules** → work on the ten listed accounts, fail on the eleventh.
- **Derived rules** → work on any account ever invented, because A = L + E has no eleventh case.

See **D12** for the eleventh case.

**Your turn**

1. A business owes a machinery supplier Rs 3,00,000 and pays it Rs 1,00,000 in cash, leaving Rs 2,00,000 owed. Derive the entry from **A = L + E alone**, without naming any golden rule, and show the equation still holds afterwards.

<details><summary>Answer</summary>

Cash leaves → assets down Rs 1,00,000 → a left-side item falling → **credit Cash Rs 1,00,000**. The debt shrinks → liabilities down Rs 1,00,000 → a right-side item falling → **debit the supplier Rs 1,00,000**. A down 1,00,000 = L down 1,00,000 + E unmoved. The equation holds.

</details>

2. "Debit the receiver" governs a party who took value from the business; "debit what comes in" governs a thing crossing into the business. They are taught as two unrelated rules, so a student meeting an account that is neither an obvious thing nor an obvious party has nothing to fall back on. Show that the two rules are the same instruction in disguise, by naming the equation side both point at.

<details><summary>Answer</summary>

Both point at the **LEFT side of A = L + E**. "What comes in" is an asset arriving; "the receiver" now owes you, which is a receivable — also an asset. Both are left-side items growing, and left-side items grow by debit. One instruction, two vocabularies.

</details>

---

## C7 — Translating both ways: equation ↔ golden-rule vocabulary      [EXT — not in your workbook]

**Definition**

Two languages describe one system. Exams and textbooks switch between them without warning, so you must translate in **both** directions on demand.

| Equation language | Golden-rule language |
|---|---|
| asset increases | "what comes in" / "the receiver" |
| asset decreases | "what goes out" |
| liability increases | "the giver" |
| liability decreases | "the receiver" |
| equity increases | "income or gain" / "the giver" (owner) |
| equity decreases | "expense or loss" |

**The format**

Translate in four steps, in this order, every time:

```
  1. WHAT MOVED?        (a thing / a party / a reason)
  2. WHICH FAMILY?      (asset / liability / equity / revenue / expense)
  3. WHICH SIDE OF A = L + E?   -> left or right
  4. GROWING OR SHRINKING?      -> left+grow = Dr | right+grow = Cr
                                   left+shrink = Cr | right+shrink = Dr
```

**In action — translating the full week, both directions**

| Day | Equation language | Golden-rule language | Entry |
|---|---|---|---|
| 1 | A ↑ 20,00,000; E ↑ 20,00,000 | cash came **in**; owner **gave** | Dr Cash 20,00,000 / Cr Capital 20,00,000 |
| 2 | A ↓ 4,00,000; E ↓ 4,00,000 | **expense** incurred; cash **out** | Dr Purchases 4,00,000 / Cr Cash 4,00,000 |
| 3 | A ↑ 4,60,000; E ↑ 4,60,000 | cash came **in**; **income** earned | Dr Cash 4,60,000 / Cr Sales 4,60,000 |
| 4 | A ↑ 3,00,000; L ↑ 3,00,000 | machine came **in**; supplier **gave** | Dr Machinery 3,00,000 / Cr Arjun & Co. 3,00,000 |
| 5 | **nothing moves** | nothing in, out, received or given | **NO ENTRY** |
| 6 | A ↓ 1,00,000; L ↓ 1,00,000 | supplier **received**; cash **out** | Dr Arjun & Co. 1,00,000 / Cr Cash 1,00,000 |
| 7 | A ↓ 50,000; E ↓ 50,000 | **expense** incurred; cash **out** | Dr Commission 50,000 / Cr Cash 50,000 |

**Reverse translation — golden-rule → equation.** Given only *"Dr Arjun & Co. 1,00,000 / Cr Cash 1,00,000"*:

- Arjun & Co. is Personal, debited → a liability shrinking → **L ↓ 1,00,000** (right side falls).
- Cash is Real, credited → an asset shrinking → **A ↓ 1,00,000** (left side falls).
- **Both sides of the equation fall by 1,00,000. Equity untouched.** The balance sheet agrees: Arjun & Co. stands at Rs 2,00,000, not Rs 3,00,000.

**Where it bites**

*Day 5 — the bait.*

Day 5 places an order for Rs 3,00,000 — the **same amount** as Day 4's credit purchase, **two lines later**. It is shaped exactly like a real transaction.

**Wrong:** "An order for Rs 3,00,000 → someone will give goods → credit the giver." The golden-rule vocabulary **has a phrase ready**, and the phrase fires on nothing.

**Right:** **NO ENTRY.** It bites because the golden-rule language runs on *words in the sentence*, while the equation language runs on *movement*. Translate to the equation first: after the order, **A unchanged, L unchanged, E unchanged.** Nothing was received, given, owed or paid. No movement, no entry.

> **Direction of travel matters.** Equation → golden rules is safe. Golden rules → equation without checking movement is how Day 5 gets journalised. **Always ask "what moved?" before "which rule?"**

**Your turn**

1. A business buys a machine for Rs 3,00,000 on credit from a supplier firm, paying nothing at the time. The entry written is *"Dr Machinery 3,00,000 / Cr [the supplier] 3,00,000."* Translate it into equation language, state the resulting balance on the supplier's account, and state why net profit is unaffected even though Rs 3,00,000 of value entered the books.

<details><summary>Answer</summary>

**A up Rs 3,00,000** (machinery) and **L up Rs 3,00,000** (the supplier); equity unmoved. The supplier's account stands at **Rs 3,00,000 credit — owed in full**. Net profit is unaffected because nothing was consumed: the business swapped a promise for a resource it still controls, so no expense arises.

</details>

2. In one week a business buys a machine on credit for Rs 3,00,000 from one supplier, and separately telephones another supplier to place an order for Rs 3,00,000 of goods. Same amount, same goods-and-supplier language — "someone will give us goods" fits both. Only one is journalised. Name the single test that separates them, and state which of the two languages — equation or golden-rule — supplies it.

<details><summary>Answer</summary>

The test is **"what moved?"** The machine moved and created a debt; the order moved nothing — A, L and E are all unchanged, so **no entry**. The **equation language** supplies the test, because it runs on movement in A, L and E; the golden-rule language runs on the words in the sentence and fires on nothing.

</details>

---

## D12 — Classifying a NOVEL account the workbook never lists      [EXT — not in your workbook]

**Definition**

The workbook lists roughly ten examples. Exams do not promise to stay inside them. A rote-trained student has a **lookup table**; a derived student has a **procedure**.

**Memorising three rules cannot pass this node.** The rules tell you what to do *once you know the type*. They never tell you the type.

**The format**

Four questions. In this order. No exceptions.

```
  Q1  Is it a THING or a claim you hold?          -> yes: REAL
  Q2  Is it a PARTY that can owe or be owed?      -> yes: PERSONAL
        (natural OR artificial: a firm, a bank, a club)
  Q3  Is it a REASON money moved this period?     -> yes: NOMINAL
  Q4  CONFIRM with persistence:
        survives period end -> Real or Personal
        dies at period end  -> Nominal
```
Q4 is not optional. It is the check that catches a wrong answer to Q1–Q3.

**In action — three accounts the workbook never lists**

**1. Prepaid Insurance A/C**

- Q1 — Is it a thing? You paid in advance; the insurer now **owes you cover**. That is a **claim you hold**. → **Real** (an asset).
- Q3 — Is it a reason money moved? Tempting: it has the word *insurance* in it, and Insurance A/C is Nominal. But **Prepaid Insurance** is not the cost consumed — it is the part **not yet** consumed.
- Q4 — Persistence: does it survive 30 June? **Yes.** Cover not yet used is still yours in July. → **Real confirmed.**
- **Side:** an asset → LEFT → **debit balance.**

**2. Goodwill A/C**

- Q1 — Is it a thing? You cannot touch it. But you **control it** and it has value. → **Real** (an intangible asset).
- Q4 — Persistence: **survives every period end.** → **Real confirmed.**
- **The trap:** "cannot be touched → nominal". False. **Nominal means existing in name only for one period, not merely invisible.** Machinery is visible and Goodwill is not, yet both are Real, because both **persist**.
- **Side:** an asset → LEFT → **debit balance.**

**3. Outstanding Salary A/C**

- Q1 — a thing? No.
- Q2 — a party? The staff are owed. The account **names the amount owed**, and it behaves exactly as a payable does. → **Personal** (representative personal — it *stands in for* the persons owed).
- Q4 — Persistence: **survives 30 June** — the salary is still unpaid on 1 July. → **not Nominal.**
- **Side:** a liability → RIGHT → **credit balance.**
- **The structural analogue in these books:** it behaves like **Arjun & Co. A/C, closing Rs 2,00,000 credit — still owed.** Same shape, different creditor.

**The scoreboard**

| Novel account | Q1 thing? | Q2 party? | Q3 reason? | Q4 persists? | **Type** | Normal balance |
|---|---|---|---|---|---|---|
| Prepaid Insurance A/C | **yes** (a claim) | no | no | **yes** | **Real** | Debit |
| Goodwill A/C | **yes** (intangible) | no | no | **yes** | **Real** | Debit |
| Outstanding Salary A/C | no | **yes** (stands for persons owed) | no | **yes** | **Personal** | Credit |
| *Salary A/C* (for contrast) | no | no | **yes** | **no** | **Nominal** | Debit |

Note the last two rows. **"Salary" and "Outstanding Salary" are different types.** One word changes the classification, because one word changes what is on the other side: a *reason* versus a *party owed*.

**Where it bites**

*The word inside the name is not the classification.*

**Wrong:** "Outstanding Salary contains 'Salary'. Salary is Nominal. So Outstanding Salary is Nominal — debit it as an expense."

**Right:** **Outstanding Salary A/C is Personal, and carries a credit balance.** It bites because rote training keys on **the noun**, not on **what the account names**.

| | Salary A/C | Outstanding Salary A/C |
|---|---|---|
| It names | the **cost consumed** this period | the **amount still owed** |
| Other side is | a reason | a party |
| Type | **Nominal** | **Personal** |
| Balance | **Debit** | **Credit** |
| On 30 June it goes to | Income statement | Balance sheet (Liabilities) |

Same for **Insurance A/C** (Nominal, debit) versus **Prepaid Insurance A/C** (Real, debit balance — but on the *balance sheet*, not the income statement).

> **The one-line defence:** never classify by reading the name. Classify by answering **"who or what is on the other side?"** — then confirm with **"is it alive on 1 July?"** Q4 catches everything Q1–Q3 got wrong.

**Your turn**

1. An agency has completed work for a client and has earned Rs 50,000 of commission on it, but the client has not paid yet and is not due to until July. The bookkeeper opens an **Accrued Commission A/C** and, seeing the word "Commission", wants to debit it as an expense and close it into the income statement. Classify the account properly: give the type, the normal balance side and the persistence check. Then state how it is structurally opposite to a supplier's account standing at Rs 2,00,000 credit for machinery bought on credit.

<details><summary>Answer</summary>

**Accrued Commission A/C is Real** — an asset, being a claim to commission already earned. **Normal balance: debit.** Persistence: it **survives** period end, because the money is still receivable on 1 July, so it cannot be Nominal and it goes to the balance sheet, not the income statement. It is the structural opposite of the supplier's Rs 2,00,000 credit: that is a party the business owes; this is an amount owed **to** the business.

</details>

2. A business pays Rs 50,000 of commission during the year for services already rendered, recorded in Commission A/C — a debit balance that closes into the income statement. It also pays a commission in advance for an agent's services covering next year, recorded in a **Prepaid Commission A/C**. Both accounts carry debit balances, so a student closes both into the income statement. Explain why Prepaid Commission A/C carries a debit balance yet does **not** close there, and name the one test that separates the two.

<details><summary>Answer</summary>

Prepaid Commission A/C is a debit balance because it is an **asset**: a claim to a service not yet consumed, which survives period end and goes to the balance sheet. The separating test is the **resource test — after the transaction, do you still control a resource?** Commission A/C: no (consumed → income statement). Prepaid Commission A/C: yes (still owed to you → balance sheet). Sharing a column is not sharing a nature.

</details>

---

# ACT 4 — Not everything is cash. Not everything is a transaction.

## F2 — What qualifies as a business transaction                    [SOURCED p.15]

**Definition**

A **business transaction** is an event that actually **moves something measurable in money** into or out of the business, or that actually **creates or settles an obligation**.

It is **step 1 of journalising**. Before you can ask "which account?" or "debit or credit?", you must ask: **is this even a transaction?** If the answer is no, the other questions never get asked.

Three tests. An event must pass **all three**:

| # | Test | Meaning |
|---|---|---|
| 1 | **Something actually moved, or someone actually became obliged** | Goods, cash, or a resource changed hands — OR a debt was created/settled |
| 2 | **It involves an outside party or an outside effect** | The business's position vs. the world changed |
| 3 | **It can be measured in money** | A definite rupee figure attaches to it |

**Why this node is the whole trap.** Students are trained to journalise. Give them a line with a rupee figure on it and they will produce a debit and a credit reflexively — because that is what the exercise "wants". The workbook's Day 5 exists to punish exactly that reflex.

**The decision tree**

```
                    An event appears on the page
                                |
                                v
              +-----------------------------------+
              | Has anything actually MOVED?      |
              | (cash, goods, machinery, service) |
              +-----------------------------------+
                     |                    |
                    YES                   NO
                     |                    |
                     |                    v
                     |   +-------------------------------------+
                     |   | Has anyone actually become OBLIGED? |
                     |   | (a debt created, or a debt settled) |
                     |   +-------------------------------------+
                     |          |                      |
                     |         YES                     NO
                     |          |                      |
                     v          v                      v
              +--------------------+          +------------------+
              | Can it be measured |          |    NO ENTRY      |
              | in money?          |          | It is an INTENT, |
              +--------------------+          | not an EVENT.    |
                   |          |               +------------------+
                  YES         NO
                   |          |
                   v          v
          +-----------------+ +----------+
          | TRANSACTION     | | NO ENTRY |
          | -> journalise   | +----------+
          +-----------------+
```

**In action**

Run all seven days of the business's first week through the tree:

| Day | Event | Moved? | Obliged? | Verdict |
|---|---|---|---|---|
| 1 | Started business with cash 20,00,000 | Cash in | — | **Transaction** |
| 2 | Purchased goods 4,00,000 | Goods in, cash out | — | **Transaction** |
| 3 | Sold goods 4,60,000 | Goods out, cash in | — | **Transaction** |
| 4 | Purchased machinery from Arjun & Co. 3,00,000 | Machinery in | Debt created | **Transaction** |
| 5 | **Placed an order** with Saksham 3,00,000 | **Nothing** | **Nobody** | **NO ENTRY** |
| 6 | Paid to Arjun & Co. 1,00,000 | Cash out | Debt reduced | **Transaction** |
| 7 | Commission paid 50,000 | Cash out | — | **Transaction** |

**Six transactions. Seven events.** The count does not match, and that mismatch is the lesson.

**Where it bites**

The bite point: **a rupee figure is not proof of a transaction.** Day 5 has a rupee figure. Day 5 is not a transaction.

> **Wrong:** "Day 5 says Rs 3,00,000, so *something* must be recorded. Maybe Purchases A/C Dr. 3,00,000 / To Saksham A/C 3,00,000."
>
> **Right:** Ask test 1 before touching the figure. Nothing arrived from Saksham. Nothing was paid to Saksham. Saksham is not owed a rupee — the goods have not shipped. **NO ENTRY.**

The figure is bait dressed as data. The tree, not the number, decides.

**Your turn**

1. A business phones its machinery supplier, Arjun & Co., and both sides agree that the business will buy a second machine next month for Rs 3,00,000. No machine is delivered, no cash is paid, and neither side can yet demand anything of the other. The business's bookkeeper sees a named supplier and a firm rupee figure and starts writing a journal entry. Run the event through the three tests (something moved or someone became obliged / outside effect / measurable in money) and state the verdict, naming the test it fails.

<details><summary>Answer</summary>

Not a transaction — it fails test 1. Nothing moved and nobody became obliged; an agreed intention to buy next month is still an intention. **NO ENTRY.**

</details>

2. A business owes Arjun & Co. Rs 3,00,000 for machinery delivered earlier. It now pays Arjun & Co. Rs 1,00,000 in cash, and nothing physically arrives at the business in return — no goods, no machinery. Earlier that week the same business had told a different supplier, Saksham, that it wanted Rs 3,00,000 of goods; nothing arrived then either. Explain why the Rs 1,00,000 payment is a transaction while the conversation with Saksham is not.

<details><summary>Answer</summary>

The payment passes test 1 through the "obliged" limb: cash actually moved out and an existing obligation was settled, taking Arjun & Co. from Rs 3,00,000 down to Rs 2,00,000. The Saksham conversation has neither an arrival nor any change to an obligation, because no obligation ever existed. "Nothing arrived" is not the test; arrival-or-obligation is.

</details>

---

## F4 — Capital introduction (Day 1)                    [SOURCED p.15 item 1]

**Definition**

**Capital** is what the **owner supplies** to the business. The business and the owner are treated as **two separate persons** — so when the owner hands over cash, the business has *received* something from an outsider, and it now **owes that outsider**.

That is why capital sits on the **right side**. Capital is a **source**: it answers *where did the resource come from?*

**In action**

Jun 1 — Started business with cash Rs 20,00,000.

| Date | Particulars | L.F | Debit | Credit |
|---|---|---|---|---|
| Jun 1 | Cash A/C **Dr.** | | 20,00,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Capital A/C | | | 20,00,000 |
| | *(Being capital introduced in cash)* | | | |

```
   SOURCE (right)                       USE (left)
   +------------------+                +------------------+
   | Capital          |  ------------> | Cash             |
   | 20,00,000        |   supplied     | 20,00,000        |
   | "the owner       |                | "sitting in the  |
   |  supplied it"    |                |  business now"   |
   +------------------+                +------------------+
```

Two names. **One** Rs 20,00,000. The left says *what the business is holding*. The right says *who it came from*.

**Where it bites**

The bite point: **the owner is not the business.**

> **Wrong:** "It's the owner's own money, so there's nothing to credit — it isn't owed to anyone."
>
> **Right:** The business is its own person. It received Rs 20,00,000 from an outside supplier of funds. Credit Capital A/C 20,00,000. The Capital A/C closes at **20,00,000 credit** and appears on the trial balance credit column at **20,00,000**.

**Your turn**

1. A business is started when its owner hands over Rs 20,00,000 in cash. Over its first month it buys goods for Rs 4,00,000 cash, sells them all for Rs 4,60,000 cash, takes machinery worth Rs 3,00,000 on credit, pays that supplier Rs 1,00,000, and pays Rs 50,000 commission. Cash at month end stands at Rs 19,10,000 and the month's net profit is Rs 10,000. The owner looks at the cash and concludes the business has been wildly profitable. Explain why the cash balance is nowhere near the profit, and name the account that accounts for the gap.

<details><summary>Answer</summary>

Cash of Rs 19,10,000 is high because Rs 20,00,000 was **supplied by the owner, not earned**; profit of Rs 10,000 measures only what was earned. **Capital A/C** is responsible. Profit ≠ cash — neither figure explains the other.

</details>

2. An owner hands over Rs 20,00,000 in cash to start a business, and by month end the business has earned Rs 10,000 of net profit, so its balance sheet carries Capital Rs 20,00,000 plus profit Rs 10,000 = Rs 20,10,000. The owner objects: it is his own money, he owes it to nobody, so the Rs 20,10,000 should not be shown as a claim against the business at all. State which side of the balance sheet the Rs 20,10,000 sits on and justify it in source/use language.

<details><summary>Answer</summary>

The **Liabilities & Equity side (right)**. The business is its own person and received the resources from an outside supplier of funds. Capital is a **source** — it records who supplied the resources — not a use of them.

</details>

---

## F5 — Cash purchase (Day 2) and cash sale (Day 3)                    [SOURCED p.15]

**Definition**

A **cash purchase** is goods in, cash out, **settled on the spot**. A **cash sale** is goods out, cash in, settled on the spot.

The defining feature of both: **no obligation survives the event.** Nobody owes anybody anything the moment it ends. Two accounts move, and the matter is closed.

**In action**

| Date | Particulars | L.F | Debit | Credit |
|---|---|---|---|---|
| Jun 2 | Purchases A/C **Dr.** | | 4,00,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Cash A/C | | | 4,00,000 |
| | *(Being goods purchased for cash)* | | | |
| Jun 3 | Cash A/C **Dr.** | | 4,60,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Sales A/C | | | 4,60,000 |
| | *(Being goods sold for cash)* | | | |

**The three-way contrast — this is the spine of Act 4:**

| | Day 2 cash purchase | Day 4 credit purchase | Day 5 order |
|---|---|---|---|
| Something arrived? | **Yes** — goods | **Yes** — machinery | **No** |
| Cash moved? | **Yes** — 4,00,000 out | **No** | **No** |
| Anyone owed after? | **No** | **Yes** — 3,00,000 to Arjun & Co. | **No** |
| Entry? | **Yes** | **Yes** | **NO ENTRY** |

Cash purchase and credit purchase are **both** transactions and disagree about cash. Credit purchase and order **both** involve no cash and disagree about whether anything happened at all. **Cash movement is not the test. Arrival-or-obligation is the test.**

**Where it bites**

The bite point: **"no cash moved" is not a reason to skip an entry.**

> **Wrong:** "Day 4 has no cash in it, same as Day 5's order — so treat them the same way and skip both."
>
> **Right:** Day 4: machinery arrived and a debt of 3,00,000 was born → **entry**. Day 5: nothing arrived and no debt was born → **NO ENTRY**. The shared feature (no cash) is irrelevant. The deciding feature is arrival-or-obligation.

**Your turn**

1. A business buys goods worth Rs 4,00,000 and hands over Rs 4,00,000 in cash on the spot. Two days later it takes delivery of machinery worth Rs 3,00,000 from Arjun & Co. and pays nothing, payment agreed for later. Both events are purchases, and in both the thing bought is debited — yet one credits Cash A/C Rs 4,00,000 and the other credits Arjun & Co. A/C Rs 3,00,000. State the single question whose answer decides which account gets credited, and apply it to both.

<details><summary>Answer</summary>

**"Was it settled on the spot, or does an obligation survive the event?"** Goods: settled on the spot, nobody is owed → credit **Cash A/C 4,00,000**. Machinery: an obligation survives → credit the supplier, **Arjun & Co. A/C 3,00,000**.

</details>

2. An owner hands over Rs 20,00,000 in cash to start a business, and later that month the business sells goods for Rs 4,60,000 cash. Both events brought cash in and both were recorded as credits — Capital A/C Rs 20,00,000 and Sales A/C Rs 4,60,000. The owner therefore treats the whole Rs 24,60,000 as a measure of how well the business traded. Explain in one sentence each what makes these two sources different.

<details><summary>Answer</summary>

Sales Rs 4,60,000: the cash came from customers and was **earned** by giving up goods — a revenue source. Capital Rs 20,00,000: the cash came from the owner and was **supplied, not earned** — an equity source. Only the first says anything about trading.

</details>

---

## F6 — Credit purchase: "Purchased machinery from Arjun & Co."                    [SOURCED p.15 item 4]

**Definition**

A **credit purchase** is a purchase where the resource **arrives now** and the **payment happens later**. The supplier has handed over a real thing and accepted a **promise** in exchange for it.

Two things happen at the same instant:

- The business **gains a resource** → machinery, an asset → **debit**
- The business **owes the supplier** → a liability → **credit**

The words "**from Arjun & Co.**" are the entire signal. A named counterparty with no mention of cash means: **that party supplied it, and that party is not yet paid.**

**In action**

Jun 4 — Purchased machinery Rs 3,00,000 from Arjun & Co.

| Date | Particulars | L.F | Debit | Credit |
|---|---|---|---|---|
| Jun 4 | Machinery A/C **Dr.** | | 3,00,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Arjun & Co. A/C | | | 3,00,000 |
| | *(Being machinery purchased on credit)* | | | |

```
   SOURCE (right)                       USE (left)
   +------------------+                +------------------+
   | Arjun & Co.      |  ------------> | Machinery        |
   | 3,00,000         |   supplied     | 3,00,000         |
   | WHO gave it      |    the         | WHAT we now hold |
   |                  |   resource     |                  |
   +------------------+                +------------------+

   Cash A/C: untouched. Not one rupee moved on Jun 4.
```

Look at the Cash A/C ledger for June: entries on Jun 1, 2, 3, 6, 7. **Jun 4 is absent.** Cash closes at **19,10,000** and Day 4 contributed nothing to it.

**Where it bites — THE PRIORITY-1 CONFRONTATION**

**The broken model:** *"Liabilities are the things we've spent the money on."*

Day 4 destroys it. Run the broken model against the facts:

| The broken model predicts | Jun 4 actually |
|---|---|
| A liability requires money to have been spent | **Zero cash left the business** |
| No spending → no liability | A liability of **3,00,000** exists |
| The liability *is* the thing bought | The thing bought is **Machinery** — an **asset**, on the **left** |

Under the broken model Jun 4 is **impossible**. It happened anyway. The model is wrong, not the transaction.

> **Wrong:** "Machinery is a liability — we bought it, we owe for it, so it's the thing we owe."
>
> **Right:** Machinery is the **USE** — the resource the business now controls, sitting on the **debit** side. Arjun & Co. is the **SOURCE** — the party who supplied it and has not been paid, sitting on the **credit** side. They are **two different accounts** carrying the **same** Rs 3,00,000 for two different reasons.

**The correction, stated flat:**

```
   Liabilities are NEVER "what we bought."
   Liabilities are ALWAYS "who supplied it and hasn't been paid."

   USE   -> left  -> what the resource IS      -> Machinery 3,00,000
   SOURCE-> right -> where it CAME FROM        -> Arjun & Co. 3,00,000
```

Confirm against Stage 5: at Jun 30 **Machinery 3,00,000 sits under Assets**; **Arjun & Co. 2,00,000 sits under Liabilities**. They are on **opposite sides of the balance sheet**. If liabilities were the things bought, they would be on the same side. They are not.

**Your turn**

1. A business takes delivery of machinery worth Rs 3,00,000 from Arjun & Co. and pays nothing that day — payment is agreed for later. Not one rupee leaves the business, and the entry recording the delivery has no Cash A/C line on it at all. The owner argues that since no money has been spent, the business cannot owe anything yet. Using the source/use split, explain why a liability of Rs 3,00,000 exists even though no cash moved.

<details><summary>Answer</summary>

Cash records only the **USE** side of a resource's arrival. The machinery arrived from a **SOURCE** — Arjun & Co. — that has not been paid, and the liability records that source. It therefore exists whether or not cash moved; cash appears only later, when the debt is settled. Liabilities are never "what we spent money on"; they are "who supplied it and hasn't been paid."

</details>

2. A business takes machinery worth Rs 3,00,000 from Arjun & Co. on credit and later pays Arjun & Co. Rs 1,00,000. At month end its balance sheet shows Machinery Rs 3,00,000 under Assets and Arjun & Co. Rs 2,00,000 under Liabilities. Both figures trace back to the same delivery, yet they sit on opposite sides and are no longer even the same amount. Explain what each side is actually reporting.

<details><summary>Answer</summary>

The **Assets** side reports the **USE**: the resource the business now controls — Machinery Rs 3,00,000. The **Liabilities** side reports the **SOURCE**: the unpaid party who supplied it — Arjun & Co. Rs 2,00,000, reduced by the Rs 1,00,000 paid. Two different accounts, two different facts about the same delivery.

</details>

---

## F7 — The order that is not a transaction                    [SOURCED p.15 item 5]

**Definition**

Jun 5 — *"Placed an order for buying goods Rs 3,00,000 with Saksham."*

**NO ENTRY.**

An order is a **statement of intention**. The business has said what it plans to do. Saying it changes nothing:

| Question | Jun 5 answer |
|---|---|
| Was anything **received**? | No — the goods are still Saksham's |
| Was anything **given**? | No — no cash, no goods left the business |
| Is anything **owed**? | No — Saksham cannot demand payment for goods not shipped |
| Was anything **paid**? | No |

Four no's. **An intention is not an event.** Nobody owes anybody anything until goods ship or money moves.

**The bait — read this carefully**

| | Day 4 | Day 5 |
|---|---|---|
| Wording | "Purchased machinery **from Arjun & Co.**" | "Placed an order for buying goods **with Saksham**" |
| Amount | **Rs 3,00,000** | **Rs 3,00,000** |
| Named counterparty | **Yes** — Arjun & Co. | **Yes** — Saksham |
| Cash mentioned | **No** | **No** |
| Position in list | item 4 | item 5 — **the very next line** |
| **Verdict** | **Transaction** | **NO ENTRY** |

**Same amount. Same shape. Same absence of cash. A named party on both. Opposite treatment.**

That mirroring is **not a coincidence**. The workbook chose Rs 3,00,000 twice and placed the two lines two apart. Day 5 is engineered to look exactly like the credit purchase that IS a transaction — and then the workbook's solution page (p.16) is **blank**, so the trap is never sprung for you. It is sprung on you, in the exam.

**The side-by-side — the sharpest discrimination in the topic**

```
  DAY 4                              |  DAY 5
  "Purchased machinery from          |  "Placed an order for buying goods
   Arjun & Co.  Rs 3,00,000"         |   Rs 3,00,000 with Saksham"
  -----------------------------------|-----------------------------------
  Machinery ARRIVED  --> yes         |  Goods arrived      --> NO
  Debt created       --> yes         |  Debt created       --> NO
  Cash moved         --> no          |  Cash moved         --> no
  -----------------------------------|-----------------------------------
  Machinery A/C Dr.       3,00,000   |
       To Arjun & Co. A/C  3,00,000  |          NO ENTRY
  -----------------------------------|-----------------------------------
  Arjun & Co. now a CREDITOR         |  Saksham is NOBODY in these books.
  Appears in the ledger,             |  No ledger account. No trial
  the trial balance, the             |  balance line. Not on the
  balance sheet.                     |  balance sheet. Zero footprint.
```

**The one test that separates them:** *has anything actually moved, or has anyone actually become obliged?* Day 4 → yes (machinery moved, obligation born). Day 5 → **neither**.

**In action — where Day 5's absence shows up**

Because Jun 5 produces no entry, Rs 3,00,000 for Saksham appears **nowhere**:

| Statement | Saksham's Rs 3,00,000 |
|---|---|
| Journal (Stage 1) | Absent — Jun 5 line reads **NO ENTRY**, debit **—**, credit **—** |
| Ledger (Stage 2) | No Saksham A/C exists at all |
| Trial balance (Stage 3) | Absent — TB totals **26,60,000** each side without it |
| Balance sheet (Stage 5) | Absent — totals **22,10,000** each side without it |

The journal totals **28,10,000 = 28,10,000** with Jun 5 contributing **zero to both columns**.

**Where it bites**

The bite point: **the word "order" is the whole tell, and a rupee figure beside it is camouflage.**

> **Wrong:** "Purchases A/C Dr. 3,00,000 / To Saksham A/C 3,00,000 — it's a credit purchase from a named party, same as Day 4."
>
> **Right:** Nothing was received from Saksham. Saksham is owed nothing — goods not shipped, no obligation exists. **NO ENTRY.** Arjun & Co. earned a ledger account by *delivering a machine*. Saksham delivered nothing and gets nothing.

A second bite, subtler:

> **Wrong:** "Fine — no entry, but the trial balance must be short by 3,00,000 somewhere."
>
> **Right:** A non-transaction leaves **no hole**. The TB balances at **26,60,000** both sides. There is nothing missing, because there was never anything there.

**Your turn**

1. In the same week a business does two things. It takes delivery of machinery worth Rs 3,00,000 from Arjun & Co. and pays nothing, payment agreed for later. It also places an order with Saksham for goods worth Rs 3,00,000; Saksham accepts the order, but nothing has been shipped and no money has changed hands. Both involve a named supplier, the identical figure of Rs 3,00,000, and no cash. State how each should be recorded, giving the accounts and amounts where an entry is required, and give the one question that decides each case.

<details><summary>Answer</summary>

Arjun & Co.: **Machinery A/C Dr. 3,00,000 / To Arjun & Co. A/C 3,00,000.** Saksham: **NO ENTRY.** The deciding question is *"has anything actually moved, or has anyone actually become obliged?"* — machinery arrived and a debt was born; from Saksham nothing arrived and no debt exists, because goods not shipped cannot be demanded payment for.

</details>

2. A business places an order with Saksham for goods worth Rs 3,00,000. Nothing ships, nothing is paid, and no entry is made. Three days later Saksham delivers the goods and the business has still not paid. The bookkeeper now worries that because the Rs 3,00,000 order was never recorded, the trial balance drawn up before the delivery must have been short by Rs 3,00,000. State what changed between the order and the delivery that turns a non-event into a transaction, name the two accounts affected, and say whether that earlier trial balance was ever short.

<details><summary>Answer</summary>

On delivery the goods actually arrived **and** Saksham became owed — arrival plus obligation, both absent when only an order existed. Accounts: **Purchases A/C Dr. 3,00,000 / To Saksham A/C 3,00,000.** The earlier trial balance was **not** short by a rupee: a non-transaction leaves no hole, because there was never anything there to omit.

</details>

---

## F8 — Settling a creditor: "Paid Rs 1,00,000 to Arjun & Co."                    [SOURCED p.15 item 6]

**Definition**

Settling a creditor is **paying off an obligation that already exists**. Nothing new arrives. The business does not gain a resource on Jun 6 — it **gives up cash** to **shrink a debt**.

**This node cannot be understood without F6.** Jun 6 is only meaningful because Jun 4 created the liability it reduces. No Day 4 → no Arjun & Co. A/C → nothing for Day 6 to touch.

- **Debit Arjun & Co. A/C** — the liability gets smaller. A liability lives on the credit side; debiting it pulls it down.
- **Credit Cash A/C** — cash leaves.

**In action**

Jun 6 — Paid Rs 1,00,000 to Arjun & Co.

| Date | Particulars | L.F | Debit | Credit |
|---|---|---|---|---|
| Jun 6 | Arjun & Co. A/C **Dr.** | | 1,00,000 | |
| | &nbsp;&nbsp;&nbsp;&nbsp;To Cash A/C | | | 1,00,000 |
| | *(Being part payment to Arjun & Co.)* | | | |

**The Arjun & Co. A/C — the whole life of one liability:**

| Date | Particulars | J.F | Amount | Date | Particulars | J.F | Amount |
|---|---|---|---|---|---|---|---|
| Jun 6 | To Cash | | 1,00,000 | Jun 4 | By Machinery | | 3,00,000 |
| Jun 30 | **To Balance c/d** | | **2,00,000** | | | | |
| | | | **3,00,000** | | | | **3,00,000** |

**Closing: 2,00,000 credit. Still owed.**

```
   Jun 4  liability born      ---------> 3,00,000 credit
   Jun 6  part payment        ---------> 1,00,000 debit
                                         -------------------
   Jun 30 still owed                     2,00,000 CREDIT
```

**Why the ledger exists, in one line.** *"How much do we still owe Arjun & Co.?"* The journal has the answer split across two dates (Jun 4 and Jun 6) on two different pages. The ledger answers it in one place: **2,00,000**. That figure carries straight to the trial balance credit column and to the balance sheet under Liabilities.

**Where it bites**

The bite point: **"paid" does not automatically mean "expense".**

> **Wrong:** "Cash went out on Jun 6, so it's a cost — treat it like the commission on Jun 7."
>
> **Right:** Compare the two payments directly:
>
> | | Jun 6 — Arjun & Co. 1,00,000 | Jun 7 — Commission 50,000 |
> |---|---|---|
> | Cash out? | Yes | Yes |
> | Debit goes to | **Arjun & Co. A/C** (a liability) | **Commission A/C** (an expense) |
> | Effect on net profit | **None** | **Reduces it** |
> | Why | A debt shrank | A service was consumed |
>
> Net profit for June is **10,000** — Sales 4,60,000, less purchases 4,00,000, less commission 50,000. The Rs 1,00,000 paid to Arjun & Co. **is not in that calculation anywhere**, because paying a debt is not a cost. It is a swap: less cash, less debt.

A second bite:

> **Wrong:** "Arjun & Co. was debited on Jun 6, so it's a debit balance — an asset."
>
> **Right:** Read the ledger, not the last entry. Credit 3,00,000, debit 1,00,000 → **net 2,00,000 credit**. Still a **liability**. A single debit does not flip an account's nature; the **balance** decides.

**Your turn**

1. A business owes Arjun & Co. Rs 3,00,000 for machinery delivered earlier on credit. During the month it pays Arjun & Co. Rs 1,00,000 in cash, and separately pays Rs 50,000 in cash as commission for a service it receives and uses up on the spot. Its sales for the month were Rs 4,60,000 and the goods sold had cost Rs 4,00,000, and its net profit is Rs 10,000. Both payments took cash out, and the owner expects both to have hurt profit — yet only one of them is inside that Rs 10,000. Explain which, and why.

<details><summary>Answer</summary>

Only the **commission Rs 50,000** is in the Rs 10,000. It bought a service that was consumed with nothing left to control → an **expense**, so it reduces profit. The Rs 1,00,000 to Arjun & Co. settled an **existing debt** → less cash, less liability, an asset/liability swap with **no effect on profit**. Paying a debt is not a cost.

</details>

2. Arjun & Co. delivers machinery worth Rs 3,00,000 to a business on credit; the business later pays Arjun & Co. Rs 1,00,000 in cash. Arjun & Co.'s account has therefore been debited with Rs 1,00,000, and a colleague argues that since the most recent entry against Arjun & Co. is a debit, the account now carries a debit balance and belongs on the asset side. Give the two journal entries that produced the account's closing balance, state that balance, and say what it means in plain words.

<details><summary>Answer</summary>

**Machinery A/C Dr. 3,00,000 / To Arjun & Co. A/C 3,00,000**, then **Arjun & Co. A/C Dr. 1,00,000 / To Cash A/C 1,00,000**. Closing balance: **Rs 2,00,000 credit** — the business still owes Arjun & Co. Rs 2,00,000. A single debit does not flip an account's nature; the balance decides, and this one is still a liability.

</details>

---

## F10 — Purchases A/C vs the asset bought                    [EXT — not in your workbook]

**Definition**

Day 2 bought goods. Day 4 bought machinery. **Both were "bought."** They go to completely different accounts, and the reason has nothing to do with price, size, or cash.

| | **Purchases A/C** | **Machinery A/C** |
|---|---|---|
| What it holds | Goods **for resale** | A resource the business **keeps and uses** |
| Its destiny | Sold on to customers, then gone | Stays, operates the business |
| Do you still control it after? | **No** — you sold it | **Yes** — it's still yours |
| Nature | **Expense** (cost of goods sold) | **Asset** |
| Lands on | **Income statement** | **Balance sheet** |

**Why the name.** "Purchases" is a **trading** word, not a general shopping word. In accounting it means **only** goods bought for resale. Machinery is bought, but it is never a "purchase" in this technical sense — the business is not in the business of selling machines.

**The test — one question:**

```
              You bought something. Which account?
                             |
                             v
        +--------------------------------------------+
        | Is this destined to be SOLD to customers?  |
        +--------------------------------------------+
              |                                |
             YES                              NO
              |                                |
              v                                v
     +-----------------+          +--------------------------+
     | PURCHASES A/C   |          | Do you still control a   |
     | Goods for       |          | resource afterward?      |
     | resale.         |          +--------------------------+
     | EXPENSE.        |             |                  |
     | -> Income stmt  |            YES                 NO
     +-----------------+             |                  |
                                     v                  v
                            +----------------+  +----------------+
                            | ASSET A/C      |  | EXPENSE A/C    |
                            | e.g. Machinery |  | e.g. Commission|
                            | -> Balance sht |  | -> Income stmt |
                            +----------------+  +----------------+
```

**In action**

| Day | Bought | Account debited | Amount | Why |
|---|---|---|---|---|
| 2 | Goods | **Purchases A/C** | 4,00,000 | For resale — and indeed sold on Jun 3 for 4,60,000 |
| 4 | Machinery | **Machinery A/C** | 3,00,000 | Kept and used — still owned on Jun 30 |
| 7 | Commission (a service) | **Commission A/C** | 50,000 | Consumed on receipt — nothing left to control |

**Follow each one to its destination:**

```
  Purchases 4,00,000 ---> INCOME STATEMENT
      Sales                4,60,000
      Less: COGS (Purchases)(4,00,000)
      Gross Profit            60,000
      Less: Commission       (50,000)
      NET PROFIT              10,000

  Machinery 3,00,000 ---> BALANCE SHEET (Assets)
      Cash                19,10,000
      Machinery            3,00,000
      TOTAL               22,10,000

  Machinery is ABSENT from the income statement.
  It wasn't consumed. It was ACQUIRED.
```

> **`[INFERRED]` — say this out loud.** The workbook gives **no closing stock**, so this income statement assumes **all goods purchased were sold**. That is why Purchases 4,00,000 is used as cost of goods sold outright. Real businesses almost never look like this.

**Where it bites**

The bite point: **both were bought, both cost lakhs — and the similarity is completely irrelevant.**

> **Wrong:** "Machinery A/C Dr. 3,00,000 → Purchases A/C Dr. 3,00,000. It's a purchase, isn't it? We purchased it."
>
> **Right:** Purchases A/C is **only** goods for resale. Route machinery there and it becomes cost of goods sold: gross profit collapses from 60,000, net profit turns into a loss, and machinery disappears from the balance sheet — the business would be reporting that it does not own a machine it is standing next to.

A second bite:

> **Wrong:** "Machinery 3,00,000 is bigger, so surely it hits profit harder than commission 50,000."
>
> **Right:** Machinery hits profit by **zero**. Commission 50,000 hits it in full. **Size is not the test.** *Do you still control a resource afterward?* Machinery: yes → asset, equity unmoved, asset swap. Commission: no → expense, equity down.

**Your turn**

1. A business buys goods for Rs 4,00,000 cash and sells all of them for Rs 4,60,000 cash. It also acquires machinery for Rs 3,00,000 on credit, which it keeps and runs the business with, and it pays Rs 50,000 commission. Recorded correctly, gross profit is Rs 60,000 and net profit is Rs 10,000, with Machinery Rs 3,00,000 sitting under Assets. The bookkeeper reasons that the machinery was "purchased" too, and debits its Rs 3,00,000 to Purchases A/C instead of Machinery A/C. State what happens to gross profit, to net profit, and to the asset side of the balance sheet.

<details><summary>Answer</summary>

Cost of goods sold becomes Rs 7,00,000 against sales of Rs 4,60,000, so the Rs 60,000 gross profit turns into a gross **loss**; after the Rs 50,000 commission the Rs 10,000 net profit becomes a **loss** too. Machinery Rs 3,00,000 **vanishes from Assets** — the business reports that it does not own a machine it is standing next to.

</details>

2. In one week a business buys goods for Rs 4,00,000, which it sells on to customers days later, and machinery for Rs 3,00,000, which it keeps and uses. Both were bought, both cost lakhs, and both were settled with suppliers. The owner assumes the bigger one must hit profit harder. Give the single question that separates the two, apply it to each, and name the statement each ends up on.

<details><summary>Answer</summary>

**"Is it destined to be sold to customers — and do you still control a resource afterward?"** Goods: destined for resale, sold on, no longer controlled → **Purchases A/C**, an expense → **income statement**. Machinery: kept and used, still controlled → **Machinery A/C**, an asset → **balance sheet**, hitting profit by zero. Size is not the test.

</details>

---

## A14 — Debtor vs Creditor                    [SOURCED p.4 item 8]

**Definition**

Two words, one direction of arrow. Get the arrow wrong and every liability question goes wrong with it.

| | **Debtor** | **Creditor** |
|---|---|---|
| Who is it | Someone who **owes the firm** | Someone the **firm owes** |
| Money will | **Come in** | **Go out** |
| To the firm it is an | **Asset** | **Liability** |
| Balance in their A/C | **Debit** | **Credit** |
| Balance sheet side | **Assets** | **Liabilities** |
| Typically arises from | A **credit sale** | A **credit purchase** |

**Where the names come from.** Both are named **from the firm's point of view**, and this is where students lose it.

- **Debtor** — the firm's books carry a **debit** balance against them. They owe the firm.
- **Creditor** — the firm's books carry a **credit** balance against them. The firm owes them.

The label describes **which side of the firm's own ledger** the party sits on. It is not about who is generous or who is trustworthy.

```
        MONEY OWED TO THE FIRM              MONEY OWED BY THE FIRM
                  |                                   |
                  v                                   v
        +-------------------+               +-------------------+
        |     DEBTOR        |               |    CREDITOR       |
        |  DEBIT balance    |               |  CREDIT balance   |
        |  -> ASSET         |               |  -> LIABILITY     |
        |  cash will COME IN|               |  cash will GO OUT |
        +-------------------+               +-------------------+
                  |                                   |
                  |          THE FIRM                 |
                  +----------> [ ] <-----------------+
                    owes us          we owe
```

**In action**

**Arjun & Co. is a creditor.** Trace it:

| Step | Evidence |
|---|---|
| Jun 4 | Machinery arrived from Arjun & Co., unpaid → **credit** Arjun & Co. A/C 3,00,000 |
| Jun 6 | Part payment → **debit** Arjun & Co. A/C 1,00,000 |
| Jun 30 ledger | Closing balance **2,00,000 credit** — still owed |
| Trial balance | Arjun & Co. A/C sits in the **credit** column at **2,00,000** |
| Balance sheet | Arjun & Co. (creditor) **2,00,000** under **Liabilities & Equity** |

**Every stage agrees.** The credit balance in the ledger is the same fact as the liability on the balance sheet.

**This business has no debtors.** Look at Jun 3: "Sold goods 4,60,000" → **Cash A/C Dr. / To Sales A/C**. Cash came in immediately. Nobody was left owing the firm. Had it been a credit sale, a debtor would exist and would sit on the **Assets** side. It was not, so none does.

**Where it bites**

The bite point: **the words are named from the firm's side, and a payment is not a reversal.**

> **Wrong:** "Arjun & Co. gave us credit, so Arjun & Co. is a debtor — they're the one who did the lending."
>
> **Right:** Read the arrow, not the favour. Arjun & Co. is owed **2,00,000 by the firm** → money will go **out** → **creditor** → **liability**. The fact that they extended credit is exactly *why* they are a creditor, not a debtor.

A second bite, straight into the Priority-1 gap:

> **Wrong:** "Arjun & Co. is a liability, and the liability is the machine we got from them."
>
> **Right:** The machine is **Machinery A/C 3,00,000 — an asset, left side.** Arjun & Co. is **2,00,000 — a liability, right side.** They are not even the same number any more, because Jun 6's payment shrank one and left the other untouched. A liability is a **person or party owed**, never an object owned. If the liability were the machine, the Jun 6 payment of 1,00,000 would have shrunk the machine. It did not — Machinery A/C still closes at **3,00,000**.

**Your turn**

1. Arjun & Co. delivers machinery worth Rs 3,00,000 to a business on credit. The business later pays Arjun & Co. Rs 1,00,000, which drops Arjun & Co.'s account from Rs 3,00,000 to Rs 2,00,000 — while Machinery A/C still stands at Rs 3,00,000 and the business still has the whole machine, unchanged. The owner insists the liability simply *is* the machine they got from Arjun & Co. Use the divergence between the Rs 2,00,000 and the Rs 3,00,000 to show why that cannot be true.

<details><summary>Answer</summary>

The payment reduced the **party owed** but not the **object owned**. If the liability were the machine, paying Rs 1,00,000 would have shrunk the machine — instead Machinery A/C still closes at Rs 3,00,000 while Arjun & Co. fell to Rs 2,00,000. A liability tracks the unpaid **source**, never the resource owned.

</details>

2. A business sells goods for Rs 4,60,000. The customer takes the goods away but pays nothing at the time, promising to pay next month. Because the customer was kind enough to buy on those terms, a clerk wants to treat them the same way as a supplier who extended credit to the business. Name the customer's classification from the business's point of view, the side of their account that carries the Rs 4,60,000 balance, and the balance sheet side on which they appear.

<details><summary>Answer</summary>

The customer is a **debtor**; their account carries a **debit** balance of Rs 4,60,000; they appear on the **Assets** side of the balance sheet. Money will come **in**, which is the opposite direction from a supplier the business owes.

</details>

---

# ACT 4b — One book or two? And the events you have not seen.

## D11 — Single entry vs double entry `[SOURCED p.11]`

**Definition**

**Single-entry** means recording each event **once** — usually just the cash movement, in one list.
It is what a notebook does. Money in, money out.

**Double-entry** records every event **twice** — once as the resource, once as its source.

Your workbook raises this on p.11 with two yes/no items and never resolves either:

- *"The double-entry system provides a more comprehensive financial picture than the single-entry system."*
- *"Only businesses with complex financial transactions use the double-entry system."*

**Why single entry fails** — it can only ever see one side, so it can only ever answer one question.
A cash notebook for June would show:

- Money in: 20,00,000 + 4,60,000
- Money out: 4,00,000 + 1,00,000 + 50,000
- **Left over: 19,10,000**

**That is the whole picture single entry can produce.** It is correct — and useless.

**What it cannot tell you:**

- **That Rs 2,00,000 is still owed to Arjun & Co.** No cash moved on Jun 4, so a cash notebook has no
  row for it. **The debt is invisible.**
- **That Rs 3,00,000 of machinery exists.** It went out as cash and never came back as anything.
- **That the owner supplied 20,00,000 and the business earned 10,000.** Both are just "money in."
- **Whether the books are even right.** Nothing to cross-check against.

**In action**

| Question | Single entry | Double entry |
|---|---|---|
| How much cash? | **19,10,000** ✓ | 19,10,000 ✓ |
| What do we owe? | **cannot see it** | Arjun & Co. **2,00,000** |
| What do we own besides cash? | **cannot see it** | Machinery **3,00,000** |
| Did we get richer? | **cannot answer** | Net profit **10,000** |
| Are the books internally consistent? | **no way to check** | TB balances at **26,60,000** |

- **Situation:** the same seven June events, recorded two ways.
- **Action:** ask each system the four questions a business actually needs answered.
- **Result:** single entry answers one of five. Double entry answers all five.
- **Principle:** **a system that records one side can only report one side.** The second entry isn't
  duplication — it's the source, and the source is where every question except "how much cash" lives.

**Where it bites**

The workbook's second item — *"Only businesses with complex financial transactions use the
double-entry system"* — invites the wrong instinct.

- **Wrong:** double-entry is heavy machinery for complicated businesses; a simple one can skip it.
- **Right:** **complexity is not the trigger. Owing and owning are.**

**The exact point it bites:** the word "complex." A business with **seven** transactions already
needs it — this one does. The moment anything is bought on credit, or any resource outlives the
moment it was paid for, single entry goes blind. That happened on **Day 4 of week one**.

A fruit cart that buys for cash and sells for cash, owning nothing and owing nothing, genuinely can
run on a notebook. **That is a business with no liabilities and no assets** — not a simple business,
a *degenerate* one.

**Your turn**

1. A business keeps one cash notebook and nothing else. For June it records money in of **Rs
20,00,000** (put in by the owner) and **Rs 4,60,000** (goods sold), and money out of **Rs 4,00,000**
(goods bought), **Rs 1,00,000** (part-paid to a machinery supplier) and **Rs 50,000** (commission),
closing at **Rs 19,10,000**. The owner sees the healthy closing balance and concludes the month went
well. A full double-entry set of the same events would additionally show that the machinery, worth
**Rs 3,00,000**, was taken on credit and that **Rs 2,00,000** of its price is still owed. Identify the
**two** facts the notebook structurally cannot show, and state which of the two matters more if that
supplier demands payment tomorrow.

<details><summary>Answer</summary>

**(i)** The **Rs 2,00,000 still owed** to the supplier, and **(ii)** the **Rs 3,00,000 of machinery**
the business holds. Neither has a cash row of its own, so a notebook has nowhere to put them. **The
debt matters more** if payment is demanded tomorrow: an unseen obligation is a **solvency risk** that
can end the business, whereas an unseen asset merely understates its wealth.

</details>

2. A business places an order for goods worth **Rs 3,00,000** with a supplier — nothing has shipped,
nothing is owed, no cash has moved. Neither its cash notebook nor a full double-entry set of books
records the order anywhere. In the same week the business takes delivery of machinery worth **Rs
3,00,000** on credit, where again no cash moves — and there the two systems part company. Explain why
the order's absence is a **correct result** in one system and a **coincidence** in the other.

<details><summary>Answer</summary>

In **double entry** the absence is correct **on principle**: nothing was received, given, owed or
paid, so the order fails the transaction test and is refused deliberately. In **single entry** it is a
**coincidence**: the notebook omits it only because no cash moved — it applies no test at all. The
proof is the machinery: no cash moved there either, and the same blindness silently loses a real Rs
3,00,000 asset and a real Rs 2,00,000 debt. Right answer, wrong reason, and the reason is what fails
next time.

</details>

---

## F9 — Paying an expense `[SOURCED p.15 item 7]`

**Definition**

An **expense** is a resource **consumed to earn revenue.** Money goes out and **nothing you control
comes back.**

Day 7: commission paid, Rs 50,000. Compare it against Day 4's machinery — same direction of cash,
opposite consequence:

| | Day 4 — Machinery 3,00,000 | Day 7 — Commission 50,000 |
|---|---|---|
| Cash | unaffected (bought on credit) | **out 50,000** |
| Afterwards you hold | **a machine** | **nothing** |
| Account type | **Real** | **Nominal** |
| Effect on equity | **none** — asset swap | **down 50,000** |
| Appears in | Balance Sheet | **Income Statement** |

**Why "nominal":** the commission account exists **in name only.** There is no commission sitting
anywhere. It is a label for value that passed through and was consumed.

**In action**

```
Jun 7   Commission A/C   Dr.        50,000
             To Cash A/C                        50,000
        (Being commission paid)
```

**Read it through the equation, not the rule:**

- Commission is an **expense** → expenses **shrink equity** → equity lives on the **right** → so its
  reduction sits on the **left** → **debit.**
- Cash left → cash is an asset → assets live left → a decrease is **credit.**

**The golden rule** — *debit all expenses and losses* — gives the same answer. **It is the shortcut,
not the reason.**

**Where the 50,000 lands:**

- Income Statement: gross profit **60,000** − commission **50,000** = net profit **10,000**
- **That single Rs 50,000 consumes 83% of the month's gross profit.**
- Balance Sheet: **nowhere.** There is nothing left to show.

- **Situation:** Rs 50,000 leaves the business on Day 7.
- **Action:** booked to a nominal account, not an asset account.
- **Result:** June's profit falls from 60,000 to 10,000.
- **Principle:** **expenses are equity dying in public.** They exist as a line precisely because they
  reduce the owner's stake and someone must see why.

**Where it bites**

- **Wrong:** Rs 50,000 of cash left, so record an asset of Rs 50,000 — value was exchanged, after all.
- **Right:** **Commission A/C Dr.** — an expense. Nothing was acquired.

**The exact point it bites:** *"I paid for something, so I must own something."* **Paying is not
acquiring.** The test is not whether money moved — money moved on Day 2, Day 6 and Day 7, with three
different results. The test is: **do you still control a resource afterward?**

- Day 2 — paid 4,00,000 → held **goods** (asset, until sold)
- Day 6 — paid 1,00,000 → held **nothing new**, but a **debt shrank** (2,00,000 remains)
- Day 7 — paid 50,000 → held **nothing**, and **equity fell**

**Three payments. Three different treatments. Cash tells you none of it.**

**Your turn**

1. A business owes a supplier **Rs 3,00,000** for machinery delivered on credit. On 6 June it pays
**Rs 1,00,000** off that debt, leaving **Rs 2,00,000** outstanding. On 7 June it pays an agent **Rs
50,000** of commission. Both payments sent cash out of the door; after each one the business holds
nothing new it can point to. Yet only one of them reduced the owner's equity. Identify which, and
state the feature of the *other* payment that spared equity.

<details><summary>Answer</summary>

The **commission** reduced equity — value was consumed and nothing came back. The **1,00,000 spared
equity because it settled a liability**: assets fell by 1,00,000 and the right side fell by the same
1,00,000 as the supplier's claim shrank from 3,00,000 to 2,00,000. The owner's stake was never
touched; only the creditor's claim got smaller.

</details>

2. A business's income statement for June shows gross profit **Rs 60,000** less commission **Rs
50,000**, giving net profit **Rs 10,000**; the commission was paid in cash on 7 June and cash closed
at **Rs 19,10,000**. Now suppose the commission had been **incurred in June but still unpaid** at 30
June. Name the two accounts the entry touches instead, and state whether June's net profit changes.

<details><summary>Answer</summary>

**Commission A/C Dr. / To Outstanding Commission A/C** — the credit goes to a **liability**, not to
cash. **Net profit is unchanged at Rs 10,000**: the expense belongs to the period that incurred it,
whether or not it was paid in that period. What changes is cash, which would close at **Rs 19,60,000**
instead, with a Rs 50,000 liability sitting on the balance sheet against it.

</details>

---

## F11 — Journalising a set the workbook never gives you `[EXT — not in your workbook]`

**Definition**

Every worked example so far runs on the same seven events. **That is the weakness.** Recognising
Day 5 as a non-transaction because you have seen Day 5 before is **recall**, not skill.

This node is the transfer test: **the same four steps (F1), applied to events you have never seen.**

**The four steps, from p.15 — the only thing you carry across:**

1. Is it a **business transaction**? (If no → **stop. No entry.**)
2. Identify **both** accounts.
3. Find their **nature**, and the rule — or derive the side from **A = L + E**.
4. Pass the entry. **Debit first**, credit indented, narration underneath.

**Why the workbook cannot test this**

- Its solution page (**p.16**) is **blank.**
- Its seven transactions are the **only** set it provides.
- **There is nothing to transfer to.** A student can master p.15 completely and still be unable to
  journalise anything else — and the workbook has no way to detect that.

**In action** — a set the workbook does not contain, run through the four steps:

| # | Event | Step 1: transaction? | Entry |
|---|---|---|---|
| 1 | Goods sold on credit to a customer | **Yes** — they owe you now | Debtor A/C **Dr.** / To Sales A/C |
| 2 | Hired an employee at Rs 40,000/month | **NO** — an agreement. Nothing received, given, owed or paid | **no entry** |
| 3 | Rent paid for the office | **Yes** | Rent A/C **Dr.** / To Cash A/C |
| 4 | Owner takes cash for personal use | **Yes** | Drawings A/C **Dr.** / To Cash A/C |
| 5 | Received a quotation from a supplier | **NO** — a piece of paper | **no entry** |
| 6 | Machinery bought, paid by cheque | **Yes** | Machinery A/C **Dr.** / To **Bank** A/C |

**Note #6:** Bank A/C, not Cash A/C. **Bank is a Personal account** — Cash is Real. The workbook lists
Bank A/C on p.13 and never says which it is.

**Note #2 and #5:** two non-transactions the workbook never shows you — **because it only ever shows
you one.** Hiring and quoting fail the same test the Saksham order fails: an intention is not an
event. If you learned "orders are the trick," you learned the example, not the rule.

- **Situation:** six events, none from your material.
- **Action:** the four steps applied without a memorised answer key.
- **Result:** four entries, two refusals.
- **Principle:** **the skill is the steps, not the seven events.** If step 1 has to be *remembered*
  rather than *asked*, it will fail on the first unfamiliar page.

**Where it bites**

- **Wrong:** six events, so six entries. Work through them in order and produce a full page.
- **Right:** **four entries and two refusals.**

**The exact point it bites:** the assumption that **a listed event is an event.** Every question set
you will ever meet lists things — and listing is not the same as happening. Step 1 exists to be
**asked every single time**, including the times the answer is obviously yes. The moment it becomes
automatic, the first hiring or quotation on the page becomes a journal entry that should not exist.

**The tell:** if the number of entries equals the number of lines in the question, **check again.**

**Your turn**

1. A printing business does three things in three consecutive weeks. **(a)** It places an order with a
manufacturer for a binding machine costing **Rs 5,00,000**; nothing arrives and nothing is paid.
**(b)** Three weeks later the machine is delivered and installed, with payment due next month. **(c)**
The following week the business pays the manufacturer **Rs 2,00,000** towards it. Journalise all
three. State how many entries the three events produce, and name the account left carrying a balance
and on which side.

<details><summary>Answer</summary>

**Two entries** from three events. **(a) No entry** — an order; nothing received, given, owed or paid.
**(b)** Machinery A/C **Dr.** 5,00,000 / To Creditor A/C 5,00,000. **(c)** Creditor A/C **Dr.**
2,00,000 / To Cash A/C 2,00,000. The **Creditor A/C** is left carrying **Rs 3,00,000 on the credit
side** — still owed.

</details>

2. A tailoring business receives **Rs 1,00,000** from a customer **in advance** for suits it has not
yet cut, let alone delivered. The money is in the bank. The first test passes — something was
genuinely received, so this is a transaction, unlike a mere order. Name both accounts in the entry,
and state why the credit is **not** Sales.

<details><summary>Answer</summary>

**Cash A/C Dr. / To Advance from Customer A/C** — the credit is a **liability**. It is not Sales
because **nothing has been delivered**, so no revenue has been earned; booking it as a sale would
anticipate a gain, which the rule against anticipating gains forbids. The business owes the customer
**goods**, and that obligation is what the credit records.

</details>

---

# ACT 5 — Your journal cannot answer the question.

## E3 — Ledger                     [SOURCED p.8 — but the definition there is circular and useless]

**What your workbook says**

> *"Ledger is the secondary book of accounts. Ledger is one where accounts are kept."* — p.8

**That definition cannot be used.** It says a ledger is where accounts are kept, and accounts are the
things kept in a ledger. It is a circle. If you read that and understood nothing, you read it
correctly — there was nothing there to understand.

Here is the definition that works.

**Definition**

A **ledger** is the book that re-files every journal entry **by account instead of by date**.

- **What it is** — one page (an "account") per thing the business tracks: Cash, Capital, Machinery,
  Arjun & Co., and so on. Every journal line about Cash is copied onto the Cash page.
- **Why it exists** — the journal is sorted by **time**, and **time-order cannot total**. Read the
  reason below; it is the whole point of this act.
- **Posting** — the name for the copying step. Journal → ledger. `[SOURCED p.8]`
- **"Secondary book"** — secondary means *second in order*, not *less important*. Nothing new enters
  it. It is a re-sort of facts the journal already holds.

---

**The question the journal cannot answer**

Two questions, same books:

| Question | Journal | Why |
|---|---|---|
| *"What happened on June 4th?"* | **Answers instantly** | It's in date order. Flip to Jun 4. |
| *"How much do we still owe Arjun & Co.?"* | **Cannot answer** | The fact is split across two pages. |

Trace the second one through the journal:

```
   JOURNAL (sorted by DATE)
   ┌──────────────────────────────────────────────┐
   │ Jun 1  Cash        Dr.  20,00,000            │
   │          To Capital          20,00,000       │
   │ Jun 2  Purchases   Dr.   4,00,000            │
   │          To Cash              4,00,000       │
   │ Jun 3  Cash        Dr.   4,60,000            │
   │          To Sales             4,60,000       │
   │ Jun 4  Machinery   Dr.   3,00,000            │  ← mention #1 of Arjun & Co.
   │          To Arjun & Co.       3,00,000       │     owed 3,00,000
   │ Jun 5  NO ENTRY               —              │
   │ Jun 6  Arjun & Co. Dr.   1,00,000            │  ← mention #2, two pages later
   │          To Cash              1,00,000       │     paid 1,00,000
   │ Jun 7  Commission  Dr.     50,000            │
   │          To Cash                50,000       │
   └──────────────────────────────────────────────┘
```

- The Rs 3,00,000 owed and the Rs 1,00,000 paid are **nowhere near each other**.
- To answer, you must read **every page**, spot **every** mention, and subtract by hand.
- **After 7 transactions that is annoying. After 7,000 it is impossible.**

**The ledger answers it in one line: Rs 2,00,000.**

---

**Where the names come from — they encode the whole difference**

| Book | Name from | Meaning |
|---|---|---|
| **Journal** | French *jour* = day `[SOURCED p.8]` | The **day** book. You carry it. Written as things happen. |
| **Ledger** | Dutch *legger* = something that **lies** | The book that **stays put** on the shelf. Permanent. Sorted. |

**One is a diary. One is an index.** A diary tells you what happened when. An index tells you where
everything about one subject is. You cannot total a diary.

---

**Posting = re-filing, not recording**

```
        JOURNAL                              LEDGER
     (sorted by DATE)                   (sorted by ACCOUNT)

   Jun 1  Cash / Capital ────────┬───────► CASH A/C
   Jun 2  Purchases / Cash ──────┤         Jun 1 To Capital   20,00,000
   Jun 3  Cash / Sales ──────────┤         Jun 3 To Sales      4,60,000
   Jun 4  Machinery / Arjun ─┐   │         Jun 2 By Purchases  4,00,000
   Jun 6  Arjun / Cash ──────┤───┤         Jun 6 By Arjun      1,00,000
   Jun 7  Commission / Cash ─│───┘         Jun 7 By Commission   50,000
                             │
                             └───────────► ARJUN & CO. A/C
                                           Jun 6 To Cash       1,00,000
                                           Jun 4 By Machinery  3,00,000
                                           ─────────────────────────────
                                           Owed:               2,00,000

   SAME FACTS. DIFFERENT SORT ORDER. NOTHING NEW ADDED.
```

**Read the arrows.** The Jun 6 entry goes to **two** ledger accounts — Cash and Arjun & Co. Every
journal entry lands in exactly two places, because every entry had two accounts in it.

---

**In action**

The Cash A/C in the ledger, built by re-filing five journal lines that were spread across five dates:

| Date | Particulars | J.F | Amount | Date | Particulars | J.F | Amount |
|---|---|---|---|---|---|---|---|
| Jun 1 | To Capital | | 20,00,000 | Jun 2 | By Purchases | | 4,00,000 |
| Jun 3 | To Sales | | 4,60,000 | Jun 6 | By Arjun & Co. | | 1,00,000 |
| | | | | Jun 7 | By Commission | | 50,000 |
| | | | | Jun 30 | **By Balance c/d** | | **19,10,000** |
| | | | **24,60,000** | | | | **24,60,000** |

**Closing: Rs 19,10,000 debit.**

- Cash was mentioned on Jun 1, 2, 3, 6 and 7 — **five separate journal pages**.
- One ledger page collects all five and produces **one number**.
- That number is the answer to *"how much cash do we have?"* — a question the journal holds the
  ingredients for but cannot cook.

---

**Where it bites**

**The confusion:** *"If the ledger has the same facts, why write it twice? Isn't it just copying?"*

Solve this: **how much does the business still owe Arjun & Co. on Jun 30?**

- **Wrong:** *"Rs 3,00,000 — that's the Arjun figure, I saw it on Jun 4."*
- **Wrong:** *"Rs 1,00,000 — that's the Arjun figure, I saw it on Jun 6."*
- **Right:** **Rs 2,00,000.**

**The exact point it bites:** the journal never puts those two figures on the same page, so whichever
one you saw last **looks like the answer**. Both are true facts and **neither is the answer.** The
answer is a *relationship* between them, and a relationship only becomes visible when the two facts
sit side by side. Sorting by date guarantees they never do.

**So the ledger is not copying. It is the only step that makes the answer physically visible.**

---

**Your turn**

1. A business records its first week in a journal, written strictly in date order: on 1 June the owner
   put in Rs 20,00,000 cash; on 2 June it bought goods for cash Rs 4,00,000; on 3 June it sold goods
   for cash Rs 4,60,000; on 6 June it paid Rs 1,00,000 cash to a machinery supplier; on 7 June it paid
   commission Rs 50,000 cash. On 30 June the owner asks a single question: *"How much cash do we have
   right now?"* The journal contains every fact needed and still cannot say. Name the book that
   answers in one line, the account inside it, the figure, and state how many separate journal entries
   someone would have to hunt down and combine by hand to reach that same figure without it.

<details><summary>Answer</summary>

The ledger, in the Cash A/C: **Rs 19,10,000 debit.** By hand you would have to find and combine
**five** separate journal entries (1, 2, 3, 6 and 7 June) — the ledger's re-sort by account puts all
five on one page and produces the one number the date-ordered journal never shows.

</details>

2. On 4 June a business bought machinery on credit for Rs 3,00,000 from a supplier, Arjun & Co. On
   5 June it placed an order with a different supplier, Saksham, for goods worth Rs 3,00,000 — the
   goods have not arrived, nothing has been paid, and nothing is yet owed. A student writing up the
   ledger argues that since the ledger is a fresh sort of everything the business has been doing, it
   should open a Saksham A/C page for that Rs 3,00,000. Is there a Saksham A/C? Justify your answer
   from what a ledger is allowed to contain.

<details><summary>Answer</summary>

**No.** The 5 June order produced **no journal entry** — nothing was received, given, owed or paid.
The ledger only re-files what the journal already holds; it adds no fact of its own, so an event the
journal never recorded can have no ledger page.

</details>

---

## E4 — Ledger format (the T-account)                     [EXT — not in your workbook]

**Say this plainly, because it is a fact about your document and not about you:**

- p.9 asks you to **"Draw the Format of a Ledger."**
- **The workbook never shows that format. Not on p.9, not anywhere in its 20 pages.**
- You were asked to reproduce a diagram you were never given.

That is a gap in the material. Here is the format.

---

**Definition**

A **T-account** is the standard shape of one ledger account: a **title**, and **two columns**
underneath it, separated by a vertical line.

- **Left column = debit side.**
- **Right column = credit side.**
- Each side carries four sub-columns: **Date · Particulars · J.F · Amount**.
- The name comes from the shape — title on top, line down the middle. It looks like the letter **T**.

---

**Why the format looks like this**

The shape is forced by the job. Work forward from the job and the T draws itself.

1. **An account is a QUESTION.** Cash A/C asks: *"how much cash do we have?"*
2. **To answer it you need two opposite things:** everything that **increased** cash, and everything
   that **decreased** it.
3. **Two opposite forces need two columns.** One force per side, or they cancel each other before you
   can see them.
4. **Left is debit, right is credit** — because that mirrors **A = L + E**'s own shape. Assets on the
   left, sources on the right. The ledger does not invent a new convention; it inherits the equation's.
5. **The T is just two columns with a line between them.** There is nothing else to it.

**And the sub-columns each have a job:**

| Sub-column | Job | Why you can't drop it |
|---|---|---|
| **Date** | When it happened | Ties the line back to a day |
| **Particulars** | Names the **OTHER** account | The pointer back to the cause — see *Where it bites* |
| **J.F** | **Journal Folio** — the journal page number | The **link**. Any figure traces to the entry that created it. |
| **Amount** | The figure | The thing being totalled |

**J.F is not decoration.** It is why a balance is auditable: pick any line in any account, read its
J.F, flip to that journal page, and you are standing on the original entry.

---

**The format**

```
                              CASH  A/C
        (Debit side — Dr.)      │      (Credit side — Cr.)
  ──────┬─────────────┬─────┬───┼───┬──────┬─────────────┬─────┬──────────
  Date  │ Particulars │ J.F │ Amt   │ Date │ Particulars │ J.F │ Amt
  ──────┼─────────────┼─────┼───┼───┼──────┼─────────────┼─────┼──────────
        │ To ______   │     │       │      │ By ______   │     │
        │ To ______   │     │       │      │ By ______   │     │
        │             │     │       │      │ By Bal. c/d │     │
  ──────┴─────────────┴─────┴───┼───┴──────┴─────────────┴─────┴──────────
                 TOTAL          │              TOTAL   (both equal)
```

**As a table — this is the version to reproduce on paper:**

| Date | Particulars | J.F | Amount | Date | Particulars | J.F | Amount |
|---|---|---|---|---|---|---|---|
| | To ______ | | | | By ______ | | |
| | | | **Total** | | | | **Total** |

**Two rules the format enforces:**

- **To / By convention** — **"To"** prefixes every entry on the **debit** side; **"By"** prefixes
  every entry on the **credit** side. They carry no meaning beyond *which side am I on* — they are
  labels, and they exist so a line read aloud tells you its side without you counting columns.
- **Balance c/d** — "**carried down**". The closing figure. It is **inserted on the smaller side** so
  that both sides total the same. **This is the answer the account was built to produce.**

---

**In action**

**Arjun & Co. A/C** — every column doing its job at once:

| Date | Particulars | J.F | Amount | Date | Particulars | J.F | Amount |
|---|---|---|---|---|---|---|---|
| Jun 6 | To Cash | | 1,00,000 | Jun 4 | By Machinery | | 3,00,000 |
| Jun 30 | **To Balance c/d** | | **2,00,000** | | | | |
| | | | **3,00,000** | | | | **3,00,000** |

**Closing: Rs 2,00,000 credit. (Still owed.)**

**Walk it line by line:**

- **Jun 4, credit side, "By Machinery", 3,00,000** — the business took on a Rs 3,00,000 debt. The
  Particulars says *Machinery* because that is **the other account in the Jun 4 entry**.
- **Jun 6, debit side, "To Cash", 1,00,000** — Rs 1,00,000 paid off. Particulars says *Cash* because
  Cash is **the other account in the Jun 6 entry**.
- **Credit side totals 3,00,000. Debit side has only 1,00,000.** Gap = Rs 2,00,000.
- **Jun 30, "To Balance c/d", 2,00,000** — the gap, written into the **smaller (debit) side**.
- **Now both sides read 3,00,000.** The account is closed, and the figure you had to insert to close
  it **is the answer**: Rs 2,00,000 still owed.

**Read the shape:** the balance goes on the side that was *short*, so the closing balance itself
belongs to the **opposite** side. Here c/d sat on the debit side → **the balance is a credit balance**
→ a liability → money owed out. The format told you the *type* as well as the amount.

---

**Where it bites**

**The Particulars column names the OTHER account in the entry — never itself.**

Post this journal entry into **Cash A/C**:

```
   Jun 1   Cash A/C   Dr.   20,00,000
              To Capital A/C     20,00,000
```

| | Particulars written in Cash A/C |
|---|---|
| **Wrong:** | `To Cash — 20,00,000` |
| **Right:** | `To Capital — 20,00,000` |

**The exact point it bites:** the entry starts with the word *Cash*, so your hand writes *Cash*.

**Why it is wrong:**

- **The account is already labelled at the top.** The page says **CASH A/C**. Writing *Cash* inside it
  tells you nothing you didn't know from the title.
- **Particulars is a pointer to the other side of the entry.** It is the one column that says *where
  did this come from / where did this go*.
- **It is what lets you walk backwards from a balance to its cause.** `To Capital` means: this
  Rs 20,00,000 arrived **from the owner**. Written `To Cash`, the trail is dead — you have a figure
  with no origin.

**The check that never fails:** every journal entry names **two** accounts. You are standing in one of
them. **Particulars gets the other one.**

Apply it to the Jun 6 entry (`Arjun & Co. Dr. 1,00,000 / To Cash 1,00,000`) — the same fact, written
twice, from two different pages:

| Standing in | Side | Particulars | Reads as |
|---|---|---|---|
| **Cash A/C** | Credit | `By Arjun & Co.` | 1,00,000 left cash → **went to Arjun & Co.** |
| **Arjun & Co. A/C** | Debit | `To Cash` | 1,00,000 reduced the debt → **came from Cash** |

**Each page points at the other. Neither points at itself.** That is the whole discipline.

---

**Your turn**

1. On 4 June a business bought machinery for Rs 3,00,000 on credit from a supplier, Arjun & Co. That
   one transaction is written into two ledger pages. In **Arjun & Co. A/C** the 4 June line sits on
   the credit side and reads `By Machinery — 3,00,000`. Write the line the **same transaction**
   produces in **Machinery A/C**: give the date, the side, the exact Particulars text, and the amount
   — then say what the Particulars text you wrote tells a reader that the account's own title does not.

<details><summary>Answer</summary>

**Jun 4 | debit side | `To Arjun & Co.` | 3,00,000.** The title already says *Machinery*; the
Particulars names the **other** account in the entry, so it tells the reader the machinery arrived
**from Arjun & Co.** — i.e. on credit, not for cash. Writing `To Machinery` would say nothing and
kill the trail back to the cause.

</details>

2. An owner put Rs 20,00,000 cash into a business on 1 June and nothing else touched capital all
   month, so **Capital A/C** holds one entry — 1 June, credit side, `By Cash — 20,00,000`. On 30 June
   the account is closed by writing `To Balance c/d — 20,00,000` on the **debit** side. A student
   objects twice: first that the Particulars should read *"To Capital"* because this is the Capital
   page, and second that the closing balance must be a debit balance because that is the side c/d was
   written on. Answer both objections.

<details><summary>Answer</summary>

Both are wrong. *"To Capital"* breaks the rule that Particulars names the **other** account — and
`Balance c/d` is not an account at all, it is the closing figure itself, which is why it is the one
permitted exception. The closing balance is a **credit balance of Rs 20,00,000**: c/d is inserted on
the **smaller (debit) side** purely to force both totals to Rs 20,00,000, so the balance belongs to
the **opposite** side — a credit balance, meaning a source of funds owed back to the owner.

</details>

---

## E9 — Journal → Ledger → Trial Balance, as one chain                     [SOURCED p.8]

**Definition**

The three books are **not three topics**. They are **one pipeline**, and each stage exists only
because the stage before it cannot do the next job.

| Stage | Sorted by | Answers | Cannot answer |
|---|---|---|---|
| **Journal** | **Date** | *What happened on Jun 4?* | *What's the Cash total?* |
| **Ledger** | **Account** | *How much cash? How much owed?* | *Do the books hang together?* |
| **Trial Balance** | **Balances, in one list** | *Do Σ debits = Σ credits?* | *Are the entries correct?* |

**Each stage is a re-sort of the one before. No new facts enter after the journal.**

---

**Why the format looks like this**

The chain has a shape because each handoff **throws information away on purpose**.

- **Journal → Ledger** drops date-order, keeps every movement. You gain totals per account.
- **Ledger → Trial Balance** drops every individual movement, keeps only the closing balance. You gain
  one flat list you can add up.

**Each step narrows.** That is not loss — the J.F column means every narrowed figure still points
back to the wide version.

---

**The format**

```
   ┌──────────────┐  post   ┌──────────────┐  balance  ┌──────────────┐
   │   JOURNAL    │────────►│    LEDGER    │──────────►│    TRIAL     │
   │              │  (J.F   │              │   c/d     │   BALANCE    │
   │  by DATE     │   links │  by ACCOUNT  │           │  one list    │
   │              │   back) │              │           │              │
   │ every entry, │         │ 7 accounts,  │           │ 7 balances,  │
   │ in time      │         │ each totalled│           │ Dr vs Cr     │
   └──────────────┘         └──────────────┘           └──────────────┘
      28,10,000                19,10,000 cash             26,60,000
      (MOVEMENTS)              2,00,000 owed              (BALANCES)
                                   ...
        ◄──────────── J.F walks you back ────────────►
```

---

**In action**

Follow **one figure** all the way down the chain — the Rs 19,10,000 in the trial balance.

**Stage 3 — Trial Balance says:**

| Account | L.F | Debit | Credit |
|---|---|---|---|
| Cash A/C | | 19,10,000 | |
| Purchases A/C | | 4,00,000 | |
| Machinery A/C | | 3,00,000 | |
| Commission A/C | | 50,000 | |
| Capital A/C | | | 20,00,000 |
| Sales A/C | | | 4,60,000 |
| Arjun & Co. A/C | | | 2,00,000 |
| **TOTAL** | | **26,60,000** | **26,60,000** |

**Walk backwards one stage — the ledger says where 19,10,000 came from:**

| Date | Particulars | J.F | Amount | Date | Particulars | J.F | Amount |
|---|---|---|---|---|---|---|---|
| Jun 1 | To Capital | | 20,00,000 | Jun 2 | By Purchases | | 4,00,000 |
| Jun 3 | To Sales | | 4,60,000 | Jun 6 | By Arjun & Co. | | 1,00,000 |
| | | | | Jun 7 | By Commission | | 50,000 |
| | | | | Jun 30 | **By Balance c/d** | | **19,10,000** |
| | | | **24,60,000** | | | | **24,60,000** |

**Walk backwards one more stage — the journal says what caused each of those five lines:**

- Jun 1 → capital introduced in cash
- Jun 2 → goods purchased for cash
- Jun 3 → goods sold for cash
- Jun 6 → part payment to Arjun & Co.
- Jun 7 → commission paid

**One trial-balance figure → five ledger lines → five journal entries.** The J.F column is the rail
that walk runs on. Without it the chain is three unrelated tables.

---

**Where it bites**

**The confusion:** *"The journal totals Rs 28,10,000 but the trial balance totals Rs 26,60,000. One of
them must be wrong."*

- **Wrong:** *"The totals disagree, so I've made an arithmetic mistake — go back and re-add."*
- **Right:** **Both are correct. They are not measuring the same thing.**

| Book | Totals | Cash appears |
|---|---|---|
| **Journal — 28,10,000** | **MOVEMENTS** — every single time money moved | **5 times** (Jun 1, 2, 3, 6, 7) |
| **Trial Balance — 26,60,000** | **BALANCES** — where each account ended up | **once** (19,10,000) |

**The exact point it bites:** both totals balance, both are labelled "total", and they sit two pages
apart — so they *look* like the same check done twice. They are not.

- The journal counts Cash **five times**, once per movement, gross.
- The ledger collapses those five into **one closing balance**.
- The trial balance carries that **one** figure forward.
- **The difference is exactly the movements that cancelled themselves out inside the accounts.**

**Expect this as an exam question.** The answer is one sentence: *the journal totals movements, the
trial balance totals balances.*

**And the limit of the chain:** the trial balance only ever checks **Σ debits = Σ credits**. It checks
the *arithmetic* of the chain, never the *truth* of it. A balanced trial balance proves the posting
was even-handed. **It proves nothing about whether the entries were right.**

---

**Your turn**

1. A business's first month runs like this: 1 June, owner puts in Rs 20,00,000 cash; 2 June, goods
   bought for cash Rs 4,00,000; 3 June, goods sold for cash Rs 4,60,000; 4 June, machinery bought on
   credit Rs 3,00,000; 6 June, Rs 1,00,000 cash paid to that supplier; 7 June, commission paid
   Rs 50,000 cash. The journal totals **Rs 28,10,000** on each side. The trial balance at 30 June
   totals **Rs 26,60,000** on each side. Both are internally balanced. The owner insists Rs 1,50,000
   has gone missing and orders the books re-added. Name the single account most responsible for the
   difference, state how many times it appears in each of the two books and why the count differs, and
   say whether the owner is right.

<details><summary>Answer</summary>

The owner is **wrong — nothing is missing and neither book needs re-adding.** The account is **Cash**:
it appears **five times** in the journal (1, 2, 3, 6 and 7 June — once per movement, gross) but
**once** in the trial balance, as its closing balance of Rs 19,10,000. The journal totals
**movements**; the trial balance totals **balances**. The gap is exactly the movements that cancelled
out inside the accounts.

</details>

2. A business bought machinery on credit for Rs 3,00,000 from a supplier, Arjun & Co., on 4 June, then
   paid that supplier Rs 1,00,000 in cash on 6 June. Its trial balance at 30 June shows **Rs 2,00,000**
   against Arjun & Co. The owner searches the journal, finds Rs 3,00,000 and Rs 1,00,000 but no
   Rs 2,00,000 anywhere in it, and concludes the trial balance has invented a figure. Walk the
   Rs 2,00,000 backwards through the chain: name the ledger account it came from, the journal entries
   (dates, sides and amounts) that produced it, and the column that makes that backward walk possible
   — then say why the figure is absent from the journal.

<details><summary>Answer</summary>

It came from **Arjun & Co. A/C**, whose two lines are 4 June credit `By Machinery — 3,00,000` and
6 June debit `To Cash — 1,00,000`; the **J.F (Journal Folio)** column is the rail that walks any
figure back to the entry that made it. Nothing was invented: the journal records only **movements**,
so Rs 2,00,000 — a **balance**, the relationship between the two movements — exists only once the
ledger sorts them onto one page.

</details>

---

# ACT 6 — Did we slip? Would we know?

## E5 — Trial balance                     [SOURCED p.8]

**Definition**

A **trial balance** is a list of the **balances of the ledger accounts**, set out in two money columns — Debit and Credit — and totalled.

- **What it is** — not a new book, not a new calculation. A **copy-out**. Every ledger account has already been closed and has one closing balance. The trial balance collects those balances onto one page.
- **Why it exists** — the ledger has grown to seven separate accounts on seven separate pages. Nobody can look at seven pages at once and see whether the debits still equal the credits. The trial balance puts all seven on one line each.
- **Where the name comes from** — a **trial**. A test run. You are putting the books *on trial* before you trust them enough to build statements on top.
- **The logic under it** — every transaction was entered with equal debits and credits (Act 2). So if the copy-out is faithful, the two columns must total the same.

**Why the format looks like this**

The shape is forced by the job.

- The job is **compare two totals**. So there must be exactly **two money columns**, side by side, never mixed.
- The job is **check, then trace back**. So each row must name its account and carry a **ledger folio (L.F)** — the page number to jump to when a figure looks wrong.
- The job is **one balance per account**. So each account gets **one row**, never two. Cash appears once here even though it was touched five times in the journal.

**The format**

```
              TRIAL BALANCE as at 30 June 2024
   +------------------+-------+-------------+-------------+
   | Account          | L.F   |   Debit     |   Credit    |
   +------------------+-------+-------------+-------------+
   | one account      | page  | Rs, if the  | Rs, if the  |
   | per row          | ref   | balance is  | balance is  |
   |                  |       | a debit     | a credit    |
   +------------------+-------+-------------+-------------+
   | TOTAL            |       |  MUST EQUAL --->  EQUAL   |
   +------------------+-------+-------------+-------------+
```

**In action**

Seven ledger accounts closed in Stage 2. Seven rows. Each balance goes in the column it already sits in.

| Account | L.F | Debit | Credit |
|---|---|---|---|
| Cash A/C | | 19,10,000 | |
| Purchases A/C | | 4,00,000 | |
| Machinery A/C | | 3,00,000 | |
| Commission A/C | | 50,000 | |
| Capital A/C | | | 20,00,000 |
| Sales A/C | | | 4,60,000 |
| Arjun & Co. A/C | | | 2,00,000 |
| **TOTAL** | | **26,60,000** | **26,60,000** |

**Balanced.**

**Where it bites**

The bite is at **which total you are quoting**. The journal also totalled — and it totalled to a different number.

- **Wrong:** "The books total Rs 28,10,000, so the trial balance total is Rs 28,10,000."
- **Right:** The journal totals **28,10,000**. The trial balance totals **26,60,000**. Both are correct.

**The exact point it bites:** the journal totals **movements**, the trial balance totals **balances**.

```
   JOURNAL              LEDGER                TRIAL BALANCE
   Cash appears     ->  Cash account      ->  Cash appears
   5 times              nets the 5 down       ONCE
   (20,00,000 +         to one figure         19,10,000
    4,60,000 in;
    4,00,000 +
    1,00,000 +
    50,000 out)
   -------------------------------------------------------
   Total 28,10,000                            Total 26,60,000
   MOVEMENTS                                  BALANCES
```

**Your turn**

1. A business has just finished its first month of trading. Its bookkeeper has seven ledger accounts written across seven separate pages, each already closed off to a single closing balance:

   | Ledger account | Closing balance |
   |---|---|
   | Cash A/C | 19,10,000 debit |
   | Purchases A/C | 4,00,000 debit |
   | Machinery A/C | 3,00,000 debit |
   | Commission A/C | 50,000 debit |
   | Capital A/C | 20,00,000 credit |
   | Sales A/C | 4,60,000 credit |
   | Arjun & Co. A/C (supplier) | 2,00,000 credit |

   The Cash page alone holds five separate entries — cash came in twice and went out three times. The owner objects: *"Every one of those figures is already written in the ledger. Why copy them onto yet another page?"* Answer the owner by stating what job the new page does that seven ledger pages cannot do. Then state whether, looking only at the finished Cash row of Rs 19,10,000 on that page, you could tell how many times cash moved during the month — and if not, which book you would have to open.

<details><summary>Answer</summary>

The new page is a trial balance: it collects all seven closing balances onto one sheet, one row each, in two columns, so the two columns can be added and compared — nobody can check Σ debits = Σ credits while the figures sit on seven separate pages. It is a copy-out and a test, not a new calculation. No, the number of cash movements cannot be recovered from the Rs 19,10,000 row — that is a single closing *balance*, not a count of movements. You would have to open the ledger's Cash A/C, which shows the five entries individually.

</details>

2. A business's first month produced these journal entries, each with a debit and an equal credit: capital introduced in cash Rs 20,00,000; goods bought for cash Rs 4,00,000; goods sold for cash Rs 4,60,000; machinery bought on credit Rs 3,00,000; part payment to the supplier Rs 1,00,000; commission paid Rs 50,000. Totalled, the journal's Debit column comes to **Rs 28,10,000**. The trial balance built from the same books is:

   | Account | L.F | Debit | Credit |
   |---|---|---|---|
   | Cash A/C | | 19,10,000 | |
   | Purchases A/C | | 4,00,000 | |
   | Machinery A/C | | 3,00,000 | |
   | Commission A/C | | 50,000 | |
   | Capital A/C | | | 20,00,000 |
   | Sales A/C | | | 4,60,000 |
   | Arjun & Co. A/C | | | 2,00,000 |
   | **TOTAL** | | **26,60,000** | **26,60,000** |

   A junior compares Rs 28,10,000 against Rs 26,60,000, finds a Rs 1,50,000 gap, and reports an error to the owner. Decide whether an error exists, and account for the Rs 1,50,000 using the Cash account specifically.

<details><summary>Answer</summary>

No error exists, and the gap is Cash. The journal totals **movements** — Cash is written there five times (20,00,000 and 4,60,000 in; 4,00,000, 1,00,000 and 50,000 out). The trial balance totals **balances** — Cash appears once, at its closing figure of Rs 19,10,000. Rs 28,10,000 and Rs 26,60,000 are both correct; they are answers to different questions, and only Rs 26,60,000 is the trial balance total.

</details>

---

## E6 — Two methods: total method and balance method                     [SOURCED p.8]

**Definition**

There are **two** legal ways to build a trial balance out of the same ledger. They give different numbers and both are correct.

- **Total method** — go to each ledger account, total its debit side, total its credit side, and carry **both totals** to the trial balance. The account's balance is never worked out at all.
- **Balance method** — go to each ledger account, work out its **closing balance** (one side minus the other), and carry **only that one figure**. Each account contributes exactly one number to one column.
- **Why two exist** — the total method is a rawer check: it catches an error inside the totalling of a ledger account, because it re-adds every line. The balance method is shorter and gives you the figures you actually need next, since the closing balances are what the financial statements are built from.
- **Which is used in practice** — the balance method, almost always. It is the one that feeds forward.

**Why the format looks like this**

The shape is forced by what each method carries out of the ledger.

- **Total method** carries **two figures per account**, so the trial balance is roughly twice as tall in value and every account writes in **both** columns.
- **Balance method** carries **one figure per account**, so each account writes in **exactly one** column and the page stays short.

**The format**

```
   Cash A/C in the ledger
   +-----------------------+-----------------------+
   | Dr side               | Cr side               |
   | 20,00,000             | 4,00,000              |
   |  4,60,000             | 1,00,000              |
   |                       |   50,000              |
   |                       | Bal c/d 19,10,000     |
   | total 24,60,000       | total 24,60,000       |
   +-----------------------+-----------------------+
            |                          |
            |                          |
   TOTAL METHOD                BALANCE METHOD
   carries BOTH side           carries the CLOSING
   totals across               BALANCE only
            |                          |
            v                          v
   Cash  Dr 24,60,000          Cash  Dr 19,10,000
         Cr  5,50,000                (nothing in Cr)
```

**In action**

Stage 3 uses the **balance method**. Every row in it is a closing balance lifted straight from Stage 2:

| Account | Closing balance in the ledger | Trial balance row |
|---|---|---|
| Cash A/C | 19,10,000 debit | Debit 19,10,000 |
| Capital A/C | 20,00,000 credit | Credit 20,00,000 |
| Purchases A/C | 4,00,000 debit | Debit 4,00,000 |
| Sales A/C | 4,60,000 credit | Credit 4,60,000 |
| Machinery A/C | 3,00,000 debit | Debit 3,00,000 |
| Arjun & Co. A/C | 2,00,000 credit | Credit 2,00,000 |
| Commission A/C | 50,000 debit | Debit 50,000 |

**Totals: 26,60,000 = 26,60,000.** That number is a **balance-method** number.

**Where it bites**

The bite is **mixing the two methods in one trial balance — and expecting the totals to catch you.**

- **Wrong:** "If I carry Cash as its side-totals (24,60,000 / 5,50,000, the total method) but carry Arjun & Co. as its closing balance (2,00,000 credit, the balance method), the page won't tally and I'll spot the mistake."
- **Right:** **it tallies perfectly.** Both sides come to **32,10,000**.

```
   MIXED-METHOD PAGE — Cash by total method, everything else by balance method

   Debit                              Credit
   Cash (side total)     24,60,000    Cash (side total)      5,50,000
   Purchases              4,00,000    Capital               20,00,000
   Machinery              3,00,000    Sales                  4,60,000
   Commission               50,000    Arjun & Co.            2,00,000
   ─────────────────────────────      ─────────────────────────────
   TOTAL                 32,10,000    TOTAL                 32,10,000
                                ▲                                  ▲
                                └────────  TALLIES  ───────────────┘
```

**Why it tallies:** the total method **preserves each account's net**. Cash's 24,60,000 − 5,50,000 is still 19,10,000 — the same figure the balance method carries. The two methods disagree about **how much to write down**, never about **what the account is worth**. So the difference between the columns is untouched, and the check passes.

**The exact point it bites:** you cannot detect a mixed-method trial balance from its totals. **They will always agree.**

**What actually gives it away:** an account appearing in **both columns**. Cash sits on the debit side *and* the credit side above — no account's balance can be in two places at once, so that duplication is the tell. **Read the rows, not the total.**

**And the total is now meaningless.** 32,10,000 is not comparable to the 26,60,000 a clean balance-method page produces, nor to next month's. Two methods produce **different totals from identical, correct books** — so a total is only interpretable if you know which method built it.

> **This is E11 arriving early.** A tallying trial balance has just failed to notice something wrong with the page. Hold that thought — the next node is entirely about how much else it cannot see.

**Your turn**

1. A business buys machinery on credit from a supplier, Arjun & Co., for Rs 3,00,000, and later pays Rs 1,00,000 of that off in cash. Its supplier ledger account therefore reads:

   | Arjun & Co. A/C — Dr side | Amount | Cr side | Amount |
   |---|---|---|---|
   | To Cash | 1,00,000 | By Machinery | 3,00,000 |

   State the **two** figures the total method would carry from this account to the trial balance, and the **one** figure the balance method would carry (naming its column). Then state which of those the business would use when it needs to report how much it still owes this supplier, and why.

<details><summary>Answer</summary>

Total method: Debit Rs 1,00,000 **and** Credit Rs 3,00,000 — both side totals, no balance worked out. Balance method: Credit Rs 2,00,000 only. The Rs 2,00,000 credit is the figure the business reports as the amount still owed — the balance method is the one that feeds forward into the financial statements, because a closing balance is what a creditor figure actually is.

</details>

2. In a business's first month, Machinery A/C receives a single entry (Rs 3,00,000 debit, machinery bought on credit), Purchases A/C a single entry (Rs 4,00,000 debit, goods bought), and Sales A/C a single entry (Rs 4,60,000 credit, goods sold). Cash A/C, by contrast, holds five entries: Rs 20,00,000 and Rs 4,60,000 received on the debit side, and Rs 4,00,000, Rs 1,00,000 and Rs 50,000 paid out on the credit side, leaving a closing balance of Rs 19,10,000 debit. An accountant redraws the trial balance using the total method instead of the balance method and finds three rows completely unchanged and the Cash row transformed. Explain why the two methods coincide for Machinery, Purchases and Sales, state the two figures the total method carries for Cash, and state the feature of Cash A/C that makes them diverge.

<details><summary>Answer</summary>

Machinery, Purchases and Sales each have entries on one side only, so the side total **is** the closing balance — there is nothing for the balance method to net off, and the two methods carry the same figure. Cash under the total method carries Debit Rs 24,60,000 and Credit Rs 5,50,000; under the balance method it carries Debit Rs 19,10,000 alone. The diverging feature is that Cash has entries on **both** sides, so its side totals and its balance are different numbers. Neither result is an error — but a trial balance must apply one method to every account, since the two methods legitimately produce different totals from identical, correct books.

</details>

---

## E7 — Purpose: arithmetical accuracy only                     [SOURCED p.8]

**Definition**

The purpose of a trial balance is **to check the arithmetical accuracy of the ledger**. That wording is the whole node, and every word in it is load-bearing.

- **"Arithmetical"** — about **addition**. Did the two columns add to the same number?
- **"Accuracy"** — not truth, not correctness of judgement. Accuracy **of the sums**.
- **"Of the ledger"** — of the copy-out and the balancing. Not of the decision to book something as Purchases rather than Machinery.

**What it therefore is:**

- a check that **Σ debits = Σ credits**
- a statement about **your addition**

**What it therefore is not:**

- a check that the right accounts were used
- a check that every transaction was recorded
- a statement about **your judgement**

**Why the format looks like this**

The shape is forced by how narrow the job is.

- The trial balance has exactly **one output**: do the totals match, yes or no. So the format ends in **one comparison**, not a report.
- It has **no column for "is this the right account?"** — because it was never asked to know that. There is no place on the page to write that judgement, and that absence is the honest signal of what the tool can do.

**The format**

```
        WHAT THE TRIAL BALANCE ACTUALLY ASKS
   +------------------------------------------------+
   |                                                |
   |   Sum of the Debit column                      |
   |             =?                                 |
   |   Sum of the Credit column                     |
   |                                                |
   +------------------------------------------------+
                       |
                       v
              ONE bit of output:
              MATCH  /  NO MATCH

   It never asks:  "is Machinery in the right account?"
                   "did all seven days get recorded?"
                   "did the business make money?"
```

**In action**

The trial balance in Stage 3 reports one thing:

| Question the trial balance answers | Answer |
|---|---|
| Does 19,10,000 + 4,00,000 + 3,00,000 + 50,000 equal 20,00,000 + 4,60,000 + 2,00,000? | **Yes — 26,60,000 both sides.** |

That is the complete output. Not "the books are right." Only "the columns add up."

**Where it bites**

The bite is the workbook's own p.11 question: *"If the trial balance totals do not match, there is definitely an error in the ledger accounts. Yes/No"*.

- **Wrong:** "No — the totals could differ for innocent reasons."
- **Right:** **Yes.** A mismatch is **definite proof of an error**. Every entry was made with equal debits and credits, so equal totals are guaranteed unless something broke.

**The exact point it bites:** the arrow runs **one way only**, and the workbook only ever walks it in the safe direction.

```
   NO MATCH  ===>  there is DEFINITELY an error      (proof)
   MATCH     -/->  the books are correct             (NOT proof)
```

A mismatch proves an error exists. A match proves **nothing about whether an error exists** — see E11.

**Your turn**

1. A business closes its first month of trading and its bookkeeper draws up this trial balance:

   | Account | L.F | Debit | Credit |
   |---|---|---|---|
   | Cash A/C | | 19,10,000 | |
   | Purchases A/C | | 4,00,000 | |
   | Machinery A/C | | 3,00,000 | |
   | Commission A/C | | 50,000 | |
   | Capital A/C | | | 20,00,000 |
   | Sales A/C | | | 4,60,000 |
   | Arjun & Co. A/C | | | 2,00,000 |
   | **TOTAL** | | **26,60,000** | **26,60,000** |

   The owner sees the two totals agree and tells the bank *"the accounts are verified — every transaction is in there and every one is in the right account."* State, in one sentence each, what the agreement has actually proved and what it has not. Then state what a **mismatch** would have proved, and explain why those two answers are not mirror images of each other.

<details><summary>Answer</summary>

Proved: the ledger's arithmetic is accurate — the balances were added and copied out correctly, and Σ debits = Σ credits. Not proved: that the books are true — the owner's claim is unsupported, because omitted transactions and wrong-account postings leave the totals untouched. A mismatch, by contrast, would have been definite proof that an error exists, since every entry was made with equal debits and credits so the totals cannot differ innocently. The arrow runs one way only: no-match proves an error; match proves nothing.

</details>

2. A business buys machinery for Rs 3,00,000 on credit from Arjun & Co. The bookkeeper credits Arjun & Co. Rs 3,00,000 correctly, but debits the Rs 3,00,000 to Purchases A/C rather than Machinery A/C — treating a machine the business still owns as goods it consumed. The month's other balances are Cash Rs 19,10,000 debit, Commission Rs 50,000 debit, Capital Rs 20,00,000 credit and Sales Rs 4,60,000 credit, and Rs 1,00,000 of the supplier's bill was paid in cash. Decide whether the trial balance still totals Rs 26,60,000 on both sides, state what Purchases A/C now reads, and give your reason using the word "arithmetical".

<details><summary>Answer</summary>

Yes — it still totals Rs 26,60,000 on both sides, with Purchases reading Rs 7,00,000 and Machinery A/C absent altogether. Purchases and Machinery are both debit accounts, so the debit column loses Rs 3,00,000 from one row and gains it in another: no arithmetic was broken, and arithmetical accuracy is the only thing the trial balance checks. It has no column for "is this the right account?" (This is an error of principle.)

</details>

---

## E8 — Trial balance format                     [EXT — not in your workbook]

**Definition**

The trial balance has a **fixed four-column shape**: **Account · L.F · Debit · Credit**. The workbook asks you to draw it on p.10 but never shows it once — so this is the drawing, in full.

The four columns, and the job each one does:

- **Account** — the name of the ledger account the balance was copied from. Written exactly as the ledger heads it, including the **A/C** suffix.
- **L.F (Ledger Folio)** — the ledger page number the balance came from. The **audit trail**: it lets a checker jump from a suspect figure straight to the account that produced it.
- **Debit** — the money column for accounts whose closing balance is a **debit**.
- **Credit** — the money column for accounts whose closing balance is a **credit**.

**Why the format looks like this**

The shape is forced by the job.

- The job is **add two columns and compare them** → **two money columns**, kept apart. A figure written in the wrong one throws the totals out by **twice** its value, which is why the columns never merge.
- The job is **find the error when it doesn't tally** → the **L.F column**. Without it you would re-read the whole ledger; with it you jump to the page.
- The job is **one balance per account** → **one row per account**. An account never occupies two rows.
- The job is **finished by a comparison** → the last row is always **TOTAL**, and it is always **double-ruled**.

**The format**

```
             TRIAL BALANCE as at [DATE]
   +-------------------+------+--------------+--------------+
   | Account           | L.F  |    Debit     |    Credit    |
   |                   |      |     Rs       |      Rs      |
   +-------------------+------+--------------+--------------+
   |                   |      |              |              |
   |  debit-balance    |  p.  |    XX,XXX    |              |
   |  accounts         |      |              |              |
   |                   |      |              |              |
   |  credit-balance   |  p.  |              |    XX,XXX    |
   |  accounts         |      |              |              |
   |                   |      |              |              |
   +-------------------+------+--------------+--------------+
   |  TOTAL            |      |  ==XX,XXX==  |  ==XX,XXX==  |
   +-------------------+------+--------------+--------------+
                                     |              |
                                     +----- = ------+
                                    these MUST agree
```

Heading rules:

| Line | Content | Why |
|---|---|---|
| 1 | Trial Balance | names the statement |
| 2 | **as at [date]** | a trial balance is an **instant**, not a period — "as at", never "for the year ended" |

**In action**

The Stage 3 trial balance, drawn into the four columns exactly:

| Account | L.F | Debit | Credit |
|---|---|---|---|
| Cash A/C | | 19,10,000 | |
| Purchases A/C | | 4,00,000 | |
| Machinery A/C | | 3,00,000 | |
| Commission A/C | | 50,000 | |
| Capital A/C | | | 20,00,000 |
| Sales A/C | | | 4,60,000 |
| Arjun & Co. A/C | | | 2,00,000 |
| **TOTAL** | | **26,60,000** | **26,60,000** |

**As at 30 June 2024.** Debit balances grouped first, credit balances after — a convention, not a rule; the totals do not care about row order.

**Where it bites**

The bite is the **date line**.

- **Wrong:** "Trial Balance **for the period 1–30 June 2024**."
- **Right:** "Trial Balance **as at 30 June 2024**."

**The exact point it bites:** every figure in it is a **closing balance** — a reading taken at one moment. Cash Rs 19,10,000 is not something that happened *during* June; it is what was left standing **on 30 June**. "For the period" describes the income statement, which totals flows across time. The trial balance is a snapshot of stock positions.

Second bite — the **L.F column**:

- **Wrong:** leave L.F out because "we don't have page numbers."
- **Right:** draw the column anyway. It is part of the format. An empty column is a format that survived; a missing column is a format that was never learned.

**Your turn**

1. A business finishes trading on 30 June 2024, its first month. Its closed ledger accounts stand at: Cash Rs 19,10,000 debit, Purchases Rs 4,00,000 debit, Machinery Rs 3,00,000 debit, Commission Rs 50,000 debit, Capital Rs 20,00,000 credit, Sales Rs 4,60,000 credit, and Arjun & Co. (a supplier still owed) Rs 2,00,000 credit. The business has no page numbers on its ledger yet. Draw the trial balance in full — heading line and all four columns — state the two column totals, and justify the wording of your date line by pointing at what the Cash figure of Rs 19,10,000 actually is.

<details><summary>Answer</summary>

Four columns — Account · L.F · Debit · Credit — headed "Trial Balance **as at 30 June 2024**", with the L.F column drawn but left empty (an empty column is part of the format; a missing one is not). Debit balances Cash, Purchases, Machinery, Commission; credit balances Capital, Sales, Arjun & Co. Both totals come to **Rs 26,60,000**, double-ruled. The date line is "as at", never "for the period", because Rs 19,10,000 is not cash that moved *during* June — it is a closing balance, the amount left standing at one instant on 30 June. A trial balance is a snapshot of positions; "for the period" belongs to the income statement, which totals flows.

</details>

2. A business's ledger closes with Cash Rs 19,10,000 debit, Purchases Rs 4,00,000 debit, Machinery Rs 3,00,000 debit, Commission Rs 50,000 debit, Capital Rs 20,00,000 credit, Sales Rs 4,60,000 credit, and Rs 2,00,000 still owed to its supplier Arjun & Co. Copying the balances across, the bookkeeper writes the supplier's Rs 2,00,000 into the Debit column. Every figure is otherwise correct and the ledger itself is sound. Work out both column totals as the trial balance now stands, state the size of the discrepancy, explain why it is not Rs 2,00,000, and name the column of the format you would use to run the figure down.

<details><summary>Answer</summary>

Debit Rs 28,60,000, Credit Rs 24,60,000 — a discrepancy of Rs 4,00,000. It is twice the misplaced balance, not equal to it, because a wrong-column error moves the figure in two directions at once: the debit column gains Rs 2,00,000 that does not belong to it and the credit column loses Rs 2,00,000 that does. Use the **L.F** column to jump straight to Arjun & Co.'s ledger page instead of re-reading the whole ledger.

</details>

---

## E10 — Debit/credit behaviour                     [SOURCED p.10, p.11]

**Definition**

Which column a balance lands in is not a choice. It is fixed by **what kind of account it is**.

- **Assets increase by debit** `[SOURCED p.10]` — Cash, Machinery. Something the business controls.
- **Revenue increases by credit** `[SOURCED p.11]` — Sales. Something earned.
- **Expenses increase by debit** `[SOURCED p.11]` — Commission, Purchases. Something consumed.
- **Capital and liabilities increase by credit** — Capital, Arjun & Co. Something owed, to the owner or an outsider.

**The logic under it:** the left side of the books tracks **where value went** (assets held, value consumed). The right side tracks **where value came from** (the owner, a creditor, a sale). Nothing arrives from nowhere, so the two sides move together.

**Why the format looks like this**

The shape is forced by the job.

- Every account has a **natural side** — the side it increases on. That is the side its closing balance lands on, and so the trial balance column it occupies is **decided before you look at any figure**.
- This makes the trial balance **predictable**: you can name every account's column from its type alone, then check the arithmetic afterwards. Type first, number second.

**The format**

```
   +----------------------------+----------------------------+
   |          DEBIT             |          CREDIT            |
   |  (where value went)        |  (where value came from)   |
   +----------------------------+----------------------------+
   |                            |                            |
   |  ASSETS      increase  ^   |  CAPITAL     increase  ^   |
   |  Cash, Machinery           |  Capital                   |
   |                            |                            |
   |  EXPENSES    increase  ^   |  LIABILITIES increase  ^   |
   |  Purchases, Commission     |  Arjun & Co.               |
   |                            |                            |
   |                            |  REVENUE     increase  ^   |
   |                            |  Sales                     |
   +----------------------------+----------------------------+
```

**In action**

Every row in the Stage 3 trial balance, predicted from type alone:

| Account | Type | Natural side | Trial balance column | Amount |
|---|---|---|---|---|
| Cash A/C | Asset | Debit | Debit | 19,10,000 |
| Machinery A/C | Asset | Debit | Debit | 3,00,000 |
| Purchases A/C | Expense | Debit | Debit | 4,00,000 |
| Commission A/C | Expense | Debit | Debit | 50,000 |
| Capital A/C | Capital | Credit | Credit | 20,00,000 |
| Arjun & Co. A/C | Liability | Credit | Credit | 2,00,000 |
| Sales A/C | Revenue | Credit | Credit | 4,60,000 |

Seven for seven. **No exceptions in this set.**

**Where it bites**

The bite is **Arjun & Co.**, because the account was **debited** on Jun 6 and still ends on the **credit** side.

- **Wrong:** "Arjun & Co. was debited Rs 1,00,000 on Jun 6, so it goes in the trial balance's Debit column."
- **Right:** Arjun & Co. ends with a **credit balance of Rs 2,00,000** and goes in the **Credit** column.

**The exact point it bites:** the trial balance takes the **closing balance**, not the last entry, and not any single entry.

```
   Arjun & Co. A/C
   Dr 1,00,000  |  Cr 3,00,000
                |
        credit side is bigger by 2,00,000
                |
                v
        CLOSING BALANCE = 2,00,000 CREDIT
                |
                v
        Trial balance --> CREDIT column
```

A liability being debited means the debt **shrank**. It shrank from 3,00,000 to 2,00,000. It did not flip sides — Rs 2,00,000 is still owed.

**Your turn**

1. A business buys machinery on credit from a supplier, Arjun & Co., for Rs 3,00,000 — Arjun & Co. credited Rs 3,00,000. Later in the month it pays Rs 1,00,000 of the bill in cash, and Arjun & Co. A/C is **debited** Rs 1,00,000. A junior preparing the trial balance reasons: *"Arjun & Co. was debited during the month, so it goes in the Debit column."* Decide which column Arjun & Co. A/C actually occupies and at what amount, state what that Rs 1,00,000 debit did to the account rather than to its side, and name the general rule the junior has broken about what the trial balance lifts out of a ledger.

<details><summary>Answer</summary>

Arjun & Co. A/C goes in the **Credit** column at **Rs 2,00,000**. The Rs 1,00,000 debit shrank the debt from Rs 3,00,000 to Rs 2,00,000; it did not flip the account's side, because Rs 2,00,000 is still owed and a liability increases by credit. The junior's broken rule: the trial balance lifts each account's **closing balance**, never its last entry and never any single entry.

</details>

2. A business's first month closes with Cash Rs 19,10,000 debit, Purchases Rs 4,00,000 debit, Machinery Rs 3,00,000 debit, Commission Rs 50,000 debit, Capital Rs 20,00,000 credit, Sales Rs 4,60,000 credit, and Rs 2,00,000 still owed to its supplier Arjun & Co. — a trial balance tallying at Rs 26,60,000 both sides. On 1 July the business pays the supplier the remaining Rs 2,00,000 in cash, clearing the debt in full. Name the trial balance column Arjun & Co. A/C then occupies, state the new Cash balance, and give the new column totals.

<details><summary>Answer</summary>

Arjun & Co. A/C occupies **neither** column — the debt is cleared, the balance is nil, and an account with no balance simply drops off the trial balance. Cash falls to Rs 17,10,000. New totals: Rs 24,60,000 on both sides (Cash 17,10,000 + Purchases 4,00,000 + Machinery 3,00,000 + Commission 50,000 against Capital 20,00,000 + Sales 4,60,000).

</details>

---

## E11 — What a tallied trial balance CANNOT catch                     [EXT — not in your workbook]

**HIGH-YIELD. The single sharpest node in the topic.**

**Definition**

**A trial balance that matches perfectly proves almost nothing.**

The workbook (p.8) tells you the purpose is "to ensure arithmetical accuracy" — that is correct. On p.11 it asks the safe question: *"If the trial balance totals do not match, there is definitely an error in the ledger accounts. Yes/No"*. **Yes.** It never asks the converse, and the converse is the whole node.

**First: why does it balance at all?**

Not luck. Not skill. **By construction.**

- Every journal entry was written with **one debit and one matching credit** (Act 2's double-entry rule).
- So the books started with Σ debits = Σ credits, guaranteed, before any checking existed.
- The ledger only **regrouped** those figures by account. Regrouping cannot break a total.
- The trial balance only **copies out** the results.

**The trial balance balancing is a near-tautology.** You built the books so that they *must* balance, then checked that they balance. That is exactly why it proves so little.

**What it can prove:** that you added correctly, and copied faithfully.
**What it cannot prove:** that what you added was **true**.

**The frame:** the trial balance checks **arithmetic**, not **truth**. Σ debits = Σ credits is a statement about your **addition**, not about your **judgement**. **It cannot see a correctly-added lie.**

**Why the format looks like this**

The shape is forced by what the check physically does.

- The check is a **sum comparison**. A sum comparison can only detect things that **change a sum**.
- Any error that alters **one debit and one credit by the same amount** slides straight through — the sums move together, so the difference stays zero.
- Any error that keeps the amount and the sides and only changes **which account** slides through too — the account name is not in the arithmetic at all.

So the filter has **exactly one hole shape**, and four common errors are that shape.

**The format**

```
   ALL ERRORS
        |
        v
   +===========================================================+
   |            THE TRIAL BALANCE FILTER                       |
   |            "does Sum(Dr) = Sum(Cr) ?"                     |
   +===========================================================+
        |                                    |
   CAUGHT (totals move)              PASSES STRAIGHT THROUGH
        |                                    |
        v                                    v
   +---------------------+         +---------------------------+
   | one side posted,    |         | 1. OMISSION               |
   |   not the other     |         |    entry never made       |
   |                     |         |                           |
   | wrong column        |         | 2. PRINCIPLE              |
   |   (out by 2x)       |         |    wrong ACCOUNT TYPE     |
   |                     |         |                           |
   | added up wrong      |         | 3. COMMISSION             |
   |                     |         |    wrong account          |
   | balance copied      |         |    within the right type  |
   |   wrong from ledger |         |                           |
   |                     |         | 4. COMPENSATING           |
   |                     |         |    two errors cancelling  |
   +---------------------+         +---------------------------+
        |                                    |
        v                                    v
   TOTALS DISAGREE                  TOTALS AGREE PERFECTLY
   "there is an error"              "...and the books are wrong"
```

**In action**

Take the trial balance that tallied at **Rs 26,60,000**.

Now **omit Day 7 entirely** — never journalise the commission at all. The Rs 50,000 was genuinely paid; it simply never got written down. An **error of omission**.

| | Full books | Day 7 omitted |
|---|---|---|
| Cash | 19,10,000 | **19,60,000** *(the 50,000 never left)* |
| Purchases | 4,00,000 | 4,00,000 |
| Machinery | 3,00,000 | 3,00,000 |
| Commission | 50,000 | **— gone —** |
| **Debit total** | **26,60,000** | **26,60,000** |
| **Credit total** | **26,60,000** | **26,60,000** |

**The total does not change. Not by one rupee.**

- **Why:** the Rs 50,000 simply **moves out of Commission and stays in Cash**. Both are debit-side accounts. The debit column loses 50,000 in one row and gains 50,000 in another.
- **The deeper why:** omitting a whole entry removes **one debit AND one credit**. The check performs a subtraction of equals — so **the check it performs is untouched**.
- **The books are wrong.** An expense the business really paid has vanished. Profit is overstated. Cash is overstated.
- **The trial balance is incapable of noticing.**

**The four errors a tallied trial balance hides:**

| # | Error | What happened | Why the totals still agree |
|---|---|---|---|
| 1 | **Omission** | The entry was never recorded **at all** | Removes one debit **and** one credit — equal amounts leave both columns |
| 2 | **Principle** | Right amount, right sides, **wrong account TYPE** — machinery booked to Purchases | The Rs 3,00,000 debit still exists and still equals its credit; only its **name** is wrong |
| 3 | **Commission** | Right amount, right type, **wrong account within it** — paid to Arjun & Co., posted to a different creditor | The Rs 1,00,000 debit is still a debit of Rs 1,00,000; the column can't read names |
| 4 | **Compensating** | **Two** errors of equal size in **opposite directions** that cancel out | Debits over by Rs 10,000 and credits over by Rs 10,000 → difference is still zero |

**Where it bites**

The bite is **error of principle**, because it is the one that survives with the whole trial balance completely unchanged.

- **Wrong:** "Day 4's Rs 3,00,000 machinery got booked to Purchases A/C. The trial balance will be out by Rs 3,00,000 and I'll catch it."
- **Right:** the trial balance **still totals Rs 26,60,000 on both sides.** Purchases simply reads 7,00,000 instead of 4,00,000, and Machinery does not appear. Both are debit accounts. The debit column is untouched.

**The exact point it bites:** the debit column **cannot read account names**. It reads amounts. Swapping one debit account for another debit account is invisible to a sum.

```
   CORRECT BOOKS                    ERROR OF PRINCIPLE
   Cash        19,10,000  Dr        Cash        19,10,000  Dr
   Purchases    4,00,000  Dr        Purchases    7,00,000  Dr  <-- wrong
   Machinery    3,00,000  Dr        Machinery    -- gone --     <-- wrong
   Commission     50,000  Dr        Commission     50,000  Dr
   ---------------------------      ---------------------------
   Dr TOTAL    26,60,000            Dr TOTAL    26,60,000
                    ^                                ^
                    +--------- IDENTICAL ------------+

   Two rows are wrong. Every asset figure is wrong. The
   income statement is wrong. The total is perfect.
```

And the damage runs downstream: machinery is a **resource still controlled**, purchases is a **cost consumed**. Booking one as the other destroys the profit figure and the balance sheet at once — while the trial balance nods it through.

**The one-line summary:**

> **A mismatch proves an error exists. A match proves nothing.**

**Your turn**

1. A business buys machinery on credit from Arjun & Co. for Rs 3,00,000, and during the month pays Rs 1,00,000 of that bill in cash — so Rs 2,00,000 is genuinely still owed to Arjun & Co. The business also has a second supplier on its books, Saksham, whom it owes nothing. The bookkeeper debits the Rs 1,00,000 payment, correctly as a debit and correctly at Rs 1,00,000, to **Saksham's** account instead of Arjun & Co.'s. The resulting trial balance reads:

   | Account | L.F | Debit | Credit |
   |---|---|---|---|
   | Cash A/C | | 19,10,000 | |
   | Purchases A/C | | 4,00,000 | |
   | Machinery A/C | | 3,00,000 | |
   | Commission A/C | | 50,000 | |
   | Saksham A/C | | 1,00,000 | |
   | Capital A/C | | | 20,00,000 |
   | Sales A/C | | | 4,60,000 |
   | Arjun & Co. A/C | | | 3,00,000 |
   | **TOTAL** | | **?** | **?** |

   Total both columns and state whether the statement tallies. Then name the error type, state which figures on this page are untrue and what each should have read, and explain why the two column totals could not have revealed the mistake.

<details><summary>Answer</summary>

It tallies — Rs 27,60,000 on both sides. This is an **error of commission**: right amount, right side, right account *type*, wrong account within it. Two figures are untrue: Arjun & Co. shows Rs 3,00,000 credit when only Rs 2,00,000 is owed (the payment looks as though it never happened), and Saksham shows a Rs 1,00,000 debit when the business has no such claim on him at all. The totals could not reveal it because the columns add **amounts**, not names — a Rs 1,00,000 debit is a Rs 1,00,000 debit whichever creditor's name sits beside it, so the arithmetic the trial balance performs is untouched.

</details>

2. A business trades for its first month: the owner puts in Rs 20,00,000 cash, goods costing Rs 4,00,000 are bought for cash and sold for cash at Rs 4,60,000, machinery is bought on credit for Rs 3,00,000 from Arjun & Co. with Rs 1,00,000 of that paid in cash, and a commission of Rs 50,000 is paid in cash. The books are closed and the trial balance is drawn:

   | Account | L.F | Debit | Credit |
   |---|---|---|---|
   | Cash A/C | | 19,60,000 | |
   | Purchases A/C | | 4,00,000 | |
   | Machinery A/C | | 3,00,000 | |
   | Capital A/C | | | 20,00,000 |
   | Sales A/C | | | 4,60,000 |
   | Arjun & Co. A/C | | | 2,00,000 |
   | **TOTAL** | | **26,60,000** | **26,60,000** |

   The bookkeeper reports a net profit of Rs 60,000 and hands the page over, saying *"it tallies to the rupee, so it's clean."* Assuming all goods bought were sold, identify what has gone wrong, name the error type, state the correct net profit and the correct cash figure, and prove — by reasoning about what the check physically does — that the trial balance was **incapable** of detecting it.

<details><summary>Answer</summary>

The Rs 50,000 commission was genuinely paid but never journalised at all — an **error of omission**. Commission A/C is missing from the page entirely, and the Rs 50,000 that really left the business is still sitting in Cash. Net profit should be **Rs 10,000**, not Rs 60,000 — overstated by Rs 50,000. Cash should be **Rs 19,10,000**, not Rs 19,60,000 — overstated by Rs 50,000. The trial balance could not catch it: omitting a whole entry removes **one debit and one matching credit**, so the check subtracts equals from both columns and its result is unchanged. Here the Rs 50,000 simply moved out of Commission and stayed in Cash — both debit accounts — so the debit column lost it in one row and gained it in another. Correct books and these broken books both total Rs 26,60,000, identically, to the rupee. "It tallies" is not evidence of anything: a mismatch proves an error exists; a match proves nothing.

</details>

---

# ACT 7 — So did the business make money?

## G1 — Why the chain can't stop at the trial balance                     [EXT — not in your workbook]

> **Scope note, up front and honest:** everything in Act 7 is `[EXT]`. Your workbook names the
> Income Statement, the Balance Sheet and Cash Flow **once**, on p.2, as vocabulary — and never
> builds one. Your facilitators will back you up through the trial balance. Past that line, this
> sheet is the extension. You should know exactly where the supported ground ends.

**Definition**

A trial balance is a **checkpoint**, not a destination.

It answers exactly one question: *did the debits and the credits come out equal?*

That is a question about **your arithmetic**. It is not a question about **your business**.

- The TB proves the books add up.
- The TB does **not** say whether the business got richer.
- The TB does **not** say whether the business can pay anyone on Friday.
- The TB is a list of account balances in no meaningful order — Cash sits next to Purchases, which
  are two completely different kinds of thing.

**Why the format looks like this**

The TB's shape is forced by its job: prove Σ debits = Σ credits. So it needs two columns and a
total. Nothing else. It has no room to answer a business question because it was never asked one.

To answer a business question you need a format shaped by **that** question. Different question,
different shape. That is the whole of Act 7.

**The format**

```
                     ┌──────────────────────────┐
   Journal ─────────▶│      TRIAL BALANCE       │
   Ledger  ─────────▶│  26,60,000 = 26,60,000   │
                     └────────────┬─────────────┘
                                  │
                   "Great. The addition is fine."
                                  │
                                  ▼
            ┌─────────────────────┴─────────────────────┐
            │                                           │
   "Did we get richer?"                     "What do we have,
    ─ TB cannot say ─                        and who has a claim on it?"
                                             ─ TB cannot say ─
```

**In action**

Look at the verified TB from Stage 3:

| Account | Debit | Credit |
|---|---|---|
| Cash A/C | 19,10,000 | |
| Purchases A/C | 4,00,000 | |
| Machinery A/C | 3,00,000 | |
| Commission A/C | 50,000 | |
| Capital A/C | | 20,00,000 |
| Sales A/C | | 4,60,000 |
| Arjun & Co. A/C | | 2,00,000 |
| **TOTAL** | **26,60,000** | **26,60,000** |

Now try to read a business answer off it:

- **"Did the business make a profit?"** — Sales 4,60,000 and Purchases 4,00,000 are on *opposite
  sides* of this table. Nothing here subtracts them.
- **"What does the business own?"** — Cash 19,10,000 and Machinery 3,00,000 are true assets, but
  they sit interleaved with Purchases 4,00,000, which the business does **not** own any more.
- **"What does the business owe?"** — Arjun & Co. 2,00,000 is buried between Capital and nothing in
  particular.

The TB has all the raw material and answers none of the questions.

**Where it bites**

The bite: **students treat "it balanced" as "we're done."**

> **Wrong:** "TB totals 26,60,000 both sides — the books are correct and the work is finished."
>
> **Right:** "TB totals 26,60,000 both sides — the *addition* is consistent. The books may still be
> wrong (see the error-of-omission demo: omit the Day 7 commission entirely and the TB **still**
> totals 26,60,000 on both sides — not off by one rupee). And even if the books are perfectly
> right, I have learned nothing about the business yet."

**The exact point it bites:** the moment you read the word *balance* as *correct* or as *complete*.
It means neither. It means **equal**.

**Your turn**

1. A business hands a lender this trial balance and asks for a loan:

   | Account | Debit | Credit |
   |---|---|---|
   | Cash | 19,10,000 | |
   | Purchases | 4,00,000 | |
   | Machinery | 3,00,000 | |
   | Commission | 50,000 | |
   | Capital | | 20,00,000 |
   | Sales | | 4,60,000 |
   | Arjun & Co. (supplier) | | 2,00,000 |
   | **TOTAL** | **26,60,000** | **26,60,000** |

   The lender's junior says: "It balances at Rs 26,60,000, so the books are correct and the business
   earned Rs 26,60,000 — approve it." Name the two separate category errors packed into that
   sentence, and state what the lender has actually been shown.

<details><summary>Answer</summary>

(a) *Balanced ≠ correct.* Rs 26,60,000 both sides proves only that Σ debits = Σ credits — omit a whole entry (say a Rs 50,000 commission payment) and the total is still Rs 26,60,000 on both sides, unchanged by a single rupee. (b) *Balanced ≠ earned.* Rs 26,60,000 is the sum of one side of a two-sided list, not value earned; Sales Rs 4,60,000 is the only earning figure there and nothing on this page subtracts anything from it. The lender has been shown that someone's addition is consistent — nothing about whether the business earned, owns enough, or can repay.

</details>

2. From that same trial balance, a supplier asks two questions: *"How much does this business still
   owe us?"* and *"Did this business make a profit in June?"* One is answerable directly from the
   page; one is not. Say which is which and explain what structural feature of the trial balance
   creates that difference.

<details><summary>Answer</summary>

"How much do we still owe?" is answerable: Rs 2,00,000 — it needs one account's balance, already computed and sitting on the page. "Did we profit?" is not: it needs a *relationship between* Sales Rs 4,60,000, Purchases Rs 4,00,000 and Commission Rs 50,000, and the trial balance's debit/credit layout actively puts them on opposite sides and never subtracts them. The TB lists balances; it does not relate them.

</details>

---

## A17 — Period vs point-in-time                     [EXT — not in your workbook]

**Definition**

The two main statements differ in **KIND**, not in detail. This is not a formatting preference.
They measure two different species of quantity.

- A **FLOW** is measured **over a stretch of time**. It has a start and an end. Example: *how far
  did you walk today?*
- A **STOCK** is measured **at one instant**. It has a timestamp, not a duration. Example: *where
  are you standing right now?*

| | Income Statement | Balance Sheet |
|---|---|---|
| Measures a… | **FLOW** | **STOCK** |
| Time | a **PERIOD** — 1–30 June 2024 | an **INSTANT** — as at 30 June 2024 |
| Metaphor | a **VIDEO** | a **PHOTOGRAPH** |
| Answers | *Did we get richer by operating?* | *What do we have, and who has a claim on it?* |
| Header must say | "**for the period** …" | "**as at** …" |
| Meaningless without | a date **RANGE** | a single **INSTANT** |

**Why the format looks like this**

The header is not decoration — it is the unit.

- "Sales 4,60,000" means nothing until you know **over what stretch**. A month? A day? A decade?
- "Cash 19,10,000" means nothing until you know **at what moment**. Cash changed five times in June.

Strip the header off either statement and the numbers stop being numbers. They become noise with
commas in them.

**The format**

```
   1 June                                                  30 June
     │                                                        │
     ├────────────────────────────────────────────────────────┤
     │        INCOME STATEMENT  ==  the VIDEO                  │
     │        "for the period 1–30 June 2024"                  │
     │        rolls the whole month                            │
     ├────────────────────────────────────────────────────────┤
                                                              │
                                                              ▼
                                                   ┌──────────────────┐
                                                   │  BALANCE SHEET   │
                                                   │ == the PHOTOGRAPH│
                                                   │ "as at 30 June"  │
                                                   │  one shutter click│
                                                   └──────────────────┘
```

**In action**

Take Rs 4,60,000 (Sales) and Rs 19,10,000 (Cash) from the spine.

| Figure | Species | Correct sentence |
|---|---|---|
| Sales 4,60,000 | FLOW | "The business sold 4,60,000 **during** 1–30 June." |
| Cash 19,10,000 | STOCK | "The business held **19,10,000 cash at the instant** of 30 June." |

You cannot ask "how much Sales did the business have *at* 30 June?" The question is malformed.
Sales isn't a thing you *have*; it's a thing that *happened*.

You cannot ask "how much Cash did the business have *during* June?" Also malformed. The Cash A/C
was struck **five separate times** in June — Day 1, 2, 3, 6, 7 — so it held a different amount at
almost every instant of the month. "During" has no answer. Only "as at" does.

**Where it bites**

The bite: **speed vs position.**

> **Wrong:** "The Income Statement and the Balance Sheet are both just summaries of the year — one
> is a bit more detailed than the other."
>
> **Right:** "They differ in KIND. Confusing them is confusing *how fast was the car going* with
> *where is the car*. Both are true facts about the same car. Neither can be derived from the
> other by adding detail."

**The exact point it bites:** when a student writes "Balance Sheet **for the year ended** 30 June"
or "Income Statement **as at** 30 June." Those headers are not sloppy — they are **category
errors**, and they announce that the writer does not know what the statement measures.

**Your turn**

1. A bank is deciding whether to lend to a business. It receives two pages with the date lines torn
   off. Page one reads only *"Cash — Rs 19,10,000."* Page two reads only *"Sales — Rs 4,60,000."*
   The bank knows, separately, that this business's cash was struck five times in June — money came
   in on the 1st and the 3rd, and went out on the 2nd, the 6th and the 7th — while its selling all
   happened inside that same month. Which torn page is more badly damaged, and why is that asymmetry
   inevitable rather than bad luck?

<details><summary>Answer</summary>

The Cash page. Sales Rs 4,60,000 without a date range is incomplete but recoverable — a flow has exactly one value for any stated period, so the bank need only ask "over what stretch?" Cash Rs 19,10,000 without an instant is meaningless: a stock has a *different* value at almost every moment, and this cash balance changed five times inside June, so "Rs 19,10,000" names one of many instants and the page does not say which. The asymmetry is inevitable because a flow is defined by a duration and a stock by a timestamp — strip the header and you strip the unit itself.

</details>

2. An investor is sent four figures from a business's books with no headers at all: Machinery
   Rs 3,00,000 (a machine bought on credit and still on the shop floor at month end); Commission
   Rs 50,000 (paid out during the month); Arjun & Co. Rs 2,00,000 (still owed to a supplier at month
   end); Purchases Rs 4,00,000 (goods bought during the month). For each, say whether it is a FLOW
   or a STOCK, and write the header line the investor must demand before the figure means anything.

<details><summary>Answer</summary>

Machinery Rs 3,00,000 — STOCK — "as at 30 June 2024". Commission Rs 50,000 — FLOW — "for the period 1–30 June 2024". Arjun & Co. Rs 2,00,000 — STOCK — "as at 30 June 2024". Purchases Rs 4,00,000 — FLOW — "for the period 1–30 June 2024".

</details>

---

## A8 / A9 / A10 — Income Statement, Balance Sheet, Cash Flow (the words)                     [SOURCED p.2 — as vocabulary only]

**Definition**

These three names **are** in your workbook — p.2, in the vocabulary list. That is the entire extent
of it. The workbook never builds one, never shows a format, never routes a figure into one. It
gives you the labels and stops.

So: the *names* are sourced. Everything this sheet does **with** them is `[EXT]`.

The three statements are three answers to three genuinely different questions:

| # | Statement | The question it answers | Time | Node |
|---|---|---|---|---|
| 1 | **Income Statement** (P&L) | *Did we get richer by operating?* | a PERIOD | A8 / G2 |
| 2 | **Balance Sheet** | *What do we have, and who has a claim on it?* | an INSTANT | A9 / G3 |
| 3 | **Cash Flow Statement** | *Can we pay people on Friday?* | a PERIOD | A10 / G6 |

**Why the format looks like this**

There are three statements because there are three questions — and **no one statement can answer
another one's question.** That is not tradition or bureaucracy. It is proved by the spine: net
profit **10,000**, cash **19,10,000**. Two honest numbers about the same business, in the same
month, that do not explain each other (see G8).

**The format**

```
   ONE set of books  ──▶  THREE questions  ──▶  THREE statements

   "Did we get richer          "What do we have,        "Can we pay people
    by operating?"              who has a claim?"        on Friday?"
          │                            │                        │
          ▼                            ▼                        ▼
   INCOME STATEMENT            BALANCE SHEET           CASH FLOW STATEMENT
      (a VIDEO)                (a PHOTOGRAPH)              (a VIDEO)
     1–30 June 2024            as at 30 June 2024        1–30 June 2024
```

**In action**

Same business, same June, from the spine:

- **Income Statement** says: **Net profit 10,000.**
- **Balance Sheet** says: **Total 22,10,000**, of which the owner's claim is **20,10,000** and
  Arjun & Co.'s claim is **2,00,000**.
- **Cash Flow** says: the business ended June holding **19,10,000** in cash.

Three answers. None is more "correct." They were never competing.

**Where it bites**

> **Wrong:** "Financial statements = one big report at the end of the year."
>
> **Right:** "*Financial statements* is a plural for a reason. It is a small **set** of documents,
> each purpose-built for one question, all drawn from the same trial balance."

**The exact point it bites:** when a student assumes the three statements are three *views* of one
number and goes looking for the one that is 'the real answer'. There is no such statement. Asking
which one is 'the real one' is like asking whether a car's speed or its location is the real fact.

**Your turn**

1. A shop owner is shown three findings about her own June: she earned a net profit of Rs 10,000;
   she holds Rs 19,10,000 of cash and a Rs 3,00,000 machine, against Rs 2,00,000 still owed to a
   supplier; and of the cash that came in during June, Rs 20,00,000 was money she herself put into
   the business on day one. She says: "I only care about one thing — am I making money? Give me the
   profit statement and bin the other two." Describe a concrete way the business dies within a few
   months if she is obeyed, and name which binned statement would have warned her.

<details><summary>Answer</summary>

She sells hard on credit: profit keeps climbing, but the money sits in customers' accounts while she has already paid for goods and running costs. Meanwhile the Rs 20,00,000 cushion was her own funding, not earnings — it drains and never refills, and the Rs 2,00,000 supplier claim falls due regardless. Payroll Friday arrives, there is no cash, and the business dies with its best-ever profit figure on the page. The Cash Flow Statement ("can we pay people on Friday?") would have shown the earning engine was tiny and the cash was financing; the Balance Sheet would have shown the outsider's claim ranking ahead of her.

</details>

2. A bookkeeper is hired to keep a business's records and stops at the trial balance — journals
   written, ledgers posted, trial balance totalling Rs 26,60,000 on both sides. The owner now wants
   to know whether to buy a second machine. State precisely what capability the bookkeeper's work
   has given the owner and what it has not, and why the answer is not "just add more detail to the
   trial balance."

<details><summary>Answer</summary>

Given: a complete, arithmetically consistent record — every event captured and provably debit-equals-credit at Rs 26,60,000. Not given: any answer to whether the business earned, what it owns against what it owes, or whether it can pay — and no protection against errors the trial balance cannot detect at all. Detail will not fix it: the trial balance's two-column shape exists to prove one equality, and no amount of extra lines makes it perform a subtraction or set claims against resources. A different question needs a differently shaped page.

</details>

---

## G2 — Income Statement                     [EXT — not in your workbook]

**Definition**

The **Income Statement** takes everything the business **earned** over a period, subtracts
everything it **used up** over that same period, and reports what is left.

**Revenue − Expenses, over a PERIOD.**

It answers one question, and only one:

> **Was the business richer at the end of June than at the start — because of operating?**

That last clause is doing real work. "Because of operating" means: **richer by trading**, not
richer because someone handed the business money.

- **Revenue** = value the business earned by doing its job. (Sales.)
- **Expense** = value the business consumed and no longer controls. (Purchases sold, Commission.)
- **The leftover** = **net profit** — the amount by which operating grew the owner's claim.

**Why the format looks like this**

The shape is forced by the job.

- The job is a **subtraction**, so the format must be **vertical** — you cannot see a subtraction
  laid out left-and-right.
- The job runs **top to bottom in stages**, because you want more than one answer:
  - *Did the goods themselves make money?* → **Gross Profit** (Sales − cost of goods sold).
  - *Did the business survive its running costs?* → **Net Profit** (Gross Profit − other expenses).
- If the goods sell at a loss, you want to know **before** you get distracted by commission. So
  cost of goods sold comes first, always, and gets its own subtotal.
- Only **consumed** things appear. Machinery is absent — not an oversight, a rule (see G7).

**The format**

```
   ┌────────────────────────────────────────────────────────┐
   │              INCOME STATEMENT                          │
   │        for the PERIOD 1–30 June 2024   ◀── date RANGE  │
   ├────────────────────────────────────────────────────────┤
   │                                                        │
   │   Revenue (what we earned)              XXXX           │
   │   Less: Cost of goods sold             (XXXX)          │
   │                                        ───────         │
   │   GROSS PROFIT                          XXXX  ◀ stage 1│
   │                                                        │
   │   Less: Other expenses                 (XXXX)          │
   │                                        ───────         │
   │   NET PROFIT                            XXXX  ◀ stage 2│
   │                                        ═══════   │     │
   └──────────────────────────────────────────────────┼─────┘
                                                      │
                       this number leaves and goes to the Balance Sheet ──▶ (G7)
```

**In action**

> ### `[INFERRED]` — READ THIS BEFORE YOU READ THE NUMBERS
>
> **The workbook gives NO CLOSING STOCK.** So this statement assumes **every rupee of goods
> purchased was sold** — nothing is left on the shelf. That is why "Purchases 4,00,000" is used
> directly as cost of goods sold.
>
> **Real businesses almost never look like this.** Normally you would subtract the unsold stock
> still sitting in the shop before calling Purchases a cost. This assumption is an inference made
> to complete the example, not a fact stated by the workbook, and you should say so out loud if
> asked.

**Stage 4 — Income Statement, for the period 1–30 June 2024:**

| | Amount |
|---|---|
| Sales | 4,60,000 |
| *Less:* Cost of goods sold (Purchases) | (4,00,000) |
| **Gross Profit** | **60,000** |
| *Less:* Commission | (50,000) |
| **NET PROFIT** | **10,000** |

Read it as a sentence:

- The goods themselves earned **60,000**. That's a real trading margin.
- Running the business ate **50,000** of it in commission.
- What survived: **10,000**.

**A period. A video.** Machinery is absent — it wasn't consumed, it was acquired.

**Where it bites**

The bite: **Capital 20,00,000 wants to walk into this statement, and it must not.**

> **Wrong:**
> Sales 4,60,000 + Capital 20,00,000 = "income" 24,60,000
> less Purchases 4,00,000, less Commission 50,000 → "profit" **20,10,000**
>
> **Right:**
> Sales 4,60,000 − Purchases 4,00,000 − Commission 50,000 → **net profit 10,000**
> Capital 20,00,000 never enters. It was **supplied by the owner**, not **earned from a customer**.

**The exact point it bites:** the word *income* in ordinary English means "money coming in," and
20,00,000 unmistakably came in. But an Income Statement measures **earning**, not **arriving**.
Money the owner puts in is the owner **funding** the business, not the business **succeeding**.
If owner money counted as profit, any business could report a spectacular profit by having its
owner move money from one pocket to another.

Notice the wrong answer produced **20,10,000** — which really is a number in the spine. It is the
**closing Capital on the Balance Sheet**, not profit. Landing on a real-looking figure is exactly
what makes this error survive a self-check.

**Your turn**

1. In its first month a business does four things: the owner puts in Rs 20,00,000 cash; it buys
   goods for Rs 4,00,000 and sells them for Rs 4,60,000; it buys a machine for Rs 3,00,000 on credit
   from a supplier; it pays Rs 50,000 commission. Its income statement for the month reads:

   | | Amount |
   |---|---|
   | Sales | 4,60,000 |
   | *Less:* Cost of goods sold | (4,00,000) |
   | **Gross Profit** | **60,000** |
   | *Less:* Commission | (50,000) |
   | **NET PROFIT** | **10,000** |

   The owner objects twice: "The machine cost me Rs 3,00,000 — my biggest commitment after the goods
   — and it isn't on here at all. And I put in Rs 20,00,000, which is money that came in, so my
   income should be Rs 24,60,000." Answer both objections from the definition of *expense* and the
   definition of *revenue*, then say what would have to become true for the machine to start
   appearing on this statement.

<details><summary>Answer</summary>

The machine is not an expense because the business still controls the resource at month end — nothing was consumed, value was only swapped (a promise to pay for a machine). Expenses are things used up; the test is *do you still control a resource afterwards?* The Rs 20,00,000 is not revenue because revenue is value **earned** from a customer, not money **supplied** by the owner — if owner money counted, any owner could manufacture profit by moving money between pockets. Net profit stays Rs 10,000. The machine begins appearing only once it is consumed — worn down over time as depreciation, or sold or scrapped.

</details>

2. The same business's income statement above treats the whole Rs 4,00,000 of goods bought as the
   cost of what it sold, because nothing was left on the shelf. Now suppose that at month end goods
   worth Rs 1,00,000 were still sitting unsold in the shop. Do **not** compute a new profit. Name
   which single line changes, say which way net profit moves, and explain why the unsold goods do
   not simply disappear from the books.

<details><summary>Answer</summary>

The "Less: Cost of goods sold (4,00,000)" line changes — only goods actually sold are a cost, so that line shrinks and net profit moves UP. The unsold goods do not vanish: the business still controls them at month end, so they stop being an expense and become an asset (closing stock) on the balance sheet instead. The rupees move statements; they are not destroyed.

</details>

---

## G5 — Why "income" statement / P&L                     [EXT — not in your workbook]

**Definition**

The name tells you the species. **Income = a FLOW.**

- **Income** is money **coming in over time** — like income from a job. You never say "my income is
  Rs 50,000 *at* Tuesday." You say "*per month*." A duration is baked into the word.
- The statement is also called the **P&L** — **Profit and Loss** account. Same document, older
  name, common in Indian practice. Both names describe **change**, not **holding**.

Every word in the title is a flow word:

| Word | Flow or stock? | Tell |
|---|---|---|
| **Income** | FLOW | comes *in*, over a stretch |
| **Profit** | FLOW | you *make* it, during something |
| **Loss** | FLOW | you *incur* it, during something |
| **Revenue** | FLOW | earned across a period |
| **Expense** | FLOW | consumed across a period |

Contrast the Balance Sheet's vocabulary — *assets, liabilities, capital, balance*. Every one of
those is a thing you **hold**. Not one is a thing that **happens**.

**Why the format looks like this**

Because the format has to report a **change**, it needs:

- a **start and an end** in the header ("for the period 1–30 June 2024"),
- accounts that **reset to zero** and start counting again each period,
- **no** carried-forward opening figure — a new period starts a new count.

That last point is the mechanical fingerprint of a flow. Sales starts every period at zero. Cash
never does.

**The format**

```
   FLOW  (Income Statement)                  STOCK  (Balance Sheet)
   ────────────────────────                  ─────────────────────────
   resets to 0 each period                   carries forward for ever

   June:  0 ──▶ Sales 4,60,000               30 June: Cash 19,10,000
   July:  0 ──▶ Sales  ...                       │
   Aug:   0 ──▶ Sales  ...                       └──▶ 1 July opens AT 19,10,000
                                                      (it does NOT reset)
   ▲                                          ▲
   │ "how fast was the car going"             │ "where is the car"
```

**In action**

From the spine's Stage 2 ledgers, the fingerprint is visible in the balancing lines:

- **Sales A/C** closed at **4,60,000 credit** — that is 4,60,000 **earned during June**, counted
  from zero on 1 June. On 1 July it starts from zero again.
- **Cash A/C** closed at **19,10,000 debit** — that is 19,10,000 **held on 30 June**. On 1 July it
  opens at 19,10,000. It does not reset, because you did not stop having the money at midnight.

Same ledger book. Two completely different species of account. The Income Statement collects the
first kind; the Balance Sheet collects the second.

**Where it bites**

> **Wrong:** "Net profit is Rs 10,000, so the business **has** Rs 10,000."
>
> **Right:** "Net profit Rs 10,000 is the **rate at which the owner's claim grew during June**. It
> is not a pile of anything. What the business *has* is Cash 19,10,000 and Machinery 3,00,000 —
> and those two figures come from a different statement entirely."

**The exact point it bites:** the instant you turn a flow noun into a stock noun — "profit" into
"a profit sitting somewhere." Profit is not stored anywhere. There is no Profit A/C with money in
it. Profit is a **measurement of change**, and asking where it's kept is asking where your walking
speed is kept.

**Your turn**

1. A business closes its June books. Two accounts end on the credit side: Sales Rs 4,60,000 (goods
   sold to customers during June) and Capital Rs 20,00,000 (money the owner put in on day one). The
   month also produced a net profit of Rs 10,000. A new bookkeeper says: "Both are credit balances
   of roughly the same order, so treat them the same way when July opens." Using only the
   reset-to-zero test, prove they are different species, and state what each account's balance is on
   1 July.

<details><summary>Answer</summary>

Sales resets to zero on 1 July — it counted only what was earned during June, and July starts a new count. That reset is the fingerprint of a FLOW. Capital does not reset: it opens 1 July at Rs 20,10,000 (the Rs 20,00,000 put in, plus the Rs 10,000 June earned into the owner's claim), because the owner's claim did not evaporate at midnight. That carry-forward is the fingerprint of a STOCK. Being credit balances of similar size is irrelevant — debit/credit is direction, not species.

</details>

2. A business's owner reads that her month produced a net profit of Rs 10,000 and asks her
   bookkeeper to "go and fetch the Rs 10,000 profit out of the drawer." The books show cash of
   Rs 19,10,000 and a machine worth Rs 3,00,000, and no account called "Profit" holding anything.
   Show why the statement's two names — "Income Statement" and "Profit and Loss account" — both
   predicted that her request would be impossible, then invent one alternative name for the same
   document that would **fail** that test, and say what a reader would wrongly expect from it.

<details><summary>Answer</summary>

Every word in both names is a change word: *income* comes in over a stretch, *profit* is made during something, *loss* is incurred during something. None names a thing you hold, so neither name ever promised a pile to fetch — the Rs 10,000 is a measurement of how much the owner's claim grew during the month, and it lives on the balance sheet as a larger claim, not as cash. What she can fetch is cash Rs 19,10,000, and that comes from a different statement entirely. A failing name: "Statement of Business Wealth" (or "Earnings Held") — it names a stock, so a reader would expect a holdable balance at an instant and would go looking for where the Rs 10,000 is stored, when nothing is stored and no such instant exists.

</details>

---

## G3 — Balance Sheet                     [EXT — not in your workbook]

**Definition**

The **Balance Sheet** is a list of everything the business **has** at one instant, set against a
list of **who has a claim on it**.

**Assets, Liabilities and Equity, at an INSTANT.**

It answers:

> **What do we have — and who has a claim on it?**

Both halves matter. Owning things is only half the story; someone else may be owed out of them.

- **Assets** = resources the business **controls**. (Cash, Machinery.)
- **Liabilities** = claims by **outsiders**. (Arjun & Co. — still owed 2,00,000.)
- **Equity / Capital** = the claim by the **owner** — whatever is left after outsiders are paid.

The rule underneath: **A = L + E.** Every rupee of stuff on the left was **funded by someone**, and
that someone is on the right.

**Why the format looks like this**

The shape is forced by the job, and the job is **two-sided**.

- You are not reporting one list. You are reporting the **same value twice**: once as **what it
  is**, once as **where it came from**.
- That is why it's **side-by-side**, not top-to-bottom. A subtraction goes vertical (G2). A
  **correspondence** goes horizontal.
- **Left = uses.** What the money became.
- **Right = sources.** Who supplied it.
- Every asset must be traceable to a source, so the sides are the same total **by construction**
  (see G4).
- **Outsiders are listed before the owner**, because outsiders get paid first. The owner is the
  residual claimant — the one who gets what's left.

**The format**

```
   ┌──────────────────────────────────────────────────────────────────┐
   │                        BALANCE SHEET                             │
   │              as at 30 June 2024   ◀── one INSTANT                │
   ├───────────────────────────────────┬──────────────────────────────┤
   │  LIABILITIES & EQUITY             │  ASSETS                      │
   │  = SOURCES (who supplied it)      │  = USES (what it became)     │
   ├───────────────────────────────────┼──────────────────────────────┤
   │                                   │                              │
   │  Outsiders' claims:               │  Cash                XXXX    │
   │     Creditors            XXXX     │  Machinery           XXXX    │
   │                                   │                              │
   │  Owner's claim:                   │                              │
   │     Capital       XXXX            │                              │
   │     Add: Net Profit XXX           │                              │
   │                          XXXX     │                              │
   │                        ───────    │                     ───────  │
   │  TOTAL                   XXXX ────┼── must equal ──▶      XXXX   │
   │                        ═══════    │                     ═══════  │
   └───────────────────────────────────┴──────────────────────────────┘
```

**In action**

**Stage 5 — Balance Sheet, as at 30 June 2024:**

| Liabilities & Equity | Amount | Assets | Amount |
|---|---|---|---|
| Arjun & Co. (creditor) | 2,00,000 | Cash | 19,10,000 |
| Capital 20,00,000 | | Machinery | 3,00,000 |
| *Add:* Net Profit 10,000 | **20,10,000** | | |
| **TOTAL** | **22,10,000** | **TOTAL** | **22,10,000** |

**An instant. A photograph.**

**The check:** 22,10,000 = 2,00,000 + 20,10,000. **A = L + E.**

Read it as sentences:

- **What do we have?** Cash 19,10,000 and Machinery 3,00,000. Total **22,10,000**.
- **Who has a claim?** Arjun & Co. has a claim of **2,00,000**. The owner's claim is the rest —
  **20,10,000**.
- **Where did the owner's claim come from?** 20,00,000 was **put in**. 10,000 was **earned**. Those
  are two different origins, and the format shows them on two separate lines *on purpose*.

**Where it bites**

The bite: **Purchases 4,00,000 tries to walk onto the asset side.**

> **Wrong:**
> Assets = Cash 19,10,000 + Machinery 3,00,000 + Purchases 4,00,000 = 26,10,000
> …and now nothing balances, and the student starts hunting for an arithmetic mistake that
> does not exist.
>
> **Right:**
> Assets = Cash 19,10,000 + Machinery 3,00,000 = **22,10,000**
> Purchases is **not** on the Balance Sheet at all. Under the `[INFERRED]` no-closing-stock
> assumption, **those goods were sold**. The business does not control them any more. They were
> consumed, so they went to the Income Statement as cost of goods sold and were **used up there**.

**The exact point it bites:** at the word "purchased." Ordinary English says buying gives you a
thing, and things are assets. Accounting asks a sharper question: **do you still control the
resource right now, at the instant of the photograph?**

- Machinery on 30 June — **yes**, still in the building. → **Asset**.
- Goods on 30 June — **no**, sold on Day 3. → **Expense**, gone.

Same word, "purchased." Opposite answers. The test is **control at the instant**, never the verb.

**Your turn**

1. A business buys a machine for Rs 3,00,000 on credit from a supplier, then a few days later pays
   that supplier Rs 1,00,000 in cash, leaving Rs 2,00,000 still owed. At month end its balance sheet
   reads:

   | Liabilities & Equity | Amount | Assets | Amount |
   |---|---|---|---|
   | Supplier (creditor) | 2,00,000 | Cash | 19,10,000 |
   | Capital 20,00,000 | | Machinery | 3,00,000 |
   | *Add:* Net Profit 10,000 | **20,10,000** | | |
   | **TOTAL** | **22,10,000** | **TOTAL** | **22,10,000** |

   The owner says: "Paying Rs 1,00,000 out of the door made us poorer — so that payment must have
   shrunk my claim." Explain what that single payment actually did to **each of the three**
   categories on this sheet, and why the sheet still closes at Rs 22,10,000 on both sides afterwards.

<details><summary>Answer</summary>

Assets fell Rs 1,00,000 (cash left). Liabilities fell Rs 1,00,000 (the supplier's claim went from Rs 3,00,000 to the Rs 2,00,000 shown). Equity was untouched — the owner is no poorer. Both sides moved down by the same amount at the same instant, so the correspondence held and the sheet still closes at Rs 22,10,000 = Rs 22,10,000. Paying a debt settles an outsider's claim with a resource; it neither creates nor destroys the owner's claim.

</details>

2. Reading that same balance sheet — Cash Rs 19,10,000, Machinery Rs 3,00,000, supplier owed
   Rs 2,00,000, owner's claim Rs 20,10,000, both sides Rs 22,10,000 — the owner announces she will
   withdraw her full Rs 20,10,000 today and take a holiday. Using only the figures on the sheet,
   give the two independent reasons she cannot, and say what her Rs 20,10,000 actually is.

<details><summary>Answer</summary>

First, a claim is not cash: there is only Rs 19,10,000 of cash on the sheet — the rest of her claim is backed by a Rs 3,00,000 machine, which is not spendable. Second, the supplier's Rs 2,00,000 ranks ahead of her; outsiders are listed before the owner precisely because they get paid first. Her Rs 20,10,000 is a *residual claim* on the assets — whatever would be left after outsiders are settled — not a withdrawable balance sitting anywhere.

</details>

---

## G4 — Why "balance SHEET"                     [EXT — not in your workbook]

**Definition**

The name is completely literal. It is a **sheet** on which the **balance** — the accounting
equation — is **laid out**.

**A Balance Sheet IS `A = L + E`, presented.**

That's it. There is no cleverness hiding in the name. Someone took the equation, drew a line down
the middle of a page, put the left side of the equation on the left and the right side on the
right, and called it a sheet showing the balance.

And here is the part that changes how you work:

> **It does not balance because you balanced it. It balances because it was never possible for it
> not to.**

**Why the format looks like this**

Because **the two sides were never independent quantities.**

They are the **same value described twice**:

- The **left** asks: *what is the value now?*
- The **right** asks: *where did that value come from?*

Every rupee of asset arrived from **somewhere** — an outsider or the owner. There is no third
option. Money does not appear. So the sources always account for exactly 100% of the uses.

Recall the **sources vs uses** demonstration from the spine:

- Day 1: right side = 20,00,000 (owner supplied it).
- Day 2: spend 4,00,000 on goods → **the right side does not move.** Only the left re-shapes.

**Spending money never changes where money came from.** That's the engine. Every transaction
either re-shapes one side, or moves both sides together — never one side alone. So the totals
cannot drift apart.

**The format**

```
              THE EQUATION                          THE SHEET
       ┌────────────────────────┐        ┌─────────────┬─────────────┐
       │    A   =   L   +   E   │  ───▶  │ L + E       │      A      │
       └────────────────────────┘        │ (sources)   │   (uses)    │
                                         │             │             │
        left of "="  ──────────────────────────────────▶  ASSETS side│
        right of "=" ──▶ LIABILITIES + EQUITY side       │           │
                                         │  22,10,000  │  22,10,000  │
                                         └──────┬──────┴──────┬──────┘
                                                └── equal ────┘
                                                 BY CONSTRUCTION
                                              (not by effort, not by luck)
```

*(Indian format traditionally puts Liabilities & Equity on the left of the page and Assets on the
right — the reverse of how the equation reads. The side of the paper is a convention; which items
belong to which side is not.)*

**In action**

Watch it be unable to break. Take the Day 2 event — 4,00,000 spent on goods:

| | Left (Assets / uses) | Right (Sources) |
|---|---|---|
| Day 1 | Cash 20,00,000 | Capital 20,00,000 |
| Day 2: buy goods 4,00,000 | Cash **down** 4,00,000, goods **up** 4,00,000 | **unchanged** |
| Net effect on totals | **no change** | **no change** |

Nothing balanced itself. Nothing needed to. The transaction **re-shaped the left side and never
touched the right**, so the totals could not possibly separate.

Now Day 4 — machinery 3,00,000 on credit:

| | Left (Assets) | Right (Sources) |
|---|---|---|
| Day 4 | Machinery **up** 3,00,000 | Arjun & Co. **up** 3,00,000 |

Both sides moved **by the same amount, at the same moment**, because they are the same event
described twice: *what we got* and *who funded it*. The final sheet reads **22,10,000 = 22,10,000**
not as an achievement, but as an inevitability.

**Where it bites**

The bite: **treating "doesn't balance" as a balance-sheet problem.**

> **Wrong:** "My Balance Sheet is off by 4,00,000. I'll adjust something on the asset side until
> the totals match."
>
> **Right:** "My Balance Sheet cannot be off. If the totals differ, the error is **upstream** — a
> wrong journal entry, a mis-posted ledger, or an item routed to the wrong statement. The gap of
> 4,00,000 is a **symptom pointing at Purchases**, which I have wrongly parked on the asset side.
> Fix the routing; the sheet will balance on its own."

**The exact point it bites:** the moment you try to **make** it balance. Plugging a figure to force
the totals is not accounting — it is vandalism with a calculator. It destroys the one property that
made the sheet worth reading. A forced balance sheet balances and means **nothing**.

**Your turn**

1. A business's month produced: cash Rs 19,10,000 held at month end; a machine Rs 3,00,000 still on
   the floor; goods bought for Rs 4,00,000 and all of them sold during the month; Rs 2,00,000 still
   owed to a supplier; and an owner's claim of Rs 20,10,000. Someone preparing the balance sheet to
   show a bank lists the assets as Cash 19,10,000 + Machinery 3,00,000 + Purchases 4,00,000 =
   Rs 26,10,000, against sources of Rs 22,10,000 — a gap of Rs 4,00,000 — and starts hunting for an
   addition mistake. Without recomputing anything, say why no addition mistake exists, name the real
   error, and explain how the *size* of the gap named it.

<details><summary>Answer</summary>

No addition mistake exists, because the two sides were never independent quantities — they are the same value described twice (what it is, and where it came from), so they cannot drift apart on their own. The real error is routing: the Rs 4,00,000 of goods was sold and is no longer controlled, so it is a consumed expense belonging to the income statement, not an asset. The gap is *exactly* Rs 4,00,000 because a single mis-routed line shifts one side by precisely its own amount — the size of the gap names the culprit. Assets are Cash Rs 19,10,000 + Machinery Rs 3,00,000 = Rs 22,10,000, and the sheet balances on its own once the routing is fixed.

</details>

2. A bank officer says: "Just send me the balance sheet — it's the only statement I can actually
   check, because it either balances or it doesn't, so a balanced one proves the books are right."
   You know that in the same business's books, if a Rs 50,000 commission payment had never been
   recorded at all, the trial balance would still have totalled Rs 26,60,000 on both sides — not off
   by one rupee. Use that fact to attack the officer's claim, and state what "balance" actually
   proves.

<details><summary>Answer</summary>

The claim is false. Balancing is not a correctness check, because the two sides were never independent — the sheet balances by construction, not by being right. The omitted commission proves it: a whole entry vanishes, the books are wrong, and the totals stay identical at Rs 26,60,000 both sides, because dropping a complete entry removes one debit and one credit together. A balance sheet built from wrong-but-balanced books balances just as smugly. "Balance" proves only **equal** — never *correct*, never *complete*.

</details>

---

## G7 — Building both statements from a trial balance                     [EXT — not in your workbook]

**Definition**

This is the answer to **"how does the format work?"** — the routing rule.

> **Every line on the trial balance goes to exactly one statement. Exactly one. Never both, never
> neither.**

That's the whole mechanism. There is no judgement call and no third pile.

| TB line's account type | Goes to | Because it is… |
|---|---|---|
| **Revenue** (Sales) | **Income Statement** | **equity in motion** — it measures **change** |
| **Expense** (Purchases, Commission) | **Income Statement** | **equity in motion** — it measures **change** |
| **Asset** (Cash, Machinery) | **Balance Sheet** | a **stock** — it measures **position** |
| **Liability** (Arjun & Co.) | **Balance Sheet** | a **stock** — it measures **position** |
| **Capital / Equity** | **Balance Sheet** | a **stock** — it measures **position** |

**Equity in motion** is the key phrase. Revenue and expense accounts are not a separate species
from equity — they are equity **while it is moving**. Sales pushes the owner's claim up. Commission
pushes it down. At period end, we stop the film, add up all that motion, and call the net figure
**net profit**.

**Why the format looks like this**

Because the trial balance already contains **both species of account, mixed together**, and nobody
sorted them.

Look at Stage 3: Cash sits above Purchases. One is a stock, one is a flow. They are lined up in the
same column because the TB only cares about debit vs credit — it has no opinion about *kind*.

The two statements are what you get when you **finally sort by kind**:

- All the **motion** accounts → one page → net it off → **net profit**.
- All the **position** accounts → another page → set uses against sources → **A = L + E**.

And then the crucial join:

> **The net profit from the Income Statement lands on the Balance Sheet as an addition to Capital.**

That is not a convention. It is forced. Profit **is** the growth in the owner's claim — so once
you've measured it on one page, it must appear as a bigger claim on the other. **The two statements
are joined at that single number.** This is the most important structural fact about them.

**The format**

```
                    ┌──────────────────────────────────┐
                    │      TRIAL BALANCE 30 Jun        │
                    │      26,60,000 = 26,60,000       │
                    ├──────────────────────────────────┤
                    │ Cash            19,10,000  Dr    │──┐
                    │ Purchases        4,00,000  Dr    │─┐│
                    │ Machinery        3,00,000  Dr    │─┼┤
                    │ Commission         50,000  Dr    │─┤│
                    │ Capital         20,00,000  Cr    │─┼┤
                    │ Sales            4,60,000  Cr    │─┤│
                    │ Arjun & Co.      2,00,000  Cr    │─┼┘
                    └──────────────────────────────────┘ │
                                                         │
        ┌────────────── SORT BY KIND ───────────────────┘
        │                                          │
        ▼ motion (revenue + expense)               ▼ position (A / L / E)
 ┌───────────────────────────┐            ┌──────────────────────────────┐
 │   INCOME STATEMENT        │            │       BALANCE SHEET          │
 │   for 1–30 June 2024      │            │      as at 30 June 2024      │
 ├───────────────────────────┤            ├──────────────┬───────────────┤
 │ Sales           4,60,000  │            │ Arjun & Co.  │ Cash          │
 │ Less: Purchases(4,00,000) │            │    2,00,000  │   19,10,000   │
 │ Gross Profit      60,000  │            │              │               │
 │ Less: Commission (50,000) │            │ Capital      │ Machinery     │
 │                 ───────── │            │   20,00,000  │    3,00,000   │
 │ NET PROFIT        10,000  │            │ Add: Profit  │               │
 │                 ═════════ │            │      10,000  │               │
 └────────┬──────────────────┘            │   ─────────  │               │
          │                               │   20,10,000  │               │
          │                               ├──────────────┼───────────────┤
          │   THE JOIN — one number       │ TOT 22,10,000│ TOT 22,10,000 │
          └───── 10,000 ─────────────────▶└──────────────┴───────────────┘
                                                  ▲
                                          lands INSIDE Capital
```

**In action**

Route the spine's TB, line by line. Seven lines, seven decisions, zero judgement calls:

| TB line | Amount | Type | Statement | Where it lands |
|---|---|---|---|---|
| Cash A/C | 19,10,000 Dr | Asset | **Balance Sheet** | Assets side |
| Purchases A/C | 4,00,000 Dr | Expense | **Income Statement** | Cost of goods sold |
| Machinery A/C | 3,00,000 Dr | Asset | **Balance Sheet** | Assets side |
| Commission A/C | 50,000 Dr | Expense | **Income Statement** | Below gross profit |
| Capital A/C | 20,00,000 Cr | Equity | **Balance Sheet** | Sources side |
| Sales A/C | 4,60,000 Cr | Revenue | **Income Statement** | Top line |
| Arjun & Co. A/C | 2,00,000 Cr | Liability | **Balance Sheet** | Sources side |

**Every line used exactly once.** Three went left, four went right. Nothing was duplicated and
nothing was dropped.

Then the join fires: the Income Statement's **10,000** appears on the Balance Sheet as
*Add: Net Profit 10,000*, lifting Capital from 20,00,000 to **20,10,000** — and the sheet closes at
**22,10,000 = 22,10,000**.

Trace the 10,000 with your finger. It is manufactured on one page and consumed on the other. That
one number is the seam between the video and the photograph.

**Where it bites**

The bite: **an item appears on both statements, or on neither.**

> **Wrong #1 — double-counting:** "Sales 4,60,000 was received in cash, so I'll show Sales on the
> Income Statement **and** the 4,60,000 among assets."
>
> **Right:** the cash from that sale is **already inside** Cash 19,10,000. Listing it again invents
> 4,60,000 out of nothing. **One TB line → one statement.** Sales the *account* goes to the Income
> Statement; the *cash it brought in* is not a second line, it is part of the Cash balance the
> ledger already computed.

> **Wrong #2 — dropping the join:** routing all seven lines perfectly, then writing Capital as
> 20,00,000 on the Balance Sheet.
>
> **Right:** Capital is **20,10,000**. Leave out the join and the sheet is short by exactly
> 10,000 — the profit figure, sitting on the other page with nowhere to go.

**The exact point it bites:** when you think of the two statements as **two separate exercises**.
They are one exercise with one sort and one join. If your Balance Sheet is out by an amount that
happens to equal your net profit, you have not made an arithmetic error — you have **forgotten to
connect the two statements.** The size of the gap tells you which mistake you made.

**Your turn**

1. A business's books close with these seven balances, and the month's net profit works out to
   Rs 10,000:

   | Account | Debit | Credit |
   |---|---|---|
   | Cash | 19,10,000 | |
   | Purchases (all goods sold) | 4,00,000 | |
   | Machinery (still owned) | 3,00,000 | |
   | Commission | 50,000 | |
   | Capital (owner put in) | | 20,00,000 |
   | Sales | | 4,60,000 |
   | Supplier (still owed) | | 2,00,000 |

   Someone preparing the balance sheet for a lender sends every one of these seven lines to the
   right statement — assets and claims one way, revenue and expenses the other — but writes the
   owner's capital as Rs 20,00,000. State the exact total of each side of their sheet, name the size
   of the gap, and explain why that specific gap is a **diagnosis** and not merely a symptom.

<details><summary>Answer</summary>

Assets Rs 22,10,000 (Cash 19,10,000 + Machinery 3,00,000). Sources Rs 22,00,000 (supplier 2,00,000 + capital 20,00,000). Gap = Rs 10,000. It is a diagnosis because Rs 10,000 *is* the net profit: a gap equal to net profit can only mean the join was dropped — the profit was measured on one page and never landed on the other as an addition to capital, which should read Rs 20,10,000. No arithmetic slip is implicated, and none should be hunted.

</details>

2. In one week a business spends Rs 4,00,000 buying goods (all of which it sells the following day)
   and Rs 3,00,000 buying a machine on credit (still on the shop floor at month end). Both are debit
   balances, both were created by spending, both sit in the same column of the same trial balance —
   and they go to **different statements**. State the single test that separates them, apply it out
   loud to each, and say why the word "purchased" decides nothing.

<details><summary>Answer</summary>

The test: *do you still control the resource at the instant of the balance sheet?* Machine — yes, still on the floor at month end → asset → balance sheet. Goods — no, sold and gone, nothing left on the shelf → consumed → expense → income statement, as cost of goods sold. The verb "purchased" is identical in both cases and carries no information; ordinary English says buying gives you a thing, but accounting asks only about control at the instant, never about how the thing was acquired.

</details>

---

## G8 — Profit ≠ cash                     [EXT — not in your workbook]   ★ HIGH-YIELD

**Definition**

> **This is the most consequential idea in the topic. If you take one thing from Act 7, take this.**

**Profit and cash are different things. They are measured differently, they move differently, and
neither one explains the other.**

- **Profit** = revenue earned **minus** expenses consumed. A **flow of value**.
- **Cash** = the money you actually hold. A **stock of money**.

They are related the way *distance travelled* is related to *fuel in the tank*. Connected, yes.
Same thing, absolutely not. You can travel far on fumes, and you can sit still with a full tank.

**Why the format looks like this**

Because **money arrives for reasons that have nothing to do with earning it**, and **value is
earned in ways that don't move money.**

Cash goes up when:

| Cash goes UP because… | Is it profit? |
|---|---|
| a customer pays you | **yes** — earned |
| the **owner puts money in** | **no** — supplied, not earned |
| you borrow from a bank | **no** — that's someone else's money |
| you sell a machine | **no** — you swapped an asset for cash |

Only the first line is the business succeeding. The rest is money **arriving**. That's why one
statement cannot do both jobs — and why cash flow (G6) has to be a **third** statement.

**The format**

```
   ┌────────────────────────────────┐     ┌────────────────────────────────┐
   │       NET PROFIT               │     │          CASH                  │
   │        10,000                  │     │       19,10,000                │
   ├────────────────────────────────┤     ├────────────────────────────────┤
   │ measures: EARNING              │     │ measures: HOLDING              │
   │ species: FLOW (a video)        │     │ species: STOCK (a photograph)  │
   │ lives on: Income Statement     │     │ lives on: Balance Sheet        │
   │ counts: Sales − Purchases      │     │ counts: every rupee that moved │
   │         − Commission           │     │         in or out, any reason  │
   └────────────────────────────────┘     └────────────────────────────────┘
                    │                                     │
                    └──── NEITHER EXPLAINS THE OTHER ─────┘

              10,000 ────╳────▶ 19,10,000     ← there is no route between them
```

**In action**

Straight from the spine, both figures verified:

| | Figure |
|---|---|
| **Net profit** (Stage 4) | **10,000** |
| **Cash** (Stage 5 / Stage 3) | **19,10,000** |

Two honest numbers. Same business. Same June. **A ratio of roughly 1 to 191.**

**Neither number explains the other:**

- **Why is cash so enormous?** Because **20,00,000 was put in by the OWNER** — supplied, not
  earned. That money walked in on Day 1 and never had anything to do with trading. Strip out the
  owner's contribution and the cash story collapses.
- **Why is profit so tiny?** Because **operating barely cleared its costs.** The goods made 60,000
  of gross margin and commission took 50,000 of it. What the business actually *earned* by trading,
  all month, was **10,000**.

So the business looks rich and trades thin. **Cash is a story about funding. Profit is a story
about performance.** Reading either as the other gets you the wrong business.

**Why this matters outside the exam — the real-world consequence:**

> **A profitable business can die of cash starvation.**

Here is how, and it is the **most common way a growing business goes under**:

```
   You sell hard. On credit.
        │
        ▼
   Income Statement: revenue soaring, profit superb.  ✓ You look successful.
        │
        ▼
   But the cash is in your CUSTOMERS' bank accounts, not yours.
        │
        ▼
   Meanwhile you have ALREADY paid for the goods, the rent, the staff.
        │
        ▼
   Friday arrives. Payroll is due. You cannot make it.
        │
        ▼
   The business dies — while its Income Statement is the best it has ever been.
```

The Income Statement was never lying. It was answering a **different question** — and answering it
correctly. It is simply not the question *"can we pay people on Friday?"*

**This is precisely why G6 (cash flow) is a THIRD statement and not a footnote.** Three different
questions. Three different answers. No shortcuts between them.

**Where it bites**

> **Wrong:** "Net profit is Rs 10,000 but there's Rs 19,10,000 in the bank — I must have made an
> arithmetic error somewhere. Let me hunt for the missing 19,00,000."
>
> **Right:** "Both figures are correct and they are **supposed** to disagree. Cash 19,10,000 is
> mostly the owner's 20,00,000 contribution. Profit 10,000 is what **trading** produced. There is
> no error and there is no reconciliation to find, because these two figures were never claiming
> to be the same quantity."

> **Wrong:** "Profit is 10,000, so 10,000 of that cash is 'the profit money'."
>
> **Right:** Rupees are not labelled. There is no drawer with 10,000 of "profit cash" in it. The
> 10,000 exists on the Balance Sheet as **a bigger claim by the owner** (Capital 20,00,000 →
> 20,10,000), not as a physical pile.

**The exact point it bites:** the moment you feel the urge to **reconcile** 10,000 to 19,10,000 —
to find the arithmetic that turns one into the other. That urge assumes they are the same quantity
measured two ways. They are not. Nothing is missing.

**Your turn**

1. A business's first month runs like this: the owner puts in Rs 20,00,000 cash on day one; the
   business buys goods for Rs 4,00,000 and sells them for Rs 4,60,000 cash; it buys a Rs 3,00,000
   machine on credit and pays the supplier Rs 1,00,000; it pays Rs 50,000 commission. Month end: net
   profit **Rs 10,000**, cash **Rs 19,10,000**. The owner stares at both and says: "One of these is
   wrong — there's no arithmetic that turns 10,000 into 19,10,000, so I've lost Rs 19,00,000
   somewhere." First, settle whether anything is missing. Then run this counterfactual: the owner
   had put in nothing, and a bank had lent the business exactly Rs 20,00,000 on day one instead,
   every other event identical. State what happens to net profit, what happens to cash, and use the
   result to say what net profit is actually measuring.

<details><summary>Answer</summary>

Nothing is missing and there is no reconciliation to find — the two figures were never claiming to be the same quantity. Both are correct and are *supposed* to disagree: cash Rs 19,10,000 is mostly the owner's Rs 20,00,000, which was **supplied**, not earned; profit Rs 10,000 is what **trading** produced (goods made Rs 60,000 of margin, commission took Rs 50,000 of it). Under the bank-loan counterfactual: net profit is **unchanged at Rs 10,000**, and cash is **unchanged at Rs 19,10,000** — the same money arrived, just from a lender instead of an owner. Only the sources side of the balance sheet changes (a liability instead of capital). That invariance is the proof: net profit measures performance from trading alone and is completely blind to how the business was funded.

</details>

2. A trader wants you to lend him money. He shows you an income statement with a large net profit
   and says the business is therefore safe. You already know that in a comparable business, a net
   profit of Rs 10,000 sat alongside cash of Rs 19,10,000 — of which Rs 20,00,000 had simply been
   put in by the owner — and Rs 2,00,000 still owed to a supplier. Name the **two** questions you
   must ask the trader before agreeing, say which statement answers each, and explain why his profit
   figure cannot answer either.

<details><summary>Answer</summary>

(1) "Is the profit in cash, or in your customers' pockets — and where did the cash you do hold come from?" → the Cash Flow Statement, which sorts money by reason and would expose an inflow that is financing rather than earning. (2) "What do you owe, and when is it due?" → the Balance Sheet, which sets outsiders' claims against the resources actually held. Profit answers neither because it measures earning over a period — not money held at an instant, and not claims outstanding. A business can earn handsomely while holding nothing and owing everything; that is the ordinary way a growing, profitable business dies.

</details>

---

## G6 — Cash Flow                     [EXT — not in your workbook]

**Definition**

The **Cash Flow Statement** tracks **every rupee of actual money** that came in and went out over a
period, and tells you what's left.

It answers the third question — the blunt one:

> **Can we pay people on Friday?**

Not *did we earn* (that's the Income Statement). Not *what do we own* (that's the Balance Sheet).
**Can we physically hand over money when it is demanded.**

The Cash Flow Statement is a **FLOW** — a video, "for the period 1–30 June 2024" — but it films a
different subject. The Income Statement films **earning**. Cash Flow films **money moving**.

**Why the format looks like this**

Because the sentence *"cash went up by a lot"* is useless on its own. You need to know **why**, and
the reasons are not equally good news.

So the format sorts every cash movement into three buckets by **reason**:

| Bucket | Means | Sustainable? |
|---|---|---|
| **Operating** | cash from doing the actual job — selling, paying costs | **Yes.** This is the engine. It can run for ever. |
| **Investing** | cash spent on / received from long-term resources | Buying capacity. Necessary, not repeatable for ever. |
| **Financing** | cash from the owner or lenders, and repayments to them | **This is not earning.** It runs out, or must be repaid. |

That sorting **is** the point. A business whose cash comes from **Operating** is alive. A business
whose cash comes from **Financing** is being kept alive. The bottom-line cash figure looks
identical either way — only the buckets tell you which business you're holding.

**The format**

```
   ┌───────────────────────────────────────────────────────────┐
   │              CASH FLOW STATEMENT                          │
   │          for the PERIOD 1–30 June 2024                    │
   ├───────────────────────────────────────────────────────────┤
   │  Opening cash                                    XXXX     │
   │                                                           │
   │  OPERATING   ── cash from doing the job ──                │
   │      + from customers                            XXXX     │
   │      − to suppliers, running costs              (XXXX)    │
   │                                                           │
   │  INVESTING   ── cash for long-term resources ──           │
   │      − to buy machinery etc.                    (XXXX)    │
   │                                                           │
   │  FINANCING   ── cash from owner / lenders ──              │
   │      + owner's contribution                      XXXX     │
   │                                                 ───────   │
   │  CLOSING CASH                                    XXXX     │
   │                                                 ═══════   │
   │         └──▶ must equal the Cash figure on the Balance    │
   │              Sheet at the same instant                    │
   └───────────────────────────────────────────────────────────┘
```

**In action**

Every cash movement in June is already in the spine's **Cash A/C** ledger. Nothing new is being
computed here — the lines are simply **sorted by reason**:

| Bucket | Day | Movement | Amount | In / Out |
|---|---|---|---|---|
| **FINANCING** | Jun 1 | Owner's capital introduced | 20,00,000 | **IN** |
| **OPERATING** | Jun 2 | Paid for goods (Purchases) | 4,00,000 | OUT |
| **OPERATING** | Jun 3 | Received from customers (Sales) | 4,60,000 | **IN** |
| **INVESTING** | Jun 6 | Paid Arjun & Co. for machinery | 1,00,000 | OUT |
| **OPERATING** | Jun 7 | Commission paid | 50,000 | OUT |
| | | **CLOSING CASH, 30 June** | **19,10,000** | |

*(Deliberately not shown: bucket subtotals. The frozen spine does not carry them, and this sheet
does not manufacture figures. The individual lines and the closing balance are all spine-verified —
and the lines alone already make the point.)*

**Now read the buckets and the whole business becomes visible:**

- The **single largest cash inflow of the month — 20,00,000 — is FINANCING.** It is the owner's
  money. It is not the business earning anything.
- **Operating** produced one inflow of 4,60,000 against outflows of 4,00,000 and 50,000 — a real
  business, running thin.
- Strip out the financing line and the cash position is unrecognisable.

**The tie-back:** closing cash **19,10,000** is exactly the **Cash** figure on the Stage 5 Balance
Sheet as at 30 June. It must be. The video's last frame **is** the photograph.

- **Day 5 note:** the Rs 3,00,000 order placed with Saksham appears **nowhere** on this statement.
  No money moved. An order is not a transaction — nothing received, given, owed or paid. Cash Flow
  is the most literal of the three statements, and it is entirely deaf to intentions.

**Where it bites**

The bite: **reading the closing cash figure and skipping the buckets.**

> **Wrong:** "The business closed June with Rs 19,10,000 cash. Excellent — it's generating money."
>
> **Right:** "The business closed June with Rs 19,10,000 cash, of which the dominant source is
> **20,00,000 of FINANCING** — the owner's own money. Operating cleared very little. The bank
> balance is healthy; the **engine** is not proven. Those are different findings and only the
> buckets separate them."

**The exact point it bites:** treating cash as a **verdict** instead of a **balance**. A big cash
number is not an achievement — it is a fact with a cause, and the cause is the entire story. Two
businesses can both show 19,10,000. In one, customers paid it. In the other, the owner did. The
first is a business. The second is a bank account with ambitions.

**Your turn**

1. You can buy one of two businesses. Both closed the month holding exactly Rs 19,10,000 in cash,
   and both cash flow statements therefore end on the identical figure. The difference is one line.
   Business A's Rs 20,00,000 inflow sits in **Financing** — the owner put it in. Business B's
   Rs 20,00,000 inflow sits in **Operating** — customers paid it. State which you would rather buy,
   name the exact line that decides it, and explain why the closing cash figure is useless for
   telling them apart.

<details><summary>Answer</summary>

Business B. The deciding line is the bucket the Rs 20,00,000 sits in. In B it is Operating — customers paid it, which is repeatable and proves an engine that can run forever. In A it is Financing — the owner paid it, which is finite and proves only funding, not earning. The closing figure cannot tell them apart because Rs 19,10,000 is a fact with a cause, and the bottom line strips the cause out: only the buckets say whether you are buying a business or a bank account with ambitions.

</details>

2. A business places a firm order with a supplier for Rs 3,00,000 of goods. The goods have not
   arrived, nothing has been paid, and no invoice exists — only the order. Days earlier the same
   business bought a Rs 3,00,000 machine on credit, which *is* recorded, so the two look
   deceptively alike. The order appears on **none** of the three statements. Take each statement in
   turn: state the test that statement applies, and why the order fails it.

<details><summary>Answer</summary>

Income statement — *has anything been earned or consumed?* No: nothing sold, nothing used up. Balance sheet — *is a resource controlled, or a claim owed, at the instant of the photograph?* No: no goods received, and an order creates no obligation to pay, so there is no liability. Cash flow — *did money move?* No: nothing received, given, owed or paid. The machine differs on exactly one point — it was received and the debt is real. An order is an intention; the statements are deaf to intentions and it fails all three tests.

</details>

---

---

# ACT 8 — The rules that stop you lying.

## A1 — Accounting defined                     [SOURCED p.2]

**Definition**

Accounting is the **identifying, recording, classifying, summarising and communicating** of financial
information so that someone can make a decision with it.

Read that chain as five verbs in order — it is the whole machine you just built:

```
IDENTIFY  ->  RECORD   ->  CLASSIFY  ->  SUMMARISE  ->  COMMUNICATE
"is this a    journal      ledger       trial balance   income statement
transaction?"                                           + balance sheet
```

- **Identify** — Day 5 (an order placed with Saksham) gets filtered out HERE, before any book opens.
- **Record** — the journal, in date order, everything that survived the filter.
- **Classify** — the ledger, gathering every Cash line into one Cash A/C.
- **Summarise** — the trial balance, one line per account.
- **Communicate** — the two statements someone actually reads.

**The last verb is the point.** Books that no one can read are not accounting. Every rule in this
section exists to protect the last verb from the first four.

**In action**

The business's first week runs the full chain:

| Verb | What happened | Figure |
|---|---|---|
| Identify | 7 events in, 6 transactions out (Day 5 rejected) | — |
| Record | journal totals | 28,10,000 = 28,10,000 |
| Classify | 7 ledger accounts opened | — |
| Summarise | trial balance | 26,60,000 = 26,60,000 |
| Communicate | net profit / balance sheet total | 10,000 / 22,10,000 |

**Your turn**

1. Accounting is the chain **identify → record → classify → summarise → communicate**. A business's
first month is written up correctly. Its journal — every debit and credit line, with the cash account
appearing five separate times — totals Rs 28,10,000 on each side. The trial balance drawn from the
same books — one closing figure per account, cash appearing once at Rs 19,10,000 — totals Rs
26,60,000 on each side. The owner suspects an error. Name the verb in the chain that causes the two
numbers to differ, and state exactly what each total counts.

<details><summary>Answer</summary>

No error. **Classify** (the ledger) is what separates them: the journal totals *movements* — every
line written, cash five times over — while the trial balance totals *balances*, one closing figure
per account, cash once at 19,10,000. Two different things counted, so two different totals.

</details>

2. Accounting is the chain **identify → record → classify → summarise → communicate**, and the first
verb asks "is this even a transaction?" A business places an order for goods worth Rs 3,00,000 with a
supplier — nothing has shipped, nothing is owed, no cash has moved. A bookkeeper journalises it
anyway as a full double entry, then posts, balances and summarises flawlessly. The trial balance
comes out equal on both sides. Which verb was mis-performed, and what does the clean balancing tell
you about which verb the trial balance protects?

<details><summary>Answer</summary>

**Identify** was mis-performed, and the trial balance still balances — a fictitious event entered as
an equal debit and credit disturbs nothing. The trial balance protects **none** of the identify verb;
it only ever checks that Σ debits = Σ credits, which is a question about arithmetic, not about
whether anything happened.

</details>

---

## A2 — Accounting vs Accountancy vs Book-keeping                     [SOURCED p.2]

**Definition**

Three words, three widths. They are **not** synonyms, and the exam asks you to rank them.

- **Book-keeping** — the *recording* of transactions. Narrowest. Mechanical, rule-driven, ends when
  the entry is written.
- **Accounting** — book-keeping **plus** classifying, summarising, interpreting and communicating.
- **Accountancy** — the whole **profession and body of knowledge**: the concepts, the conventions,
  the standards, the practice. Widest.

```
+-------------------------------------------------+
|                  ACCOUNTANCY                    |   the field / the profession
|   +-----------------------------------------+   |
|   |              ACCOUNTING                 |   |   the process, end to end
|   |    +-------------------------+          |   |
|   |    |     BOOK-KEEPING        |          |   |   the recording only
|   |    +-------------------------+          |   |
|   +-----------------------------------------+   |
+-------------------------------------------------+
```

**In action**

| Task in the first week | Which word |
|---|---|
| Writing "Jun 4 Machinery A/C Dr. 3,00,000 / To Arjun & Co. 3,00,000" | Book-keeping |
| Deciding Day 5 gets **no entry** | Accounting |
| Reading net profit 10,000 against cash 19,10,000 and saying what it means | Accounting |
| The rule that says a loss is booked and a hoped-for gain is not | Accountancy |

**Where it bites**

The confusion: "book-keeping ends where accounting begins."

- **Wrong:** book-keeping and accounting are two separate stages laid end to end.
- **Right:** book-keeping is *contained inside* accounting. The journal entry is simultaneously a
  book-keeping act and the second verb of accounting. Containment, not sequence.

**Your turn**

1. **Book-keeping** is the recording of transactions and nothing else. **Accounting** is book-keeping
plus classifying, summarising, interpreting and communicating. A business's first month contains six
transactions. The person hired to keep the books journalises all six correctly, closes the book and
hands it over. The owner asks "did we make money this month?" and finds no one can answer from what
was produced. Name what was performed, name what was not, and name the specific output that is
missing.

<details><summary>Answer</summary>

**Book-keeping was performed** — the recording, done correctly. **Accounting was not** — no
classifying, summarising, interpreting or communicating. The missing output is the **income
statement**, which is where net profit of 10,000 would have appeared. Books nobody can read are not
accounting.

</details>

2. **Book-keeping** is defined as the recording of transactions. **Accounting** is book-keeping plus
classifying, summarising, interpreting and communicating. A business places an order for goods worth
Rs 3,00,000 with a supplier; nothing has shipped, nothing is owed, no cash has moved. Someone decides
this gets no entry at all. Using the definitions above, argue which of the two words that decision
belongs to.

<details><summary>Answer</summary>

**Accounting.** Book-keeping is the recording of transactions — it can only begin once you already
have one. Deciding whether the order *is* a transaction happens before recording and determines
whether any recording occurs at all; it is a judgement about identification, which sits in
accounting. Note the shape: book-keeping is *contained inside* accounting, not a stage that ends
where accounting starts.

</details>

---

## B1 — Relevance of accountancy: the five stated reasons                     [SOURCED p.6]

**Definition**

Why the subject exists at all. The workbook states **five** reasons. Learn them as five different
failures that accounting prevents.

| # | Reason | The failure without it |
|---|---|---|
| 1 | **Human memory is limited** | You cannot hold 6 transactions, let alone 6,000 |
| 2 | **Legal compliance** | Tax and company law demand records; no records, no defence |
| 3 | **Ascertaining performance** | "Did we make money?" has no answer |
| 4 | **Supporting economic decisions** | Lenders, owners, suppliers decide blind |
| 5 | **Valuing the business** | Nobody can price what nobody can measure |

**Reason 1 is the origin of everything else.** Books are a memory prosthetic first. The other four
are what becomes possible once memory stops being the constraint.

**In action**

Reason 1, made concrete. On **Jun 6** the business pays Arjun & Co. 1,00,000. To know what is still
owed you must recall Jun 4 (3,00,000 credit purchase) — two days and four entries earlier.

```
memory:  "we owe Arjun... something?"          -> unusable
ledger:  Arjun & Co. A/C, closing balance      -> 2,00,000 credit
```

Reason 3, made concrete: **net profit 10,000** for 1-30 June. Reason 5, made concrete: **balance
sheet total 22,10,000**. Neither number is available to memory. Both are available to books.

**Your turn**

1. Accountancy is said to exist for five reasons: **human memory is limited; legal compliance;
ascertaining performance; supporting economic decisions; valuing the business.** A business's first
month produces two headline figures — a net profit of **Rs 10,000** for the month, and a balance
sheet totalling **Rs 22,10,000**, of which **Rs 2,00,000** is still owed to a supplier. A bank
deciding whether to advance funds and the owner deciding whether to keep trading each fix on a
different figure. Say which figure each takes, name the reason it serves, and explain why they
diverge.

<details><summary>Answer</summary>

The **bank takes the balance sheet — 22,10,000, and the 2,00,000 already owed** (reason 5, valuing
the business): it shows what backs repayment at an instant. The **owner takes net profit 10,000**
(reason 3, ascertaining performance): it is the only evidence the operation earns over time. They
diverge because the two figures answer different questions — **position versus performance** — and
neither can be read off the other.

</details>

2. Accountancy is said to exist for five reasons: **human memory is limited; legal compliance;
ascertaining performance; supporting economic decisions; valuing the business.** Consider a business
that does exactly one transaction a year — a single annual licence sale, invoiced and settled in one
day. Which of the five reasons still apply to it, and which collapses? Justify each verdict.

<details><summary>Answer</summary>

**Still apply:** legal compliance (tax and company law demand records at any volume), ascertaining
performance, supporting economic decisions, and valuing the business — none of these depends on how
many transactions there are. **Collapses:** human memory is limited — one event a year is perfectly
holdable in a head, so the memory prosthetic is not needed. This shows memory is the *origin* of
book-keeping but not its *justification*; the other four survive on their own.

</details>

---

## A15 — Profit                     [SOURCED p.4]

**Definition**

Profit is **what income exceeds expenses by, over a stated period.** Two words in that sentence do
all the work.

- **Exceeds** — profit is a *difference*, never a balance you can point at.
- **Over a stated period** — with no period, the word is meaningless (see **B4**).

Two profits, not one:

| Layer | Formula | First week |
|---|---|---|
| **Gross Profit** | Sales − Cost of goods sold | 4,60,000 − 4,00,000 = **60,000** |
| **Net Profit** | Gross Profit − other expenses | 60,000 − 50,000 = **10,000** |

**In action**

```
Sales                          4,60,000
Less: Cost of goods sold      (4,00,000)
                              ----------
GROSS PROFIT                     60,000
Less: Commission                (50,000)
                              ----------
NET PROFIT                       10,000
```

> **`[INFERRED]` — say this out loud:** the workbook gives **no closing stock**, so this assumes
> **all goods purchased were sold**. Real businesses almost never look like this.

**Machinery (3,00,000) is nowhere in this statement.** It was acquired, not consumed.

**Where it bites**

The confusion: profit is money.

- **Wrong:** "profit is 10,000, so there's 10,000 in the till."
- **Right:** profit **10,000**, cash **19,10,000**. Neither number explains the other. Cash is high
  because 20,00,000 was *supplied by the owner*, not earned. Profit measures performance; cash
  measures a resource. They answer different questions and are computed from different lines.

**Your turn**

1. In one month a business sells goods for **Rs 4,60,000**. The goods it sold had cost it **Rs
4,00,000** to buy. During the same month it also pays **Rs 50,000** of commission to an agent. Gross
profit comes to **Rs 60,000** and net profit to **Rs 10,000** — a gap of 50,000. Name the single line
that creates the gap, and explain why it sits *below* gross profit rather than inside cost of goods
sold.

<details><summary>Answer</summary>

The **commission, 50,000**. It sits below gross profit because it is not a cost of the goods
themselves — cost of goods sold contains only what was bought in order to be sold (the 4,00,000).
Gross profit exists to isolate the **trading margin**; commission is an operating expense of running
the business, so it is charged after that margin has been struck.

</details>

2. A business ends its first month holding **Rs 19,10,000** in cash and reports a net profit of **Rs
10,000** for the month. The cash is large mainly because the owner put **Rs 20,00,000** into the
business at the start — money supplied, not earned. A supplier who is owed **Rs 2,00,000** and a
prospective partner considering buying in each fix on a different one of those two figures. Construct
both arguments, and say why "profit 10,000 means there's 10,000 in the till" is wrong.

<details><summary>Answer</summary>

**Supplier:** cares about **cash 19,10,000** — it is the resource that will actually settle the
2,00,000 owed. **Partner:** cares about **profit 10,000** — it is the only evidence the operation
earns anything, and it is what a future stake would be a share of. The "10,000 in the till" reading
is wrong because profit measures **performance over a period** and cash measures a **resource at an
instant**; here the cash is high only because 20,00,000 was supplied by the owner, so neither number
explains the other.

</details>

---

## B10 — Concept vs Convention                     [SOURCED pp.6-7]

**Definition**

The distinction the exam loves, in two words:

- **Concepts are POSTULATES** — the workbook's own word (p.6). A postulate is a **basic assumption
  the system is built ON.** You do not prove it. You assume it, and everything else stands on it.
- **Conventions are TRADITIONS** — customs that guide **how accountants actually prepare** the
  statements. They are practice, agreed over time, not foundation.

```
                CONVENTIONS  ->  Consistency, Full Disclosure, Conservatism, Materiality
                (traditions)     "how we prepare the statements"
   =========================================================================
                CONCEPTS     ->  Business Entity, Going Concern, Accounting Period,
                (postulates)     Dual Aspect, Money Measurement, Cost, Matching...
                                 "what the system assumes is true"
   =========================================================================
```

**Concepts are foundations. Conventions are practices.** Remove a concept and the statements stop
*meaning* anything. Remove a convention and the statements still mean something — they just stop
being *comparable or trustworthy.*

**In action**

| Item | Concept or Convention | Why |
|---|---|---|
| **Going Concern** — assume the business continues | **Concept** | An assumption you cannot prove; machinery 3,00,000 is valued on it |
| **Accounting Period** — cut time into 1-30 June | **Concept** | An assumption imposed on continuous life |
| **Consistency** — same method next month | **Convention** | A tradition about preparation |
| **Full Disclosure** — state the no-closing-stock assumption | **Convention** | A tradition about presentation |
| **Conservatism** — book Day 5 as nothing | **Convention** | A tradition about judgement |
| **Materiality** — don't chase a rupee | **Convention** | A tradition about effort |

**Where it bites**

The confusion: "concepts are the important ones, conventions are the optional ones."

- **Wrong:** conventions are soft, so you may ignore them.
- **Right:** the split is about **position, not importance.** A concept is *underneath*
  (unprovable assumption). A convention is *on top* (agreed practice). Ignoring Full Disclosure is
  not a lesser sin than ignoring Going Concern — it is a different *kind* of sin.

**Your turn**

1. A **concept** is a *postulate* — a basic assumption the system is built on, which you do not prove
but assume, and on which everything else stands. A **convention** is a *tradition* — a custom, agreed
over time, guiding how accountants actually prepare the statements. **Business Entity** — the rule
that a business's affairs are kept separate from its owner's, so that money the owner puts in becomes
the business's capital and a debt of the business back to him — is classified as a concept, not a
convention. Using only the meaning of "postulate", explain why it *cannot* be a convention.

<details><summary>Answer</summary>

Because it is assumed **before any entry can be written**: you cannot record a single transaction
until you have already decided whose books these are, and there is no way to prove the separation —
you posit it. A convention is a preparation habit that could defensibly have been done another way
and the statements would still mean something. Remove Business Entity and nothing is recordable at
all. Foundation, not practice — the split is about **position, not importance**.

</details>

2. A business carries machinery it bought for **Rs 3,00,000** at that cost on its balance sheet. Two
rules act on that one line: the assumption that the business will keep operating for the foreseeable
future (an unprovable postulate), and the tradition that potential losses are recognised while gains
are never anticipated — and that no arbitrary write-downs are made either. Explain how one assumption
and one tradition can both act on the same number without one overruling the other.

<details><summary>Answer</summary>

They act at different **levels**. The going-concern assumption supplies the **basis**: cost, because
there is assumed to be a future in which the machine gets used. The conservatism tradition polices
the **judgement exercised within that basis**: no anticipating gains, and no writing the 3,00,000
down to 2,00,000 "to be safe" either. One sets the frame; the other governs behaviour inside it. Both
land on the same 3,00,000 without conflict.

</details>

---

## B3 — Going Concern                     [SOURCED p.6]

**Definition**

**Going Concern** = you assume the business will **keep operating for the foreseeable future.** It
will not be shut down or sold off next week.

The name is literal: a business that is *going* — still moving — is a *concern* still in operation.

**This single assumption decides what everything is WORTH.** Machinery of **3,00,000** is:

```
   +----------------------------+        +-----------------------------+
   |  GOING CONCERN = TRUE      |        |  GOING CONCERN = FALSE      |
   |  worth years of USE        |        |  worth whatever a scrap     |
   |  -> carry at 3,00,000      |        |  dealer pays TODAY          |
   |  -> spread cost over life  |        |  -> carry at break-up value |
   +----------------------------+        +-----------------------------+
            ^                                        ^
            |                                        |
            +----- the ONLY thing choosing ----------+
                   between them is the ASSUMPTION
```

Two wildly different numbers for one identical machine. Nothing about the metal changed. The
assumption changed.

**What lie does this stop?** **Valuing a dying business as if it were healthy.** A company weeks
from collapse can show assets priced for decades of use — and the balance sheet looks fine right up
until nobody can be paid. Going Concern is the assumption you must *state* so that a reader can
challenge it.

**In action**

The 30 June balance sheet carries **Machinery 3,00,000** and totals **22,10,000**.

- That 3,00,000 is **not** "what the machine would fetch today."
- It is **cost**, carried because the business is assumed to be continuing and will *use* the machine.
- Withdraw the assumption and the asset side must be rebuilt on break-up values — and the total
  22,10,000 loses its meaning.

**Where it bites**

The confusion: "going concern means the business is definitely fine."

- **Wrong:** the accounts assume going concern, therefore the business is safe.
- **Right:** going concern is an **assumption made in order to value things**, not a verdict on
  health. It is an input to the statements, not a conclusion from them. Reading it backwards is
  exactly the lie it was written to stop.

**Your turn**

1. A business's balance sheet at 30 June totals **Rs 22,10,000** on each side. Its assets are cash
**Rs 19,10,000** and machinery **Rs 3,00,000**, the machinery carried at what it cost. Against them
sit **Rs 2,00,000** owed to a supplier and the owner's capital of **Rs 20,10,000** (Rs 20,00,000 put
in, plus the month's Rs 10,000 profit). On 30 June the owner announces that the business will close
on 1 July and everything will be sold off. Name every line whose **basis** is now wrong, state the
new basis each would need, and say what happens to the 22,10,000 total.

<details><summary>Answer</summary>

**Machinery 3,00,000** — basis was cost, justified only by an assumed future of use; it must become
**break-up / net realisable value**, whatever a buyer pays now. **Capital 20,10,000** — it is the
residual, so it absorbs the revaluation. **Cash 19,10,000** is unaffected (already at realisable
value) and the **supplier's 2,00,000** remains payable. The **22,10,000 total loses its meaning as
stated** — it was built on an assumption that has been withdrawn.

</details>

2. A business holds cash of **Rs 19,10,000** and machinery costing **Rs 3,00,000**. If the assumption
that the business will keep operating for the foreseeable future is withdrawn, the cash figure does
not move at all while the machinery figure may change beyond recognition. Explain what property of an
asset determines how exposed it is to that assumption — and say why "the accounts assume it, so the
business must be fine" reads the assumption backwards.

<details><summary>Answer</summary>

Exposure is determined by **how much of the asset's worth is stored in future use rather than present
realisability**. Cash is already realised — worth the same in use or in liquidation. The machinery's
3,00,000 is a **cost awaiting consumption over a life**; remove the life and only resale price
remains. The backwards reading fails because going concern is an **assumption made in order to value
things** — an input to the statements, not a verdict on health drawn from them.

</details>

---

## A11 — Depreciation                     [SOURCED p.2]

**Definition**

**Depreciation** = spreading a fixed asset's cost **over its useful life**, instead of dumping the
whole cost into the period it was bought.

**This hangs directly off Going Concern.** Read the definition again — it contains the words
*useful life ahead.* Those words only mean something if you have already assumed there IS a future
in which the asset gets used.

```
  GOING CONCERN (B3)   ->   "there is a future"
          |
          v
  the asset has a USEFUL LIFE
          |
          v
  DEPRECIATION (A11)   ->   spread the cost across that life
```

Kill Going Concern and depreciation becomes incoherent — you cannot spread a cost across a life that
you are simultaneously assuming does not exist.

**Why it exists — the lie underneath:** machinery bought for 3,00,000 is not consumed in the month
it is bought. Charging all 3,00,000 to June would crush June's profit and gift every later month a
free machine. Depreciation is the fix.

**In action**

Follow the machinery through the first week:

| Where | Machinery treatment | Reason |
|---|---|---|
| Jun 4 journal | Machinery A/C **Dr.** 3,00,000 | An asset was acquired, not an expense incurred |
| Ledger | closing **3,00,000 debit** | Still controlled |
| Trial balance | debit **3,00,000** | Still an asset |
| **Income statement** | **absent** | *"it wasn't consumed, it was acquired"* |
| Balance sheet | asset **3,00,000** | Carried at cost |

**The test that put it there (from Day 4 vs Day 7):** *do you still control a resource afterward?*

- Machinery 3,00,000 → **yes** → asset → the cost waits, to be released over the life.
- Commission 50,000 → **no** → expense → the cost hits net profit **10,000** now.

Depreciation is the mechanism that eventually releases the waiting cost — a little at a time, into
each period that actually got the use.

**Where it bites**

The confusion: depreciation is a fall in market value.

- **Wrong:** "the machine is worth less now, so we write it down to what it would sell for."
- **Right:** depreciation is **cost allocation across periods**, not revaluation. It answers "how
  much of this 3,00,000 belongs to *this* period?" — not "what would a buyer pay?" Under Going
  Concern, resale price is the wrong question entirely: the business is not selling it, it is using it.

**Your turn**

1. In one month a business buys machinery for **Rs 3,00,000** on credit from a supplier and pays **Rs
50,000** of commission to an agent. Both are purchases; both are things the business chose to spend
that amount on. Yet the commission is charged straight against the month's profit — cutting gross
profit of Rs 60,000 down to net profit of **Rs 10,000** — while the machinery appears nowhere in the
income statement. State the single test that separates them, apply it to each, and name the mechanism
that eventually releases the machinery's cost.

<details><summary>Answer</summary>

The test is: **do you still control a resource afterward?** Machinery — **yes**, so it is an asset and
its 3,00,000 waits on the balance sheet. Commission — **no**, nothing is held, so it is an expense and
hits profit now, producing the 10,000. **Depreciation** is the mechanism that releases the waiting
3,00,000 a little at a time, into each period that actually gets the use.

</details>

2. A business trading for its first month buys machinery for **Rs 3,00,000** during that month and
reports net profit of **Rs 10,000** for the month with **no depreciation charged at all**. A reviewer
objects that machinery always loses value the moment it is bought, so something should have been
written off. Explain why the omission is defensible here, why the reviewer's reason is the wrong
reason, and state precisely what would have to change for the omission to become a misstatement.

<details><summary>Answer</summary>

**Defensible:** the reporting period is a single month, the machine was acquired inside it and has
barely been used; depreciation allocates cost to the periods that got the use, and this one got almost
none. **The reviewer's reason is wrong** because depreciation is **cost allocation across periods, not
revaluation** — what a buyer would pay is never the trigger, and under going concern the business is
not selling the machine, it is using it. **It becomes a misstatement** once periods of real use pass
with a determinable useful life, and the charge that should have been made is large enough to change
the reported result.

</details>

---

## B4 — Accounting Period                     [SOURCED p.6]

**Definition**

**Accounting Period** = the assumption that the continuous life of a business is **chopped into
equal, stated blocks of time** — a month, a quarter, a year — and results are reported per block.

The name is the definition: *accounting* happens per *period*.

**Why it is needed:** a business's life is continuous. Performance is not. "Did we make money?" is
unanswerable until you say **money over what?**

```
   business life:  ==========================================>  (continuous, unbounded)

   without a cut-off:   "did we make money?"   ->  no answer possible

   with a cut-off:  |----- 1-30 June -----|         ->  NET PROFIT 10,000
                    |---- 1-31 July ------|         ->  comparable to June
                        ^             ^
                     bounded       bounded    -> two bounded things CAN be compared
```

**You cannot compare two things unless both are bounded.** That is the entire justification.

**What lie does this stop?** **"We'll be profitable eventually."** Forever. An unbounded promise can
never be tested and therefore can never be falsified. Force a cut-off and the claim becomes a number
that either arrives or does not.

**In action**

Two statements, two relationships with time — this is the cleanest illustration of the concept:

| Statement | Heading | Nature |
|---|---|---|
| Income statement | **for the period 1-30 June 2024** | **A period. A video.** |
| Balance sheet | **as at 30 June 2024** | **An instant. A photograph.** |

- **Net profit 10,000** is a *rate* — 10,000 *per that month.* Move the boundary, the number moves.
- **Cash 19,10,000** is a *level* — it is simply true at that instant.
- The period concept is what makes 10,000 a meaningful figure instead of a fragment.

**Where it bites**

The confusion: the balance sheet also covers the period.

- **Wrong:** "the balance sheet shows June, like the income statement does."
- **Right:** the balance sheet shows **30 June only** — a single instant. It has no duration. Its
  heading says *as at*, not *for the period*. The period concept **creates** the income statement and
  merely **dates** the balance sheet.

**Your turn**

1. A business closes its books at each month end and reports a net profit of **Rs 10,000** for the
month running **1–30 June**. The owner, unhappy with the figure, proposes abandoning the fixed month
end and reporting instead "from 1 June until we're comfortable." Name what becomes impossible under
that proposal, and name the specific lie it enables.

<details><summary>Answer</summary>

**Comparison becomes impossible** — you cannot compare two things unless both are bounded, so a
result for an open-ended stretch cannot be set against any other period. It also becomes
**unfalsifiable**: with the boundary free to move to wherever the number looks good, no claim can ever
be tested. The lie it enables is **"we'll be profitable eventually"** — forever, with the finish line
walked forward each time it is approached.

</details>

2. A business's income statement is headed **"for the period 1–30 June 2024"** and reports net profit
**Rs 10,000**. Its balance sheet is headed **"as at 30 June 2024"** and reports cash **Rs 19,10,000**.
Swap the two headings over. Describe exactly what each swapped heading would now be falsely claiming
about the figure sitting under it.

<details><summary>Answer</summary>

**"As at 30 June" over net profit 10,000** would falsely claim the 10,000 is a **level existing at an
instant** — a pot you could point at — when it is a **rate** earned across 30 days that moves the
moment you move the boundary. **"For the period 1–30 June" over cash 19,10,000** would falsely claim
the 19,10,000 is a **flow accumulated over the month**, when it is a single instant's level with no
duration. The period concept **creates** the income statement and merely **dates** the balance sheet.

</details>

---

## A12 — Accruals                     [SOURCED p.2]

**Definition**

**Accruals** = record income and expenses **when they are earned or incurred — not when cash moves.**

- **Earned** — you did the thing you were paid for.
- **Incurred** — the obligation arose, whether or not you have paid it.

Cash timing is a separate fact. It belongs to the balance sheet, not to the profit calculation.

```
   EVENT HAPPENS  ------------------->  CASH MOVES
        ^                                    ^
        |                                    |
   accruals books it HERE            cash accounting would
   (earned / incurred)               book it HERE
```

**Why it exists:** without accruals, a business could shift its profit by simply delaying a payment
across the cut-off. Accruals nail the expense to the period that caused it.

**In action**

**Day 4 is the demonstration.** Machinery 3,00,000 was purchased from Arjun & Co. — **no cash moved
that day.** Cash-based thinking would say nothing happened.

Accruals say the obligation was **incurred**, so it is booked:

| Date | Entry | Cash moved? |
|---|---|---|
| Jun 4 | Machinery A/C **Dr.** 3,00,000 / To Arjun & Co. 3,00,000 | **No** |
| Jun 6 | Arjun & Co. A/C **Dr.** 1,00,000 / To Cash 1,00,000 | Yes |

Result: **Arjun & Co. closing balance 2,00,000 credit** — still owed, and visible on the balance
sheet as a liability. The obligation was recorded when it *arose*, not when it *settles*.

The same principle is why **profit 10,000** and **cash 19,10,000** are unrelated numbers.

**Where it bites**

The confusion: "no cash, no entry."

- **Wrong:** Day 4 moved no cash, so there is nothing to record.
- **Right:** Day 4 created a **resource** (machinery 3,00,000) and an **obligation** (Arjun & Co.
  3,00,000). Both exist regardless of cash. Skip the entry and the balance sheet loses an asset and
  a liability, and 22,10,000 is wrong on both sides.

**Careful — Day 4 and Day 5 look identical and are not:**

| | Day 4 | Day 5 |
|---|---|---|
| Amount | 3,00,000 | 3,00,000 |
| Cash moved | No | No |
| **Was anything received, given, owed or paid?** | **Yes — machinery received, 3,00,000 owed** | **No** |
| Entry | Full entry | **NO ENTRY** |

Accruals removes the *cash* requirement. It does **not** remove the *event* requirement.

**Your turn**

1. In the same week, a business takes delivery of machinery worth **Rs 3,00,000** from a supplier on
credit — no cash moves — and separately places an order for goods worth **Rs 3,00,000** with a
different supplier, where nothing has shipped and no cash moves either. Same amount, same absence of
cash, two days apart. One is journalised in full; the other gets no entry. State the exact test that
separates them, and explain why "cash didn't move" is useless as a reason here.

<details><summary>Answer</summary>

The test is: **was anything received, given, owed or paid?** The machinery — **yes**: a resource was
received and 3,00,000 became owed, so a full entry is passed. The order — **no**: nothing on any of
the four counts, so no entry. "Cash didn't move" is useless because it is **true of both**. Accruals
removes the *cash* requirement; it does not remove the *event* requirement.

</details>

2. A business owes a supplier **Rs 3,00,000** for machinery delivered on credit. On 6 June it pays
**Rs 1,00,000** of that debt, leaving **Rs 2,00,000** outstanding at the 30 June month end, with cash
closing at **Rs 19,10,000** and net profit for the month at **Rs 10,000**. Now suppose that payment
had instead been made on 1 July. State which figures at 30 June change and which do not, and explain
why net profit is untouched either way.

<details><summary>Answer</summary>

**Change:** cash is 1,00,000 higher (the payment never left), and the supplier's credit balance is
1,00,000 higher — the full 3,00,000 still owed instead of 2,00,000. Both trial balance columns and
both sides of the balance sheet rise by that same 1,00,000, so everything still balances.
**Unchanged:** machinery, capital, sales, purchases and commission. **Net profit stays 10,000** —
settling a liability is not an expense; the expense was recognised when it was incurred, and paying a
debt never touches the income statement. That is exactly the shift the rule exists to prevent.

</details>

---

## B6 — Consistency                     [SOURCED p.7]

**Definition**

**Consistency** = once you choose an accounting method, **keep using it, period after period.** If
you must change it, disclose the change and its effect.

**Why it exists:** a number is only meaningful against another number. Change the method between
periods and you have not measured a change in the business — you have measured a change in your own
ruler.

```
   CONSISTENT:                          INCONSISTENT:
   June  --[method A]--> 10,000         June  --[method A]--> 10,000
   July  --[method A]--> 14,000         July  --[method B]--> 14,000
          ^                                    ^
   the business changed                 the RULER changed.
   -> the comparison MEANS something    -> the comparison means NOTHING
```

**What lie does this stop?** **Method-shopping for a flattering result.** Change your method every
year and you can always look good — pick whichever rule makes this year's number the biggest, then
pick a different one next year. Every individual year is defensible. The trend is fabricated.

**In action**

The first week's trial balance is drawn using the **balance method** — each account reduced to one
closing figure. The workbook names two methods: **total** and **balance**.

- June: balance method → Cash appears as **19,10,000**, one line.
- July: switching to the total method changes what the Cash line *displays*, so June's 19,10,000 and
  July's figure would no longer be measuring the same thing.
- Consistency says: **pick one, keep it.** If it must change, say so and quantify.

Same logic anywhere a choice exists — the moment two defensible methods sit side by side,
Consistency is what stops the choice being re-made every period in whichever direction flatters.

**Where it bites**

The confusion: consistency forbids change.

- **Wrong:** "we can never switch methods."
- **Right:** you **may** switch — to a better method — but you must **disclose the change and its
  effect** (that is **B7** doing the work). Consistency bans *silent, self-serving* switching. The
  crime is the silence and the motive, not the change.

**Your turn**

1. A business draws its June trial balance using the **balance method** — each account reduced to a
single closing figure, so cash appears once at **Rs 19,10,000** — and it totals **Rs 26,60,000** on
each side. In July, saying nothing to anyone, it switches to the **total method**, which instead
displays each account's total debits and total credits. July's trial balance balances perfectly and
every figure in it is correct. Explain why this is still a breach of the rule that a chosen method be
kept period after period.

<details><summary>Answer</summary>

Because what breaks is the **comparison, not the arithmetic** — and balancing was never the standard
this rule polices. July's trial balance can balance flawlessly while measuring something different
from June's 26,60,000. The reader assumes one ruler across periods; a silent switch changes the ruler,
so any apparent trend between the two months is fabricated rather than observed.

</details>

2. Six months into its year, a business genuinely finds a better method for valuing one of its
figures — better in a way it could defend to anyone who asked. The bookkeeper says the rule requiring
the same method every period means they are now stuck with the old one forever. Set out what that rule
actually permits, what it forbids, and which other convention makes the permitted route legitimate.

<details><summary>Answer</summary>

**Permits:** switching to the better method — the rule does not forbid change. **Forbids:** switching
**silently**, or switching to flatter the result; the crime is the silence and the motive, not the
change. **Full Disclosure** legitimises the permitted route: disclose the change and **quantify its
effect**, so a reader can restate the old period and compare like with like.

</details>

---

## B7 — Full Disclosure                     [SOURCED p.7]

**Definition**

**Full Disclosure** = the statements must reveal **everything a reader needs to interpret them
correctly** — not just the numbers, but the assumptions, methods and events behind the numbers.

The test is not "is every figure true?" The test is: **could a reasonable reader be misled by what
is missing?**

**What lie does this stop?** **The technically-true statement that misleads by omission.** This is
the most sophisticated lie in accounting, because every individual figure survives audit. Nothing is
false. The *picture* is false. Full Disclosure is the only rule aimed at the gap between accurate
figures and an accurate impression.

```
   Every figure TRUE   +   a key fact MISSING   =   a FALSE picture
                                   ^
                          this is what B7 attacks
```

**In action**

**The live example is in your own income statement.** The workbook gives **no closing stock**, so the
statement assumes **all goods purchased were sold**:

```
Sales                          4,60,000
Less: Cost of goods sold      (4,00,000)     <-- ALL of purchases treated as sold
GROSS PROFIT                     60,000
Less: Commission                (50,000)
NET PROFIT                       10,000
```

- **Wrong:** print net profit 10,000 and stop. Every figure traces to the trial balance. Nothing is
  false.
- **Right:** print net profit 10,000 **and state the assumption**: *no closing stock is given;
  therefore all goods purchased are assumed sold; real businesses almost never look like this.*

Without the note, a reader takes 60,000 as a real trading margin. With the note, the reader knows
exactly which brick is a guess and can push on it.

**Second live example:** the **Going Concern** basis behind Machinery 3,00,000. Disclosed, the reader
can challenge it. Undisclosed, the 3,00,000 looks like a fact rather than a consequence of an
assumption.

**Where it bites**

The confusion: disclosure means volume.

- **Wrong:** "disclose everything, so print everything."
- **Right:** Full Disclosure demands **what changes the reader's understanding.** Padding the notes
  is not compliance — it is the **Materiality (B9)** offence of hiding the important thing in
  trivia. B7 and B9 are a pair: B7 says *don't hide it by leaving it out*, B9 says *don't hide it by
  burying it*.

**Your turn**

1. In one month a business buys goods for **Rs 4,00,000** and sells goods for **Rs 4,60,000**. Nobody
counted what was left in the storeroom at month end, so the income statement treats the entire **Rs
4,00,000** as the cost of the goods sold, showing gross profit **Rs 60,000** and, after **Rs 50,000**
of commission, net profit **Rs 10,000**. Every figure ties exactly to the books. The statement is
published with no note about the assumption. Name a decision a reader would make differently once
told, and explain why "but every number is correct" is not a defence.

<details><summary>Answer</summary>

Once told, the reader **stops treating the 60,000 as a real trading margin** and stops extrapolating
the 10,000 forward — they would not fund, buy into or expand the business on the strength of a margin
that rests on an uncounted storeroom. **"Every number is correct" fails** because the test is *could a
reasonable reader be misled by what is missing?* — the picture, not the figures. True figures plus a
missing assumption produce a false impression, and that is precisely the lie this rule exists to
attack.

</details>

2. One convention says the statements must reveal **everything a reader needs to interpret them
correctly** — assumptions and methods, not just figures. Another says only information **big enough to
change a reader's decision** needs separate treatment; the rest may be grouped, rounded or dropped.
The first appears to demand more information and the second to permit less. A business, hearing the
first, proposes attaching 40 pages of notes to be safe. Reconcile the two into a single rule for what
belongs in a note, and judge the proposal.

<details><summary>Answer</summary>

**The single rule: disclose exactly what would change a reader's decision, and nothing that would
not.** They are one rule read from both ends — the first sets the **floor** (don't hide the decisive
thing by leaving it out), the second sets the **ceiling** (don't hide it by burying it in trivia). The
40 pages **fail both**: padding is not compliance, it is the offence of drowning the decisive fact,
and "but we disclosed it" on page 38 is not disclosure.

</details>

---

## B8 — Conservatism                     [SOURCED p.7]

**Definition**

**Conservatism** (also called prudence) = **recognise potential losses; never anticipate gains.**

Say it as a two-line rule and never say it any other way:

```
   +------------------------------------------------------+
   |  POSSIBLE LOSS   ->  BOOK IT (even if not yet certain)|
   |  POSSIBLE GAIN   ->  DO NOT BOOK IT (wait until real) |
   +------------------------------------------------------+
             ^
      DELIBERATELY ASYMMETRIC. This is not a bug.
```

**The asymmetry is the whole design.** A reader harmed by an overstated business loses money. A
reader who finds the business quietly better than reported is not harmed. So the rule tilts one way
on purpose.

**What lie does this stop?** **Every business looks magnificent right up until it collapses.** The
mechanism of that lie is always the same: gains that *might* happen get counted now, losses that
*might* happen get counted "later" — and later never arrives. Conservatism removes the first half of
the trick.

**In action — this is Day 5, and you have met it before**

On **Day 5** the business **placed an order for buying goods with Saksham — 3,00,000.**

**Could the business book Rs 3,00,000 as a sale?**

> **No.** Conservatism forbids anticipating a gain that has not happened.

**This is the SAME trap from Act 4, now stated as a principle.** In Act 4 you rejected Day 5 on the
mechanics: *nothing was received, given, owed or paid* — so **NO ENTRY**. That was the rule of
transactions. Conservatism is *why that rule is built the way it is*:

```
   ACT 4 (mechanics)                    ACT 8 (principle)
   -----------------                    -----------------
   "nothing received, given,             "never anticipate a gain"
    owed or paid"                                |
          |                                      |
          +------------- same answer ------------+
                              |
                      Jun 5 -> NO ENTRY
```

**The bait, stated plainly:** Day 5 is 3,00,000 — the *same amount* as Day 4's credit purchase, two
lines later. It mirrors a real transaction and is not one. Journalise it and:

- an order becomes revenue,
- profit inflates above **10,000**,
- and the trial balance still totals **26,60,000**-plus-noise without complaint.

The books would not catch it. Conservatism is the thing that catches it.

**Where it bites — correct this misconception now**

The confusion: conservatism = pessimism = "understate everything."

- **Wrong:** "be cautious, so write assets down, write profits down, keep every number low."
- **Right:** conservatism is **NOT** "understate everything." **Deliberately understating assets
  violates it too** — understatement is a misstatement, and creates hidden reserves that flatter a
  later period.

The rule is **specifically directional**:

| | Book it? |
|---|---|
| Potential **loss** | **Yes** |
| Potential **gain** | **No** |
| Deliberately understated **asset** | **No — this is a violation** |
| Deliberately understated **profit** | **No — this is a violation** |

Carrying machinery at **3,00,000** cost is conservative-correct. Writing it to 2,00,000 "to be
safe" is a **breach**, not caution.

**Your turn**

1. A business takes delivery of machinery worth **Rs 3,00,000** from a supplier on credit — the
machine is in the building, the money is not yet paid. In the same week it places an order for goods
worth **Rs 3,00,000** with a different supplier — nothing has shipped, nothing is owed. Only one of
the two is recorded. Explain that outcome first using the rule that **potential losses are recognised
but gains are never anticipated**, then using only the test of **whether anything was received, given,
owed or paid** — and state why the two explanations must agree.

<details><summary>Answer</summary>

**By the recognition rule:** the order is an **anticipated gain** — nothing earned, nothing certain —
so it is not booked; the machinery is an **incurred obligation with a resource received**, so it is
booked in full. **By the transaction test:** machinery was received and 3,00,000 became owed; on the
order, nothing was received, given, owed or paid. **They must agree** because the transaction test is
the **mechanical expression** of the principle — the rule of recognition was built the way it is
precisely to enforce the asymmetry.

</details>

2. A business's machinery cost **Rs 3,00,000** and there is no evidence whatever that it is worth
less. Drawn correctly, its balance sheet totals **Rs 22,10,000**. The owner instructs that the
machinery be carried at **Rs 2,00,000** instead, saying "I'd rather be conservative — nobody was ever
hurt by a cautious number." State whether this complies with the rule that potential losses are
recognised but gains never anticipated, give the balance sheet total it produces against the correct
22,10,000, and explain why the direction of the error does not make it acceptable.

<details><summary>Answer</summary>

**It does not comply — it is a violation.** The rule is **directional** (book potential losses, never
book potential gains), not "keep every number low"; deliberately understating an asset is a
misstatement, not caution. It produces a total of **21,10,000 against the correct 22,10,000**, and
creates a **hidden reserve** that will flatter a later period when the 1,00,000 quietly reappears. An
error's direction does not change the fact that the statement is wrong — the owner is describing
pessimism, not conservatism.

</details>

---

## B9 — Materiality                     [SOURCED p.7]

**Definition**

**Materiality** = only information **big enough to change a reader's decision** needs separate,
precise treatment. Everything else may be approximated, grouped, or ignored.

An item is **material** if omitting or misstating it would change what someone does.

**Materiality is permission to stop.** It is the only rule in this section that *reduces* work — and
it exists because **perfect precision costs more than it's worth.** Chasing every rupee is not
virtue; it is a misallocation of effort that produces no better decision.

```
   Would knowing this change the reader's decision?
                |                       |
              YES                      NO
                |                       |
          MATERIAL:               IMMATERIAL:
          disclose it             group it, round it, drop it
          separately              -> STOP WORKING
```

**What lie does this stop?** **Drowning the reader in trivia so the important thing can't be found.**
Note that this is a lie told with *true* information — the classic defence is "but we disclosed it."
Disclosed on page 90 among 400 irrelevant items is not disclosed.

**In action**

Judge each first-week figure against the balance sheet total of **22,10,000**:

| Item | Amount | Material? | Why |
|---|---|---|---|
| Capital | 20,00,000 | **Yes** | Nearly the entire funding of the business |
| Cash | 19,10,000 | **Yes** | The dominant asset; every liquidity judgement uses it |
| Machinery | 3,00,000 | **Yes** | Own line — it carries the Going Concern assumption |
| Arjun & Co. | 2,00,000 | **Yes** | The only liability; a reader must see what is owed |
| Commission | 50,000 | **Yes** | It converts gross profit 60,000 into net profit **10,000** |

**Look at Commission 50,000 carefully — this is the lesson.** Against 22,10,000 it looks tiny. It is
absolutely material anyway: it consumes five-sixths of gross profit and is the difference between a
comfortable result and net profit of 10,000.

**Materiality is not a size test. It is a decision test.** A small number attached to a decisive
outcome is material; a large number that changes nothing is not.

**Where it bites**

The confusion: materiality is a percentage.

- **Wrong:** "anything under some fixed cut-off of the total is immaterial — 50,000 against
  22,10,000 is noise, group it."
- **Right:** 50,000 is what turns 60,000 into 10,000. It **changes the reader's conclusion**,
  therefore it is material, whatever the ratio says. Size is *evidence* of materiality. **Decision
  impact is the definition.**

**Your turn**

1. A business's balance sheet totals **Rs 22,10,000**. In the same month's income statement, a
commission of **Rs 50,000** turns gross profit of **Rs 60,000** into net profit of **Rs 10,000**.
Against 22,10,000 that commission is roughly two-tenths of one percent, and a junior proposes folding
it into a "sundry expenses" line on the grounds that anything that small is noise. Build the argument
that it is material from the definition — *material = would change a reader's decision if omitted or
misstated* — and state the decision that would change if it were buried.

<details><summary>Answer</summary>

It is **material**, because it **decides the reader's conclusion**: it consumes five-sixths of the
gross margin and is the whole difference between a business apparently earning 60,000 a month and one
earning 10,000. **Buried**, a reader concludes the operation throws off roughly 60,000 a month and
lends to, buys into or expands it on that basis; **disclosed**, that decision changes. The percentage
is irrelevant — **size is only evidence of materiality; decision impact is the definition.**

</details>

2. A business's balance sheet shows machinery of **Rs 3,00,000**, acquired and not consumed, so it
never touches the income statement at all. That statement shows gross profit **Rs 60,000** less
commission **Rs 50,000**, giving net profit **Rs 10,000**. A reader is deciding one thing only: does
this operation earn? Show that for *that* reader the larger amount is **less** material than the
smaller one, and say what this proves about fixed percentage cut-offs.

<details><summary>Answer</summary>

For that decision the **3,00,000 changes nothing** — it never enters profit, so knowing it or not
leaves the answer identical; the **50,000 decides it outright**, turning 60,000 into 10,000. So the
larger figure is the less material of the two. This proves materiality is a **decision test, not a
size test**, and that a fixed percentage cut-off will **misclassify in both directions** — waving
through big irrelevancies and discarding small decisive ones.

</details>

---

## B11 — Which concept does the scenario violate?                     [SOURCED p.7]

**Definition**

The workbook's own **"Who am I?"** exercise (p.7) tests exactly one skill: **read a scenario, name
the rule it breaks.** It runs five cases. This node is the drill.

**The method — three questions, in order:**

```
   1. WHAT is being distorted?
      value  -> Going Concern (B3)
      timing -> Accounting Period (B4) or Accruals (A12)
      whose  -> Business Entity (B2, Act 1)

   2. Is a GAIN being anticipated, or a LOSS hidden?     -> Conservatism (B8)

   3. Is something TRUE but MISSING?                     -> Full Disclosure (B7)
      Did the RULER change between periods?              -> Consistency (B6)
      Is trivia crowding out the decisive figure?        -> Materiality (B9)
```

**The single highest-yield discriminator:** *did the business change, or did the method change?*
Business changed → probably fine. Method changed silently → **Consistency.**

**In action**

Five scenarios, all drawn from the first week. Diagnose each:

| # | Scenario | Violates | Because |
|---|---|---|---|
| 1 | Day 5's order with Saksham (3,00,000) is booked as a sale | **Conservatism (B8)** | A gain is anticipated; nothing was earned |
| 2 | Machinery 3,00,000 is carried at cost although the business will be shut and sold next month | **Going Concern (B3)** | The assumption underpinning cost has failed; break-up values are required |
| 3 | Net profit 10,000 is published with no mention that closing stock is absent and all goods are assumed sold | **Full Disclosure (B7)** | Every figure is true; the omission makes the picture false |
| 4 | July's trial balance switches from the balance method to the total method, silently | **Consistency (B6)** | The ruler changed, so June's 26,60,000 and July's are no longer comparable |
| 5 | The owner asks "are we profitable?" and is told "eventually — no cut-off yet" | **Accounting Period (B4)** | An unbounded claim cannot be tested; performance needs 1-30 June |

**Where it bites**

The confusion: Conservatism and Full Disclosure overlap.

- **Wrong:** "the business hid bad news, so that's conservatism."
- **Right:** ask *what was done with the number*:
  - A **gain was counted early** or a **loss was ignored** → **Conservatism (B8)**. The offence is in
    the *recognition decision*.
  - The **numbers are all correct** but a needed fact is **absent** → **Full Disclosure (B7)**. The
    offence is in the *telling*.

Booking Day 5 as revenue is B8. Publishing profit 10,000 while silent on the stock assumption is B7.
Neither is the other.

**Your turn**

1. A business's machinery cost **Rs 3,00,000** and nothing suggests it is worth any less. The business
carries it on the balance sheet at **Rs 2,00,000**, states the Rs 1,00,000 reduction plainly in a note
that any reader can find, and applies exactly the same treatment every single month without deviation.
Three conventions are in play: **keep the same method period after period**; **reveal what a reader
needs to interpret the statements**; **recognise potential losses but never anticipate gains, and make
no arbitrary write-downs**. Two are satisfied and one is violated. Name all three verdicts and defend
each.

<details><summary>Answer</summary>

**Consistency — satisfied:** the same treatment every month, so the ruler never changes. **Full
Disclosure — satisfied:** the reduction is stated clearly enough for a reader to find and undo it.
**Conservatism — violated:** deliberately understating an asset from 3,00,000 to 2,00,000 breaches the
directional rule; understatement is a misstatement, and applying a wrong number **consistently and
openly** does not make it right — it only makes it a well-documented wrong number.

</details>

2. Two things happen in one set of accounts. **(i)** A business places an order for goods worth **Rs
3,00,000** with a supplier — nothing shipped, nothing owed, no cash moved — and books it as a sale.
**(ii)** Nobody counted the closing storeroom, so the whole **Rs 4,00,000** of purchases is treated as
sold, and net profit is published with no mention of that assumption. Separate the two offences,
assign the correct rule to each, and state which of them the trial balance could have caught.

<details><summary>Answer</summary>

**(i) Conservatism** — a gain is anticipated on an order where nothing was earned; the offence lies in
the **recognition decision**. **(ii) Full Disclosure** — every figure is true but a needed fact is
absent, so the picture is false; the offence lies in the **telling**. **The trial balance could have
caught neither:** a fabricated sale entered as an equal debit and credit still balances, and an
undisclosed assumption is not a figure at all.

</details>

---

## A16 — Peripheral glossary                     [SOURCED pp.4-5 — puzzle filler; the workbook never uses these terms again]

**Be honest about this one.** These five terms appear on pp.4-5 of the workbook **as word-search
puzzle terms and nowhere else.** No session uses them. No session defines them. They are **puzzle
filler.**

They are listed here — separately, at the end, deliberately not woven into anything — because
forcing them into the narrative would fake a need the material does not have. Know the one-liners.
Do not expect them to connect to the first week's figures, because in this workbook they do not.

| Term | One-line definition |
|---|---|
| **Amortization** | Spreading the cost of an **intangible** asset (a patent, goodwill) over its useful life — depreciation's counterpart for things you cannot touch. |
| **Contingent** | A liability or asset that **depends on a future event** that may or may not happen — e.g. the outcome of a lawsuit. |
| **Acquisition** | Obtaining control of an asset or of another business. |
| **Dividend** | A distribution of profit paid out to a company's shareholders. |
| **Taxation** | Compulsory payments levied by government on income, profit or transactions. |

**The one connection that is real:** **amortization** is the intangible-asset twin of **depreciation
(A11)** — same idea, same dependence on **Going Concern (B3)**, different kind of asset. That link is
genuine. The other four have none in this workbook.

**Your turn**

1. **Amortization** is the spreading of an **intangible** asset's cost — a patent, goodwill — over its
useful life: depreciation's counterpart for things you cannot touch. Depreciation depends on the
assumption that the business will keep operating for the foreseeable future, because the words *useful
life* only mean something if a future in which the asset gets used has already been assumed. A
business carries a patent at cost and is then told it will be wound up and sold off next month.
Explain why amortization leans on that same assumption in exactly the same way, and name what happens
to the patent's carrying amount once the assumption fails.

<details><summary>Answer</summary>

Amortization spreads the cost over a **useful life**, and "useful life" **presupposes a future in
which the asset is used** — which is exactly what the going-concern assumption supplies. Kill the
assumption and there is **no life to spread the cost across**, so the exercise becomes incoherent. The
patent would have to be carried at whatever it could **realise on break-up** — and for many
intangibles, goodwill above all, that is nil or close to it.

</details>

2. A **contingent** item is a liability or asset whose existence depends on a future event that may or
may not happen. A business is defending a lawsuit it may well lose, which would cost it money, and is
separately the claimant in a different lawsuit it may well win, which would bring money in. Both are
uncertain to roughly the same degree. Using the rule that **potential losses are recognised but gains
are never anticipated**, state how each is treated, and explain why the asymmetry is deliberate rather
than pessimism.

<details><summary>Answer</summary>

**Contingent loss (the suit it may lose): recognise it / provide for it**, even though it is
uncertain. **Contingent gain (the suit it may win): do not book it** until it is realised. The
asymmetry is deliberate because **the two errors do not cause symmetric harm** — a reader misled by an
overstated business loses money, while one who later finds the business quietly better than reported
loses nothing. It is directional protection, not gloom: arbitrarily writing assets down would violate
the very same rule.

</details>

---

## THE SECTION IN ONE TABLE — convention/concept → the lie it stops

| Rule | Type | The lie it stops |
|---|---|---|
| **B3 Going Concern** | Concept (postulate) | Valuing a dying business as if it were healthy |
| **B4 Accounting Period** | Concept (postulate) | "We'll be profitable eventually" — forever |
| **B6 Consistency** | Convention (tradition) | Method-shopping for a flattering result |
| **B7 Full Disclosure** | Convention (tradition) | The technically-true statement that misleads by omission |
| **B8 Conservatism** | Convention (tradition) | Every business looks magnificent right up until it collapses |
| **B9 Materiality** | Convention (tradition) | Drowning the reader in trivia so the important thing can't be found |

```
   CONCEPTS (postulates)  -> decide whether the statements MEAN anything
   CONVENTIONS (traditions) -> decide whether the statements can be TRUSTED
```
