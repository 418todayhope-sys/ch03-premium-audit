# Classification and payroll audit report

VERIFIED describes evidence-supported calculations, not final audit approval. OPEN wages and unresolved payment basis remain separate. UNAPPROVED PROPOSED treatments are excluded from every verified CSV and total. All linked questions remain unanswered.

Responsible policy reviewer: auditor assigned to this file. Employer payroll/records contact confirms duties, identities, payment purposes and source completeness; the auditor decides rule applicability and approves any proposed treatment. Named policy authorities retain their original interview citations below; those citations do not appoint a reviewer for a new audit. No stakeholder has been contacted by this generator.

Review state: /home/maxg/ch03-premium-audit/deliverables/classification-review.json. SHA-256 2c2b20f534cd015aa186778713ac0a1a2f3785fc0dbd001cb9c4dcfa273a57a8.

Question document: [audit-questions.md](audit-questions.md); SHA-256 7c23a93a86af5735976f2e0b748cda8e836f772324c94be46cb0d9a640ef7ce3.

## Employer conclusions

| Employer | Submitted split | Verified CSV payroll | OPEN wages | OPEN payment basis |
| --- | --- | --- | --- | --- |
| Annapolis Courier | CORRECTED | 284515.40 | 0.00 | NOT EVALUATED |
| Bay Crest Exteriors | CORRECTED | 541498.05 | 0.00 | NOT EVALUATED |
| Harbor Point Legal | PARTIALLY UNRESOLVED | 360935.68 | 64212.48 | NOT EVALUATED |
| Larkspur Lane Bistro | PARTIALLY UNRESOLVED | 226431.55 | 114293.80 | NOT EVALUATED |
| Patuxent Electric | PARTIALLY UNRESOLVED | 470090.45 | 0.00 | 390.00 |
| Severn Homebuilders | PARTIALLY UNRESOLVED | 415322.64 | 71250.45 | 45945.65 |

## Recorded priority calls

The interview records a first-call group; it establishes no order between its members and no universal ranking rule.

- **Severn Homebuilders**: Subcontractor certificate coverage and identity require confirmation: verified additions $24693.39, OPEN payment basis $45945.65. An exactly named certificate covers the entire audit period, including both endpoints. Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Missing or incomplete/expired full-period certificate: include 60 percent of payments under the documented work code; do not prorate coverage. Work-record classification changes affect 1 employees and $59840.70 of wages. The employer's application and employee-attribution questions must be confirmed against actual work records. Reported split: H-420: 5 employees, $284670.30; C-110: 3 employees, $177209.40. Recorded acknowledgement: Nadia Brennan · 09:18 PM, /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md:681-683; SHA-256 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160.

- **Bay Crest Exteriors**: Work-record classification changes affect 6 employees and $319158.10 of wages. The employer's application and employee-attribution questions must be confirmed against actual work records. crew-timesheets.csv and site-signin-log.csv support substantial field work rather than the reported clerical split; confirm each changed employee's records below. Reported split: C-110: 7 employees, $363970.45; R-310: 3 employees, $177527.60. Recorded acknowledgement: Nadia Brennan · 09:18 PM, /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md:681-683; SHA-256 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160.

## Portfolio arithmetic controls

Payment controls include only the evaluated adjustment records. NOT EVALUATED employer adjustments are outside that control; amounts are never estimates of missing exposure.

Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):

`2521697.11 + 26853.39 = 2298793.77 + 249756.73`; difference 0.00.

Known payroll basis (includes OPEN wages): $2548550.50. Verified classified payroll: $2298793.77.

Payment reconciliation (evaluated payment basis = verified addition + nonpayroll + OPEN payment basis):

`161341.05 = 26853.39 + 88152.01 + 46335.65`; difference 0.00.

Cash reconciliation (original wages + evaluated payments = verified payroll + OPEN wages + excluded/nonpayroll payments + OPEN payment basis):

`2683038.16 = 2298793.77 + 249756.73 + 88152.01 + 46335.65`; difference 0.00.

<a id="e01"></a>
## Annapolis Courier (annapolis-courier)

Audit period: 2025-07-07 through 2026-07-05. Submitted split: **CORRECTED**.

The submitted split requires the verified class transfers/additions below. This arithmetic correction remains subject to the linked employer confirmations and auditor sign-off.

Verified-only CSV: /home/maxg/ch03-premium-audit/deliverables/codes/annapolis-courier.csv; SHA-256 a570882f537b4bf01c544c8b025d39c347a0956b445d86d6db3c5f699db307eb.

| Code | Reported payroll | Verified payroll | Difference (verified minus reported) | Verified code paragraph |
| --- | --- | --- | --- | --- |
| C-110 | 130629.20 | 107820.45 | -22808.75 | CG-04 |
| T-610 | 153886.20 | 176694.95 | 22808.75 | CG-31 |

Reported total $284515.40; original register $284515.40; register-minus-reported difference $0.00. Comparison definitive for current classifications: True (not human approval).

Application reported employee counts: T-610: 3; C-110: 3. Register employees: 6.

Application sources: S1263 application.md:7-7 (application class T-610); S1264 application.md:8-8 (application class C-110).

### Employee payroll — VERIFIED and OPEN

| Employee ID | Name | Original wages | VERIFIED wage allocation | VERIFIED additions | OPEN wages | Register source |
| --- | --- | --- | --- | --- | --- | --- |
| AC-E01 | Derek Nolan | 52956.80 | T-610 52956.80 | — | 0.00 | S0004 payroll-register.csv:2-2 (CSV line 2) |
| AC-E02 | Maria Santos | 51311.00 | T-610 51311.00 | — | 0.00 | S0996 payroll-register.csv:3-3 (CSV line 3) |
| AC-E03 | Felix Grant | 49618.40 | T-610 49618.40 | — | 0.00 | S1049 payroll-register.csv:4-4 (CSV line 4) |
| AC-E04 | Lena Ortiz | 47442.20 | C-110 24633.45; T-610 22808.75 | — | 0.00 | S1105 payroll-register.csv:5-5 (CSV line 5) |
| AC-E05 | Paul Haskins | 46675.20 | C-110 46675.20 | — | 0.00 | S1158 payroll-register.csv:6-6 (CSV line 6) |
| AC-E06 | Irene Voss | 36511.80 | C-110 36511.80 | — | 0.00 | S1211 payroll-register.csv:7-7 (CSV line 7) |

No engine-supported employee-level application coding list is available. Individual results and weekly transfers below are evidenced calculations; only the aggregate submitted split is directly compared.

### Applied rule boundaries

Each decision retains the existing evaluator's scope and conditions. OPEN decisions below describe an applicability/evidence gap, not an assigned classification. Payment rule reasons and exact references are also preserved with each adjustment.

| Rule | Decision status | Scope | Applicability boundaries | Exact rule sources |
| --- | --- | --- | --- | --- |
| courier_documented_driver | CLASSIFIED | whole_pay_week | courier delivery business; documented regular driver and actual route evidence | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:53-54 (CG-31) |
| courier_week | CLASSIFIED | whole_pay_week | courier employer; inside employee by actual duties; one complete Monday-to-Sunday pay week; complete route and pay-week evidence | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:53-54 (CG-31); S1102 classification-guide.md:32-34 (CG-04); S1103 classification-guide.md:27-30 (CG-07); S1104 ch03-premium-audit-20261105-0222(1).md:529-531 (Nadia Brennan · 09:05 PM) |

### Reconciliation and excluded payments

Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):

`284515.40 + 0.00 = 284515.40 + 0.00`; difference 0.00.

Known payroll basis (includes OPEN wages): $284515.40. Verified classified payroll: $284515.40.

Other payment adjustments: **NOT EVALUATED**. No verified assertion of zero additional exposure is made; the wage reconciliation covers supplied employee records only.

| Engine control | Reconciled | Difference |
| --- | --- | --- |
| allocation | True | 0.00 |
| independent | True | 0.00 |
| weekly | True | 0.00 |

### OPEN findings and required human resolution

Each finding remains unanswered even if its monetary effect is zero. Employer payroll/records contact supplies the requested records; responsible policy reviewer: auditor. Identity issues require documentary confirmation of the exact employee/payee, not an assumed alias.

- **OPEN — Application/classification comparison**: The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved. Required evidence/confirmation: Confirm the evidence-backed classification changes and resolve pending employee decisions; the application is not classification authority. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E01-Q007](audit-questions.md#e01-q007). Records: S1263 application.md:7-7 (application class T-610); S1264 application.md:8-8 (application class C-110).

### UNAPPROVED PROPOSED treatments

These alternatives are outside all verified totals. They require the specific evidence below and explicit auditor approval, followed by a supported rerun.

No supported conditional treatment is recorded; do not invent one for the OPEN cases.

### Allocation, payment and evidence review detail

The following entries preserve each employee/pay week, adjustment/payment, deciding reason and record confirmation. VERIFIED calculations, OPEN findings and UNAPPROVED alternatives retain their original labels. Exact dated record fields and all confirmation prompts are in the linked question document.

#### E01-Q001 — Derek Nolan [AC-E01]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E01-Q001](audit-questions.md#e01-q001).

Verified base-wage allocation: T-610 $52956.80. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Delivery business, documented driver duties and actual route-driving records support courier driver payroll.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-E01@2025-07-07#2 | 2025-07-07 | 2025-07-13 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-07-14#8 | 2025-07-14 | 2025-07-20 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-07-21#14 | 2025-07-21 | 2025-07-27 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-07-28#20 | 2025-07-28 | 2025-08-03 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-08-04#26 | 2025-08-04 | 2025-08-10 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-08-11#32 | 2025-08-11 | 2025-08-17 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-08-18#38 | 2025-08-18 | 2025-08-24 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-08-25#44 | 2025-08-25 | 2025-08-31 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-09-01#50 | 2025-09-01 | 2025-09-07 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-09-08#56 | 2025-09-08 | 2025-09-14 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-09-15#62 | 2025-09-15 | 2025-09-21 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-09-22#68 | 2025-09-22 | 2025-09-28 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-09-29#74 | 2025-09-29 | 2025-10-05 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-10-06#80 | 2025-10-06 | 2025-10-12 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-10-13#86 | 2025-10-13 | 2025-10-19 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-10-20#92 | 2025-10-20 | 2025-10-26 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-10-27#98 | 2025-10-27 | 2025-11-02 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-11-03#104 | 2025-11-03 | 2025-11-09 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-11-10#110 | 2025-11-10 | 2025-11-16 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-11-17#116 | 2025-11-17 | 2025-11-23 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-11-24#122 | 2025-11-24 | 2025-11-30 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-12-01#128 | 2025-12-01 | 2025-12-07 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-12-08#134 | 2025-12-08 | 2025-12-14 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-12-15#140 | 2025-12-15 | 2025-12-21 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-12-22#146 | 2025-12-22 | 2025-12-28 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2025-12-29#152 | 2025-12-29 | 2026-01-04 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-01-05#158 | 2026-01-05 | 2026-01-11 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-01-12#164 | 2026-01-12 | 2026-01-18 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-01-19#170 | 2026-01-19 | 2026-01-25 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-01-26#176 | 2026-01-26 | 2026-02-01 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-02-02#182 | 2026-02-02 | 2026-02-08 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-02-09#188 | 2026-02-09 | 2026-02-15 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-02-16#194 | 2026-02-16 | 2026-02-22 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-02-23#200 | 2026-02-23 | 2026-03-01 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-03-02#206 | 2026-03-02 | 2026-03-08 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-03-09#212 | 2026-03-09 | 2026-03-15 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-03-16#218 | 2026-03-16 | 2026-03-22 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-03-23#224 | 2026-03-23 | 2026-03-29 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-03-30#230 | 2026-03-30 | 2026-04-05 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-04-06#236 | 2026-04-06 | 2026-04-12 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-04-13#242 | 2026-04-13 | 2026-04-19 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-04-20#248 | 2026-04-20 | 2026-04-26 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-04-27#254 | 2026-04-27 | 2026-05-03 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-05-04#260 | 2026-05-04 | 2026-05-10 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-05-11#266 | 2026-05-11 | 2026-05-17 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-05-18#272 | 2026-05-18 | 2026-05-24 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-05-25#278 | 2026-05-25 | 2026-05-31 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-06-01#284 | 2026-06-01 | 2026-06-07 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-06-08#290 | 2026-06-08 | 2026-06-14 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-06-15#296 | 2026-06-15 | 2026-06-21 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-06-22#302 | 2026-06-22 | 2026-06-28 | 1018.40 | T-610 | CG-31 | — |
| AC-E01@2026-06-29#308 | 2026-06-29 | 2026-07-05 | 1018.40 | T-610 | CG-31 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0083, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0102, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0140, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0197, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0216, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0235, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0254, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0273, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0292, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0311, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0330, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0349, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0368, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0387, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0406, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0425, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0444, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0463, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0482, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0501, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0520, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0539, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0558, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0577, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0596, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0615, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0634, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0653, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0672, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0691, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0710, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0729, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0748, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0767, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0786, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0805, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0824, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0843, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0862, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0881, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0900, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0919, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0938, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0957, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0976, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q002 — Maria Santos [AC-E02]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E01-Q002](audit-questions.md#e01-q002).

Verified base-wage allocation: T-610 $51311.00. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Delivery business, documented driver duties and actual route-driving records support courier driver payroll.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-E02@2025-07-07#3 | 2025-07-07 | 2025-07-13 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-07-14#9 | 2025-07-14 | 2025-07-20 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-07-21#15 | 2025-07-21 | 2025-07-27 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-07-28#21 | 2025-07-28 | 2025-08-03 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-08-04#27 | 2025-08-04 | 2025-08-10 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-08-11#33 | 2025-08-11 | 2025-08-17 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-08-18#39 | 2025-08-18 | 2025-08-24 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-08-25#45 | 2025-08-25 | 2025-08-31 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-09-01#51 | 2025-09-01 | 2025-09-07 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-09-08#57 | 2025-09-08 | 2025-09-14 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-09-15#63 | 2025-09-15 | 2025-09-21 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-09-22#69 | 2025-09-22 | 2025-09-28 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-09-29#75 | 2025-09-29 | 2025-10-05 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-10-06#81 | 2025-10-06 | 2025-10-12 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-10-13#87 | 2025-10-13 | 2025-10-19 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-10-20#93 | 2025-10-20 | 2025-10-26 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-10-27#99 | 2025-10-27 | 2025-11-02 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-11-03#105 | 2025-11-03 | 2025-11-09 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-11-10#111 | 2025-11-10 | 2025-11-16 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-11-17#117 | 2025-11-17 | 2025-11-23 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-11-24#123 | 2025-11-24 | 2025-11-30 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-12-01#129 | 2025-12-01 | 2025-12-07 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-12-08#135 | 2025-12-08 | 2025-12-14 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-12-15#141 | 2025-12-15 | 2025-12-21 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-12-22#147 | 2025-12-22 | 2025-12-28 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2025-12-29#153 | 2025-12-29 | 2026-01-04 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-01-05#159 | 2026-01-05 | 2026-01-11 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-01-12#165 | 2026-01-12 | 2026-01-18 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-01-19#171 | 2026-01-19 | 2026-01-25 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-01-26#177 | 2026-01-26 | 2026-02-01 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-02-02#183 | 2026-02-02 | 2026-02-08 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-02-09#189 | 2026-02-09 | 2026-02-15 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-02-16#195 | 2026-02-16 | 2026-02-22 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-02-23#201 | 2026-02-23 | 2026-03-01 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-03-02#207 | 2026-03-02 | 2026-03-08 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-03-09#213 | 2026-03-09 | 2026-03-15 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-03-16#219 | 2026-03-16 | 2026-03-22 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-03-23#225 | 2026-03-23 | 2026-03-29 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-03-30#231 | 2026-03-30 | 2026-04-05 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-04-06#237 | 2026-04-06 | 2026-04-12 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-04-13#243 | 2026-04-13 | 2026-04-19 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-04-20#249 | 2026-04-20 | 2026-04-26 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-04-27#255 | 2026-04-27 | 2026-05-03 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-05-04#261 | 2026-05-04 | 2026-05-10 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-05-11#267 | 2026-05-11 | 2026-05-17 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-05-18#273 | 2026-05-18 | 2026-05-24 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-05-25#279 | 2026-05-25 | 2026-05-31 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-06-01#285 | 2026-06-01 | 2026-06-07 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-06-08#291 | 2026-06-08 | 2026-06-14 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-06-15#297 | 2026-06-15 | 2026-06-21 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-06-22#303 | 2026-06-22 | 2026-06-28 | 986.75 | T-610 | CG-31 | — |
| AC-E02@2026-06-29#309 | 2026-06-29 | 2026-07-05 | 986.75 | T-610 | CG-31 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S0995, S0996, S0997, S0998, S0999, S1000, S1001, S1002, S1003, S1004, S1005, S1006, S1007, S1008, S1009, S1010, S1011, S1012, S1013, S1014, S1015, S1016, S1017, S1018, S1019, S1020, S1021, S1022, S1023, S1024, S1025, S1026, S1027, S1028, S1029, S1030, S1031, S1032, S1033, S1034, S1035, S1036, S1037, S1038, S1039, S1040, S1041, S1042, S1043, S1044, S1045, S1046, S1047.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q003 — Felix Grant [AC-E03]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E01-Q003](audit-questions.md#e01-q003).

Verified base-wage allocation: T-610 $49618.40. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Delivery business, documented driver duties and actual route-driving records support courier driver payroll.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-E03@2025-07-07#4 | 2025-07-07 | 2025-07-13 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-07-14#10 | 2025-07-14 | 2025-07-20 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-07-21#16 | 2025-07-21 | 2025-07-27 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-07-28#22 | 2025-07-28 | 2025-08-03 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-08-04#28 | 2025-08-04 | 2025-08-10 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-08-11#34 | 2025-08-11 | 2025-08-17 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-08-18#40 | 2025-08-18 | 2025-08-24 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-08-25#46 | 2025-08-25 | 2025-08-31 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-09-01#52 | 2025-09-01 | 2025-09-07 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-09-08#58 | 2025-09-08 | 2025-09-14 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-09-15#64 | 2025-09-15 | 2025-09-21 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-09-22#70 | 2025-09-22 | 2025-09-28 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-09-29#76 | 2025-09-29 | 2025-10-05 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-10-06#82 | 2025-10-06 | 2025-10-12 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-10-13#88 | 2025-10-13 | 2025-10-19 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-10-20#94 | 2025-10-20 | 2025-10-26 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-10-27#100 | 2025-10-27 | 2025-11-02 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-11-03#106 | 2025-11-03 | 2025-11-09 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-11-10#112 | 2025-11-10 | 2025-11-16 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-11-17#118 | 2025-11-17 | 2025-11-23 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-11-24#124 | 2025-11-24 | 2025-11-30 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-12-01#130 | 2025-12-01 | 2025-12-07 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-12-08#136 | 2025-12-08 | 2025-12-14 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-12-15#142 | 2025-12-15 | 2025-12-21 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-12-22#148 | 2025-12-22 | 2025-12-28 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2025-12-29#154 | 2025-12-29 | 2026-01-04 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-01-05#160 | 2026-01-05 | 2026-01-11 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-01-12#166 | 2026-01-12 | 2026-01-18 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-01-19#172 | 2026-01-19 | 2026-01-25 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-01-26#178 | 2026-01-26 | 2026-02-01 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-02-02#184 | 2026-02-02 | 2026-02-08 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-02-09#190 | 2026-02-09 | 2026-02-15 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-02-16#196 | 2026-02-16 | 2026-02-22 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-02-23#202 | 2026-02-23 | 2026-03-01 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-03-02#208 | 2026-03-02 | 2026-03-08 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-03-09#214 | 2026-03-09 | 2026-03-15 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-03-16#220 | 2026-03-16 | 2026-03-22 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-03-23#226 | 2026-03-23 | 2026-03-29 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-03-30#232 | 2026-03-30 | 2026-04-05 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-04-06#238 | 2026-04-06 | 2026-04-12 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-04-13#244 | 2026-04-13 | 2026-04-19 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-04-20#250 | 2026-04-20 | 2026-04-26 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-04-27#256 | 2026-04-27 | 2026-05-03 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-05-04#262 | 2026-05-04 | 2026-05-10 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-05-11#268 | 2026-05-11 | 2026-05-17 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-05-18#274 | 2026-05-18 | 2026-05-24 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-05-25#280 | 2026-05-25 | 2026-05-31 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-06-01#286 | 2026-06-01 | 2026-06-07 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-06-08#292 | 2026-06-08 | 2026-06-14 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-06-15#298 | 2026-06-15 | 2026-06-21 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-06-22#304 | 2026-06-22 | 2026-06-28 | 954.20 | T-610 | CG-31 | — |
| AC-E03@2026-06-29#310 | 2026-06-29 | 2026-07-05 | 954.20 | T-610 | CG-31 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S1048, S1049, S1050, S1051, S1052, S1053, S1054, S1055, S1056, S1057, S1058, S1059, S1060, S1061, S1062, S1063, S1064, S1065, S1066, S1067, S1068, S1069, S1070, S1071, S1072, S1073, S1074, S1075, S1076, S1077, S1078, S1079, S1080, S1081, S1082, S1083, S1084, S1085, S1086, S1087, S1088, S1089, S1090, S1091, S1092, S1093, S1094, S1095, S1096, S1097, S1098, S1099, S1100.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q004 — Lena Ortiz [AC-E04]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E01-Q004](audit-questions.md#e01-q004).

Verified base-wage allocation: C-110 $24633.45; T-610 $22808.75. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Between 2 confirmed and 2 possible distinct ride days; both bounds yield T-610. 2 distinct ride days in this Monday-to-Sunday pay week; the driver code applies to the whole week.

Between 0 confirmed and 0 possible distinct ride days; both bounds yield C-110. 0 distinct ride days in this Monday-to-Sunday pay week; the clerical code applies to the whole week.

Between 1 confirmed and 1 possible distinct ride days; both bounds yield C-110. 1 distinct ride days in this Monday-to-Sunday pay week; the clerical code applies to the whole week.

Between 3 confirmed and 3 possible distinct ride days; both bounds yield T-610. 3 distinct ride days in this Monday-to-Sunday pay week; the driver code applies to the whole week.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-E04@2025-07-07#5 | 2025-07-07 | 2025-07-13 | 912.35 | T-610 | CG-31 | 2025-07-10, 2025-07-11 |
| AC-E04@2025-07-14#11 | 2025-07-14 | 2025-07-20 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2025-07-21#17 | 2025-07-21 | 2025-07-27 | 912.35 | C-110 | CG-04 | 2025-07-23 |
| AC-E04@2025-07-28#23 | 2025-07-28 | 2025-08-03 | 912.35 | T-610 | CG-31 | 2025-07-28, 2025-07-30 |
| AC-E04@2025-08-04#29 | 2025-08-04 | 2025-08-10 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2025-08-11#35 | 2025-08-11 | 2025-08-17 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2025-08-18#41 | 2025-08-18 | 2025-08-24 | 912.35 | T-610 | CG-31 | 2025-08-19, 2025-08-20, 2025-08-21 |
| AC-E04@2025-08-25#47 | 2025-08-25 | 2025-08-31 | 912.35 | T-610 | CG-31 | 2025-08-25, 2025-08-28 |
| AC-E04@2025-09-01#53 | 2025-09-01 | 2025-09-07 | 912.35 | T-610 | CG-31 | 2025-09-02, 2025-09-06 |
| AC-E04@2025-09-08#59 | 2025-09-08 | 2025-09-14 | 912.35 | T-610 | CG-31 | 2025-09-08, 2025-09-13 |
| AC-E04@2025-09-15#65 | 2025-09-15 | 2025-09-21 | 912.35 | T-610 | CG-31 | 2025-09-15, 2025-09-17 |
| AC-E04@2025-09-22#71 | 2025-09-22 | 2025-09-28 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2025-09-29#77 | 2025-09-29 | 2025-10-05 | 912.35 | T-610 | CG-31 | 2025-09-29, 2025-10-02, 2025-10-03 |
| AC-E04@2025-10-06#83 | 2025-10-06 | 2025-10-12 | 912.35 | T-610 | CG-31 | 2025-10-09, 2025-10-11 |
| AC-E04@2025-10-13#89 | 2025-10-13 | 2025-10-19 | 912.35 | T-610 | CG-31 | 2025-10-13, 2025-10-18 |
| AC-E04@2025-10-20#95 | 2025-10-20 | 2025-10-26 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2025-10-27#101 | 2025-10-27 | 2025-11-02 | 912.35 | T-610 | CG-31 | 2025-10-27, 2025-11-01 |
| AC-E04@2025-11-03#107 | 2025-11-03 | 2025-11-09 | 912.35 | T-610 | CG-31 | 2025-11-03, 2025-11-04 |
| AC-E04@2025-11-10#113 | 2025-11-10 | 2025-11-16 | 912.35 | T-610 | CG-31 | 2025-11-11, 2025-11-14 |
| AC-E04@2025-11-17#119 | 2025-11-17 | 2025-11-23 | 912.35 | T-610 | CG-31 | 2025-11-17, 2025-11-20 |
| AC-E04@2025-11-24#125 | 2025-11-24 | 2025-11-30 | 912.35 | T-610 | CG-31 | 2025-11-25, 2025-11-26, 2025-11-29 |
| AC-E04@2025-12-01#131 | 2025-12-01 | 2025-12-07 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2025-12-08#137 | 2025-12-08 | 2025-12-14 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2025-12-15#143 | 2025-12-15 | 2025-12-21 | 912.35 | C-110 | CG-04 | 2025-12-15 |
| AC-E04@2025-12-22#149 | 2025-12-22 | 2025-12-28 | 912.35 | T-610 | CG-31 | 2025-12-24, 2025-12-25 |
| AC-E04@2025-12-29#155 | 2025-12-29 | 2026-01-04 | 912.35 | T-610 | CG-31 | 2025-12-29, 2026-01-01 |
| AC-E04@2026-01-05#161 | 2026-01-05 | 2026-01-11 | 912.35 | C-110 | CG-04 | 2026-01-08 |
| AC-E04@2026-01-12#167 | 2026-01-12 | 2026-01-18 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-01-19#173 | 2026-01-19 | 2026-01-25 | 912.35 | T-610 | CG-31 | 2026-01-20, 2026-01-21 |
| AC-E04@2026-01-26#179 | 2026-01-26 | 2026-02-01 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-02-02#185 | 2026-02-02 | 2026-02-08 | 912.35 | T-610 | CG-31 | 2026-02-02, 2026-02-03, 2026-02-04 |
| AC-E04@2026-02-09#191 | 2026-02-09 | 2026-02-15 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-02-16#197 | 2026-02-16 | 2026-02-22 | 912.35 | T-610 | CG-31 | 2026-02-16, 2026-02-18 |
| AC-E04@2026-02-23#203 | 2026-02-23 | 2026-03-01 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-03-02#209 | 2026-03-02 | 2026-03-08 | 912.35 | T-610 | CG-31 | 2026-03-05, 2026-03-07 |
| AC-E04@2026-03-09#215 | 2026-03-09 | 2026-03-15 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-03-16#221 | 2026-03-16 | 2026-03-22 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-03-23#227 | 2026-03-23 | 2026-03-29 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-03-30#233 | 2026-03-30 | 2026-04-05 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-04-06#239 | 2026-04-06 | 2026-04-12 | 912.35 | C-110 | CG-04 | 2026-04-09 |
| AC-E04@2026-04-13#245 | 2026-04-13 | 2026-04-19 | 912.35 | C-110 | CG-04 | 2026-04-16 |
| AC-E04@2026-04-20#251 | 2026-04-20 | 2026-04-26 | 912.35 | T-610 | CG-31 | 2026-04-22, 2026-04-25 |
| AC-E04@2026-04-27#257 | 2026-04-27 | 2026-05-03 | 912.35 | T-610 | CG-31 | 2026-05-01, 2026-05-02 |
| AC-E04@2026-05-04#263 | 2026-05-04 | 2026-05-10 | 912.35 | C-110 | CG-04 | 2026-05-05 |
| AC-E04@2026-05-11#269 | 2026-05-11 | 2026-05-17 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-05-18#275 | 2026-05-18 | 2026-05-24 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-05-25#281 | 2026-05-25 | 2026-05-31 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-06-01#287 | 2026-06-01 | 2026-06-07 | 912.35 | T-610 | CG-31 | 2026-06-03, 2026-06-06 |
| AC-E04@2026-06-08#293 | 2026-06-08 | 2026-06-14 | 912.35 | T-610 | CG-31 | 2026-06-09, 2026-06-12 |
| AC-E04@2026-06-15#299 | 2026-06-15 | 2026-06-21 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-06-22#305 | 2026-06-22 | 2026-06-28 | 912.35 | C-110 | CG-04 |  |
| AC-E04@2026-06-29#311 | 2026-06-29 | 2026-07-05 | 912.35 | C-110 | CG-04 |  |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S1101, S1102, S1103, S1104, S1105, S1106, S1107, S1108, S1109, S1110, S1111, S1112, S1113, S1114, S1115, S1116, S1117, S1118, S1119, S1120, S1121, S1122, S1123, S1124, S1125, S1126, S1127, S1128, S1129, S1130, S1131, S1132, S1133, S1134, S1135, S1136, S1137, S1138, S1139, S1140, S1141, S1142, S1143, S1144, S1145, S1146, S1147, S1148, S1149, S1150, S1151, S1152, S1153, S1154, S1155, S1156.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q005 — Paul Haskins [AC-E05]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E01-Q005](audit-questions.md#e01-q005).

Verified base-wage allocation: C-110 $46675.20. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Between 0 confirmed and 0 possible distinct ride days; both bounds yield C-110. 0 distinct ride days in this Monday-to-Sunday pay week; the clerical code applies to the whole week.

Between 1 confirmed and 1 possible distinct ride days; both bounds yield C-110. 1 distinct ride days in this Monday-to-Sunday pay week; the clerical code applies to the whole week.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-E05@2025-07-07#6 | 2025-07-07 | 2025-07-13 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-07-14#12 | 2025-07-14 | 2025-07-20 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-07-21#18 | 2025-07-21 | 2025-07-27 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-07-28#24 | 2025-07-28 | 2025-08-03 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-08-04#30 | 2025-08-04 | 2025-08-10 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-08-11#36 | 2025-08-11 | 2025-08-17 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-08-18#42 | 2025-08-18 | 2025-08-24 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-08-25#48 | 2025-08-25 | 2025-08-31 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-09-01#54 | 2025-09-01 | 2025-09-07 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-09-08#60 | 2025-09-08 | 2025-09-14 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-09-15#66 | 2025-09-15 | 2025-09-21 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-09-22#72 | 2025-09-22 | 2025-09-28 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-09-29#78 | 2025-09-29 | 2025-10-05 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-10-06#84 | 2025-10-06 | 2025-10-12 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-10-13#90 | 2025-10-13 | 2025-10-19 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-10-20#96 | 2025-10-20 | 2025-10-26 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-10-27#102 | 2025-10-27 | 2025-11-02 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-11-03#108 | 2025-11-03 | 2025-11-09 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-11-10#114 | 2025-11-10 | 2025-11-16 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-11-17#120 | 2025-11-17 | 2025-11-23 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-11-24#126 | 2025-11-24 | 2025-11-30 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-12-01#132 | 2025-12-01 | 2025-12-07 | 897.60 | C-110 | CG-04 | 2025-12-03 |
| AC-E05@2025-12-08#138 | 2025-12-08 | 2025-12-14 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-12-15#144 | 2025-12-15 | 2025-12-21 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-12-22#150 | 2025-12-22 | 2025-12-28 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2025-12-29#156 | 2025-12-29 | 2026-01-04 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-01-05#162 | 2026-01-05 | 2026-01-11 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-01-12#168 | 2026-01-12 | 2026-01-18 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-01-19#174 | 2026-01-19 | 2026-01-25 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-01-26#180 | 2026-01-26 | 2026-02-01 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-02-02#186 | 2026-02-02 | 2026-02-08 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-02-09#192 | 2026-02-09 | 2026-02-15 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-02-16#198 | 2026-02-16 | 2026-02-22 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-02-23#204 | 2026-02-23 | 2026-03-01 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-03-02#210 | 2026-03-02 | 2026-03-08 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-03-09#216 | 2026-03-09 | 2026-03-15 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-03-16#222 | 2026-03-16 | 2026-03-22 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-03-23#228 | 2026-03-23 | 2026-03-29 | 897.60 | C-110 | CG-04 | 2026-03-26 |
| AC-E05@2026-03-30#234 | 2026-03-30 | 2026-04-05 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-04-06#240 | 2026-04-06 | 2026-04-12 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-04-13#246 | 2026-04-13 | 2026-04-19 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-04-20#252 | 2026-04-20 | 2026-04-26 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-04-27#258 | 2026-04-27 | 2026-05-03 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-05-04#264 | 2026-05-04 | 2026-05-10 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-05-11#270 | 2026-05-11 | 2026-05-17 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-05-18#276 | 2026-05-18 | 2026-05-24 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-05-25#282 | 2026-05-25 | 2026-05-31 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-06-01#288 | 2026-06-01 | 2026-06-07 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-06-08#294 | 2026-06-08 | 2026-06-14 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-06-15#300 | 2026-06-15 | 2026-06-21 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-06-22#306 | 2026-06-22 | 2026-06-28 | 897.60 | C-110 | CG-04 |  |
| AC-E05@2026-06-29#312 | 2026-06-29 | 2026-07-05 | 897.60 | C-110 | CG-04 |  |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S1102, S1103, S1104, S1157, S1158, S1159, S1160, S1161, S1162, S1163, S1164, S1165, S1166, S1167, S1168, S1169, S1170, S1171, S1172, S1173, S1174, S1175, S1176, S1177, S1178, S1179, S1180, S1181, S1182, S1183, S1184, S1185, S1186, S1187, S1188, S1189, S1190, S1191, S1192, S1193, S1194, S1195, S1196, S1197, S1198, S1199, S1200, S1201, S1202, S1203, S1204, S1205, S1206, S1207, S1208, S1209.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q006 — Irene Voss [AC-E06]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E01-Q006](audit-questions.md#e01-q006).

Verified base-wage allocation: C-110 $36511.80. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Between 0 confirmed and 0 possible distinct ride days; both bounds yield C-110. 0 distinct ride days in this Monday-to-Sunday pay week; the clerical code applies to the whole week.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| AC-E06@2025-07-07#7 | 2025-07-07 | 2025-07-13 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-07-14#13 | 2025-07-14 | 2025-07-20 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-07-21#19 | 2025-07-21 | 2025-07-27 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-07-28#25 | 2025-07-28 | 2025-08-03 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-08-04#31 | 2025-08-04 | 2025-08-10 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-08-11#37 | 2025-08-11 | 2025-08-17 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-08-18#43 | 2025-08-18 | 2025-08-24 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-08-25#49 | 2025-08-25 | 2025-08-31 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-09-01#55 | 2025-09-01 | 2025-09-07 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-09-08#61 | 2025-09-08 | 2025-09-14 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-09-15#67 | 2025-09-15 | 2025-09-21 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-09-22#73 | 2025-09-22 | 2025-09-28 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-09-29#79 | 2025-09-29 | 2025-10-05 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-10-06#85 | 2025-10-06 | 2025-10-12 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-10-13#91 | 2025-10-13 | 2025-10-19 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-10-20#97 | 2025-10-20 | 2025-10-26 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-10-27#103 | 2025-10-27 | 2025-11-02 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-11-03#109 | 2025-11-03 | 2025-11-09 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-11-10#115 | 2025-11-10 | 2025-11-16 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-11-17#121 | 2025-11-17 | 2025-11-23 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-11-24#127 | 2025-11-24 | 2025-11-30 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-12-01#133 | 2025-12-01 | 2025-12-07 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-12-08#139 | 2025-12-08 | 2025-12-14 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-12-15#145 | 2025-12-15 | 2025-12-21 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-12-22#151 | 2025-12-22 | 2025-12-28 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2025-12-29#157 | 2025-12-29 | 2026-01-04 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-01-05#163 | 2026-01-05 | 2026-01-11 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-01-12#169 | 2026-01-12 | 2026-01-18 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-01-19#175 | 2026-01-19 | 2026-01-25 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-01-26#181 | 2026-01-26 | 2026-02-01 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-02-02#187 | 2026-02-02 | 2026-02-08 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-02-09#193 | 2026-02-09 | 2026-02-15 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-02-16#199 | 2026-02-16 | 2026-02-22 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-02-23#205 | 2026-02-23 | 2026-03-01 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-03-02#211 | 2026-03-02 | 2026-03-08 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-03-09#217 | 2026-03-09 | 2026-03-15 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-03-16#223 | 2026-03-16 | 2026-03-22 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-03-23#229 | 2026-03-23 | 2026-03-29 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-03-30#235 | 2026-03-30 | 2026-04-05 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-04-06#241 | 2026-04-06 | 2026-04-12 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-04-13#247 | 2026-04-13 | 2026-04-19 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-04-20#253 | 2026-04-20 | 2026-04-26 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-04-27#259 | 2026-04-27 | 2026-05-03 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-05-04#265 | 2026-05-04 | 2026-05-10 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-05-11#271 | 2026-05-11 | 2026-05-17 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-05-18#277 | 2026-05-18 | 2026-05-24 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-05-25#283 | 2026-05-25 | 2026-05-31 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-06-01#289 | 2026-06-01 | 2026-06-07 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-06-08#295 | 2026-06-08 | 2026-06-14 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-06-15#301 | 2026-06-15 | 2026-06-21 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-06-22#307 | 2026-06-22 | 2026-06-28 | 702.15 | C-110 | CG-04 |  |
| AC-E06@2026-06-29#313 | 2026-06-29 | 2026-07-05 | 702.15 | C-110 | CG-04 |  |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S1102, S1103, S1104, S1210, S1211, S1212, S1213, S1214, S1215, S1216, S1217, S1218, S1219, S1220, S1221, S1222, S1223, S1224, S1225, S1226, S1227, S1228, S1229, S1230, S1231, S1232, S1233, S1234, S1235, S1236, S1237, S1238, S1239, S1240, S1241, S1242, S1243, S1244, S1245, S1246, S1247, S1248, S1249, S1250, S1251, S1252, S1253, S1254, S1255, S1256, S1257, S1258, S1259, S1260, S1261, S1262.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q007 — Application split, employee attribution and payroll reconciliation

**VERIFIED CALCULATION + OPEN FINDING / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E01-Q007](audit-questions.md#e01-q007).

Reconciliation verifies arithmetic, not employer confirmation or approval. Verified CSVs exclude OPEN wages and every unapproved proposal.

Application comparison definitive for current classifications: True; this is not audit approval.

The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved.

| Code | Reported payroll | Verified CSV payroll | Difference (verified minus reported) |
| --- | --- | --- | --- |
| C-110 | 130629.20 | 107820.45 | -22808.75 |
| T-610 | 153886.20 | 176694.95 | 22808.75 |

| Control | Reconciled | Original basis | Unresolved amount |
| --- | --- | --- | --- |
| allocation | True | 284515.40 | 0.00 |
| independent | True | 284515.40 | 0.00 |
| weekly | True | 284515.40 | see review state |

Supporting source IDs (local to this employer; exact locators below): S1263, S1264.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q008 — Business, actual-duty observations and audit-period completeness

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E01-Q008](audit-questions.md#e01-q008).

Classification depends on actual work and complete period evidence; job titles and the submitted application alone do not establish a code.

Supporting source IDs (local to this employer; exact locators below): S0005, S0006.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E01-Q009 — Company-rule applicability — auditor confirmation

**AUDITOR APPROVAL / EMPLOYER FACT CONFIRMATION**. Follow-up: [E01-Q009](audit-questions.md#e01-q009).

Contractor-specific practices cannot be extended to unrelated industries; proposals are not verified rules or allocations.

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S1102, S1103, S1104.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

<details>
<summary>Source and rule index — 1264 exact citations</summary>

Original Classification Guide paragraph identifiers and interview timestamps/line spans are preserved here. Rule applicability is bounded by the recorded decision; a citation is not permission to extend a contractor practice to another business. Physical CSV row identities and confirmation links are preserved in the question document's record index.

| Source ID | Original document | Original paragraph / interview / record locator | Lines |
| --- | --- | --- | --- |
| S0001 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 2 | 2-2 |
| S0002 | /home/maxg/insurance01-inputs/classification-guide.md | CG-02 | 15-16 |
| S0003 | /home/maxg/insurance01-inputs/classification-guide.md | CG-31 | 53-54 |
| S0004 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/payroll-register.csv | CSV line 2 | 2-2 |
| S0005 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/business-description.md | business description | 1-7 |
| S0006 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/field-notes.md | auditor field notes | 1-5 |
| S0007 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | examined audit-period route log | 1-937 |
| S0008 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 2 | 2-2 |
| S0009 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 3 | 3-3 |
| S0010 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 4 | 4-4 |
| S0011 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 5 | 5-5 |
| S0012 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 6 | 6-6 |
| S0013 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 7 | 7-7 |
| S0014 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 8 | 8-8 |
| S0015 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 9 | 9-9 |
| S0016 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 10 | 10-10 |
| S0017 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 11 | 11-11 |
| S0018 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 12 | 12-12 |
| S0019 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 13 | 13-13 |
| S0020 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 14 | 14-14 |
| S0021 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 15 | 15-15 |
| S0022 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 16 | 16-16 |
| S0023 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 17 | 17-17 |
| S0024 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 18 | 18-18 |
| S0025 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 19 | 19-19 |
| S0026 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 8 | 8-8 |
| S0027 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 20 | 20-20 |
| S0028 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 21 | 21-21 |
| S0029 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 22 | 22-22 |
| S0030 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 23 | 23-23 |
| S0031 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 24 | 24-24 |
| S0032 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 25 | 25-25 |
| S0033 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 26 | 26-26 |
| S0034 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 27 | 27-27 |
| S0035 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 28 | 28-28 |
| S0036 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 29 | 29-29 |
| S0037 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 30 | 30-30 |
| S0038 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 31 | 31-31 |
| S0039 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 32 | 32-32 |
| S0040 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 33 | 33-33 |
| S0041 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 34 | 34-34 |
| S0042 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 35 | 35-35 |
| S0043 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 36 | 36-36 |
| S0044 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 37 | 37-37 |
| S0045 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 14 | 14-14 |
| S0046 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 38 | 38-38 |
| S0047 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 39 | 39-39 |
| S0048 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 40 | 40-40 |
| S0049 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 41 | 41-41 |
| S0050 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 42 | 42-42 |
| S0051 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 43 | 43-43 |
| S0052 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 44 | 44-44 |
| S0053 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 45 | 45-45 |
| S0054 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 46 | 46-46 |
| S0055 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 47 | 47-47 |
| S0056 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 48 | 48-48 |
| S0057 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 49 | 49-49 |
| S0058 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 50 | 50-50 |
| S0059 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 51 | 51-51 |
| S0060 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 52 | 52-52 |
| S0061 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 53 | 53-53 |
| S0062 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 54 | 54-54 |
| S0063 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 55 | 55-55 |
| S0064 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 20 | 20-20 |
| S0065 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 56 | 56-56 |
| S0066 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 57 | 57-57 |
| S0067 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 58 | 58-58 |
| S0068 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 59 | 59-59 |
| S0069 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 60 | 60-60 |
| S0070 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 61 | 61-61 |
| S0071 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 62 | 62-62 |
| S0072 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 63 | 63-63 |
| S0073 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 64 | 64-64 |
| S0074 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 65 | 65-65 |
| S0075 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 66 | 66-66 |
| S0076 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 67 | 67-67 |
| S0077 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 68 | 68-68 |
| S0078 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 69 | 69-69 |
| S0079 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 70 | 70-70 |
| S0080 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 71 | 71-71 |
| S0081 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 72 | 72-72 |
| S0082 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 73 | 73-73 |
| S0083 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 26 | 26-26 |
| S0084 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 74 | 74-74 |
| S0085 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 75 | 75-75 |
| S0086 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 76 | 76-76 |
| S0087 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 77 | 77-77 |
| S0088 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 78 | 78-78 |
| S0089 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 79 | 79-79 |
| S0090 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 80 | 80-80 |
| S0091 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 81 | 81-81 |
| S0092 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 82 | 82-82 |
| S0093 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 83 | 83-83 |
| S0094 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 84 | 84-84 |
| S0095 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 85 | 85-85 |
| S0096 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 86 | 86-86 |
| S0097 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 87 | 87-87 |
| S0098 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 88 | 88-88 |
| S0099 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 89 | 89-89 |
| S0100 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 90 | 90-90 |
| S0101 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 91 | 91-91 |
| S0102 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 32 | 32-32 |
| S0103 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 92 | 92-92 |
| S0104 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 93 | 93-93 |
| S0105 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 94 | 94-94 |
| S0106 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 95 | 95-95 |
| S0107 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 96 | 96-96 |
| S0108 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 97 | 97-97 |
| S0109 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 98 | 98-98 |
| S0110 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 99 | 99-99 |
| S0111 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 100 | 100-100 |
| S0112 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 101 | 101-101 |
| S0113 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 102 | 102-102 |
| S0114 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 103 | 103-103 |
| S0115 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 104 | 104-104 |
| S0116 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 105 | 105-105 |
| S0117 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 106 | 106-106 |
| S0118 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 107 | 107-107 |
| S0119 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 108 | 108-108 |
| S0120 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 109 | 109-109 |
| S0121 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 38 | 38-38 |
| S0122 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 110 | 110-110 |
| S0123 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 111 | 111-111 |
| S0124 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 112 | 112-112 |
| S0125 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 113 | 113-113 |
| S0126 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 114 | 114-114 |
| S0127 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 115 | 115-115 |
| S0128 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 116 | 116-116 |
| S0129 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 117 | 117-117 |
| S0130 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 118 | 118-118 |
| S0131 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 119 | 119-119 |
| S0132 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 120 | 120-120 |
| S0133 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 121 | 121-121 |
| S0134 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 122 | 122-122 |
| S0135 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 123 | 123-123 |
| S0136 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 124 | 124-124 |
| S0137 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 125 | 125-125 |
| S0138 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 126 | 126-126 |
| S0139 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 127 | 127-127 |
| S0140 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 44 | 44-44 |
| S0141 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 128 | 128-128 |
| S0142 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 129 | 129-129 |
| S0143 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 130 | 130-130 |
| S0144 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 131 | 131-131 |
| S0145 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 132 | 132-132 |
| S0146 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 133 | 133-133 |
| S0147 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 134 | 134-134 |
| S0148 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 135 | 135-135 |
| S0149 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 136 | 136-136 |
| S0150 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 137 | 137-137 |
| S0151 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 138 | 138-138 |
| S0152 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 139 | 139-139 |
| S0153 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 140 | 140-140 |
| S0154 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 141 | 141-141 |
| S0155 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 142 | 142-142 |
| S0156 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 143 | 143-143 |
| S0157 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 144 | 144-144 |
| S0158 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 145 | 145-145 |
| S0159 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 50 | 50-50 |
| S0160 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 146 | 146-146 |
| S0161 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 147 | 147-147 |
| S0162 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 148 | 148-148 |
| S0163 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 149 | 149-149 |
| S0164 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 150 | 150-150 |
| S0165 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 151 | 151-151 |
| S0166 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 152 | 152-152 |
| S0167 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 153 | 153-153 |
| S0168 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 154 | 154-154 |
| S0169 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 155 | 155-155 |
| S0170 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 156 | 156-156 |
| S0171 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 157 | 157-157 |
| S0172 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 158 | 158-158 |
| S0173 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 159 | 159-159 |
| S0174 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 160 | 160-160 |
| S0175 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 161 | 161-161 |
| S0176 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 162 | 162-162 |
| S0177 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 163 | 163-163 |
| S0178 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 56 | 56-56 |
| S0179 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 164 | 164-164 |
| S0180 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 165 | 165-165 |
| S0181 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 166 | 166-166 |
| S0182 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 167 | 167-167 |
| S0183 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 168 | 168-168 |
| S0184 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 169 | 169-169 |
| S0185 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 170 | 170-170 |
| S0186 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 171 | 171-171 |
| S0187 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 172 | 172-172 |
| S0188 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 173 | 173-173 |
| S0189 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 174 | 174-174 |
| S0190 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 175 | 175-175 |
| S0191 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 176 | 176-176 |
| S0192 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 177 | 177-177 |
| S0193 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 178 | 178-178 |
| S0194 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 179 | 179-179 |
| S0195 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 180 | 180-180 |
| S0196 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 181 | 181-181 |
| S0197 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 62 | 62-62 |
| S0198 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 182 | 182-182 |
| S0199 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 183 | 183-183 |
| S0200 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 184 | 184-184 |
| S0201 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 185 | 185-185 |
| S0202 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 186 | 186-186 |
| S0203 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 187 | 187-187 |
| S0204 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 188 | 188-188 |
| S0205 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 189 | 189-189 |
| S0206 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 190 | 190-190 |
| S0207 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 191 | 191-191 |
| S0208 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 192 | 192-192 |
| S0209 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 193 | 193-193 |
| S0210 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 194 | 194-194 |
| S0211 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 195 | 195-195 |
| S0212 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 196 | 196-196 |
| S0213 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 197 | 197-197 |
| S0214 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 198 | 198-198 |
| S0215 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 199 | 199-199 |
| S0216 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 68 | 68-68 |
| S0217 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 200 | 200-200 |
| S0218 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 201 | 201-201 |
| S0219 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 202 | 202-202 |
| S0220 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 203 | 203-203 |
| S0221 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 204 | 204-204 |
| S0222 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 205 | 205-205 |
| S0223 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 206 | 206-206 |
| S0224 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 207 | 207-207 |
| S0225 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 208 | 208-208 |
| S0226 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 209 | 209-209 |
| S0227 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 210 | 210-210 |
| S0228 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 211 | 211-211 |
| S0229 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 212 | 212-212 |
| S0230 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 213 | 213-213 |
| S0231 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 214 | 214-214 |
| S0232 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 215 | 215-215 |
| S0233 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 216 | 216-216 |
| S0234 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 217 | 217-217 |
| S0235 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 74 | 74-74 |
| S0236 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 218 | 218-218 |
| S0237 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 219 | 219-219 |
| S0238 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 220 | 220-220 |
| S0239 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 221 | 221-221 |
| S0240 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 222 | 222-222 |
| S0241 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 223 | 223-223 |
| S0242 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 224 | 224-224 |
| S0243 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 225 | 225-225 |
| S0244 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 226 | 226-226 |
| S0245 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 227 | 227-227 |
| S0246 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 228 | 228-228 |
| S0247 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 229 | 229-229 |
| S0248 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 230 | 230-230 |
| S0249 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 231 | 231-231 |
| S0250 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 232 | 232-232 |
| S0251 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 233 | 233-233 |
| S0252 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 234 | 234-234 |
| S0253 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 235 | 235-235 |
| S0254 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 80 | 80-80 |
| S0255 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 236 | 236-236 |
| S0256 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 237 | 237-237 |
| S0257 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 238 | 238-238 |
| S0258 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 239 | 239-239 |
| S0259 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 240 | 240-240 |
| S0260 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 241 | 241-241 |
| S0261 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 242 | 242-242 |
| S0262 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 243 | 243-243 |
| S0263 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 244 | 244-244 |
| S0264 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 245 | 245-245 |
| S0265 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 246 | 246-246 |
| S0266 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 247 | 247-247 |
| S0267 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 248 | 248-248 |
| S0268 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 249 | 249-249 |
| S0269 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 250 | 250-250 |
| S0270 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 251 | 251-251 |
| S0271 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 252 | 252-252 |
| S0272 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 253 | 253-253 |
| S0273 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 86 | 86-86 |
| S0274 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 254 | 254-254 |
| S0275 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 255 | 255-255 |
| S0276 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 256 | 256-256 |
| S0277 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 257 | 257-257 |
| S0278 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 258 | 258-258 |
| S0279 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 259 | 259-259 |
| S0280 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 260 | 260-260 |
| S0281 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 261 | 261-261 |
| S0282 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 262 | 262-262 |
| S0283 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 263 | 263-263 |
| S0284 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 264 | 264-264 |
| S0285 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 265 | 265-265 |
| S0286 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 266 | 266-266 |
| S0287 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 267 | 267-267 |
| S0288 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 268 | 268-268 |
| S0289 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 269 | 269-269 |
| S0290 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 270 | 270-270 |
| S0291 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 271 | 271-271 |
| S0292 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 92 | 92-92 |
| S0293 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 272 | 272-272 |
| S0294 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 273 | 273-273 |
| S0295 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 274 | 274-274 |
| S0296 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 275 | 275-275 |
| S0297 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 276 | 276-276 |
| S0298 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 277 | 277-277 |
| S0299 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 278 | 278-278 |
| S0300 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 279 | 279-279 |
| S0301 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 280 | 280-280 |
| S0302 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 281 | 281-281 |
| S0303 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 282 | 282-282 |
| S0304 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 283 | 283-283 |
| S0305 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 284 | 284-284 |
| S0306 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 285 | 285-285 |
| S0307 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 286 | 286-286 |
| S0308 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 287 | 287-287 |
| S0309 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 288 | 288-288 |
| S0310 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 289 | 289-289 |
| S0311 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 98 | 98-98 |
| S0312 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 290 | 290-290 |
| S0313 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 291 | 291-291 |
| S0314 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 292 | 292-292 |
| S0315 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 293 | 293-293 |
| S0316 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 294 | 294-294 |
| S0317 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 295 | 295-295 |
| S0318 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 296 | 296-296 |
| S0319 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 297 | 297-297 |
| S0320 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 298 | 298-298 |
| S0321 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 299 | 299-299 |
| S0322 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 300 | 300-300 |
| S0323 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 301 | 301-301 |
| S0324 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 302 | 302-302 |
| S0325 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 303 | 303-303 |
| S0326 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 304 | 304-304 |
| S0327 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 305 | 305-305 |
| S0328 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 306 | 306-306 |
| S0329 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 307 | 307-307 |
| S0330 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 104 | 104-104 |
| S0331 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 308 | 308-308 |
| S0332 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 309 | 309-309 |
| S0333 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 310 | 310-310 |
| S0334 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 311 | 311-311 |
| S0335 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 312 | 312-312 |
| S0336 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 313 | 313-313 |
| S0337 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 314 | 314-314 |
| S0338 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 315 | 315-315 |
| S0339 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 316 | 316-316 |
| S0340 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 317 | 317-317 |
| S0341 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 318 | 318-318 |
| S0342 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 319 | 319-319 |
| S0343 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 320 | 320-320 |
| S0344 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 321 | 321-321 |
| S0345 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 322 | 322-322 |
| S0346 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 323 | 323-323 |
| S0347 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 324 | 324-324 |
| S0348 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 325 | 325-325 |
| S0349 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 110 | 110-110 |
| S0350 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 326 | 326-326 |
| S0351 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 327 | 327-327 |
| S0352 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 328 | 328-328 |
| S0353 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 329 | 329-329 |
| S0354 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 330 | 330-330 |
| S0355 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 331 | 331-331 |
| S0356 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 332 | 332-332 |
| S0357 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 333 | 333-333 |
| S0358 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 334 | 334-334 |
| S0359 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 335 | 335-335 |
| S0360 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 336 | 336-336 |
| S0361 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 337 | 337-337 |
| S0362 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 338 | 338-338 |
| S0363 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 339 | 339-339 |
| S0364 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 340 | 340-340 |
| S0365 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 341 | 341-341 |
| S0366 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 342 | 342-342 |
| S0367 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 343 | 343-343 |
| S0368 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 116 | 116-116 |
| S0369 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 344 | 344-344 |
| S0370 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 345 | 345-345 |
| S0371 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 346 | 346-346 |
| S0372 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 347 | 347-347 |
| S0373 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 348 | 348-348 |
| S0374 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 349 | 349-349 |
| S0375 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 350 | 350-350 |
| S0376 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 351 | 351-351 |
| S0377 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 352 | 352-352 |
| S0378 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 353 | 353-353 |
| S0379 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 354 | 354-354 |
| S0380 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 355 | 355-355 |
| S0381 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 356 | 356-356 |
| S0382 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 357 | 357-357 |
| S0383 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 358 | 358-358 |
| S0384 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 359 | 359-359 |
| S0385 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 360 | 360-360 |
| S0386 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 361 | 361-361 |
| S0387 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 122 | 122-122 |
| S0388 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 362 | 362-362 |
| S0389 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 363 | 363-363 |
| S0390 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 364 | 364-364 |
| S0391 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 365 | 365-365 |
| S0392 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 366 | 366-366 |
| S0393 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 367 | 367-367 |
| S0394 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 368 | 368-368 |
| S0395 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 369 | 369-369 |
| S0396 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 370 | 370-370 |
| S0397 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 371 | 371-371 |
| S0398 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 372 | 372-372 |
| S0399 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 373 | 373-373 |
| S0400 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 374 | 374-374 |
| S0401 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 375 | 375-375 |
| S0402 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 376 | 376-376 |
| S0403 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 377 | 377-377 |
| S0404 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 378 | 378-378 |
| S0405 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 379 | 379-379 |
| S0406 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 128 | 128-128 |
| S0407 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 380 | 380-380 |
| S0408 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 381 | 381-381 |
| S0409 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 382 | 382-382 |
| S0410 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 383 | 383-383 |
| S0411 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 384 | 384-384 |
| S0412 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 385 | 385-385 |
| S0413 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 386 | 386-386 |
| S0414 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 387 | 387-387 |
| S0415 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 388 | 388-388 |
| S0416 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 389 | 389-389 |
| S0417 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 390 | 390-390 |
| S0418 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 391 | 391-391 |
| S0419 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 392 | 392-392 |
| S0420 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 393 | 393-393 |
| S0421 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 394 | 394-394 |
| S0422 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 395 | 395-395 |
| S0423 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 396 | 396-396 |
| S0424 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 397 | 397-397 |
| S0425 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 134 | 134-134 |
| S0426 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 398 | 398-398 |
| S0427 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 399 | 399-399 |
| S0428 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 400 | 400-400 |
| S0429 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 401 | 401-401 |
| S0430 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 402 | 402-402 |
| S0431 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 403 | 403-403 |
| S0432 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 404 | 404-404 |
| S0433 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 405 | 405-405 |
| S0434 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 406 | 406-406 |
| S0435 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 407 | 407-407 |
| S0436 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 408 | 408-408 |
| S0437 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 409 | 409-409 |
| S0438 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 410 | 410-410 |
| S0439 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 411 | 411-411 |
| S0440 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 412 | 412-412 |
| S0441 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 413 | 413-413 |
| S0442 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 414 | 414-414 |
| S0443 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 415 | 415-415 |
| S0444 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 140 | 140-140 |
| S0445 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 416 | 416-416 |
| S0446 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 417 | 417-417 |
| S0447 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 418 | 418-418 |
| S0448 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 419 | 419-419 |
| S0449 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 420 | 420-420 |
| S0450 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 421 | 421-421 |
| S0451 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 422 | 422-422 |
| S0452 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 423 | 423-423 |
| S0453 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 424 | 424-424 |
| S0454 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 425 | 425-425 |
| S0455 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 426 | 426-426 |
| S0456 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 427 | 427-427 |
| S0457 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 428 | 428-428 |
| S0458 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 429 | 429-429 |
| S0459 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 430 | 430-430 |
| S0460 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 431 | 431-431 |
| S0461 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 432 | 432-432 |
| S0462 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 433 | 433-433 |
| S0463 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 146 | 146-146 |
| S0464 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 434 | 434-434 |
| S0465 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 435 | 435-435 |
| S0466 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 436 | 436-436 |
| S0467 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 437 | 437-437 |
| S0468 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 438 | 438-438 |
| S0469 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 439 | 439-439 |
| S0470 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 440 | 440-440 |
| S0471 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 441 | 441-441 |
| S0472 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 442 | 442-442 |
| S0473 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 443 | 443-443 |
| S0474 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 444 | 444-444 |
| S0475 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 445 | 445-445 |
| S0476 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 446 | 446-446 |
| S0477 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 447 | 447-447 |
| S0478 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 448 | 448-448 |
| S0479 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 449 | 449-449 |
| S0480 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 450 | 450-450 |
| S0481 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 451 | 451-451 |
| S0482 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 152 | 152-152 |
| S0483 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 452 | 452-452 |
| S0484 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 453 | 453-453 |
| S0485 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 454 | 454-454 |
| S0486 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 455 | 455-455 |
| S0487 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 456 | 456-456 |
| S0488 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 457 | 457-457 |
| S0489 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 458 | 458-458 |
| S0490 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 459 | 459-459 |
| S0491 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 460 | 460-460 |
| S0492 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 461 | 461-461 |
| S0493 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 462 | 462-462 |
| S0494 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 463 | 463-463 |
| S0495 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 464 | 464-464 |
| S0496 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 465 | 465-465 |
| S0497 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 466 | 466-466 |
| S0498 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 467 | 467-467 |
| S0499 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 468 | 468-468 |
| S0500 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 469 | 469-469 |
| S0501 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 158 | 158-158 |
| S0502 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 470 | 470-470 |
| S0503 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 471 | 471-471 |
| S0504 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 472 | 472-472 |
| S0505 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 473 | 473-473 |
| S0506 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 474 | 474-474 |
| S0507 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 475 | 475-475 |
| S0508 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 476 | 476-476 |
| S0509 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 477 | 477-477 |
| S0510 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 478 | 478-478 |
| S0511 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 479 | 479-479 |
| S0512 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 480 | 480-480 |
| S0513 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 481 | 481-481 |
| S0514 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 482 | 482-482 |
| S0515 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 483 | 483-483 |
| S0516 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 484 | 484-484 |
| S0517 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 485 | 485-485 |
| S0518 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 486 | 486-486 |
| S0519 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 487 | 487-487 |
| S0520 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 164 | 164-164 |
| S0521 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 488 | 488-488 |
| S0522 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 489 | 489-489 |
| S0523 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 490 | 490-490 |
| S0524 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 491 | 491-491 |
| S0525 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 492 | 492-492 |
| S0526 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 493 | 493-493 |
| S0527 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 494 | 494-494 |
| S0528 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 495 | 495-495 |
| S0529 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 496 | 496-496 |
| S0530 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 497 | 497-497 |
| S0531 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 498 | 498-498 |
| S0532 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 499 | 499-499 |
| S0533 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 500 | 500-500 |
| S0534 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 501 | 501-501 |
| S0535 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 502 | 502-502 |
| S0536 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 503 | 503-503 |
| S0537 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 504 | 504-504 |
| S0538 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 505 | 505-505 |
| S0539 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 170 | 170-170 |
| S0540 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 506 | 506-506 |
| S0541 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 507 | 507-507 |
| S0542 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 508 | 508-508 |
| S0543 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 509 | 509-509 |
| S0544 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 510 | 510-510 |
| S0545 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 511 | 511-511 |
| S0546 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 512 | 512-512 |
| S0547 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 513 | 513-513 |
| S0548 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 514 | 514-514 |
| S0549 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 515 | 515-515 |
| S0550 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 516 | 516-516 |
| S0551 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 517 | 517-517 |
| S0552 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 518 | 518-518 |
| S0553 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 519 | 519-519 |
| S0554 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 520 | 520-520 |
| S0555 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 521 | 521-521 |
| S0556 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 522 | 522-522 |
| S0557 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 523 | 523-523 |
| S0558 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 176 | 176-176 |
| S0559 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 524 | 524-524 |
| S0560 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 525 | 525-525 |
| S0561 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 526 | 526-526 |
| S0562 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 527 | 527-527 |
| S0563 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 528 | 528-528 |
| S0564 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 529 | 529-529 |
| S0565 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 530 | 530-530 |
| S0566 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 531 | 531-531 |
| S0567 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 532 | 532-532 |
| S0568 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 533 | 533-533 |
| S0569 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 534 | 534-534 |
| S0570 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 535 | 535-535 |
| S0571 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 536 | 536-536 |
| S0572 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 537 | 537-537 |
| S0573 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 538 | 538-538 |
| S0574 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 539 | 539-539 |
| S0575 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 540 | 540-540 |
| S0576 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 541 | 541-541 |
| S0577 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 182 | 182-182 |
| S0578 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 542 | 542-542 |
| S0579 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 543 | 543-543 |
| S0580 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 544 | 544-544 |
| S0581 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 545 | 545-545 |
| S0582 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 546 | 546-546 |
| S0583 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 547 | 547-547 |
| S0584 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 548 | 548-548 |
| S0585 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 549 | 549-549 |
| S0586 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 550 | 550-550 |
| S0587 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 551 | 551-551 |
| S0588 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 552 | 552-552 |
| S0589 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 553 | 553-553 |
| S0590 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 554 | 554-554 |
| S0591 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 555 | 555-555 |
| S0592 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 556 | 556-556 |
| S0593 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 557 | 557-557 |
| S0594 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 558 | 558-558 |
| S0595 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 559 | 559-559 |
| S0596 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 188 | 188-188 |
| S0597 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 560 | 560-560 |
| S0598 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 561 | 561-561 |
| S0599 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 562 | 562-562 |
| S0600 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 563 | 563-563 |
| S0601 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 564 | 564-564 |
| S0602 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 565 | 565-565 |
| S0603 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 566 | 566-566 |
| S0604 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 567 | 567-567 |
| S0605 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 568 | 568-568 |
| S0606 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 569 | 569-569 |
| S0607 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 570 | 570-570 |
| S0608 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 571 | 571-571 |
| S0609 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 572 | 572-572 |
| S0610 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 573 | 573-573 |
| S0611 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 574 | 574-574 |
| S0612 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 575 | 575-575 |
| S0613 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 576 | 576-576 |
| S0614 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 577 | 577-577 |
| S0615 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 194 | 194-194 |
| S0616 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 578 | 578-578 |
| S0617 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 579 | 579-579 |
| S0618 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 580 | 580-580 |
| S0619 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 581 | 581-581 |
| S0620 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 582 | 582-582 |
| S0621 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 583 | 583-583 |
| S0622 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 584 | 584-584 |
| S0623 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 585 | 585-585 |
| S0624 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 586 | 586-586 |
| S0625 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 587 | 587-587 |
| S0626 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 588 | 588-588 |
| S0627 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 589 | 589-589 |
| S0628 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 590 | 590-590 |
| S0629 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 591 | 591-591 |
| S0630 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 592 | 592-592 |
| S0631 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 593 | 593-593 |
| S0632 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 594 | 594-594 |
| S0633 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 595 | 595-595 |
| S0634 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 200 | 200-200 |
| S0635 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 596 | 596-596 |
| S0636 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 597 | 597-597 |
| S0637 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 598 | 598-598 |
| S0638 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 599 | 599-599 |
| S0639 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 600 | 600-600 |
| S0640 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 601 | 601-601 |
| S0641 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 602 | 602-602 |
| S0642 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 603 | 603-603 |
| S0643 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 604 | 604-604 |
| S0644 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 605 | 605-605 |
| S0645 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 606 | 606-606 |
| S0646 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 607 | 607-607 |
| S0647 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 608 | 608-608 |
| S0648 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 609 | 609-609 |
| S0649 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 610 | 610-610 |
| S0650 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 611 | 611-611 |
| S0651 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 612 | 612-612 |
| S0652 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 613 | 613-613 |
| S0653 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 206 | 206-206 |
| S0654 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 614 | 614-614 |
| S0655 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 615 | 615-615 |
| S0656 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 616 | 616-616 |
| S0657 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 617 | 617-617 |
| S0658 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 618 | 618-618 |
| S0659 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 619 | 619-619 |
| S0660 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 620 | 620-620 |
| S0661 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 621 | 621-621 |
| S0662 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 622 | 622-622 |
| S0663 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 623 | 623-623 |
| S0664 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 624 | 624-624 |
| S0665 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 625 | 625-625 |
| S0666 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 626 | 626-626 |
| S0667 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 627 | 627-627 |
| S0668 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 628 | 628-628 |
| S0669 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 629 | 629-629 |
| S0670 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 630 | 630-630 |
| S0671 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 631 | 631-631 |
| S0672 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 212 | 212-212 |
| S0673 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 632 | 632-632 |
| S0674 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 633 | 633-633 |
| S0675 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 634 | 634-634 |
| S0676 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 635 | 635-635 |
| S0677 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 636 | 636-636 |
| S0678 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 637 | 637-637 |
| S0679 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 638 | 638-638 |
| S0680 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 639 | 639-639 |
| S0681 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 640 | 640-640 |
| S0682 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 641 | 641-641 |
| S0683 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 642 | 642-642 |
| S0684 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 643 | 643-643 |
| S0685 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 644 | 644-644 |
| S0686 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 645 | 645-645 |
| S0687 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 646 | 646-646 |
| S0688 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 647 | 647-647 |
| S0689 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 648 | 648-648 |
| S0690 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 649 | 649-649 |
| S0691 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 218 | 218-218 |
| S0692 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 650 | 650-650 |
| S0693 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 651 | 651-651 |
| S0694 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 652 | 652-652 |
| S0695 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 653 | 653-653 |
| S0696 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 654 | 654-654 |
| S0697 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 655 | 655-655 |
| S0698 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 656 | 656-656 |
| S0699 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 657 | 657-657 |
| S0700 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 658 | 658-658 |
| S0701 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 659 | 659-659 |
| S0702 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 660 | 660-660 |
| S0703 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 661 | 661-661 |
| S0704 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 662 | 662-662 |
| S0705 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 663 | 663-663 |
| S0706 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 664 | 664-664 |
| S0707 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 665 | 665-665 |
| S0708 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 666 | 666-666 |
| S0709 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 667 | 667-667 |
| S0710 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 224 | 224-224 |
| S0711 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 668 | 668-668 |
| S0712 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 669 | 669-669 |
| S0713 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 670 | 670-670 |
| S0714 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 671 | 671-671 |
| S0715 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 672 | 672-672 |
| S0716 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 673 | 673-673 |
| S0717 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 674 | 674-674 |
| S0718 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 675 | 675-675 |
| S0719 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 676 | 676-676 |
| S0720 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 677 | 677-677 |
| S0721 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 678 | 678-678 |
| S0722 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 679 | 679-679 |
| S0723 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 680 | 680-680 |
| S0724 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 681 | 681-681 |
| S0725 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 682 | 682-682 |
| S0726 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 683 | 683-683 |
| S0727 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 684 | 684-684 |
| S0728 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 685 | 685-685 |
| S0729 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 230 | 230-230 |
| S0730 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 686 | 686-686 |
| S0731 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 687 | 687-687 |
| S0732 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 688 | 688-688 |
| S0733 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 689 | 689-689 |
| S0734 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 690 | 690-690 |
| S0735 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 691 | 691-691 |
| S0736 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 692 | 692-692 |
| S0737 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 693 | 693-693 |
| S0738 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 694 | 694-694 |
| S0739 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 695 | 695-695 |
| S0740 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 696 | 696-696 |
| S0741 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 697 | 697-697 |
| S0742 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 698 | 698-698 |
| S0743 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 699 | 699-699 |
| S0744 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 700 | 700-700 |
| S0745 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 701 | 701-701 |
| S0746 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 702 | 702-702 |
| S0747 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 703 | 703-703 |
| S0748 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 236 | 236-236 |
| S0749 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 704 | 704-704 |
| S0750 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 705 | 705-705 |
| S0751 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 706 | 706-706 |
| S0752 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 707 | 707-707 |
| S0753 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 708 | 708-708 |
| S0754 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 709 | 709-709 |
| S0755 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 710 | 710-710 |
| S0756 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 711 | 711-711 |
| S0757 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 712 | 712-712 |
| S0758 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 713 | 713-713 |
| S0759 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 714 | 714-714 |
| S0760 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 715 | 715-715 |
| S0761 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 716 | 716-716 |
| S0762 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 717 | 717-717 |
| S0763 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 718 | 718-718 |
| S0764 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 719 | 719-719 |
| S0765 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 720 | 720-720 |
| S0766 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 721 | 721-721 |
| S0767 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 242 | 242-242 |
| S0768 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 722 | 722-722 |
| S0769 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 723 | 723-723 |
| S0770 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 724 | 724-724 |
| S0771 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 725 | 725-725 |
| S0772 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 726 | 726-726 |
| S0773 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 727 | 727-727 |
| S0774 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 728 | 728-728 |
| S0775 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 729 | 729-729 |
| S0776 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 730 | 730-730 |
| S0777 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 731 | 731-731 |
| S0778 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 732 | 732-732 |
| S0779 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 733 | 733-733 |
| S0780 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 734 | 734-734 |
| S0781 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 735 | 735-735 |
| S0782 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 736 | 736-736 |
| S0783 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 737 | 737-737 |
| S0784 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 738 | 738-738 |
| S0785 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 739 | 739-739 |
| S0786 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 248 | 248-248 |
| S0787 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 740 | 740-740 |
| S0788 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 741 | 741-741 |
| S0789 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 742 | 742-742 |
| S0790 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 743 | 743-743 |
| S0791 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 744 | 744-744 |
| S0792 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 745 | 745-745 |
| S0793 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 746 | 746-746 |
| S0794 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 747 | 747-747 |
| S0795 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 748 | 748-748 |
| S0796 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 749 | 749-749 |
| S0797 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 750 | 750-750 |
| S0798 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 751 | 751-751 |
| S0799 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 752 | 752-752 |
| S0800 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 753 | 753-753 |
| S0801 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 754 | 754-754 |
| S0802 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 755 | 755-755 |
| S0803 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 756 | 756-756 |
| S0804 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 757 | 757-757 |
| S0805 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 254 | 254-254 |
| S0806 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 758 | 758-758 |
| S0807 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 759 | 759-759 |
| S0808 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 760 | 760-760 |
| S0809 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 761 | 761-761 |
| S0810 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 762 | 762-762 |
| S0811 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 763 | 763-763 |
| S0812 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 764 | 764-764 |
| S0813 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 765 | 765-765 |
| S0814 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 766 | 766-766 |
| S0815 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 767 | 767-767 |
| S0816 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 768 | 768-768 |
| S0817 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 769 | 769-769 |
| S0818 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 770 | 770-770 |
| S0819 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 771 | 771-771 |
| S0820 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 772 | 772-772 |
| S0821 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 773 | 773-773 |
| S0822 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 774 | 774-774 |
| S0823 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 775 | 775-775 |
| S0824 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 260 | 260-260 |
| S0825 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 776 | 776-776 |
| S0826 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 777 | 777-777 |
| S0827 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 778 | 778-778 |
| S0828 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 779 | 779-779 |
| S0829 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 780 | 780-780 |
| S0830 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 781 | 781-781 |
| S0831 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 782 | 782-782 |
| S0832 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 783 | 783-783 |
| S0833 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 784 | 784-784 |
| S0834 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 785 | 785-785 |
| S0835 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 786 | 786-786 |
| S0836 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 787 | 787-787 |
| S0837 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 788 | 788-788 |
| S0838 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 789 | 789-789 |
| S0839 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 790 | 790-790 |
| S0840 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 791 | 791-791 |
| S0841 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 792 | 792-792 |
| S0842 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 793 | 793-793 |
| S0843 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 266 | 266-266 |
| S0844 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 794 | 794-794 |
| S0845 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 795 | 795-795 |
| S0846 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 796 | 796-796 |
| S0847 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 797 | 797-797 |
| S0848 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 798 | 798-798 |
| S0849 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 799 | 799-799 |
| S0850 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 800 | 800-800 |
| S0851 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 801 | 801-801 |
| S0852 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 802 | 802-802 |
| S0853 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 803 | 803-803 |
| S0854 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 804 | 804-804 |
| S0855 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 805 | 805-805 |
| S0856 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 806 | 806-806 |
| S0857 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 807 | 807-807 |
| S0858 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 808 | 808-808 |
| S0859 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 809 | 809-809 |
| S0860 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 810 | 810-810 |
| S0861 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 811 | 811-811 |
| S0862 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 272 | 272-272 |
| S0863 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 812 | 812-812 |
| S0864 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 813 | 813-813 |
| S0865 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 814 | 814-814 |
| S0866 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 815 | 815-815 |
| S0867 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 816 | 816-816 |
| S0868 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 817 | 817-817 |
| S0869 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 818 | 818-818 |
| S0870 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 819 | 819-819 |
| S0871 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 820 | 820-820 |
| S0872 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 821 | 821-821 |
| S0873 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 822 | 822-822 |
| S0874 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 823 | 823-823 |
| S0875 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 824 | 824-824 |
| S0876 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 825 | 825-825 |
| S0877 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 826 | 826-826 |
| S0878 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 827 | 827-827 |
| S0879 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 828 | 828-828 |
| S0880 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 829 | 829-829 |
| S0881 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 278 | 278-278 |
| S0882 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 830 | 830-830 |
| S0883 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 831 | 831-831 |
| S0884 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 832 | 832-832 |
| S0885 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 833 | 833-833 |
| S0886 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 834 | 834-834 |
| S0887 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 835 | 835-835 |
| S0888 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 836 | 836-836 |
| S0889 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 837 | 837-837 |
| S0890 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 838 | 838-838 |
| S0891 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 839 | 839-839 |
| S0892 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 840 | 840-840 |
| S0893 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 841 | 841-841 |
| S0894 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 842 | 842-842 |
| S0895 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 843 | 843-843 |
| S0896 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 844 | 844-844 |
| S0897 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 845 | 845-845 |
| S0898 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 846 | 846-846 |
| S0899 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 847 | 847-847 |
| S0900 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 284 | 284-284 |
| S0901 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 848 | 848-848 |
| S0902 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 849 | 849-849 |
| S0903 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 850 | 850-850 |
| S0904 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 851 | 851-851 |
| S0905 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 852 | 852-852 |
| S0906 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 853 | 853-853 |
| S0907 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 854 | 854-854 |
| S0908 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 855 | 855-855 |
| S0909 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 856 | 856-856 |
| S0910 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 857 | 857-857 |
| S0911 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 858 | 858-858 |
| S0912 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 859 | 859-859 |
| S0913 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 860 | 860-860 |
| S0914 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 861 | 861-861 |
| S0915 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 862 | 862-862 |
| S0916 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 863 | 863-863 |
| S0917 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 864 | 864-864 |
| S0918 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 865 | 865-865 |
| S0919 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 290 | 290-290 |
| S0920 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 866 | 866-866 |
| S0921 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 867 | 867-867 |
| S0922 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 868 | 868-868 |
| S0923 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 869 | 869-869 |
| S0924 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 870 | 870-870 |
| S0925 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 871 | 871-871 |
| S0926 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 872 | 872-872 |
| S0927 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 873 | 873-873 |
| S0928 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 874 | 874-874 |
| S0929 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 875 | 875-875 |
| S0930 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 876 | 876-876 |
| S0931 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 877 | 877-877 |
| S0932 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 878 | 878-878 |
| S0933 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 879 | 879-879 |
| S0934 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 880 | 880-880 |
| S0935 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 881 | 881-881 |
| S0936 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 882 | 882-882 |
| S0937 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 883 | 883-883 |
| S0938 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 296 | 296-296 |
| S0939 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 884 | 884-884 |
| S0940 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 885 | 885-885 |
| S0941 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 886 | 886-886 |
| S0942 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 887 | 887-887 |
| S0943 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 888 | 888-888 |
| S0944 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 889 | 889-889 |
| S0945 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 890 | 890-890 |
| S0946 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 891 | 891-891 |
| S0947 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 892 | 892-892 |
| S0948 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 893 | 893-893 |
| S0949 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 894 | 894-894 |
| S0950 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 895 | 895-895 |
| S0951 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 896 | 896-896 |
| S0952 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 897 | 897-897 |
| S0953 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 898 | 898-898 |
| S0954 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 899 | 899-899 |
| S0955 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 900 | 900-900 |
| S0956 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 901 | 901-901 |
| S0957 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 302 | 302-302 |
| S0958 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 902 | 902-902 |
| S0959 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 903 | 903-903 |
| S0960 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 904 | 904-904 |
| S0961 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 905 | 905-905 |
| S0962 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 906 | 906-906 |
| S0963 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 907 | 907-907 |
| S0964 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 908 | 908-908 |
| S0965 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 909 | 909-909 |
| S0966 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 910 | 910-910 |
| S0967 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 911 | 911-911 |
| S0968 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 912 | 912-912 |
| S0969 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 913 | 913-913 |
| S0970 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 914 | 914-914 |
| S0971 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 915 | 915-915 |
| S0972 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 916 | 916-916 |
| S0973 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 917 | 917-917 |
| S0974 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 918 | 918-918 |
| S0975 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 919 | 919-919 |
| S0976 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 308 | 308-308 |
| S0977 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 920 | 920-920 |
| S0978 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 921 | 921-921 |
| S0979 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 922 | 922-922 |
| S0980 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 923 | 923-923 |
| S0981 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 924 | 924-924 |
| S0982 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 925 | 925-925 |
| S0983 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 926 | 926-926 |
| S0984 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 927 | 927-927 |
| S0985 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 928 | 928-928 |
| S0986 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 929 | 929-929 |
| S0987 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 930 | 930-930 |
| S0988 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 931 | 931-931 |
| S0989 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 932 | 932-932 |
| S0990 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 933 | 933-933 |
| S0991 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 934 | 934-934 |
| S0992 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 935 | 935-935 |
| S0993 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 936 | 936-936 |
| S0994 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | CSV line 937 | 937-937 |
| S0995 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 3 | 3-3 |
| S0996 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/payroll-register.csv | CSV line 3 | 3-3 |
| S0997 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 9 | 9-9 |
| S0998 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 15 | 15-15 |
| S0999 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 21 | 21-21 |
| S1000 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 27 | 27-27 |
| S1001 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 33 | 33-33 |
| S1002 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 39 | 39-39 |
| S1003 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 45 | 45-45 |
| S1004 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 51 | 51-51 |
| S1005 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 57 | 57-57 |
| S1006 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 63 | 63-63 |
| S1007 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 69 | 69-69 |
| S1008 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 75 | 75-75 |
| S1009 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 81 | 81-81 |
| S1010 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 87 | 87-87 |
| S1011 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 93 | 93-93 |
| S1012 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 99 | 99-99 |
| S1013 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 105 | 105-105 |
| S1014 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 111 | 111-111 |
| S1015 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 117 | 117-117 |
| S1016 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 123 | 123-123 |
| S1017 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 129 | 129-129 |
| S1018 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 135 | 135-135 |
| S1019 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 141 | 141-141 |
| S1020 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 147 | 147-147 |
| S1021 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 153 | 153-153 |
| S1022 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 159 | 159-159 |
| S1023 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 165 | 165-165 |
| S1024 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 171 | 171-171 |
| S1025 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 177 | 177-177 |
| S1026 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 183 | 183-183 |
| S1027 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 189 | 189-189 |
| S1028 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 195 | 195-195 |
| S1029 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 201 | 201-201 |
| S1030 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 207 | 207-207 |
| S1031 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 213 | 213-213 |
| S1032 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 219 | 219-219 |
| S1033 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 225 | 225-225 |
| S1034 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 231 | 231-231 |
| S1035 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 237 | 237-237 |
| S1036 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 243 | 243-243 |
| S1037 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 249 | 249-249 |
| S1038 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 255 | 255-255 |
| S1039 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 261 | 261-261 |
| S1040 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 267 | 267-267 |
| S1041 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 273 | 273-273 |
| S1042 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 279 | 279-279 |
| S1043 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 285 | 285-285 |
| S1044 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 291 | 291-291 |
| S1045 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 297 | 297-297 |
| S1046 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 303 | 303-303 |
| S1047 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 309 | 309-309 |
| S1048 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 4 | 4-4 |
| S1049 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/payroll-register.csv | CSV line 4 | 4-4 |
| S1050 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 10 | 10-10 |
| S1051 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 16 | 16-16 |
| S1052 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 22 | 22-22 |
| S1053 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 28 | 28-28 |
| S1054 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 34 | 34-34 |
| S1055 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 40 | 40-40 |
| S1056 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 46 | 46-46 |
| S1057 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 52 | 52-52 |
| S1058 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 58 | 58-58 |
| S1059 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 64 | 64-64 |
| S1060 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 70 | 70-70 |
| S1061 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 76 | 76-76 |
| S1062 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 82 | 82-82 |
| S1063 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 88 | 88-88 |
| S1064 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 94 | 94-94 |
| S1065 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 100 | 100-100 |
| S1066 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 106 | 106-106 |
| S1067 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 112 | 112-112 |
| S1068 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 118 | 118-118 |
| S1069 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 124 | 124-124 |
| S1070 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 130 | 130-130 |
| S1071 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 136 | 136-136 |
| S1072 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 142 | 142-142 |
| S1073 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 148 | 148-148 |
| S1074 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 154 | 154-154 |
| S1075 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 160 | 160-160 |
| S1076 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 166 | 166-166 |
| S1077 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 172 | 172-172 |
| S1078 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 178 | 178-178 |
| S1079 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 184 | 184-184 |
| S1080 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 190 | 190-190 |
| S1081 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 196 | 196-196 |
| S1082 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 202 | 202-202 |
| S1083 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 208 | 208-208 |
| S1084 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 214 | 214-214 |
| S1085 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 220 | 220-220 |
| S1086 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 226 | 226-226 |
| S1087 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 232 | 232-232 |
| S1088 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 238 | 238-238 |
| S1089 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 244 | 244-244 |
| S1090 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 250 | 250-250 |
| S1091 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 256 | 256-256 |
| S1092 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 262 | 262-262 |
| S1093 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 268 | 268-268 |
| S1094 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 274 | 274-274 |
| S1095 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 280 | 280-280 |
| S1096 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 286 | 286-286 |
| S1097 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 292 | 292-292 |
| S1098 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 298 | 298-298 |
| S1099 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 304 | 304-304 |
| S1100 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 310 | 310-310 |
| S1101 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 5 | 5-5 |
| S1102 | /home/maxg/insurance01-inputs/classification-guide.md | CG-04 | 32-34 |
| S1103 | /home/maxg/insurance01-inputs/classification-guide.md | CG-07 | 27-30 |
| S1104 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:05 PM | 529-531 |
| S1105 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/payroll-register.csv | CSV line 5 | 5-5 |
| S1106 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 11 | 11-11 |
| S1107 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 17 | 17-17 |
| S1108 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 23 | 23-23 |
| S1109 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 29 | 29-29 |
| S1110 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 35 | 35-35 |
| S1111 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 41 | 41-41 |
| S1112 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 47 | 47-47 |
| S1113 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 53 | 53-53 |
| S1114 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 59 | 59-59 |
| S1115 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 65 | 65-65 |
| S1116 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 71 | 71-71 |
| S1117 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 77 | 77-77 |
| S1118 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 83 | 83-83 |
| S1119 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 89 | 89-89 |
| S1120 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 95 | 95-95 |
| S1121 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 101 | 101-101 |
| S1122 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 107 | 107-107 |
| S1123 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 113 | 113-113 |
| S1124 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 119 | 119-119 |
| S1125 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 125 | 125-125 |
| S1126 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 131 | 131-131 |
| S1127 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 137 | 137-137 |
| S1128 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 143 | 143-143 |
| S1129 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 149 | 149-149 |
| S1130 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 155 | 155-155 |
| S1131 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 161 | 161-161 |
| S1132 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 167 | 167-167 |
| S1133 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 173 | 173-173 |
| S1134 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 179 | 179-179 |
| S1135 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 185 | 185-185 |
| S1136 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 191 | 191-191 |
| S1137 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 197 | 197-197 |
| S1138 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 203 | 203-203 |
| S1139 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 209 | 209-209 |
| S1140 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 215 | 215-215 |
| S1141 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 221 | 221-221 |
| S1142 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 227 | 227-227 |
| S1143 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 233 | 233-233 |
| S1144 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 239 | 239-239 |
| S1145 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 245 | 245-245 |
| S1146 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 251 | 251-251 |
| S1147 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 257 | 257-257 |
| S1148 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 263 | 263-263 |
| S1149 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 269 | 269-269 |
| S1150 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 275 | 275-275 |
| S1151 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 281 | 281-281 |
| S1152 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 287 | 287-287 |
| S1153 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 293 | 293-293 |
| S1154 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 299 | 299-299 |
| S1155 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 305 | 305-305 |
| S1156 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 311 | 311-311 |
| S1157 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 6 | 6-6 |
| S1158 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/payroll-register.csv | CSV line 6 | 6-6 |
| S1159 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 12 | 12-12 |
| S1160 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 18 | 18-18 |
| S1161 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 24 | 24-24 |
| S1162 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 30 | 30-30 |
| S1163 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 36 | 36-36 |
| S1164 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 42 | 42-42 |
| S1165 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 48 | 48-48 |
| S1166 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 54 | 54-54 |
| S1167 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 60 | 60-60 |
| S1168 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 66 | 66-66 |
| S1169 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 72 | 72-72 |
| S1170 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 78 | 78-78 |
| S1171 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 84 | 84-84 |
| S1172 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 90 | 90-90 |
| S1173 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 96 | 96-96 |
| S1174 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 102 | 102-102 |
| S1175 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 108 | 108-108 |
| S1176 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 114 | 114-114 |
| S1177 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 120 | 120-120 |
| S1178 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 126 | 126-126 |
| S1179 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 132 | 132-132 |
| S1180 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 138 | 138-138 |
| S1181 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 144 | 144-144 |
| S1182 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 150 | 150-150 |
| S1183 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 156 | 156-156 |
| S1184 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 162 | 162-162 |
| S1185 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 168 | 168-168 |
| S1186 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 174 | 174-174 |
| S1187 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 180 | 180-180 |
| S1188 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 186 | 186-186 |
| S1189 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 192 | 192-192 |
| S1190 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 198 | 198-198 |
| S1191 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 204 | 204-204 |
| S1192 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 210 | 210-210 |
| S1193 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 216 | 216-216 |
| S1194 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 222 | 222-222 |
| S1195 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 228 | 228-228 |
| S1196 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 234 | 234-234 |
| S1197 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 240 | 240-240 |
| S1198 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 246 | 246-246 |
| S1199 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 252 | 252-252 |
| S1200 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 258 | 258-258 |
| S1201 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 264 | 264-264 |
| S1202 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 270 | 270-270 |
| S1203 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 276 | 276-276 |
| S1204 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 282 | 282-282 |
| S1205 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 288 | 288-288 |
| S1206 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 294 | 294-294 |
| S1207 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 300 | 300-300 |
| S1208 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 306 | 306-306 |
| S1209 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 312 | 312-312 |
| S1210 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 7 | 7-7 |
| S1211 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/payroll-register.csv | CSV line 7 | 7-7 |
| S1212 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 13 | 13-13 |
| S1213 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 19 | 19-19 |
| S1214 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 25 | 25-25 |
| S1215 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 31 | 31-31 |
| S1216 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 37 | 37-37 |
| S1217 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 43 | 43-43 |
| S1218 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 49 | 49-49 |
| S1219 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 55 | 55-55 |
| S1220 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 61 | 61-61 |
| S1221 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 67 | 67-67 |
| S1222 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 73 | 73-73 |
| S1223 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 79 | 79-79 |
| S1224 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 85 | 85-85 |
| S1225 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 91 | 91-91 |
| S1226 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 97 | 97-97 |
| S1227 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 103 | 103-103 |
| S1228 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 109 | 109-109 |
| S1229 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 115 | 115-115 |
| S1230 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 121 | 121-121 |
| S1231 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 127 | 127-127 |
| S1232 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 133 | 133-133 |
| S1233 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 139 | 139-139 |
| S1234 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 145 | 145-145 |
| S1235 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 151 | 151-151 |
| S1236 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 157 | 157-157 |
| S1237 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 163 | 163-163 |
| S1238 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 169 | 169-169 |
| S1239 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 175 | 175-175 |
| S1240 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 181 | 181-181 |
| S1241 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 187 | 187-187 |
| S1242 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 193 | 193-193 |
| S1243 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 199 | 199-199 |
| S1244 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 205 | 205-205 |
| S1245 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 211 | 211-211 |
| S1246 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 217 | 217-217 |
| S1247 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 223 | 223-223 |
| S1248 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 229 | 229-229 |
| S1249 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 235 | 235-235 |
| S1250 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 241 | 241-241 |
| S1251 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 247 | 247-247 |
| S1252 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 253 | 253-253 |
| S1253 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 259 | 259-259 |
| S1254 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 265 | 265-265 |
| S1255 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 271 | 271-271 |
| S1256 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 277 | 277-277 |
| S1257 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 283 | 283-283 |
| S1258 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 289 | 289-289 |
| S1259 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 295 | 295-295 |
| S1260 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 301 | 301-301 |
| S1261 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 307 | 307-307 |
| S1262 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | CSV line 313 | 313-313 |
| S1263 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/application.md | application class T-610 | 7-7 |
| S1264 | /home/maxg/insurance01-inputs/employer-files/annapolis-courier/application.md | application class C-110 | 8-8 |

| Original source file | SHA-256 |
| --- | --- |
| /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160 |
| /home/maxg/insurance01-inputs/classification-guide.md | 89480f691737a0e8a762a836b8412476e0ed9d0b37639eb898e2826771c1dba8 |
| /home/maxg/insurance01-inputs/employer-files/annapolis-courier/application.md | 8f3c3326bf18874c1c43cfaf60312f5b3ada13ad29a885c5a49f5418afc5b21b |
| /home/maxg/insurance01-inputs/employer-files/annapolis-courier/business-description.md | 89ca4f6f3f3944fd1642514c9f7991e5943b8f013ab6e293ac8b4af562aca220 |
| /home/maxg/insurance01-inputs/employer-files/annapolis-courier/field-notes.md | 38916588e94bb87cb17a4c4e8988515c505c53f943287d2c17e55a13efd8dc84 |
| /home/maxg/insurance01-inputs/employer-files/annapolis-courier/payroll-register.csv | 5d88008ff2ce2ea367a89e95bdd81f38cc14d210ee15fd1556ec37fb6493930b |
| /home/maxg/insurance01-inputs/employer-files/annapolis-courier/route-log.csv | b7a8a9584ee7a4df25a6506f4473cbb6f52189b4b8ccc628bf442457b0400189 |
| /home/maxg/insurance01-inputs/employer-files/annapolis-courier/weekly-payroll.csv | 3e23df9b8139a36585e96760027d6d8d3117aa441f416431a71679e8f3ad5782 |

</details>

<a id="e02"></a>
## Bay Crest Exteriors (bay-crest-exteriors)

Audit period: 2025-07-07 through 2026-07-05. Submitted split: **CORRECTED**.

The submitted split requires the verified class transfers/additions below. This arithmetic correction remains subject to the linked employer confirmations and auditor sign-off.

Verified-only CSV: /home/maxg/ch03-premium-audit/deliverables/codes/bay-crest-exteriors.csv; SHA-256 2cdc2c31cec105074269aa30c62c59b1bbd9fbb4d982d828bd56903c27211750.

| Code | Reported payroll | Verified payroll | Difference (verified minus reported) | Verified code paragraph |
| --- | --- | --- | --- | --- |
| C-110 | 363970.45 | 44812.35 | -319158.10 | CG-04 |
| R-310 | 177527.60 | 450480.60 | 272953.00 | CG-11 |
| R-320 | 0.00 | 46205.10 | 46205.10 | CG-12 |

Reported total $541498.05; original register $541498.05; register-minus-reported difference $0.00. Comparison definitive for current classifications: True (not human approval).

Application reported employee counts: C-110: 7; R-310: 3. Register employees: 10.

Application sources: S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310).

### Employee payroll — VERIFIED and OPEN

| Employee ID | Name | Original wages | VERIFIED wage allocation | VERIFIED additions | OPEN wages | Register source |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E01 | Darnell Price | 61240.55 | R-310 61240.55 | — | 0.00 | S0001 payroll-register.csv:2-2 (CSV line 2) |
| BC-E02 | Kevin Moraes | 58976.20 | R-310 58976.20 | — | 0.00 | S0232 payroll-register.csv:3-3 (CSV line 3) |
| BC-E03 | Sam Okonjo | 57310.85 | R-310 57310.85 | — | 0.00 | S0450 payroll-register.csv:4-4 (CSV line 4) |
| BC-E04 | Luis Carrillo | 54880.40 | R-310 54880.40 | — | 0.00 | S0670 payroll-register.csv:5-5 (CSV line 5) |
| BC-E05 | Brian Tull | 52115.75 | R-310 52115.75 | — | 0.00 | S0887 payroll-register.csv:6-6 (CSV line 6) |
| BC-E06 | Owen Petrakis | 49607.30 | R-310 49607.30 | — | 0.00 | S1100 payroll-register.csv:7-7 (CSV line 7) |
| BC-E07 | Rafael Duarte | 47918.65 | R-310 47918.65 | — | 0.00 | S1316 payroll-register.csv:8-8 (CSV line 8) |
| BC-E08 | Jamal Whitfield | 46205.10 | R-320 46205.10 | — | 0.00 | S1528 payroll-register.csv:9-9 (CSV line 9) |
| BC-E09 | Teresa Lindqvist | 68430.90 | R-310 68430.90 | — | 0.00 | S1743 payroll-register.csv:10-10 (CSV line 10) |
| BC-E10 | Nora Beckett | 44812.35 | C-110 44812.35 | — | 0.00 | S1758 payroll-register.csv:11-11 (CSV line 11) |

Employee-level application assignments below are marked inferred where the engine derives them from the submitted counts/payroll; they are not employer-supplied employee coding lists.

| Employee | Wage basis | Reported code | Calculated code | Status | Reported attribution | Reason / records |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E01 Darnell Price | 61240.55 | R-310 | R-310 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0001 payroll-register.csv:2-2 (CSV line 2); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E02 Kevin Moraes | 58976.20 | R-310 | R-310 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0232 payroll-register.csv:3-3 (CSV line 3); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E03 Sam Okonjo | 57310.85 | R-310 | R-310 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0450 payroll-register.csv:4-4 (CSV line 4); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E04 Luis Carrillo | 54880.40 | C-110 | R-310 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0670 payroll-register.csv:5-5 (CSV line 5); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E05 Brian Tull | 52115.75 | C-110 | R-310 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0887 payroll-register.csv:6-6 (CSV line 6); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E06 Owen Petrakis | 49607.30 | C-110 | R-310 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S1100 payroll-register.csv:7-7 (CSV line 7); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E07 Rafael Duarte | 47918.65 | C-110 | R-310 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S1316 payroll-register.csv:8-8 (CSV line 8); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E08 Jamal Whitfield | 46205.10 | C-110 | R-320 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S1528 payroll-register.csv:9-9 (CSV line 9); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E09 Teresa Lindqvist | 68430.90 | C-110 | R-310 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S1743 payroll-register.csv:10-10 (CSV line 10); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |
| BC-E10 Nora Beckett | 44812.35 | C-110 | C-110 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S1758 payroll-register.csv:11-11 (CSV line 11); S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310) |

### Applied rule boundaries

Each decision retains the existing evaluator's scope and conditions. OPEN decisions below describe an applicability/evidence gap, not an assigned classification. Payment rule reasons and exact references are also preserved with each adjustment.

| Rule | Decision status | Scope | Applicability boundaries | Exact rule sources |
| --- | --- | --- | --- | --- |
| roofing_siding | CLASSIFIED | whole_audit_period | contractor employer performing both roofing and siding within the audit period; field worker by actual duties; complete audit-period roof-day evidence | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:27-30 (CG-07); S0004 classification-guide.md:36-37 (CG-11); S0005 classification-guide.md:39-40 (CG-12); S0006 ch03-premium-audit-20261105-0222(1).md:513-515 (Nadia Brennan · 09:04 PM); S0007 ch03-premium-audit-20261105-0222(1).md:673-675 (Nadia Brennan · 09:16 PM) |
| contractor_office_visits | CLASSIFIED | whole_audit_period | contractor employer; office employee by actual duties; complete audit-period site sign-in evidence; five or more days requires an evidenced unique governing field code | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:27-30 (CG-07); S0004 classification-guide.md:36-37 (CG-11); S0005 classification-guide.md:39-40 (CG-12); S0006 ch03-premium-audit-20261105-0222(1).md:513-515 (Nadia Brennan · 09:04 PM); S0007 ch03-premium-audit-20261105-0222(1).md:673-675 (Nadia Brennan · 09:16 PM); S1744 classification-guide.md:32-34 (CG-04); S1745 ch03-premium-audit-20261105-0222(1).md:153-155 (Nadia Brennan · 06:03 PM); S1746 ch03-premium-audit-20261105-0222(1).md:305-307 (Nadia Brennan · 06:10 PM); S1747 ch03-premium-audit-20261105-0222(1).md:545-547 (Nadia Brennan · 09:06 PM) |
| contractor_office_visits | CLASSIFIED | whole_audit_period | contractor employer; office employee by actual duties; complete audit-period site sign-in evidence; five or more days requires an evidenced unique governing field code | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:27-30 (CG-07); S0004 classification-guide.md:36-37 (CG-11); S0005 classification-guide.md:39-40 (CG-12); S0006 ch03-premium-audit-20261105-0222(1).md:513-515 (Nadia Brennan · 09:04 PM); S0007 ch03-premium-audit-20261105-0222(1).md:673-675 (Nadia Brennan · 09:16 PM); S1744 classification-guide.md:32-34 (CG-04); S1745 ch03-premium-audit-20261105-0222(1).md:153-155 (Nadia Brennan · 06:03 PM); S1746 ch03-premium-audit-20261105-0222(1).md:305-307 (Nadia Brennan · 06:10 PM); S1747 ch03-premium-audit-20261105-0222(1).md:545-547 (Nadia Brennan · 09:06 PM) |

### Reconciliation and excluded payments

Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):

`541498.05 + 0.00 = 541498.05 + 0.00`; difference 0.00.

Known payroll basis (includes OPEN wages): $541498.05. Verified classified payroll: $541498.05.

Other payment adjustments: **NOT EVALUATED**. No verified assertion of zero additional exposure is made; the wage reconciliation covers supplied employee records only.

| Engine control | Reconciled | Difference |
| --- | --- | --- |
| allocation | True | 0.00 |
| independent | True | 0.00 |

Governing field code: R-310; supported field payroll R-310 382049.70; R-320 46205.10. Unique largest verified field-worker payroll; office wages are excluded from this first stage to avoid circular classification. Exact evidence and rule references follow in the review detail and source index.

### OPEN findings and required human resolution

Each finding remains unanswered even if its monetary effect is zero. Employer payroll/records contact supplies the requested records; responsible policy reviewer: auditor. Identity issues require documentary confirmation of the exact employee/payee, not an assumed alias.

- **OPEN — Unattributed site sign-ins**: Site rows lack a matching payroll identity. No employee identity or exact employee day count is inferred; their dates bound possible additional office visits. Required evidence/confirmation: Confirm whether the unmatched entries are nonpayroll visitors and correct any missing employee identities. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E02-Q014](audit-questions.md#e02-q014). Records: S1757 site-signin-log.csv:4-4 (CSV line 4).

- **OPEN — Application/classification comparison**: The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved. Required evidence/confirmation: Confirm the evidence-backed classification changes and resolve pending employee decisions; the application is not classification authority. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E02-Q011](audit-questions.md#e02-q011). Records: S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310).

- **OPEN — Application employee attribution**: Employee assignments are not explicitly listed on the application. A unique exact count/wage partition supports the inferred comparison. Required evidence/confirmation: Confirm the employer's employee-level reported codes; classification decisions remain based on work records. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E02-Q011](audit-questions.md#e02-q011). Records: S1759 application.md:7-7 (application class C-110); S1760 application.md:8-8 (application class R-310).

### UNAPPROVED PROPOSED treatments

These alternatives are outside all verified totals. They require the specific evidence below and explicit auditor approval, followed by a supported rerun.

No supported conditional treatment is recorded; do not invent one for the OPEN cases.

### Allocation, payment and evidence review detail

The following entries preserve each employee/pay week, adjustment/payment, deciding reason and record confirmation. VERIFIED calculations, OPEN findings and UNAPPROVED alternatives retain their original labels. Exact dated record fields and all confirmation prompts are in the linked question document.

#### E02-Q001 — Darnell Price [BC-E01]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q001](audit-questions.md#e02-q001).

Verified base-wage allocation: R-310 $61240.55. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

188 distinct roof days is at least 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 188; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E01 | audit period | audit period | 61240.55 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0083, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0102, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0140, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0197, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0216, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q002 — Kevin Moraes [BC-E02]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q002](audit-questions.md#e02-q002).

Verified base-wage allocation: R-310 $58976.20. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

176 distinct roof days is at least 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 176; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E02 | audit period | audit period | 58976.20 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0232, S0233, S0234, S0235, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0254, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0273, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0292, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0311, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0330, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0349, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0368, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0387, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0406, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0425, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0444, S0445, S0446, S0447, S0448, S0449, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q003 — Sam Okonjo [BC-E03]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q003](audit-questions.md#e02-q003).

Verified base-wage allocation: R-310 $57310.85. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

201 distinct roof days is at least 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 201; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E03 | audit period | audit period | 57310.85 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0463, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0482, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0501, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0520, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0539, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0558, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0577, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0596, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0615, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0634, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0653, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q004 — Luis Carrillo [BC-E04]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q004](audit-questions.md#e02-q004).

Verified base-wage allocation: R-310 $54880.40. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

164 distinct roof days is at least 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 164; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E04 | audit period | audit period | 54880.40 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0670, S0671, S0672, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0691, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0710, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0729, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0748, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0767, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0786, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0805, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0824, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0843, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0862, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0881, S0882, S0883, S0884, S0885, S0886, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q005 — Brian Tull [BC-E05]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q005](audit-questions.md#e02-q005).

Verified base-wage allocation: R-310 $52115.75. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

152 distinct roof days is at least 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 152; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E05 | audit period | audit period | 52115.75 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0900, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0919, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0938, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0957, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0976, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S0995, S0996, S0997, S0998, S0999, S1000, S1001, S1002, S1003, S1004, S1005, S1006, S1007, S1008, S1009, S1010, S1011, S1012, S1013, S1014, S1015, S1016, S1017, S1018, S1019, S1020, S1021, S1022, S1023, S1024, S1025, S1026, S1027, S1028, S1029, S1030, S1031, S1032, S1033, S1034, S1035, S1036, S1037, S1038, S1039, S1040, S1041, S1042, S1043, S1044, S1045, S1046, S1047, S1048, S1049, S1050, S1051, S1052, S1053, S1054, S1055, S1056, S1057, S1058, S1059, S1060, S1061, S1062, S1063, S1064, S1065, S1066, S1067, S1068, S1069, S1070, S1071, S1072, S1073, S1074, S1075, S1076, S1077, S1078, S1079, S1080, S1081, S1082, S1083, S1084, S1085, S1086, S1087, S1088, S1089, S1090, S1091, S1092, S1093, S1094, S1095, S1096, S1097, S1098, S1099, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q006 — Owen Petrakis [BC-E06]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q006](audit-questions.md#e02-q006).

Verified base-wage allocation: R-310 $49607.30. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

97 distinct roof days is at least 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 97; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E06 | audit period | audit period | 49607.30 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S1100, S1101, S1102, S1103, S1104, S1105, S1106, S1107, S1108, S1109, S1110, S1111, S1112, S1113, S1114, S1115, S1116, S1117, S1118, S1119, S1120, S1121, S1122, S1123, S1124, S1125, S1126, S1127, S1128, S1129, S1130, S1131, S1132, S1133, S1134, S1135, S1136, S1137, S1138, S1139, S1140, S1141, S1142, S1143, S1144, S1145, S1146, S1147, S1148, S1149, S1150, S1151, S1152, S1153, S1154, S1155, S1156, S1157, S1158, S1159, S1160, S1161, S1162, S1163, S1164, S1165, S1166, S1167, S1168, S1169, S1170, S1171, S1172, S1173, S1174, S1175, S1176, S1177, S1178, S1179, S1180, S1181, S1182, S1183, S1184, S1185, S1186, S1187, S1188, S1189, S1190, S1191, S1192, S1193, S1194, S1195, S1196, S1197, S1198, S1199, S1200, S1201, S1202, S1203, S1204, S1205, S1206, S1207, S1208, S1209, S1210, S1211, S1212, S1213, S1214, S1215, S1216, S1217, S1218, S1219, S1220, S1221, S1222, S1223, S1224, S1225, S1226, S1227, S1228, S1229, S1230, S1231, S1232, S1233, S1234, S1235, S1236, S1237, S1238, S1239, S1240, S1241, S1242, S1243, S1244, S1245, S1246, S1247, S1248, S1249, S1250, S1251, S1252, S1253, S1254, S1255, S1256, S1257, S1258, S1259, S1260, S1261, S1262, S1263, S1264, S1265, S1266, S1267, S1268, S1269, S1270, S1271, S1272, S1273, S1274, S1275, S1276, S1277, S1278, S1279, S1280, S1281, S1282, S1283, S1284, S1285, S1286, S1287, S1288, S1289, S1290, S1291, S1292, S1293, S1294, S1295, S1296, S1297, S1298, S1299, S1300, S1301, S1302, S1303, S1304, S1305, S1306, S1307, S1308, S1309, S1310, S1311, S1312, S1313, S1314, S1315, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q007 — Rafael Duarte [BC-E07]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q007](audit-questions.md#e02-q007).

Verified base-wage allocation: R-310 $47918.65. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

15 distinct roof days is at least 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 15; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E07 | audit period | audit period | 47918.65 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S1316, S1317, S1318, S1319, S1320, S1321, S1322, S1323, S1324, S1325, S1326, S1327, S1328, S1329, S1330, S1331, S1332, S1333, S1334, S1335, S1336, S1337, S1338, S1339, S1340, S1341, S1342, S1343, S1344, S1345, S1346, S1347, S1348, S1349, S1350, S1351, S1352, S1353, S1354, S1355, S1356, S1357, S1358, S1359, S1360, S1361, S1362, S1363, S1364, S1365, S1366, S1367, S1368, S1369, S1370, S1371, S1372, S1373, S1374, S1375, S1376, S1377, S1378, S1379, S1380, S1381, S1382, S1383, S1384, S1385, S1386, S1387, S1388, S1389, S1390, S1391, S1392, S1393, S1394, S1395, S1396, S1397, S1398, S1399, S1400, S1401, S1402, S1403, S1404, S1405, S1406, S1407, S1408, S1409, S1410, S1411, S1412, S1413, S1414, S1415, S1416, S1417, S1418, S1419, S1420, S1421, S1422, S1423, S1424, S1425, S1426, S1427, S1428, S1429, S1430, S1431, S1432, S1433, S1434, S1435, S1436, S1437, S1438, S1439, S1440, S1441, S1442, S1443, S1444, S1445, S1446, S1447, S1448, S1449, S1450, S1451, S1452, S1453, S1454, S1455, S1456, S1457, S1458, S1459, S1460, S1461, S1462, S1463, S1464, S1465, S1466, S1467, S1468, S1469, S1470, S1471, S1472, S1473, S1474, S1475, S1476, S1477, S1478, S1479, S1480, S1481, S1482, S1483, S1484, S1485, S1486, S1487, S1488, S1489, S1490, S1491, S1492, S1493, S1494, S1495, S1496, S1497, S1498, S1499, S1500, S1501, S1502, S1503, S1504, S1505, S1506, S1507, S1508, S1509, S1510, S1511, S1512, S1513, S1514, S1515, S1516, S1517, S1518, S1519, S1520, S1521, S1522, S1523, S1524, S1525, S1526, S1527, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q008 — Jamal Whitfield [BC-E08]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q008](audit-questions.md#e02-q008).

Verified base-wage allocation: R-320 $46205.10. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

9 distinct roof days is fewer than 15 for this roofing-and-siding contractor's field worker.

Recorded distinct roofing days: 9; confirm the indexed dated crew records and the rule's applicable business scope.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E08 | audit period | audit period | 46205.10 | R-320 | CG-12 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S1528, S1529, S1530, S1531, S1532, S1533, S1534, S1535, S1536, S1537, S1538, S1539, S1540, S1541, S1542, S1543, S1544, S1545, S1546, S1547, S1548, S1549, S1550, S1551, S1552, S1553, S1554, S1555, S1556, S1557, S1558, S1559, S1560, S1561, S1562, S1563, S1564, S1565, S1566, S1567, S1568, S1569, S1570, S1571, S1572, S1573, S1574, S1575, S1576, S1577, S1578, S1579, S1580, S1581, S1582, S1583, S1584, S1585, S1586, S1587, S1588, S1589, S1590, S1591, S1592, S1593, S1594, S1595, S1596, S1597, S1598, S1599, S1600, S1601, S1602, S1603, S1604, S1605, S1606, S1607, S1608, S1609, S1610, S1611, S1612, S1613, S1614, S1615, S1616, S1617, S1618, S1619, S1620, S1621, S1622, S1623, S1624, S1625, S1626, S1627, S1628, S1629, S1630, S1631, S1632, S1633, S1634, S1635, S1636, S1637, S1638, S1639, S1640, S1641, S1642, S1643, S1644, S1645, S1646, S1647, S1648, S1649, S1650, S1651, S1652, S1653, S1654, S1655, S1656, S1657, S1658, S1659, S1660, S1661, S1662, S1663, S1664, S1665, S1666, S1667, S1668, S1669, S1670, S1671, S1672, S1673, S1674, S1675, S1676, S1677, S1678, S1679, S1680, S1681, S1682, S1683, S1684, S1685, S1686, S1687, S1688, S1689, S1690, S1691, S1692, S1693, S1694, S1695, S1696, S1697, S1698, S1699, S1700, S1701, S1702, S1703, S1704, S1705, S1706, S1707, S1708, S1709, S1710, S1711, S1712, S1713, S1714, S1715, S1716, S1717, S1718, S1719, S1720, S1721, S1722, S1723, S1724, S1725, S1726, S1727, S1728, S1729, S1730, S1731, S1732, S1733, S1734, S1735, S1736, S1737, S1738, S1739, S1740, S1741, S1742, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q009 — Teresa Lindqvist [BC-E09]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q009](audit-questions.md#e02-q009).

Verified base-wage allocation: R-310 $68430.90. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Between 9 confirmed and 10 possible site days; the existing contractor rule returns R-310 at both bounds. 9 distinct job-site days is at least five; use the evidenced governing field code for the whole audit period.

Confirmed distinct site-visit dates: 2025-07-24, 2025-09-02, 2025-11-17, 2025-11-26, 2025-12-25, 2026-03-04, 2026-05-26, 2026-06-03, 2026-07-01. Unattributed rows remain unassigned; confirm completeness separately.

| Unattributed source record | Date | Original employee ID | Original name | Site |
| --- | --- | --- | --- | --- |
| site-signin-log.csv:4 | 2025-10-09 | BLANK / UNATTRIBUTED | County inspector | Arnold re-roof |

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E09 | audit period | audit period | 68430.90 | R-310 | CG-11 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0083, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0102, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0140, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0197, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0216, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0235, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0254, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0273, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0292, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0311, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0330, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0349, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0368, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0387, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0406, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0425, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0444, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0463, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0482, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0501, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0520, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0539, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0558, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0577, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0596, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0615, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0634, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0653, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0672, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0691, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0710, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0729, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0748, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0767, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0786, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0805, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0824, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0843, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0862, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0881, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0900, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0919, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0938, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0957, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0976, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S0995, S0996, S0997, S0998, S0999, S1000, S1001, S1002, S1003, S1004, S1005, S1006, S1007, S1008, S1009, S1010, S1011, S1012, S1013, S1014, S1015, S1016, S1017, S1018, S1019, S1020, S1021, S1022, S1023, S1024, S1025, S1026, S1027, S1028, S1029, S1030, S1031, S1032, S1033, S1034, S1035, S1036, S1037, S1038, S1039, S1040, S1041, S1042, S1043, S1044, S1045, S1046, S1047, S1048, S1049, S1050, S1051, S1052, S1053, S1054, S1055, S1056, S1057, S1058, S1059, S1060, S1061, S1062, S1063, S1064, S1065, S1066, S1067, S1068, S1069, S1070, S1071, S1072, S1073, S1074, S1075, S1076, S1077, S1078, S1079, S1080, S1081, S1082, S1083, S1084, S1085, S1086, S1087, S1088, S1089, S1090, S1091, S1092, S1093, S1094, S1095, S1096, S1097, S1098, S1099, S1100, S1101, S1102, S1103, S1104, S1105, S1106, S1107, S1108, S1109, S1110, S1111, S1112, S1113, S1114, S1115, S1116, S1117, S1118, S1119, S1120, S1121, S1122, S1123, S1124, S1125, S1126, S1127, S1128, S1129, S1130, S1131, S1132, S1133, S1134, S1135, S1136, S1137, S1138, S1139, S1140, S1141, S1142, S1143, S1144, S1145, S1146, S1147, S1148, S1149, S1150, S1151, S1152, S1153, S1154, S1155, S1156, S1157, S1158, S1159, S1160, S1161, S1162, S1163, S1164, S1165, S1166, S1167, S1168, S1169, S1170, S1171, S1172, S1173, S1174, S1175, S1176, S1177, S1178, S1179, S1180, S1181, S1182, S1183, S1184, S1185, S1186, S1187, S1188, S1189, S1190, S1191, S1192, S1193, S1194, S1195, S1196, S1197, S1198, S1199, S1200, S1201, S1202, S1203, S1204, S1205, S1206, S1207, S1208, S1209, S1210, S1211, S1212, S1213, S1214, S1215, S1216, S1217, S1218, S1219, S1220, S1221, S1222, S1223, S1224, S1225, S1226, S1227, S1228, S1229, S1230, S1231, S1232, S1233, S1234, S1235, S1236, S1237, S1238, S1239, S1240, S1241, S1242, S1243, S1244, S1245, S1246, S1247, S1248, S1249, S1250, S1251, S1252, S1253, S1254, S1255, S1256, S1257, S1258, S1259, S1260, S1261, S1262, S1263, S1264, S1265, S1266, S1267, S1268, S1269, S1270, S1271, S1272, S1273, S1274, S1275, S1276, S1277, S1278, S1279, S1280, S1281, S1282, S1283, S1284, S1285, S1286, S1287, S1288, S1289, S1290, S1291, S1292, S1293, S1294, S1295, S1296, S1297, S1298, S1299, S1300, S1301, S1302, S1303, S1304, S1305, S1306, S1307, S1308, S1309, S1310, S1311, S1312, S1313, S1314, S1315, S1316, S1317, S1318, S1319, S1320, S1321, S1322, S1323, S1324, S1325, S1326, S1327, S1328, S1329, S1330, S1331, S1332, S1333, S1334, S1335, S1336, S1337, S1338, S1339, S1340, S1341, S1342, S1343, S1344, S1345, S1346, S1347, S1348, S1349, S1350, S1351, S1352, S1353, S1354, S1355, S1356, S1357, S1358, S1359, S1360, S1361, S1362, S1363, S1364, S1365, S1366, S1367, S1368, S1369, S1370, S1371, S1372, S1373, S1374, S1375, S1376, S1377, S1378, S1379, S1380, S1381, S1382, S1383, S1384, S1385, S1386, S1387, S1388, S1389, S1390, S1391, S1392, S1393, S1394, S1395, S1396, S1397, S1398, S1399, S1400, S1401, S1402, S1403, S1404, S1405, S1406, S1407, S1408, S1409, S1410, S1411, S1412, S1413, S1414, S1415, S1416, S1417, S1418, S1419, S1420, S1421, S1422, S1423, S1424, S1425, S1426, S1427, S1428, S1429, S1430, S1431, S1432, S1433, S1434, S1435, S1436, S1437, S1438, S1439, S1440, S1441, S1442, S1443, S1444, S1445, S1446, S1447, S1448, S1449, S1450, S1451, S1452, S1453, S1454, S1455, S1456, S1457, S1458, S1459, S1460, S1461, S1462, S1463, S1464, S1465, S1466, S1467, S1468, S1469, S1470, S1471, S1472, S1473, S1474, S1475, S1476, S1477, S1478, S1479, S1480, S1481, S1482, S1483, S1484, S1485, S1486, S1487, S1488, S1489, S1490, S1491, S1492, S1493, S1494, S1495, S1496, S1497, S1498, S1499, S1500, S1501, S1502, S1503, S1504, S1505, S1506, S1507, S1508, S1509, S1510, S1511, S1512, S1513, S1514, S1515, S1516, S1517, S1518, S1519, S1520, S1521, S1522, S1523, S1524, S1525, S1526, S1527, S1528, S1529, S1530, S1531, S1532, S1533, S1534, S1535, S1536, S1537, S1538, S1539, S1540, S1541, S1542, S1543, S1544, S1545, S1546, S1547, S1548, S1549, S1550, S1551, S1552, S1553, S1554, S1555, S1556, S1557, S1558, S1559, S1560, S1561, S1562, S1563, S1564, S1565, S1566, S1567, S1568, S1569, S1570, S1571, S1572, S1573, S1574, S1575, S1576, S1577, S1578, S1579, S1580, S1581, S1582, S1583, S1584, S1585, S1586, S1587, S1588, S1589, S1590, S1591, S1592, S1593, S1594, S1595, S1596, S1597, S1598, S1599, S1600, S1601, S1602, S1603, S1604, S1605, S1606, S1607, S1608, S1609, S1610, S1611, S1612, S1613, S1614, S1615, S1616, S1617, S1618, S1619, S1620, S1621, S1622, S1623, S1624, S1625, S1626, S1627, S1628, S1629, S1630, S1631, S1632, S1633, S1634, S1635, S1636, S1637, S1638, S1639, S1640, S1641, S1642, S1643, S1644, S1645, S1646, S1647, S1648, S1649, S1650, S1651, S1652, S1653, S1654, S1655, S1656, S1657, S1658, S1659, S1660, S1661, S1662, S1663, S1664, S1665, S1666, S1667, S1668, S1669, S1670, S1671, S1672, S1673, S1674, S1675, S1676, S1677, S1678, S1679, S1680, S1681, S1682, S1683, S1684, S1685, S1686, S1687, S1688, S1689, S1690, S1691, S1692, S1693, S1694, S1695, S1696, S1697, S1698, S1699, S1700, S1701, S1702, S1703, S1704, S1705, S1706, S1707, S1708, S1709, S1710, S1711, S1712, S1713, S1714, S1715, S1716, S1717, S1718, S1719, S1720, S1721, S1722, S1723, S1724, S1725, S1726, S1727, S1728, S1729, S1730, S1731, S1732, S1733, S1734, S1735, S1736, S1737, S1738, S1739, S1740, S1741, S1742, S1743, S1744, S1745, S1746, S1747, S1748, S1749, S1750, S1751, S1752, S1753, S1754, S1755, S1756, S1757, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q010 — Nora Beckett [BC-E10]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q010](audit-questions.md#e02-q010).

Verified base-wage allocation: C-110 $44812.35. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Between 0 confirmed and 1 possible site days; the existing contractor rule returns C-110 at both bounds. 0 distinct job-site days is at most four in the audit period.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Unattributed source record | Date | Original employee ID | Original name | Site |
| --- | --- | --- | --- | --- |
| site-signin-log.csv:4 | 2025-10-09 | BLANK / UNATTRIBUTED | County inspector | Arnold re-roof |

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-E10 | audit period | audit period | 44812.35 | C-110 | CG-04 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0083, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0102, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0140, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0197, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0216, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0235, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0254, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0273, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0292, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0311, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0330, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0349, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0368, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0387, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0406, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0425, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0444, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0463, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0482, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0501, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0520, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0539, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0558, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0577, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0596, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0615, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0634, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0653, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0672, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0691, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0710, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0729, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0748, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0767, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0786, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0805, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0824, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0843, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0862, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0881, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0900, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0919, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0938, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0957, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0976, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S0995, S0996, S0997, S0998, S0999, S1000, S1001, S1002, S1003, S1004, S1005, S1006, S1007, S1008, S1009, S1010, S1011, S1012, S1013, S1014, S1015, S1016, S1017, S1018, S1019, S1020, S1021, S1022, S1023, S1024, S1025, S1026, S1027, S1028, S1029, S1030, S1031, S1032, S1033, S1034, S1035, S1036, S1037, S1038, S1039, S1040, S1041, S1042, S1043, S1044, S1045, S1046, S1047, S1048, S1049, S1050, S1051, S1052, S1053, S1054, S1055, S1056, S1057, S1058, S1059, S1060, S1061, S1062, S1063, S1064, S1065, S1066, S1067, S1068, S1069, S1070, S1071, S1072, S1073, S1074, S1075, S1076, S1077, S1078, S1079, S1080, S1081, S1082, S1083, S1084, S1085, S1086, S1087, S1088, S1089, S1090, S1091, S1092, S1093, S1094, S1095, S1096, S1097, S1098, S1099, S1100, S1101, S1102, S1103, S1104, S1105, S1106, S1107, S1108, S1109, S1110, S1111, S1112, S1113, S1114, S1115, S1116, S1117, S1118, S1119, S1120, S1121, S1122, S1123, S1124, S1125, S1126, S1127, S1128, S1129, S1130, S1131, S1132, S1133, S1134, S1135, S1136, S1137, S1138, S1139, S1140, S1141, S1142, S1143, S1144, S1145, S1146, S1147, S1148, S1149, S1150, S1151, S1152, S1153, S1154, S1155, S1156, S1157, S1158, S1159, S1160, S1161, S1162, S1163, S1164, S1165, S1166, S1167, S1168, S1169, S1170, S1171, S1172, S1173, S1174, S1175, S1176, S1177, S1178, S1179, S1180, S1181, S1182, S1183, S1184, S1185, S1186, S1187, S1188, S1189, S1190, S1191, S1192, S1193, S1194, S1195, S1196, S1197, S1198, S1199, S1200, S1201, S1202, S1203, S1204, S1205, S1206, S1207, S1208, S1209, S1210, S1211, S1212, S1213, S1214, S1215, S1216, S1217, S1218, S1219, S1220, S1221, S1222, S1223, S1224, S1225, S1226, S1227, S1228, S1229, S1230, S1231, S1232, S1233, S1234, S1235, S1236, S1237, S1238, S1239, S1240, S1241, S1242, S1243, S1244, S1245, S1246, S1247, S1248, S1249, S1250, S1251, S1252, S1253, S1254, S1255, S1256, S1257, S1258, S1259, S1260, S1261, S1262, S1263, S1264, S1265, S1266, S1267, S1268, S1269, S1270, S1271, S1272, S1273, S1274, S1275, S1276, S1277, S1278, S1279, S1280, S1281, S1282, S1283, S1284, S1285, S1286, S1287, S1288, S1289, S1290, S1291, S1292, S1293, S1294, S1295, S1296, S1297, S1298, S1299, S1300, S1301, S1302, S1303, S1304, S1305, S1306, S1307, S1308, S1309, S1310, S1311, S1312, S1313, S1314, S1315, S1316, S1317, S1318, S1319, S1320, S1321, S1322, S1323, S1324, S1325, S1326, S1327, S1328, S1329, S1330, S1331, S1332, S1333, S1334, S1335, S1336, S1337, S1338, S1339, S1340, S1341, S1342, S1343, S1344, S1345, S1346, S1347, S1348, S1349, S1350, S1351, S1352, S1353, S1354, S1355, S1356, S1357, S1358, S1359, S1360, S1361, S1362, S1363, S1364, S1365, S1366, S1367, S1368, S1369, S1370, S1371, S1372, S1373, S1374, S1375, S1376, S1377, S1378, S1379, S1380, S1381, S1382, S1383, S1384, S1385, S1386, S1387, S1388, S1389, S1390, S1391, S1392, S1393, S1394, S1395, S1396, S1397, S1398, S1399, S1400, S1401, S1402, S1403, S1404, S1405, S1406, S1407, S1408, S1409, S1410, S1411, S1412, S1413, S1414, S1415, S1416, S1417, S1418, S1419, S1420, S1421, S1422, S1423, S1424, S1425, S1426, S1427, S1428, S1429, S1430, S1431, S1432, S1433, S1434, S1435, S1436, S1437, S1438, S1439, S1440, S1441, S1442, S1443, S1444, S1445, S1446, S1447, S1448, S1449, S1450, S1451, S1452, S1453, S1454, S1455, S1456, S1457, S1458, S1459, S1460, S1461, S1462, S1463, S1464, S1465, S1466, S1467, S1468, S1469, S1470, S1471, S1472, S1473, S1474, S1475, S1476, S1477, S1478, S1479, S1480, S1481, S1482, S1483, S1484, S1485, S1486, S1487, S1488, S1489, S1490, S1491, S1492, S1493, S1494, S1495, S1496, S1497, S1498, S1499, S1500, S1501, S1502, S1503, S1504, S1505, S1506, S1507, S1508, S1509, S1510, S1511, S1512, S1513, S1514, S1515, S1516, S1517, S1518, S1519, S1520, S1521, S1522, S1523, S1524, S1525, S1526, S1527, S1528, S1529, S1530, S1531, S1532, S1533, S1534, S1535, S1536, S1537, S1538, S1539, S1540, S1541, S1542, S1543, S1544, S1545, S1546, S1547, S1548, S1549, S1550, S1551, S1552, S1553, S1554, S1555, S1556, S1557, S1558, S1559, S1560, S1561, S1562, S1563, S1564, S1565, S1566, S1567, S1568, S1569, S1570, S1571, S1572, S1573, S1574, S1575, S1576, S1577, S1578, S1579, S1580, S1581, S1582, S1583, S1584, S1585, S1586, S1587, S1588, S1589, S1590, S1591, S1592, S1593, S1594, S1595, S1596, S1597, S1598, S1599, S1600, S1601, S1602, S1603, S1604, S1605, S1606, S1607, S1608, S1609, S1610, S1611, S1612, S1613, S1614, S1615, S1616, S1617, S1618, S1619, S1620, S1621, S1622, S1623, S1624, S1625, S1626, S1627, S1628, S1629, S1630, S1631, S1632, S1633, S1634, S1635, S1636, S1637, S1638, S1639, S1640, S1641, S1642, S1643, S1644, S1645, S1646, S1647, S1648, S1649, S1650, S1651, S1652, S1653, S1654, S1655, S1656, S1657, S1658, S1659, S1660, S1661, S1662, S1663, S1664, S1665, S1666, S1667, S1668, S1669, S1670, S1671, S1672, S1673, S1674, S1675, S1676, S1677, S1678, S1679, S1680, S1681, S1682, S1683, S1684, S1685, S1686, S1687, S1688, S1689, S1690, S1691, S1692, S1693, S1694, S1695, S1696, S1697, S1698, S1699, S1700, S1701, S1702, S1703, S1704, S1705, S1706, S1707, S1708, S1709, S1710, S1711, S1712, S1713, S1714, S1715, S1716, S1717, S1718, S1719, S1720, S1721, S1722, S1723, S1724, S1725, S1726, S1727, S1728, S1729, S1730, S1731, S1732, S1733, S1734, S1735, S1736, S1737, S1738, S1739, S1740, S1741, S1742, S1744, S1745, S1746, S1747, S1757, S1758, S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q011 — Application split, employee attribution and payroll reconciliation

**VERIFIED CALCULATION + OPEN FINDING / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E02-Q011](audit-questions.md#e02-q011).

Reconciliation verifies arithmetic, not employer confirmation or approval. Verified CSVs exclude OPEN wages and every unapproved proposal.

Application comparison definitive for current classifications: True; this is not audit approval.

The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved.

Employee assignments are not explicitly listed on the application. A unique exact count/wage partition supports the inferred comparison.

| Code | Reported payroll | Verified CSV payroll | Difference (verified minus reported) |
| --- | --- | --- | --- |
| C-110 | 363970.45 | 44812.35 | -319158.10 |
| R-310 | 177527.60 | 450480.60 | 272953.00 |
| R-320 | 0.00 | 46205.10 | 46205.10 |

| Control | Reconciled | Original basis | Unresolved amount |
| --- | --- | --- | --- |
| allocation | True | 541498.05 | 0.00 |
| independent | True | 541498.05 | 0.00 |

Supporting source IDs (local to this employer; exact locators below): S1759, S1760.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q012 — Business, actual-duty observations and audit-period completeness

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E02-Q012](audit-questions.md#e02-q012).

Classification depends on actual work and complete period evidence; job titles and the submitted application alone do not establish a code.

Unique largest verified field-worker payroll; office wages are excluded from this first stage to avoid circular classification.

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0083, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0102, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0140, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0197, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0216, S0217, S0218, S0219, S0220, S0221, S0222, S0223, S0224, S0225, S0226, S0227, S0228, S0229, S0230, S0231, S0232, S0233, S0234, S0235, S0236, S0237, S0238, S0239, S0240, S0241, S0242, S0243, S0244, S0245, S0246, S0247, S0248, S0249, S0250, S0251, S0252, S0253, S0254, S0255, S0256, S0257, S0258, S0259, S0260, S0261, S0262, S0263, S0264, S0265, S0266, S0267, S0268, S0269, S0270, S0271, S0272, S0273, S0274, S0275, S0276, S0277, S0278, S0279, S0280, S0281, S0282, S0283, S0284, S0285, S0286, S0287, S0288, S0289, S0290, S0291, S0292, S0293, S0294, S0295, S0296, S0297, S0298, S0299, S0300, S0301, S0302, S0303, S0304, S0305, S0306, S0307, S0308, S0309, S0310, S0311, S0312, S0313, S0314, S0315, S0316, S0317, S0318, S0319, S0320, S0321, S0322, S0323, S0324, S0325, S0326, S0327, S0328, S0329, S0330, S0331, S0332, S0333, S0334, S0335, S0336, S0337, S0338, S0339, S0340, S0341, S0342, S0343, S0344, S0345, S0346, S0347, S0348, S0349, S0350, S0351, S0352, S0353, S0354, S0355, S0356, S0357, S0358, S0359, S0360, S0361, S0362, S0363, S0364, S0365, S0366, S0367, S0368, S0369, S0370, S0371, S0372, S0373, S0374, S0375, S0376, S0377, S0378, S0379, S0380, S0381, S0382, S0383, S0384, S0385, S0386, S0387, S0388, S0389, S0390, S0391, S0392, S0393, S0394, S0395, S0396, S0397, S0398, S0399, S0400, S0401, S0402, S0403, S0404, S0405, S0406, S0407, S0408, S0409, S0410, S0411, S0412, S0413, S0414, S0415, S0416, S0417, S0418, S0419, S0420, S0421, S0422, S0423, S0424, S0425, S0426, S0427, S0428, S0429, S0430, S0431, S0432, S0433, S0434, S0435, S0436, S0437, S0438, S0439, S0440, S0441, S0442, S0443, S0444, S0445, S0446, S0447, S0448, S0449, S0450, S0451, S0452, S0453, S0454, S0455, S0456, S0457, S0458, S0459, S0460, S0461, S0462, S0463, S0464, S0465, S0466, S0467, S0468, S0469, S0470, S0471, S0472, S0473, S0474, S0475, S0476, S0477, S0478, S0479, S0480, S0481, S0482, S0483, S0484, S0485, S0486, S0487, S0488, S0489, S0490, S0491, S0492, S0493, S0494, S0495, S0496, S0497, S0498, S0499, S0500, S0501, S0502, S0503, S0504, S0505, S0506, S0507, S0508, S0509, S0510, S0511, S0512, S0513, S0514, S0515, S0516, S0517, S0518, S0519, S0520, S0521, S0522, S0523, S0524, S0525, S0526, S0527, S0528, S0529, S0530, S0531, S0532, S0533, S0534, S0535, S0536, S0537, S0538, S0539, S0540, S0541, S0542, S0543, S0544, S0545, S0546, S0547, S0548, S0549, S0550, S0551, S0552, S0553, S0554, S0555, S0556, S0557, S0558, S0559, S0560, S0561, S0562, S0563, S0564, S0565, S0566, S0567, S0568, S0569, S0570, S0571, S0572, S0573, S0574, S0575, S0576, S0577, S0578, S0579, S0580, S0581, S0582, S0583, S0584, S0585, S0586, S0587, S0588, S0589, S0590, S0591, S0592, S0593, S0594, S0595, S0596, S0597, S0598, S0599, S0600, S0601, S0602, S0603, S0604, S0605, S0606, S0607, S0608, S0609, S0610, S0611, S0612, S0613, S0614, S0615, S0616, S0617, S0618, S0619, S0620, S0621, S0622, S0623, S0624, S0625, S0626, S0627, S0628, S0629, S0630, S0631, S0632, S0633, S0634, S0635, S0636, S0637, S0638, S0639, S0640, S0641, S0642, S0643, S0644, S0645, S0646, S0647, S0648, S0649, S0650, S0651, S0652, S0653, S0654, S0655, S0656, S0657, S0658, S0659, S0660, S0661, S0662, S0663, S0664, S0665, S0666, S0667, S0668, S0669, S0670, S0671, S0672, S0673, S0674, S0675, S0676, S0677, S0678, S0679, S0680, S0681, S0682, S0683, S0684, S0685, S0686, S0687, S0688, S0689, S0690, S0691, S0692, S0693, S0694, S0695, S0696, S0697, S0698, S0699, S0700, S0701, S0702, S0703, S0704, S0705, S0706, S0707, S0708, S0709, S0710, S0711, S0712, S0713, S0714, S0715, S0716, S0717, S0718, S0719, S0720, S0721, S0722, S0723, S0724, S0725, S0726, S0727, S0728, S0729, S0730, S0731, S0732, S0733, S0734, S0735, S0736, S0737, S0738, S0739, S0740, S0741, S0742, S0743, S0744, S0745, S0746, S0747, S0748, S0749, S0750, S0751, S0752, S0753, S0754, S0755, S0756, S0757, S0758, S0759, S0760, S0761, S0762, S0763, S0764, S0765, S0766, S0767, S0768, S0769, S0770, S0771, S0772, S0773, S0774, S0775, S0776, S0777, S0778, S0779, S0780, S0781, S0782, S0783, S0784, S0785, S0786, S0787, S0788, S0789, S0790, S0791, S0792, S0793, S0794, S0795, S0796, S0797, S0798, S0799, S0800, S0801, S0802, S0803, S0804, S0805, S0806, S0807, S0808, S0809, S0810, S0811, S0812, S0813, S0814, S0815, S0816, S0817, S0818, S0819, S0820, S0821, S0822, S0823, S0824, S0825, S0826, S0827, S0828, S0829, S0830, S0831, S0832, S0833, S0834, S0835, S0836, S0837, S0838, S0839, S0840, S0841, S0842, S0843, S0844, S0845, S0846, S0847, S0848, S0849, S0850, S0851, S0852, S0853, S0854, S0855, S0856, S0857, S0858, S0859, S0860, S0861, S0862, S0863, S0864, S0865, S0866, S0867, S0868, S0869, S0870, S0871, S0872, S0873, S0874, S0875, S0876, S0877, S0878, S0879, S0880, S0881, S0882, S0883, S0884, S0885, S0886, S0887, S0888, S0889, S0890, S0891, S0892, S0893, S0894, S0895, S0896, S0897, S0898, S0899, S0900, S0901, S0902, S0903, S0904, S0905, S0906, S0907, S0908, S0909, S0910, S0911, S0912, S0913, S0914, S0915, S0916, S0917, S0918, S0919, S0920, S0921, S0922, S0923, S0924, S0925, S0926, S0927, S0928, S0929, S0930, S0931, S0932, S0933, S0934, S0935, S0936, S0937, S0938, S0939, S0940, S0941, S0942, S0943, S0944, S0945, S0946, S0947, S0948, S0949, S0950, S0951, S0952, S0953, S0954, S0955, S0956, S0957, S0958, S0959, S0960, S0961, S0962, S0963, S0964, S0965, S0966, S0967, S0968, S0969, S0970, S0971, S0972, S0973, S0974, S0975, S0976, S0977, S0978, S0979, S0980, S0981, S0982, S0983, S0984, S0985, S0986, S0987, S0988, S0989, S0990, S0991, S0992, S0993, S0994, S0995, S0996, S0997, S0998, S0999, S1000, S1001, S1002, S1003, S1004, S1005, S1006, S1007, S1008, S1009, S1010, S1011, S1012, S1013, S1014, S1015, S1016, S1017, S1018, S1019, S1020, S1021, S1022, S1023, S1024, S1025, S1026, S1027, S1028, S1029, S1030, S1031, S1032, S1033, S1034, S1035, S1036, S1037, S1038, S1039, S1040, S1041, S1042, S1043, S1044, S1045, S1046, S1047, S1048, S1049, S1050, S1051, S1052, S1053, S1054, S1055, S1056, S1057, S1058, S1059, S1060, S1061, S1062, S1063, S1064, S1065, S1066, S1067, S1068, S1069, S1070, S1071, S1072, S1073, S1074, S1075, S1076, S1077, S1078, S1079, S1080, S1081, S1082, S1083, S1084, S1085, S1086, S1087, S1088, S1089, S1090, S1091, S1092, S1093, S1094, S1095, S1096, S1097, S1098, S1099, S1100, S1101, S1102, S1103, S1104, S1105, S1106, S1107, S1108, S1109, S1110, S1111, S1112, S1113, S1114, S1115, S1116, S1117, S1118, S1119, S1120, S1121, S1122, S1123, S1124, S1125, S1126, S1127, S1128, S1129, S1130, S1131, S1132, S1133, S1134, S1135, S1136, S1137, S1138, S1139, S1140, S1141, S1142, S1143, S1144, S1145, S1146, S1147, S1148, S1149, S1150, S1151, S1152, S1153, S1154, S1155, S1156, S1157, S1158, S1159, S1160, S1161, S1162, S1163, S1164, S1165, S1166, S1167, S1168, S1169, S1170, S1171, S1172, S1173, S1174, S1175, S1176, S1177, S1178, S1179, S1180, S1181, S1182, S1183, S1184, S1185, S1186, S1187, S1188, S1189, S1190, S1191, S1192, S1193, S1194, S1195, S1196, S1197, S1198, S1199, S1200, S1201, S1202, S1203, S1204, S1205, S1206, S1207, S1208, S1209, S1210, S1211, S1212, S1213, S1214, S1215, S1216, S1217, S1218, S1219, S1220, S1221, S1222, S1223, S1224, S1225, S1226, S1227, S1228, S1229, S1230, S1231, S1232, S1233, S1234, S1235, S1236, S1237, S1238, S1239, S1240, S1241, S1242, S1243, S1244, S1245, S1246, S1247, S1248, S1249, S1250, S1251, S1252, S1253, S1254, S1255, S1256, S1257, S1258, S1259, S1260, S1261, S1262, S1263, S1264, S1265, S1266, S1267, S1268, S1269, S1270, S1271, S1272, S1273, S1274, S1275, S1276, S1277, S1278, S1279, S1280, S1281, S1282, S1283, S1284, S1285, S1286, S1287, S1288, S1289, S1290, S1291, S1292, S1293, S1294, S1295, S1296, S1297, S1298, S1299, S1300, S1301, S1302, S1303, S1304, S1305, S1306, S1307, S1308, S1309, S1310, S1311, S1312, S1313, S1314, S1315, S1316, S1317, S1318, S1319, S1320, S1321, S1322, S1323, S1324, S1325, S1326, S1327, S1328, S1329, S1330, S1331, S1332, S1333, S1334, S1335, S1336, S1337, S1338, S1339, S1340, S1341, S1342, S1343, S1344, S1345, S1346, S1347, S1348, S1349, S1350, S1351, S1352, S1353, S1354, S1355, S1356, S1357, S1358, S1359, S1360, S1361, S1362, S1363, S1364, S1365, S1366, S1367, S1368, S1369, S1370, S1371, S1372, S1373, S1374, S1375, S1376, S1377, S1378, S1379, S1380, S1381, S1382, S1383, S1384, S1385, S1386, S1387, S1388, S1389, S1390, S1391, S1392, S1393, S1394, S1395, S1396, S1397, S1398, S1399, S1400, S1401, S1402, S1403, S1404, S1405, S1406, S1407, S1408, S1409, S1410, S1411, S1412, S1413, S1414, S1415, S1416, S1417, S1418, S1419, S1420, S1421, S1422, S1423, S1424, S1425, S1426, S1427, S1428, S1429, S1430, S1431, S1432, S1433, S1434, S1435, S1436, S1437, S1438, S1439, S1440, S1441, S1442, S1443, S1444, S1445, S1446, S1447, S1448, S1449, S1450, S1451, S1452, S1453, S1454, S1455, S1456, S1457, S1458, S1459, S1460, S1461, S1462, S1463, S1464, S1465, S1466, S1467, S1468, S1469, S1470, S1471, S1472, S1473, S1474, S1475, S1476, S1477, S1478, S1479, S1480, S1481, S1482, S1483, S1484, S1485, S1486, S1487, S1488, S1489, S1490, S1491, S1492, S1493, S1494, S1495, S1496, S1497, S1498, S1499, S1500, S1501, S1502, S1503, S1504, S1505, S1506, S1507, S1508, S1509, S1510, S1511, S1512, S1513, S1514, S1515, S1516, S1517, S1518, S1519, S1520, S1521, S1522, S1523, S1524, S1525, S1526, S1527, S1528, S1529, S1530, S1531, S1532, S1533, S1534, S1535, S1536, S1537, S1538, S1539, S1540, S1541, S1542, S1543, S1544, S1545, S1546, S1547, S1548, S1549, S1550, S1551, S1552, S1553, S1554, S1555, S1556, S1557, S1558, S1559, S1560, S1561, S1562, S1563, S1564, S1565, S1566, S1567, S1568, S1569, S1570, S1571, S1572, S1573, S1574, S1575, S1576, S1577, S1578, S1579, S1580, S1581, S1582, S1583, S1584, S1585, S1586, S1587, S1588, S1589, S1590, S1591, S1592, S1593, S1594, S1595, S1596, S1597, S1598, S1599, S1600, S1601, S1602, S1603, S1604, S1605, S1606, S1607, S1608, S1609, S1610, S1611, S1612, S1613, S1614, S1615, S1616, S1617, S1618, S1619, S1620, S1621, S1622, S1623, S1624, S1625, S1626, S1627, S1628, S1629, S1630, S1631, S1632, S1633, S1634, S1635, S1636, S1637, S1638, S1639, S1640, S1641, S1642, S1643, S1644, S1645, S1646, S1647, S1648, S1649, S1650, S1651, S1652, S1653, S1654, S1655, S1656, S1657, S1658, S1659, S1660, S1661, S1662, S1663, S1664, S1665, S1666, S1667, S1668, S1669, S1670, S1671, S1672, S1673, S1674, S1675, S1676, S1677, S1678, S1679, S1680, S1681, S1682, S1683, S1684, S1685, S1686, S1687, S1688, S1689, S1690, S1691, S1692, S1693, S1694, S1695, S1696, S1697, S1698, S1699, S1700, S1701, S1702, S1703, S1704, S1705, S1706, S1707, S1708, S1709, S1710, S1711, S1712, S1713, S1714, S1715, S1716, S1717, S1718, S1719, S1720, S1721, S1722, S1723, S1724, S1725, S1726, S1727, S1728, S1729, S1730, S1731, S1732, S1733, S1734, S1735, S1736, S1737, S1738, S1739, S1740, S1741, S1742.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q013 — Company-rule applicability — auditor confirmation

**AUDITOR APPROVAL / EMPLOYER FACT CONFIRMATION**. Follow-up: [E02-Q013](audit-questions.md#e02-q013).

Contractor-specific practices cannot be extended to unrelated industries; proposals are not verified rules or allocations.

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0007, S1744, S1745, S1746, S1747.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E02-Q014 — Unattributed site sign-ins

**OPEN / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E02-Q014](audit-questions.md#e02-q014).

Site rows lack a matching payroll identity. No employee identity or exact employee day count is inferred; their dates bound possible additional office visits.

| Original source record | Date | Original employee ID | Original name | Site |
| --- | --- | --- | --- | --- |
| site-signin-log.csv:4 | 2025-10-09 | BLANK / UNATTRIBUTED | County inspector | Arnold re-roof |

Supporting source IDs (local to this employer; exact locators below): S1757.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

<details>
<summary>Source and rule index — 1760 exact citations</summary>

Original Classification Guide paragraph identifiers and interview timestamps/line spans are preserved here. Rule applicability is bounded by the recorded decision; a citation is not permission to extend a contractor practice to another business. Physical CSV row identities and confirmation links are preserved in the question document's record index.

| Source ID | Original document | Original paragraph / interview / record locator | Lines |
| --- | --- | --- | --- |
| S0001 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 2 | 2-2 |
| S0002 | /home/maxg/insurance01-inputs/classification-guide.md | CG-02 | 15-16 |
| S0003 | /home/maxg/insurance01-inputs/classification-guide.md | CG-07 | 27-30 |
| S0004 | /home/maxg/insurance01-inputs/classification-guide.md | CG-11 | 36-37 |
| S0005 | /home/maxg/insurance01-inputs/classification-guide.md | CG-12 | 39-40 |
| S0006 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:04 PM | 513-515 |
| S0007 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:16 PM | 673-675 |
| S0008 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/business-description.md | business description | 1-7 |
| S0009 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/field-notes.md | auditor field notes | 1-8 |
| S0010 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 2 | 2-2 |
| S0011 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 10 | 10-10 |
| S0012 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 16 | 16-16 |
| S0013 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 23 | 23-23 |
| S0014 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 29 | 29-29 |
| S0015 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 35 | 35-35 |
| S0016 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 43 | 43-43 |
| S0017 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 51 | 51-51 |
| S0018 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 58 | 58-58 |
| S0019 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 66 | 66-66 |
| S0020 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 74 | 74-74 |
| S0021 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 89 | 89-89 |
| S0022 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 96 | 96-96 |
| S0023 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 104 | 104-104 |
| S0024 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 111 | 111-111 |
| S0025 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 116 | 116-116 |
| S0026 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 124 | 124-124 |
| S0027 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 131 | 131-131 |
| S0028 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 137 | 137-137 |
| S0029 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 144 | 144-144 |
| S0030 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 152 | 152-152 |
| S0031 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 158 | 158-158 |
| S0032 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 163 | 163-163 |
| S0033 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 171 | 171-171 |
| S0034 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 178 | 178-178 |
| S0035 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 186 | 186-186 |
| S0036 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 192 | 192-192 |
| S0037 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 198 | 198-198 |
| S0038 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 204 | 204-204 |
| S0039 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 209 | 209-209 |
| S0040 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 223 | 223-223 |
| S0041 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 234 | 234-234 |
| S0042 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 242 | 242-242 |
| S0043 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 253 | 253-253 |
| S0044 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 261 | 261-261 |
| S0045 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 269 | 269-269 |
| S0046 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 276 | 276-276 |
| S0047 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 284 | 284-284 |
| S0048 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 291 | 291-291 |
| S0049 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 298 | 298-298 |
| S0050 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 305 | 305-305 |
| S0051 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 312 | 312-312 |
| S0052 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 320 | 320-320 |
| S0053 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 328 | 328-328 |
| S0054 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 333 | 333-333 |
| S0055 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 347 | 347-347 |
| S0056 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 354 | 354-354 |
| S0057 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 362 | 362-362 |
| S0058 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 369 | 369-369 |
| S0059 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 375 | 375-375 |
| S0060 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 382 | 382-382 |
| S0061 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 389 | 389-389 |
| S0062 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 395 | 395-395 |
| S0063 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 401 | 401-401 |
| S0064 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 408 | 408-408 |
| S0065 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 416 | 416-416 |
| S0066 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 421 | 421-421 |
| S0067 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 429 | 429-429 |
| S0068 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 445 | 445-445 |
| S0069 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 452 | 452-452 |
| S0070 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 460 | 460-460 |
| S0071 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 472 | 472-472 |
| S0072 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 484 | 484-484 |
| S0073 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 496 | 496-496 |
| S0074 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 504 | 504-504 |
| S0075 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 510 | 510-510 |
| S0076 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 518 | 518-518 |
| S0077 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 522 | 522-522 |
| S0078 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 530 | 530-530 |
| S0079 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 537 | 537-537 |
| S0080 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 545 | 545-545 |
| S0081 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 552 | 552-552 |
| S0082 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 557 | 557-557 |
| S0083 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 564 | 564-564 |
| S0084 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 571 | 571-571 |
| S0085 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 578 | 578-578 |
| S0086 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 585 | 585-585 |
| S0087 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 593 | 593-593 |
| S0088 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 601 | 601-601 |
| S0089 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 608 | 608-608 |
| S0090 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 616 | 616-616 |
| S0091 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 623 | 623-623 |
| S0092 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 627 | 627-627 |
| S0093 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 634 | 634-634 |
| S0094 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 638 | 638-638 |
| S0095 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 645 | 645-645 |
| S0096 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 651 | 651-651 |
| S0097 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 658 | 658-658 |
| S0098 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 666 | 666-666 |
| S0099 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 672 | 672-672 |
| S0100 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 680 | 680-680 |
| S0101 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 687 | 687-687 |
| S0102 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 694 | 694-694 |
| S0103 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 701 | 701-701 |
| S0104 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 708 | 708-708 |
| S0105 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 716 | 716-716 |
| S0106 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 722 | 722-722 |
| S0107 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 729 | 729-729 |
| S0108 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 735 | 735-735 |
| S0109 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 742 | 742-742 |
| S0110 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 749 | 749-749 |
| S0111 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 763 | 763-763 |
| S0112 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 776 | 776-776 |
| S0113 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 783 | 783-783 |
| S0114 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 790 | 790-790 |
| S0115 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 796 | 796-796 |
| S0116 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 802 | 802-802 |
| S0117 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 809 | 809-809 |
| S0118 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 817 | 817-817 |
| S0119 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 823 | 823-823 |
| S0120 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 830 | 830-830 |
| S0121 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 837 | 837-837 |
| S0122 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 850 | 850-850 |
| S0123 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 858 | 858-858 |
| S0124 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 866 | 866-866 |
| S0125 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 880 | 880-880 |
| S0126 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 886 | 886-886 |
| S0127 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 906 | 906-906 |
| S0128 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 911 | 911-911 |
| S0129 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 919 | 919-919 |
| S0130 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 927 | 927-927 |
| S0131 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 933 | 933-933 |
| S0132 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 939 | 939-939 |
| S0133 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 944 | 944-944 |
| S0134 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 952 | 952-952 |
| S0135 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 959 | 959-959 |
| S0136 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 972 | 972-972 |
| S0137 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 979 | 979-979 |
| S0138 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 987 | 987-987 |
| S0139 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 994 | 994-994 |
| S0140 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1005 | 1005-1005 |
| S0141 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1012 | 1012-1012 |
| S0142 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1020 | 1020-1020 |
| S0143 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1027 | 1027-1027 |
| S0144 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1032 | 1032-1032 |
| S0145 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1052 | 1052-1052 |
| S0146 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1060 | 1060-1060 |
| S0147 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1066 | 1066-1066 |
| S0148 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1074 | 1074-1074 |
| S0149 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1080 | 1080-1080 |
| S0150 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1086 | 1086-1086 |
| S0151 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1093 | 1093-1093 |
| S0152 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1101 | 1101-1101 |
| S0153 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1107 | 1107-1107 |
| S0154 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1114 | 1114-1114 |
| S0155 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1122 | 1122-1122 |
| S0156 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1130 | 1130-1130 |
| S0157 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1136 | 1136-1136 |
| S0158 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1142 | 1142-1142 |
| S0159 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1155 | 1155-1155 |
| S0160 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1162 | 1162-1162 |
| S0161 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1170 | 1170-1170 |
| S0162 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1177 | 1177-1177 |
| S0163 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1184 | 1184-1184 |
| S0164 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1192 | 1192-1192 |
| S0165 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1198 | 1198-1198 |
| S0166 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1205 | 1205-1205 |
| S0167 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1212 | 1212-1212 |
| S0168 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1219 | 1219-1219 |
| S0169 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1226 | 1226-1226 |
| S0170 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1232 | 1232-1232 |
| S0171 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1240 | 1240-1240 |
| S0172 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1247 | 1247-1247 |
| S0173 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1257 | 1257-1257 |
| S0174 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1263 | 1263-1263 |
| S0175 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1274 | 1274-1274 |
| S0176 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1281 | 1281-1281 |
| S0177 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1287 | 1287-1287 |
| S0178 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1295 | 1295-1295 |
| S0179 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1310 | 1310-1310 |
| S0180 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1316 | 1316-1316 |
| S0181 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1323 | 1323-1323 |
| S0182 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1340 | 1340-1340 |
| S0183 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1347 | 1347-1347 |
| S0184 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1354 | 1354-1354 |
| S0185 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1366 | 1366-1366 |
| S0186 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1372 | 1372-1372 |
| S0187 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1380 | 1380-1380 |
| S0188 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1387 | 1387-1387 |
| S0189 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1394 | 1394-1394 |
| S0190 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1401 | 1401-1401 |
| S0191 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1408 | 1408-1408 |
| S0192 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1415 | 1415-1415 |
| S0193 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1422 | 1422-1422 |
| S0194 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1431 | 1431-1431 |
| S0195 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1439 | 1439-1439 |
| S0196 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1443 | 1443-1443 |
| S0197 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1449 | 1449-1449 |
| S0198 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1455 | 1455-1455 |
| S0199 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1462 | 1462-1462 |
| S0200 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1469 | 1469-1469 |
| S0201 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1487 | 1487-1487 |
| S0202 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1495 | 1495-1495 |
| S0203 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1509 | 1509-1509 |
| S0204 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1516 | 1516-1516 |
| S0205 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1530 | 1530-1530 |
| S0206 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1536 | 1536-1536 |
| S0207 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1541 | 1541-1541 |
| S0208 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1548 | 1548-1548 |
| S0209 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1554 | 1554-1554 |
| S0210 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1561 | 1561-1561 |
| S0211 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1573 | 1573-1573 |
| S0212 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1585 | 1585-1585 |
| S0213 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1590 | 1590-1590 |
| S0214 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1597 | 1597-1597 |
| S0215 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1602 | 1602-1602 |
| S0216 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1609 | 1609-1609 |
| S0217 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1615 | 1615-1615 |
| S0218 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1621 | 1621-1621 |
| S0219 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1626 | 1626-1626 |
| S0220 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1636 | 1636-1636 |
| S0221 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1642 | 1642-1642 |
| S0222 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1649 | 1649-1649 |
| S0223 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1654 | 1654-1654 |
| S0224 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1662 | 1662-1662 |
| S0225 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1667 | 1667-1667 |
| S0226 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1682 | 1682-1682 |
| S0227 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1689 | 1689-1689 |
| S0228 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1702 | 1702-1702 |
| S0229 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1707 | 1707-1707 |
| S0230 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1713 | 1713-1713 |
| S0231 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1721 | 1721-1721 |
| S0232 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 3 | 3-3 |
| S0233 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 3 | 3-3 |
| S0234 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 11 | 11-11 |
| S0235 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 17 | 17-17 |
| S0236 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 30 | 30-30 |
| S0237 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 36 | 36-36 |
| S0238 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 44 | 44-44 |
| S0239 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 52 | 52-52 |
| S0240 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 59 | 59-59 |
| S0241 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 67 | 67-67 |
| S0242 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 75 | 75-75 |
| S0243 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 82 | 82-82 |
| S0244 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 97 | 97-97 |
| S0245 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 105 | 105-105 |
| S0246 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 112 | 112-112 |
| S0247 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 117 | 117-117 |
| S0248 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 125 | 125-125 |
| S0249 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 132 | 132-132 |
| S0250 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 138 | 138-138 |
| S0251 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 145 | 145-145 |
| S0252 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 153 | 153-153 |
| S0253 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 164 | 164-164 |
| S0254 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 172 | 172-172 |
| S0255 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 179 | 179-179 |
| S0256 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 187 | 187-187 |
| S0257 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 193 | 193-193 |
| S0258 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 205 | 205-205 |
| S0259 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 210 | 210-210 |
| S0260 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 216 | 216-216 |
| S0261 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 224 | 224-224 |
| S0262 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 229 | 229-229 |
| S0263 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 235 | 235-235 |
| S0264 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 243 | 243-243 |
| S0265 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 247 | 247-247 |
| S0266 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 254 | 254-254 |
| S0267 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 262 | 262-262 |
| S0268 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 270 | 270-270 |
| S0269 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 277 | 277-277 |
| S0270 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 285 | 285-285 |
| S0271 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 299 | 299-299 |
| S0272 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 306 | 306-306 |
| S0273 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 313 | 313-313 |
| S0274 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 321 | 321-321 |
| S0275 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 329 | 329-329 |
| S0276 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 334 | 334-334 |
| S0277 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 340 | 340-340 |
| S0278 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 348 | 348-348 |
| S0279 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 355 | 355-355 |
| S0280 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 363 | 363-363 |
| S0281 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 370 | 370-370 |
| S0282 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 376 | 376-376 |
| S0283 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 390 | 390-390 |
| S0284 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 402 | 402-402 |
| S0285 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 409 | 409-409 |
| S0286 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 422 | 422-422 |
| S0287 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 436 | 436-436 |
| S0288 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 446 | 446-446 |
| S0289 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 453 | 453-453 |
| S0290 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 461 | 461-461 |
| S0291 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 466 | 466-466 |
| S0292 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 473 | 473-473 |
| S0293 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 479 | 479-479 |
| S0294 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 485 | 485-485 |
| S0295 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 491 | 491-491 |
| S0296 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 497 | 497-497 |
| S0297 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 511 | 511-511 |
| S0298 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 523 | 523-523 |
| S0299 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 531 | 531-531 |
| S0300 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 538 | 538-538 |
| S0301 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 546 | 546-546 |
| S0302 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 553 | 553-553 |
| S0303 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 558 | 558-558 |
| S0304 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 565 | 565-565 |
| S0305 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 572 | 572-572 |
| S0306 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 579 | 579-579 |
| S0307 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 586 | 586-586 |
| S0308 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 594 | 594-594 |
| S0309 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 602 | 602-602 |
| S0310 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 609 | 609-609 |
| S0311 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 617 | 617-617 |
| S0312 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 624 | 624-624 |
| S0313 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 628 | 628-628 |
| S0314 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 639 | 639-639 |
| S0315 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 646 | 646-646 |
| S0316 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 652 | 652-652 |
| S0317 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 659 | 659-659 |
| S0318 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 667 | 667-667 |
| S0319 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 673 | 673-673 |
| S0320 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 681 | 681-681 |
| S0321 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 688 | 688-688 |
| S0322 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 695 | 695-695 |
| S0323 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 702 | 702-702 |
| S0324 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 709 | 709-709 |
| S0325 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 717 | 717-717 |
| S0326 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 723 | 723-723 |
| S0327 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 730 | 730-730 |
| S0328 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 736 | 736-736 |
| S0329 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 743 | 743-743 |
| S0330 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 750 | 750-750 |
| S0331 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 757 | 757-757 |
| S0332 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 764 | 764-764 |
| S0333 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 770 | 770-770 |
| S0334 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 777 | 777-777 |
| S0335 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 784 | 784-784 |
| S0336 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 797 | 797-797 |
| S0337 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 803 | 803-803 |
| S0338 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 810 | 810-810 |
| S0339 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 824 | 824-824 |
| S0340 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 831 | 831-831 |
| S0341 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 838 | 838-838 |
| S0342 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 843 | 843-843 |
| S0343 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 851 | 851-851 |
| S0344 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 859 | 859-859 |
| S0345 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 867 | 867-867 |
| S0346 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 874 | 874-874 |
| S0347 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 887 | 887-887 |
| S0348 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 892 | 892-892 |
| S0349 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 899 | 899-899 |
| S0350 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 907 | 907-907 |
| S0351 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 912 | 912-912 |
| S0352 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 920 | 920-920 |
| S0353 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 940 | 940-940 |
| S0354 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 945 | 945-945 |
| S0355 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 953 | 953-953 |
| S0356 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 960 | 960-960 |
| S0357 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 965 | 965-965 |
| S0358 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 973 | 973-973 |
| S0359 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 980 | 980-980 |
| S0360 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 995 | 995-995 |
| S0361 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1006 | 1006-1006 |
| S0362 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1013 | 1013-1013 |
| S0363 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1021 | 1021-1021 |
| S0364 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1033 | 1033-1033 |
| S0365 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1045 | 1045-1045 |
| S0366 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1053 | 1053-1053 |
| S0367 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1061 | 1061-1061 |
| S0368 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1067 | 1067-1067 |
| S0369 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1075 | 1075-1075 |
| S0370 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1087 | 1087-1087 |
| S0371 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1094 | 1094-1094 |
| S0372 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1108 | 1108-1108 |
| S0373 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1115 | 1115-1115 |
| S0374 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1123 | 1123-1123 |
| S0375 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1131 | 1131-1131 |
| S0376 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1143 | 1143-1143 |
| S0377 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1149 | 1149-1149 |
| S0378 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1156 | 1156-1156 |
| S0379 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1163 | 1163-1163 |
| S0380 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1171 | 1171-1171 |
| S0381 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1185 | 1185-1185 |
| S0382 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1193 | 1193-1193 |
| S0383 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1220 | 1220-1220 |
| S0384 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1227 | 1227-1227 |
| S0385 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1233 | 1233-1233 |
| S0386 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1248 | 1248-1248 |
| S0387 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1253 | 1253-1253 |
| S0388 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1258 | 1258-1258 |
| S0389 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1264 | 1264-1264 |
| S0390 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1275 | 1275-1275 |
| S0391 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1282 | 1282-1282 |
| S0392 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1288 | 1288-1288 |
| S0393 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1296 | 1296-1296 |
| S0394 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1303 | 1303-1303 |
| S0395 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1311 | 1311-1311 |
| S0396 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1317 | 1317-1317 |
| S0397 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1324 | 1324-1324 |
| S0398 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1330 | 1330-1330 |
| S0399 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1335 | 1335-1335 |
| S0400 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1341 | 1341-1341 |
| S0401 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1348 | 1348-1348 |
| S0402 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1355 | 1355-1355 |
| S0403 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1359 | 1359-1359 |
| S0404 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1367 | 1367-1367 |
| S0405 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1373 | 1373-1373 |
| S0406 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1382 | 1382-1382 |
| S0407 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1388 | 1388-1388 |
| S0408 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1402 | 1402-1402 |
| S0409 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1416 | 1416-1416 |
| S0410 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1423 | 1423-1423 |
| S0411 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1432 | 1432-1432 |
| S0412 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1444 | 1444-1444 |
| S0413 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1450 | 1450-1450 |
| S0414 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1456 | 1456-1456 |
| S0415 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1463 | 1463-1463 |
| S0416 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1470 | 1470-1470 |
| S0417 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1477 | 1477-1477 |
| S0418 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1488 | 1488-1488 |
| S0419 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1496 | 1496-1496 |
| S0420 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1502 | 1502-1502 |
| S0421 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1510 | 1510-1510 |
| S0422 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1517 | 1517-1517 |
| S0423 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1523 | 1523-1523 |
| S0424 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1531 | 1531-1531 |
| S0425 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1537 | 1537-1537 |
| S0426 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1542 | 1542-1542 |
| S0427 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1555 | 1555-1555 |
| S0428 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1567 | 1567-1567 |
| S0429 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1579 | 1579-1579 |
| S0430 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1586 | 1586-1586 |
| S0431 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1591 | 1591-1591 |
| S0432 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1598 | 1598-1598 |
| S0433 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1603 | 1603-1603 |
| S0434 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1610 | 1610-1610 |
| S0435 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1616 | 1616-1616 |
| S0436 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1622 | 1622-1622 |
| S0437 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1627 | 1627-1627 |
| S0438 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1632 | 1632-1632 |
| S0439 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1637 | 1637-1637 |
| S0440 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1643 | 1643-1643 |
| S0441 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1655 | 1655-1655 |
| S0442 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1663 | 1663-1663 |
| S0443 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1668 | 1668-1668 |
| S0444 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1675 | 1675-1675 |
| S0445 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1683 | 1683-1683 |
| S0446 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1690 | 1690-1690 |
| S0447 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1697 | 1697-1697 |
| S0448 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1708 | 1708-1708 |
| S0449 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1714 | 1714-1714 |
| S0450 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 4 | 4-4 |
| S0451 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 4 | 4-4 |
| S0452 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 18 | 18-18 |
| S0453 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 24 | 24-24 |
| S0454 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 31 | 31-31 |
| S0455 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 37 | 37-37 |
| S0456 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 45 | 45-45 |
| S0457 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 53 | 53-53 |
| S0458 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 60 | 60-60 |
| S0459 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 68 | 68-68 |
| S0460 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 76 | 76-76 |
| S0461 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 83 | 83-83 |
| S0462 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 90 | 90-90 |
| S0463 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 98 | 98-98 |
| S0464 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 106 | 106-106 |
| S0465 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 118 | 118-118 |
| S0466 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 126 | 126-126 |
| S0467 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 133 | 133-133 |
| S0468 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 139 | 139-139 |
| S0469 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 146 | 146-146 |
| S0470 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 154 | 154-154 |
| S0471 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 165 | 165-165 |
| S0472 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 173 | 173-173 |
| S0473 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 180 | 180-180 |
| S0474 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 188 | 188-188 |
| S0475 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 194 | 194-194 |
| S0476 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 199 | 199-199 |
| S0477 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 206 | 206-206 |
| S0478 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 211 | 211-211 |
| S0479 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 217 | 217-217 |
| S0480 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 225 | 225-225 |
| S0481 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 230 | 230-230 |
| S0482 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 236 | 236-236 |
| S0483 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 244 | 244-244 |
| S0484 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 248 | 248-248 |
| S0485 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 255 | 255-255 |
| S0486 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 263 | 263-263 |
| S0487 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 271 | 271-271 |
| S0488 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 278 | 278-278 |
| S0489 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 292 | 292-292 |
| S0490 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 300 | 300-300 |
| S0491 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 307 | 307-307 |
| S0492 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 314 | 314-314 |
| S0493 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 322 | 322-322 |
| S0494 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 335 | 335-335 |
| S0495 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 341 | 341-341 |
| S0496 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 349 | 349-349 |
| S0497 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 356 | 356-356 |
| S0498 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 364 | 364-364 |
| S0499 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 371 | 371-371 |
| S0500 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 377 | 377-377 |
| S0501 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 383 | 383-383 |
| S0502 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 396 | 396-396 |
| S0503 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 403 | 403-403 |
| S0504 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 410 | 410-410 |
| S0505 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 423 | 423-423 |
| S0506 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 430 | 430-430 |
| S0507 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 442 | 442-442 |
| S0508 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 447 | 447-447 |
| S0509 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 454 | 454-454 |
| S0510 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 462 | 462-462 |
| S0511 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 467 | 467-467 |
| S0512 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 474 | 474-474 |
| S0513 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 480 | 480-480 |
| S0514 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 486 | 486-486 |
| S0515 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 498 | 498-498 |
| S0516 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 505 | 505-505 |
| S0517 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 512 | 512-512 |
| S0518 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 519 | 519-519 |
| S0519 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 524 | 524-524 |
| S0520 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 532 | 532-532 |
| S0521 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 539 | 539-539 |
| S0522 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 554 | 554-554 |
| S0523 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 559 | 559-559 |
| S0524 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 566 | 566-566 |
| S0525 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 573 | 573-573 |
| S0526 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 580 | 580-580 |
| S0527 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 587 | 587-587 |
| S0528 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 595 | 595-595 |
| S0529 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 603 | 603-603 |
| S0530 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 610 | 610-610 |
| S0531 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 629 | 629-629 |
| S0532 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 640 | 640-640 |
| S0533 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 647 | 647-647 |
| S0534 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 660 | 660-660 |
| S0535 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 668 | 668-668 |
| S0536 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 674 | 674-674 |
| S0537 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 682 | 682-682 |
| S0538 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 689 | 689-689 |
| S0539 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 710 | 710-710 |
| S0540 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 718 | 718-718 |
| S0541 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 724 | 724-724 |
| S0542 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 737 | 737-737 |
| S0543 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 744 | 744-744 |
| S0544 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 751 | 751-751 |
| S0545 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 758 | 758-758 |
| S0546 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 765 | 765-765 |
| S0547 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 771 | 771-771 |
| S0548 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 778 | 778-778 |
| S0549 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 785 | 785-785 |
| S0550 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 791 | 791-791 |
| S0551 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 798 | 798-798 |
| S0552 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 804 | 804-804 |
| S0553 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 811 | 811-811 |
| S0554 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 818 | 818-818 |
| S0555 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 825 | 825-825 |
| S0556 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 832 | 832-832 |
| S0557 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 839 | 839-839 |
| S0558 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 844 | 844-844 |
| S0559 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 852 | 852-852 |
| S0560 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 860 | 860-860 |
| S0561 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 868 | 868-868 |
| S0562 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 875 | 875-875 |
| S0563 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 881 | 881-881 |
| S0564 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 888 | 888-888 |
| S0565 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 893 | 893-893 |
| S0566 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 900 | 900-900 |
| S0567 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 913 | 913-913 |
| S0568 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 921 | 921-921 |
| S0569 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 928 | 928-928 |
| S0570 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 934 | 934-934 |
| S0571 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 946 | 946-946 |
| S0572 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 954 | 954-954 |
| S0573 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 966 | 966-966 |
| S0574 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 974 | 974-974 |
| S0575 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 981 | 981-981 |
| S0576 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 988 | 988-988 |
| S0577 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1000 | 1000-1000 |
| S0578 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1007 | 1007-1007 |
| S0579 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1014 | 1014-1014 |
| S0580 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1022 | 1022-1022 |
| S0581 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1028 | 1028-1028 |
| S0582 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1034 | 1034-1034 |
| S0583 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1040 | 1040-1040 |
| S0584 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1046 | 1046-1046 |
| S0585 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1054 | 1054-1054 |
| S0586 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1062 | 1062-1062 |
| S0587 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1068 | 1068-1068 |
| S0588 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1076 | 1076-1076 |
| S0589 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1081 | 1081-1081 |
| S0590 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1088 | 1088-1088 |
| S0591 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1095 | 1095-1095 |
| S0592 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1102 | 1102-1102 |
| S0593 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1109 | 1109-1109 |
| S0594 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1116 | 1116-1116 |
| S0595 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1124 | 1124-1124 |
| S0596 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1132 | 1132-1132 |
| S0597 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1137 | 1137-1137 |
| S0598 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1144 | 1144-1144 |
| S0599 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1150 | 1150-1150 |
| S0600 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1157 | 1157-1157 |
| S0601 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1164 | 1164-1164 |
| S0602 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1178 | 1178-1178 |
| S0603 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1186 | 1186-1186 |
| S0604 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1199 | 1199-1199 |
| S0605 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1206 | 1206-1206 |
| S0606 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1213 | 1213-1213 |
| S0607 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1221 | 1221-1221 |
| S0608 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1234 | 1234-1234 |
| S0609 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1241 | 1241-1241 |
| S0610 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1254 | 1254-1254 |
| S0611 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1265 | 1265-1265 |
| S0612 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1276 | 1276-1276 |
| S0613 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1283 | 1283-1283 |
| S0614 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1289 | 1289-1289 |
| S0615 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1297 | 1297-1297 |
| S0616 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1304 | 1304-1304 |
| S0617 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1312 | 1312-1312 |
| S0618 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1318 | 1318-1318 |
| S0619 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1325 | 1325-1325 |
| S0620 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1331 | 1331-1331 |
| S0621 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1342 | 1342-1342 |
| S0622 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1356 | 1356-1356 |
| S0623 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1360 | 1360-1360 |
| S0624 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1368 | 1368-1368 |
| S0625 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1374 | 1374-1374 |
| S0626 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1383 | 1383-1383 |
| S0627 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1395 | 1395-1395 |
| S0628 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1403 | 1403-1403 |
| S0629 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1409 | 1409-1409 |
| S0630 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1417 | 1417-1417 |
| S0631 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1433 | 1433-1433 |
| S0632 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1445 | 1445-1445 |
| S0633 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1451 | 1451-1451 |
| S0634 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1457 | 1457-1457 |
| S0635 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1464 | 1464-1464 |
| S0636 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1471 | 1471-1471 |
| S0637 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1478 | 1478-1478 |
| S0638 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1482 | 1482-1482 |
| S0639 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1489 | 1489-1489 |
| S0640 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1497 | 1497-1497 |
| S0641 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1503 | 1503-1503 |
| S0642 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1511 | 1511-1511 |
| S0643 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1518 | 1518-1518 |
| S0644 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1524 | 1524-1524 |
| S0645 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1532 | 1532-1532 |
| S0646 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1549 | 1549-1549 |
| S0647 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1556 | 1556-1556 |
| S0648 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1562 | 1562-1562 |
| S0649 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1568 | 1568-1568 |
| S0650 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1574 | 1574-1574 |
| S0651 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1580 | 1580-1580 |
| S0652 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1587 | 1587-1587 |
| S0653 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1592 | 1592-1592 |
| S0654 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1599 | 1599-1599 |
| S0655 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1604 | 1604-1604 |
| S0656 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1611 | 1611-1611 |
| S0657 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1617 | 1617-1617 |
| S0658 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1628 | 1628-1628 |
| S0659 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1633 | 1633-1633 |
| S0660 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1644 | 1644-1644 |
| S0661 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1650 | 1650-1650 |
| S0662 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1656 | 1656-1656 |
| S0663 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1669 | 1669-1669 |
| S0664 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1676 | 1676-1676 |
| S0665 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1684 | 1684-1684 |
| S0666 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1691 | 1691-1691 |
| S0667 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1703 | 1703-1703 |
| S0668 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1715 | 1715-1715 |
| S0669 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1722 | 1722-1722 |
| S0670 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 5 | 5-5 |
| S0671 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 5 | 5-5 |
| S0672 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 12 | 12-12 |
| S0673 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 19 | 19-19 |
| S0674 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 25 | 25-25 |
| S0675 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 38 | 38-38 |
| S0676 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 46 | 46-46 |
| S0677 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 54 | 54-54 |
| S0678 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 61 | 61-61 |
| S0679 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 69 | 69-69 |
| S0680 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 77 | 77-77 |
| S0681 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 84 | 84-84 |
| S0682 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 91 | 91-91 |
| S0683 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 99 | 99-99 |
| S0684 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 107 | 107-107 |
| S0685 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 113 | 113-113 |
| S0686 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 119 | 119-119 |
| S0687 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 127 | 127-127 |
| S0688 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 134 | 134-134 |
| S0689 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 140 | 140-140 |
| S0690 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 147 | 147-147 |
| S0691 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 155 | 155-155 |
| S0692 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 159 | 159-159 |
| S0693 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 166 | 166-166 |
| S0694 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 174 | 174-174 |
| S0695 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 181 | 181-181 |
| S0696 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 189 | 189-189 |
| S0697 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 195 | 195-195 |
| S0698 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 200 | 200-200 |
| S0699 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 207 | 207-207 |
| S0700 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 212 | 212-212 |
| S0701 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 218 | 218-218 |
| S0702 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 226 | 226-226 |
| S0703 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 231 | 231-231 |
| S0704 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 237 | 237-237 |
| S0705 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 249 | 249-249 |
| S0706 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 256 | 256-256 |
| S0707 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 264 | 264-264 |
| S0708 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 279 | 279-279 |
| S0709 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 286 | 286-286 |
| S0710 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 293 | 293-293 |
| S0711 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 301 | 301-301 |
| S0712 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 315 | 315-315 |
| S0713 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 323 | 323-323 |
| S0714 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 330 | 330-330 |
| S0715 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 336 | 336-336 |
| S0716 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 342 | 342-342 |
| S0717 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 350 | 350-350 |
| S0718 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 357 | 357-357 |
| S0719 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 365 | 365-365 |
| S0720 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 378 | 378-378 |
| S0721 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 384 | 384-384 |
| S0722 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 391 | 391-391 |
| S0723 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 397 | 397-397 |
| S0724 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 404 | 404-404 |
| S0725 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 411 | 411-411 |
| S0726 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 417 | 417-417 |
| S0727 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 424 | 424-424 |
| S0728 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 431 | 431-431 |
| S0729 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 437 | 437-437 |
| S0730 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 448 | 448-448 |
| S0731 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 455 | 455-455 |
| S0732 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 463 | 463-463 |
| S0733 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 468 | 468-468 |
| S0734 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 475 | 475-475 |
| S0735 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 481 | 481-481 |
| S0736 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 487 | 487-487 |
| S0737 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 492 | 492-492 |
| S0738 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 499 | 499-499 |
| S0739 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 506 | 506-506 |
| S0740 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 513 | 513-513 |
| S0741 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 525 | 525-525 |
| S0742 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 540 | 540-540 |
| S0743 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 547 | 547-547 |
| S0744 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 555 | 555-555 |
| S0745 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 567 | 567-567 |
| S0746 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 574 | 574-574 |
| S0747 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 581 | 581-581 |
| S0748 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 588 | 588-588 |
| S0749 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 596 | 596-596 |
| S0750 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 604 | 604-604 |
| S0751 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 611 | 611-611 |
| S0752 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 618 | 618-618 |
| S0753 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 630 | 630-630 |
| S0754 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 641 | 641-641 |
| S0755 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 648 | 648-648 |
| S0756 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 653 | 653-653 |
| S0757 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 661 | 661-661 |
| S0758 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 669 | 669-669 |
| S0759 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 675 | 675-675 |
| S0760 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 690 | 690-690 |
| S0761 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 696 | 696-696 |
| S0762 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 703 | 703-703 |
| S0763 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 711 | 711-711 |
| S0764 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 731 | 731-731 |
| S0765 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 738 | 738-738 |
| S0766 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 752 | 752-752 |
| S0767 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 759 | 759-759 |
| S0768 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 766 | 766-766 |
| S0769 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 772 | 772-772 |
| S0770 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 779 | 779-779 |
| S0771 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 786 | 786-786 |
| S0772 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 792 | 792-792 |
| S0773 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 799 | 799-799 |
| S0774 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 805 | 805-805 |
| S0775 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 812 | 812-812 |
| S0776 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 819 | 819-819 |
| S0777 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 833 | 833-833 |
| S0778 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 840 | 840-840 |
| S0779 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 845 | 845-845 |
| S0780 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 853 | 853-853 |
| S0781 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 861 | 861-861 |
| S0782 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 869 | 869-869 |
| S0783 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 876 | 876-876 |
| S0784 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 894 | 894-894 |
| S0785 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 901 | 901-901 |
| S0786 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 914 | 914-914 |
| S0787 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 922 | 922-922 |
| S0788 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 935 | 935-935 |
| S0789 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 941 | 941-941 |
| S0790 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 947 | 947-947 |
| S0791 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 955 | 955-955 |
| S0792 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 967 | 967-967 |
| S0793 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 975 | 975-975 |
| S0794 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 982 | 982-982 |
| S0795 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 989 | 989-989 |
| S0796 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 996 | 996-996 |
| S0797 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1001 | 1001-1001 |
| S0798 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1008 | 1008-1008 |
| S0799 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1015 | 1015-1015 |
| S0800 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1035 | 1035-1035 |
| S0801 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1041 | 1041-1041 |
| S0802 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1047 | 1047-1047 |
| S0803 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1055 | 1055-1055 |
| S0804 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1063 | 1063-1063 |
| S0805 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1069 | 1069-1069 |
| S0806 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1082 | 1082-1082 |
| S0807 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1089 | 1089-1089 |
| S0808 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1096 | 1096-1096 |
| S0809 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1110 | 1110-1110 |
| S0810 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1117 | 1117-1117 |
| S0811 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1125 | 1125-1125 |
| S0812 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1133 | 1133-1133 |
| S0813 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1138 | 1138-1138 |
| S0814 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1145 | 1145-1145 |
| S0815 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1151 | 1151-1151 |
| S0816 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1158 | 1158-1158 |
| S0817 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1165 | 1165-1165 |
| S0818 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1172 | 1172-1172 |
| S0819 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1179 | 1179-1179 |
| S0820 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1187 | 1187-1187 |
| S0821 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1194 | 1194-1194 |
| S0822 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1200 | 1200-1200 |
| S0823 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1207 | 1207-1207 |
| S0824 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1214 | 1214-1214 |
| S0825 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1222 | 1222-1222 |
| S0826 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1228 | 1228-1228 |
| S0827 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1235 | 1235-1235 |
| S0828 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1242 | 1242-1242 |
| S0829 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1249 | 1249-1249 |
| S0830 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1266 | 1266-1266 |
| S0831 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1269 | 1269-1269 |
| S0832 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1277 | 1277-1277 |
| S0833 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1290 | 1290-1290 |
| S0834 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1298 | 1298-1298 |
| S0835 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1305 | 1305-1305 |
| S0836 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1319 | 1319-1319 |
| S0837 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1336 | 1336-1336 |
| S0838 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1343 | 1343-1343 |
| S0839 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1349 | 1349-1349 |
| S0840 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1357 | 1357-1357 |
| S0841 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1361 | 1361-1361 |
| S0842 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1369 | 1369-1369 |
| S0843 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1375 | 1375-1375 |
| S0844 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1384 | 1384-1384 |
| S0845 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1389 | 1389-1389 |
| S0846 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1396 | 1396-1396 |
| S0847 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1404 | 1404-1404 |
| S0848 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1410 | 1410-1410 |
| S0849 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1428 | 1428-1428 |
| S0850 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1434 | 1434-1434 |
| S0851 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1440 | 1440-1440 |
| S0852 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1446 | 1446-1446 |
| S0853 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1452 | 1452-1452 |
| S0854 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1458 | 1458-1458 |
| S0855 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1465 | 1465-1465 |
| S0856 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1472 | 1472-1472 |
| S0857 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1479 | 1479-1479 |
| S0858 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1483 | 1483-1483 |
| S0859 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1490 | 1490-1490 |
| S0860 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1504 | 1504-1504 |
| S0861 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1512 | 1512-1512 |
| S0862 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1519 | 1519-1519 |
| S0863 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1525 | 1525-1525 |
| S0864 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1533 | 1533-1533 |
| S0865 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1543 | 1543-1543 |
| S0866 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1550 | 1550-1550 |
| S0867 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1557 | 1557-1557 |
| S0868 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1563 | 1563-1563 |
| S0869 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1569 | 1569-1569 |
| S0870 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1575 | 1575-1575 |
| S0871 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1581 | 1581-1581 |
| S0872 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1588 | 1588-1588 |
| S0873 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1593 | 1593-1593 |
| S0874 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1600 | 1600-1600 |
| S0875 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1605 | 1605-1605 |
| S0876 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1638 | 1638-1638 |
| S0877 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1645 | 1645-1645 |
| S0878 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1657 | 1657-1657 |
| S0879 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1670 | 1670-1670 |
| S0880 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1677 | 1677-1677 |
| S0881 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1685 | 1685-1685 |
| S0882 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1692 | 1692-1692 |
| S0883 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1704 | 1704-1704 |
| S0884 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1709 | 1709-1709 |
| S0885 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1716 | 1716-1716 |
| S0886 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1723 | 1723-1723 |
| S0887 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 6 | 6-6 |
| S0888 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 6 | 6-6 |
| S0889 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 13 | 13-13 |
| S0890 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 32 | 32-32 |
| S0891 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 39 | 39-39 |
| S0892 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 47 | 47-47 |
| S0893 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 55 | 55-55 |
| S0894 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 62 | 62-62 |
| S0895 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 70 | 70-70 |
| S0896 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 78 | 78-78 |
| S0897 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 85 | 85-85 |
| S0898 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 92 | 92-92 |
| S0899 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 100 | 100-100 |
| S0900 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 108 | 108-108 |
| S0901 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 114 | 114-114 |
| S0902 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 120 | 120-120 |
| S0903 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 128 | 128-128 |
| S0904 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 141 | 141-141 |
| S0905 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 148 | 148-148 |
| S0906 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 156 | 156-156 |
| S0907 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 160 | 160-160 |
| S0908 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 167 | 167-167 |
| S0909 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 175 | 175-175 |
| S0910 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 182 | 182-182 |
| S0911 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 196 | 196-196 |
| S0912 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 201 | 201-201 |
| S0913 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 219 | 219-219 |
| S0914 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 238 | 238-238 |
| S0915 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 245 | 245-245 |
| S0916 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 250 | 250-250 |
| S0917 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 257 | 257-257 |
| S0918 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 265 | 265-265 |
| S0919 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 272 | 272-272 |
| S0920 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 280 | 280-280 |
| S0921 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 287 | 287-287 |
| S0922 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 294 | 294-294 |
| S0923 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 302 | 302-302 |
| S0924 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 308 | 308-308 |
| S0925 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 316 | 316-316 |
| S0926 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 324 | 324-324 |
| S0927 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 331 | 331-331 |
| S0928 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 337 | 337-337 |
| S0929 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 343 | 343-343 |
| S0930 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 351 | 351-351 |
| S0931 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 358 | 358-358 |
| S0932 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 366 | 366-366 |
| S0933 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 372 | 372-372 |
| S0934 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 379 | 379-379 |
| S0935 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 385 | 385-385 |
| S0936 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 392 | 392-392 |
| S0937 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 412 | 412-412 |
| S0938 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 418 | 418-418 |
| S0939 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 425 | 425-425 |
| S0940 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 432 | 432-432 |
| S0941 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 438 | 438-438 |
| S0942 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 443 | 443-443 |
| S0943 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 449 | 449-449 |
| S0944 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 456 | 456-456 |
| S0945 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 464 | 464-464 |
| S0946 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 469 | 469-469 |
| S0947 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 488 | 488-488 |
| S0948 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 493 | 493-493 |
| S0949 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 500 | 500-500 |
| S0950 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 507 | 507-507 |
| S0951 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 514 | 514-514 |
| S0952 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 526 | 526-526 |
| S0953 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 533 | 533-533 |
| S0954 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 541 | 541-541 |
| S0955 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 548 | 548-548 |
| S0956 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 560 | 560-560 |
| S0957 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 568 | 568-568 |
| S0958 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 575 | 575-575 |
| S0959 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 589 | 589-589 |
| S0960 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 597 | 597-597 |
| S0961 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 612 | 612-612 |
| S0962 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 619 | 619-619 |
| S0963 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 635 | 635-635 |
| S0964 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 654 | 654-654 |
| S0965 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 662 | 662-662 |
| S0966 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 676 | 676-676 |
| S0967 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 683 | 683-683 |
| S0968 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 691 | 691-691 |
| S0969 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 697 | 697-697 |
| S0970 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 704 | 704-704 |
| S0971 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 712 | 712-712 |
| S0972 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 725 | 725-725 |
| S0973 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 732 | 732-732 |
| S0974 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 739 | 739-739 |
| S0975 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 745 | 745-745 |
| S0976 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 753 | 753-753 |
| S0977 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 760 | 760-760 |
| S0978 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 780 | 780-780 |
| S0979 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 787 | 787-787 |
| S0980 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 793 | 793-793 |
| S0981 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 806 | 806-806 |
| S0982 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 813 | 813-813 |
| S0983 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 820 | 820-820 |
| S0984 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 826 | 826-826 |
| S0985 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 846 | 846-846 |
| S0986 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 854 | 854-854 |
| S0987 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 862 | 862-862 |
| S0988 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 870 | 870-870 |
| S0989 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 877 | 877-877 |
| S0990 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 882 | 882-882 |
| S0991 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 895 | 895-895 |
| S0992 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 902 | 902-902 |
| S0993 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 915 | 915-915 |
| S0994 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 923 | 923-923 |
| S0995 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 929 | 929-929 |
| S0996 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 936 | 936-936 |
| S0997 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 942 | 942-942 |
| S0998 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 948 | 948-948 |
| S0999 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 956 | 956-956 |
| S1000 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 961 | 961-961 |
| S1001 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 968 | 968-968 |
| S1002 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 976 | 976-976 |
| S1003 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 983 | 983-983 |
| S1004 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 990 | 990-990 |
| S1005 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 997 | 997-997 |
| S1006 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1002 | 1002-1002 |
| S1007 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1009 | 1009-1009 |
| S1008 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1016 | 1016-1016 |
| S1009 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1023 | 1023-1023 |
| S1010 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1029 | 1029-1029 |
| S1011 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1036 | 1036-1036 |
| S1012 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1042 | 1042-1042 |
| S1013 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1048 | 1048-1048 |
| S1014 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1056 | 1056-1056 |
| S1015 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1070 | 1070-1070 |
| S1016 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1077 | 1077-1077 |
| S1017 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1083 | 1083-1083 |
| S1018 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1090 | 1090-1090 |
| S1019 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1097 | 1097-1097 |
| S1020 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1103 | 1103-1103 |
| S1021 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1111 | 1111-1111 |
| S1022 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1118 | 1118-1118 |
| S1023 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1126 | 1126-1126 |
| S1024 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1134 | 1134-1134 |
| S1025 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1146 | 1146-1146 |
| S1026 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1152 | 1152-1152 |
| S1027 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1159 | 1159-1159 |
| S1028 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1166 | 1166-1166 |
| S1029 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1173 | 1173-1173 |
| S1030 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1180 | 1180-1180 |
| S1031 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1188 | 1188-1188 |
| S1032 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1201 | 1201-1201 |
| S1033 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1208 | 1208-1208 |
| S1034 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1215 | 1215-1215 |
| S1035 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1229 | 1229-1229 |
| S1036 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1236 | 1236-1236 |
| S1037 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1243 | 1243-1243 |
| S1038 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1259 | 1259-1259 |
| S1039 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1267 | 1267-1267 |
| S1040 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1270 | 1270-1270 |
| S1041 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1278 | 1278-1278 |
| S1042 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1284 | 1284-1284 |
| S1043 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1291 | 1291-1291 |
| S1044 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1299 | 1299-1299 |
| S1045 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1306 | 1306-1306 |
| S1046 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1313 | 1313-1313 |
| S1047 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1320 | 1320-1320 |
| S1048 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1326 | 1326-1326 |
| S1049 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1332 | 1332-1332 |
| S1050 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1344 | 1344-1344 |
| S1051 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1350 | 1350-1350 |
| S1052 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1362 | 1362-1362 |
| S1053 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1376 | 1376-1376 |
| S1054 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1385 | 1385-1385 |
| S1055 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1390 | 1390-1390 |
| S1056 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1397 | 1397-1397 |
| S1057 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1405 | 1405-1405 |
| S1058 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1411 | 1411-1411 |
| S1059 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1418 | 1418-1418 |
| S1060 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1424 | 1424-1424 |
| S1061 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1435 | 1435-1435 |
| S1062 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1441 | 1441-1441 |
| S1063 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1466 | 1466-1466 |
| S1064 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1473 | 1473-1473 |
| S1065 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1484 | 1484-1484 |
| S1066 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1491 | 1491-1491 |
| S1067 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1498 | 1498-1498 |
| S1068 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1505 | 1505-1505 |
| S1069 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1513 | 1513-1513 |
| S1070 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1520 | 1520-1520 |
| S1071 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1526 | 1526-1526 |
| S1072 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1534 | 1534-1534 |
| S1073 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1538 | 1538-1538 |
| S1074 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1544 | 1544-1544 |
| S1075 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1551 | 1551-1551 |
| S1076 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1558 | 1558-1558 |
| S1077 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1564 | 1564-1564 |
| S1078 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1570 | 1570-1570 |
| S1079 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1589 | 1589-1589 |
| S1080 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1594 | 1594-1594 |
| S1081 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1606 | 1606-1606 |
| S1082 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1612 | 1612-1612 |
| S1083 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1618 | 1618-1618 |
| S1084 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1623 | 1623-1623 |
| S1085 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1629 | 1629-1629 |
| S1086 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1634 | 1634-1634 |
| S1087 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1639 | 1639-1639 |
| S1088 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1646 | 1646-1646 |
| S1089 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1651 | 1651-1651 |
| S1090 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1658 | 1658-1658 |
| S1091 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1664 | 1664-1664 |
| S1092 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1671 | 1671-1671 |
| S1093 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1678 | 1678-1678 |
| S1094 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1693 | 1693-1693 |
| S1095 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1698 | 1698-1698 |
| S1096 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1705 | 1705-1705 |
| S1097 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1710 | 1710-1710 |
| S1098 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1717 | 1717-1717 |
| S1099 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1724 | 1724-1724 |
| S1100 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 7 | 7-7 |
| S1101 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 7 | 7-7 |
| S1102 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 14 | 14-14 |
| S1103 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 20 | 20-20 |
| S1104 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 26 | 26-26 |
| S1105 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 33 | 33-33 |
| S1106 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 40 | 40-40 |
| S1107 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 48 | 48-48 |
| S1108 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 56 | 56-56 |
| S1109 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 63 | 63-63 |
| S1110 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 71 | 71-71 |
| S1111 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 79 | 79-79 |
| S1112 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 86 | 86-86 |
| S1113 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 93 | 93-93 |
| S1114 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 101 | 101-101 |
| S1115 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 121 | 121-121 |
| S1116 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 135 | 135-135 |
| S1117 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 142 | 142-142 |
| S1118 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 149 | 149-149 |
| S1119 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 168 | 168-168 |
| S1120 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 176 | 176-176 |
| S1121 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 183 | 183-183 |
| S1122 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 213 | 213-213 |
| S1123 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 220 | 220-220 |
| S1124 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 227 | 227-227 |
| S1125 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 232 | 232-232 |
| S1126 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 239 | 239-239 |
| S1127 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 251 | 251-251 |
| S1128 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 258 | 258-258 |
| S1129 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 266 | 266-266 |
| S1130 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 273 | 273-273 |
| S1131 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 281 | 281-281 |
| S1132 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 288 | 288-288 |
| S1133 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 295 | 295-295 |
| S1134 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 309 | 309-309 |
| S1135 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 317 | 317-317 |
| S1136 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 325 | 325-325 |
| S1137 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 332 | 332-332 |
| S1138 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 344 | 344-344 |
| S1139 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 352 | 352-352 |
| S1140 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 359 | 359-359 |
| S1141 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 367 | 367-367 |
| S1142 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 373 | 373-373 |
| S1143 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 386 | 386-386 |
| S1144 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 393 | 393-393 |
| S1145 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 398 | 398-398 |
| S1146 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 405 | 405-405 |
| S1147 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 413 | 413-413 |
| S1148 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 426 | 426-426 |
| S1149 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 433 | 433-433 |
| S1150 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 439 | 439-439 |
| S1151 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 450 | 450-450 |
| S1152 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 457 | 457-457 |
| S1153 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 465 | 465-465 |
| S1154 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 470 | 470-470 |
| S1155 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 476 | 476-476 |
| S1156 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 482 | 482-482 |
| S1157 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 489 | 489-489 |
| S1158 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 494 | 494-494 |
| S1159 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 501 | 501-501 |
| S1160 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 515 | 515-515 |
| S1161 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 520 | 520-520 |
| S1162 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 527 | 527-527 |
| S1163 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 534 | 534-534 |
| S1164 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 542 | 542-542 |
| S1165 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 549 | 549-549 |
| S1166 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 556 | 556-556 |
| S1167 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 561 | 561-561 |
| S1168 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 569 | 569-569 |
| S1169 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 576 | 576-576 |
| S1170 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 582 | 582-582 |
| S1171 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 590 | 590-590 |
| S1172 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 598 | 598-598 |
| S1173 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 605 | 605-605 |
| S1174 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 613 | 613-613 |
| S1175 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 620 | 620-620 |
| S1176 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 631 | 631-631 |
| S1177 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 636 | 636-636 |
| S1178 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 642 | 642-642 |
| S1179 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 655 | 655-655 |
| S1180 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 663 | 663-663 |
| S1181 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 670 | 670-670 |
| S1182 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 677 | 677-677 |
| S1183 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 684 | 684-684 |
| S1184 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 692 | 692-692 |
| S1185 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 698 | 698-698 |
| S1186 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 705 | 705-705 |
| S1187 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 713 | 713-713 |
| S1188 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 719 | 719-719 |
| S1189 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 726 | 726-726 |
| S1190 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 733 | 733-733 |
| S1191 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 740 | 740-740 |
| S1192 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 746 | 746-746 |
| S1193 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 754 | 754-754 |
| S1194 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 767 | 767-767 |
| S1195 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 773 | 773-773 |
| S1196 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 781 | 781-781 |
| S1197 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 788 | 788-788 |
| S1198 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 794 | 794-794 |
| S1199 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 807 | 807-807 |
| S1200 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 814 | 814-814 |
| S1201 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 827 | 827-827 |
| S1202 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 834 | 834-834 |
| S1203 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 841 | 841-841 |
| S1204 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 847 | 847-847 |
| S1205 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 855 | 855-855 |
| S1206 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 863 | 863-863 |
| S1207 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 871 | 871-871 |
| S1208 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 878 | 878-878 |
| S1209 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 883 | 883-883 |
| S1210 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 889 | 889-889 |
| S1211 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 896 | 896-896 |
| S1212 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 903 | 903-903 |
| S1213 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 908 | 908-908 |
| S1214 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 916 | 916-916 |
| S1215 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 924 | 924-924 |
| S1216 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 930 | 930-930 |
| S1217 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 937 | 937-937 |
| S1218 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 949 | 949-949 |
| S1219 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 962 | 962-962 |
| S1220 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 969 | 969-969 |
| S1221 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 977 | 977-977 |
| S1222 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 984 | 984-984 |
| S1223 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 991 | 991-991 |
| S1224 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 998 | 998-998 |
| S1225 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1003 | 1003-1003 |
| S1226 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1017 | 1017-1017 |
| S1227 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1024 | 1024-1024 |
| S1228 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1030 | 1030-1030 |
| S1229 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1037 | 1037-1037 |
| S1230 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1043 | 1043-1043 |
| S1231 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1049 | 1049-1049 |
| S1232 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1057 | 1057-1057 |
| S1233 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1071 | 1071-1071 |
| S1234 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1078 | 1078-1078 |
| S1235 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1091 | 1091-1091 |
| S1236 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1098 | 1098-1098 |
| S1237 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1104 | 1104-1104 |
| S1238 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1112 | 1112-1112 |
| S1239 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1119 | 1119-1119 |
| S1240 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1127 | 1127-1127 |
| S1241 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1135 | 1135-1135 |
| S1242 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1139 | 1139-1139 |
| S1243 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1160 | 1160-1160 |
| S1244 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1167 | 1167-1167 |
| S1245 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1174 | 1174-1174 |
| S1246 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1181 | 1181-1181 |
| S1247 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1189 | 1189-1189 |
| S1248 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1195 | 1195-1195 |
| S1249 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1202 | 1202-1202 |
| S1250 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1209 | 1209-1209 |
| S1251 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1216 | 1216-1216 |
| S1252 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1223 | 1223-1223 |
| S1253 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1230 | 1230-1230 |
| S1254 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1237 | 1237-1237 |
| S1255 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1244 | 1244-1244 |
| S1256 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1250 | 1250-1250 |
| S1257 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1260 | 1260-1260 |
| S1258 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1268 | 1268-1268 |
| S1259 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1271 | 1271-1271 |
| S1260 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1279 | 1279-1279 |
| S1261 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1285 | 1285-1285 |
| S1262 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1292 | 1292-1292 |
| S1263 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1300 | 1300-1300 |
| S1264 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1307 | 1307-1307 |
| S1265 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1314 | 1314-1314 |
| S1266 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1321 | 1321-1321 |
| S1267 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1327 | 1327-1327 |
| S1268 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1337 | 1337-1337 |
| S1269 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1345 | 1345-1345 |
| S1270 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1351 | 1351-1351 |
| S1271 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1363 | 1363-1363 |
| S1272 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1377 | 1377-1377 |
| S1273 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1391 | 1391-1391 |
| S1274 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1398 | 1398-1398 |
| S1275 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1412 | 1412-1412 |
| S1276 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1419 | 1419-1419 |
| S1277 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1425 | 1425-1425 |
| S1278 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1429 | 1429-1429 |
| S1279 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1436 | 1436-1436 |
| S1280 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1442 | 1442-1442 |
| S1281 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1447 | 1447-1447 |
| S1282 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1453 | 1453-1453 |
| S1283 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1459 | 1459-1459 |
| S1284 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1467 | 1467-1467 |
| S1285 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1474 | 1474-1474 |
| S1286 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1485 | 1485-1485 |
| S1287 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1492 | 1492-1492 |
| S1288 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1499 | 1499-1499 |
| S1289 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1506 | 1506-1506 |
| S1290 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1514 | 1514-1514 |
| S1291 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1527 | 1527-1527 |
| S1292 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1539 | 1539-1539 |
| S1293 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1545 | 1545-1545 |
| S1294 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1559 | 1559-1559 |
| S1295 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1565 | 1565-1565 |
| S1296 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1571 | 1571-1571 |
| S1297 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1576 | 1576-1576 |
| S1298 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1582 | 1582-1582 |
| S1299 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1601 | 1601-1601 |
| S1300 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1607 | 1607-1607 |
| S1301 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1613 | 1613-1613 |
| S1302 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1619 | 1619-1619 |
| S1303 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1624 | 1624-1624 |
| S1304 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1630 | 1630-1630 |
| S1305 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1635 | 1635-1635 |
| S1306 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1647 | 1647-1647 |
| S1307 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1659 | 1659-1659 |
| S1308 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1672 | 1672-1672 |
| S1309 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1679 | 1679-1679 |
| S1310 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1686 | 1686-1686 |
| S1311 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1694 | 1694-1694 |
| S1312 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1699 | 1699-1699 |
| S1313 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1711 | 1711-1711 |
| S1314 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1718 | 1718-1718 |
| S1315 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1725 | 1725-1725 |
| S1316 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 8 | 8-8 |
| S1317 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 8 | 8-8 |
| S1318 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 15 | 15-15 |
| S1319 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 21 | 21-21 |
| S1320 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 27 | 27-27 |
| S1321 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 34 | 34-34 |
| S1322 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 41 | 41-41 |
| S1323 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 49 | 49-49 |
| S1324 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 57 | 57-57 |
| S1325 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 64 | 64-64 |
| S1326 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 72 | 72-72 |
| S1327 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 80 | 80-80 |
| S1328 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 87 | 87-87 |
| S1329 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 94 | 94-94 |
| S1330 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 102 | 102-102 |
| S1331 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 109 | 109-109 |
| S1332 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 122 | 122-122 |
| S1333 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 129 | 129-129 |
| S1334 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 136 | 136-136 |
| S1335 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 150 | 150-150 |
| S1336 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 157 | 157-157 |
| S1337 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 161 | 161-161 |
| S1338 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 169 | 169-169 |
| S1339 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 184 | 184-184 |
| S1340 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 190 | 190-190 |
| S1341 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 202 | 202-202 |
| S1342 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 208 | 208-208 |
| S1343 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 214 | 214-214 |
| S1344 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 221 | 221-221 |
| S1345 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 240 | 240-240 |
| S1346 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 246 | 246-246 |
| S1347 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 259 | 259-259 |
| S1348 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 267 | 267-267 |
| S1349 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 274 | 274-274 |
| S1350 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 282 | 282-282 |
| S1351 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 289 | 289-289 |
| S1352 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 296 | 296-296 |
| S1353 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 303 | 303-303 |
| S1354 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 310 | 310-310 |
| S1355 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 318 | 318-318 |
| S1356 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 326 | 326-326 |
| S1357 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 338 | 338-338 |
| S1358 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 345 | 345-345 |
| S1359 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 360 | 360-360 |
| S1360 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 368 | 368-368 |
| S1361 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 380 | 380-380 |
| S1362 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 387 | 387-387 |
| S1363 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 399 | 399-399 |
| S1364 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 406 | 406-406 |
| S1365 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 414 | 414-414 |
| S1366 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 419 | 419-419 |
| S1367 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 427 | 427-427 |
| S1368 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 434 | 434-434 |
| S1369 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 440 | 440-440 |
| S1370 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 444 | 444-444 |
| S1371 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 458 | 458-458 |
| S1372 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 471 | 471-471 |
| S1373 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 477 | 477-477 |
| S1374 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 502 | 502-502 |
| S1375 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 508 | 508-508 |
| S1376 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 516 | 516-516 |
| S1377 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 521 | 521-521 |
| S1378 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 528 | 528-528 |
| S1379 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 535 | 535-535 |
| S1380 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 543 | 543-543 |
| S1381 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 550 | 550-550 |
| S1382 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 562 | 562-562 |
| S1383 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 570 | 570-570 |
| S1384 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 583 | 583-583 |
| S1385 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 591 | 591-591 |
| S1386 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 599 | 599-599 |
| S1387 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 606 | 606-606 |
| S1388 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 614 | 614-614 |
| S1389 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 621 | 621-621 |
| S1390 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 625 | 625-625 |
| S1391 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 632 | 632-632 |
| S1392 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 643 | 643-643 |
| S1393 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 649 | 649-649 |
| S1394 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 656 | 656-656 |
| S1395 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 664 | 664-664 |
| S1396 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 671 | 671-671 |
| S1397 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 678 | 678-678 |
| S1398 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 685 | 685-685 |
| S1399 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 693 | 693-693 |
| S1400 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 699 | 699-699 |
| S1401 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 706 | 706-706 |
| S1402 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 714 | 714-714 |
| S1403 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 720 | 720-720 |
| S1404 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 727 | 727-727 |
| S1405 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 747 | 747-747 |
| S1406 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 755 | 755-755 |
| S1407 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 761 | 761-761 |
| S1408 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 768 | 768-768 |
| S1409 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 774 | 774-774 |
| S1410 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 795 | 795-795 |
| S1411 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 800 | 800-800 |
| S1412 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 808 | 808-808 |
| S1413 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 815 | 815-815 |
| S1414 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 821 | 821-821 |
| S1415 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 828 | 828-828 |
| S1416 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 835 | 835-835 |
| S1417 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 848 | 848-848 |
| S1418 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 856 | 856-856 |
| S1419 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 864 | 864-864 |
| S1420 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 872 | 872-872 |
| S1421 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 879 | 879-879 |
| S1422 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 884 | 884-884 |
| S1423 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 890 | 890-890 |
| S1424 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 897 | 897-897 |
| S1425 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 904 | 904-904 |
| S1426 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 909 | 909-909 |
| S1427 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 917 | 917-917 |
| S1428 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 925 | 925-925 |
| S1429 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 931 | 931-931 |
| S1430 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 950 | 950-950 |
| S1431 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 957 | 957-957 |
| S1432 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 963 | 963-963 |
| S1433 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 970 | 970-970 |
| S1434 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 985 | 985-985 |
| S1435 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 992 | 992-992 |
| S1436 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 999 | 999-999 |
| S1437 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1010 | 1010-1010 |
| S1438 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1018 | 1018-1018 |
| S1439 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1025 | 1025-1025 |
| S1440 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1038 | 1038-1038 |
| S1441 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1044 | 1044-1044 |
| S1442 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1050 | 1050-1050 |
| S1443 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1058 | 1058-1058 |
| S1444 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1064 | 1064-1064 |
| S1445 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1072 | 1072-1072 |
| S1446 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1079 | 1079-1079 |
| S1447 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1084 | 1084-1084 |
| S1448 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1092 | 1092-1092 |
| S1449 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1099 | 1099-1099 |
| S1450 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1105 | 1105-1105 |
| S1451 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1120 | 1120-1120 |
| S1452 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1128 | 1128-1128 |
| S1453 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1140 | 1140-1140 |
| S1454 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1147 | 1147-1147 |
| S1455 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1153 | 1153-1153 |
| S1456 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1168 | 1168-1168 |
| S1457 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1175 | 1175-1175 |
| S1458 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1182 | 1182-1182 |
| S1459 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1190 | 1190-1190 |
| S1460 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1196 | 1196-1196 |
| S1461 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1203 | 1203-1203 |
| S1462 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1210 | 1210-1210 |
| S1463 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1217 | 1217-1217 |
| S1464 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1224 | 1224-1224 |
| S1465 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1231 | 1231-1231 |
| S1466 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1238 | 1238-1238 |
| S1467 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1245 | 1245-1245 |
| S1468 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1251 | 1251-1251 |
| S1469 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1255 | 1255-1255 |
| S1470 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1261 | 1261-1261 |
| S1471 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1272 | 1272-1272 |
| S1472 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1280 | 1280-1280 |
| S1473 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1286 | 1286-1286 |
| S1474 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1293 | 1293-1293 |
| S1475 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1301 | 1301-1301 |
| S1476 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1308 | 1308-1308 |
| S1477 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1328 | 1328-1328 |
| S1478 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1333 | 1333-1333 |
| S1479 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1338 | 1338-1338 |
| S1480 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1346 | 1346-1346 |
| S1481 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1352 | 1352-1352 |
| S1482 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1364 | 1364-1364 |
| S1483 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1370 | 1370-1370 |
| S1484 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1378 | 1378-1378 |
| S1485 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1386 | 1386-1386 |
| S1486 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1392 | 1392-1392 |
| S1487 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1399 | 1399-1399 |
| S1488 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1406 | 1406-1406 |
| S1489 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1413 | 1413-1413 |
| S1490 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1420 | 1420-1420 |
| S1491 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1426 | 1426-1426 |
| S1492 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1430 | 1430-1430 |
| S1493 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1437 | 1437-1437 |
| S1494 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1448 | 1448-1448 |
| S1495 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1460 | 1460-1460 |
| S1496 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1468 | 1468-1468 |
| S1497 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1475 | 1475-1475 |
| S1498 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1480 | 1480-1480 |
| S1499 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1486 | 1486-1486 |
| S1500 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1493 | 1493-1493 |
| S1501 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1500 | 1500-1500 |
| S1502 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1507 | 1507-1507 |
| S1503 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1521 | 1521-1521 |
| S1504 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1528 | 1528-1528 |
| S1505 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1546 | 1546-1546 |
| S1506 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1552 | 1552-1552 |
| S1507 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1560 | 1560-1560 |
| S1508 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1566 | 1566-1566 |
| S1509 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1577 | 1577-1577 |
| S1510 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1583 | 1583-1583 |
| S1511 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1595 | 1595-1595 |
| S1512 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1614 | 1614-1614 |
| S1513 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1625 | 1625-1625 |
| S1514 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1631 | 1631-1631 |
| S1515 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1640 | 1640-1640 |
| S1516 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1652 | 1652-1652 |
| S1517 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1660 | 1660-1660 |
| S1518 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1665 | 1665-1665 |
| S1519 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1673 | 1673-1673 |
| S1520 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1680 | 1680-1680 |
| S1521 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1687 | 1687-1687 |
| S1522 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1695 | 1695-1695 |
| S1523 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1700 | 1700-1700 |
| S1524 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1706 | 1706-1706 |
| S1525 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1712 | 1712-1712 |
| S1526 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1719 | 1719-1719 |
| S1527 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1726 | 1726-1726 |
| S1528 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 9 | 9-9 |
| S1529 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 9 | 9-9 |
| S1530 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 22 | 22-22 |
| S1531 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 28 | 28-28 |
| S1532 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 42 | 42-42 |
| S1533 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 50 | 50-50 |
| S1534 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 65 | 65-65 |
| S1535 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 73 | 73-73 |
| S1536 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 81 | 81-81 |
| S1537 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 88 | 88-88 |
| S1538 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 95 | 95-95 |
| S1539 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 103 | 103-103 |
| S1540 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 110 | 110-110 |
| S1541 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 115 | 115-115 |
| S1542 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 123 | 123-123 |
| S1543 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 130 | 130-130 |
| S1544 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 143 | 143-143 |
| S1545 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 151 | 151-151 |
| S1546 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 162 | 162-162 |
| S1547 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 170 | 170-170 |
| S1548 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 177 | 177-177 |
| S1549 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 185 | 185-185 |
| S1550 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 191 | 191-191 |
| S1551 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 197 | 197-197 |
| S1552 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 203 | 203-203 |
| S1553 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 215 | 215-215 |
| S1554 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 222 | 222-222 |
| S1555 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 228 | 228-228 |
| S1556 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 233 | 233-233 |
| S1557 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 241 | 241-241 |
| S1558 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 252 | 252-252 |
| S1559 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 260 | 260-260 |
| S1560 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 268 | 268-268 |
| S1561 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 275 | 275-275 |
| S1562 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 283 | 283-283 |
| S1563 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 290 | 290-290 |
| S1564 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 297 | 297-297 |
| S1565 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 304 | 304-304 |
| S1566 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 311 | 311-311 |
| S1567 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 319 | 319-319 |
| S1568 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 327 | 327-327 |
| S1569 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 339 | 339-339 |
| S1570 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 346 | 346-346 |
| S1571 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 353 | 353-353 |
| S1572 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 361 | 361-361 |
| S1573 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 374 | 374-374 |
| S1574 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 381 | 381-381 |
| S1575 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 388 | 388-388 |
| S1576 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 394 | 394-394 |
| S1577 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 400 | 400-400 |
| S1578 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 407 | 407-407 |
| S1579 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 415 | 415-415 |
| S1580 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 420 | 420-420 |
| S1581 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 428 | 428-428 |
| S1582 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 435 | 435-435 |
| S1583 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 441 | 441-441 |
| S1584 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 451 | 451-451 |
| S1585 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 459 | 459-459 |
| S1586 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 478 | 478-478 |
| S1587 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 483 | 483-483 |
| S1588 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 490 | 490-490 |
| S1589 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 495 | 495-495 |
| S1590 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 503 | 503-503 |
| S1591 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 509 | 509-509 |
| S1592 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 517 | 517-517 |
| S1593 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 529 | 529-529 |
| S1594 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 536 | 536-536 |
| S1595 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 544 | 544-544 |
| S1596 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 551 | 551-551 |
| S1597 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 563 | 563-563 |
| S1598 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 577 | 577-577 |
| S1599 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 584 | 584-584 |
| S1600 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 592 | 592-592 |
| S1601 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 600 | 600-600 |
| S1602 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 607 | 607-607 |
| S1603 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 615 | 615-615 |
| S1604 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 622 | 622-622 |
| S1605 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 626 | 626-626 |
| S1606 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 633 | 633-633 |
| S1607 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 637 | 637-637 |
| S1608 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 644 | 644-644 |
| S1609 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 650 | 650-650 |
| S1610 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 657 | 657-657 |
| S1611 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 665 | 665-665 |
| S1612 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 679 | 679-679 |
| S1613 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 686 | 686-686 |
| S1614 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 700 | 700-700 |
| S1615 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 707 | 707-707 |
| S1616 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 715 | 715-715 |
| S1617 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 721 | 721-721 |
| S1618 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 728 | 728-728 |
| S1619 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 734 | 734-734 |
| S1620 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 741 | 741-741 |
| S1621 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 748 | 748-748 |
| S1622 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 756 | 756-756 |
| S1623 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 762 | 762-762 |
| S1624 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 769 | 769-769 |
| S1625 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 775 | 775-775 |
| S1626 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 782 | 782-782 |
| S1627 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 789 | 789-789 |
| S1628 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 801 | 801-801 |
| S1629 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 816 | 816-816 |
| S1630 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 822 | 822-822 |
| S1631 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 829 | 829-829 |
| S1632 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 836 | 836-836 |
| S1633 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 842 | 842-842 |
| S1634 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 849 | 849-849 |
| S1635 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 857 | 857-857 |
| S1636 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 865 | 865-865 |
| S1637 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 873 | 873-873 |
| S1638 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 885 | 885-885 |
| S1639 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 891 | 891-891 |
| S1640 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 898 | 898-898 |
| S1641 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 905 | 905-905 |
| S1642 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 910 | 910-910 |
| S1643 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 918 | 918-918 |
| S1644 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 926 | 926-926 |
| S1645 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 932 | 932-932 |
| S1646 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 938 | 938-938 |
| S1647 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 943 | 943-943 |
| S1648 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 951 | 951-951 |
| S1649 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 958 | 958-958 |
| S1650 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 964 | 964-964 |
| S1651 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 971 | 971-971 |
| S1652 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 978 | 978-978 |
| S1653 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 986 | 986-986 |
| S1654 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 993 | 993-993 |
| S1655 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1004 | 1004-1004 |
| S1656 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1011 | 1011-1011 |
| S1657 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1019 | 1019-1019 |
| S1658 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1026 | 1026-1026 |
| S1659 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1031 | 1031-1031 |
| S1660 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1039 | 1039-1039 |
| S1661 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1051 | 1051-1051 |
| S1662 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1059 | 1059-1059 |
| S1663 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1065 | 1065-1065 |
| S1664 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1073 | 1073-1073 |
| S1665 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1085 | 1085-1085 |
| S1666 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1100 | 1100-1100 |
| S1667 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1106 | 1106-1106 |
| S1668 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1113 | 1113-1113 |
| S1669 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1121 | 1121-1121 |
| S1670 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1129 | 1129-1129 |
| S1671 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1141 | 1141-1141 |
| S1672 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1148 | 1148-1148 |
| S1673 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1154 | 1154-1154 |
| S1674 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1161 | 1161-1161 |
| S1675 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1169 | 1169-1169 |
| S1676 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1176 | 1176-1176 |
| S1677 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1183 | 1183-1183 |
| S1678 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1191 | 1191-1191 |
| S1679 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1197 | 1197-1197 |
| S1680 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1204 | 1204-1204 |
| S1681 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1211 | 1211-1211 |
| S1682 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1218 | 1218-1218 |
| S1683 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1225 | 1225-1225 |
| S1684 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1239 | 1239-1239 |
| S1685 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1246 | 1246-1246 |
| S1686 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1252 | 1252-1252 |
| S1687 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1256 | 1256-1256 |
| S1688 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1262 | 1262-1262 |
| S1689 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1273 | 1273-1273 |
| S1690 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1294 | 1294-1294 |
| S1691 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1302 | 1302-1302 |
| S1692 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1309 | 1309-1309 |
| S1693 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1315 | 1315-1315 |
| S1694 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1322 | 1322-1322 |
| S1695 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1329 | 1329-1329 |
| S1696 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1334 | 1334-1334 |
| S1697 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1339 | 1339-1339 |
| S1698 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1353 | 1353-1353 |
| S1699 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1358 | 1358-1358 |
| S1700 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1365 | 1365-1365 |
| S1701 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1371 | 1371-1371 |
| S1702 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1379 | 1379-1379 |
| S1703 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1381 | 1381-1381 |
| S1704 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1393 | 1393-1393 |
| S1705 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1400 | 1400-1400 |
| S1706 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1407 | 1407-1407 |
| S1707 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1414 | 1414-1414 |
| S1708 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1421 | 1421-1421 |
| S1709 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1427 | 1427-1427 |
| S1710 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1438 | 1438-1438 |
| S1711 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1454 | 1454-1454 |
| S1712 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1461 | 1461-1461 |
| S1713 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1476 | 1476-1476 |
| S1714 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1481 | 1481-1481 |
| S1715 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1494 | 1494-1494 |
| S1716 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1501 | 1501-1501 |
| S1717 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1508 | 1508-1508 |
| S1718 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1515 | 1515-1515 |
| S1719 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1522 | 1522-1522 |
| S1720 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1529 | 1529-1529 |
| S1721 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1535 | 1535-1535 |
| S1722 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1540 | 1540-1540 |
| S1723 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1547 | 1547-1547 |
| S1724 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1553 | 1553-1553 |
| S1725 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1572 | 1572-1572 |
| S1726 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1578 | 1578-1578 |
| S1727 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1584 | 1584-1584 |
| S1728 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1596 | 1596-1596 |
| S1729 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1608 | 1608-1608 |
| S1730 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1620 | 1620-1620 |
| S1731 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1641 | 1641-1641 |
| S1732 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1648 | 1648-1648 |
| S1733 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1653 | 1653-1653 |
| S1734 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1661 | 1661-1661 |
| S1735 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1666 | 1666-1666 |
| S1736 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1674 | 1674-1674 |
| S1737 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1681 | 1681-1681 |
| S1738 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1688 | 1688-1688 |
| S1739 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1696 | 1696-1696 |
| S1740 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1701 | 1701-1701 |
| S1741 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1720 | 1720-1720 |
| S1742 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | CSV line 1727 | 1727-1727 |
| S1743 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 10 | 10-10 |
| S1744 | /home/maxg/insurance01-inputs/classification-guide.md | CG-04 | 32-34 |
| S1745 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:03 PM | 153-155 |
| S1746 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:10 PM | 305-307 |
| S1747 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:06 PM | 545-547 |
| S1748 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 2 | 2-2 |
| S1749 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 3 | 3-3 |
| S1750 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 5 | 5-5 |
| S1751 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 6 | 6-6 |
| S1752 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 7 | 7-7 |
| S1753 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 8 | 8-8 |
| S1754 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 9 | 9-9 |
| S1755 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 10 | 10-10 |
| S1756 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 11 | 11-11 |
| S1757 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | CSV line 4 | 4-4 |
| S1758 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | CSV line 11 | 11-11 |
| S1759 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/application.md | application class C-110 | 7-7 |
| S1760 | /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/application.md | application class R-310 | 8-8 |

| Original source file | SHA-256 |
| --- | --- |
| /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160 |
| /home/maxg/insurance01-inputs/classification-guide.md | 89480f691737a0e8a762a836b8412476e0ed9d0b37639eb898e2826771c1dba8 |
| /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/application.md | 8df9839f4ee7b50bd3b065126c0c41560b912388732b2f663a7fb9bc6d1321be |
| /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/business-description.md | 22e444081d2d03944c083c01b0edc3969eefb8312f913d1b07c28610f4590e29 |
| /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/crew-timesheets.csv | 3f1317828f41db0e5b7e2daa74620b7e8785e2455b3599f66b2bc2612bd42d6c |
| /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/field-notes.md | f7b6b2c39c776fb5c6eae78d5552d5630e7ef2c8f832a5176bbd5c589b777405 |
| /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/payroll-register.csv | 2c05577fa783f77dd45f922c7e5a449cee03f6a3423d2ffb56526ed5d4df827d |
| /home/maxg/insurance01-inputs/employer-files/bay-crest-exteriors/site-signin-log.csv | 42b7021d03d32913a53173a5360c32fad36c6f60a0d264c87f81097da1a638e5 |

</details>

<a id="e03"></a>
## Harbor Point Legal (harbor-point-legal)

Audit period: 2025-07-07 through 2026-07-05. Submitted split: **PARTIALLY UNRESOLVED**.

Verified corrections and supported components are shown below; the full submitted split cannot yet be accepted. Differences are a **provisional comparison** of verified CSV payroll minus reported payroll. An OPEN wage omission is **not a verified payroll reduction**; unresolved payment basis may change the final allocation after evidence and approval.

Verified-only CSV: /home/maxg/ch03-premium-audit/deliverables/codes/harbor-point-legal.csv; SHA-256 a9a13218ce77920f278c3cc139e298f7d69d9baa9c580467ab13ffa40e0f91d1.

| Code | Reported payroll | Verified payroll | Difference (verified minus reported) | Verified code paragraph |
| --- | --- | --- | --- | --- |
| C-110 | 425148.16 | 360935.68 | -64212.48 | CG-04 |

Reported total $425148.16; original register $425148.16; register-minus-reported difference $0.00. Comparison definitive for current classifications: False (not human approval).

Application reported employee counts: C-110: 5. Register employees: 5.

Application sources: S0020 application.md:7-7 (application class C-110).

### Employee payroll — VERIFIED and OPEN

| Employee ID | Name | Original wages | VERIFIED wage allocation | VERIFIED additions | OPEN wages | Register source |
| --- | --- | --- | --- | --- | --- | --- |
| HP-E01 | Marcus Adeyemi | 128400.00 | C-110 128400.00 | — | 0.00 | S0001 payroll-register.csv:2-2 (CSV line 2) |
| HP-E02 | Julia Fenwick | 121750.00 | C-110 121750.00 | — | 0.00 | S0006 payroll-register.csv:3-3 (CSV line 3) |
| HP-E03 | Tomas Reyes | 64212.48 | — | — | 64212.48 | S0007 payroll-register.csv:4-4 (CSV line 4) |
| HP-E04 | Ellen Short | 51880.16 | C-110 51880.16 | — | 0.00 | S0018 payroll-register.csv:5-5 (CSV line 5) |
| HP-E05 | Gwen Talbot | 58905.52 | C-110 58905.52 | — | 0.00 | S0019 payroll-register.csv:6-6 (CSV line 6) |

No engine-supported employee-level application coding list is available. Individual results and weekly transfers below are evidenced calculations; only the aggregate submitted split is directly compared.

### Applied rule boundaries

Each decision retains the existing evaluator's scope and conditions. OPEN decisions below describe an applicability/evidence gap, not an assigned classification. Payment rule reasons and exact references are also preserved with each adjustment.

| Rule | Decision status | Scope | Applicability boundaries | Exact rule sources |
| --- | --- | --- | --- | --- |
| legal_office_actual_duties | CLASSIFIED | whole_audit_period | law office; corroborated office/professional duties; no recorded site-duty exception | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:32-34 (CG-04) |
| employer_evidence | OPEN | whole_audit_period | legal office, not a contractor; office-professional duties with unresolved exceptions | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:32-34 (CG-04); S0008 ch03-premium-audit-20261105-0222(1).md:153-155 (Nadia Brennan · 06:03 PM); S0009 ch03-premium-audit-20261105-0222(1).md:305-307 (Nadia Brennan · 06:10 PM); S0010 ch03-premium-audit-20261105-0222(1).md:545-547 (Nadia Brennan · 09:06 PM); S0011 ch03-premium-audit-20261105-0222(1).md:625-627 (Nadia Brennan · 09:11 PM) |

### Reconciliation and excluded payments

Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):

`425148.16 + 0.00 = 360935.68 + 64212.48`; difference 0.00.

Known payroll basis (includes OPEN wages): $425148.16. Verified classified payroll: $360935.68.

Other payment adjustments: **NOT EVALUATED**. No verified assertion of zero additional exposure is made; the wage reconciliation covers supplied employee records only.

| Engine control | Reconciled | Difference |
| --- | --- | --- |
| allocation | True | 0.00 |
| independent | True | 0.00 |

### OPEN findings and required human resolution

Each finding remains unanswered even if its monetary effect is zero. Employer payroll/records contact supplies the requested records; responsible policy reviewer: auditor. Identity issues require documentary confirmation of the exact employee/payee, not an assumed alias.

- **OPEN — Tomas Reyes [HP-E03]**: 6 distinct in-period site-visit dates are recorded. Nadia's sign-in practice is for contractors' office staff; no verified application exists for this legal office without a field code. Do not apply the contractor threshold or invent a field classification. Required evidence/confirmation: Confirm Tomas Reyes [HP-E03]'s actual work during every recorded site visit, including whether it was legal/client-document work or physical/inspection work.; Confirm the complete audit-period log and resolve any identity, date or duty-evidence conflicts.; Nadia or the auditor must approve treatment under CG-04 for legal-office visits; the contractor day-count threshold supplies no answer here. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E03-Q003](audit-questions.md#e03-q003). Records: S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:32-34 (CG-04); S0004 business-description.md:1-7 (business description); S0005 field-notes.md:1-5 (auditor field notes); S0007 payroll-register.csv:4-4 (CSV line 4); S0008 ch03-premium-audit-20261105-0222(1).md:153-155 (Nadia Brennan · 06:03 PM); S0009 ch03-premium-audit-20261105-0222(1).md:305-307 (Nadia Brennan · 06:10 PM); S0010 ch03-premium-audit-20261105-0222(1).md:545-547 (Nadia Brennan · 09:06 PM); S0011 ch03-premium-audit-20261105-0222(1).md:625-627 (Nadia Brennan · 09:11 PM); S0012 site-signin-log.csv:2-2 (CSV line 2); S0013 site-signin-log.csv:3-3 (CSV line 3); S0014 site-signin-log.csv:4-4 (CSV line 4); S0015 site-signin-log.csv:5-5 (CSV line 5); S0016 site-signin-log.csv:6-6 (CSV line 6); S0017 site-signin-log.csv:7-7 (CSV line 7).

- **OPEN — Application/classification comparison**: The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved. Required evidence/confirmation: Confirm the evidence-backed classification changes and resolve pending employee decisions; the application is not classification authority. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E03-Q006](audit-questions.md#e03-q006). Records: S0020 application.md:7-7 (application class C-110).

### UNAPPROVED PROPOSED treatments

These alternatives are outside all verified totals. They require the specific evidence below and explicit auditor approval, followed by a supported rerun.

- **UNAPPROVED — HP-E03**: Candidate C-110; wage basis $64212.48; paragraph CG-04. Propose retaining the entire wage basis under C-110 if the visits were solely legal/office-related work and the auditor confirms that treatment; office/professional observations support this candidate, but it is not an established house rule. Required confirmation: Confirm Tomas Reyes [HP-E03]'s actual work during every recorded site visit, including whether it was legal/client-document work or physical/inspection work.; Confirm the complete audit-period log and resolve any identity, date or duty-evidence conflicts.; Nadia or the auditor must approve treatment under CG-04 for legal-office visits; the contractor day-count threshold supplies no answer here. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E03-Q003](audit-questions.md#e03-q003).

### Allocation, payment and evidence review detail

The following entries preserve each employee/pay week, adjustment/payment, deciding reason and record confirmation. VERIFIED calculations, OPEN findings and UNAPPROVED alternatives retain their original labels. Exact dated record fields and all confirmation prompts are in the linked question document.

#### E03-Q001 — Marcus Adeyemi [HP-E01]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E03-Q001](audit-questions.md#e03-q001).

Verified base-wage allocation: C-110 $128400.00. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Law-office operations and observed office/professional duties support CG-02/CG-04; court/closings are documented as not job sites and no site exception is recorded for this employee.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| HP-E01 | audit period | audit period | 128400.00 | C-110 | CG-04 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E03-Q002 — Julia Fenwick [HP-E02]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E03-Q002](audit-questions.md#e03-q002).

Verified base-wage allocation: C-110 $121750.00. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Law-office operations and observed office/professional duties support CG-02/CG-04; court/closings are documented as not job sites and no site exception is recorded for this employee.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| HP-E02 | audit period | audit period | 121750.00 | C-110 | CG-04 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E03-Q003 — Tomas Reyes [HP-E03]

**OPEN / HUMAN APPROVAL REQUIRED**. Follow-up: [E03-Q003](audit-questions.md#e03-q003).

Verified base-wage allocation: none. OPEN base wages: $64212.48; OPEN wages are excluded from CSV totals.

6 distinct in-period site-visit dates are recorded. Nadia's sign-in practice is for contractors' office staff; no verified application exists for this legal office without a field code. Do not apply the contractor threshold or invent a field classification.

Confirmed distinct site-visit dates: 2025-09-16, 2025-10-22, 2025-12-09, 2026-01-28, 2026-03-04, 2026-04-15. Unattributed rows remain unassigned; confirm completeness separately.

UNAPPROVED PROPOSAL for HP-E03: Propose retaining the entire wage basis under C-110 if the visits were solely legal/office-related work and the auditor confirms that treatment; office/professional observations support this candidate, but it is not an established house rule.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| HP-E03 | audit period | audit period | 64212.48 | OPEN | OPEN | — |

| Proposal subject | Candidate code | Wage basis | Approval |
| --- | --- | --- | --- |
| HP-E03 | C-110 | 64212.48 | UNAPPROVED; excluded from CSV |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E03-Q004 — Ellen Short [HP-E04]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E03-Q004](audit-questions.md#e03-q004).

Verified base-wage allocation: C-110 $51880.16. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Law-office operations and observed office/professional duties support CG-02/CG-04; court/closings are documented as not job sites and no site exception is recorded for this employee.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| HP-E04 | audit period | audit period | 51880.16 | C-110 | CG-04 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0018.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E03-Q005 — Gwen Talbot [HP-E05]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E03-Q005](audit-questions.md#e03-q005).

Verified base-wage allocation: C-110 $58905.52. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Law-office operations and observed office/professional duties support CG-02/CG-04; court/closings are documented as not job sites and no site exception is recorded for this employee.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| HP-E05 | audit period | audit period | 58905.52 | C-110 | CG-04 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0019.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E03-Q006 — Application split, employee attribution and payroll reconciliation

**VERIFIED CALCULATION + OPEN FINDING / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E03-Q006](audit-questions.md#e03-q006).

Reconciliation verifies arithmetic, not employer confirmation or approval. Verified CSVs exclude OPEN wages and every unapproved proposal.

Application comparison definitive for current classifications: False; this is not audit approval.

The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved.

| Code | Reported payroll | Verified CSV payroll | Difference (verified minus reported) |
| --- | --- | --- | --- |
| C-110 | 425148.16 | 360935.68 | -64212.48 |

| Control | Reconciled | Original basis | Unresolved amount |
| --- | --- | --- | --- |
| allocation | True | 425148.16 | 64212.48 |
| independent | True | 425148.16 | 64212.48 |

Supporting source IDs (local to this employer; exact locators below): S0020.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E03-Q007 — Business, actual-duty observations and audit-period completeness

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E03-Q007](audit-questions.md#e03-q007).

Classification depends on actual work and complete period evidence; job titles and the submitted application alone do not establish a code.

Supporting source IDs (local to this employer; exact locators below): S0004, S0005.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E03-Q008 — Company-rule applicability — auditor confirmation

**AUDITOR APPROVAL / EMPLOYER FACT CONFIRMATION**. Follow-up: [E03-Q008](audit-questions.md#e03-q008).

Contractor-specific practices cannot be extended to unrelated industries; proposals are not verified rules or allocations.

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0008, S0009, S0010, S0011.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

<details>
<summary>Source and rule index — 20 exact citations</summary>

Original Classification Guide paragraph identifiers and interview timestamps/line spans are preserved here. Rule applicability is bounded by the recorded decision; a citation is not permission to extend a contractor practice to another business. Physical CSV row identities and confirmation links are preserved in the question document's record index.

| Source ID | Original document | Original paragraph / interview / record locator | Lines |
| --- | --- | --- | --- |
| S0001 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/payroll-register.csv | CSV line 2 | 2-2 |
| S0002 | /home/maxg/insurance01-inputs/classification-guide.md | CG-02 | 15-16 |
| S0003 | /home/maxg/insurance01-inputs/classification-guide.md | CG-04 | 32-34 |
| S0004 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/business-description.md | business description | 1-7 |
| S0005 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/field-notes.md | auditor field notes | 1-5 |
| S0006 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/payroll-register.csv | CSV line 3 | 3-3 |
| S0007 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/payroll-register.csv | CSV line 4 | 4-4 |
| S0008 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:03 PM | 153-155 |
| S0009 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:10 PM | 305-307 |
| S0010 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:06 PM | 545-547 |
| S0011 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:11 PM | 625-627 |
| S0012 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/site-signin-log.csv | CSV line 2 | 2-2 |
| S0013 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/site-signin-log.csv | CSV line 3 | 3-3 |
| S0014 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/site-signin-log.csv | CSV line 4 | 4-4 |
| S0015 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/site-signin-log.csv | CSV line 5 | 5-5 |
| S0016 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/site-signin-log.csv | CSV line 6 | 6-6 |
| S0017 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/site-signin-log.csv | CSV line 7 | 7-7 |
| S0018 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/payroll-register.csv | CSV line 5 | 5-5 |
| S0019 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/payroll-register.csv | CSV line 6 | 6-6 |
| S0020 | /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/application.md | application class C-110 | 7-7 |

| Original source file | SHA-256 |
| --- | --- |
| /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160 |
| /home/maxg/insurance01-inputs/classification-guide.md | 89480f691737a0e8a762a836b8412476e0ed9d0b37639eb898e2826771c1dba8 |
| /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/application.md | bfe89a3e1b01cceda79c992cda0e9fae9aef9148311b0d353bff4fb4fa1d18f1 |
| /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/business-description.md | e2836b532e7aae28f3a9d2bf755f57240dcfefeb7ccb9a81302c6403277ecf20 |
| /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/field-notes.md | 79182f054841680bbd9878653043af29b0c10f4d866cc2339a62572cd9f69cee |
| /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/payroll-register.csv | d7473ff1ddf6a2d2dbd4a09925d0cd3afbdf8ca5ad4e59d0d0c4755fd01f60bb |
| /home/maxg/insurance01-inputs/employer-files/harbor-point-legal/site-signin-log.csv | 27674afc3b226422543bc722a1148791f9f5a54e063acb9bf46af6a46f6fe461 |

</details>

<a id="e04"></a>
## Larkspur Lane Bistro (larkspur-lane-bistro)

Audit period: 2025-07-07 through 2026-07-05. Submitted split: **PARTIALLY UNRESOLVED**.

Verified corrections and supported components are shown below; the full submitted split cannot yet be accepted. Differences are a **provisional comparison** of verified CSV payroll minus reported payroll. An OPEN wage omission is **not a verified payroll reduction**; unresolved payment basis may change the final allocation after evidence and approval.

Verified-only CSV: /home/maxg/ch03-premium-audit/deliverables/codes/larkspur-lane-bistro.csv; SHA-256 c447bda4ffba3c6fce13ffeec8155ddef14725e16ece5691789d540c9974cfa5.

| Code | Reported payroll | Verified payroll | Difference (verified minus reported) | Verified code paragraph |
| --- | --- | --- | --- | --- |
| F-710 | 226431.55 | 226431.55 | 0.00 | CG-41 |
| F-720 | 114293.80 | 0.00 | -114293.80 | — no verified allocation |

Reported total $340725.35; original register $340725.35; register-minus-reported difference $0.00. Comparison definitive for current classifications: False (not human approval).

Application reported employee counts: F-710: 6; F-720: 3. Register employees: 9.

Application sources: S0020 application.md:7-7 (application class F-710); S0021 application.md:8-8 (application class F-720).

### Employee payroll — VERIFIED and OPEN

| Employee ID | Name | Original wages | VERIFIED wage allocation | VERIFIED additions | OPEN wages | Register source |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E01 | Anton Varga | 52310.45 | F-710 52310.45 | — | 0.00 | S0001 payroll-register.csv:2-2 (CSV line 2) |
| LL-E02 | Bea Lindell | 41872.30 | F-710 41872.30 | — | 0.00 | S0006 payroll-register.csv:3-3 (CSV line 3) |
| LL-E03 | Omar Haddad | 39640.15 | F-710 39640.15 | — | 0.00 | S0007 payroll-register.csv:4-4 (CSV line 4) |
| LL-E04 | Sophie Tran | 33215.80 | F-710 33215.80 | — | 0.00 | S0008 payroll-register.csv:5-5 (CSV line 5) |
| LL-E05 | Will Garner | 31904.65 | F-710 31904.65 | — | 0.00 | S0009 payroll-register.csv:6-6 (CSV line 6) |
| LL-E06 | Jose Melendez | 27488.20 | F-710 27488.20 | — | 0.00 | S0010 payroll-register.csv:7-7 (CSV line 7) |
| LL-E07 | Hannah Pryor | 46725.55 | — | — | 46725.55 | S0011 payroll-register.csv:8-8 (CSV line 8) |
| LL-E08 | Ivan Petrov | 38190.40 | — | — | 38190.40 | S0018 payroll-register.csv:9-9 (CSV line 9) |
| LL-E09 | Clara Bose | 29377.85 | — | — | 29377.85 | S0019 payroll-register.csv:10-10 (CSV line 10) |

No engine-supported employee-level application coding list is available. Individual results and weekly transfers below are evidenced calculations; only the aggregate submitted split is directly compared.

### Applied rule boundaries

Each decision retains the existing evaluator's scope and conditions. OPEN decisions below describe an applicability/evidence gap, not an assigned classification. Payment rule reasons and exact references are also preserved with each adjustment.

| Rule | Decision status | Scope | Applicability boundaries | Exact rule sources |
| --- | --- | --- | --- | --- |
| restaurant_actual_duties | CLASSIFIED | whole_audit_period | restaurant employer; corroborated restaurant kitchen/dining duties; whole audit-period register | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:58-58 (CG-41) |
| catering_receipts | OPEN | whole_audit_period | restaurant employer with a catering crew; mixed catering and restaurant duties without employee timesheets (documented interview context); complete audited-period off-site and total gross receipts | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:58-58 (CG-41); S0012 classification-guide.md:27-30 (CG-07); S0013 classification-guide.md:60-61 (CG-42); S0014 ch03-premium-audit-20261105-0222(1).md:501-503 (Max Gabel · 09:02 PM); S0015 ch03-premium-audit-20261105-0222(1).md:505-507 (Nadia Brennan · 09:02 PM); S0016 ch03-premium-audit-20261105-0222(1).md:521-523 (Nadia Brennan · 09:05 PM) |

### Reconciliation and excluded payments

Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):

`340725.35 + 0.00 = 226431.55 + 114293.80`; difference 0.00.

Known payroll basis (includes OPEN wages): $340725.35. Verified classified payroll: $226431.55.

Other payment adjustments: **NOT EVALUATED**. No verified assertion of zero additional exposure is made; the wage reconciliation covers supplied employee records only.

| Engine control | Reconciled | Difference |
| --- | --- | --- |
| allocation | True | 0.00 |
| independent | True | 0.00 |

### OPEN findings and required human resolution

Each finding remains unanswered even if its monetary effect is zero. Employer payroll/records contact supplies the requested records; responsible policy reviewer: auditor. Identity issues require documentary confirmation of the exact employee/payee, not an assumed alias.

- **OPEN — Receipt audit-period coverage**: Monthly receipt labels do not establish the same complete audit period; partial-month boundaries or missing/duplicate months require confirmation. Required evidence/confirmation: Supply receipts for the exact audited dates or authoritative evidence explaining the summary's period boundaries. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E04-Q013](audit-questions.md#e04-q013). Records: S0017 gross-receipts.csv:1-13 (monthly gross receipts).

- **OPEN — Employee timesheets**: No record confirms that employee timesheets are unavailable, or timesheet records are present; the verified mixed-duty rule requires no employee timesheets. Required evidence/confirmation: Confirm timesheet availability and provide records or an authoritative no-timesheets statement. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E04-Q014](audit-questions.md#e04-q014). Records: S0004 business-description.md:1-7 (business description); S0005 field-notes.md:1-5 (auditor field notes).

- **OPEN — Hannah Pryor [LL-E07]**: Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity. Required evidence/confirmation: Auditor or employer must confirm LL-E07: Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E04-Q007](audit-questions.md#e04-q007). Records: S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:58-58 (CG-41); S0004 business-description.md:1-7 (business description); S0005 field-notes.md:1-5 (auditor field notes); S0011 payroll-register.csv:8-8 (CSV line 8); S0012 classification-guide.md:27-30 (CG-07); S0013 classification-guide.md:60-61 (CG-42); S0014 ch03-premium-audit-20261105-0222(1).md:501-503 (Max Gabel · 09:02 PM); S0015 ch03-premium-audit-20261105-0222(1).md:505-507 (Nadia Brennan · 09:02 PM); S0016 ch03-premium-audit-20261105-0222(1).md:521-523 (Nadia Brennan · 09:05 PM); S0017 gross-receipts.csv:1-13 (monthly gross receipts).

- **OPEN — Ivan Petrov [LL-E08]**: Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity. Required evidence/confirmation: Auditor or employer must confirm LL-E08: Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E04-Q008](audit-questions.md#e04-q008). Records: S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:58-58 (CG-41); S0004 business-description.md:1-7 (business description); S0005 field-notes.md:1-5 (auditor field notes); S0012 classification-guide.md:27-30 (CG-07); S0013 classification-guide.md:60-61 (CG-42); S0014 ch03-premium-audit-20261105-0222(1).md:501-503 (Max Gabel · 09:02 PM); S0015 ch03-premium-audit-20261105-0222(1).md:505-507 (Nadia Brennan · 09:02 PM); S0016 ch03-premium-audit-20261105-0222(1).md:521-523 (Nadia Brennan · 09:05 PM); S0017 gross-receipts.csv:1-13 (monthly gross receipts); S0018 payroll-register.csv:9-9 (CSV line 9).

- **OPEN — Clara Bose [LL-E09]**: Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity. Required evidence/confirmation: Auditor or employer must confirm LL-E09: Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E04-Q009](audit-questions.md#e04-q009). Records: S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:58-58 (CG-41); S0004 business-description.md:1-7 (business description); S0005 field-notes.md:1-5 (auditor field notes); S0012 classification-guide.md:27-30 (CG-07); S0013 classification-guide.md:60-61 (CG-42); S0014 ch03-premium-audit-20261105-0222(1).md:501-503 (Max Gabel · 09:02 PM); S0015 ch03-premium-audit-20261105-0222(1).md:505-507 (Nadia Brennan · 09:02 PM); S0016 ch03-premium-audit-20261105-0222(1).md:521-523 (Nadia Brennan · 09:05 PM); S0017 gross-receipts.csv:1-13 (monthly gross receipts); S0019 payroll-register.csv:10-10 (CSV line 10).

- **OPEN — Application/classification comparison**: The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved. Required evidence/confirmation: Confirm the evidence-backed classification changes and resolve pending employee decisions; the application is not classification authority. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E04-Q010](audit-questions.md#e04-q010). Records: S0020 application.md:7-7 (application class F-710); S0021 application.md:8-8 (application class F-720).

### UNAPPROVED PROPOSED treatments

These alternatives are outside all verified totals. They require the specific evidence below and explicit auditor approval, followed by a supported rerun.

- **UNAPPROVED — LL-E07**: Candidate F-710; wage basis $46725.55; paragraph CG-41. Propose the entire wage basis under F-710 only if complete audit-period receipts confirm off-site catering below 40% of total gross receipts, the mixed-duty/no-timesheets practice applies, and the auditor approves. The supplied receipt ratio indicates this candidate but does not resolve the original OPEN evidence gaps. If complete receipts reach 40% or more, or employee timesheets exist, this proposal does not apply. Required confirmation: Employer must supply complete off-site catering and total gross receipts for 2025-07-07 through 2026-07-05, including partial-month boundaries, confirming catering below 40% of total gross receipts.; Confirm this employee's mixed catering and restaurant duties and that no employee timesheets are available; provide an authoritative no-timesheets statement. If timesheets exist, obtain CG-07 review instead.; The assigned auditor must review the exact-period evidence, confirm the below-40% rule applies, and approve F-710 before these OPEN wages can enter verified allocations. The current monthly-receipts schema does not verify partial-month coverage automatically. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E04-Q007](audit-questions.md#e04-q007).

- **UNAPPROVED — LL-E08**: Candidate F-710; wage basis $38190.40; paragraph CG-41. Propose the entire wage basis under F-710 only if complete audit-period receipts confirm off-site catering below 40% of total gross receipts, the mixed-duty/no-timesheets practice applies, and the auditor approves. The supplied receipt ratio indicates this candidate but does not resolve the original OPEN evidence gaps. If complete receipts reach 40% or more, or employee timesheets exist, this proposal does not apply. Required confirmation: Employer must supply complete off-site catering and total gross receipts for 2025-07-07 through 2026-07-05, including partial-month boundaries, confirming catering below 40% of total gross receipts.; Confirm this employee's mixed catering and restaurant duties and that no employee timesheets are available; provide an authoritative no-timesheets statement. If timesheets exist, obtain CG-07 review instead.; The assigned auditor must review the exact-period evidence, confirm the below-40% rule applies, and approve F-710 before these OPEN wages can enter verified allocations. The current monthly-receipts schema does not verify partial-month coverage automatically. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E04-Q008](audit-questions.md#e04-q008).

- **UNAPPROVED — LL-E09**: Candidate F-710; wage basis $29377.85; paragraph CG-41. Propose the entire wage basis under F-710 only if complete audit-period receipts confirm off-site catering below 40% of total gross receipts, the mixed-duty/no-timesheets practice applies, and the auditor approves. The supplied receipt ratio indicates this candidate but does not resolve the original OPEN evidence gaps. If complete receipts reach 40% or more, or employee timesheets exist, this proposal does not apply. Required confirmation: Employer must supply complete off-site catering and total gross receipts for 2025-07-07 through 2026-07-05, including partial-month boundaries, confirming catering below 40% of total gross receipts.; Confirm this employee's mixed catering and restaurant duties and that no employee timesheets are available; provide an authoritative no-timesheets statement. If timesheets exist, obtain CG-07 review instead.; The assigned auditor must review the exact-period evidence, confirm the below-40% rule applies, and approve F-710 before these OPEN wages can enter verified allocations. The current monthly-receipts schema does not verify partial-month coverage automatically. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E04-Q009](audit-questions.md#e04-q009).

### Allocation, payment and evidence review detail

The following entries preserve each employee/pay week, adjustment/payment, deciding reason and record confirmation. VERIFIED calculations, OPEN findings and UNAPPROVED alternatives retain their original labels. Exact dated record fields and all confirmation prompts are in the linked question document.

#### E04-Q001 — Anton Varga [LL-E01]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E04-Q001](audit-questions.md#e04-q001).

Verified base-wage allocation: F-710 $52310.45. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Restaurant business and kitchen/dining field observations corroborate this register role as preparation/service of meals under CG-02 and CG-41.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E01 | audit period | audit period | 52310.45 | F-710 | CG-41 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q002 — Bea Lindell [LL-E02]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E04-Q002](audit-questions.md#e04-q002).

Verified base-wage allocation: F-710 $41872.30. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Restaurant business and kitchen/dining field observations corroborate this register role as preparation/service of meals under CG-02 and CG-41.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E02 | audit period | audit period | 41872.30 | F-710 | CG-41 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q003 — Omar Haddad [LL-E03]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E04-Q003](audit-questions.md#e04-q003).

Verified base-wage allocation: F-710 $39640.15. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Restaurant business and kitchen/dining field observations corroborate this register role as preparation/service of meals under CG-02 and CG-41.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E03 | audit period | audit period | 39640.15 | F-710 | CG-41 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0007.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q004 — Sophie Tran [LL-E04]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E04-Q004](audit-questions.md#e04-q004).

Verified base-wage allocation: F-710 $33215.80. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Restaurant business and kitchen/dining field observations corroborate this register role as preparation/service of meals under CG-02 and CG-41.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E04 | audit period | audit period | 33215.80 | F-710 | CG-41 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0008.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q005 — Will Garner [LL-E05]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E04-Q005](audit-questions.md#e04-q005).

Verified base-wage allocation: F-710 $31904.65. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Restaurant business and kitchen/dining field observations corroborate this register role as preparation/service of meals under CG-02 and CG-41.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E05 | audit period | audit period | 31904.65 | F-710 | CG-41 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0009.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q006 — Jose Melendez [LL-E06]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E04-Q006](audit-questions.md#e04-q006).

Verified base-wage allocation: F-710 $27488.20. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Restaurant business and kitchen/dining field observations corroborate this register role as preparation/service of meals under CG-02 and CG-41.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E06 | audit period | audit period | 27488.20 | F-710 | CG-41 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0010.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q007 — Hannah Pryor [LL-E07]

**OPEN / HUMAN APPROVAL REQUIRED**. Follow-up: [E04-Q007](audit-questions.md#e04-q007).

Verified base-wage allocation: none. OPEN base wages: $46725.55; OPEN wages are excluded from CSV totals.

Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity.

UNAPPROVED PROPOSAL for LL-E07: Propose the entire wage basis under F-710 only if complete audit-period receipts confirm off-site catering below 40% of total gross receipts, the mixed-duty/no-timesheets practice applies, and the auditor approves. The supplied receipt ratio indicates this candidate but does not resolve the original OPEN evidence gaps. If complete receipts reach 40% or more, or employee timesheets exist, this proposal does not apply.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E07 | audit period | audit period | 46725.55 | OPEN | OPEN | — |

| Proposal subject | Candidate code | Wage basis | Approval |
| --- | --- | --- | --- |
| LL-E07 | F-710 | 46725.55 | UNAPPROVED; excluded from CSV |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0011, S0012, S0013, S0014, S0015, S0016, S0017.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q008 — Ivan Petrov [LL-E08]

**OPEN / HUMAN APPROVAL REQUIRED**. Follow-up: [E04-Q008](audit-questions.md#e04-q008).

Verified base-wage allocation: none. OPEN base wages: $38190.40; OPEN wages are excluded from CSV totals.

Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity.

UNAPPROVED PROPOSAL for LL-E08: Propose the entire wage basis under F-710 only if complete audit-period receipts confirm off-site catering below 40% of total gross receipts, the mixed-duty/no-timesheets practice applies, and the auditor approves. The supplied receipt ratio indicates this candidate but does not resolve the original OPEN evidence gaps. If complete receipts reach 40% or more, or employee timesheets exist, this proposal does not apply.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E08 | audit period | audit period | 38190.40 | OPEN | OPEN | — |

| Proposal subject | Candidate code | Wage basis | Approval |
| --- | --- | --- | --- |
| LL-E08 | F-710 | 38190.40 | UNAPPROVED; excluded from CSV |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0012, S0013, S0014, S0015, S0016, S0017, S0018.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q009 — Clara Bose [LL-E09]

**OPEN / HUMAN APPROVAL REQUIRED**. Follow-up: [E04-Q009](audit-questions.md#e04-q009).

Verified base-wage allocation: none. OPEN base wages: $29377.85; OPEN wages are excluded from CSV totals.

Confirm the cited records cover the complete relevant audit period or pay week; missing records cannot establish zero activity.

UNAPPROVED PROPOSAL for LL-E09: Propose the entire wage basis under F-710 only if complete audit-period receipts confirm off-site catering below 40% of total gross receipts, the mixed-duty/no-timesheets practice applies, and the auditor approves. The supplied receipt ratio indicates this candidate but does not resolve the original OPEN evidence gaps. If complete receipts reach 40% or more, or employee timesheets exist, this proposal does not apply.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| LL-E09 | audit period | audit period | 29377.85 | OPEN | OPEN | — |

| Proposal subject | Candidate code | Wage basis | Approval |
| --- | --- | --- | --- |
| LL-E09 | F-710 | 29377.85 | UNAPPROVED; excluded from CSV |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0012, S0013, S0014, S0015, S0016, S0017, S0019.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q010 — Application split, employee attribution and payroll reconciliation

**VERIFIED CALCULATION + OPEN FINDING / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E04-Q010](audit-questions.md#e04-q010).

Reconciliation verifies arithmetic, not employer confirmation or approval. Verified CSVs exclude OPEN wages and every unapproved proposal.

Application comparison definitive for current classifications: False; this is not audit approval.

The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved.

| Code | Reported payroll | Verified CSV payroll | Difference (verified minus reported) |
| --- | --- | --- | --- |
| F-710 | 226431.55 | 226431.55 | 0.00 |
| F-720 | 114293.80 | 0.00 | -114293.80 |

| Control | Reconciled | Original basis | Unresolved amount |
| --- | --- | --- | --- |
| allocation | True | 340725.35 | 114293.80 |
| independent | True | 340725.35 | 114293.80 |

Supporting source IDs (local to this employer; exact locators below): S0020, S0021.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q011 — Business, actual-duty observations and audit-period completeness

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E04-Q011](audit-questions.md#e04-q011).

Classification depends on actual work and complete period evidence; job titles and the submitted application alone do not establish a code.

Supporting source IDs (local to this employer; exact locators below): S0004, S0005.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q012 — Company-rule applicability — auditor confirmation

**AUDITOR APPROVAL / EMPLOYER FACT CONFIRMATION**. Follow-up: [E04-Q012](audit-questions.md#e04-q012).

Contractor-specific practices cannot be extended to unrelated industries; proposals are not verified rules or allocations.

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0012, S0013, S0014, S0015, S0016.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q013 — Receipt audit-period coverage and mixed-duty catering evidence

**OPEN / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E04-Q013](audit-questions.md#e04-q013).

Recorded dine-in $1284615.20, off-site $362410.85, total $1647026.05; diagnostic percentage 22.00% (rounded for display only); complete period confirmed: False. Exact values remain in review state; an unconfirmed period does not verify a catering allocation.

Monthly receipt labels do not establish the same complete audit period; partial-month boundaries or missing/duplicate months require confirmation.

Supporting source IDs (local to this employer; exact locators below): S0017.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E04-Q014 — Employee timesheets

**OPEN / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E04-Q014](audit-questions.md#e04-q014).

No record confirms that employee timesheets are unavailable, or timesheet records are present; the verified mixed-duty rule requires no employee timesheets.

Supporting source IDs (local to this employer; exact locators below): S0004, S0005.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

<details>
<summary>Source and rule index — 21 exact citations</summary>

Original Classification Guide paragraph identifiers and interview timestamps/line spans are preserved here. Rule applicability is bounded by the recorded decision; a citation is not permission to extend a contractor practice to another business. Physical CSV row identities and confirmation links are preserved in the question document's record index.

| Source ID | Original document | Original paragraph / interview / record locator | Lines |
| --- | --- | --- | --- |
| S0001 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 2 | 2-2 |
| S0002 | /home/maxg/insurance01-inputs/classification-guide.md | CG-02 | 15-16 |
| S0003 | /home/maxg/insurance01-inputs/classification-guide.md | CG-41 | 58-58 |
| S0004 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/business-description.md | business description | 1-7 |
| S0005 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/field-notes.md | auditor field notes | 1-5 |
| S0006 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 3 | 3-3 |
| S0007 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 4 | 4-4 |
| S0008 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 5 | 5-5 |
| S0009 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 6 | 6-6 |
| S0010 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 7 | 7-7 |
| S0011 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 8 | 8-8 |
| S0012 | /home/maxg/insurance01-inputs/classification-guide.md | CG-07 | 27-30 |
| S0013 | /home/maxg/insurance01-inputs/classification-guide.md | CG-42 | 60-61 |
| S0014 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Max Gabel · 09:02 PM | 501-503 |
| S0015 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:02 PM | 505-507 |
| S0016 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:05 PM | 521-523 |
| S0017 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/gross-receipts.csv | monthly gross receipts | 1-13 |
| S0018 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 9 | 9-9 |
| S0019 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | CSV line 10 | 10-10 |
| S0020 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/application.md | application class F-710 | 7-7 |
| S0021 | /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/application.md | application class F-720 | 8-8 |

| Original source file | SHA-256 |
| --- | --- |
| /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160 |
| /home/maxg/insurance01-inputs/classification-guide.md | 89480f691737a0e8a762a836b8412476e0ed9d0b37639eb898e2826771c1dba8 |
| /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/application.md | e80ab8ffeb32d9208515da8f8671416f0897a71d83f6f6f223dd54e62486df7b |
| /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/business-description.md | 296ef9224ae172d208941e67f6ba83bfa5ab049c46117acb56873bf56e707e5e |
| /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/field-notes.md | d7df20e3f376bd598149a7d0394a4a55dd898caaeb1cb1c9d73b2cf76b0f782c |
| /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/gross-receipts.csv | 66f5e8a17bfe7cc4b0f4c36029859d4d20fa25ac64df3b426ccefb0471186d55 |
| /home/maxg/insurance01-inputs/employer-files/larkspur-lane-bistro/payroll-register.csv | 2190e692efc90ec036d6b69ee51726ca37d5ada823148c928e55396c0f188ecf |

</details>

<a id="e05"></a>
## Patuxent Electric (patuxent-electric)

Audit period: 2025-07-07 through 2026-07-05. Submitted split: **PARTIALLY UNRESOLVED**.

Verified corrections and supported components are shown below; the full submitted split cannot yet be accepted. Differences are a **provisional comparison** of verified CSV payroll minus reported payroll. An OPEN wage omission is **not a verified payroll reduction**; unresolved payment basis may change the final allocation after evidence and approval.

Verified-only CSV: /home/maxg/ch03-premium-audit/deliverables/codes/patuxent-electric.csv; SHA-256 d15c7eae8e969cec8f807ccebedf9c3b584e849460c03f918497c3c0067ffef7.

| Code | Reported payroll | Verified payroll | Difference (verified minus reported) | Verified code paragraph |
| --- | --- | --- | --- | --- |
| C-110 | 161905.60 | 43905.60 | -118000.00 | CG-04 |
| E-510 | 306024.85 | 426184.85 | 120160.00 | CG-21 |

Reported total $467930.45; original register $467930.45; register-minus-reported difference $0.00. Comparison definitive for current classifications: False (not human approval).

Application reported employee counts: E-510: 5; C-110: 2. Register employees: 7.

Application sources: S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110).

### Employee payroll — VERIFIED and OPEN

| Employee ID | Name | Original wages | VERIFIED wage allocation | VERIFIED additions | OPEN wages | Register source |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E01 | Raymond Dunmore | 118000.00 | E-510 118000.00 | — | 0.00 | S0001 payroll-register.csv:2-2 (CSV line 2) |
| PE-E02 | Curtis Bell | 72410.35 | E-510 72410.35 | E-510 720.00 | 0.00 | S0222 payroll-register.csv:3-3 (CSV line 3) |
| PE-E03 | Hector Ruiz | 69855.90 | E-510 69855.90 | E-510 720.00 | 0.00 | S0223 payroll-register.csv:4-4 (CSV line 4) |
| PE-E04 | Aaron Weiss | 64120.65 | E-510 64120.65 | E-510 720.00 | 0.00 | S0224 payroll-register.csv:5-5 (CSV line 5) |
| PE-E05 | Tyrone Banks | 58377.20 | E-510 58377.20 | — | 0.00 | S0225 payroll-register.csv:6-6 (CSV line 6) |
| PE-E06 | Kyle Brandt | 41260.75 | E-510 41260.75 | — | 0.00 | S0226 payroll-register.csv:7-7 (CSV line 7) |
| PE-E07 | Linda Marsh | 43905.60 | C-110 43905.60 | — | 0.00 | S0227 payroll-register.csv:8-8 (CSV line 8) |

Employee-level application assignments below are marked inferred where the engine derives them from the submitted counts/payroll; they are not employer-supplied employee coding lists.

| Employee | Wage basis | Reported code | Calculated code | Status | Reported attribution | Reason / records |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E01 Raymond Dunmore | 118000.00 | C-110 | E-510 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0001 payroll-register.csv:2-2 (CSV line 2); S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110) |
| PE-E02 Curtis Bell | 72410.35 | E-510 | E-510 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0222 payroll-register.csv:3-3 (CSV line 3); S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110) |
| PE-E03 Hector Ruiz | 69855.90 | E-510 | E-510 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0223 payroll-register.csv:4-4 (CSV line 4); S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110) |
| PE-E04 Aaron Weiss | 64120.65 | E-510 | E-510 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0224 payroll-register.csv:5-5 (CSV line 5); S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110) |
| PE-E05 Tyrone Banks | 58377.20 | E-510 | E-510 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0225 payroll-register.csv:6-6 (CSV line 6); S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110) |
| PE-E06 Kyle Brandt | 41260.75 | E-510 | E-510 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0226 payroll-register.csv:7-7 (CSV line 7); S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110) |
| PE-E07 Linda Marsh | 43905.60 | C-110 | C-110 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0227 payroll-register.csv:8-8 (CSV line 8); S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110) |

### Applied rule boundaries

Each decision retains the existing evaluator's scope and conditions. OPEN decisions below describe an applicability/evidence gap, not an assigned classification. Payment rule reasons and exact references are also preserved with each adjustment.

| Rule | Decision status | Scope | Applicability boundaries | Exact rule sources |
| --- | --- | --- | --- | --- |
| electrical_actual_duties | CLASSIFIED | whole_audit_period | electrical employer; corroborated actual duties; included owner evidence under CG-05 | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:48-49 (CG-21); S0004 classification-guide.md:21-22 (CG-05) |
| electrical_actual_duties | CLASSIFIED | whole_audit_period | electrical employer; corroborated actual duties; documented employee work | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:48-49 (CG-21) |
| electrical_actual_duties | CLASSIFIED | whole_audit_period | electrical employer; corroborated actual duties; documented employee work | S0002 classification-guide.md:15-16 (CG-02); S0228 classification-guide.md:32-34 (CG-04) |

### Reconciliation and excluded payments

Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):

`467930.45 + 2160.00 = 470090.45 + 0.00`; difference 0.00.

Known payroll basis (includes OPEN wages): $470090.45. Verified classified payroll: $470090.45.

Payment reconciliation (evaluated payment basis = verified addition + nonpayroll + OPEN payment basis):

`9224.00 = 2160.00 + 6674.00 + 390.00`; difference 0.00.

Cash reconciliation (original wages + evaluated payments = verified payroll + OPEN wages + excluded/nonpayroll payments + OPEN payment basis):

`477154.45 = 470090.45 + 0.00 + 6674.00 + 390.00`; difference 0.00.

| Engine control | Reconciled | Difference |
| --- | --- | --- |
| allocation | True | 0.00 |
| independent | True | 0.00 |
| adjustments | True | 0.00 |
| travel | True | 0.00 |

Owner Raymond Dunmore: **INCLUDED**; removed register wages $0.00. No exclusion is documented, and actual electrical fieldwork supports including the owner's recorded wages under CG-05/CG-21. Records: S0001 payroll-register.csv:2-2 (CSV line 2); S0004 classification-guide.md:21-22 (CG-05); S0005 business-description.md:1-7 (business description); S0006 field-notes.md:1-6 (auditor field notes).

### OPEN findings and required human resolution

Each finding remains unanswered even if its monetary effect is zero. Employer payroll/records contact supplies the requested records; responsible policy reviewer: auditor. Identity issues require documentary confirmation of the exact employee/payee, not an assumed alias.

- **OPEN — travel:PE-E06**: Nadia has no practice for a paid allowance with zero documented out-of-town days; confirm treatment and any missing travel evidence. Required evidence/confirmation: Auditor or employer must confirm Kyle Brandt [PE-E06], record travel:PE-E06: Nadia has no practice for a paid allowance with zero documented out-of-town days; confirm treatment and any missing travel evidence.; Confirm whether zero recorded out-of-town days is correct and provide any missing travel dates.; Explain the allowance's purpose and supply supporting payment/travel documentation.; Confirm this payment is not already included in wages_paid before approving an addition.; Approve or revise the separate proposed inclusion under the verified work code; no zero-day treatment is assumed. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E05-Q013](audit-questions.md#e05-q013). Records: S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:48-49 (CG-21); S0005 business-description.md:1-7 (business description); S0006 field-notes.md:1-6 (auditor field notes); S0007 site-signin-log.csv:1-215 (examined site sign-in log); S0226 payroll-register.csv:7-7 (CSV line 7); S0229 classification-guide.md:18-19 (CG-03); S0230 ch03-premium-audit-20261105-0222(1).md:185-187 (Nadia Brennan · 06:05 PM); S0231 ch03-premium-audit-20261105-0222(1).md:609-611 (Nadia Brennan · 09:09 PM); S0232 field-notes.md:1-6 (documented flat daily allowance and additional wage basis).

- **OPEN — Application/classification comparison**: The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved. Required evidence/confirmation: Confirm the evidence-backed classification changes and resolve pending employee decisions; the application is not classification authority. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E05-Q015](audit-questions.md#e05-q015). Records: S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110).

- **OPEN — Application employee attribution**: Employee assignments are not explicitly listed on the application. A unique exact count/wage partition supports the inferred comparison. Required evidence/confirmation: Confirm the employer's employee-level reported codes; classification decisions remain based on work records. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E05-Q015](audit-questions.md#e05-q015). Records: S0233 application.md:7-7 (application class E-510); S0234 application.md:8-8 (application class C-110).

### UNAPPROVED PROPOSED treatments

These alternatives are outside all verified totals. They require the specific evidence below and explicit auditor approval, followed by a supported rerun.

- **UNAPPROVED — travel:PE-E06**: Candidate E-510; proposed payroll $390.00; proposed nonpayroll $0.00. Propose including the full allowance as payroll because no exclusion days are documented, pending auditor/employer confirmation; this is not a verified house rule. Required confirmation: Auditor or employer must confirm Kyle Brandt [PE-E06], record travel:PE-E06: Nadia has no practice for a paid allowance with zero documented out-of-town days; confirm treatment and any missing travel evidence.; Confirm whether zero recorded out-of-town days is correct and provide any missing travel dates.; Explain the allowance's purpose and supply supporting payment/travel documentation.; Confirm this payment is not already included in wages_paid before approving an addition.; Approve or revise the separate proposed inclusion under the verified work code; no zero-day treatment is assumed. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E05-Q013](audit-questions.md#e05-q013).

### Allocation, payment and evidence review detail

The following entries preserve each employee/pay week, adjustment/payment, deciding reason and record confirmation. VERIFIED calculations, OPEN findings and UNAPPROVED alternatives retain their original labels. Exact dated record fields and all confirmation prompts are in the linked question document.

#### E05-Q001 — Raymond Dunmore [PE-E01]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q001](audit-questions.md#e05-q001).

Verified base-wage allocation: E-510 $118000.00. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented wiring business and corroborated actual duties support electrical field payroll under CG-21.

Confirmed distinct site-visit dates: 2025-07-07, 2025-07-08, 2025-07-09, 2025-07-10, 2025-07-11, 2025-07-14, 2025-07-15, 2025-07-16, 2025-07-17, 2025-07-21, 2025-07-23, 2025-07-25, 2025-07-28, 2025-07-29, 2025-07-30, 2025-07-31, 2025-08-01, 2025-08-04, 2025-08-05, 2025-08-06, 2025-08-07, 2025-08-08, 2025-08-11, 2025-08-12, 2025-08-13, 2025-08-14, 2025-08-15, 2025-08-18, 2025-08-19, 2025-08-20, 2025-08-21, 2025-08-25, 2025-08-27, 2025-08-28, 2025-08-29, 2025-09-01, 2025-09-02, 2025-09-03, 2025-09-04, 2025-09-05, 2025-09-09, 2025-09-10, 2025-09-12, 2025-09-15, 2025-09-17, 2025-09-18, 2025-09-19, 2025-09-22, 2025-09-23, 2025-09-25, 2025-09-26, 2025-09-29, 2025-09-30, 2025-10-01, 2025-10-02, 2025-10-06, 2025-10-07, 2025-10-08, 2025-10-09, 2025-10-13, 2025-10-14, 2025-10-15, 2025-10-16, 2025-10-17, 2025-10-22, 2025-10-23, 2025-10-24, 2025-10-27, 2025-10-28, 2025-10-30, 2025-10-31, 2025-11-03, 2025-11-04, 2025-11-05, 2025-11-07, 2025-11-10, 2025-11-12, 2025-11-13, 2025-11-14, 2025-11-17, 2025-11-18, 2025-11-20, 2025-11-21, 2025-11-24, 2025-11-25, 2025-11-26, 2025-11-28, 2025-12-01, 2025-12-03, 2025-12-04, 2025-12-05, 2025-12-08, 2025-12-09, 2025-12-10, 2025-12-11, 2025-12-12, 2025-12-15, 2025-12-16, 2025-12-18, 2025-12-19, 2025-12-22, 2025-12-24, 2025-12-25, 2025-12-26, 2025-12-29, 2025-12-30, 2025-12-31, 2026-01-02, 2026-01-05, 2026-01-06, 2026-01-07, 2026-01-08, 2026-01-09, 2026-01-12, 2026-01-14, 2026-01-15, 2026-01-19, 2026-01-20, 2026-01-21, 2026-01-22, 2026-01-23, 2026-01-26, 2026-01-27, 2026-01-28, 2026-01-30, 2026-02-02, 2026-02-03, 2026-02-04, 2026-02-05, 2026-02-06, 2026-02-09, 2026-02-11, 2026-02-12, 2026-02-13, 2026-02-16, 2026-02-18, 2026-02-19, 2026-02-20, 2026-02-23, 2026-02-24, 2026-02-25, 2026-02-26, 2026-02-27, 2026-03-06, 2026-03-09, 2026-03-11, 2026-03-12, 2026-03-13, 2026-03-16, 2026-03-17, 2026-03-18, 2026-03-19, 2026-03-20, 2026-03-23, 2026-03-24, 2026-03-26, 2026-03-27, 2026-03-31, 2026-04-02, 2026-04-03, 2026-04-06, 2026-04-07, 2026-04-08, 2026-04-09, 2026-04-10, 2026-04-13, 2026-04-14, 2026-04-16, 2026-04-17, 2026-04-20, 2026-04-21, 2026-04-23, 2026-04-24, 2026-04-27, 2026-04-28, 2026-04-30, 2026-05-01, 2026-05-04, 2026-05-05, 2026-05-06, 2026-05-07, 2026-05-08, 2026-05-11, 2026-05-12, 2026-05-13, 2026-05-14, 2026-05-15, 2026-05-18, 2026-05-19, 2026-05-21, 2026-05-25, 2026-05-26, 2026-05-27, 2026-05-29, 2026-06-03, 2026-06-04, 2026-06-08, 2026-06-09, 2026-06-10, 2026-06-11, 2026-06-15, 2026-06-16, 2026-06-17, 2026-06-19, 2026-06-22, 2026-06-23, 2026-06-24, 2026-06-25, 2026-06-26, 2026-06-29, 2026-06-30, 2026-07-01, 2026-07-02, 2026-07-03. Unattributed rows remain unassigned; confirm completeness separately.

No exclusion is documented, and actual electrical fieldwork supports including the owner's recorded wages under CG-05/CG-21.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E01 | audit period | audit period | 118000.00 | E-510 | CG-21 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0083, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0102, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0140, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0197, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0216, S0217, S0218, S0219, S0220, S0221, S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q002 — Curtis Bell [PE-E02]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q002](audit-questions.md#e05-q002).

Verified base-wage allocation: E-510 $72410.35. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented wiring business and corroborated actual duties support electrical field payroll under CG-21.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E02 | audit period | audit period | 72410.35 | E-510 | CG-21 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0222, S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q003 — Hector Ruiz [PE-E03]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q003](audit-questions.md#e05-q003).

Verified base-wage allocation: E-510 $69855.90. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented wiring business and corroborated actual duties support electrical field payroll under CG-21.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E03 | audit period | audit period | 69855.90 | E-510 | CG-21 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0223, S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q004 — Aaron Weiss [PE-E04]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q004](audit-questions.md#e05-q004).

Verified base-wage allocation: E-510 $64120.65. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented wiring business and corroborated actual duties support electrical field payroll under CG-21.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E04 | audit period | audit period | 64120.65 | E-510 | CG-21 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0224, S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q005 — Tyrone Banks [PE-E05]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q005](audit-questions.md#e05-q005).

Verified base-wage allocation: E-510 $58377.20. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented wiring business and corroborated actual duties support electrical field payroll under CG-21.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E05 | audit period | audit period | 58377.20 | E-510 | CG-21 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0225, S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q006 — Kyle Brandt [PE-E06]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q006](audit-questions.md#e05-q006).

Verified base-wage allocation: E-510 $41260.75. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented wiring business and corroborated actual duties support electrical field payroll under CG-21.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E06 | audit period | audit period | 41260.75 | E-510 | CG-21 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0226, S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q007 — Linda Marsh [PE-E07]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q007](audit-questions.md#e05-q007).

Verified base-wage allocation: C-110 $43905.60. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Named field observations establish office-only duties, corroborated by the examined sign-ins, under CG-04.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| PE-E07 | audit period | audit period | 43905.60 | C-110 | CG-04 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0005, S0006, S0007, S0227, S0228, S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q008 — Raymond Dunmore [PE-E01] — travel allowance

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q008](audit-questions.md#e05-q008).

No allowance was paid; no payroll addition or exclusion is required.

Verified payroll addition $0.00; verified nonpayroll $0.00; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| travel:PE-E01 | 2025-07-07 through 2026-07-05 | 0.00 | 0 | 0.00 | 0.00 | 0.00 | — no payroll allocation | VERIFIED |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0041, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0050, S0051, S0052, S0053, S0054, S0055, S0056, S0057, S0058, S0059, S0060, S0061, S0062, S0063, S0064, S0065, S0066, S0067, S0068, S0069, S0070, S0071, S0072, S0073, S0074, S0075, S0076, S0077, S0078, S0079, S0080, S0081, S0082, S0083, S0084, S0085, S0086, S0087, S0088, S0089, S0090, S0091, S0092, S0093, S0094, S0095, S0096, S0097, S0098, S0099, S0100, S0101, S0102, S0103, S0104, S0105, S0106, S0107, S0108, S0109, S0110, S0111, S0112, S0113, S0114, S0115, S0116, S0117, S0118, S0119, S0120, S0121, S0122, S0123, S0124, S0125, S0126, S0127, S0128, S0129, S0130, S0131, S0132, S0133, S0134, S0135, S0136, S0137, S0138, S0139, S0140, S0141, S0142, S0143, S0144, S0145, S0146, S0147, S0148, S0149, S0150, S0151, S0152, S0153, S0154, S0155, S0156, S0157, S0158, S0159, S0160, S0161, S0162, S0163, S0164, S0165, S0166, S0167, S0168, S0169, S0170, S0171, S0172, S0173, S0174, S0175, S0176, S0177, S0178, S0179, S0180, S0181, S0182, S0183, S0184, S0185, S0186, S0187, S0188, S0189, S0190, S0191, S0192, S0193, S0194, S0195, S0196, S0197, S0198, S0199, S0200, S0201, S0202, S0203, S0204, S0205, S0206, S0207, S0208, S0209, S0210, S0211, S0212, S0213, S0214, S0215, S0216, S0217, S0218, S0219, S0220, S0221, S0229, S0230, S0231, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q009 — Curtis Bell [PE-E02] — travel allowance

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q009](audit-questions.md#e05-q009).

Exclude up to $47 for each of 40 documented out-of-town days; add only the excess to payroll.

Verified payroll addition $720.00; verified nonpayroll $1880.00; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| travel:PE-E02 | 2025-07-07 through 2026-07-05 | 2600.00 | 40 | 720.00 | 1880.00 | 0.00 | E-510 | VERIFIED |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0222, S0229, S0230, S0231, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q010 — Hector Ruiz [PE-E03] — travel allowance

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q010](audit-questions.md#e05-q010).

Exclude up to $47 for each of 40 documented out-of-town days; add only the excess to payroll.

Verified payroll addition $720.00; verified nonpayroll $1880.00; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| travel:PE-E03 | 2025-07-07 through 2026-07-05 | 2600.00 | 40 | 720.00 | 1880.00 | 0.00 | E-510 | VERIFIED |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0223, S0229, S0230, S0231, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q011 — Aaron Weiss [PE-E04] — travel allowance

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q011](audit-questions.md#e05-q011).

Exclude up to $47 for each of 40 documented out-of-town days; add only the excess to payroll.

Verified payroll addition $720.00; verified nonpayroll $1880.00; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| travel:PE-E04 | 2025-07-07 through 2026-07-05 | 2600.00 | 40 | 720.00 | 1880.00 | 0.00 | E-510 | VERIFIED |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0224, S0229, S0230, S0231, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q012 — Tyrone Banks [PE-E05] — travel allowance

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q012](audit-questions.md#e05-q012).

Exclude up to $47 for each of 22 documented out-of-town days; add only the excess to payroll.

Verified payroll addition $0.00; verified nonpayroll $1034.00; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| travel:PE-E05 | 2025-07-07 through 2026-07-05 | 1034.00 | 22 | 0.00 | 1034.00 | 0.00 | — no payroll allocation | VERIFIED |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0225, S0229, S0230, S0231, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q013 — Kyle Brandt [PE-E06] — travel allowance

**OPEN / HUMAN APPROVAL REQUIRED**. Follow-up: [E05-Q013](audit-questions.md#e05-q013).

Nadia has no practice for a paid allowance with zero documented out-of-town days; confirm treatment and any missing travel evidence.

Verified payroll addition $0.00; verified nonpayroll $0.00; OPEN payment basis $390.00. OPEN basis is not itself an assigned payroll amount.

UNAPPROVED PROPOSAL for travel:PE-E06: Propose including the full allowance as payroll because no exclusion days are documented, pending auditor/employer confirmation; this is not a verified house rule.

UNAPPROVED PROPOSAL total payroll addition: $390.00; not in verified CSV totals.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| travel:PE-E06 | 2025-07-07 through 2026-07-05 | 390.00 | 0 | 0.00 | 0.00 | 390.00 | OPEN | OPEN |

| Proposal payment | Candidate work code | Proposed payroll | Proposed nonpayroll | Approval |
| --- | --- | --- | --- | --- |
| travel:PE-E06 | E-510 | 390.00 | 0.00 | UNAPPROVED; excluded from CSV |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0005, S0006, S0007, S0226, S0229, S0230, S0231, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q014 — Linda Marsh [PE-E07] — travel allowance

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q014](audit-questions.md#e05-q014).

No allowance was paid; no payroll addition or exclusion is required.

Verified payroll addition $0.00; verified nonpayroll $0.00; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| travel:PE-E07 | 2025-07-07 through 2026-07-05 | 0.00 | 0 | 0.00 | 0.00 | 0.00 | — no payroll allocation | VERIFIED |

Supporting source IDs (local to this employer; exact locators below): S0002, S0005, S0006, S0007, S0227, S0228, S0229, S0230, S0231, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q015 — Application split, employee attribution and payroll reconciliation

**VERIFIED CALCULATION + OPEN FINDING / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E05-Q015](audit-questions.md#e05-q015).

Reconciliation verifies arithmetic, not employer confirmation or approval. Verified CSVs exclude OPEN wages and every unapproved proposal.

Application comparison definitive for current classifications: False; this is not audit approval.

The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved.

Employee assignments are not explicitly listed on the application. A unique exact count/wage partition supports the inferred comparison.

| Code | Reported payroll | Verified CSV payroll | Difference (verified minus reported) |
| --- | --- | --- | --- |
| C-110 | 161905.60 | 43905.60 | -118000.00 |
| E-510 | 306024.85 | 426184.85 | 120160.00 |

| Control | Reconciled | Original basis | Unresolved amount |
| --- | --- | --- | --- |
| allocation | True | 467930.45 | 0.00 |
| independent | True | 467930.45 | 0.00 |
| adjustments | True | 9224.00 | 390.00 |
| travel | True | 467930.45 | see review state |

Supporting source IDs (local to this employer; exact locators below): S0233, S0234.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q016 — Business, actual-duty observations and audit-period completeness

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E05-Q016](audit-questions.md#e05-q016).

Classification depends on actual work and complete period evidence; job titles and the submitted application alone do not establish a code.

Supporting source IDs (local to this employer; exact locators below): S0005, S0006, S0232.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E05-Q017 — Company-rule applicability — auditor confirmation

**AUDITOR APPROVAL / EMPLOYER FACT CONFIRMATION**. Follow-up: [E05-Q017](audit-questions.md#e05-q017).

Contractor-specific practices cannot be extended to unrelated industries; proposals are not verified rules or allocations.

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0228, S0229, S0230, S0231.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

<details>
<summary>Source and rule index — 234 exact citations</summary>

Original Classification Guide paragraph identifiers and interview timestamps/line spans are preserved here. Rule applicability is bounded by the recorded decision; a citation is not permission to extend a contractor practice to another business. Physical CSV row identities and confirmation links are preserved in the question document's record index.

| Source ID | Original document | Original paragraph / interview / record locator | Lines |
| --- | --- | --- | --- |
| S0001 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | CSV line 2 | 2-2 |
| S0002 | /home/maxg/insurance01-inputs/classification-guide.md | CG-02 | 15-16 |
| S0003 | /home/maxg/insurance01-inputs/classification-guide.md | CG-21 | 48-49 |
| S0004 | /home/maxg/insurance01-inputs/classification-guide.md | CG-05 | 21-22 |
| S0005 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/business-description.md | business description | 1-7 |
| S0006 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/field-notes.md | auditor field notes | 1-6 |
| S0007 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | examined site sign-in log | 1-215 |
| S0008 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 2 | 2-2 |
| S0009 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 3 | 3-3 |
| S0010 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 4 | 4-4 |
| S0011 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 5 | 5-5 |
| S0012 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 6 | 6-6 |
| S0013 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 7 | 7-7 |
| S0014 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 8 | 8-8 |
| S0015 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 9 | 9-9 |
| S0016 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 10 | 10-10 |
| S0017 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 11 | 11-11 |
| S0018 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 12 | 12-12 |
| S0019 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 13 | 13-13 |
| S0020 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 14 | 14-14 |
| S0021 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 15 | 15-15 |
| S0022 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 16 | 16-16 |
| S0023 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 17 | 17-17 |
| S0024 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 18 | 18-18 |
| S0025 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 19 | 19-19 |
| S0026 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 20 | 20-20 |
| S0027 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 21 | 21-21 |
| S0028 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 22 | 22-22 |
| S0029 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 23 | 23-23 |
| S0030 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 24 | 24-24 |
| S0031 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 25 | 25-25 |
| S0032 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 26 | 26-26 |
| S0033 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 27 | 27-27 |
| S0034 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 28 | 28-28 |
| S0035 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 29 | 29-29 |
| S0036 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 30 | 30-30 |
| S0037 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 31 | 31-31 |
| S0038 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 32 | 32-32 |
| S0039 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 33 | 33-33 |
| S0040 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 34 | 34-34 |
| S0041 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 35 | 35-35 |
| S0042 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 36 | 36-36 |
| S0043 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 37 | 37-37 |
| S0044 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 38 | 38-38 |
| S0045 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 39 | 39-39 |
| S0046 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 40 | 40-40 |
| S0047 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 41 | 41-41 |
| S0048 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 42 | 42-42 |
| S0049 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 43 | 43-43 |
| S0050 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 44 | 44-44 |
| S0051 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 45 | 45-45 |
| S0052 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 46 | 46-46 |
| S0053 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 47 | 47-47 |
| S0054 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 48 | 48-48 |
| S0055 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 49 | 49-49 |
| S0056 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 50 | 50-50 |
| S0057 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 51 | 51-51 |
| S0058 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 52 | 52-52 |
| S0059 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 53 | 53-53 |
| S0060 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 54 | 54-54 |
| S0061 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 55 | 55-55 |
| S0062 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 56 | 56-56 |
| S0063 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 57 | 57-57 |
| S0064 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 58 | 58-58 |
| S0065 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 59 | 59-59 |
| S0066 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 60 | 60-60 |
| S0067 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 61 | 61-61 |
| S0068 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 62 | 62-62 |
| S0069 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 63 | 63-63 |
| S0070 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 64 | 64-64 |
| S0071 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 65 | 65-65 |
| S0072 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 66 | 66-66 |
| S0073 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 67 | 67-67 |
| S0074 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 68 | 68-68 |
| S0075 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 69 | 69-69 |
| S0076 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 70 | 70-70 |
| S0077 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 71 | 71-71 |
| S0078 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 72 | 72-72 |
| S0079 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 73 | 73-73 |
| S0080 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 74 | 74-74 |
| S0081 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 75 | 75-75 |
| S0082 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 76 | 76-76 |
| S0083 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 77 | 77-77 |
| S0084 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 78 | 78-78 |
| S0085 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 79 | 79-79 |
| S0086 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 80 | 80-80 |
| S0087 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 81 | 81-81 |
| S0088 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 82 | 82-82 |
| S0089 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 83 | 83-83 |
| S0090 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 84 | 84-84 |
| S0091 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 85 | 85-85 |
| S0092 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 86 | 86-86 |
| S0093 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 87 | 87-87 |
| S0094 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 88 | 88-88 |
| S0095 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 89 | 89-89 |
| S0096 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 90 | 90-90 |
| S0097 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 91 | 91-91 |
| S0098 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 92 | 92-92 |
| S0099 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 93 | 93-93 |
| S0100 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 94 | 94-94 |
| S0101 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 95 | 95-95 |
| S0102 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 96 | 96-96 |
| S0103 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 97 | 97-97 |
| S0104 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 98 | 98-98 |
| S0105 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 99 | 99-99 |
| S0106 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 100 | 100-100 |
| S0107 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 101 | 101-101 |
| S0108 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 102 | 102-102 |
| S0109 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 103 | 103-103 |
| S0110 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 104 | 104-104 |
| S0111 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 105 | 105-105 |
| S0112 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 106 | 106-106 |
| S0113 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 107 | 107-107 |
| S0114 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 108 | 108-108 |
| S0115 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 109 | 109-109 |
| S0116 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 110 | 110-110 |
| S0117 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 111 | 111-111 |
| S0118 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 112 | 112-112 |
| S0119 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 113 | 113-113 |
| S0120 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 114 | 114-114 |
| S0121 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 115 | 115-115 |
| S0122 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 116 | 116-116 |
| S0123 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 117 | 117-117 |
| S0124 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 118 | 118-118 |
| S0125 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 119 | 119-119 |
| S0126 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 120 | 120-120 |
| S0127 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 121 | 121-121 |
| S0128 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 122 | 122-122 |
| S0129 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 123 | 123-123 |
| S0130 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 124 | 124-124 |
| S0131 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 125 | 125-125 |
| S0132 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 126 | 126-126 |
| S0133 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 127 | 127-127 |
| S0134 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 128 | 128-128 |
| S0135 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 129 | 129-129 |
| S0136 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 130 | 130-130 |
| S0137 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 131 | 131-131 |
| S0138 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 132 | 132-132 |
| S0139 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 133 | 133-133 |
| S0140 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 134 | 134-134 |
| S0141 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 135 | 135-135 |
| S0142 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 136 | 136-136 |
| S0143 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 137 | 137-137 |
| S0144 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 138 | 138-138 |
| S0145 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 139 | 139-139 |
| S0146 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 140 | 140-140 |
| S0147 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 141 | 141-141 |
| S0148 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 142 | 142-142 |
| S0149 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 143 | 143-143 |
| S0150 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 144 | 144-144 |
| S0151 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 145 | 145-145 |
| S0152 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 146 | 146-146 |
| S0153 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 147 | 147-147 |
| S0154 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 148 | 148-148 |
| S0155 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 149 | 149-149 |
| S0156 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 150 | 150-150 |
| S0157 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 151 | 151-151 |
| S0158 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 152 | 152-152 |
| S0159 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 153 | 153-153 |
| S0160 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 154 | 154-154 |
| S0161 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 155 | 155-155 |
| S0162 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 156 | 156-156 |
| S0163 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 157 | 157-157 |
| S0164 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 158 | 158-158 |
| S0165 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 159 | 159-159 |
| S0166 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 160 | 160-160 |
| S0167 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 161 | 161-161 |
| S0168 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 162 | 162-162 |
| S0169 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 163 | 163-163 |
| S0170 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 164 | 164-164 |
| S0171 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 165 | 165-165 |
| S0172 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 166 | 166-166 |
| S0173 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 167 | 167-167 |
| S0174 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 168 | 168-168 |
| S0175 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 169 | 169-169 |
| S0176 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 170 | 170-170 |
| S0177 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 171 | 171-171 |
| S0178 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 172 | 172-172 |
| S0179 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 173 | 173-173 |
| S0180 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 174 | 174-174 |
| S0181 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 175 | 175-175 |
| S0182 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 176 | 176-176 |
| S0183 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 177 | 177-177 |
| S0184 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 178 | 178-178 |
| S0185 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 179 | 179-179 |
| S0186 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 180 | 180-180 |
| S0187 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 181 | 181-181 |
| S0188 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 182 | 182-182 |
| S0189 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 183 | 183-183 |
| S0190 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 184 | 184-184 |
| S0191 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 185 | 185-185 |
| S0192 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 186 | 186-186 |
| S0193 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 187 | 187-187 |
| S0194 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 188 | 188-188 |
| S0195 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 189 | 189-189 |
| S0196 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 190 | 190-190 |
| S0197 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 191 | 191-191 |
| S0198 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 192 | 192-192 |
| S0199 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 193 | 193-193 |
| S0200 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 194 | 194-194 |
| S0201 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 195 | 195-195 |
| S0202 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 196 | 196-196 |
| S0203 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 197 | 197-197 |
| S0204 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 198 | 198-198 |
| S0205 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 199 | 199-199 |
| S0206 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 200 | 200-200 |
| S0207 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 201 | 201-201 |
| S0208 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 202 | 202-202 |
| S0209 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 203 | 203-203 |
| S0210 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 204 | 204-204 |
| S0211 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 205 | 205-205 |
| S0212 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 206 | 206-206 |
| S0213 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 207 | 207-207 |
| S0214 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 208 | 208-208 |
| S0215 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 209 | 209-209 |
| S0216 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 210 | 210-210 |
| S0217 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 211 | 211-211 |
| S0218 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 212 | 212-212 |
| S0219 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 213 | 213-213 |
| S0220 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 214 | 214-214 |
| S0221 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | CSV line 215 | 215-215 |
| S0222 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | CSV line 3 | 3-3 |
| S0223 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | CSV line 4 | 4-4 |
| S0224 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | CSV line 5 | 5-5 |
| S0225 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | CSV line 6 | 6-6 |
| S0226 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | CSV line 7 | 7-7 |
| S0227 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | CSV line 8 | 8-8 |
| S0228 | /home/maxg/insurance01-inputs/classification-guide.md | CG-04 | 32-34 |
| S0229 | /home/maxg/insurance01-inputs/classification-guide.md | CG-03 | 18-19 |
| S0230 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:05 PM | 185-187 |
| S0231 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:09 PM | 609-611 |
| S0232 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/field-notes.md | documented flat daily allowance and additional wage basis | 1-6 |
| S0233 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/application.md | application class E-510 | 7-7 |
| S0234 | /home/maxg/insurance01-inputs/employer-files/patuxent-electric/application.md | application class C-110 | 8-8 |

| Original source file | SHA-256 |
| --- | --- |
| /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160 |
| /home/maxg/insurance01-inputs/classification-guide.md | 89480f691737a0e8a762a836b8412476e0ed9d0b37639eb898e2826771c1dba8 |
| /home/maxg/insurance01-inputs/employer-files/patuxent-electric/application.md | 55f0c7b086ac550f0f8b98a9d22aa906ffe4005e2c8259fd5d9fe72e2d2bd07e |
| /home/maxg/insurance01-inputs/employer-files/patuxent-electric/business-description.md | ab025cd6d057708188e0060ef2309e64e990cdbbb25e4fe97402af6cf5434bfd |
| /home/maxg/insurance01-inputs/employer-files/patuxent-electric/field-notes.md | 6055df5e294c902b884ece23e30a9b424f3f1df801e5c97c39eb12b93453d72e |
| /home/maxg/insurance01-inputs/employer-files/patuxent-electric/payroll-register.csv | 1dd09ea917394706df1c0166ba3869cdb20820b0e7605c500d0a11d3f6263e71 |
| /home/maxg/insurance01-inputs/employer-files/patuxent-electric/site-signin-log.csv | 49e585c8512862c1959eefb431419d416e3bf236f0b4004347a4e7bfcc1195b6 |

</details>

<a id="e06"></a>
## Severn Homebuilders (severn-homebuilders)

Audit period: 2025-07-07 through 2026-07-05. Submitted split: **PARTIALLY UNRESOLVED**.

Verified corrections and supported components are shown below; the full submitted split cannot yet be accepted. Differences are a **provisional comparison** of verified CSV payroll minus reported payroll. An OPEN wage omission is **not a verified payroll reduction**; unresolved payment basis may change the final allocation after evidence and approval.

Verified-only CSV: /home/maxg/ch03-premium-audit/deliverables/codes/severn-homebuilders.csv; SHA-256 4dd5979377d949d81c05d6f7d46eaa78832702aa47721312b61932691d6549f5.

| Code | Reported payroll | Verified payroll | Difference (verified minus reported) | Verified code paragraph |
| --- | --- | --- | --- | --- |
| C-110 | 177209.40 | 46118.25 | -131091.15 | CG-04 |
| H-420 | 284670.30 | 369204.39 | 84534.09 | CG-15 |

Reported total $461879.70; original register $461879.70; register-minus-reported difference $0.00. Comparison definitive for current classifications: False (not human approval).

Application reported employee counts: H-420: 5; C-110: 3. Register employees: 8.

Application sources: S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110).

### Employee payroll — VERIFIED and OPEN

| Employee ID | Name | Original wages | VERIFIED wage allocation | VERIFIED additions | OPEN wages | Register source |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E01 | Garrett Holm | 66315.40 | H-420 66315.40 | — | 0.00 | S0001 payroll-register.csv:2-2 (CSV line 2) |
| SH-E02 | Victor Amadi | 62780.15 | H-420 62780.15 | — | 0.00 | S0006 payroll-register.csv:3-3 (CSV line 3) |
| SH-E03 | Peter Kowal | 58442.60 | H-420 58442.60 | — | 0.00 | S0007 payroll-register.csv:4-4 (CSV line 4) |
| SH-E04 | Andre Sutton | 49905.85 | H-420 49905.85 | — | 0.00 | S0008 payroll-register.csv:5-5 (CSV line 5) |
| SH-E05 | Colin Rusk | 47226.30 | H-420 47226.30 | — | 0.00 | S0009 payroll-register.csv:6-6 (CSV line 6) |
| SH-E06 | Marissa Gale | 71250.45 | — | — | 71250.45 | S0010 payroll-register.csv:7-7 (CSV line 7) |
| SH-E07 | Dana Whitcomb | 59840.70 | H-420 59840.70 | — | 0.00 | S0029 payroll-register.csv:8-8 (CSV line 8) |
| SH-E08 | Helen Ostrow | 46118.25 | C-110 46118.25 | — | 0.00 | S0041 payroll-register.csv:9-9 (CSV line 9) |

Employee-level application assignments below are marked inferred where the engine derives them from the submitted counts/payroll; they are not employer-supplied employee coding lists.

| Employee | Wage basis | Reported code | Calculated code | Status | Reported attribution | Reason / records |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E01 Garrett Holm | 66315.40 | H-420 | H-420 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0001 payroll-register.csv:2-2 (CSV line 2); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |
| SH-E02 Victor Amadi | 62780.15 | H-420 | H-420 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0006 payroll-register.csv:3-3 (CSV line 3); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |
| SH-E03 Peter Kowal | 58442.60 | H-420 | H-420 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0007 payroll-register.csv:4-4 (CSV line 4); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |
| SH-E04 Andre Sutton | 49905.85 | H-420 | H-420 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0008 payroll-register.csv:5-5 (CSV line 5); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |
| SH-E05 Colin Rusk | 47226.30 | H-420 | H-420 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0009 payroll-register.csv:6-6 (CSV line 6); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |
| SH-E06 Marissa Gale | 71250.45 | C-110 | OPEN | OPEN | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0010 payroll-register.csv:7-7 (CSV line 7); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |
| SH-E07 Dana Whitcomb | 59840.70 | C-110 | H-420 | CHANGE | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0029 payroll-register.csv:8-8 (CSV line 8); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |
| SH-E08 Helen Ostrow | 46118.25 | C-110 | C-110 | UNCHANGED | INFERRED — confirm | Reported code is inferred from a unique exact application headcount/wage partition; employer confirmation is required. S0041 payroll-register.csv:9-9 (CSV line 9); S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110) |

### Applied rule boundaries

Each decision retains the existing evaluator's scope and conditions. OPEN decisions below describe an applicability/evidence gap, not an assigned classification. Payment rule reasons and exact references are also preserved with each adjustment.

| Rule | Decision status | Scope | Applicability boundaries | Exact rule sources |
| --- | --- | --- | --- | --- |
| documented_homebuilding_work | CLASSIFIED | whole_audit_period | documented construction/trade work; verified current guide definition | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:44-46 (CG-15) |
| employer_evidence | OPEN | whole_audit_period | documented actual duties and audit period | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:44-46 (CG-15); S0011 classification-guide.md:32-34 (CG-04); S0012 ch03-premium-audit-20261105-0222(1).md:153-155 (Nadia Brennan · 06:03 PM); S0013 ch03-premium-audit-20261105-0222(1).md:305-307 (Nadia Brennan · 06:10 PM); S0014 ch03-premium-audit-20261105-0222(1).md:545-547 (Nadia Brennan · 09:06 PM) |
| contractor_office_visits | CLASSIFIED | whole_audit_period | contractor employer; office employee by actual duties; complete audit-period site sign-in evidence; five or more days requires an evidenced unique governing field code | S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:44-46 (CG-15); S0011 classification-guide.md:32-34 (CG-04); S0012 ch03-premium-audit-20261105-0222(1).md:153-155 (Nadia Brennan · 06:03 PM); S0013 ch03-premium-audit-20261105-0222(1).md:305-307 (Nadia Brennan · 06:10 PM); S0014 ch03-premium-audit-20261105-0222(1).md:545-547 (Nadia Brennan · 09:06 PM) |
| documented_homebuilding_work | CLASSIFIED | whole_audit_period | documented construction/trade work; verified current guide definition | S0002 classification-guide.md:15-16 (CG-02); S0053 classification-guide.md:36-37 (CG-11) |

### Reconciliation and excluded payments

Employee reconciliation (original register + verified additions = verified classified payroll + OPEN wages):

`461879.70 + 24693.39 = 415322.64 + 71250.45`; difference 0.00.

Known payroll basis (includes OPEN wages): $486573.09. Verified classified payroll: $415322.64.

Payment reconciliation (evaluated payment basis = verified addition + nonpayroll + OPEN payment basis):

`152117.05 = 24693.39 + 81478.01 + 45945.65`; difference 0.00.

Cash reconciliation (original wages + evaluated payments = verified payroll + OPEN wages + excluded/nonpayroll payments + OPEN payment basis):

`613996.75 = 415322.64 + 71250.45 + 81478.01 + 45945.65`; difference 0.00.

| Engine control | Reconciled | Difference |
| --- | --- | --- |
| allocation | True | 0.00 |
| independent | True | 0.00 |
| adjustments | True | 0.00 |
| combined | True | 0.00 |

Owner Martin Severn: **EXCLUDED**; removed register wages $0.00. The business record documents a filed exclusion election and no owner wage appears in the register. Records: S0054 business-description.md:1-7 (owner election statement); S0055 classification-guide.md:21-22 (CG-05).

Governing field code: H-420; supported field payroll H-420 284670.30. Verified own-crew H-420 wages exceed even the full recorded competing trade payment basis; office wages are excluded to avoid circular assignment. Exact evidence and rule references follow in the review detail and source index.

### OPEN findings and required human resolution

Each finding remains unanswered even if its monetary effect is zero. Employer payroll/records contact supplies the requested records; responsible policy reviewer: auditor. Identity issues require documentary confirmation of the exact employee/payee, not an assumed alias.

- **OPEN — Unattributed site sign-ins**: No employee identity is assumed for unmatched sign-ins; dates provide possible-visit bounds only. Required evidence/confirmation: Confirm whether the unmatched entries are nonpayroll visitors and correct any missing employee identities. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E06-Q016](audit-questions.md#e06-q016). Records: S0020 site-signin-log.csv:8-8 (CSV line 8).

- **OPEN — Marissa Gale [SH-E06]**: Office visit bounds or the governing field code do not establish one verified classification. 4 distinct job-site days is at most four in the audit period. 5 distinct job-site days is at least five; use the evidenced governing field code for the whole audit period. Required evidence/confirmation: Auditor or employer must confirm: Office visit bounds or the governing field code do not establish one verified classification. 4 distinct job-site days is at most four in the audit period. 5 distinct job-site days is at least five; use the evidenced governing field code for the whole audit period. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E06-Q006](audit-questions.md#e06-q006). Records: S0001 payroll-register.csv:2-2 (CSV line 2); S0002 classification-guide.md:15-16 (CG-02); S0003 classification-guide.md:44-46 (CG-15); S0004 business-description.md:1-7 (business description); S0005 field-notes.md:1-8 (auditor field notes); S0006 payroll-register.csv:3-3 (CSV line 3); S0007 payroll-register.csv:4-4 (CSV line 4); S0008 payroll-register.csv:5-5 (CSV line 5); S0009 payroll-register.csv:6-6 (CSV line 6); S0010 payroll-register.csv:7-7 (CSV line 7); S0011 classification-guide.md:32-34 (CG-04); S0012 ch03-premium-audit-20261105-0222(1).md:153-155 (Nadia Brennan · 06:03 PM); S0013 ch03-premium-audit-20261105-0222(1).md:305-307 (Nadia Brennan · 06:10 PM); S0014 ch03-premium-audit-20261105-0222(1).md:545-547 (Nadia Brennan · 09:06 PM); S0015 site-signin-log.csv:1-17 (examined audit-period site sign-in log); S0016 site-signin-log.csv:2-2 (CSV line 2); S0017 site-signin-log.csv:11-11 (CSV line 11); S0018 site-signin-log.csv:14-14 (CSV line 14); S0019 site-signin-log.csv:15-15 (CSV line 15); S0020 site-signin-log.csv:8-8 (CSV line 8); S0021 subcontractor-payments.csv:2-2 (CSV line 2); S0022 subcontractor-payments.csv:3-3 (CSV line 3); S0023 subcontractor-payments.csv:4-4 (CSV line 4); S0024 subcontractor-payments.csv:5-5 (CSV line 5); S0025 subcontractor-payments.csv:6-6 (CSV line 6); S0026 subcontractor-payments.csv:7-7 (CSV line 7); S0027 subcontractor-payments.csv:8-8 (CSV line 8); S0028 subcontractor-payments.csv:9-9 (CSV line 9).

- **OPEN — SV-KEN-01**: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Required evidence/confirmation: Auditor or employer must confirm Kent Island Roofing, record SV-KEN-01: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E06-Q010](audit-questions.md#e06-q010). Records: S0022 subcontractor-payments.csv:3-3 (CSV line 3); S0042 classification-guide.md:24-25 (CG-06); S0043 ch03-premium-audit-20261105-0222(1).md:369-371 (Nadia Brennan · 06:12 PM); S0044 ch03-premium-audit-20261105-0222(1).md:377-379 (Nadia Brennan · 06:12 PM); S0045 ch03-premium-audit-20261105-0222(1).md:577-579 (Nadia Brennan · 09:08 PM); S0046 ch03-premium-audit-20261105-0222(1).md:601-603 (Nadia Brennan · 09:09 PM); S0047 insurance-certificates.csv:3-3 (CSV line 3); S0048 insurance-certificates.csv:1-3 (complete supplied certificate inventory); S0049 field-notes.md:1-8 (subcontractor field observations).

- **OPEN — SV-KEN-02**: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Required evidence/confirmation: Auditor or employer must confirm Kent Island Roofing, record SV-KEN-02: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E06-Q010](audit-questions.md#e06-q010). Records: S0026 subcontractor-payments.csv:7-7 (CSV line 7); S0042 classification-guide.md:24-25 (CG-06); S0043 ch03-premium-audit-20261105-0222(1).md:369-371 (Nadia Brennan · 06:12 PM); S0044 ch03-premium-audit-20261105-0222(1).md:377-379 (Nadia Brennan · 06:12 PM); S0045 ch03-premium-audit-20261105-0222(1).md:577-579 (Nadia Brennan · 09:08 PM); S0046 ch03-premium-audit-20261105-0222(1).md:601-603 (Nadia Brennan · 09:09 PM); S0047 insurance-certificates.csv:3-3 (CSV line 3); S0048 insurance-certificates.csv:1-3 (complete supplied certificate inventory); S0049 field-notes.md:1-8 (subcontractor field observations).

- **OPEN — SV-KEN-03**: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Required evidence/confirmation: Auditor or employer must confirm Kent Island Roofing, record SV-KEN-03: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E06-Q010](audit-questions.md#e06-q010). Records: S0028 subcontractor-payments.csv:9-9 (CSV line 9); S0042 classification-guide.md:24-25 (CG-06); S0043 ch03-premium-audit-20261105-0222(1).md:369-371 (Nadia Brennan · 06:12 PM); S0044 ch03-premium-audit-20261105-0222(1).md:377-379 (Nadia Brennan · 06:12 PM); S0045 ch03-premium-audit-20261105-0222(1).md:577-579 (Nadia Brennan · 09:08 PM); S0046 ch03-premium-audit-20261105-0222(1).md:601-603 (Nadia Brennan · 09:09 PM); S0047 insurance-certificates.csv:3-3 (CSV line 3); S0048 insurance-certificates.csv:1-3 (complete supplied certificate inventory); S0049 field-notes.md:1-8 (subcontractor field observations).

- **OPEN — Application/classification comparison**: The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved. Required evidence/confirmation: Confirm the evidence-backed classification changes and resolve pending employee decisions; the application is not classification authority. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E06-Q012](audit-questions.md#e06-q012). Records: S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110).

- **OPEN — Application employee attribution**: Employee assignments are not explicitly listed on the application. A unique exact count/wage partition supports the inferred comparison. Required evidence/confirmation: Confirm the employer's employee-level reported codes; classification decisions remain based on work records. Responsible fact reviewer: employer payroll/records contact; responsible policy reviewer: auditor. Questions: [E06-Q012](audit-questions.md#e06-q012). Records: S0050 application.md:7-7 (application class H-420); S0051 application.md:8-8 (application class C-110).

### UNAPPROVED PROPOSED treatments

These alternatives are outside all verified totals. They require the specific evidence below and explicit auditor approval, followed by a supported rerun.

- **UNAPPROVED — SH-E06**: Candidate C-110; wage basis $71250.45; paragraph CG-04. Conditional treatment using only confirmed visits, pending identity/completeness confirmation; not a verified allocation. Required confirmation: Auditor or employer must confirm: Office visit bounds or the governing field code do not establish one verified classification. 4 distinct job-site days is at most four in the audit period. 5 distinct job-site days is at least five; use the evidenced governing field code for the whole audit period. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E06-Q006](audit-questions.md#e06-q006).

- **UNAPPROVED — SV-KEN-01**: Candidate R-310; proposed payroll $8580.00; proposed nonpayroll $5720.00. Conditional missing-full-period-coverage treatment only; confirm payee/certificate identity and any replacement coverage. This proposal contributes no verified payroll. Required confirmation: Auditor or employer must confirm Kent Island Roofing, record SV-KEN-01: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E06-Q010](audit-questions.md#e06-q010).

- **UNAPPROVED — SV-KEN-02**: Candidate R-310; proposed payroll $11928.27; proposed nonpayroll $7952.18. Conditional missing-full-period-coverage treatment only; confirm payee/certificate identity and any replacement coverage. This proposal contributes no verified payroll. Required confirmation: Auditor or employer must confirm Kent Island Roofing, record SV-KEN-02: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E06-Q010](audit-questions.md#e06-q010).

- **UNAPPROVED — SV-KEN-03**: Candidate R-310; proposed payroll $7059.12; proposed nonpayroll $4706.08. Conditional missing-full-period-coverage treatment only; confirm payee/certificate identity and any replacement coverage. This proposal contributes no verified payroll. Required confirmation: Auditor or employer must confirm Kent Island Roofing, record SV-KEN-03: Certificate/payee names do not match exactly; confirm identity without assuming a name alias. Responsible policy reviewer: auditor; employer payroll/records contact supplies evidence. Questions: [E06-Q010](audit-questions.md#e06-q010).

### Allocation, payment and evidence review detail

The following entries preserve each employee/pay week, adjustment/payment, deciding reason and record confirmation. VERIFIED calculations, OPEN findings and UNAPPROVED alternatives retain their original labels. Exact dated record fields and all confirmation prompts are in the linked question document.

#### E06-Q001 — Garrett Holm [SH-E01]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q001](audit-questions.md#e06-q001).

Verified base-wage allocation: H-420 $66315.40. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented carpentry duties fall within the verified CG-15 definition.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E01 | audit period | audit period | 66315.40 | H-420 | CG-15 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q002 — Victor Amadi [SH-E02]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q002](audit-questions.md#e06-q002).

Verified base-wage allocation: H-420 $62780.15. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented carpentry duties fall within the verified CG-15 definition.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E02 | audit period | audit period | 62780.15 | H-420 | CG-15 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0006, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q003 — Peter Kowal [SH-E03]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q003](audit-questions.md#e06-q003).

Verified base-wage allocation: H-420 $58442.60. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented carpentry duties fall within the verified CG-15 definition.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E03 | audit period | audit period | 58442.60 | H-420 | CG-15 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0007, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q004 — Andre Sutton [SH-E04]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q004](audit-questions.md#e06-q004).

Verified base-wage allocation: H-420 $49905.85. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented general labor duties fall within the verified CG-15 definition.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E04 | audit period | audit period | 49905.85 | H-420 | CG-15 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0008, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q005 — Colin Rusk [SH-E05]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q005](audit-questions.md#e06-q005).

Verified base-wage allocation: H-420 $47226.30. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Documented general labor duties fall within the verified CG-15 definition.

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E05 | audit period | audit period | 47226.30 | H-420 | CG-15 | — |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0004, S0005, S0009, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q006 — Marissa Gale [SH-E06]

**OPEN / HUMAN APPROVAL REQUIRED**. Follow-up: [E06-Q006](audit-questions.md#e06-q006).

Verified base-wage allocation: none. OPEN base wages: $71250.45; OPEN wages are excluded from CSV totals.

Office visit bounds or the governing field code do not establish one verified classification. 4 distinct job-site days is at most four in the audit period. 5 distinct job-site days is at least five; use the evidenced governing field code for the whole audit period.

Confirmed distinct site-visit dates: 2025-07-24, 2026-01-16, 2026-03-24, 2026-04-21. Unattributed rows remain unassigned; confirm completeness separately.

UNAPPROVED alternatives from the cited office-visit rule: candidate C-110 using only 4 confirmed dates; governing field code H-420 only if human confirmation establishes the additional visit evidence (up to 5 distinct dates) and the rule applies. Both the identity and resulting treatment require approval; the unmatched record is not attributed.

UNAPPROVED PROPOSAL for SH-E06: Conditional treatment using only confirmed visits, pending identity/completeness confirmation; not a verified allocation.

| Unattributed source record | Date | Original employee ID | Original name | Site |
| --- | --- | --- | --- | --- |
| site-signin-log.csv:8 | 2025-12-02 | BLANK / UNATTRIBUTED | County inspector | Lot 7 Mill Pond Rd |

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E06 | audit period | audit period | 71250.45 | OPEN | OPEN | — |

| Proposal subject | Candidate code | Wage basis | Approval |
| --- | --- | --- | --- |
| SH-E06 | C-110 | 71250.45 | UNAPPROVED; excluded from CSV |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0010, S0011, S0012, S0013, S0014, S0015, S0016, S0017, S0018, S0019, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q007 — Dana Whitcomb [SH-E07]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q007](audit-questions.md#e06-q007).

Verified base-wage allocation: H-420 $59840.70. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Between 11 confirmed and 12 possible distinct site days; both bounds return H-420. 11 distinct job-site days is at least five; use the evidenced governing field code for the whole audit period.

Confirmed distinct site-visit dates: 2025-09-17, 2025-09-19, 2025-10-02, 2025-10-17, 2025-11-14, 2026-01-08, 2026-01-14, 2026-01-16, 2026-03-04, 2026-06-16, 2026-06-23. Unattributed rows remain unassigned; confirm completeness separately.

| Unattributed source record | Date | Original employee ID | Original name | Site |
| --- | --- | --- | --- | --- |
| site-signin-log.csv:8 | 2025-12-02 | BLANK / UNATTRIBUTED | County inspector | Lot 7 Mill Pond Rd |

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E07 | audit period | audit period | 59840.70 | H-420 | CG-15 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0011, S0012, S0013, S0014, S0015, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0029, S0030, S0031, S0032, S0033, S0034, S0035, S0036, S0037, S0038, S0039, S0040, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q008 — Helen Ostrow [SH-E08]

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q008](audit-questions.md#e06-q008).

Verified base-wage allocation: C-110 $46118.25. OPEN base wages: $0.00; OPEN wages are excluded from CSV totals.

Between 0 confirmed and 1 possible distinct site days; both bounds return C-110. 0 distinct job-site days is at most four in the audit period.

Confirmed distinct site-visit dates: none recorded. Unattributed rows remain unassigned; confirm completeness separately.

| Unattributed source record | Date | Original employee ID | Original name | Site |
| --- | --- | --- | --- | --- |
| site-signin-log.csv:8 | 2025-12-02 | BLANK / UNATTRIBUTED | County inspector | Lot 7 Mill Pond Rd |

| Payroll part | Week start | Week end | Wages | Result | Paragraph | Ride dates (inside rule only) |
| --- | --- | --- | --- | --- | --- | --- |
| SH-E08 | audit period | audit period | 46118.25 | C-110 | CG-04 | — |

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0011, S0012, S0013, S0014, S0015, S0020, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0041, S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q009 — Tenbury Ridge Framing Co.

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q009](audit-questions.md#e06-q009).

An exactly named certificate covers the entire audit period, including both endpoints.

Verified payroll addition $0.00; verified nonpayroll $65015.75; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SV-TRF-01 | 2025-08-22 | 21480.00 | — | 0.00 | 21480.00 | 0.00 | — no payroll allocation | VERIFIED |
| SV-TRF-02 | 2025-11-14 | 18925.50 | — | 0.00 | 18925.50 | 0.00 | — no payroll allocation | VERIFIED |
| SV-TRF-03 | 2026-04-03 | 24610.25 | — | 0.00 | 24610.25 | 0.00 | — no payroll allocation | VERIFIED |

| Certificate entity | Certificate number | Coverage from | Coverage through |
| --- | --- | --- | --- |
| Tenbury Ridge Framing Co. | MD-WC-448201 | 2025-06-01 | 2026-12-31 |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0021, S0024, S0027, S0042, S0043, S0044, S0045, S0046, S0048, S0049, S0052.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q010 — Kent Island Roofing

**OPEN / HUMAN APPROVAL REQUIRED**. Follow-up: [E06-Q010](audit-questions.md#e06-q010).

Certificate/payee names do not match exactly; confirm identity without assuming a name alias.

Verified payroll addition $0.00; verified nonpayroll $0.00; OPEN payment basis $45945.65. OPEN basis is not itself an assigned payroll amount.

UNAPPROVED PROPOSAL for SV-KEN-01: Conditional missing-full-period-coverage treatment only; confirm payee/certificate identity and any replacement coverage. This proposal contributes no verified payroll.

UNAPPROVED PROPOSAL for SV-KEN-02: Conditional missing-full-period-coverage treatment only; confirm payee/certificate identity and any replacement coverage. This proposal contributes no verified payroll.

UNAPPROVED PROPOSAL for SV-KEN-03: Conditional missing-full-period-coverage treatment only; confirm payee/certificate identity and any replacement coverage. This proposal contributes no verified payroll.

UNAPPROVED PROPOSAL total payroll addition: $27567.39; not in verified CSV totals.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SV-KEN-01 | 2025-09-12 | 14300.00 | — | 0.00 | 0.00 | 14300.00 | OPEN | OPEN |
| SV-KEN-02 | 2026-03-20 | 19880.45 | — | 0.00 | 0.00 | 19880.45 | OPEN | OPEN |
| SV-KEN-03 | 2026-05-08 | 11765.20 | — | 0.00 | 0.00 | 11765.20 | OPEN | OPEN |

| Certificate entity | Certificate number | Coverage from | Coverage through |
| --- | --- | --- | --- |
| Kent Island Roofing & Siding LLC | MD-WC-517736 | 2025-04-01 | 2026-01-31 |

| Proposal payment | Candidate work code | Proposed payroll | Proposed nonpayroll | Approval |
| --- | --- | --- | --- | --- |
| SV-KEN-01 | R-310 | 8580.00 | 5720.00 | UNAPPROVED; excluded from CSV |

| Proposal payment | Candidate work code | Proposed payroll | Proposed nonpayroll | Approval |
| --- | --- | --- | --- | --- |
| SV-KEN-02 | R-310 | 11928.27 | 7952.18 | UNAPPROVED; excluded from CSV |

| Proposal payment | Candidate work code | Proposed payroll | Proposed nonpayroll | Approval |
| --- | --- | --- | --- | --- |
| SV-KEN-03 | R-310 | 7059.12 | 4706.08 | UNAPPROVED; excluded from CSV |

Supporting source IDs (local to this employer; exact locators below): S0002, S0022, S0026, S0028, S0042, S0043, S0044, S0045, S0046, S0047, S0048, S0049, S0053.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q011 — Tidewater Drywall

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q011](audit-questions.md#e06-q011).

Missing or incomplete/expired full-period certificate: include 60 percent of payments under the documented work code; do not prorate coverage.

Verified payroll addition $24693.39; verified nonpayroll $16462.26; OPEN payment basis $0.00. OPEN basis is not itself an assigned payroll amount.

| Payment / allowance ID | Date / period | Original amount | Days | Verified payroll | Nonpayroll | OPEN basis | Code | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SV-TID-01 | 2025-10-03 | 18240.55 | — | 10944.33 | 7296.22 | 0.00 | H-420 | VERIFIED |
| SV-TID-02 | 2026-02-27 | 22915.10 | — | 13749.06 | 9166.04 | 0.00 | H-420 | VERIFIED |

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0023, S0025, S0042, S0043, S0044, S0045, S0046, S0048, S0049.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q012 — Application split, employee attribution and payroll reconciliation

**VERIFIED CALCULATION + OPEN FINDING / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E06-Q012](audit-questions.md#e06-q012).

Reconciliation verifies arithmetic, not employer confirmation or approval. Verified CSVs exclude OPEN wages and every unapproved proposal.

Application comparison definitive for current classifications: False; this is not audit approval.

The verified allocation differs from the application or contains OPEN payroll; class differences are provisional while payroll remains unresolved.

Employee assignments are not explicitly listed on the application. A unique exact count/wage partition supports the inferred comparison.

| Code | Reported payroll | Verified CSV payroll | Difference (verified minus reported) |
| --- | --- | --- | --- |
| C-110 | 177209.40 | 46118.25 | -131091.15 |
| H-420 | 284670.30 | 369204.39 | 84534.09 |

| Control | Reconciled | Original basis | Unresolved amount |
| --- | --- | --- | --- |
| allocation | True | 461879.70 | 71250.45 |
| independent | True | 461879.70 | 71250.45 |
| adjustments | True | 152117.05 | 45945.65 |
| combined | True | 461879.70 | 71250.45 |

Supporting source IDs (local to this employer; exact locators below): S0050, S0051.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q013 — Business, actual-duty observations and audit-period completeness

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q013](audit-questions.md#e06-q013).

Classification depends on actual work and complete period evidence; job titles and the submitted application alone do not establish a code.

Verified own-crew H-420 wages exceed even the full recorded competing trade payment basis; office wages are excluded to avoid circular assignment.

Supporting source IDs (local to this employer; exact locators below): S0001, S0002, S0003, S0004, S0005, S0006, S0007, S0008, S0009, S0021, S0022, S0023, S0024, S0025, S0026, S0027, S0028, S0049, S0054.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q014 — Company-rule applicability — auditor confirmation

**AUDITOR APPROVAL / EMPLOYER FACT CONFIRMATION**. Follow-up: [E06-Q014](audit-questions.md#e06-q014).

Contractor-specific practices cannot be extended to unrelated industries; proposals are not verified rules or allocations.

Supporting source IDs (local to this employer; exact locators below): S0002, S0003, S0011, S0012, S0013, S0014, S0042, S0043, S0044, S0045, S0046, S0053, S0055.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q015 — Owner election — Martin Severn

**VERIFIED CALCULATION / EMPLOYER CONFIRMATION**. Follow-up: [E06-Q015](audit-questions.md#e06-q015).

The business record documents a filed exclusion election and no owner wage appears in the register.

Supporting source IDs (local to this employer; exact locators below): S0054, S0055.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

#### E06-Q016 — Unattributed site sign-ins

**OPEN / HUMAN CONFIRMATION REQUIRED**. Follow-up: [E06-Q016](audit-questions.md#e06-q016).

No employee identity is assumed for unmatched sign-ins; dates provide possible-visit bounds only.

| Original source record | Date | Original employee ID | Original name | Site |
| --- | --- | --- | --- | --- |
| site-signin-log.csv:8 | 2025-12-02 | BLANK / UNATTRIBUTED | County inspector | Lot 7 Mill Pond Rd |

Supporting source IDs (local to this employer; exact locators below): S0020.

Required evidence and approval: employer payroll/records contact confirms the linked original records and facts; the auditor resolves policy and any OPEN/proposed treatment. See the linked question for the specific unanswered prompts.

<details>
<summary>Source and rule index — 55 exact citations</summary>

Original Classification Guide paragraph identifiers and interview timestamps/line spans are preserved here. Rule applicability is bounded by the recorded decision; a citation is not permission to extend a contractor practice to another business. Physical CSV row identities and confirmation links are preserved in the question document's record index.

| Source ID | Original document | Original paragraph / interview / record locator | Lines |
| --- | --- | --- | --- |
| S0001 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 2 | 2-2 |
| S0002 | /home/maxg/insurance01-inputs/classification-guide.md | CG-02 | 15-16 |
| S0003 | /home/maxg/insurance01-inputs/classification-guide.md | CG-15 | 44-46 |
| S0004 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/business-description.md | business description | 1-7 |
| S0005 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/field-notes.md | auditor field notes | 1-8 |
| S0006 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 3 | 3-3 |
| S0007 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 4 | 4-4 |
| S0008 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 5 | 5-5 |
| S0009 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 6 | 6-6 |
| S0010 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 7 | 7-7 |
| S0011 | /home/maxg/insurance01-inputs/classification-guide.md | CG-04 | 32-34 |
| S0012 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:03 PM | 153-155 |
| S0013 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:10 PM | 305-307 |
| S0014 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:06 PM | 545-547 |
| S0015 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | examined audit-period site sign-in log | 1-17 |
| S0016 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 2 | 2-2 |
| S0017 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 11 | 11-11 |
| S0018 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 14 | 14-14 |
| S0019 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 15 | 15-15 |
| S0020 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 8 | 8-8 |
| S0021 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 2 | 2-2 |
| S0022 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 3 | 3-3 |
| S0023 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 4 | 4-4 |
| S0024 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 5 | 5-5 |
| S0025 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 6 | 6-6 |
| S0026 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 7 | 7-7 |
| S0027 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 8 | 8-8 |
| S0028 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | CSV line 9 | 9-9 |
| S0029 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 8 | 8-8 |
| S0030 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 3 | 3-3 |
| S0031 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 4 | 4-4 |
| S0032 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 5 | 5-5 |
| S0033 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 6 | 6-6 |
| S0034 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 7 | 7-7 |
| S0035 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 9 | 9-9 |
| S0036 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 10 | 10-10 |
| S0037 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 12 | 12-12 |
| S0038 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 13 | 13-13 |
| S0039 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 16 | 16-16 |
| S0040 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | CSV line 17 | 17-17 |
| S0041 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | CSV line 9 | 9-9 |
| S0042 | /home/maxg/insurance01-inputs/classification-guide.md | CG-06 | 24-25 |
| S0043 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:12 PM | 369-371 |
| S0044 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 06:12 PM | 377-379 |
| S0045 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:08 PM | 577-579 |
| S0046 | /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | Nadia Brennan · 09:09 PM | 601-603 |
| S0047 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/insurance-certificates.csv | CSV line 3 | 3-3 |
| S0048 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/insurance-certificates.csv | complete supplied certificate inventory | 1-3 |
| S0049 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/field-notes.md | subcontractor field observations | 1-8 |
| S0050 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/application.md | application class H-420 | 7-7 |
| S0051 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/application.md | application class C-110 | 8-8 |
| S0052 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/insurance-certificates.csv | CSV line 2 | 2-2 |
| S0053 | /home/maxg/insurance01-inputs/classification-guide.md | CG-11 | 36-37 |
| S0054 | /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/business-description.md | owner election statement | 1-7 |
| S0055 | /home/maxg/insurance01-inputs/classification-guide.md | CG-05 | 21-22 |

| Original source file | SHA-256 |
| --- | --- |
| /home/maxg/ch03-premium-audit/interviews/ch03-premium-audit-20261105-0222(1).md | 99aef3d77cc496ad8a9ab033af4eb951b4cdbcb22d9455fb64edad600f5fb160 |
| /home/maxg/insurance01-inputs/classification-guide.md | 89480f691737a0e8a762a836b8412476e0ed9d0b37639eb898e2826771c1dba8 |
| /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/application.md | ee9aa45fe1247743dd9da4c6e7693dd8151630e98653fd944acdb817ff4b25ed |
| /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/business-description.md | 7404b81d9cb83a1256a2e25299a5f9197a41f0f170236ac7633dc5f98692e9f5 |
| /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/field-notes.md | 1460d5cc05dc487d80bb2c382152dad609baf45cc24bec77035cf00359e5be6d |
| /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/insurance-certificates.csv | 77ff18a72e35e9326e752e14d09aa5a8db63fd923d13afb107c06970ee489909 |
| /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/payroll-register.csv | 4536004d11a63f4e733a37905ab9201f021ee34a05982405dd7f8f48a81bd075 |
| /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/site-signin-log.csv | 9ae36a9e35bb64f9ccbecb9321c0fddf9f721ff1cfce7633bc5f45f00e9937f7 |
| /home/maxg/insurance01-inputs/employer-files/severn-homebuilders/subcontractor-payments.csv | 114f76a91a9a66ea0c1fee4f8c19e268ada6119f18d4ec561d6a168833d4c516 |

</details>

## Scope and remaining limitations

This report rereads the supplied authoritative paths and requires the current processing, CSVs and unanswered question document to agree. It supports the existing evidence schemas; unsupported duties or incomplete evidence remain OPEN. There is no source locking, atomic multi-file snapshot, approval ledger, external certificate verification, rate calculation or premium quote. Final-source hashes detect changes before publication but do not authenticate source authorship or resolve factual contradictions. Payment proposals may retain fractional cents pending an explicit rounding decision; they never enter verified totals. Future runs need current auditor-supplied locations and regenerated dependent outputs when sources change.
