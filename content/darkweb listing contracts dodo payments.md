**# Dark web listing contradicts Dodo Payments' data breach disclosures

Dodo Payments, a Bengaluru-based payments company, [told](https://dodopayments.com/blogs/security-incident-internal-analytics-system) its customers on August 17 that a breach of an internal analytics system did not touch API keys, passwords, or account credentials. However, the threat actor’s website on dark web, reviewed by MediaNama, describes a stolen dataset from the company that includes the data types labeled as:

- “KYC verification requests, identity verifications and requests, bank verification requests, business phone and verification requests, UBO requests, payout compliance requests, payout bank accounts, additional verification requests, custom verification forms”
    
- “Fingerprint events with user emails, client IPs, thumbmark hashes and IP identifiers; visitor-merchant links; visitors”
    
- “Customer records (email, name, phone, metadata, search text); business records; business users; live customers”
    
- “Invoice records with customer emails and names, billing street/city/state/zip, tax IDs (DE366513651), metadata (created_from ad_creator_app)”
    

There are a total 58 such data types listed on the websites.

MediaNama has not independently verified the data on the dark website, and cannot confirm that the data it describes is authentic. It is also possible that the threat actors marketing stolen data may have a financial incentive to overstate its scope and sensitivity. The listing's claims are presented here as claims, not as confirmed facts. Even if the database is not public, unlike the [Kudankulam-Reliance data breach](https://www.medianama.com/2026/07/223-reliance-data-breach-kudankulam-files-dark-web/) incident,  we are not revealing the threat actor and the Tor/Onion URL of the website to prevent the further spread of the alleged leaked data. 

What did the Dodo payments say? In a blog post disclosing the incident, Dodo Payments said "Merchant API keys, dashboard passwords and account credentials are not stored in the affected system and were not accessed." Co-founder Rishabh Goel repeated the same on X, writing that "No passwords, API keys, webhook secrets, card numbers, or stored payment tokens were involved."

What we found on the dark web? Dated August 15, 2026, just a day before Dodo Payments’ public disclosure of the data breach, the index of the claimed data breach described the data leak as roughly 60.8 GB of data across four [ClickHouse](https://clickhouse.com/) databases and some 39.3 million rows, drawn from what it says are Dodo Payments' production and development analytics warehouses. 

Among the categories it names, in two separate production databases, is "Internal API & auth" data, which it says includes "API keys," alongside signup and login OTPs, signup tokens, and email-change records. That is roughly 375,000 rows in each database.

The listing does not make clear whether these are merchant-facing API keys of the kind Dodo Payments and Goel specifically denied were involved, or internal service-to-service keys used by the company's own infrastructure. Dodo Payments' statements do not address that distinction. The company did not respond to a request for clarification before publication. [placeholder, update once the company responds]

The listing also names a "Credentials" table among data drawn from [Keycloak](https://www.keycloak.org/), an identity management system Dodo Payments appears to have been using. The company's public disclosure did not mention this system by name or explain what it holds.

MediaNama has sent an email to Dodo Payments asking for the confirmation/denial of the claims on the dark website. We’ll update the copy once we receive the response.

Also Read: 

- [Kudankulam Nuclear Data Leaked On Dark Web: What We Found](https://www.medianama.com/2026/07/223-reliance-data-breach-kudankulam-files-dark-web/)
    
- [Ten things wrong with India's cybersecurity system: what the experts say](https://www.medianama.com/2026/07/223-india-cybersecurity-problems/)
    

  
  
  

Hi Team Dodo Payments,

I'm Azdhan, a journalist with MediaNama. I'm working on a story about Dodo Payments' August 17 disclosure of a security incident involving your internal analytics system. As part of my reporting, I've reviewed a listing on a dark web marketplace describing a dataset attributed to Dodo Payments.

Your [blog post](https://dodopayments.com/blogs/security-incident-internal-analytics-system) states that "Merchant API keys, dashboard passwords and account credentials are not stored in the affected system and were not accessed," and co-founder Rishabh Goel [stated](https://x.com/goelrishabh/status/2089356146213785622?s=20) on X that "No passwords, API keys, webhook secrets, card numbers, or stored payment tokens were involved."

 I'd appreciate your response to the following:

1. Are these claims true? Have you checked the index on the dark website that listed over 58 data types from the claimed data breach?
    
2.  Can you confirm or deny whether any API key values, merchant-facing or internal/service-to-service, were present in the data accessed during this incident?
    
3. Can you clarify whether the "Credentials" table referenced in the listing, apparently from a Keycloak deployment, was part of the affected system, and if so, what it stores?
    
4. Does the scope described in the listing, about 39.3 million rows across production and development databases, including KYC/KYB verification data, fraud/fingerprinting data, payout bank account records, and raw change-data-capture replication streams, match what your own forensic review has found so far?
    
5. Any other comment you'd like to offer on the discrepancy between your public statements and what this listing describes.
    

I'd appreciate a response by 4pm on September 1. Happy to hop on a call if that's easier. You can reach out to me at (91) 6309502648. 

Thanks,  
Azdhan.

  
  

[http://direwolfcdkv5whaz2spehizdg22jsuf5aeje4asmetpbt6ri4jnd4qd.onion/article/82](http://direwolfcdkv5whaz2spehizdg22jsuf5aeje4asmetpbt6ri4jnd4qd.onion/article/82)**