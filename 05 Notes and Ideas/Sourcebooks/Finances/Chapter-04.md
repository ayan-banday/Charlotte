# CHAPTER 4: How Do I Know When I Stop Losing Money?

---

## 1. THE SITUATION

**Company:** **MasalaBox Kitchen** — a cloud kitchen in Bengaluru. You cook North Indian meals and sell through Swiggy and Zomato. No dine-in. One kitchen, four cooks, two delivery riders on payroll.

It is month six. Revenue is climbing — ₹12 lakh last month, up from ₹8 lakh three months ago. Your accountant says you are "almost profitable." Your bank balance says otherwise. Rent is due in ten days and you are ₹1.8 lakh short.

Your ops lead walks in with three questions:

1. **"How many orders do we actually need to stop losing money?"**
2. **"Swiggy wants us on a 30% discount campaign. Should we join?"**
3. **"If we want ₹50,000 profit next month, how many orders is that?"**

You cannot answer any of these from the audited P&L alone. The P&L tells you what happened last month. These questions are about **what must happen next** — and that requires a different tool: **break-even analysis**, built on **marginal costing**.

---

## 2. WHY THIS MATTERS

Startups do not fail because founders cannot read a Balance Sheet. They fail because founders **grow revenue while still losing money on every order** — or because they accept discount deals that look like "growth" but destroy contribution.

Three traps MasalaBox is facing right now:

| Trap | What it sounds like | What is actually happening |
|---|---|---|
| **Revenue vanity** | "We did ₹12 lakh in sales!" | Sales ≠ profit. Fixed costs may still exceed contribution. |
| **Full-cost pricing panic** | "₹180 per meal costs us ₹220 to make — every order loses ₹40!" | Full cost includes fixed costs allocated per unit. That is wrong for a one-off discount decision. |
| **Cash vs break-even confusion** | "We broke even on the P&L but cannot pay rent" | Break-even is a **contribution** concept. Cash timing (commissions paid weekly, rent monthly) is separate. |

Lamba's warning applies directly: **"Profit is an opinion; cash in the bank is a fact."** Break-even analysis tells you when contribution covers fixed costs — your **minimum survival sales level**. It does not replace cash flow planning, but without it you are flying blind on pricing, discounts, and growth.

This is **Managerial Accounting** at its most useful: a forward-looking calculation you run in a spreadsheet, not a report your CA files with the tax department.

---

## 3. THE THEORY

### 3.1 Marginal costing — why "marginal"?

**Marginal costing** (also called **variable costing** for decision purposes) focuses on what changes when you sell **one more unit** — the **margin** at the edge of your business.

- **Marginal** — from Latin *margo*, "edge." The cost or revenue at the **margin** of your current activity: one more thali, one more biryani order.
- **Costing** — assigning costs to understand what you are really spending.

Under marginal costing, costs split into two buckets:

| Bucket | Definition | MasalaBox examples |
|---|---|---|
| **Variable costs (VC)** | Change with each order | Ingredients, packaging, aggregator commission %, per-order delivery fee, payment gateway charges |
| **Fixed costs (FC)** | Stay the same for the period regardless of orders | Kitchen rent, core cook salaries, insurance, base software subscriptions |

**Why separate them?** Because fixed costs are **already committed** whether you sell 50 orders or 500. The decision question is never "does this order cover rent?" — rent is sunk for the month. The question is: **"Does this order contribute something toward rent, or does it cost us more than it brings in?"**

That "something" has a name.

---

### 3.2 Contribution — the building block

You met contribution in Chapter 3. Here is why it sits at the centre of break-even analysis:

```
Contribution = Sales − Variable Costs
```

Or per unit:

```
Contribution per unit = Selling Price − Variable Cost per unit
```

**Why "contribution"?** Lamba: *"Contribution is called Contribution because it is the contribution of each unit sold towards the organization's bottom line."*

Think of fixed costs as a **hurdle**. Every order throws contribution over the hurdle. Until total contribution equals fixed costs, you are **below break-even** — still losing money overall. After that point, each order adds **profit**.

```
Profit = Total Contribution − Fixed Costs
```

**Key insight:** A sale can have **positive contribution** but the business still loses money — if total contribution has not yet cleared fixed costs. You are losing **less** with each sale, not necessarily making profit yet.

---

### 3.3 Break-even — why "break even"?

**Break-even** is the sales volume where total contribution **exactly equals** fixed costs. No profit. No loss. You "break even" — you stop the bleeding.

