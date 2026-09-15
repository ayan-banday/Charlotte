import fs from "fs";
import fsp from "fs/promises";
import path from "path";
import { pathToFileURL } from "url";
import {
  Presentation,
  PresentationFile,
} from "@oai/artifact-tool";

process.env.RUNTIME_NODE_MODULES = "C:/Users/ayanb/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules";
const buildDir = "S:/Charlotte/.codex-build/mni-v6";
const candidate = path.join(buildDir, "candidate.pptx");
const output = "S:/Charlotte/02 Projects/Venture-Scale Opportunity/output/Market-Narrative-Intelligence-Pitch-Deck-v6-final-2.pptx";
fs.mkdirSync(buildDir, { recursive: true });

const skillDir = "C:/Users/ayanb/.codex/plugins/cache/openai-primary-runtime/presentations/26.904.11930/skills/presentations";
const { resolvePresentationFont, finalizePresentation } = await import(pathToFileURL(
  path.join(skillDir, "container_tools/artifact_tool_utils.mjs"),
).href);
const family = resolvePresentationFont();

const C = {
  paper: "#FAFAF8",
  ink: "#172938",
  teal: "#63C7B5",
  tealDark: "#208F82",
  tealPale: "#E7F6F2",
  coral: "#F16154",
  coralPale: "#FDEBE8",
  line: "#D8E0DE",
  grey: "#6D7B83",
  pale: "#F2F5F3",
  white: "#FFFFFF",
};

const p = Presentation.create({ slideSize: { width: 1280, height: 720 } });

function shape(slide, left, top, width, height, fill = "none", line = { style: "solid", fill: "none", width: 0 }, geometry = "rect", radius = undefined) {
  return slide.shapes.add({
    geometry,
    position: { left, top, width, height },
    fill,
    line,
    ...(radius ? { borderRadius: radius } : {}),
  });
}

function text(slide, value, left, top, width, height, {
  size = 22,
  color = C.ink,
  bold = false,
  align = "left",
  valign = "top",
  italic = false,
  letterSpacing,
} = {}) {
  const s = shape(slide, left, top, width, height, "none", { style: "solid", fill: "none", width: 0 }, "textbox");
  s.text = value;
  s.text.style = {
    typeface: family,
    fontSize: size,
    color,
    bold,
    italic,
    align,
    verticalAlignment: valign,
    ...(letterSpacing !== undefined ? { letterSpacing } : {}),
  };
  return s;
}

function line(slide, left, top, width, color = C.line, weight = 1) {
  return shape(slide, left, top, width, 0, "none", { style: "solid", fill: color, width: weight }, "line");
}

function title(slide, value, { top = 110, width = 690, size = 45, dark = false } = {}) {
  return text(slide, value, 60, top, width, 122, { size, color: dark ? C.white : C.ink, bold: true });
}

function kicker(slide, value, { dark = false } = {}) {
  text(slide, value.toUpperCase(), 60, 58, 500, 24, { size: 14, color: dark ? "#D8FFF6" : C.coral, bold: true, letterSpacing: 1.3 });
}

function footer(slide, n, { dark = false, note = "" } = {}) {
  if (note) text(slide, note, 60, 678, 680, 18, { size: 10, color: dark ? "#D8FFF6" : C.grey });
  text(slide, String(n).padStart(2, "0"), 1175, 673, 45, 20, { size: 12, color: dark ? "#D8FFF6" : C.grey, align: "right", bold: true });
}

function note(slide, value) {
  slide.speakerNotes.textFrame.setText(value);
}

function dot(slide, x, y, fill, size = 10) {
  return shape(slide, x, y, size, size, fill, { style: "solid", fill, width: 0 }, "ellipse");
}

function tag(slide, value, left, top, width, fill, color) {
  shape(slide, left, top, width, 28, fill, { style: "solid", fill, width: 0 }, "rect", "rounded-full");
  text(slide, value.toUpperCase(), left + 12, top + 6, width - 24, 16, { size: 11, color, bold: true, align: "center", letterSpacing: 0.8 });
}

