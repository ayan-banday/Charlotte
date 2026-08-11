from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
import os, textwrap

ROOT = r'S:\Charlotte'
OUT = os.path.join(ROOT, 'output', 'pdf', 'Udyan_From_Idea_to_Business_Proposal.pdf')
ART = os.path.join(ROOT, 'assets', 'udyan-course', 'ash-journey-cover.png')
W, H = A4
NAVY = colors.HexColor('#243B53'); CREAM = colors.HexColor('#FFF8EE'); INK = colors.HexColor('#26384A')
MUTED = colors.HexColor('#6B7785'); GREEN = colors.HexColor('#27A6A1'); ORANGE = colors.HexColor('#F3B33D')
CORAL = colors.HexColor('#F27A62'); PURPLE = colors.HexColor('#8B6FC2'); PALE_GREEN = colors.HexColor('#DDF5F0')
PALE_ORANGE = colors.HexColor('#FFF1C9'); PALE_CORAL = colors.HexColor('#FFE3DC'); PALE_PURPLE = colors.HexColor('#EEE7FF')

def font(c, size, color=INK, bold=False, italic=False):
    c.setFont('Helvetica-Bold' if bold else ('Helvetica-Oblique' if italic else 'Helvetica'), size)
    c.setFillColor(color)

def para(c, txt, x, y, width, size=9.2, leading=13, color=INK, bold=False, italic=False):
    font(c, size, color, bold, italic)
    words = txt.split(); line=''; lines=[]
    for word in words:
        test = (line+' '+word).strip()
        if stringWidth(test, 'Helvetica-Bold' if bold else ('Helvetica-Oblique' if italic else 'Helvetica'), size) <= width:
            line=test
        else:
            if line: lines.append(line)
            line=word
    if line: lines.append(line)
    for i, line in enumerate(lines): c.drawString(x, y-i*leading, line)
    return y-len(lines)*leading

def title(c, text, subtitle=None):
    font(c, 24, NAVY, True); c.drawString(50, H-62, text)
    if subtitle: para(c, subtitle, 50, H-88, W-100, 10.5, 14, MUTED)

def footer(c, page):
    c.setStrokeColor(colors.HexColor('#DED7C9')); c.line(42, 30, W-42, 30)
    font(c, 7.5, MUTED); c.drawString(42, 18, 'UDYAN | FROM IDEA TO BUSINESS'); c.drawRightString(W-42, 18, str(page))

def card(c, x, y, w, h, heading, body, fill, accent):
    c.setFillColor(fill); c.setStrokeColor(accent); c.setLineWidth(1); c.roundRect(x, y-h, w, h, 8, fill=1, stroke=1)
    c.setFillColor(accent); c.rect(x, y-h, 5, h, fill=1, stroke=0)
    font(c, 11, NAVY, True); c.drawString(x+15, y-22, heading)
    para(c, body, x+15, y-42, w-28, 8.7, 12)

def phase_banner(c, num, heading, subtitle, color):
    c.setFillColor(color); c.roundRect(42, H-145, W-84, 73, 10, fill=1, stroke=0)
    font(c, 22, colors.white, True); c.drawString(58, H-101, 'PHASE '+num)
    font(c, 21, colors.white, True); c.drawString(155, H-101, heading)
    para(c, subtitle, 58, H-119, W-116, 9.2, 12, colors.white)

def table(c, x, y, widths, rows, row_h=40, header=True):
    total=sum(widths); yy=y
    for ri, row in enumerate(rows):
        fill = NAVY if ri==0 and header else (CREAM if ri%2 else colors.white)
        c.setFillColor(fill); c.setStrokeColor(colors.HexColor('#D7D9DE')); c.rect(x, yy-row_h, total, row_h, fill=1, stroke=1)
        xx=x
        for ci, cell in enumerate(row):
            c.setStrokeColor(colors.HexColor('#D7D9DE')); c.line(xx, yy, xx, yy-row_h)
            para(c, cell, xx+7, yy-15, widths[ci]-14, 7.6 if ri else 7.5, 10, colors.white if ri==0 and header else INK, ri==0 and header)
            xx += widths[ci]
        yy -= row_h
    return yy

