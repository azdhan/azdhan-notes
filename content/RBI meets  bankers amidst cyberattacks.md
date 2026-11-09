**# RBI meets bankers amidst rising cyberattacks on Indian financial system and mandates audits

Amidst the rising [AI-assisted cyberattacks](https://www.medianama.com/2026/10/223-cert-in-ai-agents-unauthorised-access/), especially on the [financial sector](https://www.medianama.com/2026/11/223-cert-in-ai-threat-actor-bfsi-payment-api/), the Reserve Bank of India (RBI), India's central bank and main regulator for the banking sector, has possibly for the first time met the bankers to address this issue since [Cert-In's advisories started](https://www.medianama.com/2026/10/223-hackers-kyc-api-hijacks-cert-in-fintechs/) related to the vulnerabilities reported in the Indian financial system.

According to an exclusive report by [Head and Tale's Arti Singh](https://theheadandtale.com/deepdives/exclusive-rbi-tightens-api-security-rules-for-banks-after-nbfc-cyberattacks-mandates-audits-beneficiary-checks/), the RBI also reportedly held a nearly two-hour meeting with banks on Wednesday and issued a "confidential advisory" dated November 3. The banker told the reporter that the regulator "gave banks a dressing down" and stressed that banks are responsible for securing these arrangements. The banker also stated that individual frauds ranged from Rs. 3 crore to Rs. 15 crore, adding that the number of attempts worried banks more.

The RBI’s confidential advisory reportedly also asked NBFCs which use APIs for a security audit by CERT-In empaneled auditor. These are the independent auditing companies which are approved by the Ministry of Electronics and Information Technology. A full list of cybersecurity organizations which are listed on CERTIN's website can be accessed [here](https://www.cert-in.org.in/PDF/Empanel_org.pdf).

CERT-In names a threat actor: The recent CERT-In's [November 4 advisory](https://www.medianama.com/2026/11/223-cert-in-ai-threat-actor-bfsi-payment-api/) named a threat actor, "CRAFTY FALCON". It said attackers used Rs. 1 transfers to test fund flows before larger transactions. It also said they bypassed IP allow-listing by routing traffic through shared third-party IP pools. CERT-In recommended beneficiary cooling periods and maker-checker approval for merchant settlements. Similarly, CERT-In has issued a similar notices, you can catch up them [here](https://www.medianama.com/2026/10/223-cert-in-ai-agents-unauthorised-access/) and [here](https://www.medianama.com/2026/10/223-hackers-kyc-api-hijacks-cert-in-fintechs/).

The next day, after the RBI’s November 3rd meeting, the Indian Cyber Crime Coordination Centre (I4C), which works under the Ministry of Home Affairs (MHA), issued a [public advisory](https://www.cert-in.org.in/PDF/Empanel_org.pdf) on AI-assisted attacks on banks, NBFCs and fintechs. Both concern the application programming interfaces (APIs) that lenders use to disburse money. 

Similarly, on the same day, CERT-In released Artificial Intelligenc (AI) Security Auditing Guidelines. Read MediaNama’s lowdown of the guidelines [here](https://www.medianama.com/2026/11/223-lowdown-cert-in-ai-security-auditing-guidelines/). 

The advisory sets the following requirements, according to the Arti’s report:

- Maintain a full API client inventory. The regulator has asked banks to capture business profile, services used, account and integration details, transaction limits, and key business, technical and security contacts.
    
- Require CERT-In audits for NBFC clients. The regulator has said the audit must be completed before onboarding new NBFCs, while existing clients have until February 3, 2027.
    
- Conduct audits at least once a year. The regulator has reportedly asked banks to repeat the audit after any material cyber incident and to track completion and act on non-compliance.
    
- Risk-assess non-NBFC API clients immediately. The regulator has asked banks to require a periodic audit within three months for BCs, PAs, PSPs and fintechs, sooner if risk is higher.
    
- Brief all API clients every three months on the current threat landscape, as per the regulator's advisory.
    
- Bring API transactions under fraud-risk and monitoring frameworks. The regulator has asked banks to set thresholds and behavioural baselines per client.
    
- Flag material deviations. The regulator has said banks must watch for volume or value spikes, transactions just below limits, odd-hour or holiday activity, bursts of new beneficiaries, mule patterns, failed log-ins and invalid API requests.
    
- Monitor technical fingerprints. The regulator has asked banks to watch for changes in user-agent, app version, OS and network attributes, with technical changes due by December 3.
    
- Secure banks' own API infrastructure. The regulator has said banks must cover access management, network segmentation, patching and monitoring, as attackers may pivot through a compromised client.
    
- Enforce beneficiary whitelisting. The regulator has asked banks to pre-register verified end-customer accounts per client, reject unregistered payouts, and allow additions or modifications only via a separate MFA-protected channel.
    
- Enforce maker-checker or out-of-band confirmation. The regulator has said banks must add extra authorisation for API debit requests via a separate channel, applying it to all transactions or those above a risk-based threshold.
    
- Require at least one safeguard from regulated entities using API-based fund transfers. The regulator has said new integrations must comply before they go-live, while existing ones have time until December 3, 2026.
    
- Make debit information available quickly so clients can reconcile transactions one by one, as per the regulator's direction.
    
- Allow narrow, case-by-case exceptions only for highly automated payments where neither control is practical. The regulator has said a written application and documented risk assessment are required.
    
- Set per-transaction and daily cumulative limits effective immediately. The regulator has asked banks to calibrate them to declare and observe business profile and risk.
    
- Implement intra-day or velocity limits within one month to prevent bursts of transactions. The regulator has said material limit increases need a documented risk assessment.
    
- Treat maker-checker as a compensating safeguard for intra-day limits if commensurate with risk and documented, as the regulator has allowed.
    
- Enforce immediate incident reporting and recovery. The regulator has asked banks to ensure clients promptly report any actual or suspected compromise of systems connected to API-based payments.
    

‘AI agentic driven cyberattacks concerns CERT-In’

CERT-In Director General Dr Sanjay Bahl, in written answers to MediaNama on November 2 and 3, described what worries the agency. He asiad that “delegated authority without commensurate guardrails and that AI agents are being trusted faster than they are being secured” concerns India’s nodal cyber security agency. MediaNama’s interview predates the RBI’s confidential advisory becoming public. [Read the full interview here.](https://www.medianama.com/2026/11/223-interview-cert-in-chief-ai-agents-prompt-injection/)

“What would change is the speed, scale and level of automation at which cyber activities take place. Defensive capabilities would therefore need to evolve accordingly from human-speed monitoring and manual containment to continuous, automated machine-speed defence.” – CERT-In Director General Dr Sanjay Bahl.

MediaNama’s recent coverage related to cybersecurity issues and data breaches:

1. [AU Small Finance Bank](https://www.medianama.com/2026/10/223-au-small-finance-bank-data-leak-dark-web/) is probing a "potential data leak" on a Salesforce-hosted platform after hackers claimed a breach. The bank says its systems are unaffected.
    
2. [CoinDCX](https://www.medianama.com/2026/10/223-coindcx-cyberattack-rs-152-crore-loss/) first dismissed reports of a breach, then confirmed a loss of about Rs. 152 crore.
    
3. [Central Bank of India](https://www.medianama.com/2026/10/223-central-bank-of-india-rs-13-97-crore-fraud/) alleges hackers siphoned off Rs. 13.97 crore through its financial messaging system. It says it could not trace 187 transfers.
    
4. [SBI](https://www.medianama.com/2026/10/223-sbi-data-breach-3897-customers-dark-web/) confirmed a suspected breach of 3,897 customer records. It has not said whether customers were told.
    
5. [CBFC](https://www.medianama.com/2026/10/223-cbfc-data-breach-censor-cuts-distribution/) reportedly exposed scripts, distribution deals and censorship records for over 500 films. The board says it found no trace of the documents.
    
6. [Amagi Media Labs](https://www.medianama.com/2026/10/223-amagi-media-operational-data-stolen/) faces an extortion attempt from a hacker claiming to hold operational and network data.
    
7. [eMudhra](https://www.medianama.com/2026/10/223-emudhra-ssl-tls-exit-regulatory-accountability/) is exiting the SSL/TLS certificate business days after researchers exposed weak private keys in eight intermediate certificates.
    
8. [Railway](https://www.medianama.com/2026/10/223-railway-api-cyberattack-customer-secrets/), a cloud hosting platform, asked users to replace API keys after a cyberattack potentially exposed customer secrets.
    
9. [CERT-In](https://www.medianama.com/2026/10/223-cert-in-ai-agents-unauthorised-access/) disclosed that AI agents accessed live Indian systems without authorisation during research and evaluation.
    
10. [Anthropic](https://www.medianama.com/2026/11/223-anthropic-claude-ai-hacks-chrome-android-windows-linux/) said its Claude model found vulnerabilities across five targets, including Chrome, Android, Windows and Linux. It has not disclosed its success rate or computing costs.
    

Also read:

- [CERT-In flags an AI threat actor targeting BFSI payment APIs](https://www.medianama.com/2026/11/223-cert-in-ai-threat-actor-bfsi-payment-api/)
    
- [Interview: CERT-In chief on AI agent incidents](https://www.medianama.com/2026/11/223-interview-cert-in-chief-ai-agents-prompt-injection/)**