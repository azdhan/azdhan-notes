---
name: reeya-application-autofill
description: Fill Indian competitive-exam application forms for Reeya Sharma. Returns answers in input question order.
---

# Reeya Application Autofill

Take a list of form questions pasted by Reeya, return a numbered list of answers **in the same order** she asked them, with copy-paste-ready values. Reduces cognitive load during form filling.

> Canonical data is embedded in this skill (built from her 5 source PDFs: SSC CGL 2026, AAI Jr Exec, RBI Grade B 2026, UPSC, Confirmation Page). Edit the data sections when facts change.

## When to use

Trigger on any of:
- "Here are the questions in the form:" / "fill this form" / "answers for these questions"
- User pastes a numbered list, bulleted list, screenshot of form fields, or PDF page of form fields.
- "What should I put for [field name]?"

Don't use for: non-form writing tasks, anything unrelated to filling forms for Reeya.

## Workflow

1. **Parse the input** into a numbered list of questions. Detect:
   - Numbered lists (`1.`, `2)`, `(a)`)
   - Bulleted lists (`-`, `*`)
   - Multi-line text where each line/paragraph is one field
   - Screenshots of form pages (use `vision_analyze`)
2. **For each question**, classify it into one of:
   - **Direct match** — exact field in the data catalogue (Name, DOB, Father's name, etc.). Return value verbatim.
   - **Yes/No boolean** — return `Yes` or `No` per the catalogue. If catalogue has neither, return `No` (Reeya's default for negative-eligibility flags).
   - **Multi-choice** — return the specific option that matches her profile, e.g. UR / General / Female / English / Karnataka.
   - **Address line / sub-field** — split the address block as the form asks (Address Line 1, City, State, Pincode). Don't paste the full block into Address Line 1.
   - **Date** — return in the form's expected format (DD/MM/YYYY is the default; if form shows MM/DD/YYYY, swap).
   - **Percentage / marks** — return `XX.XX` (e.g. `93.10`).
   - **Code-based** — return the exact code (centre codes, EQ codes) from the catalogue.
   - **"Not in record"** — say "Not in record — please provide" and explain what the field typically expects.
3. **Output format** — Markdown numbered list mirroring the input order. One line per question. Format:
   `1. <Question text>: <Answer>`
   For long answers (full address), keep on one logical block but preserve line breaks.
4. **End with a flag block** listing any questions that needed interpretation, had multiple possible answers, or aren't in the record.

## Defaults for ambiguous questions

These come up across forms and Reeya's answers are stable:

| Pattern | Default answer |
|---|---|
| Nationality | Indian |
| Gender | Female |
| Category (UR/OBC/SC/ST) | UR / General / Unreserved |
| Marital status | Unmarried |
| PwBD / Disability | No |
| Need scribe / compensatory time | No |
| Ex-serviceman / ESM / ECO / SSCO | No |
| Government employee | No |
| M.Phil / PhD | No |
| Indian citizen? | Yes |
| Belongs to minority? | No |
| Criminal case pending? | No |
| Willing to serve anywhere in India? | Yes |
| Medium of exam | English |
| Exam centres (if Karnataka + Telangana cities allowed) | Bengaluru > Mysuru > Hyderabad > Mangaluru |

## Yes/No question bank (return "No" unless noted)

- Are you a person with benchmark disability (PwBD) of 40% or more? — **No**
- Are you a person with specified disability under Section 2(s) of RPwD Act 2016? — **No**
- Do you have a physical limitation to write? — **No**
- Do you need a scribe? — **No**
- Do you need compensatory time? — **No**
- Are you an Ex-Serviceman (ESM)? — **No**
- Have you rendered 5+ years of military service? — **No**
- Are you an Indian National? — **Yes**
- Have you completed 1 year apprenticeship in AAI? — **No**
- Are you seeking age relaxation? — **No**
- Are you seeking relaxation under widow / divorced / judicially separated? — **No**
- Are you an AAI Employee? — **No**
- Are you an RBI Employee? — **No**
- Are you a Government / PSU / Public Sector employee? — **No**
- Have you informed your Head of Office about this application? — **No**
- Are you an Ex-employee of banking institutions retrenched? — **No**
- Have you appeared for Phase-I in this RBI post before? — **No**
- Do you possess M.Phil? — **No**
- Do you possess Doctorate / PhD? — **No**
- Do you have an Integrated / Dual Degree? — **No**
- Do you have operating knowledge of computers? — **Yes**
- Do you have prior experience in SCBs / PSBs / AIFIs / RBI? — **No**
- Do you possess Master's with Research/Teaching experience? — Not in record (assume No if forced)
- Do you have a twin brother/sister? — **No**
- Consent to Aadhaar verification? — **Yes**
- I agree to authorize SSC/RBI to use my Aadhaar data — **Yes**
- I have read the notice and accept all T&Cs — **Yes**
- Willing to serve anywhere in India? — **Yes**
- I agree to connect to DigiLocker — **Yes**

## Identity fields (verbatim)

| Field label (any form)                                   | Answer                                                            |
| -------------------------------------------------------- | ----------------------------------------------------------------- |
| Name (as per matric cert) / Candidate's Name / Full Name | `REEYA SHARMA`                                                    |
| New / Changed Name (if any)                              | `-` (None)                                                        |
| Father's Name                                            | `RAVINDRA SHARMA`                                                 |
| Mother's Name                                            | `ANITA SHARMA`                                                    |
| Spouse's Name (if married)                               | `-` (Not applicable)                                              |
| Date of Birth (DD/MM/YYYY)                               | `11/12/2001`                                                      |
| Gender                                                   | `Female`                                                          |
| Category                                                 | `UR` (or `General` / `Un-reserved` — pick whatever the form uses) |
| Nationality                                              | `Indian`                                                          |
| Marital Status                                           | `Unmarried`                                                       |
| Visible Identification Mark                              | `A MOLE ON CHIN`                                                  |
| Aadhaar Number                                           | 850652933717                                                      |
| PAN Card Number                                          |  GOFOS9797F                                                       |

## Contact fields

| Field | Answer |
|---|---|
| Mobile Number (primary) | `9080048726` (or `+91 9080048726` if form asks for country code) |
| Alternate Mobile | ⚠️ Two values in record: `8122418407` (RBI form) / `8015211029` (AAI form). Default to `8122418407`; flag for user confirmation. |
| Email ID | ⚠️ Two values: `reeyaeeshu01@gmail.com` (RBI, SSC) / `reeyasharmaworkspace@gmail.com` (AAI). Default to `reeyaeeshu01@gmail.com`; flag. |

## Correspondence Address (Bengaluru)

- **Address Line 1**: `Sreeja Thanishq Flat No 110 A Block`
- **Address Line 2**: `2nd Cross, Byrasandra`
- **Address Line 3 / Landmark**: `CV Raman Nagar`
- **City / Town / Village**: `Bengaluru`
- **District**: `Bengaluru Urban` (or just `Bengaluru` if the form uses the older naming)
- **State**: `Karnataka`
- **Pincode / ZIP**: `560093`
- **Country**: `India`

## Permanent Address (Jharkhand)

- **Address Line 1**: `Rupashray Bhawan at Laldih`
- **Address Line 2**: `Near Gopalpur Panchayat`
- **Address Line 3**: `PO Ghatsila`
- **City / Town / Village**: `Ghatsila`
- **District**: `East Singhbhum`
- **State**: `Jharkhand`
- **Pincode / ZIP**: `832303`
- **Country**: `India`

## Education

### 10th / SSC / Matriculation

| Field             | Answer                                                                         |
| ----------------- | ------------------------------------------------------------------------------ |
| Board             | `Central Board of Secondary Education (CBSE)`                                  |
| School name       | `Kendriya Vidyalaya AFS Sulur, Coimbatore` (if form asks; otherwise just CBSE) |
| Year of passing   | `2017`                                                                         |
| Date of passing   | 03/06/2017                                                                     |
| Roll No           | `4021340`                                                                      |
| Percentage / CGPA | `93.10`                                                                        |
| Class / Division  | `First Class with Distinction` (93.10% implies distinction)                    |

### 12th / HSC / Intermediate

| Field             | Answer                                                                        |
| ----------------- | ----------------------------------------------------------------------------- |
| Board             | `CBSE` (Central Board of Secondary Education)                                 |
| School name       | `Kendriya Vidyalaya AFS Yelahanka, Bengaluru`                                 |
| Year of passing   | `2019`                                                                        |
| Date of passing   | 02/05/2019                                                                    |
| Stream / Subjects | `PCM + Computer Science` (Physics, Chemistry, Mathematics + Computer Science) |
| Percentage / CGPA | `71.00`                                                                       |
| Class / Division  | `First Class`                                                                 |

### Graduation / Bachelor's Degree

| Field                       | Answer                                                                          |
| --------------------------- | ------------------------------------------------------------------------------- |
| Degree                      | `B.A. (Bachelor of Arts)`                                                       |
| University / Board          | `Bengaluru North University`                                                    |
| State of University         | `Karnataka`                                                                     |
| Year of passing             | `2023` (or `2022` if form asks "course completion year" — see discrepancy note) |
| Date of result              | `02/09/2023`                                                                    |
| Roll No                     | `19HU1A1018`                                                                    |
| Percentage / CGPA           | `73.29`                                                                         |
| Class / Division            | `First Class`                                                                   |
| Status (Passed / Appearing) | `Passed`                                                                        |

⚠️ **Graduation year discrepancy** — AAI form has date 28-07-2022; RBI/SSC forms have 2023. If the form asks "Date of result" use 02/09/2023. If it asks "Year of course completion" use 2022. If just "Year of passing" use 2023 (more recent across sources).

### Highest Educational Qualification

- `Graduation` (B.A.) — this is the highest as of all source PDFs.

### Languages Known

- `English` — Read: Yes, Write: Yes, Speak: Yes
- `Hindi` — Read: Yes, Write: Yes, Speak: Yes

### Computer Knowledge

- `Yes` — "Proficient in Computer Applications"

## Bank Account (only if asked; mostly RBI forms)

| Field | Answer |
|---|---|
| Account Holder Name | `Reeya Sharma` |
| Bank Account Number | `34999464000` |
| Confirm Bank Account Number | `34999464000` |
| Bank Name & Branch | `SBI Air Force Station Yelahanka` |
| IFSC Code | `SBIN0002187` |
| Account Type | `Savings Account` |

## Examination Centres

Default ordering (most Karnataka-friendly; matches all 3 of her actual applications):

**SSC CGL 2026 (Medium: English):**
- Preference 1: `KKR-Bengaluru (9001)` — Karnataka
- Preference 2: `KKR-Mysuru (9009)` — Karnataka
- Preference 3: `KKR-Mangaluru (9008)` — Karnataka

**AAI Jr Executive (only 3 prefs):**
- Preference 1: `Telangana — Hyderabad - Rangareddy`
- Preference 2: `Karnataka — Bengaluru`
- Preference 3: `Karnataka — Mysore`

**RBI Grade B (DR) Phase I (Medium: English):**
- Preference 1: `Karnataka — Bengaluru`
- Preference 2: `Karnataka — Mysuru (Mysore)`
- Preference 3: `Telangana — Hyderabad`
- Preference 4: `Karnataka — Mangaluru (Mangalore)`

**RBI Grade B (DR) Phase II (Medium: English):**
- Preference 1: `Bengaluru` (Centre Code: `12`)
- Preference 2: `Mysuru (Mysore)` (Code: `33`)
- Preference 3: `Hyderabad` (Code: `19`)
- Preference 4: `Madurai` (Code: `38`)

 

## Exam-specific flags

- **SSC CGL 2026** — Also applying for: JSO (MoSPI) = **Yes**; AAO (Central Cadre) = **Yes**. JSO/AAO EQ status = **Yes**. Languages studied at matric level: `English, Hindi`. Applied for JSO/Statistical Investigator/AAO other cadres = mostly **No**.
- **RBI Grade B 2026** — Cadre: General. Phase I medium: English. Fee paid: ₹1003 (₹850 + ₹153 IGST) online on 03/05/2026, Ref: `CHD54O41J2RQRT`. Aadhaar consent: Yes. DigiLocker consent: Yes.
- **AAI** — Post 03 = Junior Executive (Common Cadre). Indian National = Yes. Apprenticeship completed = No. AAI Employee = No.

## Common "other" fields

- **"Are you willing to serve anywhere in India?"** — `Yes`
- **"Do you want to make your personal info available for job opportunities (DoPT OM)?"** — `No`
- **"Whether seeking age relaxation?"** — `No`
- **"Age as on [cutoff date]:"** — Compute from DOB 11/12/2001. Reference values already in record:
  - As on 01/08/2026: `24 Years 7 Months 22 Days`
  - As on 01/04/2026: `24 Years 3 Months 22 Days`
  - As on 04/09/2023: `21 Years`
- **Visible Identification Mark** — `A MOLE ON CHIN`
- **Whether employed in Govt / PSU / PSB** — `No**

 

## Output template

```markdown
**Form answers for Reeya Sharma** (in question order)

1. <Question text>: <Answer>
2. <Question text>: <Answer>
3. <Question text>: <Answer>
...

---

⚠️ **Flagged for your review:**
- Q<sub>n</sub>: <reason> — alternative value in record: <alt>
- Q<sub>n</sub>: not in record — please provide
```

## Pitfalls

- **Do not paste the full address block into Address Line 1.** Most forms split address into 2-3 lines plus District/State/Pincode. Always distribute.
- **Do not invent missing IDs.** Aadhaar and PAN are redacted in source PDFs; return "Not in record" and let the user fill.
- **Discrepancies** (alt mobile, email, graduation year, 10th/12th dates) — return the most common / most recent value and flag. Don't pick silently.
- **Date format** — most Indian government forms want DD/MM/YYYY. If the form says MM/DD/YYYY or shows a calendar picker, use the candidate's DOB 11 December 2001.
- **"Not applicable" vs "-"** — match the form's convention. If form has `-` placeholders, use `-`. If form has "NA", use `NA`. If form has "Not Applicable" radio, select it.
- **Category field** — Reeya is UR. Forms that say "UR" use UR; forms that say "General" use General; forms that say "Un-reserved" use Un-reserved. Match the form's label exactly.
- **Centre codes vs centre names** — for SSC use centre code (e.g. 9001), for RBI use centre name (or both if form has both columns). Never mix.

## Verification

Before returning:
- Every input question has exactly one answer line.
- Order matches input order.
- Flag block at the end covers every ambiguous answer.
- No internal data structure leaked; output is user-facing.