def newpage(c, page):
    footer(c, page); c.showPage()

c=canvas.Canvas(OUT, pagesize=A4); c.setTitle('Udyan - From Idea to Business Proposal')
page=1
# 1 cover
c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
font(c, 28, NAVY, True); c.drawString(50, H-70, 'FROM IDEA TO BUSINESS')
para(c, 'A practical entrepreneurship course for Udyan students', 50, H-95, 240, 12, 16, INK)
para(c, 'Ash enters the business world with an exciting idea - and discovers that a business is not built by guessing. It is built by mapping a market, finding a valuable problem, making an offer, earning payment, and learning from what happens next.', 50, H-135, 240, 10.5, 15, NAVY, False, True)
c.drawImage(ImageReader(ART), 285, 370, width=265, height=205, preserveAspectRatio=True, mask='auto')
card(c, 50, 265, 500, 72, 'THE COURSE PROMISE', 'Every student leaves with real-world business experience: a specific opportunity, a tested offer, customer evidence, and a next build decision. The goal is not to protect students from uncertainty. It is to teach them how to navigate it.', PALE_ORANGE, ORANGE)
font(c, 10, MUTED); c.drawString(50, 175, 'A visual course proposal | Story structure + business outputs + experiential assessment')
footer(c,page); c.showPage(); page+=1
# 2 transformation
c.setFillColor(colors.white); c.rect(0,0,W,H,fill=1,stroke=0); title(c,'The transformation','Students arrive excited about entrepreneurship, but many have incomplete mental models of what a business is. The course turns that uncertainty into a sequence of real decisions.')
card(c, 50, H-145, 235, 170, 'BEFORE', '“I have an idea, but I do not know how to turn it into a business.”\n\nI want to build something cool, but I do not know who needs it, what they would pay, or what to do first.', PALE_CORAL, CORAL)
card(c, 310, H-145, 235, 170, 'AFTER', '“I can identify a customer problem, create an offer, test demand, sell it, build a first version, and adapt based on evidence.”', PALE_GREEN, GREEN)
font(c, 15, NAVY, True); c.drawCentredString(W/2, 430, 'THE CENTRAL LESSON')
para(c, 'A product idea is only a starting point. A business emerges when a person understands a valuable problem, creates a credible offer, earns a buying signal, and improves through real-world feedback.', 75, 400, W-150, 13, 18, NAVY, False, True)
card(c, 50, 270, 500, 80, 'WHAT STUDENTS PRACTISE', 'Choosing a market segment, finding a problem, estimating its value, shaping an offer, writing outreach, speaking with customers, asking for payment, delivering a first version, and deciding what to change.', PALE_PURPLE, PURPLE)
newpage(c,page); page+=1
# 3 journey overview
c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0); title(c,'The journey','The course is presented as a story. Ash is the student avatar: motivated, intelligent, and initially eager to build too soon. Each story beat corresponds to a real business capability and a visible artifact.')
table(c,50, H-145, [72,245,183], [['PHASE','ASH\'S STORY','STUDENT OUTPUT'],['1. MAP','Choose territory, find the dragon, measure the problem','Defined segment + validated problem'],['2. FORGE','Create the offer and prepare sales tools','Offer + value proposition + outreach kit'],['3. BATTLE','Reach customers, test demand, build, and learn','Buying signal + first delivery + iteration']], 47)
font(c, 14, NAVY, True); c.drawCentredString(W/2, 385, 'THE REPEATABLE LOOP')
para(c, 'Business capability is not a one-time victory. Students complete the loop once, then leave able to run it again with better evidence.', 70, 360, W-140, 10, 14, INK)
para(c, 'MAP  ->  FIND A PROBLEM  ->  FORGE AN OFFER  ->  APPROACH CUSTOMERS  ->  TEST PAYMENT  ->  BUILD  ->  LEARN  ->  UPDATE THE MAP', 60, 310, W-120, 11, 16, NAVY, True)
card(c, 50, 195, 500, 70, 'THE STORY RULE', 'Every story beat must correspond to a business decision. Every business decision must produce a visible artifact.', PALE_ORANGE, ORANGE)
newpage(c,page); page+=1
# phase 1
c.setFillColor(colors.white); c.rect(0,0,W,H,fill=1,stroke=0); phase_banner(c,'1','MAP THE TERRITORY','Ash begins with a product idea. The market is covered in fog. Before building, Ash must discover who is in the territory and which problem is worth solving.',GREEN)
font(c, 14, NAVY, True); c.drawString(50, H-180, 'PROBLEM BEING SOLVED')
para(c, '“I have an idea, but I do not know who it is for, whether the problem is real, or whether it is valuable enough to build around.”', 60, H-210, W-120, 11, 15, NAVY, False, True)
rows=[['SUBPHASE','WHAT ASH DOES','CHECKPOINT'],['Understand business','Separate an idea, product, offer, and business. Learn how value is created and how money enters the system.','Business direction + revenue logic.'],['Choose a territory','Move from broad interest to a specific market segment with reachable customers.','Defined segment + customer profile.'],['Find the dragon','Conduct customer conversations and distinguish recurring pain from opinions.','Evidence-backed problem statement.'],['Measure the dragon','Estimate frequency, urgency, alternatives, and financial cost.','Quantified problem worth investigating.']]
table(c,50,H-240,[110,270,120],rows,52)
card(c,50,190,500,75,'STORY TO BUSINESS','Ash maps a continent. The student narrows a broad interest into a market segment. Ash follows clues through the fog. The student conducts customer conversations. The dragon becomes visible. The student states a costly, recurring problem with evidence.',PALE_GREEN,GREEN)
newpage(c,page); page+=1
# phase 2
c.setFillColor(colors.white); c.rect(0,0,W,H,fill=1,stroke=0); phase_banner(c,'2','FORGE THE WEAPON','Ash has found a real problem. Now the weapon must be designed for this particular fight. The weapon is not merely a product - it is the complete offer.',ORANGE)
font(c, 14, NAVY, True); c.drawString(50, H-180, 'PROBLEM BEING SOLVED')
para(c, '“I understand the problem, but I do not know exactly what to sell, what result to promise, how to deliver it, or how to price it.”', 60, H-210, W-120, 11, 15, NAVY, False, True)
rows=[['SUBPHASE','WHAT ASH DOES','CHECKPOINT'],['Define the result','Translate the problem into a specific result the customer wants and can recognise.','Clear customer outcome.'],['Shape the value proposition','Explain who the offer is for, what it changes, and why it matters.','Concise value proposition.'],['Build the offer','Set the customer, result, scope, delivery method, and price logic.','Concrete offer someone could buy.'],['Prepare the sales kit','Create copy, outreach messages, proposals, and tools needed to approach customers.','Usable sales and marketing kit.']]
table(c,50,H-240,[110,270,120],rows,52)
card(c,50,190,500,75,'THE OFFER LOADOUT','Target = customer segment | Enemy = customer problem | Mission = promised result | Weapon = solution | Ammunition = deliverables | Deployment = delivery method | Cost = price',PALE_ORANGE,ORANGE)
newpage(c,page); page+=1
# phase 3
c.setFillColor(colors.white); c.rect(0,0,W,H,fill=1,stroke=0); phase_banner(c,'3','ENTER THE BATTLE','The weapon has never been tested. Ash must approach real customers, ask for commitment, deliver a first version, and learn what needs to change.',CORAL)
font(c, 14, NAVY, True); c.drawString(50, H-180, 'PROBLEM BEING SOLVED')
para(c, '“I have an offer, but I do not know whether people will buy it, whether I can deliver it, or what needs to change.”', 60, H-210, W-120, 11, 15, NAVY, False, True)
rows=[['SUBPHASE','WHAT ASH DOES','CHECKPOINT'],['Find the dragon','Build a target list and identify reachable prospects.','Prioritised outreach plan.'],['Approach the dragon','Send messages, start conversations, listen for signals, and handle rejection.','Completed outreach + conversations.'],['Test the weapon','Present the offer and ask for payment, pre-sale, deposit, or commitment.','Evidence of demand.'],['Fight the first battle','Deliver the smallest version that can produce the promised result.','First delivery or prototype.'],['Study the battle','Use feedback to change the customer, problem, offer, price, or solution.','Revised offer + next build plan.']]
table(c,50,H-240,[110,270,120],rows,45)
card(c,50,160,500,82,'THE FIRST BATTLE IS NOT THE FINAL VICTORY','The first version may misfire. Customers may ignore it, misunderstand it, or ask for something different. That is not a course failure. The student is assessed on whether they learn, adapt, and make the next decision from evidence.',PALE_CORAL,CORAL)
newpage(c,page); page+=1
# teaching model
c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0); title(c,'How the course is taught','The course is hybrid: written lessons establish concepts, short Loom videos make the thinking visible, and attached GPTs help students practise and improve real work.')
rows=[['STEP','WHAT HAPPENS'],['Written lesson','A focused idea, misconception, or framework.'],['Ash\'s story beat','The concept appears as a decision Ash must make.'],['GPT practice','Students draft, role-play, critique, or test the idea with AI.'],['Real-world task','Students speak to customers, write outreach, or test an offer.'],['Artifact submission','The work becomes evidence of business capability.'],['Feedback and iteration','AI and human feedback improve the next version.']]
table(c,50,H-150,[150,350],rows,48)
card(c,50,235,500,70,'THE TEACHING PRINCIPLE','Every story beat should lead to a business decision. Every decision produces an artifact. Every artifact improves through evidence.',PALE_PURPLE,PURPLE)
para(c, 'Written lesson  ->  Loom  ->  GPT practice  ->  Real-world task  ->  Artifact  ->  Feedback  ->  Iteration', 65, 135, W-130, 10, 14, NAVY, True)
newpage(c,page); page+=1
# final outputs
c.setFillColor(colors.white); c.rect(0,0,W,H,fill=1,stroke=0); title(c,'What every student must leave with','The course does not promise that every idea will succeed. It promises that every student will experience the business cycle and leave with stronger evidence about what to do next.')
rows=[['ARTIFACT','WHAT IT PROVES'],['Market territory','A specific segment and customer group.'],['Problem evidence','Customer conversations and a meaningful problem statement.'],['Problem value','A view of urgency, cost, and existing alternatives.'],['Offer','Customer, result, scope, delivery method, and price logic.'],['Sales kit','Copy, outreach messages, and a simple way to present the offer.'],['Demand test','A real buying signal, pre-sale attempt, or documented market response.'],['First build','The smallest useful version delivered or tested.'],['Iteration decision','A revised offer and evidence-based next build plan.']]
table(c,50,H-145,[165,335],rows,39)
font(c, 14, NAVY, True); c.drawCentredString(W/2, 210, 'THE FINAL CAPABILITY')
para(c, 'Students should be able to repeat the loop: enter an unfamiliar market, find a valuable problem, make an offer, ask for payment, deliver, learn, and adapt. That is the durable skill the course is designed to build.', 70, 180, W-140, 11, 16, NAVY, False, True)
card(c,50,112,500,58,'THE COURSE IN ONE SENTENCE','Ash enters with an idea and leaves able to turn uncertainty into evidence, offers, and real customer value.',PALE_GREEN,GREEN)
footer(c,page); c.save(); print(OUT)
