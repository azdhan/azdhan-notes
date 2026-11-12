# Questions | Technical Issues with SIM Binding
**Event:** #NAMA — *Technical Issues with SIM Binding* · Friday, 13 Nov 2026 · online
**Runs:** 1:30–1:50 opening presentation (Meghna Bal) · 1:50–3:10 Panel 1: Technical Alternatives to SIM Binding · 3:10–4:30 Panel 2: Implications for Users and Businesses
**Built from:** three pre-event speaker calls — Parag Kar, Parag Modi, Suman Kar (with Azdhan) — plus the Dec 2025 event record
**Status:** working moderator's cue sheet. Edited live, cut on the day.

---

## 0. How to read this sheet

### Tagging

| Marker | Meaning |
|---|---|
| `[ANSWER: Parag Kar]` | **Answerer.** Kar (ex-Qualcomm, govt affairs; telecom / OS / operator layer) |
| `[ANSWER: Parag Modi]` | **Answerer.** Modi (Bureau; ex-Idea Cellular, ex-GSMA; fraud prevention, device fingerprinting) |
| `[ANSWER: Suman Kar]` | **Answerer.** Kar (security research; threat models, policy design, harms) |
| `[ANSWER: Meghna Bal]` | **Answerer.** Opening presentation — business impact and edge use cases |
| `[ANSWER: Kar + Modi]` | Both must answer. Ask Kar first, then Modi. |
| `[ASKER: Pahwa]` | Nikhil **Pahwa** asks this personally, in addition to the answerer tag. Always paired. |
| `MUST ASK BEFORE 2:30` | Hard scheduling constraint. Drops first if the panel runs late. |
| `**Bold**` | Priority. Must land. |
| `*italics*` | Stress on the operative word — *exactly*, *any*, *technically*, *present*. |
| `~~struck through~~` | Considered and cut. Kept visible so it isn't re-proposed. |
| No tag | Open floor. |

Labels are written out in full everywhere. No bare "Parag", no bare "Nikhil" — there are two Parags and one Nikhil on this sheet, and the December 2025 sheet lost time to that.

### Who can answer what (routing cheat sheet)

| If the question is about… | Go to |
|---|---|
| OS APIs, entitlements, eSIM, what the handset can assert | Parag Kar |
| Operator-side verification, GSMA / CAMARA / Mobile Connect, telco products | Parag Kar |
| Continuous vs discrete checking, what "binding" *technically* means | Parag Kar |
| UPI mechanics, device fingerprinting, silent verification POCs | Parag Modi |
| Fraudster behaviour, SIM swap / cloning, mules, numbers on rent | Parag Modi |
| Multi-device, roaming, dual-SIM, what breaks for real users in real apps | Parag Modi |
| Threat models, metrics of success, profiling harms, redressal, cost, intermediaries | Suman Kar |
| Business impact, survey numbers, edge cohorts | Meghna Bal |

### Source-integrity notes
- The three call transcripts carry unreliable speaker diarization in places; attribution in this sheet follows the **substance** of what each speaker claimed expertise in.
- The Suman Kar call **ends mid-sentence** (on whether Meta becomes the judge of who gets access). Follow up with him before Friday and finish that thread on the panel.
- Kar said on the call that he has **not yet researched** the current state of play and needs documents from Azan. Do not put him on a fact he hasn't read — route those to Modi or Suman Kar.

---

# PANEL 1 — Technical Alternatives to SIM Binding (1:50–3:10)