// 01
{
  const s = p.slides.add();
  shape(s, 0, 0, 1280, 720, C.teal, { style: "solid", fill: C.teal, width: 0 });
  kicker(s, "Discovery deck", { dark: true });
  text(s, "The Promise\nProblem", 60, 142, 675, 190, { size: 70, color: C.white, bold: true });
  line(s, 60, 370, 150, "#D8FFF6", 3);
  text(s, "A grant-stage test of how B2B teams learn from buyer response.", 60, 402, 575, 58, { size: 25, color: C.white });
  text(s, "“We will add five new members every month\nwithout cutting prices.”", 775, 180, 410, 118, { size: 26, color: C.ink, bold: true });
  text(s, "The campaign ends.\nThe promise should not.", 775, 342, 360, 90, { size: 30, color: C.white, bold: true });
  footer(s, 1, { dark: true });
  note(s, "Internal deck. The example promise is illustrative, not a customer claim. Narrative premise informed by Market Narrative Intelligence Presentation Draft.md and 01 Brain Dump and Unstructured Thinking.md.");
}

// 02
{
  const s = p.slides.add();
  kicker(s, "A simple buyer moment");
  title(s, "One promise enters the market");
  text(s, "Brightside Growth tells a gym owner:", 60, 250, 360, 30, { size: 20, color: C.grey });
  shape(s, 475, 168, 650, 280, C.tealPale, { style: "solid", fill: "#B7E9DF", width: 1 }, "rect", "rounded-2xl");
  text(s, "We will add five new members every month without cutting prices.", 535, 228, 535, 104, { size: 34, color: C.ink, bold: true });
  line(s, 535, 365, 225, C.teal, 4);
  text(s, "A clear commercial promise.", 535, 390, 330, 26, { size: 17, color: C.tealDark, bold: true });
  footer(s, 2, { note: "ILLUSTRATIVE EXAMPLE" });
  note(s, "Illustrative example used to make the buyer-learning problem concrete. It is not customer evidence.");
}

