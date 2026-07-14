# India's Cybersecurity Problem, Listed: What the Experts Say Is Broken


1. **CERT-In answers to nobody, so anything it fixes is a favour rather than a accountable duty**

Every interviewee, without prompting, raised the accountability concerns of Cert-In as an organisation, which is the India's designated national cybersecurity agency, and there is no mechanism in law that requires it to act on what it receives or answer for what it ignores.

> "Just like how no regulator is accountable in India, the cyber regulator is also not accountable in India. So it's not a problem specific to cybersecurity. Usually, abroad, you will see regulators are held accountable by parliamentary committees and things like that. In India, that structure is totally absent." - Srikanth L


> "Certain does not actually have teeth to say that, 'you have not acted upon this so you need to shut down', or 'we will basically make this vulnerability public and make public aware.' CERT-In basically says that, 'okay, somebody gave us this thing', and asks 'can you fix it if it's possible?' But, CERT-In under no legal obligation to go beyond." - Srikanth L

Kiran Jonnalagadda draws the same conclusion from his long standing experience of dealing with CERT-In, and frames it as the difference between a service and a privilege.

> "Everything with Cert is like it's a privilege. If they feel like it, they will do something. If you cannot hold them responsible for delivering the service, then it's not a service. It's a privilege... Anything that works in Cert is a lucky accident because there is no requirement for any of it to work in their setup." - Kiran Jonnalagadda

Karan Saini, who has spent years reporting vulnerabilities to government agencies, has arrived at the harshest position of the three.

> "I don't know why CERT-In exist, really. In the [Deccan Herald piece](https://x.com/squeal/status/2068572819789881743?s=20), the editors changed the language significantly. I was asking for it to be closed. I was saying, let's shut down CERT-In." - Karan Saini

**What can be done:** Jonnalagadda's prescription is statutory. "Go get an act of parliament passed that makes Cert accountable for services... It should be like RTI, that they have to act or there are consequences for not acting on it." He argues there are only two workable models like being answerable to parliament or to public. He cites the US CERT Coordination Center, which comes under the[ Carnegie Mellon University](https://www.sei.cmu.edu/divisions/cert/) outside government control, but acts as a coordination organisation for cyber security incidents as proof the second model that could work for India. 

It is important to note that CERT-CC is different from US-CERT, which is a federal government agency under the Department of Homeland Security that aims to protect US national cybersecurity infrastructure.

2. **Reporting to CERT-In is a one-way street: you give everything and get a ticket number back**

Beyond the accountability gap sits a design choice. CERT-In collects reports and returns nothing, and its founding director described that as a feature. Jonnalagadda recalls a consultation where Gulshan Rai, the agency's first head, defended the architecture.

> "He [Gulshan Rai] was proud of this architecture, that it is completely safe to give information to CERT-In because we never give anything back... By design, CERT-In will tell you nothing, but you tell CERT-In everything. That would have been fine if CERT-In had something holding it accountable for its confidentiality. But where in the law is anything that says CERT is accountable for the confidentiality of the report it receives? All of that is a black hole... They simply are a data demander. It is not obvious why any company should ever bother reporting to Cert." - Kiran Jonnalagadda

Saini's reporting history bears this out across agencies. His most recent CERT-In report, on a master-password exposure in the Maharashtra State Board's portal, produced a response that claimed a false fix, where in fact the fix has not been implemented.

> "They said it's fixed, but it wasn't. It just wasn't fixed. I clicked the same link I sent them in the email, it was still there. I just did not respond to that because at that point, you're wasting your own energy trying to get them to respond." - Karan Saini

He notes the problem extends past CERT-In.  National Critical Information Infrastructure Protection Centre (NCIIPC), the agency responsible for critical infrastructure, acknowledged his report on a vulnerability in the Telecom Regulatory Authority of India (TRAI) portal, said it was verifying, and never wrote back.

> "None of these agencies are as transparent as they expect the [incident] reporters or the people who are finding the issues to be." - Karan Saini

