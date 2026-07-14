
# Telegram's t.me domain stops working; Pavel Durov asks domain registry to look into it

Telegram's short-link domain, t.me, stopped working worldwide on July 13, 2026. Links like t.me/[username], t.me/[channelname], and group invite links stopped opening in web browsers. 



 **"Hey @domainME, t.me links stopped working. Can you look into it?"** Telegram founder Pavel Durov noticed the issue and posted on X, tagging the .me domain registry. At the time of writing this report, there is no official explanation from Telegram, the .me registry.

**What is a .ME domain?** The [.ME domain](https://domain.me/about-me/) is the internet address for Montenegro, a small Mediterranean country with about 600,000 people. This country code top-level domain ([ccTLD](https://www.icann.org/resources/pages/cctlds-21-2012-02-25-en)) doesn't have any restrictions on who can use the domain. 

**How we checked the status of t.me domain**? To verify the domain's status ourselves, using Claude we ran two standard checks that anyone can use to look up a domain's official records.

1. **nslookup** This is a simple command that checks whether a domain actually loads or not. We ran nslookup on t.me and got back "Non-existent domain," meaning the domain could not be found at all. View the full response of the command [here](https://www.medianama.com/wp-content/uploads/2026/07/when-t.me-domian-was-blocked-nslookup-results.txt). 
2. **WHOIS commnad**: This is also a basic lookup that shows a domain's registration details and its current status. We ran a WHOIS check on t.me and found a status flag called "serverHold."  View the full response of the command [here](https://www.medianama.com/wp-content/uploads/2026/07/when-t.me-domain-was-blocked-whois-results.txt). 
3. **RDAP**:  Registration Data Access Protocol (RDAP) is a more detailed version of the same kind of Whois lookup. We [ran](https://rdap.identitydigital.services/rdap/domain/t.me) an RDAP check on t.me and it also showed "server hold," along with a timestamp showing the status was last changed on July 13, 2026, at 7:24:55 PM (UTC). View the full response of the command [here](https://gist.github.com/azdhan/82bb786975198323a3e0ada9acb23018). 

**What we found**: Both Whois and RDAP lookup checks resulted that t.me currently carries a "server hold" status. This is a flag applied by the domain registry and not by Telegram or GoDaddy, Telegram's domain registrar. When this status is applied, the domain stops working everywhere until the flag is removed. Since the block is at registry-level, it can't be accessible even through a VPN.

The RDAP's log record also showed that the domain details were last updated on July 13, 2026, which slightly matches with when Pavel Durov flagged this on X. He posted on Jul 14, 2026 at 6:39 AM IST, over 5 hours later the domain update was logged.

A [couple](https://x.com/chiefofautism/status/2076860835524215143?s=20) of [users](https://x.com/ResistanceDog/status/2076853480929591407?s=20) on X pointed out to US Department of Treasury's Office of Foreign Assets Control's press release on Specially Designated Nationals (SDN). In that press release, First VPN Service is blacklisted. According to FBI's May 2026 [notice](https://www.ic3.gov/CSA/2026/260521.pdf) on First VPN Service, it was reportedly used by at least 25 ransomware groups. Among the URLs and email addresses [specified](https://ofac.treasury.gov/recent-actions/20260713) under First VPN Service, t.me/FirstVPNService is also present. However, there is no official confirmation to know if this OFAC list is really behind the blocking of t.me domain.

**Throwback:** In August 2025, MediaNama reported that t.me domain was blocked on BSNL networks along with a few legitimate websites. Read MediaNama's full report [here](https://www.medianama.com/2025/08/223-bsnl-selective-website-blocking-violates-net-neutrality/). 

Also Read: 
- [BSNL’s Selective Website Blocking Violates Net Neutrality, Hides Reasons Behind RTI Loophole](https://www.medianama.com/2025/08/223-bsnl-selective-website-blocking-violates-net-neutrality/)
- [Who Ordered the Block on Medium? Why Is It Blocked by Some ISPs?](https://www.medianama.com/2025/10/223-medium-blocked-india-isp-level/)
- [Delhi HC Warns Domain Name Registrars to Comply with Domain Blocking Orders if they Want to Operate in India](https://www.medianama.com/2023/11/223-delhi-hc-domain-name-registrars-blocking-orders/)