At break-even:

```
Total Contribution = Fixed Costs
```

**Why the term matters psychologically:** Founders often celebrate "record revenue months" without knowing their break-even point. If break-even is ₹14 lakh and you did ₹12 lakh, you had your best month ever — and still lost money. The break-even number turns vague anxiety into a **concrete target**.

Two ways to express it:

| Measure | Formula | What it tells you |
|---|---|---|
| **Break-even units** | Fixed Costs ÷ Contribution per unit | How many orders you need |
| **Break-even sales (₹)** | Break-even units × Selling Price | Revenue value of that volume |

---

### 3.4 PV Ratio — why "profit-volume"?

The **PV Ratio** (Profit-Volume Ratio), also called **Contribution Margin Ratio**:

```
PV Ratio = Contribution ÷ Sales × 100
```

Or per unit:

```
PV Ratio = Contribution per unit ÷ Selling Price × 100
```

**Why "profit-volume"?** It shows the relationship between **volume of sales** and **contribution toward profit**. It answers: *"Of every ₹100 of revenue, how many rupees are available to cover fixed costs and profit?"*

**Example intuition:** If PV Ratio is 40%, every ₹1,00,000 of sales contributes ₹40,000 toward fixed costs. Once fixed costs are covered, that same 40% flows to profit.

**Why it is useful:** Compare product lines or channels quickly. A biryani with 50% PV Ratio is more "efficient" at generating contribution than a ₹99 combo at 20% — even if the combo sells more units.

---

### 3.5 Target profit — extending break-even

Break-even is profit = zero. But Priya wants **₹50,000 profit**. The formula extends naturally:

```
Required Contribution = Fixed Costs + Target Profit

Break-even units (for target profit) = (Fixed Costs + Target Profit) ÷ Contribution per unit
```

**Why this matters:** Investors, lenders, and your own salary are not optional forever. "Stop losing money" is step one. "Earn enough to pay myself" is step two. Target profit calculation turns break-even into a **business plan number**.

---

### 3.6 Operating leverage — a first look

**Operating leverage** measures how sensitive your profit is to changes in sales volume, given your mix of fixed and variable costs.

```
Degree of Operating Leverage (DOL) = Contribution ÷ Profit
```

(At a given volume, when profit > 0.)

**Why "leverage"?** Fixed costs act like a **lever**. Once you clear break-even, each additional rupee of sales drops mostly to profit — because variable costs are the only thing rising. High fixed costs mean:

- **Above break-even:** Profits grow fast. A 10% sales increase might produce a 30% profit increase.
- **Below break-even:** Losses are painful. A 10% sales drop deepens the hole because fixed costs do not shrink.

**Why startups should care:** Cloud kitchens, SaaS, and manufacturing all share high fixed costs. Lamba's point: understand your leverage before you celebrate growth. **Revenue up 20% means nothing if you are still below break-even.**

---

### 3.7 The discount decision — marginal costing in action