// 03
{
  const s = p.slides.add();
  kicker(s, "The buyer response");
  title(s, "The buyer tests the promise");
  text(s, "A buyer does not respond to a campaign. They test the claim inside it.", 60, 246, 440, 70, { size: 24, color: C.grey });
  shape(s, 615, 170, 450, 108, C.coralPale, { style: "solid", fill: "#F5BBB4", width: 1 }, "rect", "rounded-2xl");
  text(s, "Will they stay?", 660, 204, 340, 38, { size: 31, color: C.ink, bold: true });
  shape(s, 695, 325, 450, 108, C.pale, { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
  text(s, "Have you done this for a gym like mine?", 735, 351, 360, 54, { size: 26, color: C.ink, bold: true });
  text(s, "The question shows the proof gap.", 615, 505, 430, 30, { size: 19, color: C.tealDark, bold: true });
  footer(s, 3, { note: "ILLUSTRATIVE EXAMPLE" });
  note(s, "Illustrative example. The core framing, marketing and sales as phases of one promise, derives from 01 Brain Dump and Unstructured Thinking.md.");
}

// 04
{
  const s = p.slides.add();
  kicker(s, "What breaks");
  title(s, "The answer breaks into pieces");
  text(s, "One buyer story. Three separate systems.", 60, 250, 380, 35, { size: 23, color: C.grey });
  const xs = [500, 750, 1000];
  const labels = ["Campaign", "Sales call", "CRM"];
  const descriptions = ["Promise", "Buyer doubt\nand response", "Outcome\nand reason"];
  const fills = [C.tealPale, C.coralPale, C.pale];
  for (let i = 0; i < 3; i++) {
    shape(s, xs[i], 220, 190, 180, fills[i], { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
    text(s, labels[i], xs[i] + 22, 246, 150, 25, { size: 16, color: C.grey, bold: true });
    text(s, descriptions[i], xs[i] + 22, 302, 145, 70, { size: 21, color: C.ink, bold: true });
  }
  line(s, 690, 310, 45, C.coral, 3);
  line(s, 940, 310, 45, C.coral, 3);
  text(s, "No system owns the full promise.", 500, 472, 500, 35, { size: 23, color: C.ink, bold: true });
  footer(s, 4);
  note(s, "Problem statement synthesized from 01 Brain Dump and Unstructured Thinking.md and 04 Market Narrative Intelligence Presentation Draft.md. The split between campaign, sales, and CRM is the product hypothesis, not a validated market fact.");
}

// 05
{
  const s = p.slides.add();
  kicker(s, "The cost of the split");
  title(s, "More activity repeats the same mistake");
  text(s, "More messages, dashboards, and AI drafts still repeat an unproven promise.", 60, 250, 450, 68, { size: 24, color: C.grey });
  shape(s, 610, 180, 245, 260, C.pale, { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
  text(s, "May", 640, 214, 100, 25, { size: 15, color: C.grey, bold: true });
  text(s, "Five new\nmembers\nevery month", 640, 270, 165, 90, { size: 29, color: C.ink, bold: true });
  shape(s, 930, 180, 245, 260, C.pale, { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
  text(s, "June", 960, 214, 100, 25, { size: 15, color: C.grey, bold: true });
  text(s, "Five new\nmembers\nevery month", 960, 270, 165, 90, { size: 29, color: C.ink, bold: true });
  text(s, "same promise", 848, 308, 80, 20, { size: 14, color: C.coral, bold: true, align: "center" });
  line(s, 855, 348, 65, C.coral, 3);
  text(s, "The campaign ends.\nThe promise should not.", 610, 478, 510, 72, { size: 25, color: C.ink, bold: true });
  footer(s, 5, { note: "ILLUSTRATIVE EXAMPLE" });
  note(s, "Illustrative example. Claim is a framing statement, not a quantified performance claim. This slide deliberately avoids asserting that existing tools are ineffective.");
}

// 06
{
  const s = p.slides.add();
  kicker(s, "The reframe");
  title(s, "Promise, not campaign");
  text(s, "The campaign is a container. The promise travels through it.", 60, 246, 495, 64, { size: 26, color: C.grey });
  text(s, "Campaign-led", 620, 170, 220, 24, { size: 16, color: C.coral, bold: true });
  text(s, "Promise-led", 930, 170, 220, 24, { size: 16, color: C.tealDark, bold: true });
  shape(s, 610, 220, 250, 250, C.coralPale, { style: "solid", fill: "#F6C8C1", width: 1 }, "rect", "rounded-2xl");
  text(s, "Launch\nMeasure\nArchive\nRepeat", 650, 260, 160, 145, { size: 27, color: C.ink, bold: true });
  shape(s, 920, 220, 270, 250, C.tealPale, { style: "solid", fill: "#B7E9DF", width: 1 }, "rect", "rounded-2xl");
  text(s, "Make promise\nCapture buyer test\nLink outcome\nChange next decision", 952, 255, 200, 168, { size: 22, color: C.ink, bold: true });
  footer(s, 6);
  note(s, "Product reframe from user direction and 04 Market Narrative Intelligence Presentation Draft.md. The two workflows are conceptual contrasts, not benchmark data.");
}

// 07
{
  const s = p.slides.add();
  kicker(s, "The product");
  title(s, "Every promise needs a record");
  tag(s, "Market Narrative Intelligence", 60, 235, 305, C.teal, C.ink);
  text(s, "Market Narrative Intelligence connects the promise, proof, buyer doubt, and revenue result in one editable record.", 60, 295, 425, 104, { size: 24, color: C.grey });
  shape(s, 560, 160, 590, 385, C.white, { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
  text(s, "PROMISE RECORD", 595, 192, 270, 20, { size: 13, color: C.tealDark, bold: true, letterSpacing: 1 });
  const rows = [
    ["Promise", "Five new members every month"],
    ["Proof needed", "Retention after month three"],
    ["Buyer asked", "Will they stay?"],
    ["CRM result", "Outcome and loss reason"],
    ["Next decision", "Change the next promise"],
  ];
  rows.forEach((r, i) => {
    const y = 235 + i * 57;
    text(s, r[0], 595, y, 130, 18, { size: 14, color: C.grey, bold: true });
    text(s, r[1], 740, y - 2, 360, 25, { size: 18, color: C.ink, bold: i === 4 });
    if (i < rows.length - 1) line(s, 595, y + 35, 505, C.line, 1);
  });
  footer(s, 7, { note: "ILLUSTRATIVE EXAMPLE" });
  note(s, "Product concept grounded in 04 Market Narrative Intelligence Presentation Draft.md: a system of record connecting promise, proof, objections, buyer response and outcome. Example contents are illustrative.");
}

// 08
{
  const s = p.slides.add();
  kicker(s, "What changes");
  title(s, "The next campaign changes for a reason");
  text(s, "The buyer question and the CRM result change the promise, not just the report.", 60, 248, 420, 85, { size: 23, color: C.grey });
  text(s, "Before", 590, 182, 120, 22, { size: 15, color: C.grey, bold: true });
  shape(s, 590, 220, 260, 148, C.pale, { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
  text(s, "Five new\nmembers every month", 618, 257, 210, 70, { size: 26, color: C.ink, bold: true });
  text(s, "Buyer asked about retention", 875, 260, 220, 45, { size: 17, color: C.coral, bold: true, align: "center" });
  line(s, 860, 335, 240, C.coral, 3);
  text(s, "After", 875, 397, 120, 22, { size: 15, color: C.grey, bold: true });
  shape(s, 875, 425, 300, 190, C.tealPale, { style: "solid", fill: "#B7E9DF", width: 1 }, "rect", "rounded-2xl");
  text(s, "Five new members\nwho stay past\nmonth three", 905, 457, 240, 120, { size: 24, color: C.ink, bold: true });
  footer(s, 8, { note: "ILLUSTRATIVE EXAMPLE" });
  note(s, "Illustrative example. It demonstrates the core product claim that commercial learning should change the next decision. It does not state an observed customer result.");
}

// 09
{
  const s = p.slides.add();
  kicker(s, "Why now");
  title(s, "Evidence\nalready exists", { width: 620 });
  text(s, "Campaign assets, sales calls, and CRM outcomes contain the missing link.", 60, 246, 450, 72, { size: 24, color: C.grey });
  const xs = [550, 760, 970];
  const labels = ["Campaign assets", "Sales calls", "CRM outcomes"];
  const details = ["What was promised", "What buyers tested", "What happened"];
  xs.forEach((x, i) => {
    dot(s, x + 78, 230, i === 1 ? C.coral : C.teal, 18);
    text(s, labels[i], x, 280, 175, 26, { size: 18, color: C.ink, bold: true, align: "center" });
    text(s, details[i], x, 315, 175, 24, { size: 15, color: C.grey, align: "center" });
  });
  line(s, 600, 410, 480, C.line, 2);
  shape(s, 695, 450, 300, 88, C.tealPale, { style: "solid", fill: "#B7E9DF", width: 1 }, "rect", "rounded-2xl");
  text(s, "One promise record", 725, 477, 240, 32, { size: 25, color: C.ink, bold: true, align: "center" });
  footer(s, 9);
  note(s, "Source-system framing from 00 Introduction to Venture-Scale Opportunity.md and 04 Market Narrative Intelligence Presentation Draft.md. Availability and access quality must be validated in pilot work.");
}

// 10
{
  const s = p.slides.add();
  kicker(s, "The benchmark");
  title(s, "An analyst rebuilds the story today");
  text(s, "Teams export data, replay calls, and write a new brief by hand.", 60, 246, 420, 68, { size: 24, color: C.grey });
  const cols = [
    ["CRM export", "Outcome\nand reason"],
    ["Call review", "Buyer question\nand response"],
    ["Campaign review", "Promise\nand proof"],
  ];
  cols.forEach((col, i) => {
    const x = 500 + i * 210;
    shape(s, x, 205, 175, 155, C.pale, { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
    text(s, col[0], x + 18, 235, 140, 24, { size: 17, color: C.grey, bold: true });
    text(s, col[1], x + 18, 287, 140, 60, { size: 18, color: C.ink, bold: true });
  });
  shape(s, 710, 435, 370, 95, C.coralPale, { style: "solid", fill: "#F5BBB4", width: 1 }, "rect", "rounded-2xl");
  text(s, "Analyst + general AI\ncreates the next brief", 745, 456, 300, 52, { size: 22, color: C.ink, bold: true, align: "center" });
  text(s, "This is the benchmark.", 60, 507, 365, 30, { size: 23, color: C.tealDark, bold: true });
  footer(s, 10);
  note(s, "Competitive baseline is drawn from 03 Marketing Intelligence Competitive Landscape.md. The document identifies the key substitute as internal stack + analyst + general LLM. This slide does not claim superiority.");
}

// 11
{
  const s = p.slides.add();
  kicker(s, "The first user");
  title(s, "Start before the next campaign goes live");
  text(s, "A growth lead at a 20–75-person performance-marketing agency using HubSpot.", 60, 246, 480, 74, { size: 24, color: C.grey });
  const roles = [
    ["Growth lead", "Chooses\nthe next move"],
    ["Agency owner", "Pays for\nthe result"],
    ["CRM owner", "Grants\ndata access"],
  ];
  roles.forEach((role, i) => {
    const x = 560 + i * 205;
    dot(s, x + 72, 225, i === 0 ? C.teal : C.ink, 16);
    text(s, role[0], x, 275, 160, 25, { size: 18, color: C.ink, bold: true, align: "center" });
    text(s, role[1], x, 316, 160, 52, { size: 18, color: C.grey, bold: true, align: "center" });
  });
  line(s, 560, 410, 570, C.line, 2);
  text(s, "Run the first review when a live commercial decision still matters.", 560, 450, 550, 44, { size: 22, color: C.ink, bold: true, align: "center" });
  footer(s, 11);
  note(s, "Customer target from 00 Introduction to Venture-Scale Opportunity.md. This is a chosen starting segment and role map for pilot recruitment, not a signed customer profile.");
}

// 12
{
  const s = p.slides.add();
  kicker(s, "The test");
  title(s, "Use the same evidence. Make a better decision.");
  text(s, "The pilot compares workflows on source traceability, decision change, and right-fit pipeline.", 60, 244, 480, 75, { size: 23, color: C.grey });
  const cols = [
    ["Current workflow", "Separate tools\nSeparate handoffs\nSeparate reports", C.pale],
    ["Analyst + general AI", "Rebuilds the story\nby hand\nCreates a brief", C.coralPale],
    ["MNI", "One promise record\nEvidence linked\nNext decision shown", C.tealPale],
  ];
  cols.forEach((c, i) => {
    const x = 545 + i * 210;
    shape(s, x, 175, 185, 300, c[2], { style: "solid", fill: C.line, width: 1 }, "rect", "rounded-2xl");
    text(s, c[0], x + 18, 210, 150, 45, { size: 18, color: C.ink, bold: true, align: "center" });
    line(s, x + 28, 275, 130, i === 2 ? C.teal : C.line, 2);
    text(s, c[1], x + 18, 305, 150, 98, { size: 19, color: C.ink, bold: true, align: "center" });
  });
  text(s, "Same inputs. Different record. Compare the decision.", 545, 535, 610, 30, { size: 21, color: C.tealDark, bold: true, align: "center" });
  footer(s, 12);
  note(s, "Evaluation design derived from 03 Marketing Intelligence Competitive Landscape.md, which identifies speed, traceability, decision quality and qualified revenue as areas the product must beat or prove. No outcome is claimed before the pilot.");
}

// 13
{
  const s = p.slides.add();
  kicker(s, "The proof path");
  title(s, "The pilot earns the next step");
  text(s, "Build a small test that creates one clear decision, not a long implementation.", 60, 246, 450, 72, { size: 24, color: C.grey });
  const metrics = [["2", "teams"], ["3", "source types"], ["1", "live decision\nper team"]];
  metrics.forEach((m, i) => {
    const x = 565 + i * 205;
    text(s, m[0], x, 195, 170, 84, { size: 62, color: i === 1 ? C.coral : C.tealDark, bold: true, align: "center" });
    text(s, m[1], x, 290, 170, 46, { size: 19, color: C.ink, bold: true, align: "center" });
  });
  line(s, 585, 405, 520, C.line, 2);
  const phases = [["Reconstruct", "Link one promise\nto its evidence"], ["Run", "Use it in a live\ncommercial choice"], ["Compare", "Pursue, probe,\nor pass"]];
  phases.forEach((ph, i) => {
    const x = 560 + i * 205;
    dot(s, x + 72, 397, i === 2 ? C.coral : C.teal, 18);
    text(s, ph[0], x, 435, 170, 24, { size: 18, color: C.ink, bold: true, align: "center" });
    text(s, ph[1], x, 470, 170, 45, { size: 16, color: C.grey, align: "center" });
  });
  footer(s, 13);
  note(s, "Pilot scope from 00 Introduction to Venture-Scale Opportunity.md and 04 Market Narrative Intelligence Presentation Draft.md: two or three B2B teams and three source types. This deck uses two teams as a deliberately small starting scope.");
}

// 14
{
  const s = p.slides.add();
  kicker(s, "The venture path");
  title(s, "The record earns its expansion");
  text(s, "The same record must help the next commercial decision before the product moves to another one.", 60, 246, 460, 84, { size: 23, color: C.grey });
  const labels = ["Demand\ncampaign", "Product\nlaunch", "Sales\nproof", "Renewal\noffer"];
  labels.forEach((label, i) => {
    const x = 545 + i * 165;
    const fill = i === 0 ? C.tealPale : C.pale;
    shape(s, x, 220, 135, 135, fill, { style: "solid", fill: i === 0 ? "#B7E9DF" : C.line, width: 1 }, "rect", "rounded-2xl");
    text(s, label, x + 14, 260, 107, 55, { size: 18, color: C.ink, bold: true, align: "center" });
  });
  text(s, "Same promise record", 545, 410, 630, 30, { size: 23, color: C.tealDark, bold: true, align: "center" });
  line(s, 595, 455, 530, C.teal, 3);
  text(s, "Expansion follows proof, not a category claim.", 545, 510, 630, 32, { size: 22, color: C.ink, bold: true, align: "center" });
  footer(s, 14);
  note(s, "Expansion logic follows 04 Market Narrative Intelligence Presentation Draft.md: land on campaigns, then expand only if the same promise record transfers across product launches, sales proof and renewal offers. This is a conditional venture path, not a market-size claim.");
}

// 15
{
  const s = p.slides.add();
  shape(s, 0, 0, 1280, 720, C.ink, { style: "solid", fill: C.ink, width: 0 });
  kicker(s, "The ask", { dark: true });
  title(s, "Give us two teams\nand one decision each", { top: 125, width: 720, size: 57, dark: true });
  text(s, "By September 30: a Pursue, Probe, or Pass decision backed by reconstructed buyer evidence.", 60, 315, 590, 70, { size: 24, color: "#D6E2DE" });
  const asks = [
    ["Two introductions", "Performance marketing\nagencies"],
    ["Three source types", "Campaigns, calls, CRM"],
    ["Mentor supervision", "Review the commercial decision"],
    ["Prototype resource", "Build the promise record"],
  ];
  asks.forEach((a, i) => {
    const x = 725 + (i % 2) * 230;
    const y = 155 + Math.floor(i / 2) * 190;
    shape(s, x, y, 200, 145, i === 0 ? C.teal : "#223746", { style: "solid", fill: i === 0 ? C.teal : "#334A59", width: 1 }, "rect", "rounded-2xl");
    text(s, a[0], x + 18, y + 25, 165, 44, { size: 20, color: i === 0 ? C.ink : C.white, bold: true });
    text(s, a[1], x + 18, y + 87, 165, 38, { size: 15, color: i === 0 ? C.ink : "#D6E2DE" });
  });
  footer(s, 15, { dark: true });
  note(s, "Ask and September 30 decision point from 00 Introduction to Venture-Scale Opportunity.md. The ask is scoped for professors and discovery support, not an investment round.");
}

await (await PresentationFile.exportPptx(p)).save(candidate);

const requirements = {
  explicitTotalSlideCount: 15,
  requiredNativeChartOwnerSlides: [],
  requiredNativeTableOwnerSlides: [],
};
const fontPolicy = { basis: "design", families: [family] };
const stagingDir = path.join(buildDir, "finalizer");
await fsp.mkdir(stagingDir, { recursive: true });
await fsp.mkdir(path.dirname(output), { recursive: true });
await finalizePresentation({
  ...requirements,
  workspaceDir: "S:/Charlotte",
  candidatePath: candidate,
  finalPath: output,
  pythonExecutable: "C:/Users/ayanb/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe",
  integrityValidatorPath: path.join(skillDir, "container_tools/inspect_presentation_package_integrity.py"),
  layoutValidatorPath: path.join(skillDir, "container_tools/inspect_presentation_layout_geometry.py"),
  layoutArgs: ["--expected-slide-size-emu", "12192000,6858000", "--validate-bullet-geometry", "--validate-heading-fit"],
  requiredNativeTableOwnerSlides: [],
  fontPolicy,
  verifyArtifactToolImport: true,
  receiptPath: path.join(stagingDir, "Market-Narrative-Intelligence-Pitch-Deck-v6-final-2.validation.json"),
});

console.log(JSON.stringify({ candidate, output, font: family }, null, 2));
