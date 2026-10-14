	**

# Cyberattackers are bypassing KYC through APIs, CERT-In warns NBFCs and fintechs

Access the original advisory here: [ [CERT-In](https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0046&pageid=PUBVLNOTES02) | [Machine readable format](https://www.medianama.com/wp-content/uploads/2026/10/cert-on-advisoy-to-the-iintechs.txt) ] 

The Indian Computer Emergency Response Team (CERT-In) and its finance-related cybersecutity arm CSIRT-Fin have warned the non-banking financial companies (NBFCs), digital lending platforms, fintech firms, payment service providers and wallet operators about coordinated cyber attack campaigns that are resulting in the unauthorised fund transfers. It also noted that these attacks may have used AI tooling for the attacks.

The advisory was issued on October 9, 2026 and carries a "Critical" severity rating. However, the advisory which follows a standard CERT-In language does not name any affected entity, and does not say how many incidents it has seen or how much money has been stolen/movied.  

‘Observed multiple cyber attack campaigns by passing KYC requirements’ says CERT-In: According to the advisory, threat actors compromise internet-facing applications, exposed APIs and privileged endpoints. They then steal payment aggregator or gateway credentials and partner-bank API credentials, and "invoke disbursal/fund-transfer APIs directly from within the entities' own whitelisted infrastructure."

Because these API calls are being made directly to the payment APIs, the attackers bypass application-level controls such as loan creation, KYC, sanction, beneficiary verification, balance sufficiency and per-transaction limits, the advisory says. The fraudulent transactions "carry dummy reference identifiers, exceed per-transaction limits, and credit funds to attacker-controlled mule accounts across multiple banks." The advisory adds that funds are moved quickly through IMPS and NEFT rails and withdrawn immediately.

‘Possible use of AI-assisted offensive tooling,’ says CERT-In: It further added that with the interval between initial compromise and the fraudulent transfer "reducing significantly in recent incidents." Attacker IP addresses are mostly linked to hosting infrastructure. The advisory also states they also delete or truncate logs, tamper with endpoint detection and response (EDR) tools, and carry out "anti-forensic cleanup."

Concerning the usage of AI in the cyber attacks, Venkata Satish Guttula, independent cybersecurity and information systems (IS) audit consultant, said: 

"Attackers have already pulled capable AI into their workflow. They do not take management approval, run a change board, or write a risk register entry before they act. Defenders wait for a budget cycle and a circular. The asymmetry is no longer subtle." – Venkata Satish Guttula. 

What the advisory recommends: CERT-In asks entities to enforce MFA on payment platforms, admin portals and bank APIs, replace long-lived static tokens with per-session authentication, and decommission unused APIs. Find the full list of recommendations either on CERT-In website or access a machine readable format here. 

  

Why an advisory note alone may not be enough: Though the recommendations are technical, they are mostly well-known data security mechanisms. In MediaNama’s previous longform story about the list of cybersecurity issues in India, several experts highlighted the lapses at CERT-In. Some of them are: 

Experts MediaNama spoke to for a [recent story on the problems in India's cybersecurity system](https://www.medianama.com/2026/07/223-india-cybersecurity-problems/) pointed to several reasons why it may not.

Kiran Jonnalagadda, co-founder of HasGeek, described the same gap: 

"Everything with CERT-In is like a privilege. If they feel like it, they will do something. If you cannot hold them responsible for delivering the service, then it's not a service. It's a privilege."

While the advisory and CERT-In routinely asks for reports, it offers back too little or nothing in return: The advisory ends by asking affected entities to report to CERT-In/CSIRT-Fin. Jonnalagadda said the existing arrangement runs one way:

 "By design, CERT-In will tell you nothing, but you tell CERT-In everything. That would have been fine if CERT-In had something holding it accountable for its confidentiality. But where in the law is anything that says CERT-In is accountable for the confidentiality of the report it receives? All of that is a black hole… They simply are a data demander. It is not obvious why any company should ever bother reporting to CERT-In."

A former analyst at information security firm SISA, who spoke on condition of anonymity, said: "When you report to CERT-In, I honestly don't know what happens… What's the government's role in this, that even I don't know. There's no recourse. Basically, the conclusion is there's no proper recourse to this."

Compliance on paper can sit alongside weak security. Many of the advisory's recommendations, such as API inventories, secret management and log retention, can be shown on paper as a compliance without full implementation. 

 "Reasonable security measures have been interpreted to mean adherence with security standards. ISO 27001, SOC 2, all of this is stemming from the fact that reasonable security measures could mean anything. They don't have a security program, but they have a certification. So that's reasonable security measures done." – Security Researcher Karan Saini 

Also Read: 

- [Ten things wrong with India's cybersecurity system: what the experts say](https://www.medianama.com/2026/07/223-india-cybersecurity-problems/)
    
-  [CERT-In Releases Blueprint to Counter AI-Assisted Cyber Threats](https://www.medianama.com/2026/05/223-cert-in-releases-blueprint-for-defending-against-ai-assisted-cyber-threats/)
    

  

  


**