A discount campaign (Swiggy's 30% off, a bulk corporate order, a festival offer) triggers one question:

**Is the discounted price still above variable cost per unit?**

| Scenario | Decision logic |
|---|---|
| Price > Variable Cost | **Positive contribution.** May accept if capacity is idle and fixed costs are already committed. |
| Price = Variable Cost | **Zero contribution.** You are working for free to cover nothing. Only accept for strategic reasons (customer acquisition with known lifetime value). |
| Price < Variable Cost | **Negative contribution.** Every order **increases** your loss. Reject unless it triggers profitable follow-on business you can measure. |

**Why founders get this wrong:** They compare the discount price to **full cost** (variable + allocated fixed). Full cost is for **long-term pricing**. Variable cost is for **this-order decisions**.

Lamba's logic: selling below full cost but above variable cost does not mean you are "profitable" — it means you are **minimising loss** when fixed costs are already unavoidable.

---

## 4. HOW IT WORKS

### Framework — The break-even toolkit

**Step 1: Separate variable and fixed costs for the period (usually one month)**

List every cost. Ask: *"If we sold zero orders this month, would we still pay this?"* Yes → Fixed. No → Variable.

**Step 2: Calculate contribution per unit**

```
Contribution per unit = Selling Price − Variable Cost per unit
```

Use **net selling price** if aggregator commission comes out of revenue (price minus platform fee).

**Step 3: Calculate break-even volume**

```
Break-even units = Fixed Costs ÷ Contribution per unit
```

Round **up** — you cannot sell 847.3 thalis.

**Step 4: Calculate break-even sales value**

```
Break-even sales (₹) = Break-even units × Selling Price
```

**Step 5: Calculate profit at any given volume**

```
Profit = (Units sold × Contribution per unit) − Fixed Costs
```

**Step 6: Calculate volume needed for target profit**

```
Required units = (Fixed Costs + Target Profit) ÷ Contribution per unit
```

**Step 7: PV Ratio (for comparison across products)**

```
PV Ratio = Contribution per unit ÷ Selling Price × 100
```

### Quick reference — all formulas

| What you need | Formula |
|---|---|
| Contribution per unit | SP − VC per unit |
| Total contribution | Units × Contribution per unit |
| Break-even units | FC ÷ Contribution per unit |
| Break-even sales (₹) | Break-even units × SP |
| Profit | Total contribution − FC |
| Units for target profit | (FC + Target profit) ÷ Contribution per unit |
| PV Ratio | Contribution ÷ Sales × 100 |
| Operating leverage | Contribution ÷ Profit (at current volume) |

### Decision checklist — when to use what

| Question | Tool |
|---|---|
| How many orders to survive this month? | Break-even units |
| What revenue number must we hit? | Break-even sales (₹) |
| Are we making money at current volume? | Profit formula |
| How many orders for ₹X profit? | Target profit formula |
| Should we accept this discount? | Contribution per unit at discounted price vs variable cost |
| Which dish is better for the business? | PV Ratio comparison |

---

## 5. WORKED EXAMPLE

### MasalaBox Kitchen — November data

**Priya pulls one month of clean numbers:**

| Item | ₹ |
|---|---|
| Average selling price per order (customer pays) | 250 |
| Aggregator commission (22% of selling price) | 55 |
| **Net revenue per order** (what MasalaBox receives) | **195** |
| Ingredients + packaging per order | 85 |
| Per-order delivery rider cost (variable portion) | 25 |
| Payment gateway / misc per order | 5 |
| **Total variable cost per order** | **115** |
| Monthly kitchen rent | 1,20,000 |
| Cook and staff salaries (fixed) | 2,40,000 |
| Insurance, utilities (fixed), software | 40,000 |
| **Total fixed costs per month** | **4,00,000** |

---

**Step 1 — Contribution per order**

Use **net revenue** (after commission) minus variable cost:

```
Contribution per order = ₹195 − ₹115 = ₹80
```

Each order contributes ₹80 toward covering rent, salaries, and profit.

---

**Step 2 — PV Ratio**

```
PV Ratio = ₹80 ÷ ₹195 × 100 = 41.0%
```

Roughly 41 paise of every rupee received (after commission) goes to fixed costs and profit.

---

**Step 3 — Break-even units**

```
Break-even orders = ₹4,00,000 ÷ ₹80 = 5,000 orders/month
```

MasalaBox must fulfil **5,000 orders** just to stop losing money.

At ~167 orders/day in a 30-day month. Priya now has a concrete target, not a feeling.

---

**Step 4 — Break-even sales value**

Two ways to express it:

**Gross sales (what customers pay):**

```
5,000 orders × ₹250 = ₹12,50,000/month
```

**Net sales (what MasalaBox receives after commission):**

```
5,000 orders × ₹195 = ₹9,75,000/month
```

When talking to your team, use **gross order count and customer-facing price** — that is what ops tracks. When checking against bank inflows, use **net**.

---

**Step 5 — Profit at 6,200 orders (last month's actual volume)**

Priya thought 6,200 orders meant a great month. Let's check:

```
Total contribution = 6,200 × ₹80 = ₹4,96,000
Profit = ₹4,96,000 − ₹4,00,000 = ₹96,000
```

**Result:** MasalaBox earned **₹96,000 profit** — above break-even by 1,200 orders. Good month. But Priya was ₹1.8 lakh short on rent — because **profit ≠ cash in hand** (commissions, supplier payments, and last month's losses consumed cash). Break-even told her the business model works at this volume; cash flow tells her **when** she can pay rent.

---

**Step 6 — Target profit: ₹50,000 next month**

```
Required contribution = ₹4,00,000 + ₹50,000 = ₹4,50,000

Required orders = ₹4,50,000 ÷ ₹80 = 5,625 orders
```

To earn **₹50,000 profit**, MasalaBox needs **5,625 orders** — 625 more than break-even.

**Check:**

```
5,625 × ₹80 = ₹4,50,000 contribution
₹4,50,000 − ₹4,00,000 = ₹50,000 profit ✓
```

---

**Step 7 — The Swiggy 30% discount campaign**

Swiggy proposes: MasalaBox offers 30% off to customers. Customer pays ₹175 instead of ₹250. Commission stays 22%.

| | Normal order | Discount order |
|---|---|---|
| Customer pays | ₹250 | ₹175 |
| Commission (22%) | ₹55 | ₹38.50 |
| **Net to MasalaBox** | **₹195** | **₹136.50** |
| Variable cost | ₹115 | ₹115 |
| **Contribution** | **₹80** | **₹21.50** |

**Analysis:**

- Discount price (₹136.50 net) is **above** variable cost (₹115). Contribution is **positive** — ₹21.50 per order.
- Discount price is **below** normal contribution. Each discount order contributes **₹58.50 less** than a full-price order.
- Full cost per order (allocating fixed costs at 5,000 break-even volume): ₹115 + (₹4,00,000 ÷ 5,000) = ₹115 + ₹80 = ₹195. At ₹136.50 net, discount orders look like a "loss" on full-cost basis — **misleading for this decision**.

**Break-even impact if ALL sales were discount orders:**

```
₹4,00,000 ÷ ₹21.50 = 18,605 orders needed to break even
```

vs 5,000 at full price. The campaign **raises break-even by 3.7×** if it becomes your normal price.

**Priya's decision framework:**

| Question | Answer |
|---|---|
| Is contribution positive? | Yes — ₹21.50/order |
| Do we have idle kitchen capacity? | Yes — can cook more without new fixed cost |
| Will discount customers only ever order at ₹175? | Unknown — risky if yes |
| Does Swiggy guarantee minimum order volume? | Ask for 2,000+ incremental orders |

**Decision:** Accept **only** if incremental discount orders exceed the volume needed to offset lost contribution on full-price orders. If the campaign brings 3,000 **new** discount orders: 3,000 × ₹21.50 = ₹64,500 extra contribution. That helps — but only if those customers would not have ordered at ₹250 anyway.

**Rule:** Never accept a discount that pushes price **below variable cost**. This one does not — but it moves break-even sharply upward.

---

**Step 8 — Operating leverage snapshot**

At 6,200 orders with ₹96,000 profit:

```
DOL = Contribution ÷ Profit = ₹4,96,000 ÷ ₹96,000 ≈ 5.2
```

A 10% increase in orders (to 6,820) adds roughly ₹40,000 contribution (620 × ₹80). Profit rises from ₹96,000 to ~₹1,36,000 — a **42% profit increase** from 10% more volume. That is operating leverage working in your favour — **above break-even**.

Below break-even, the same leverage works against you.

---

## 6. YOUR TURN

**Company:** **BowlBox** — single-location cloud kitchen, Mumbai. Sells grain bowls via aggregators.

**Monthly data:**

| Item | Value |
|---|---|
| Selling price per bowl | ₹320 |
| Aggregator commission | 20% of selling price |
| Variable cost per bowl (ingredients, packaging, delivery) | ₹140 |
| Monthly fixed costs | ₹5,60,000 |

**Questions:**

1. What is net revenue per bowl (after commission)?  
2. What is contribution per bowl?  
3. What is the PV Ratio?  
4. How many bowls must BowlBox sell to break even?  
5. BowlBox sold 3,200 bowls last month. What was profit or loss?  
6. BowlBox wants ₹1,00,000 profit next month. How many bowls are needed?  
7. A corporate caterer offers to buy 800 bowls at ₹200 each (no aggregator commission). Variable cost unchanged. Accept or reject? Show the contribution math.

**Answer key:**

1. **Commission = 20% × ₹320 = ₹64. Net revenue = ₹320 − ₹64 = ₹256 per bowl.**  
2. **Contribution = ₹256 − ₹140 = ₹116 per bowl.**  
3. **PV Ratio = ₹116 ÷ ₹256 × 100 = 45.3%.**  
4. **Break-even = ₹5,60,000 ÷ ₹116 = 4,828 bowls** (round up; exact 4,827.59).  
5. **Total contribution = 3,200 × ₹116 = ₹3,71,200. Profit/Loss = ₹3,71,200 − ₹5,60,000 = −₹1,88,800 loss.** Below break-even by 1,628 bowls.  
6. **Required contribution = ₹5,60,000 + ₹1,00,000 = ₹6,60,000. Bowls needed = ₹6,60,000 ÷ ₹116 = 5,690 bowls.**  
7. **At ₹200 with no commission: Contribution = ₹200 − ₹140 = ₹60 per bowl.** Positive contribution. 800 × ₹60 = ₹48,000 toward fixed costs. **Accept if capacity is idle** and it does not replace full-price sales. **Reject** if kitchen is at capacity and you would sell those 800 bowls at ₹256 net (₹116 contribution) instead — you would lose ₹56 per bowl in opportunity contribution (₹116 − ₹60).

---

## 7. PRACTICE QUESTIONS

**Question 14**  
Which situation demonstrates the MOST appropriate use of Managerial Accounting?

A) Preparing audited financial statements for shareholders  
B) Estimating the break-even sales required before launching a new product  
C) Filing annual tax returns  
D) Reporting earnings to the stock exchange  

