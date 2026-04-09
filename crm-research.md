# XASCOM CRM & Analytics Dashboard - Deep Research

## Google Sheet Analysis: "FEB'24 RENEWAL BASE"

### Sheet Structure (Columns A-X+)
- A: SL.NO | B: POLICY NO (11220015036402 format)
- C: MONTH (DEC'22, JAN 23) | D: DATE (original commencement)
- E: COMPANY (STAR = Star Health) | F: FRESH/RENEWAL
- G: WEEK | H: START DATE | I: END DATE (policy validity)
- J: CUSTOMER NAME | K: MOBILE
- L: NEW GROSS | M: GROSS PREMIUM (shows premium change between years)
- N: PRODUCT (COMP, FHO, SCRC, PA, ASSURE, Arogya Sanjeevani, Young Star, Out Patient Care)
- O: ISSUANCE DATE | P: SUM INSURED (3L to 5Cr)
- Q: NEW NET | R: NOP (always 1)
- S: Assigned (mostly empty) | T: RENEWED | U: STATUS
- V: FEROZ FEEDBACK | W: PRIYA FEEDBACK

### Key Sheet Naming Pattern
"FEB'24 RENEWAL BASE" = policies expiring in Feb 2024 from Star Health
Implication: ~192 sheets/year (12 months × 16 carriers)

### Real Feedback Cell Examples (the core problem)
- "MONEY ISSUES/NEED SOMETIME/24/02/2024 CALL BACK @3CLK /CALL BACK AFTER SOMETIME MONEY ISSUES"
- "CLAIM ISSUES/NEED FEEDBACK AFTER THAT WILL RENEW THE POLICY"
- "23/02/2024 CALL BACK(OUT OF STATION)"
- "RNR/NOT INTEREST TO PAY/DONT TELL ANY REASON"
- "EMPLOYEE EXIT/OFZ INSURANCE"
- "NO:391/3A,VASANTHAN NAGAR,PERIYAR NAGAR SOUTH,VIRUDHACHALAM,606001" (address in feedback!)
- "WILL CALL BACK 5 CLK"
- "SOURCED/PROPOSER CHANGE"

### Observed STATUS values (unstructured)
Outcomes: RENEWED (DEC), RENEWED (JAN), NOT RENEWED
Dispositions: CALL BACK, RNR, CUT THE CALL
Reasons: CLAIM ISSUE, EMPLOYEE EXIT, NOT INTEREST, MONEY ISSUES

### Product codes found
COMP (Comprehensive), FHO (Family Health Optima), SCRC, PA (Personal Accident), 
ASSURE, Arogya Sanjeevani, Young Star, Out Patient Care

### Premium ranges observed
Sum Insured: 3L to 5Cr  
Gross Premium: ~900 to ~40,000+

---

## Gaps Found in Other AI's Plan

### CRITICAL GAPS (must have):
1. **No saved carrier mapping templates** - must remember Star Health column layout forever after first mapping
2. **No call attempt counter** - feedback overwrites previous; zero visibility into attempts
3. **No grace period tracking** - 15-30 day grace period after expiry = highest urgency
4. **No disposition/outcome/reason separation** - currently all mixed in one cell
5. **No premium change indicator** - agents need to see "premium up 15%" BEFORE calling
6. **No daily call targets** - management can't set "40 calls/day per agent"
7. **No SLA/aging tracking** - leads uncontacted for 3+ days should be flagged
8. **No customer deduplication** - same customer may have policies across carriers
9. **No commission slab calculation** - different carriers have different commission rates
10. **No export functionality** - MIS reports, carrier reports

### IMPORTANT GAPS (should have):
11. **No bulk WhatsApp/SMS** - pre-warm leads before calling
12. **No manager notes/escalation** - VIP customer handling
13. **No premium-based prioritization** - ₹5L policy is 50x more valuable than ₹10K
14. **No callback calendar view** - only list view mentioned
15. **No FRESH vs RENEWAL workflow split** - different approaches needed
16. **No lost revenue dashboard** - "₹2.5L commission lost this month" = powerful motivator
17. **No duplicate phone detection** - same number across policies
18. **No auto-archival** - old month data should auto-archive

### NICE-TO-HAVE GAPS:
19. Mobile-friendly agent view
20. Family policy linking
21. Customer communication timeline (all channels)
22. Renewal prediction (ML-based)
23. Quick reference product cards for agents
24. Offline queue capability

---

## Industry Research Insights (from LeadSquared Insurance CRM)
- Lead scoring and prioritization is standard
- Day planner for agents (calendar + list)
- Automated renewal reminders via SMS/WhatsApp/Email
- Cross-sell/upsell engine based on customer profile
- Real-time reports for call center and field agents
- Complete customer 360-degree view
- Agent performance tracking across products/carriers
- Escalation workflows (uncontacted leads auto-escalate)

---

## Presentation Plan (CRM Proposal)
Will create multi-page HTML presentation matching Project 1 style:
1. Cover + ToC
2. Current Workflow Problem Analysis (with sheet screenshots reference)
3. Solution Overview + Features
4. Tech Stack & Architecture
5. Timeline & Pricing