The ex-SISA analyst, a working security professional, could not describe what happens after a report is filed, which highlights how CERT-In is currently positioned and how much importance the industry gives it. 

> "When you report to certain, I honestly don't know what happens... What's the government role in this, that even I don't know. There's no recourse. Basically, the conclusion is there's no proper recourse to this." - ex-SISA analyst

**What can be done:** Jonnalagadda wants CERT-In rebuilt as a coordination agency on the model of the [US CVE (Common Vulnerabilities and Exposures) ](https://www.cve.org)system, where a reported vulnerability gets a confidential window for fixing and then mandatory publication. "There has to be a confidentiality period where you mitigate the risk for users before you go public. But going public has to be mandatory." He points to what a functioning system enables downstream: because the CVE database is dependable, services like [GitHub's Dependabot](https://github.com/dependabot) can automatically alert and patch developers worldwide. 

"When you can depend on an institution to behave properly, then you can create downstream services that ride on the dependency and make life better for everyone." - Kiran Jonnalagadda

3. **Denying a breach is the safest option, so nobody knows how bad India's problem actually is**

The two problems above produce a third. If reporting brings liability and returns nothing, companies deny. If everyone denies, the true scale of the problem is unknowable, and the resulting secrecy is itself a security failure.

> "In every single breach that I have experienced, I have not had the company ever acknowledge it." - Kiran Jonnalagadda

He traces the incentive precisely to CERT-In's proposed rules, which demand disclosure and create liability for non-disclosure while offering nothing in return, including an acknowledgement.

> "The incentive is structured towards denial and not towards disclosure... Denying the breach is legally the safest thing to do for a company. Because what is the user going to do? Nothing in the law keeps them accountable if a breach happens, if they never told CERT-In and if they never accepted a breach." - Kiran Jonnalagadda

The ex-SISA analyst confirms the pattern from inside the industry, and cites the Pine Labs case as an example of public denial after a real breach. In August 2021, then Pine Labs' CTO [denied](https://www.medianama.com/2021/08/223-pine-labs-ransomware-attack-records-exposed/) the data breach that was reported by cybersecurity firm [Cyble Research Lab](https://blog.cyble.com/2021/08/11/blackmatter-ransomware-attack-impacting-multiple-financial-institutions/).  The research firm claimed that over 5,00,000 unique records including sensitive information such as phone, name, and email ids were breached and the company responded saying, "our systems continue to be fully secure and our production systems continue to operate as usual and all customer data is safe." 

> "I think a lot of companies do not self-report... In the public segment, some companies might completely denied it. But in reality, they might be really breached and there might be  a data dump that occurred. The only time in India we hear about breaches is where somebody dumps the data in the dark web and some researcher or some activist finds it and reports on it." - ex-SISA analyst

One of the speakers we spoke to for this story, who requested anonymity, admitted that a person who runs a cybersecurity firm said, "Speaking up is bad for their cybersecurity business."

**What can be done:** The analyst's answer is enforcement with real cost, on the pattern of the US and EU, where companies face heavy fines for failing to report within fixed windows. "It shouldn't be an incentive. It should be a penalty, a fine, legal action." Security researcher Saini agrees on the mechanism and is blunt about the trigger: "Until some news headlines break that, oh, this company was fined 10 crores or 100 crores, nothing's going to happen, I think."

4. **India has run schemes and circulars since 2013 without a national strategy or policy to hold them together**

The last published National Cyber Security Policy dates to 2013. Read the the document here : [ Original PDF ](https://www.meity.gov.in/static/uploads/2024/02/National_cyber_security_policy-2013_0.pdf) |  [Archived PDF](https://web.archive.org/web/20260218023849/https://www.meity.gov.in/static/uploads/2024/02/National_cyber_security_policy-2013_0.pdf) 

> "India doesn't have a latest cybersecurity policy. At least it's not public. We are doing everything without strategy." - Karan Saini

Guttula, writing from the audit and governance side, describes the same vacuum in structural terms.

> "CERT-In rules, sectoral frameworks and mission programmes are all real, but they point in different directions. Without a single strategy that sets direction and accountability, no individual initiative can carry the load, and sovereign efforts stall in committees." - Venkata Satish Guttula

He further cites that sovereign cloud as the clearest casualty, a concept "keeps being studied and shuffled between bodies on long timelines," even as dependence on foreign providers continues to grow. This is much true and relevant when US government can decide which countries can have access to which models at what time. 

Saini contrasts this with the US, where even policy he considers flawed shows evidence of some background process. "Even the rubbish executive orders are still well-reasoned. Someone is doing the scientific thinking behind it... We are not even doing that," he added. 

**What can be done:** Guttula asks for "a published national cybersecurity strategy that names the objective and the owner, and a ring-fenced statutory authority for sovereign infrastructure with its own mandate and funding, rather than repeated bureaucratic transfers."

  5. **The state's cyber capacity is spread across duplicating agencies that cannot hire talent or spend money well**

Saini's critique of state capacity runs across three fronts: agency sprawl, broken recruitment, and wasted public spending.

On sprawl, CERT-In, NCIIPC, I4C and state police cyber cells overlap without coordination, and even if they do, with very less efficiency. Therefore resulting in the duplication of efforts without the intended results. 

> "Just as far as agencies go, I think we've created too many. They're conflating cybercrime and cybersecurity. They've become one thing... There is no one agency doing any of this in a coordinated manner. So duplication of efforts exists." - Karan Saini

His worked example is the I4C portal for reporting child sexual abuse material, which accepts one URL at a time. To report 165 abusive domains he had to zip a password-protected text file, upload it, and paste the password into the complaint's comment box. 

On recruitment, there is no open hiring route into these agencies for security specialists, especially if the entry runs through state or central generalist civil-service examinations.

> "Recruitment is absolutely worse... If you are a security geek, why would you be in the UPSC circles? If you can become a Babu, why will you want to become a keyboard presser?" - Karan Saini

He can name a single technically minded security professional who cracked the government route, a former UIDAI CISO, and that person has since left India altogether.

On spending, he reviewed the cybersecurity components of the Viksit Bharat 2047 roadmaps during a stint at a policy organisation and found nothing to show for the money.

> "Public money on cybersecurity in India is largely wasted. I can't think of anything which has come out of any of these big projects." - Karan Saini

He points to C-DAC (Centre for Development of Advanced Computing)-funded projects that "appear to be doing some things which we will have no use for" and money "funnelled into all these IITs to fund nonsense proof of concepts which don't go anywhere." **[ADD: specific C-DAC/IIT project examples; Karan said he would send concrete instances.]**

**What can be done:** Saini's fix for recruitment already exists inside the same ministry. "MeitY hires consultants. They hire consultants for law, for taxation, but not for security. At least CERT-In could literally do it because it comes under MeitY." Guttula suggests similar solution by asking to change the approach from "CERT-In empanelled auditors and independent CISOs with hands-on incident response, alongside the institutional members. "A five-year CISO cannot defend against a Mythos class capability," he affirmed.  
 

  7. **Empanelled auditors certify vulnerable infrastructure and keep their empanelment anyway**

CERT-In maintains a panel of approved security auditors, and RBI regulation requires regulated entities to file an empanelled auditor's certificate at least once a year. The infrastructure Srikanth investigated had carried its vulnerability for 30 months, through what should have been multiple audit cycles.

> "Somebody would have audited this site. How does one justify a company issuing a cybersecurity audit certificate for an infra that had so much vulnerabilities? Should they be allowed to audit? Or what value do you take on their audit certificate?" - Srikanth L

He draws the parallel with financial auditing, where the same failure mode exists but at least a consequence mechanism has been built.

> "Every company that has gone through major financial irregularities would have anyway been audited by a popular audit firm before that... and then the auditor faces a liability punishment. There's no accountability on the part of auditors [in cyber]. The same thing happens in some other verticals, say a doctor, where the person is incompetent and the incompetence is costing and that is proven, their licenses would be revoked. And that is not happening here." - Srikanth L

Jonnalagadda's one direct experience of the audit industry matches this.

> "The only experience I've had is where I had to call out a cybersecurity audit firm that gave a clean chit in a breach that really happened, where their report said no such thing happened... If I have proof of a breach and the cybersecurity audit firm denies the breach despite my proof, then are we still talking about error of judgment or malice?" - Kiran Jonnalagadda

He also raised a structural explanation, that a firm's empanelment status may itself depend on not reporting problems on government systems, but explicitly asked that this claim not be attributed to him and that an independent source be found. **[NEEDS SECOND SOURCE: the claim that empanelment incentives discourage firms from reporting incidents.]**

**What can be done:** Srikanth points to the financial sector, where a dedicated regulator for audit firms now exists with powers up to withdrawing an auditor's licence, and argues cyber auditing needs "the similar thing." Guttula notes the regulatory tightening has already begun on the financial side: NFRA inspections of the Big 4 network firms "have repeatedly flagged deficiencies in independence, documentation and professional skepticism," the RBI now requires IT Strategy Committees led by independent directors with substantial IT expertise, and ICAI is moving to formal Information Systems Audit Standards. **[ADD: citations for the NFRA inspection reports and RBI/ICAI requirements.]**

  8. **Compliance has become theatre: an organisation can be fully certified and fundamentally exposed**

The audit problem above has a mirror inside companies. Compliance is performed for the certificate, and the certificate has become the legal definition of security. Saini traces the loop to the IT Act's requirement of "reasonable security measures," a phrase courts and companies have filled with paperwork.

> "Reasonable security measures have been interpreted to mean adherence with security standards. ISO 27001, SOC 2, all of this is stemming from the fact that reasonable security measures could mean anything. They don't have a security program, but they have a certification. So that's reasonable security measures done." - Karan Saini

> "We run SOC2 shops and ISO shops where you pay 10,000 rupees, you get your certificate. That's it." - Karan Saini

The ex-SISA analyst, who worked at a compliance-and-security firm, describes how the certification is obtained.

> "Just to show on paper, they will establish something, but in reality, there won't be real data protection or continuous monitoring or security infrastructure in place, in a lot of the cases that I've seen at least." - ex-SISA analyst 

Guttula, who audits regulated entities for a living, dissects the mechanics from the auditor's chair.

> "Two habits do the damage. First, checklist auditing, where a junior asks whether a patch management policy exists, receives a 50-page document, ticks the box, and never traces whether the critical vulnerability was actually patched. Second, the split reality at audit time: the SOC telemetry lives in one tool while the audit evidence pack lives in a parallel spreadsheet maintained by a junior analyst at month end. The two are joined only for the audit, and the join adds no defensive value." - Venkata Satish Guttula

> "An organisation can look completely secure on paper and remain fundamentally exposed. Green dashboards mask real architectural vulnerabilities, and that gap is exactly where a capable attacker lives. Threat actors do not have a checklist." - Venkata Satish Guttula

**What can be done:** Guttula proposes making telemetry the evidence. Telemetry refers to the automated collection and transmission of data from distributed or remote sources to a centralised system, according to [IBM](https://www.ibm.com/think/topics/telemetry). He suggests to have a cyber security detection events from Security Operations Centers in a common standardised language that can be understood by everyone. In his opinion, this will enable the auditors to identify the issues instead of them having to independently dig through logs to identify the weak cybersecurity spots. 

Detection events from the M-SOC and entity SOCs would be tagged at source using a common taxonomy mapped to CSCRF, NCIIPC and CERT-In controls 

  9. **Companies treat security as a cost to be minimised, because failing at it costs them nothing**

The commercial logic is consistent across sources: security spending is discretionary because breaches carry no penalty outside banking.

> "In most enterprises, the problem with security is it costs money. The top guy, the CEO, will be focused on building the business and the marketing side of things. Security will be a low priority for a lot of these people." - ex-SISA analyst

> "It is entirely a market concern where if you are not part of a regulated industry where you know you'll be taken by the collar, [there are no stakes]. Which is only banks. Because there are no stakes, even with the Digital Personal Data Protection Act, who cares?" - Karan Saini

Jonnalagadda locates the cost precisely, and links it back to the institutional failure: the expense is labour, and the labour is heavy in India because no institution shares it.

> "It is not a technical cost, it's an HR cost... Unlike the US system, in India, nobody helps you. Therefore, everybody is watching their own back when it comes to security. Which is a lot of labor." - Kiran Jonnalagadda

Srikanth complicates the cost argument from the engineering side. In his experience the expense is a function of organisational maturity, and disappears inside teams that hire and build well.

> "There are organizations where this is seen as extra cost. And then there are organizations where, by the quality of hires and the quality of tools and processes, these costs are basically auto-absorbed. So it doesn't cost anything extra to ensure that security guarantee." - Srikanth L

  10. **Basic security consciousness is missing at every link of the chain, from the vendor's developers to the procuring agency to the end users**

Srikanth's dissection of the bank.in portal vulnerability found no single point of failure; nobody in the chain applied elementary security thinking. The portal, built for bank IT administrators, exposed an unauthenticated endpoint.

> "This is a very rookie thing... In the entire organization, in that private company that's the vendor here, there is nobody who had basic security consciousness. And this consciousness has to basically come from education. Why will you leave an unauthenticated [end]point?" - Srikanth L

The procuring agency evaluated nothing, and the intended users, technically savvy by definition, asked no questions either.

> "This is supposed to be a website for bank IT admins who are supposed to handle domain names. They are supposed to be an IT staff. At least 1,500 technical people have logged into this portal and actually given their details... You are an end user in charge of domain names. Would you register your domain with a random service provider, or if your service provider has a shady page, would you confidently give all your data, just because your boss told [you] so?" - Srikanth L

The ex-SISA analyst saw the same pattern in the C-DAC exposure connected to the CBSE case, where credentials sat in plain sight in the page source. **[ADD: one-line factual description of the CBSE/C-DAC incident with date.]**

> "They've openly left the master key or password just open there, which is not even a hack. It's basically you're opening a book and reading it." - ex-SISA analyst

He adds the procurement layer: the contracted vendor in that case "appears to be blacklisted" and the work appears to have gone "to the lowest bidder" who did "the bare minimum." **[ADD: verify the vendor's blacklist status and the procurement details before using; transcript wording is garbled here.]**

**What can be done:** Srikanth's answer is upstream of any regulation: security consciousness "has to come from education," built into how developers are trained, so that standard secure practices run automatically the way type-checking now runs in an editor, at no marginal cost.


 11. **Attackers have already put AI into their workflow, while defenders might wait for budget cycles and circulars**

Every weakness above is now exposed to adversaries operating at machine speed. Srikanth, who used AI tooling in his own recent disclosure, describes what changed.

> "The thing that models bring in is the agility with which they can detect vulnerabilities, how they can quickly compound vulnerabilities which would have taken days and months for humans to compound. If you do it on an agentic speed, you're basically doing it several orders of magnitude faster." - Srikanth L

His own case supplies the arithmetic. The investigation and the 30-page report that would once have taken him ten days took a couple of hours with AI orchestration; the fix, which he describes as trivial, took the operator 16 days.

The ex-SISA analyst identifies the same shift as the present threat, ahead of speculative ones like quantum computing.

> "Given that AI is advancing, people can automate certain tasks and build malware just out of prompts and stuff. That's a whole different threat which really exists, which is the real threat that exists now." - ex-SISA analyst

Guttula also highlights this institutional asymmetry through the possible bureaucratic hurdles that the government institutions have to face.

> "Attackers have already pulled capable AI into their workflow. They do not take management approval, run a change board, or write a risk register entry before they act. Defenders wait for a budget cycle and a circular. The asymmetry is no longer subtle." - Venkata Satish Guttula

**What can be done:** Guttula’s core proposal is to build internal AI capabilities across five key areas: detection, triage (where the most urgent problems are dealt first), threat-intelligence correlation, log analysis, and [red teaming](https://www.ibm.com/think/topics/red-teaming). His specific recommendations are as follows:

- **Strengthen advisory language**:  He argues that phrases like _"where suitable"_ and _"where possible"_ are effectively treated as optional, and should therefore be replaced with firmer, more directive wording.
- **Mandate data residency and an Indian data plane**: Given the RBI’s April 2018 localisation mandate and the cross-border transfer restrictions expected in  Section 16 of the DPDP Act.
- **Deploy ensembles of genuinely diverse AI models that encourage human intervention**: When a high-fidelity model sharply disagrees with the rest of the ensemble, that divergence should trigger a human-led investigation, rather than being dismissed as noise.
- **Establish behavioural baselines over both short and extended windows**: Guttula cautions that "a Mythos‑class capability does not leave neat single‑event signatures," meaning that threat detection cannot rely solely on immediate alerts. Instead, systems should monitor activity across both narrow timeframes and extended 30‑to‑90‑day horizons to expose latent, persistent intrusions.


 


























# might not be relevant to the cyber security 
2. Third parties and data brokers hold vast amounts of Indian personal data, and nobody alerts anyone when they leak it

The entities holding your data are frequently ones you have never heard of, and when they are breached, no mechanism exists to tell the companies or people downstream. Saini's example is the Hitek Group breach of March last year, in which the Babuk ransomware group exfiltrated 460 gigabytes of telecom customer-acquisition records. **[ADD: independent verification of the Hitek Group breach; Karan states he examined a copy of the data himself.]**

> "How [does] Hitek Group have access to the literal database records of Airtel, Jio? I know this for a fact because I found a copy of the database. I searched myself in it. It has my bloody Aadhaar number in 850 million records. For some people, it has the driver's license." - Karan Saini

> "Ideally, both Airtel should be taken to court as well as Hitek Group, but nothing happened. They view themselves as victims, really." - Karan Saini

Below the breach economy sits an open retail market: broker sites selling students' exam records, including phone numbers, emails and disability status, for a few thousand rupees per exam. **[ADD: your own verification calls to affected families, which you conducted; describe without identifying anyone.]**

Jonnalagadda explains why the surface keeps growing: ordinary websites assemble functionality from plugins and third-party services, each of which receives personal data.

> "Who are these plugin providers who are now getting access to customer data to do this job? How many of these different entities now are receiving PII, and their security breaches are your problem because you're the source of the data as a merchant? But how do they know that third party had a breach? Where is the alerting mechanism for them? And that's what I would expect Certain to be doing." - Kiran Jonnalagadda

---




## II. The Sovereignty Problem

### 6. Almost the entire technology stack is rented from abroad, and the off switch sits in foreign hands

Guttula ranks this as India's most under-priced digital risk, ahead of any attack scenario.

> "India's most under-priced digital risk is not a cyberattack, it is dependency. We rent almost the entire technology stack from foreign providers, and any of them can be switched off by a foreign government or a foreign corporation, with no Indian law invoked and no Indian override." - Venkata Satish Guttula

His evidence begins with the July 2025 Microsoft suspension of services to Nayara Energy, an Indian refinery processing 20 million tonnes of crude a year, to comply with EU sanctions. "No Indian court ordered it and no Indian law required it... That is a corporate kill switch over a strategically important refiner, and India had no override of its own." **[ADD: independent verification of the Nayara Energy suspension and the litigation that followed.]** The June 2026 US export-control suspension of Anthropic's Fable 5 and Mythos 5 models made the same point at the AI layer: "Access returned when Washington decided. The switch was never ours." **[ADD: verification of the export-control directive and its withdrawal.]**

His paper maps the dependency across ten domains, from cloud (most Indian workloads sit within reach of the US CLOUD Act, which binds a US-incorporated provider wherever the data physically sits) to internet governance (India operates none of the thirteen DNS root-server identities) to digital trust (there is "still no sovereign, government-controlled certificate authority with broad default trust," a gap he traces to the 2014 NIC misissuance).

This is the one point on which the sources directly disagree, and the disagreement is worth preserving. Jonnalagadda argues the foreign dependency is currently what keeps Indian developers safe, precisely because Indian institutions do not function.

> "Pretty much 100% of all developers in India depend on the US system to watch their backs, and not the Indian system, where it's your luck if something nice happens." - Kiran Jonnalagadda _[transcript reads "banks"; confirm "backs" with Kiran at sign-off]_

> "We're all talking about sovereignty and nationalism and whatnot. And in software, that is just going to make your life much worse." - Kiran Jonnalagadda

Jonnalagadda's position extends to commerce: "I'm afraid to do business with any Indian company. I'm much more comfortable giving my data to a foreign company because I know that they're accountable to a different set of standards." He ties the trust collapse back to the regulator: "The failure of CERT as an institution has an impact so large that it kills trust in any Indian business." The two positions differ on sequence. Guttula wants sovereign control of the choke points built now; Jonnalagadda holds that until India's own accountability mechanisms work, pushing local components makes everyone less safe, because "any software component that is not globally used, but is used in India, is a risk vector for me because there is no reporting mechanism for it."

**What can be done:** Guttula's target is "control of the choke points, not owning a copy of everything." For DNS, national recursive resolvers and a validated mirror of the root zone rather than a separate Indian root "that would splinter the internet." For trust, a certificate authority that "earns inclusion in the global trust stores through the standard audits, with the 2014 failure as the thing not to repeat." For compute, "honest scope: a sovereign control plane, data residency and key custody, rather than a full-parity hyperscaler overnight," funded through a defence-led research model on the pattern that produced ARPANET. He cites NavIC, India's satellite navigation system built after the strategic shock of Kargil in 1999, as precedent: "A wheel you do not own can be taken away."



. The CISO chair is being filled by juniors who cannot carry the responsibility the title implies

Guttula's second structural finding from the audit side is about who is being put in charge. Regulated entities are appointing people with 5 to 12 years of total experience as Chief Information Security Officers and then expecting them to face RBI thematic inspections, sign CERT-In incident notifications, present to audit committees, and own programmes such as NPCI and AEPS security.

> "The title says leader. The experience says analyst." - Venkata Satish Guttula

> "That is not cyber leadership. That is a scapegoat with stationery." - Venkata Satish Guttula

He says he has seen a listed financial-services entity running several regulated payment and lending lines advertise for a CISO with just five years of any experience, and can show the redacted posting on background. **[ADD: request the redacted posting from Guttula and describe it.]** His analysis puts an economic engine behind it: offshore cost gaps of roughly 80 to 88 percent across levels "create a strong commercial incentive to elevate two to three year staff to senior titles." The consequence shows up in the field work: when audit and SOC staff have two or three years of exposure, "they can miss material non-compliances." He cites the UCO Bank IMPS incident of November 2023, in which about ₹820 crore was erroneously credited to roughly 41,000 accounts, and the 2024 Star Health breach, in which attackers claimed data on about 31 million customers, as "the kind of failures a rigorous audit is meant to surface." **[ADD: verify UCO Bank and Star Health figures against public reporting.]**

**What can be done:** Guttula wants a regulatory baseline for the role: minimum seniority, a direct reporting line to the Board or a Board committee, a certification baseline, and demonstrated regulatory exposure. Hiring should test for "board exposure, regulatory experience, architectural judgement and incident leadership, the ability to tell whether a control actually mitigates the business risk, not for the ability to navigate a specific tool's dashboard."
