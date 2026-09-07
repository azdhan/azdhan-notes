**# Explainer: Meta is testing AI agent integration on WhatsApp. Here is what it means

  

Meta is currently developing features that allow users to connect and communicate with AI agents on WhatsApp, according to [WABetaInfo](https://wabetainfo.com/whatsapp-is-rolling-out-chats-with-third-party-agents/), which reports on the technical developments of WhatsApp based on its beta versions of the apps. 

  

Some of the features:

- Only limited up to five AI agents for personal use cases using the API keys. 
    
- AI agentic chats are not end-to-end encrypted (E2EE). 
    
- Agents are restricted to individual chats and cannot be added to groups, which prevents exposure to sensitive multi-party conversations. 
    
- Each agent has isolated chat access and cannot read other conversations, contacts, or media.
    
- Chat history is retained even after an agent is disconnected, which is useful for reference but also might raise data retention questions, as 'WhatsApp doesn't delete the chat history automatically.’ 
    

  

“WhatsApp is making the ability to create a chat for an agent available to a limited number of users. At the moment, WhatsApp is gradually rolling out this feature, and most users won't see the Agents section within the app settings right now. If the feature does not appear, it will become available in a future update. WhatsApp has not announced when it will extend this functionality to everyone,” wrote [WABetaInfo](https://wabetainfo.com/whatsapp-is-rolling-out-chats-with-third-party-agents/). 

Why this matters: 

- Adds flexibility to communicate with AI agents: Currently, [Telegram](https://hermes-agent.ai/how-to/connect-telegram-to-hermes), [Discord](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord), and Slack are the most accessible platforms for individual hobbyist users or developers to integrate AI agents. WhatsApp has historically restricted programmatic access to just the business API. 
    

- Meta's continued attempts for a 'super app': Mark Zuckerberg's plans of building a [super app](https://finance.yahoo.com/news/mark-zuckerberg-dreams-building-super-075931712.html) out of WhatsApp date back to the [Reliance-Jio deal](https://www.medianama.com/2022/08/223-whatsapp-jiomart-ecommerce-launch/) in 2022. Similarly, in December 2023, [Meta partnered with ONDC](https://www.medianama.com/2023/12/223-ondc-meta-partnership-whatsapp-small-businesses/) as well. However, the full e-commerce integration hasn't kicked off on WhatsApp yet. So, this might be yet another attempt to leverage AI agents for business use cases like e-commerce if the [agentic payment](https://www.medianama.com/2026/07/223-npci-agentic-payments-upi/) integration works fine as intended in non-personal commercial space. This move is similar to China’s super app WeChat, which recently [integrated](https://techwireasia.com/2026/06/wechat-ai-agents-super-apps/) an AI agentic chat interface into the app. We are not sure if we WhatsApp revives/strengthens these partnerships.
    
- To stay relevant and updated with competitors: iMessages already has [Apple Intelligence](https://www.medianama.com/2026/01/223-apple-build-ai-models-using-google-gemini-siri/) integrated. Similarly, Google has also [integrated](https://www.medianama.com/2024/06/223-google-gemini-app-launched-india-supports-9-languages/#:~:text=of%20Gemini%20with-,Google%20Messages%2C,-which%20the%20company) Gemini into its Android messaging app. Telegram already has a [mature bot ecosystem](https://telegram.org/blog/bot-revolution). Therefore, this is a Meta attempt to keep WhatsApp’s relevance as messaging apps continue to embed AI and AI-related tools directly into their platforms.
    
- Bot limitations might work for WhatsApp Plus: The beta versions state that one individual can create AI agentic connections via WhatsApp. However, this figure stands at [20](https://github.com/tginfo/Telegram-Limits/issues/288) for Telegram users and is [50](https://support.discord.com/hc/en-us/articles/360045093012-Server-Integrations-Page) integrations for Discord. This limitation also might be to leverage the recently rolled-out [WhatsPlus plan](https://www.medianama.com/2026/06/223-whatsapp-plus/). However, the WABetaInfo doesn’t specify separate pricing if the user intends to have more than five bots. 
    

After [Kunal Shah joined Whats App](https://www.medianama.com/2026/06/223-kunal-shah-cred-ceo-lead-whatsapp-meta/), Meta has been introducing new features. Some of them are: 

- Integration with the Bharat Bill Pay System (BBPS) network: This is to enable in-app bill payments. After this integration users can find, manage, and pay utility bills directly within the app. Some of the categories include electricity, water, and credit card bills. Read MediaNama coverage of this [here](https://www.medianama.com/2026/09/223-whatsapp-bill-payments-india/). 
    
- Usernames system: This will let the users connect without phone numbers during initial contact. Read MediaNama’s coverage of this [here](https://www.medianama.com/2026/06/223-whatsapp-usernames-users-reserve-handles-before-rollout-later-year/). Addressing this, MeitY secretary S Krishnan [called](https://www.medianama.com/2026/07/223-meity-whatsapp-signal-telegram-usernames/) usernames as ‘another dimension of cybercrimes.’ Later, as per the Hindustan Times report, MeitY is [considering](https://www.medianama.com/2026/07/223-meity-whatsapp-username-dispute-messaging-standards/) coming up with common standards for messaging platforms operating in India. 
    
- Browser-based calling: This lets the users make and receive audio and video [calls directly in browsers](https://blog.whatsapp.com/introducing-web-calling-on-whatsapp-plus-more-new-updates). Earlier, you could only make calls using the dedicated WhatsApp application.
    

What is the current unofficial way to connect your AI agent to WhatsApp: Before Meta’s plans to add official third-party AI agent support, developers who wanted to connect an AI agent to WhatsApp had an unofficial workaround, like reverse-engineered bridges that mimicks the WhatsApp Web client. The most popular is Baileys, an open-source library. 

How Baileys’s protocol works: These tools act as a headless browser or protocol client, logging into WhatsApp the same way you would scan a QR code to access WhatsApp Web on a laptop. Once paired, the bridge exposes a programmatic interface. Your AI agent connects by listening for incoming messages, passing the text to its inference pipeline, and sending responses back through the same. Read the full guide on how to connect the Hermes agent to WhatsApp [here](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/whatsapp). 

  

However, using the unofficial workarounds might lead to the risk of banning and opening for new security risks, as it might violate its terms of service. Additionally, if WhatsApp makes any changes, the Bailey’s protocol might not work, and there can’t be official support. 

  

Also Read: 

- [Mozilla President Mark Surman on AI agents, the future of browsers, and a new browser war](https://www.medianama.com/2026/04/223-browsers-future-ai-agents-mark-surman/)
    
- [How NPCI should approach agentic payments](https://www.medianama.com/2026/07/223-npci-agentic-payments-upi/)
    

  

Subject: 

  

Media inquiry: WhatsApp AI agent features (beta)

Hi Meta Press Team,

I’m a tech journalist at [MediaNama](https://www.medianama.com/author/azdhan-basha/). I am covering the new [AI agent features](https://wabetainfo.com/whatsapp-is-rolling-out-chats-with-third-party-agents/) in WhatsApp’s beta. 

I’d appreciate your comments on a few points:

1. Why aren’t AI agent chats end-to-end encrypted, and what protections exist for user data shared with these agents? Is there any technical reason behind the feasibility of enabling E2EE for AI agentic conversations?
    
2. What’s the retention policy for disconnected agents, and will users have a clear way to permanently delete this history?
    
3. What support or transition period will you offer developers moving from unofficial workarounds to official methods to avoid sudden account bans?
    
4. What’s the reasoning behind the 5-agent limit for personal users, and is this linked to a "WhatsPlus" plan (e.g., tiered pricing for additional agents)?
    
5. Does this integration set the stage for agent-based commerce or automated payments (e.g., NPCI) in India?
    

We’re on a deadline and would appreciate a response by Sepember 7, 5 pm. Happy to take brief on-the-record comments or a quick call if a full statement isn’t ready.**