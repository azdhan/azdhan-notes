**# Explainer: What is NPCI's AI-powered MyUPI and what we found while using it

The National Payments Corporation of India (NPCI) has launched AI-powered chatbot version of UPI Help, MyUPI. NPCI’s [press release](https://www.npci.org.in/uploads/NPCI_Press_Release_RBI_Governor_Unveils_New_UPI_Capabilities_at_GFF_2026_AI_Powered_Customer_Support_and_Seamless_Tap_and_Pay_Experience_bb763a7670.pdf) describes as being built using in-house "Small Language Model" called FiMI, Finance Model for India. NPCI announced this on September 10 at Global Fintech Fest 2026 and l;aunched today intending it as a single view of their UPI transactions and AutoPay mandates across third-party UPI apps.

“MyUPI is an AI-enabled support and service platform designed to help end-users of participating banks and UPI Apps, access and manage certain UPI features. Any information, responses, insights and assistance provided through MyUPI, including those generated through automated technologies or artificial intelligence, are intended solely for information and support purposes only and should not be treated as advisory or a substitute for independent judgment. Any action requested through MyUPI shall be subject to the applicable verification / authentication, consent, validation, regulatory requirements and approval processes of the relevant participating banks and/or UPI app, as the case may be.” – NPCI’s disclaimer on [MyUPI website](https://www.upihelp.npci.org.in/). 

MediaNama tested AI chatbot against NPCI's own privacy policy and terms of use, both effective September 1, 2026. We found that several of the features NPCI announced, including Safety Switch and Automated Chargeback Processing, don't appear to work yet. According to the privacy policy and terms of use, it is stil unclear whether user transaction data is being used to train the NPCI’s FiMI model, or how a AI chatbot built to become the so-called "proactive trust and safety" can “enable users to request declining of UPI debit transactions in case of a suspected compromise.” (It can’t).

What model is actually behind FiMI? The press release states that MyUPI uses FiMI NPCI's Small Language Model FiMl. Its an acronym for “[Finance Model for India](https://www.medianama.com/2026/02/223-fimi-npci-in-house-ai-model-upi-ecosystem/).” You can read the technical paper on FiMI [here](https://arxiv.org/html/2602.05794v2).

According to the Section 9 of the MyUPI [terms of use](https://www.upihelp.npci.org.in/), "Third Party Products and Dependencies," which lists the following models and tools that were used in "the creation, training or operation of MyUPI":

- [Mistral Small 24B Instruct 2501](https://huggingface.co/mistralai/Mistral-Small-24B-Instruct-2501)
    
- [Mistral NeMo](https://mistral.ai/news/mistral-nemo)
    
- [Llama 3](https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md)
    
- [SmolLM2](https://arxiv.org/abs/2502.02737)
    
- [BERT](https://arxiv.org/abs/1810.04805)
    
- [Gemma 3](https://arxiv.org/abs/2503.19786)
    
- [FineWeb](https://openreview.net/forum?id=n6SCkn2QaG)
    

BERT is Google's 2018 encoder model, typically [used](https://www.nvidia.com/en-us/glossary/bert/) to pre-train deep bidirectional data from unlabeled text. According to NVDIA, this process makes the enables to train and process the data quickly. [FineWeb](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fineweb-v1) is also not a language model. It's a large web-text dataset for pretraining language models. 

Separately, RazorPay recently [launched](https://www.medianama.com/2026/08/223-razorpay-vulcan-ai-foundation-model-payments/) a foundational model trained specifically on the payments data. Read more about it [here](https://www.medianama.com/2026/08/223-razorpay-vulcan-ai-foundation-model-payments-2/). 

What we found: 

The “Pay Safe” feature also doesn’t fulfill the intended function. When the user types the VPA ID or scans a QR to auto-fill the VPA, the “Payee Context Information” doesn’t provide any useful information except a few cautionary alerts which the user might already knows. 

MyUPI’s [privacy policy](https://www.upihelp.npci.org.in/) states that this feature does not generate "reputational ratings, blacklist classifications or recommendations to transact or not transact with a particular beneficiary." It further stated that it only gives the "factual, contextual" information already available in NPCI's systems.

PIC

While this feature largely doesn’t have a real-life use cases, there is a limit to how many times you can check a particular VPA. After three attempts it shows: “You have reached the daily limit to check the vpa.”  

NPCI announced a feature called “Safety Switch,” which apparently could “enable users to request declining of UPI debit transactions in case of a suspected compromise.” But, at present, there is no such feature. When MediaNama asked the AI-powered chat bot to turn on this feature, it said: “I don't have specific information about the Safety Switch feature” and prompted to features like UPI Circle and Fraud Risk Management (FRM).  

The “Automated Chargeback Processing” feature which is supposed to enable “real-time chargeback creation for eligible transactions,” is also not implemented yet. While there is no separate feature for this, when we asked the chatbot for the “Automated Chargeback” of Rs 2 transaction, the chatbot had no response.  

The "learn about scams" section only lists a few online news stories from the previous years March to August. The chatbot links out to news stories of [NDTV](https://www.ndtv.com/india-news/hyderabad-company-cyber-fraud-rs-1-95-crore-boss-message-whatsapp-whatsapp-message-from-boss-how-hyderabad-firm-nearly-lost-rs-1-95-crore-7923420), [Times of India](https://timesofindia.indiatimes.com/city/kochi/scam-spread-via-whatsapp-hack/articleshow/122843971.cms) and [Hindustan Times](https://www.hindustantimes.com/cities/bengaluru-news/bengaluru-woman-falls-for-kerala-lottery-trap-loses-rs-11-8-lakh-to-scammers-posing-as-cops-101755744875008.html).

NPCI says the platform will offer 24x7 multilingual. However, users have to toggle the language of the whole user interface to interact with the AI model FiMi. However, at present, MyUPI only supports five indian languages: English, Hindi, Tamil, Telugu and Bengali.

What data does MyUPI collect? The [privacy policy](https://www.upihelp.npci.org.in/) lists six categories of personal data NPCI can collect through MyUPI, depending on the service used:

- Identity and contact information: mobile number, device-bound mobile identifier, UPI ID/VPA, beneficiary UPI ID, linked bank details, masked account information
    
- Transaction information: transaction reference number (RRN), amount, date and time, status, merchant details, mandate information, complaint and chargeback references
    
- Device and technical information: device type, OS, browser, IP address, session and application identifiers, security logs
    
- User interaction information: queries submitted through MyUPI, chat conversations, complaint narratives, feedback and any uploaded supporting documents
    
- Consent and authentication information: consent records, OTP validation, Safety Switch and mapper-delink requests
    
- Analytical user spend information: spending patterns, spending categories, aggregated transaction insights and usage analytics
    

Is users’ financial data used to train the AI? We don’t know. Section 5 of the privacy policy, "AI-Assisted Processing," says FiMI is used for query resolution, complaint intake, chargeback recommendations, spend-analysis explanations and generating payee context information. 

However, it does not say whether the transaction, chat or spend data collected from users is used to train, fine-tune or otherwise improve FiMI or the underlying models. The policy commits only to not selling personal data and to retaining data for "the minimum period necessary."

AI responses are just informational nature and it can’t the decisions: The privacy policy is explicit that AI-generated outputs are "advisory and informational" and that MyUPI does not let AI make final calls on approving or declining transactions, restricting account access, blocking users, or executing chargebacks. NPCI states that these remain with "deterministic systems and rule-based workflows," subject to human and system oversight. 

The terms of use separately warn that AI-generated responses may contain "hallucinations" and should not be the sole basis for any financial decision.

Data sharing, security and retention: NPCI says it does not sell personal data. Beyond this, it will share the user data with “participating banks” and Payment Service Providers (PSPs) and Third-Party Application Providers (TPAPs for complaint processing, chargebacks, Safety Switch actions and mandate management, with infrastructure and security service providers under some confidentiality obligations, and with regulators’ requirements where required. 

Stated security measures include AES-256 encryption, RSA-2048 key protection, TLS 1.3, mutual TLS and token-based authentication. Data is meant to be retained only for the minimum period necessary and then deleted, anonymised or archived, though the policy does not specify concrete retention timelines for each data category. 

Also Read:

- [Razorpay CEO Harshil Mathur on building Vulcan](https://www.medianama.com/2026/08/223-razorpay-vulcan-ai-foundation-model-payments-2/)
    
- [MeitY proposes mandatory human-in-the-loop interventions in agentic AI payments](https://www.medianama.com/2026/07/223-meity-proposes-mandatory-human-interventions-agentic-ai-payments/)**