**Answer: B — Estimating the break-even sales required before launching a new product**

Break-even estimation is forward-looking, internal, and tailored to a specific decision — the core purpose of Managerial Accounting. Options A, C, and D are external reporting and compliance tasks governed by standardized rules (GAAP/IFRS, tax law, listing requirements). Those are Financial Accounting and tax accounting domains.

---

**Question 8**  
MasalaBox's contribution per order is ₹80 and fixed costs are ₹4,00,000. If it sells 4,000 orders in a month, what is the profit or loss?

A) ₹80,000 profit  
B) ₹80,000 loss  
C) ₹3,20,000 profit  
D) ₹3,20,000 loss  

**Answer: B — ₹80,000 loss**

Total contribution = 4,000 × ₹80 = ₹3,20,000. Profit = ₹3,20,000 − ₹4,00,000 = **−₹80,000** (loss). The company is 1,000 orders below break-even (5,000). Each missing order costs ₹80 in contribution — 1,000 × ₹80 = ₹80,000 shortfall.

---

**Question 9**  
A cloud kitchen has a PV Ratio of 50% and fixed costs of ₹6,00,000. What net sales revenue is needed to break even?

A) ₹3,00,000  
B) ₹6,00,000  
C) ₹12,00,000  
D) ₹18,00,000  