## 1. Opening — the impact map, before we argue mechanism
*(1:50–2:05. The floor is Meghna's. Pahwa does not editorialise here; he only sets up the next two slots.)*

1. **`[ANSWER: Meghna Bal]`** `[ASKER: Pahwa]` — Can you map what SIM binding actually breaks for a business that runs its customer conversations on WhatsApp: one business number across several devices, two or three people answering customers, a laptop and a tablet in the loop? Where does the *critical* use case fail first?
2. **`[ANSWER: Meghna Bal]`** — Your material finds roughly 86% of businesses run one business number on more than one device, about 92% reach messaging from laptops, desktops or tablets, and 75.6% have two or three people handling customer messages. Of those three, which breaks on day one, and which survives with a workaround?
3. **`[ANSWER: Meghna Bal]`** — Only about 33% of frequent travellers rely on an Indian SIM with roaming. What does SIM binding do to the other two-thirds, and to NRIs and students keeping an Indian number alive from outside the country?
4. **`[ANSWER: Meghna Bal]`** — Rank the edge cases by damage: SIM-less tablets, shared household devices, crisis and abuse survivors who change numbers deliberately, prepaid numbers that lapse, merchant navy and offshore crews who are offline up to 40 days.
5. **`[ANSWER: Meghna Bal]`** — Which single number from your analysis should we **stop** quoting, because it was measured against a six-hour logout rule that no longer formally exists?
6. `[ANSWER: Meghna Bal]` — Does the business picture change if the check is silent and network-side rather than OTP-based? What would you need to see before calling the disruption acceptable?

## 2. From impact to feasibility — the bridge
*(2:05–2:20. This is where the two Parags take the use cases Meghna just named and run them through the rule.)*

7. **`[ANSWER: Parag Kar]`** `MUST ASK BEFORE 2:30` — Take the use cases Meghna just laid out. Which of them does SIM binding actually touch, and which does it miss entirely? Is there any configuration of this rule that a user with a SIM-less tablet, or a SIM in another country, never notices?
8. **`[ANSWER: Parag Modi]`** — Same list, from the fraud side. For each broken use case, what does the *fraudster* lose? Walk us through it — is the crook stopped, or is the honest user stopped?
9. **`[ANSWER: Parag Kar]`** — You said on our call that this "treats WhatsApp in isolation." Is there a version of binding that is invisible to the user and still effective against fraud? If yes, why isn't *that* the direction?
10. `[ANSWER: Parag Modi]` — A messaging app is not a payments app: it is used all day, every day, on secondary devices, for files, work and family. Can the banking lens *technically* be applied here at all — or is the comparison itself the error?

## 3. Definition and demarcation — what is actually being mandated
*(2:20–2:40)*

11. **`[ANSWER: Kar + Modi]`** `MUST ASK BEFORE 2:30` — What *exactly* does the direction require: that **a** SIM is *present* in the device, that **the registered** SIM is present, or that an active plan for the number exists? These are three different checks with three different reliability profiles.
12. **`[ANSWER: Parag Kar]`** — You've said flatly that this "is actually not SIM binding, it is device binding." Which is it, technically and legally — and what changes if we name it correctly?
13. `[ANSWER: Parag Modi]` — UPI does device binding through `SendSMS` plus a bespoke NPCI-certified, entitlement-gated API; `CTCarrier` is deprecated and gone. Is UPI-style binding consistent with what the direction asks messaging apps to do — or is the UPI analogy doing work it can't support?
14. **`[ANSWER: Parag Kar]`** — December 2025's position was categorical: apps cannot read SIM identifiers, iOS blocked it long ago, Android stopped. Reporting now says Apple has made "the necessary changes." What is the *actual* Apple surface — and what does it establish?
15. `[ANSWER: Kar + Modi]` — The mechanism open to ordinary apps returns a confidence-rated estimate of whether a cellular plan appears to exist, is user-consent gated, and may return "not supported." What does an app do when the user denies permission — lock them out, or let the session run? Who carries liability for a false lockout?
16. `[ANSWER: Parag Kar]` — Which predicate does DoT actually want? A prepaid number that lapses fails an "active" test while sitting physically in the handset. Is that user locked out of WhatsApp for forgetting to recharge?

## 4. eSIM, dual-SIM, travel, roaming
*(2:40–2:55)*

17. **`[ANSWER: Parag Kar]`** — You said eSIM versus physical SIM makes no difference: the information simply moves from the plastic into a secure element in the device. Does that cut both ways — is the check stronger or weaker when the identity lives in the handset?
18. **`[ANSWER: Parag Kar]`** — The direction says the SIM "present in the device"; the announcement says "physically present and active"; press reports say a *Physical* SIM. Which text governs an eSIM-only iPhone with no SIM tray — and which governs the iPhone 16 Airtel eSIM sold in India today?
19. `[ANSWER: Parag Modi]` — You put it plainly on our call: OS APIs report SIM presence in slot one and slot two, not *which* SIM. "Then how do you do SIM binding? Because you can put any SIM then." Are we binding identity, or slot occupancy?
20. `[ANSWER: Parag Modi]` — Dual-SIM user, WhatsApp on SIM two, data on SIM one. Silent verification is a mobile-data-layer technology. What does the check see?
21. **`[ANSWER: Parag Modi]`** — Your Almaty test: two and a half hours Delhi to Almaty, phone off or in flight mode, land, location changed. Does the account need re-verification — and if yes, how many times a year is an ordinary traveller asked to prove who they are?
22. `[ANSWER: Parag Modi]` — Traveller swaps to a local SIM or a travel eSIM for cheaper data. The account is bound to the Indian SIM; WhatsApp asks for re-verification when the original SIM comes out, and the contacts go with the account. Is that the *intended* behaviour of this rule?
23. `[ANSWER: Parag Kar]` — You made the hardware argument on the call: Apple drops the tray, Android copies within six to twelve months, exactly as with the headphone jack. In an eSIM-first cycle, is a rule written around a physical SIM redundant at launch — *literally* at launch?

## 5. Frequency, trigger, and what "binding" means once it's not continuous
*(2:40 onward — carry this in parallel with section 4; it is the spine of the panel.)*

24. **`[ANSWER: Parag Kar]`** `MUST ASK BEFORE 2:30` — Continuous checking was technically feasible and practically impossible: battery drain, heat, no phone calls. So the plan becomes a discrete window. What is the *operational* difference between a one-hour window and a two-day window, from a fraudster's chair?
25. **`[ANSWER: Parag Kar]`** — If the check runs once in two days, someone changes the SIM, runs the fraud, and is gone before the app notices. What exactly has been prevented? You called the earlier regime "absolutely nonsense" — is the discrete version worse, because it looks like it works?
26. `[ANSWER: Parag Modi]` — The written direction says six hours. The April parliamentary answer says risk-based, no fixed period. You said you'd operate on the assumption that six hours still holds, since nothing has been retracted. Which one do app teams build against **today**?
27. **`[ANSWER: Parag Modi]`** — Define a risk-based event for messaging, concretely: SIM change, location change, IP change, device change, behaviour change. What weight does each carry, and what is the tolerance window for a tunnel, a flight, a network drop?
28. `[ANSWER: Kar + Modi]` — When a check fails because of network loss and not fraud, does the session die, or is there a grace state? What is the safe failure mode — and can an attacker *force* the fallback by degrading the network?
29. `[ANSWER: Suman Kar]` — No published methodology, no threat model, no metrics of success defined before implementation. Is "risk-based" a specification, or a blank cheque the platform fills in however it likes?

## 6. Alternatives — what should replace it
*(This is the section that makes the event advance the conversation rather than re-argue 2025. Keep it.)*

30. **`[ANSWER: Parag Kar]`** — Your proposal: poll the operator. The operator already knows where the subscriber is, which BTS they're on, whether the number appears in two places at once, whether the SIM is cloned. Describe the check end to end — what does the app ask, what does the operator return, what does the user experience? Nothing?
31. **`[ANSWER: Parag Kar]`** — GSMA's OTP-less / Mobile Connect / CAMARA family. How does it work, what does it require from the SIM's data connection, does it work over Wi-Fi, and what is the latency?
32. `[ANSWER: Parag Modi]` — Your NPCI proof of concept with Slice and Navi reported SIM-binding fraud at **zero** with silent mobile verification versus SMS-based binding. Zero is a strong number. What was the population, the period, and what counted as a SIM-binding fraud in that test?
33. **`[ANSWER: Parag Modi]`** — Vi's silent verification with Meta works "when a Vi user accesses WhatsApp on the Vi mobile network." So: Wi-Fi? Another operator? Roaming? Build us the coverage matrix — what works under what condition, because nothing like it exists in the public record.
34. `[ANSWER: Kar + Modi]` — Airtel's IQ Gateway promises silent authentication that "replaces OTP SMS for login and SIM-binding flows," with network-first fraud scoring on network, device and usage signals. Is this the 2025 alternative — CAMARA, composite risk index, probabilistic indicators — now shipped as a telco product? And what does one check cost an app?
35. `[ANSWER: Kar + Modi]` — What does a "silent" check *assert*: a point-in-time network-side confirmation, or something that survives an hour of disconnection? Does the 2025 objection — that a check never establishes continued presence — still hold against these products?
36. `[ANSWER: Parag Kar]` — You called the whole SIM-binding story wrong because it isolates WhatsApp from fraud on ordinary voice calls and digital arrest. What does an integrated fraud architecture look like, layer by layer — and who owns it?
37. `[ANSWER: Parag Modi]` — Device fingerprinting as pseudo-IMEI, surviving factory reset and root, deployed across hundreds of millions of devices. Is that a privacy improvement on SIM binding, or a new tracking surface wearing a fraud costume?
38. `[ANSWER: Parag Modi]` — Cross-operator case: a Jio number, an app integrated with a different carrier's verification service. Who answers the query, and what does the app do when nobody does?

## 7. AI agents, bots, remote sessions, multi-device
*(The genuinely new material. It must land.)*

39. **`[ANSWER: Parag Kar]`** `[ASKER: Pahwa]` — Use me as the test case: six agents running off a Raspberry Pi at home, a WhatsApp QR sign-in done remotely from anywhere in the world, an agent reading only selected chats to track my commitments, buying on Amazon against my account, executing a trading strategy on a broker API. Under SIM binding, which of these dies *first*?
40. **`[ANSWER: Kar + Modi]`** — Does an agent's session inherit the principal device's SIM check, or must every agent hold its own number and its own SIM in its own device? Nobody has specified this.
41. `[ANSWER: Parag Kar]` — Telegram bots run cron jobs and health checks that people use to manage entire server infrastructures; when Telegram went down around the exams in May, there was panic in the tech community. What happens to those scheduled tasks on 1 January?
42. **`[ANSWER: Parag Modi]`** — A remote server in Malaysia, running an agent against WhatsApp Web: location change, device change, no SIM. Is that a fraud signal, or a Tuesday?
43. `[ANSWER: Parag Modi]` — Is the WhatsApp Business API an "app-based communication service"? Does a business number need a SIM in a data centre — and is there *any* exemption class in the direction as written?
44. `[ANSWER: Parag Modi]` — Multi-device reality on the record: a child's tablet with the same WhatsApp for file transfer, SIM-less tablets with Telegram logged in, whole organisations working in WhatsApp Web. Which of these survives a hard SIM-presence requirement, and how?
45. `[ANSWER: Parag Kar]` — If this extends to Discord or similar, you said you'd have to write your own messaging app. Is that a joke — or the actual price of scope creep for anyone running agents?

## 8. Countermeasures — what the fraudsters do next
*(If this section is short, the panel has failed to test the policy on its own terms.)*

46. **`[ANSWER: Parag Modi]`** — If this lands, which fraud grows first? SIM swap? SIM cloning? Numbers on rent at ten rupees bundled with a shopping account?
47. **`[ANSWER: Parag Modi]`** — SIM swap mechanics here: a duplicate SIM obtained with a signed Aadhaar copy at a store — replacement, not issuance, so no video KYC. Victim's phone is dark for an hour while the scam runs. Has SIM binding made that attack *more* valuable, not less?
48. `[ANSWER: Suman Kar]` — Mules: willing, complicit, unaware, coerced. The mule in India holds the SIM and the handset; the operator abroad drives the session over a second channel and shares QR codes. Does the check see anything wrong at all?
49. `[ANSWER: Suman Kar]` — Even a *successful* SIM binding displaces: the scam moves to a neighbouring country's numbers, or to Facebook Marketplace, Instagram, TikTok, X. Has anything been prevented — or only relocated?
50. `[ANSWER: Modi + Kar]` — Session-token theft is cited as behind the large majority of successful breaches in 2024 — the strongest evidence anywhere *for* this policy. Does SIM binding touch that vector at all, or does the long-lived desktop session survive untouched?
51. **`[ANSWER: Parag Kar]`** — Your countermeasure test: if I am a scammer, what does this cost me versus what it costs a regular user? Do we keep making things continuously inconvenient every time a scammer finds a new method?

## 9. Close Panel 1 on prescription
*(Not on complaint. Hard stop on section 8 at 3:05 and run this.)*

52. **`[ANSWER: Kar / Modi / Suman Kar]`** — One each, one paragraph: what replaces SIM binding, and who implements it?
53. `[ANSWER: Parag Kar]` — Is operator-side authentication or Mobile Connect a *complete* substitute for app-level SIM binding — yes or no, and what's left over?
54. `[ANSWER: Parag Modi]` — If DoT said "device fingerprinting plus risk-based re-verification, and we drop the SIM check," is fraud better or worse off?
55. `[ANSWER: Suman Kar]` — What evidence would justify this mandate, who holds it, and what evidence would *falsify* it? Will DoT publish post-implementation metrics?
56. **`[ANSWER: Parag Kar]`** — You want a written note of problems to take into the room. Give us the three sentences that should be at the top of it.
57. `[ANSWER: all]` — If we could ship exactly one thing before 1 January, what should it be?

---

# PANEL 2 — Implications for Users and Businesses (3:10–4:30)

## 10. Opening — frame the panel

58. **`[ANSWER: Suman Kar]`** `[ASKER: Pahwa]` — You said the policy measures the number of checks completed and never measures prevention. Frame this panel for us: what does a policy that measures *prevention* actually look like?
59. **`[ANSWER: Parag Kar]`** — You were never in favour of this: the value unlocked through WhatsApp "will be completely destroyed." Name the value. What is the specific thing a user loses on 1 January?

## 11. Users, cohorts, and the edge cases that are now the whole case
*(Carry Meghna's cohorts forward; put real people in the question, not segments.)*

60. **`[ANSWER: Suman Kar]`** — A woman's mobile number is written on a public wall. She wants to keep her WhatsApp account and change her number. Under an account bound to a single SIM, what happens to her — and is she forced to keep the number that is being used to harass her?
61. `[ANSWER: Suman Kar]` — Elderly users and recharge cycles: a prepaid number that lapses fails an "active" check while the SIM sits in the phone. Who explains that to a seventy-year-old, and who is accountable when they simply lose their account?
62. `[ANSWER: Suman Kar]` — Crisis and abuse survivors, doxxing, shared household devices, migrant workers, crews at sea with up to forty days of no connectivity. Which of these is the hardest failure to design around — and is any of it on DoT's radar at all?
63. `[ANSWER: Suman Kar]` — NRIs and students living on Indian numbers from abroad. Under risk-based profiling, are they risk events by default?
64. `[ANSWER: Parag Kar]` `[ASKER: Pahwa]` — I once lost my agents for six hours because someone cleaning the house pulled the hard disk out of my Raspberry Pi, and I discovered how dependent I'd become. Multiply that by a forced re-verification regime. What is the felt user experience of one failed check?
65. `[ANSWER: Parag Modi]` — From the fraud-prevention side: is there a version of re-verification a legitimate user never *sees*? Silent, network-side, weighted to device constancy? Or is friction structurally unavoidable here?

## 12. Cost — who pays, and who profits
*(Dropped from the current agenda. Put it back. It has changed since 2025.)*

66. **`[ANSWER: Suman Kar]`** — Your back-of-envelope: if the six-hour logout holds across WhatsApp, Telegram, Snapchat and ShareChat, we're looking at four to five and a half billion SMS a day and something like fifteen to thirty-five thousand crore rupees a year. Now that verification is a *telco product* — Vi with Meta, Airtel's gateway — where does that bill land in January?
67. `[ANSWER: Parag Modi]` — Is silent verification free? You said number validation won't be free of cost. What does a per-check enterprise deal look like — flat fee per tier with overage? Who signs it, and what does it do to a small app?
68. `[ANSWER: Suman Kar]` — If the largest beneficiary of SIM binding is the telcos, how should that change the way we read the rule?

## 13. Privacy, profiling, surveillance
*(One bullet in the current agenda for two new data architectures. It needs its own block.)*

69. **`[ANSWER: Suman Kar]`** — Risk-based profiling requires WhatsApp and Signal to build user profiles — and Signal doesn't do that today. Give us the allocative and representational harm in one sentence a regulator can act on.
70. **`[ANSWER: Parag Kar]`** — Your suspicion on the call was blunt: this is a route to traceability, to knowing where a message came from — and the operator already knows that. If traceability is the real objective, is SIM binding even the right instrument?
71. `[ANSWER: Parag Modi]` — Silent authentication creates a carrier-to-app data surface that did not exist before. Who is the controller under DPDP, what is the lawful basis, and what stops the signal being reused for something else?
72. `[ANSWER: Suman Kar]` — Your STIR/SHAKEN argument: authentication protocols create non-repudiable records that outlive their purpose, and complex systems need intermediaries who then monetise the data. Which of those is the real risk in an Indian implementation — and what is the DKIM lesson here?
73. `[ANSWER: Suman Kar]` — The sinister case you raised: a carrier that cannot say no to a request to block a group of protesting students, and a state that can say "the algorithm did it." Where is the redressal mechanism, and who do I call?

## 14. Scope, jurisdiction, enforcement, and what is actually live on 1 January

74. **`[ANSWER: Suman Kar]`** — Snapchat says the rule doesn't apply to it because phone numbers aren't its primary identifier. Telegram lets you register with a username and no number at all. ShareChat and Josh received the directive anyway. What *exactly* is the criterion for being in scope?
75. **`[ANSWER: Parag Kar]`** — The self-eroding rule: if a messenger moves to usernames and handles, it exits the mandate entirely. Is the whole thing built on an identifier the platforms are already walking away from?
76. `[ANSWER: Suman Kar]` — Which version binds on 1 January — the November text requiring a six-hour logout, the April parliamentary answer promising risk-based analysis with no fixed period, or whatever each platform has already shipped? Two scant primary documents for one point four billion people is not a policy record.
77. **`[ANSWER: Kar + Suman Kar]`** — What is live on day one: hard cut or phasing, which apps first, what percentage of users, what is the published penalty for non-compliance, and is there a grace period for someone whose SIM is in a different handset on 1 January?
78. `[ANSWER: Suman Kar]` — No public consultation, no regulatory impact assessment, no threat model, no baseline metrics, no published fraud data. What is the *minimum* this policy needs before it goes live — and what should the community do if it doesn't get it?
79. `[ANSWER: Suman Kar]` — Telecom cybersecurity directions regulating internet services governed by the IT Act: is this a legitimate instrument, or jurisdiction by the back door? *(If no legal voice is on the panel, mark this as an unresolved gap and say so on the record.)*

## 15. Close Panel 2 — recommendations and artefacts
*(Event output. Non-negotiable.)*

80. **`[ANSWER: Suman Kar]`** — Your staged prescription: publish a threat model and a baseline → minimise → define risk-based expiry for diverse customer groups → protected access and disclosure → honest evaluation at twelve to eighteen months. Who signs up for stage one, and by when?
81. **`[ANSWER: Meghna Bal]`** — If your disruption numbers hold, what is the one sentence you want DoT reading on the morning of 14 November?
82. `[ANSWER: Parag Kar]` — The note to DoT: three problems, three alternatives, no adjectives.
83. `[ANSWER: Parag Modi]` — The build guidance for app teams shipping against a rule that hasn't been finalised: what do you tell them to build this month?
84. `[ANSWER: Suman Kar]` — The threat model DoT should have published first. What are its five headings?
85. **`[ANSWER: all]`** — Verdict, one sentence each, no hedging: will SIM binding reduce fraud in India?

---

# 16. Moderation control layer

**Must land before 2:30 (Panel 1):** Q7, Q11, Q24, Q30/31, Q39–Q40. If the panel runs long, cut sections 3 and 4 down to Q11, Q18, Q21 and protect the alternatives block.
**Must land before 4:15 (Panel 2):** Q60, Q66, Q69, Q74, Q85.
**Cut first if needed:** Q13, Q16, Q38, Q45, Q65.
**Protect at all costs:** Q30–Q35 (alternatives), Q39–Q42 (agents and remote sessions), Q74–Q75 (scope), Q80–Q85 (output).

**Empty slots are not errors** — but no new question goes on this sheet without a named addressee. That was the December 2025 gap and it cost us a platform slot.

**Register check:** policy-legal vocabulary in sections 3, 5, 13, 14 ("app-based communication services," "risk indicators," "allocative harm"). Plain-spoken in sections 11 and 12 ("a woman's mobile number is written on a public wall"). Both registers in one sheet, on purpose.

**Tone:** sceptically respectful. State the tension, ask for the resolution. Quote the counterparty — the direction, the parliamentary answer, the telco press release — never put words in the speaker's mouth.

---

# 17. Do not re-ask these

| ~~Question~~ | Why it's cut |
|---|---|
| ~~"What is SIM binding?" as a standalone opener~~ | Settled in the 2025 record. Sharpened into Q11 — the *which predicate* contradiction test. |
| ~~"Isn't a six-hour logout absurd for messaging?"~~ | Settled in 2025 and quoted to death. Only use it as the *which rule binds* test (Q26, Q76). |
| ~~"Is WhatsApp testing SIM binding?"~~ | Yes, publicly, since April 2026. The answer is on the record — theatre. |
| ~~"What do you think about privacy?"~~ | No mechanism, no architecture, no verdict. Replaced by Q69–Q73. |
| ~~"Are you for or against the government?"~~ | Not a question. Q85 is the verdict question. |
| ~~A question with no addressee~~ | The December 2025 sheet had one. It went unanswered. Every question here carries a tag. |
| ~~Asking a platform person a legal question, or a lawyer an OS question~~ | Route via the cheat sheet at the top. |

---

# 18. Open loops from the calls — chase before Friday

1. **Parag Kar** offered to send his published pieces on how he uses agents. Get them; they are quotable evidence for Q39.
2. **Parag Kar** has *not* studied Airtel/Bharati's non-SIM-binding application and said so. Get the document to him, or route those questions to Modi. Kar also asked for anything in the public domain from Azan.
3. **Airtel / Rahul's team** were invited to the earlier conversation and couldn't join. Given Q34 and Q35, an Airtel engineer on the silent-authentication block is the single highest-value addition to the panel.
4. **Parag Modi** offered to send draft questions for the panelists. Circulate this sheet to him first — he should mark what he can answer with numbers and what he can't answer on the record.
5. **Suman Kar's** call ended mid-sentence on whether Meta becomes the arbiter of who gets access. Finish that thread, and get his cost-model slides for the record.
6. **Apple** has said on its own developer forums that there is no such plan as the rumoured API; reporting says changes were made. Someone must resolve this on the record — Q14 cannot be asked as an open question twice.
7. **Snapchat's** position is a live scope test case. If nobody in the room can answer Q74, say so publicly and make the absence part of the story.