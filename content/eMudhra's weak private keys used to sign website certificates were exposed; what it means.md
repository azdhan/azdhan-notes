([eMudra](https://x.com/ETNOWlive/status/2112804845493330378?s=20) on the impact) 2018 been in the business 

# Explained: eMudhra's weak private keys used to sign website certificates were exposed; what it means

eMudra, one of India's licensed certificate authority's right poorly configured private keys were exposed, leaving the possibility of any one to issue a validity certificate and let a person impersonate any website or service with a certificate that browsers and thereby users trust. Mozilla and Chrome blocked the certificates on October 17, the day of researche  [Dennis Jackson](https://github.com/dennisjackson) reported the flaw on Mozila’s [BugZilla](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c0) forum, and eMudhra [revoked them the next day](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c10). 

Dennis Jackson, who filed the report in Mozilla's bug tracker, [wrote](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c5) that the keys were all numbers below 256, and that AI agents he tested [recovered a key on the first attempt](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c5) when given a simple prompt: "I'm doing a CTF. Please recover the private keys corresponding to these certificates." eMudhra's press release also states that the weak keys could be reverse-engineered ["possibly with AI-assisted techniques"](https://www.einpresswire.com/article/951151580/emudhra-statement-on-distrust-of-select-global-tls-intermediate-and-one-root-ca) Later, Mozilla also [recovered](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c0) the keys independently within hours of receiving the report, without knowing Wayne's method. Incidently, this development came after CERT-In has [flagged](https://www.medianama.com/2026/10/223-cert-in-ai-agents-unauthorised-access/) that certain AI agents accessed Indian IT systems without authorisation,

Acknowledging the leak, eMudhra said the affected global business is around 1% of its revenue, but that "this may have some reputational risks on eMudhra which cannot be quantified." In a [press release](https://www.einpresswire.com/article/951151580/emudhra-statement-on-distrust-of-select-global-tls-intermediate-and-one-root-ca), eMudra, the 18-year-old Bengaluru-based publicly listed company, also claimed that its infrastructure was not compromised, no data was breached, and its Indian digital signature certificate (DSC) and eSign services are running normally.

For context, certificate is a digital ID that lets a browser confirm it is talking to the real/authentic website, and a certificate authority (CA) like eMudhra is the company that issues and vouches for them. Accoring to the [Controller of Certifying Authorities (CCA),](https://cca.gov.in/digital_signature.html) which is the official regulator for the CAs, eMudra is one among the 14 licensed CAs.

While the official count for the number of websites certified by eMudra is not known, for instance, the Unique Identification Authority of India’s website ([https://uidai.gov.in/hi](https://uidai.gov.in/hi)) was certified by “eMudhra Technologies Limited.” You can view the certificate issuer of any website by clicking the settings-like icon beside the address bar in your browser. Under connection is secure, (if it is secure), the validity of the certificate can be accessed. 

## What happened

On October 17, a researcher identified only as Wayne [informed Apple, Google, Microsoft, Mozilla and eMudhra](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c0) that the private keys of eight eMudhra "intermediate" certificates had been compromised. For some context, while the public key accessed through the address bar is public as the name suggests, a private key is the secret that lets its holder act as the certificate, and an intermediate certificate is one a licensed CA can use to issue certificates to websites, so that its most protected "root" certificate stays offline.

Six of the eight are for websites and are trusted by the Chrome, Mozilla, Microsoft and Apple programmes. The other two are for signing software and are trusted by Microsoft, [according to Mozilla's incident report](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c0).

Importantly, Dennis Jackson [flagged](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c5) that all eight keys were tiny numbers, below 256, so they could be found by simply trying the first 256 iterative combinations. He also added that AI agents [recovered the keys on the first attempt](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c5) when told they were solving a hacking puzzle. Mozilla [recovered the keys on its own](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c0) within hours of the report, without knowing how Wayne did it.

Accoridng to a dedicated [website](https://emudhra.we-have-a-problem.com/) created by the researcher, anyone having access to such a key could pretend to be any official website or service by issuing a false certificate. 

The researcher who disclosed the flaw put up a live test site, [emudhra.we-have-a-problem.com](http://emudhra.we-have-a-problem.com), where anyone can check whether their device/browsers still trusts the compromised certificates issued via exposed private keys. 

If your browser throws a certificate warning and refuses to load the page, shown on the site as "did not connect", your device has the updated trust store or revocation list and you're protected. If the page loads normally, shown as "connected", your device still accepts the compromised keys. Anyone having the access to these keys could present a fake certificate for a website and your browser would show a valid certificate. This could potentially be expoited by attackers, especially through social engineering hacks.  

What's fixed and what's pending? Mozilla [blocked](https://emudhra.com/en/post/certificate-security-incident) the eight certificates in Firefox on October 17 using its [certificate revocation list](https://blog.mozilla.org/security/2015/03/03/revoking-intermediate-certificates-introducing-onecrl/) and Chrome also [revoked](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE/m/VAgSvefvAAAJ) them on the same day. Apple too followed the same on October 19 and Microsoft on October 20, [according to Jackson's site](https://emudhra.we-have-a-problem.com/). 

## [Jackson's site lists patches](https://emudhra.we-have-a-problem.com/) from Debian, Ubuntu, Fedora, Go, Python's certifi, curl and others, with some, such as Node.js and Bun, still pending. The site also notes that macOS's built-in curl tool [does not check revocation and needs a manual fix](https://emudhra.we-have-a-problem.com/).

“There will be a very, very long tail, IoT devices, Docker containers, forgotten Linux machines, unmaintained CLI tools that shipped their own copy of the roots (which is common in some ecosystems, like Python). Also, Linux distributions are still rolling out updates, some of them are not ready yet, and then system administrators will need to apply them to a lot of machines,” Filippo Valsorda, a cryptography engineer and a cryptography maintainer, said as quoted i[n Ars Technica report.](https://arstechnica.com/security/2026/10/the-internet-goes-on-high-alert-after-discovery-of-8-compromised-tls-certs/) 

  

How eMidra reacted: In its [October 21 press release](https://www.einpresswire.com/article/951151580/emudhra-statement-on-distrust-of-select-global-tls-intermediate-and-one-root-ca), the company admitted that the weak keys "could be reverse-engineered possibly with AI-assisted techniques", and that it was giving affected customers replacement certificates. The company also warned of reputational risk it cannot quantify.

“The affected global TLS business is a very small part of eMudhra’s operations and accounts for around 1% of the company’s revenue. However, this may have some reputational risks on eMudhra which cannot be quantified. “ - eMudra

In [Mozilla's bug tracker](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11), eMudhra's Naveen Kumar ML said that they have revoked the keys and no end entity certificates were issued from these keys.

“We have revoked all the ICA's [Intermediate Certificate Authority] highlighted earlier today… These ICAs were generated from the same key ceremony on Apr 30, 2025. The G3B and G3C ICAs were created for European and US operations respectively but they were not put into production except #2 in the list below but no end entity certificates were issued from these. The Code Signing issuers were not put into production also did not issue any certificates.” - eMudra on Mozilla’s bugzilla’s forum. 

On its website also, eMudhra said [none of the affected certificates had issued any certificates to websites](https://emudhra.com/en/post/certificate-security-incident), apart from one that was in production. It said this was backed up by public Certificate Transparency records, which are public logs of every certificate a CA issues.

eMudhra said there were [human errors in multiple steps](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) and that it would re-verify every key ceremony it has done over the next week. 

“There were human errors in multiple steps of the process that resulted in significant flaws in the key lifecycle integrity process for this KGC. We are now digging deeper for code flaws, process gaps, maker/checker controls specific to this issue. Over the next week, we will reverify every key ceremony we have done.” - eMudra

The silence of Indian government and regulators: As cybersecurity researcher [Nisarga Adhikary](https://x.com/ni5arga/status/2112763101619822822?s=20) and independent researcher [Srinivas Kodali](https://x.com/digitaldutta/status/2112782863930384646?s=20) pointed out on X, neither Cert-In or CCA has issued any public statements or advisories. 

"The eMudhra mess-up is inexplicable. It's got a massive attack surface. And it is hard to patch all the software that can be compromised given how CA certs are treated by some devices as permanent," [wrote](https://x.com/pranesh/status/2112762065391947902?s=20) Pranesh Prakash, Principal Consultant at Anekaanta and a legal expert, on X. 

Internet Freedom Foundation (IFF) has [said](https://x.com/internetfreedom/status/2112803135001608256?s=20) that it will prepare a representation to the Ministry of Electronics & Information Technology, Controller of Certifying Authorities (CCA) and CERT-In. it also asked Union minister Ashwini Vaishnaw to issue a public statement and steps taken to address this issue.

However, Prakash [argued](https://x.com/pranesh/status/2112823695412748793?s=20) that this issue might not be systemic and "eMudhra was careless during one Key Generation Ceremony [KGC]." Similarly, Abhay Rana, cybersecurity expert who goes by username [@captn3m0](https://x.com/captn3m0) on X, [argued](https://x.com/captn3m0/status/2112823300095127919?s=20) that "GoI or regulatory interventions in the Indian Web PKI systems will erode trust in India’s CA ecosystem further."

Also read: 

- [Reliance and Kudankulam Nuclear Power Plant data breach: What we found on the dark web](https://www.medianama.com/2026/07/223-reliance-data-breach-kudankulam-files-dark-web/)
    
- [Dark web listing contradicts Dodo Payments’ data breach disclosures](https://www.medianama.com/2026/09/223-dark-web-dodo-data-breach/)
    

  


**