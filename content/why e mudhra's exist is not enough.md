 **# Why eMudhra’s exit as the Certifying Authority is not enough

eMudhra, one of India's 14 licensed certificate authorities, said that it will withdraw from the global SSL/TLS certificate business, according to a [press release](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business) issued on October 22. The decision comes five days after cyber security researchers [reported](https://www.medianama.com/2026/10/223-emudhra-security-flaw-weak-private-keys-explained/) that the private keys of eight eMudhra intermediate certificates were too weak that could be exploited. 

For context, an SSL/TLS certificate refers to the identification and the verification of a particular website’s domain name and thereby establishes an encrypted network connection to another system using the Secure Sockets Layer/Transport Layer Security (SSL/TLS) protocol. Read more about this on [AWS website.](https://aws.amazon.com/what-is/ssl-certificate/) 

The company clarified that its other services like global digital signature certificate (DSC), which is generally used to sign electronic documents such as PDFs, tax filings, or corporate forms and other signing services, including those in India, along with enterprise products like its identity verification solutions remain functional. 

After the weak security keys were exposded, browsers like Mozilla and Chrome blocked the certificates on October 17, Apple followed on October 19 and Microsoft on October 20. 

Chairman V. Srinivasan claimed that the company "handled the recent incident diligently", revoking the affected CAs within 14 hours of discovery. The release repeated that no end-entity certificates were issued from the affected CAs, that its infrastructure was not compromised, and that no data was breached.

“..after detailed deliberations our board has concluded that withdrawing from global SSL/TLS is the right decision for eMudhra and its shareholders.” – eMudhra

What is eMudhra’s reasoning behind the exit: The company gave three reasons, including the incident itself.

1. Social media pushback and scrutiny that followed: "The level of social media amplification around this incident has brought scrutiny that is out of proportion to SSL/TLS's place in our business."  
      
    Earlier, after the weak keys were exposed, it said that eMudhra’s affected global business impact was around 1% of its revenue, but said that the incident could pose reputational risks that “cannot be quantified”.  
      
    
2. Compliance costs: "Due to increasing data sovereignty & compliance requirements, complexity and cost associated with this business is increasing over the years."  
      
    
3. Competition and the reduced profits: ”This, paired with the fact that some of the large entities issue the SSL/TLS free of cost, the business potential and RoI of this line of business also has considerably reduced for eMudhra when measured against our cumulative revenue base.”
    

Websites with eMudhra certificates have already started to update their certifiactes. For instance, when the keys were exposed, the Unique Identification Authority of India’s website ([uidai.gov.in](https://uidai.gov.in/hi)) listed “eMudhra Technologies Limited” as its certificate issuer. 

  

However, right now, the UIDAI website was certified by not the [other 13 ilicensed certificate issuers](https://cca.gov.in/digital_signature.html), but the US-based “[Sectigo Limited](https://www.sectigo.com/).” The company said it will contact affected customers to replace certificates free of cost "from partners". It has not specified which partners. 

What was MeitY and CERT-In’s response: On October 21, a day before the company announced the exit, MeitY [said](https://x.com/GoI_MeitY/status/2112914708261179404?s=20) that "some social media accounts are indulging in fear mongering about the impact of this incident". The minsitry also added that the Controller of Certifying Authorities (CCA), which regulates certifying authorities (CAs) in India, "remains completely unaffected by this incident."

On the same day. CERT-In [published an advisory](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0050) summarising the incident and listing best practices. It acknowledged that an attacker able to exploit the compromised TLS private keys "could issue fraudulent TLS certificates and potentially impersonate legitimate websites or intercept or modify data exchanged between users and servers". 

It also acknowledged that this could facilitate credential theft, sensitive data exposure and financial fraud, and that compromised code-signing keys could make malicious software appear to be signed by a trusted publisher.

However, even after the five days of the incident, the CCA, the regulator that licenses eMudhra, had not issued any public statement. 

MediaNama take: MeitY was rightfully [pushed back](https://x.com/nixxin/status/2113229825879978242?s=20) against its nonchalant reaction to the possibly world’s weakest security keys that are used to certify the legitimacy of websites. Just for context, these were the keys used: 4, 56, 66, 115, 155, 156, 230, and 237, according to the cyber security researcher [Scott Helme](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/).

“Not a number that starts with 4, or the number 4 followed by a few hundred random digits, just, 4... Another one is 56, and another is 115. I know, because I recovered all of them from their public certificates on my laptop just now, and it took less than a second.” –  [Scott Helme](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/), cyber security researcher.

Seriously, who keeps a single digit as a security key for anything? This could have exposed both websites and users to various types of vulnerabilities and possible scams. 

“The problem is that with that an attacker could create a certificate and, if they could get in the traffic flow, intercept traffic to any site or service.” – [Matthew Prince, CEO of Cloudflare.](https://x.com/eastdakota/status/2112933115215905229)

What Cloudflare CEO was referring to is generally called as man-in-the-middle attacks, where the cyberattackers can possibly impersonate a legitimate website like a bank website, if they have access to the eMudhra’s or any other certificate issuer’s private keys. These keys could be exploited to generate the valid certificates to the fake websites. 

Moreover, the risk described in the CERT-In advisory, which comes under the MeitY', also echoes what researchers and browsers acted on. Additionally, eMudhra himself acknowledged the keys could be "reverse-engineered possibly with AI-assisted techniques", warned of reputational risks that "cannot be quantified", and attributed the incident to "human errors in multiple steps of the process". And, finally, it announced the complete exit from the certification  business. 

So, what does MeitY’s description of this eMudhra incident as “fear mongering” explain to us if not the incompetency of the Minsitry’s risk assessment and the real-life impact?

Similarly, if the “fear mongering” is true, what explains the exit of eMudhra from the website certification business? Are compliance costs and so-called reputational concerns the only reasons for its exit? Possibly.

Nonetheless, an independent audit must be carried out to weigh the impact of this and identify the websites that were issued the certifiactres under these weak private keys to make the responsible people accaounable. 

How is this not a violation of [Section 30 in The Information Technology Act,](https://indiankanoon.org/doc/371543/) 200 that mandates the  Certifying Authorities to "adhere to security procedures to ensure the secrecy and privacy of the electronic signatures" and "observe such other standards" by the regulations? The authorities should also do a broader audit to rule out the possibility of no more weak security keys across the remaining 13 CAs.

Will there be a regulatory action against e Mudhra by CCA? We are sure if there will be any accountability action taken against the company, potentially for maintaining the poor cybersecurity standards and exposing the websites that it might have certified using those weak private keys. 

"They should undergo a thorough Digital and Financial Forensic Audit and their assets should get frozen with immediate effect." [suggested](https://x.com/CreativeWolf/status/2113256534952247335?s=20) an X user who goes by username @CreativeWolf, who apparently works in the information security sector. 

When the Internet Freedom Foundation (IFF) said that it would write to MeitY, the CCA and CERT-In and asked Union Minister Ashwini Vaishnaw to explain the steps taken, legal expert Pranesh Prakash [argued](https://x.com/pranesh/status/2112823695412748793?s=20) the incident may not indicate a systemic problem and that eMudhra "was careless during one Key Generation Ceremony", but he also called the lapse "inexplicable". 

Abhay Rana, a cybersecurity expert who goes by the name @captn3m0 on X [cautioned](https://x.com/captn3m0/status/2112823300095127919?s=20) that regulatory intervention could erode trust in India's CA ecosystem.

Also Read:

- [Explained: What are the two PHP vulnerabilities behind a global rush to update and why it matters](https://www.medianama.com/2026/10/223-php-vulnerabilities-global-rush-update/)
    
- [Ten things wrong with India’s cybersecurity system: what the experts say](https://www.medianama.com/2026/07/223-india-cybersecurity-problems/)**