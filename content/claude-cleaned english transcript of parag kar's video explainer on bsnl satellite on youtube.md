
# BSNL's Satellite Phone: What It Is, and Whether Smartphones Can Do the Same

Hello, everyone. BSNL has launched a new satellite phone — you can see it in the tweet BSNL put out. The phone looks like this, and its price tag is ₹1,34,166, which is roughly what you'd pay for an iPhone.
 
So what's the issue? Using this phone is expensive. It wasn't initially available to the public, though it may have been made available since. You get very little talk time for a lot of money. It isn't listed on the BSNL portal, but several people have reported paying ₹5,000–6,000 a month in service charges just to use the phone.

Why am I making this video? Because I want to ask: can the capability that this BSNL satellite phone offers eventually be built into a conventional smartphone — an iPhone or a Google Pixel? Will this dedicated satellite phone become redundant in the future? What are the challenges in building satellite capability into a regular smartphone, what would the advantages be, and what technological changes would be needed?

There's a useful historical parallel here. When GSM phones launched in India in the mid-1990s, a handset cost around ₹50,000 — the equivalent of roughly ₹5 lakh today — and call rates were about ₹16 a minute. Are satellite phones at a similar stage today? Just as 4G and 5G eventually brought per-minute costs down sharply, will the same happen with satellite phones? That's what this video sets out to examine — the spectrum involved, how these phones work, how a conventional smartphone might integrate this capability, and whether that would require dismantling the existing network or could run on top of it.

## What BSNL Has Actually Launched

BSNL has launched a dedicated satellite phone that connects to geostationary satellites positioned about 36,000 kilometres above the Earth. "Geostationary" means the satellite doesn't appear to move relative to the ground: it orbits the Earth, but at a speed that matches Earth's rotation, so it appears fixed in the sky. Other satellites orbit at different speeds and altitudes and don't stay fixed over one point.

This BSNL device is a dedicated handset with a physical antenna that has to be pulled out before you can make a call — unlike a conventional smartphone, where the antenna is built into the body of the phone. It also uses a separate SIM, meaning a separate phone number from your regular mobile number, and connects directly to the geostationary satellite for voice and SMS. This is a conventional satellite phone, not satellite connectivity added to an ordinary smartphone.

On how BSNL's network connects: terrestrial mobile networks rely on ground-based towers, but here the connection is to a satellite orbiting in sync with the Earth. This isn't a new concept — it's essentially an upgraded version of the satellite phones BSNL has offered before. It runs on the geostationary satellite network of Viasat/Inmarsat, roughly 36,000 kilometres above the Earth's surface. BSNL controls a ground gateway along with a Radio Access Network (RAN) — referred to as the GMR-2 satellite RAN — which functions much like a base station, processing the radio signal. This gateway connects directly into BSNL's telephone network, allowing calls to and from the satellite handset.

## Why Two Separate Phones Are Needed

As mentioned, this device is satellite-specific — it isn't a smartphone. A regular smartphone has an internal antenna, a regular SIM, a connection to terrestrial base stations, and a standard mobile number, all built in. The satellite phone requires a different modem, a different antenna, a different radio network, and a different service platform altogether — it has essentially nothing in common with a smartphone's terrestrial network setup. So there are really two separate integration problems: one device and one number. Combining smartphone connectivity with satellite connectivity means solving both.

The bigger of the two problems is the antenna. In a smartphone, you can't have a protruding external antenna — it would look and feel impractical — so the antenna has to be built into the body of the phone. But an internal antenna is omnidirectional and much weaker: if your hand covers it, signal strength drops further, and its link margin is poor. A dedicated satellite phone's external antenna, by contrast, significantly improves the link budget — the phone's ability to maintain a usable connection to the satellite.

This is the core challenge in building satellite capability into a smartphone: talking to a satellite 36,000 kilometres away requires far more technological refinement than talking to a terrestrial mobile tower, which might be only 1 to 5 kilometres away. Signal strength falls off with the square of distance (the familiar 1/r² relationship), so by the time a smartphone-strength signal reaches a satellite 36,000 kilometres away, it has attenuated enormously — effectively becoming unusable without a much stronger link. That's the fundamental link-budget problem in satellite communication, and it's a large part of why this integration hasn't happened seamlessly yet.

## Why Voice Is Harder Than Messaging

Satellite voice calls are considerably harder to support than satellite messaging. Apple's emergency satellite messaging feature on the iPhone works because text messages are stored on the device: the phone attempts to send them and retries on failure, without needing an instant, continuous connection. A short delay in an SMS is barely noticeable.

Voice calls are different — they require continuous, real-time, two-way communication with essentially no room to pause and retry without the conversation sounding broken. That's a large part of why Apple has only implemented emergency text messaging via satellite so far, not voice calls.

BSNL's satellite phone is built specifically to support voice. It uses a dedicated antenna and a satellite-specific GMR-2 modem, along with narrow radio channels — since voice doesn't need broadband bandwidth, just a small channel of roughly 4–8 kHz depending on the codec used. It relies on low-rate voice codecs rather than the higher-fidelity codecs used in regular phone calls, along with strong error coding and interleaving, all built around a dedicated satellite gateway network. In short: to make voice reliable, the phone sacrifices convenience and data speed, and accepts a protruding external antenna. Supporting real-time voice reliably is the single most important design requirement for a satellite phone.

## Building Satellite Capability Into a Smartphone: The NTN Standard

