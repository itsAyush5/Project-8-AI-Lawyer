import json

# Load existing constitution data
with open('constitution_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add more critical parts
more_parts = [
    {
        "part": "X",
        "title": "The Scheduled and Tribal Areas",
        "articles": [
            {"number": "244", "title": "Administration of Scheduled Areas and Tribal Areas", "text": "The provisions of the Fifth Schedule shall apply to the administration and control of the Scheduled Areas and Scheduled Tribes in any State other than the States of Assam, Meghalaya, Tripura and Mizoram.", "keywords": ["scheduled areas", "tribal areas", "administration"]},
            {"number": "244A", "title": "Formation of an autonomous State comprising certain tribal areas in Assam", "text": "Notwithstanding anything in this Constitution, Parliament may, by law, form within the State of Assam an autonomous State comprising certain tribal areas.", "keywords": ["autonomous state", "assam", "tribal areas"]}
        ]
    },
    {
        "part": "XI",
        "title": "Relations Between the Union and the States",
        "articles": [
            {"number": "245", "title": "Extent of laws made by Parliament and by the Legislatures of States", "text": "Parliament may make laws for the whole or any part of the territory of India, and the Legislature of a State may make laws for the whole or any part of the State.", "keywords": ["parliament", "legislature", "laws", "jurisdiction"]},
            {"number": "246", "title": "Subject-matter of laws made by Parliament and by the Legislatures of States", "text": "Parliament has exclusive power to make laws with respect to any of the matters enumerated in List I in the Seventh Schedule (Union List). Parliament and the Legislature of any State have power to make laws with respect to any of the matters enumerated in List III in the Seventh Schedule (Concurrent List).", "keywords": ["union list", "state list", "concurrent list", "seventh schedule"]},
            {"number": "248", "title": "Residuary powers of legislation", "text": "Parliament has exclusive power to make any law with respect to any matter not enumerated in the Concurrent List or State List.", "keywords": ["residuary powers", "parliament"]},
            {"number": "249", "title": "Power of Parliament to legislate with respect to a matter in the State List in the national interest", "text": "Notwithstanding anything in the foregoing provisions of this Chapter, if the Council of States has declared by resolution that it is necessary or expedient in the national interest that Parliament should make laws with respect to any matter enumerated in the State List, it shall be lawful for Parliament to make laws for the whole or any part of the territory of India with respect to that matter.", "keywords": ["parliament", "state list", "national interest", "rajya sabha"]},
            {"number": "250", "title": "Power of Parliament to legislate with respect to any matter in the State List if a Proclamation of Emergency is in operation", "text": "Notwithstanding anything in this Chapter, Parliament shall, while a Proclamation of Emergency is in operation, have power to make laws for the whole or any part of the territory of India with respect to any of the matters enumerated in the State List.", "keywords": ["emergency", "parliament", "state list"]},
            {"number": "256", "title": "Obligation of States and the Union", "text": "The executive power of every State shall be so exercised as to ensure compliance with the laws made by Parliament and any existing laws which apply in that State, and the executive power of the Union shall extend to the giving of such directions to a State as may appear to the Government of India to be necessary for that purpose.", "keywords": ["union", "state", "compliance", "directions"]},
            {"number": "257", "title": "Control of the Union over States in certain cases", "text": "The executive power of every State shall be so exercised as not to impede or prejudice the exercise of the executive power of the Union.", "keywords": ["union", "state", "executive power"]},
            {"number": "262", "title": "Adjudication of disputes relating to waters of inter-State rivers or river valleys", "text": "Parliament may by law provide for the adjudication of any dispute or complaint with respect to the use, distribution or control of the waters of, or in, any inter-State river or river valley.", "keywords": ["inter-state", "water disputes", "rivers"]},
            {"number": "263", "title": "Provisions with respect to an inter-State Council", "text": "If at any time it appears to the President that the public interests would be served by the establishment of a Council charged with the duty of inquiring into and advising upon disputes which may have arisen between States, it shall be lawful for the President by order to establish such a Council.", "keywords": ["inter-state council", "disputes", "president"]}
        ]
    },
    {
        "part": "XII",
        "title": "Finance, Property, Contracts and Suits",
        "articles": [
            {"number": "264", "title": "Interpretation", "text": "In this Part, Finance Commission means a Finance Commission constituted under article 280.", "keywords": ["finance commission", "definition"]},
            {"number": "265", "title": "Taxes not to be imposed save by authority of law", "text": "No tax shall be levied or collected except by authority of law.", "keywords": ["taxation", "law", "authority"]},
            {"number": "266", "title": "Consolidated Funds and public accounts of India and of the States", "text": "All revenues received by the Government of India, all loans raised by that Government and all moneys received by that Government in repayment of loans shall form one consolidated fund to be entitled the Consolidated Fund of India.", "keywords": ["consolidated fund", "revenue", "loans"]},
            {"number": "267", "title": "Contingency Fund", "text": "Parliament may by law establish a Contingency Fund in the nature of an imprest to be entitled the Contingency Fund of India into which shall be paid from time to time such sums as may be determined by such law.", "keywords": ["contingency fund", "parliament"]},
            {"number": "268", "title": "Duties levied by the Union but collected and appropriated by the States", "text": "Such stamp duties and such duties of excise on medicinal and toilet preparations as are mentioned in the Union List shall be levied by the Government of India but shall be collected in such manner as Parliament may by law prescribe.", "keywords": ["duties", "union", "states", "collection"]},
            {"number": "270", "title": "Taxes levied and distributed between the Union and the States", "text": "All taxes and duties referred to in the Union List, except the duties and taxes referred to in articles 268, 269 and 269A, respectively, surcharge on taxes and duties referred to in article 271 and any cess levied for specific purposes under any law made by Parliament shall be levied and collected by the Government of India and shall be distributed between the Union and the States.", "keywords": ["tax distribution", "union", "states"]},
            {"number": "280", "title": "Finance Commission", "text": "The President shall, within two years from the commencement of this Constitution and thereafter at the expiration of every fifth year or at such earlier time as the President considers necessary, by order constitute a Finance Commission.", "keywords": ["finance commission", "president", "constitution"]},
            {"number": "300", "title": "Suits and proceedings", "text": "The Government of India may sue or be sued by the name of the Union of India and the Government of a State may sue or be sued by the name of the State.", "keywords": ["suits", "government", "legal proceedings"]},
            {"number": "300A", "title": "Persons not to be deprived of property save by authority of law", "text": "No person shall be deprived of his property save by authority of law.", "keywords": ["property", "deprivation", "law"]}
        ]
    },
    {
        "part": "XIV",
        "title": "Services Under the Union and the States",
        "articles": [
            {"number": "308", "title": "Interpretation", "text": "In this Part, unless the context otherwise requires, the expression State includes a Union territory having a Legislative Assembly.", "keywords": ["state", "definition", "union territory"]},
            {"number": "309", "title": "Recruitment and conditions of service of persons serving the Union or a State", "text": "Subject to the provisions of this Constitution, Acts of the appropriate Legislature may regulate the recruitment, and conditions of service of persons appointed, to public services and posts in connection with the affairs of the Union or of any State.", "keywords": ["recruitment", "public service", "conditions"]},
            {"number": "310", "title": "Tenure of office of persons serving the Union or a State", "text": "Every person who is a member of a defence service or of a civil service of the Union or of an all-India service or holds any post connected with defence or any civil post under the Union holds office during the pleasure of the President.", "keywords": ["tenure", "civil service", "president"]},
            {"number": "311", "title": "Dismissal, removal or reduction in rank of persons employed in civil capacities under the Union or a State", "text": "No person who is a member of a civil service of the Union or an all-India service or a civil service of a State or holds a civil post under the Union or a State shall be dismissed or removed by an authority subordinate to that by which he was appointed.", "keywords": ["dismissal", "civil service", "protection"]},
            {"number": "312", "title": "All-India services", "text": "Notwithstanding anything in Chapter VI of Part VI or Part XI, if the Council of States has declared by resolution that it is necessary or expedient in the national interest so to do, Parliament may by law provide for the creation of one or more all-India services common to the Union and the States.", "keywords": ["all-india services", "parliament", "union", "states"]},
            {"number": "315", "title": "Public Service Commissions for the Union and for the States", "text": "There shall be a Public Service Commission for the Union and a Public Service Commission for each State.", "keywords": ["public service commission", "union", "state"]},
            {"number": "320", "title": "Functions of Public Service Commissions", "text": "It shall be the duty of the Union and the State Public Service Commissions to conduct examinations for appointments to the services of the Union and the services of the State respectively.", "keywords": ["public service commission", "examinations", "appointments"]}
        ]
    },
    {
        "part": "XV",
        "title": "Elections",
        "articles": [
            {"number": "324", "title": "Superintendence, direction and control of elections to be vested in an Election Commission", "text": "The superintendence, direction and control of the preparation of the electoral rolls for, and the conduct of, all elections to Parliament and to the Legislature of every State and of elections to the offices of President and Vice-President held under this Constitution shall be vested in a Commission (referred to in this Constitution as the Election Commission).", "keywords": ["election commission", "elections", "superintendence"]},
            {"number": "325", "title": "No person to be ineligible for inclusion in electoral rolls on grounds of religion, race, caste or sex", "text": "There shall be one general electoral roll for every territorial constituency for election to either House of Parliament or to the House or either House of the Legislature of a State and no person shall be ineligible for inclusion in any such roll or claim to be included in any special electoral roll for any such constituency on grounds only of religion, race, caste, sex or any of them.", "keywords": ["electoral roll", "equality", "discrimination"]},
            {"number": "326", "title": "Elections to the House of the People and to the Legislative Assemblies of States to be on the basis of adult suffrage", "text": "The elections to the House of the People and to the Legislative Assembly of every State shall be on the basis of adult suffrage; that is to say, every person who is a citizen of India and who is not less than eighteen years of age on such date as may be fixed in that behalf by or under any law made by the appropriate Legislature and is not otherwise disqualified under this Constitution or any law made by the appropriate Legislature on the ground of non-residence, unsoundness of mind, crime or corrupt or illegal practice, shall be entitled to be registered as a voter at any such election.", "keywords": ["adult suffrage", "voting age", "eighteen years", "elections"]},
            {"number": "327", "title": "Power of Parliament to make provision with respect to elections to Legislatures", "text": "Subject to the provisions of this Constitution, Parliament may from time to time by law make provision with respect to all matters relating to, or in connection with, elections to either House of Parliament or to the House or either House of the Legislature of a State.", "keywords": ["parliament", "elections", "legislature"]},
            {"number": "329", "title": "Bar to interference by courts in electoral matters", "text": "Notwithstanding anything in this Constitution, no election to either House of Parliament or to the House or either House of the Legislature of a State shall be called in question except by an election petition presented to such authority and in such manner as may be provided for by or under any law made by the appropriate Legislature.", "keywords": ["elections", "court", "election petition"]}
        ]
    },
    {
        "part": "XVI",
        "title": "Special Provisions Relating to Certain Classes",
        "articles": [
            {"number": "330", "title": "Reservation of seats for Scheduled Castes and Scheduled Tribes in the House of the People", "text": "Seats shall be reserved in the House of the People for the Scheduled Castes and the Scheduled Tribes.", "keywords": ["reservation", "scheduled castes", "scheduled tribes", "lok sabha"]},
            {"number": "332", "title": "Reservation of seats for Scheduled Castes and Scheduled Tribes in the Legislative Assemblies of the States", "text": "Seats shall be reserved for the Scheduled Castes and the Scheduled Tribes in the Legislative Assembly of every State.", "keywords": ["reservation", "scheduled castes", "scheduled tribes", "assembly"]},
            {"number": "335", "title": "Claims of Scheduled Castes and Scheduled Tribes to services and posts", "text": "The claims of the members of the Scheduled Castes and the Scheduled Tribes shall be taken into consideration, consistently with the maintenance of efficiency of administration, in the making of appointments to services and posts in connection with the affairs of the Union or of a State.", "keywords": ["scheduled castes", "scheduled tribes", "services", "appointments"]},
            {"number": "338", "title": "National Commission for Scheduled Castes", "text": "There shall be a Commission for the Scheduled Castes to be known as the National Commission for the Scheduled Castes.", "keywords": ["national commission", "scheduled castes"]},
            {"number": "338A", "title": "National Commission for Scheduled Tribes", "text": "There shall be a Commission for the Scheduled Tribes to be known as the National Commission for the Scheduled Tribes.", "keywords": ["national commission", "scheduled tribes"]},
            {"number": "340", "title": "Appointment of a Commission to investigate the conditions of backward classes", "text": "The President may by order appoint a Commission consisting of such persons as he thinks fit to investigate the conditions of socially and educationally backward classes within the territory of India.", "keywords": ["backward classes", "commission", "investigation"]},
            {"number": "341", "title": "Scheduled Castes", "text": "The President may with respect to any State or Union territory, and where it is a State, after consultation with the Governor thereof, by public notification, specify the castes, races or tribes or parts of or groups within castes, races or tribes which shall for the purposes of this Constitution be deemed to be Scheduled Castes in relation to that State or Union territory.", "keywords": ["scheduled castes", "president", "notification"]},
            {"number": "342", "title": "Scheduled Tribes", "text": "The President may with respect to any State or Union territory, and where it is a State, after consultation with the Governor thereof, by public notification, specify the tribes or tribal communities or parts of or groups within tribes or tribal communities which shall for the purposes of this Constitution be deemed to be Scheduled Tribes in relation to that State or Union territory.", "keywords": ["scheduled tribes", "president", "notification"]}
        ]
    },
    {
        "part": "XVIII",
        "title": "Emergency Provisions",
        "articles": [
            {"number": "352", "title": "Proclamation of Emergency", "text": "If the President is satisfied that a grave emergency exists whereby the security of India or of any part of the territory thereof is threatened, whether by war or external aggression or armed rebellion, he may, by Proclamation, make a declaration to that effect.", "keywords": ["emergency", "proclamation", "president", "national security"]},
            {"number": "353", "title": "Effect of Proclamation of Emergency", "text": "While a Proclamation of Emergency is in operation, the executive power of the Union shall extend to the giving of directions to any State as to the manner in which the executive power thereof is to be exercised.", "keywords": ["emergency", "executive power", "union", "state"]},
            {"number": "356", "title": "Provisions in case of failure of constitutional machinery in States", "text": "If the President, on receipt of a report from the Governor of a State or otherwise, is satisfied that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of this Constitution, the President may by Proclamation assume to himself all or any of the functions of the Government of the State.", "keywords": ["president's rule", "state emergency", "constitutional machinery"]},
            {"number": "358", "title": "Suspension of provisions of article 19 during emergencies", "text": "While a Proclamation of Emergency declaring that the security of India or any part of the territory thereof is threatened by war or by external aggression is in operation, nothing in article 19 shall restrict the power of the State as defined in Part III to make any law or to take any executive action.", "keywords": ["emergency", "article 19", "suspension", "fundamental rights"]},
            {"number": "359", "title": "Suspension of the enforcement of the rights conferred by Part III during emergencies", "text": "Where a Proclamation of Emergency is in operation, the President may by order declare that the right to move any court for the enforcement of such of the rights conferred by Part III as may be mentioned in the order and all proceedings pending in any court for the enforcement of the rights so mentioned shall remain suspended for the period during which the Proclamation is in force.", "keywords": ["emergency", "fundamental rights", "suspension"]},
            {"number": "360", "title": "Provisions as to financial emergency", "text": "If the President is satisfied that a situation has arisen whereby the financial stability or credit of India or of any part of the territory thereof is threatened, he may by a Proclamation make a declaration to that effect.", "keywords": ["financial emergency", "president", "proclamation"]}
        ]
    },
    {
        "part": "XX",
        "title": "Amendment of the Constitution",
        "articles": [
            {"number": "368", "title": "Power of Parliament to amend the Constitution and procedure therefor", "text": "Parliament may in exercise of its constituent power amend by way of addition, variation or repeal any provision of this Constitution in accordance with the procedure laid down in this article. An amendment of this Constitution may be initiated only by the introduction of a Bill for the purpose in either House of Parliament, and when the Bill is passed in each House by a majority of the total membership of that House and by a majority of not less than two-thirds of the members of that House present and voting, it shall be presented to the President who shall give his assent to the Bill and thereupon the Constitution shall stand amended.", "keywords": ["amendment", "parliament", "constituent power", "procedure"]}
        ]
    }
]

# Extend the parts array
data['parts'].extend(more_parts)

# Update summary
data['summary']['articles_in_this_database'] = sum(len(part['articles']) for part in data['parts'])
data['summary']['parts_covered'] = [part['part'] for part in data['parts']]

# Save updated file
with open('constitution_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Constitution database further expanded!")
print(f"📚 Total articles now: {data['summary']['articles_in_this_database']}")
print(f"📑 Parts covered: {', '.join(data['summary']['parts_covered'])}")
print(f"\n🎯 Coverage includes:")
print(f"   - All Fundamental Rights (Part III)")
print(f"   - All Directive Principles (Part IV)")
print(f"   - Fundamental Duties (Part IVA)")
print(f"   - Union & State Government structures (Parts V, VI)")
print(f"   - Panchayats & Municipalities (Parts IX, IXA)")
print(f"   - Emergency Provisions (Part XVIII)")
print(f"   - Elections (Part XV)")
print(f"   - And many more critical articles!")
