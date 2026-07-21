


deploying open-source models locally was the only economically viable way to bypass the prohibitive costs and limits associated with massive-scale, continuous vulnerability scanning. 

In the speed-race of modern cybersecurity—detection, verification, coordination, and patching across systems—access to powerful open-source LLMs that can be modified and run cost-efficiently at scale is far more critical than having the absolute best model at any moment.

 [Clement Delangue, Huggingface’s CEO, points out that ‘the Mythos moment’ is asymmetrical in its impact](https://x.com/ClementDelangue/status/2046245285613969481): it helps the defenders more when it comes to FOSS, but attackers more when it comes to proprietary software. Historically, proprietary software relied on ‘security through obscurity’: hoping that obscuring the source code makes software harder to exploit. FOSS (and all of cryptography) relies on openness for security, captured in the dictum “[given enough eyeballs, all bugs are shallow](https://en.wikipedia.org/wiki/Linus%27s_law)”. Delangue argues that since LLMs [can now read stripped binaries](https://aclanthology.org/2024.emnlp-main.203.pdf) (the part that proprietary software cannot hide), legacy proprietary firmware running in critical information infrastructure (CII) is suddenly legible to automated analysis and attacks. But FOSS is better protected since independent developers can use diverse AI toolchains (as long as they aren’t regulated away) to investigate and fix bugs—“given enough eyeballs” simply evolves into “given enough eyeballs and AI agents and computing power.”

In 2019, OpenAI initially held that [GPT-2 was too dangerous to release](https://www.theguardian.com/technology/2019/feb/14/elon-musk-backed-ai-writes-convincing-news-fiction), though that was clearly false. Now Anthropic is saying the same thing. We should learn to ignore such self-serving hype, and urgently push for FOSS and open models for the sake of our digital sovereignty and security


