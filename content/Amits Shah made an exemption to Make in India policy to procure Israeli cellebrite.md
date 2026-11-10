**

# NIA got Home Minister’s approval for Cellebrite under Make in India exemption

Union Home Minister Amit Shah approved the National Investigation Agency's (NIA) purchase of Cellebrite's most powerful phone-cracking tool, according to a Ministry of Home Affairs [letter](https://drive.google.com/file/d/1QnfmEdfrJqJsFb6BDgQONflukAC8gToA/view) made public by the [Internet Freedom Foundation (IFF).](https://internetfreedom.in/the-home-minister-signed-off-on-it-who-is-cracking-indias-phones-and-whose-phones-have-they-cracked/) The letter, dated 20 January 2026, records that Shah approved a one-time exemption from the government's Make in India procurement rules. The exemption covers one Cellebrite Premium Tool with a three-year licence, priced at Rs. 4,98,15,000. 

“The NIA’s purchase carries the most senior approval on record, but it is part of a wider pattern,” wrote IFF in its blogpost. It also listed 15 procurement listings naming Cellebrite products across 11 tenders published in 2026. Access the full list on [IFF’s website](https://internetfreedom.in/the-home-minister-signed-off-on-it-who-is-cracking-indias-phones-and-whose-phones-have-they-cracked/#:~:text=earnest%20money%20deposit.-,Buyer,-What%20is%20being). 

“India has no statute, rule or published protocol governing the forensic extraction of a person’s phone.” - IFF

However, the Delhi Police has had Cellebrite tools since at least 2020, as MediaNama [reported](https://www.medianama.com/2020/12/223-exclusive-delhi-police-has-tools-extract-data-from-smartphones-iphones/) then. We also reported that Delhi police had tther tools available to the Delhi Police including Swedish firm MicroSystemation AB’s (MSAB) XRY tool, Russian firm Oxygen Forensics’ Detective, and Czech firm Compelson Labs’ MOBILEdit. “All the forensic tools through which data can be extracted, they are available,” Anyesh Roy, the then deputy commissioner of police who heads Delhi Police’s Cyber Crime Cell unit, told MediaNama.

What the documents reveal:

The letter which states that Home Minister Amit Shah’s approval for “one time exemption from "[Public Procurement (Preference to Make-in-India) order 2017](https://www.dpiit.gov.in/ministry/about-us/details/Title=Public-Procurement-\(Preference-to-Make-in-India\)-Order,-2017-ITMwETMtQWa) and its subsequent revision order dated 19.07.2024" is signed by Vinod Kumar Dubey, Assistant Commissioner (Procurement), in the ministry's Police Modernisation Division. It is addressed to the NIA's Director General and refers to an NIA note of 20 August 2025. It records that the ministry's Integrated Finance Division concurred on 13 January 2026, and that the Home Minister approved the proposal on a note dated 17 January 2026.

Later, the NIA published [a bid on the Government e-Marketplace (GeM)](https://drive.google.com/file/d/1LRkjkKFbECbvabIFd-K0o_RCfgNr_om5/view). The bid's field for the authority that waived the Make in India preference names "Shri Amit Shah, Hon'ble Home Minister of India". GeM now shows the contract awarded to Nextechno Gen Private Limited for Rs. 4,97,99,515, which is Rs. 15,485 below the estimate, IFF said.

IFF clarified that it has not seen the Minister's note itself, and has sought it under the Right to Information (RTI) Act. Its account of the Minister's role rests on the ministry's letter and the NIA's bid.

The  Serious Fraud Investigation Office (SFIO) contract, [dated 25 March 2026](https://drive.google.com/file/d/1VsW8ySSqy7_k_fGa0iZtVdoq-Vh6YjrK/view), records Israel as the country of origin for the Cellebrite. 

What is the reason for exemption? 

The NIA's recorded reason for waiving the order is that "no other Company is manufacturing the software with the same name and specifications". A [Proprietary Article Certificate](https://drive.google.com/file/d/1C8cXfC_4TIkxjMKy8CROVaN2DhhNDWXK/view) under Rule 166 of the General Financial Rules names Cellebrite DI Ltd. of Petah Tikva, Israel, as sole proprietor. It adds that "No other make or model is acceptable."

“This is true of every branded product, and it does not answer the question the order actually asks, which is whether an Indian product could perform the same function… Nothing in the record we have seen shows that anyone tested whether one could.” - IFF

### What the tool is built to do

According to the  [two-page technical specification](https://drive.google.com/file/d/1DGVk5KN_c7bETFtthJNZBMl-o_c-Wcw7/view) attached by NIA to its bid, the Cellebrite premium tool must extract a full filesystem copy from major Android vendors, including Samsung, Huawei, Xiaomi, Motorola, LG, Nokia, ZTE, OnePlus, Alcatel, Pixel, Realme, Vivo, and Oppo, once the device has been unlocked at least once since boot. This is technically known as After-First-Unlock (AFU).

According to MobiLedit, a Czech-based digital forensics software used in forensic investigations, full file system refers to extraction of a wide range of data, including retrieval of deleted files. It [explains](https://forensic.manuals.mobiledit.com/MM/full-file-system-vs-file-system): 

“A full filesystem goes a step beyond basic file system extraction. It involves accessing the complete file system, including areas that are not usually accessible during normal device operation. This type of extraction can retrieve deleted files, hidden files, and system logs, offering a much more comprehensive view of the data on the device. It's a deeper form of data extraction that can be crucial for forensic investigations, as it can uncover evidence that wouldn't be visible through a standard file system extraction. – [MobiLedit](https://forensic.manuals.mobiledit.com/MM/full-file-system-vs-file-system)

For context, MediaNama [reported in April 2025](https://www.medianama.com/2025/04/223-google-play-update-automatic-reboot-android-phones/) that Android phones will reboot after three days locked, returning them to "before first unlock", where data is harder to reach. Therefore, the specifications document also states that the software should be updated to make it compatible with the latest OS versions and chips of phones. 

Essentially, the tool should also be able to brute-force unlock devices, a method used to automatically guess passcodes with multiple iterations.

The specification document also states that It should also support both full-disk encryption (FDE) and or file-based encryption (FBE), which means that it is capable of full filesystem extraction as well as the  bit-by-bit copy of the device storage respectively.

Some of excerpts from the specification document are:

- “The solution should allow data to be extracted in a forensically sound process.”
    
- “The solution should identify, extract and decrypt Samsung Secure folder, Huawei Private Space and Xiaomi second space.”
    
- “The solution should be able to conduct brute-force (cold) on iPhone chip A8 all the way to A13 (iPhone 11 and iphone SE Gen 2) to determine the device passcode.”
    
- “The solution should be able to perform Before-First-Unlock(BFU) extraction for iPhone 6 and above. The solution should be able to conduct full file system from olderiPhone version running on chip from A7, A8 and A9.”
    
- “The solution should be able to conduct After-First Unlock (AFU) based Full Filesystem extraction from iPhone 11, 12, 13,14 with chip running on A13, A14, A15 to A16 or latest.”
    
- “The solution should be able to conduct Full File-system support for unlocked iPhone 15 or latest.”
    
- “The solution should also allow Full File-system extraction of iOs devices with greater data extraction.”
    
- “The solution should be able to support autonomous Brute-Force for iOS devices.”
    
- “The solution should enable the user to enter potential passcodes while performing brute-force on iOs devices without affecting the ongoing process.”
    
- “The solution should allow user to perform selective extraction at the level of the individual installed applications for both iOS and Android devices.”
    
- “The solution should be regularly updated to support additional operating system versions and devices during the valid license and support period.
    

In its blog post, IFF listed a few cases of documented misuse of the Cellebrite in foreign countries. Read more about it [here](https://internetfreedom.in/the-home-minister-signed-off-on-it-who-is-cracking-indias-phones-and-whose-phones-have-they-cracked/#:~:text=been%20used%20in-,other%20countries,-The%20case%20for). 

IFF checked every Cellebrite entry in its tracker of surveillance-related tenders against GeM and state procurement portals as of 6 November 2026. It found 15 listings across 11 tenders, three of them awarded. Many state bids disclose only the earnest money deposit, not the contract value.Source: IFF.

  

Delhi Police

In July 2025, [The Wire reported](https://m.thewire.in/article/tech/delhi-police-ai-companies) that the Home Ministry had approved a Make in India exemption for foreign forensic tools sought by the force. IFF later obtained [the order](https://drive.google.com/file/d/1cfCqzmygsr81xEHtOA14hkyqJ044jkAp/view), dated 20 March 2025 and signed by an Under Secretary. It clears 19 products, three of them Cellebrite: UFED 4PC, Digital Collector, and Inspector with MacBook Pro.

The order refers to "the Competent Authority" without naming it. The NIA's single licence, by contrast, is recorded as approved by the Minister himself.

Five days later, the Crime Branch floated [a cyber lab tender](https://drive.google.com/file/d/1sUq1MIO8fYug0jpkh5tg_I752pkU4YLx/view). Its [108-page request for proposal](https://drive.google.com/file/d/14Gn0tNzWQV7UNYOHqQe-jONdHW-sM8S0/view) specifies tools that can reach from a seized phone into the cloud accounts it is logged into. GeM shows the tender awarded to 3rd Eye Techno Solutions Private Limited for Rs. 4,98,04,850, though the award record does not list brands.

Why it matters now: 

On [Kunal Kamra's YouTube reaction video](https://youtu.be/3snIdzecvjQ), Rathee claimed that he believes police tried to clone his iPhone using Cellebrite. He said the attempt appears to have failed because his phone ran a newer iOS version than the tool could process. He cited battery history showing hours on charge in custody. 

[Here](https://youtu.be/3snIdzecvjQ?t=141) is the timestamped URL of the YouTube video: 

[https://youtu.be/3snIdzecvjQ?t=141](https://youtu.be/3snIdzecvjQ?t=141) 

During the recent Jantar Mantar protests seeking the resignation of Chief Election Commissioner Gyanesh Kumar, several student protestors and journalists mobile phones were allegedly confiscated by the Delhi Police and in some cases, they have denied the holding their phones despite the phone’s GPS location contradicting their claims, as reported by NewsLaundry. 

 “No officer at the detention centre accepted responsibility for the devices. They told us to approach the police personnel in Connaught Place who had taken our phones in the first place. They did not tell us which officers had taken the phones or which police station in Connaught Place we should approach.” – S Singh, a 30-year-old singer, as quoted in [NewsLaundry](https://www.newslaundry.com/2026/10/20/the-curious-case-of-protesters-missing-phones-neither-fir-for-snatching-nor-memo-for-seizure). 

No law governs phone extraction, argues IFF

IFF says India has no statute, rule or published protocol for forensic extraction of a person's phone. In [Puttaswamy (2017)](https://www.scobserver.in/court-case/fundamental-right-to-privacy), the Supreme Court held that any intrusion on privacy must rest on a law, pursue a legitimate aim and be proportionate. IFF argues that copying a whole phone fails the first test, since no law authorises it or sets its limits.

The following nearest provisions do not fill this gap, IFF says:

- Section 106 of the Bharatiya Nagarik Suraksha Sanhita (BNSS) allows police to seize property, and Section 105 requires searches and seizures to be video recorded. Neither addresses unlocking or extracting data.
    
- Section 63 of the Bharatiya Sakshya Adhiniyam governs how electronic records are certified in court. IFF says it presumes an extraction was lawful rather than making it so.
    
- Section 69 of the Information Technology (IT) Act requires a written order from the Union or State Home Secretary before decryption. IFF says it knows of no such order for the October phones.
    
- Section 17(1)(c) of the Digital Personal Data Protection Act exempts processing for investigating offences.
    

Section 69 is itself under challenge, as per the IFF's [petition filed in January 2019](https://internetfreedom.in/supreme-court-issues-notice-on-iffs-petition-for-survelliance-reform-saveourprivacy/)  that challenges the sectio 69 and the 2009 Interception Rules and a 20 December 2018 notification authorising ten agencies to intercept and decrypt data. The NIA and the Delhi Police Commissioner are among them. The Supreme Court issued notice on 14 January 2019, and the petition is still pending.

In a separate case, [Foundation for Media Professionals v. Union of India](https://www.scobserver.in/cases/guidelines-for-search-and-seizure-of-digital-devices/), petitioners sought binding guidelines on seizing digital devices. The Centre [told the Court in December 2023](https://www.outlookindia.com/national/committee-being-constituted-to-frame-guidelines-on-seizure-of-electronic-devices-centre-to-sc-news-334903) that a committee was being formed to frame them. IFF says the guidelines have not been placed before the Court.

What IFF is asking for:

IFF said it is filing RTI applications with the Delhi Police and the Home Ministry. From Delhi Police, it seeks seizure memos and recordings for every phone taken between 10 and 12 October, and extraction logs for the forensic workstations that handled them. It also seeks licences and user logs for every Cellebrite product the force holds, and any Section 69 order relied on to decrypt a device.

From the Home Ministry, IFF seeks the full NIA file, including the Minister's 17 January note, the award letter and licence agreement, and any protocol on storing, sharing and deleting extracted data. It addressed the ministry because the NIA is in the Second Schedule of the RTI Act, and answers only on corruption and human rights allegations.

IFF has asked the Delhi Police and the Home Ministry to:

1. disclose whether any phone taken in October, including Rathee's, his parents' and the Newslaundry reporters', was connected to an extraction tool;
    
2. return every device still held, and certify deletion of data copied from anyone not charged;
    
3. suspend use of these tools on phones of preventive detainees, journalists and lawyers until binding rules exist; and
    
4. place the promised guidelines before the Supreme Court in the Foundation for Media Professionals case.
    

Also read:

- [Exclusive: Delhi Police has tools to extract data from smartphones, including iPhones](https://www.medianama.com/2020/12/223-exclusive-delhi-police-has-tools-extract-data-from-smartphones-iphones/)
    
- [Into the unknown: search and seizure of digital devices in India](https://www.medianama.com/2024/01/223-search-seizure-digital-devices-india/)
    
- [Telangana Police Tender for Cyber Tools Sparks Privacy Fears](https://www.medianama.com/2025/10/223-telangana-police-cyber-tools-tender-privacy-concerns/)
    

  
**