So what would it take to build this capability into an ordinary smartphone? This is where the 3GPP (3rd Generation Partnership Project) comes in — the body that writes the technical standards that chipset and device manufacturers such as Qualcomm, MediaTek, and Samsung build into their hardware.

3GPP has defined a standard for this: Non-Terrestrial Networks (NTN), introduced under Release 17. Under this standard, a smartphone would need an LTE/5G modem, an NTN-capable chipset, and dedicated satellite firmware.

Why is separate firmware needed? A terrestrial base station is only a few kilometres away, but a satellite is 36,000 kilometres away, which introduces significant signal delay that has to be accounted for. There's also the question of movement: a terrestrial base station is static, while satellites may or may not be. Geostationary satellites appear fixed, but other satellites are geosynchronous or move faster, introducing Doppler shift that has to be corrected for. Handling all of this requires firmware distinct from what runs on a conventional terrestrial-only phone — firmware that works with the terrestrial network by default, and switches to satellite connectivity when terrestrial coverage isn't available.

In essence, the NTN standard aims to create a common radio "language" between mainstream smartphones and satellite networks. It standardises the network side, but it doesn't eliminate the antenna and link-budget limitations — which is why smartphones still need considerable technical modification to support this. There are, in effect, two distinct approaches to satellite connectivity: the dedicated satellite phone discussed earlier, optimised purely for reliability, and the emerging 3GPP NTN-capable smartphone, optimised for integration and scale.

## Would BSNL Need to Rebuild Its Network for Smartphones?

A natural question: if BSNL eventually offers satellite connectivity through ordinary smartphones using the same satellite network, would it need to dismantle its existing satellite phone infrastructure? The answer is no — both services can run off the same satellite. It's a matter of allocating some channels to existing satellite-phone services and opening up other channels for new NTN-based services, provided there's sufficient bandwidth. Existing satellite phone services wouldn't need to be dismantled, and new services could be launched on the same network.

The satellite itself mostly acts as a relay: it receives a signal and relays it down to a ground station, where a ground-based radio network processes it — functioning much like a terrestrial base station and mobile switching centre — before the signal is routed through the gateway into the conventional telephone network. In that sense, the innovation isn't simply about relocating processing to the ground (existing satellite systems already do that); it's about maintaining the 3GPP standard within the RAN itself, so satellite and terrestrial networks can interoperate.

## GEO vs NGSO Satellites

There are broadly two categories of satellite systems relevant here: GEO (geostationary, above 36,000 kilometres) and NGSO (non-geostationary, at lower altitudes). Smartphones can, in principle, work with both. The NTN standard isn't limited to GEO satellites — it's designed to work with NGSO systems too.

NGSO systems introduce additional complexity because satellites at lower altitudes orbit much faster, which increases Doppler shift and requires further refinement of the standard. GEO satellites, being farther away and effectively stationary relative to the ground, introduce comparatively less of this issue but come with higher latency, while NGSO systems have lower latency but move faster. Both are designed to work within the same 3GPP standard, which means an operator like BSNL isn't locked into choosing one architecture over the other — it can support both.

## Why Testing Is the Real Bottleneck

Beyond the standards and handset design, the most significant practical challenge is testing. Testing is relatively straightforward on a conventional terrestrial network because there are fewer variables to account for. Satellite networks introduce many more radio-level challenges, which is why a commercial demonstration by BSNL doesn't mean commercial services are ready to roll out immediately.

Device-level testing alone covers chipset and protocol performance, antenna radiation pattern efficiency, hand/body signal-blockage testing, receiver sensitivity, link margin, EIRP limits, battery drain, heat management, and real-world usage testing. After that comes satellite network testing: one-way delay, Doppler correction, random access, beam handovers, hand-off performance, and message retransmission/error recovery. On top of this sits e-SIM integration across both terrestrial and satellite networks, billing, roaming, emergency services, lawful interception, location services, and regulatory approvals.

In short, a handset has to be extensively tested and certified to work with a given satellite RAN before commercial rollout — much as terrestrial handsets need to be tested for compatibility with a specific vendor's RAN (Ericsson, Samsung, Nokia, and so on). A satellite NTN-capable, 3GPP Release 17 handset would similarly need to be tested against BSNL's specific satellite RAN before it can be deployed at scale.

This has implications for scale across operators. If every operator in India — BSNL, Reliance Jio, Bharti Airtel, Vodafone Idea — ends up using a different, proprietary RAN, each network and handset combination would need to be tested separately, and international roaming would become significantly more complicated, since handsets wouldn't work seamlessly across networks. A common, integrated RAN that multiple operators can use — while still issuing their own numbers — would make scaling satellite services considerably easier.

## Closing Thoughts

That's the essence of what I wanted to cover: what BSNL's satellite phone actually is, the challenges involved in eventually building this capability into conventional smartphones, and where the opportunities lie going forward. It isn't possible to cover every detail in a single video, but I've tried to lay out the key technical considerations. If you have questions, do leave them in the comments — I'll try to answer them. Thanks for watching, and I'll be back soon with another video.

---

_Editorial note: A few proper nouns and technical abbreviations in the source audio were unclear or appear to have been mistranscribed (e.g., a reference to "Jio" used in the context of satellite orbit types has been corrected to "GEO," and references to the satellite operator have been standardised as "Viasat/Inmarsat"). These should be verified against BSNL's official announcements before publication._