**Answer: C — ₹12,00,000**

At break-even, Contribution = Fixed Costs. Since PV Ratio = Contribution ÷ Sales, then Sales = Fixed Costs ÷ PV Ratio = ₹6,00,000 ÷ 0.50 = **₹12,00,000**. Half of every rupee of net sales becomes contribution; you need ₹12 lakh in sales to generate ₹6 lakh contribution.

---

**Question 10**  
A food delivery startup is offered a bulk order at a price below its normal selling price but above its variable cost per unit. Fixed costs for the month are already committed. Which statement is MOST accurate?

A) The order should be rejected because price is below full cost  
B) The order should be accepted because it contributes toward covering fixed costs  
C) The order should be rejected because it reduces the PV Ratio to zero  
D) The order should be accepted only if price exceeds total fixed costs  

**Answer: B — The order should be accepted because it contributes toward covering fixed costs**

When fixed costs are sunk for the period, the relevant comparison is **price vs variable cost**, not price vs full cost. A positive contribution helps cover committed fixed costs and reduces total loss — or adds to profit. Option A uses the wrong cost basis. Option C is wrong — PV Ratio is not zero if contribution is positive. Option D confuses per-unit price with total fixed costs.

---

**Question 11**  
Which cost structure creates the HIGHEST operating leverage once a company is above break-even?

A) Mostly variable costs, few fixed costs  
B) Mostly fixed costs, few variable costs  
C) Equal split of fixed and variable costs  
D) No fixed costs at all  

**Answer: B — Mostly fixed costs, few variable costs**

High fixed costs mean that above break-even, most additional revenue flows to profit (only variable costs rise with volume). That amplifies profit growth — and loss depth below break-even. Option A and D have low leverage because costs flex with revenue.

---

**Question 12**  
BowlBox needs ₹5,60,000 in contribution to cover fixed costs. Its contribution per bowl is ₹116. It wants ₹84,000 profit on top. How many bowls must it sell?

A) 4,828  
B) 5,000  
C) 5,552  
D) 6,400  

**Answer: C — 5,552**

Required contribution = ₹5,60,000 + ₹84,000 = ₹6,44,000. Bowls = ₹6,44,000 ÷ ₹116 = **5,551.72 → 5,552 bowls** (round up). Option A is break-even only (no profit). Option B is insufficient. Option D would generate more profit than needed.

---
