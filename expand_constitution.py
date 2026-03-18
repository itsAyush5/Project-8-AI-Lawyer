import json

# Load existing constitution data
with open('constitution_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add more parts with key articles
additional_parts = [
    {
        "part": "VI",
        "title": "The States",
        "articles": [
            {"number": "152", "title": "Definition", "text": "In this Part, unless the context otherwise requires, the State means a State specified in the First Schedule.", "keywords": ["state", "definition"]},
            {"number": "153", "title": "Governors of States", "text": "There shall be a Governor for each State.", "keywords": ["governor", "state"]},
            {"number": "154", "title": "Executive power of State", "text": "The executive power of the State shall be vested in the Governor and shall be exercised by him either directly or through officers subordinate to him.", "keywords": ["executive", "governor", "state power"]},
            {"number": "155", "title": "Appointment of Governor", "text": "The Governor of a State shall be appointed by the President by warrant under his hand and seal.", "keywords": ["governor", "appointment", "president"]},
            {"number": "156", "title": "Term of office of Governor", "text": "The Governor shall hold office during the pleasure of the President for a term of five years from the date on which he enters upon his office.", "keywords": ["governor", "term", "five years"]},
            {"number": "157", "title": "Qualifications for appointment as Governor", "text": "No person shall be eligible for appointment as Governor unless he is a citizen of India and has completed the age of thirty-five years.", "keywords": ["governor", "qualifications", "citizenship"]},
            {"number": "158", "title": "Conditions of Governor's office", "text": "The Governor shall not be a member of either House of Parliament or of a House of the Legislature of any State.", "keywords": ["governor", "conditions"]},
            {"number": "159", "title": "Oath or affirmation by the Governor", "text": "Every Governor shall, before entering upon his office, make and subscribe an oath or affirmation.", "keywords": ["governor", "oath"]},
            {"number": "161", "title": "Power of Governor to grant pardons", "text": "The Governor of a State shall have the power to grant pardons, reprieves, respites or remissions of punishment or to suspend, remit or commute the sentence of any person convicted of any offence against any law relating to a matter to which the executive power of the State extends.", "keywords": ["governor", "pardon", "clemency"]},
            {"number": "163", "title": "Council of Ministers to aid and advise Governor", "text": "There shall be a Council of Ministers with the Chief Minister at the head to aid and advise the Governor in the exercise of his functions.", "keywords": ["council of ministers", "chief minister", "governor"]},
            {"number": "164", "title": "Other provisions as to Ministers", "text": "The Chief Minister shall be appointed by the Governor and the other Ministers shall be appointed by the Governor on the advice of the Chief Minister.", "keywords": ["chief minister", "ministers", "appointment"]},
            {"number": "165", "title": "Advocate-General for the State", "text": "The Governor of each State shall appoint a person who is qualified to be appointed a Judge of a High Court to be Advocate-General for the State.", "keywords": ["advocate general", "state", "legal officer"]},
            {"number": "168", "title": "Constitution of Legislatures in States", "text": "For every State there shall be a Legislature which shall consist of the Governor, and in the States of Bihar, Maharashtra, Karnataka, and Uttar Pradesh, two Houses, and in other States, one House.", "keywords": ["legislature", "state", "bicameral", "unicameral"]},
            {"number": "170", "title": "Composition of the Legislative Assemblies", "text": "The Legislative Assembly of each State shall be composed of members chosen by direct election from territorial constituencies in the State.", "keywords": ["legislative assembly", "elections", "constituencies"]},
            {"number": "171", "title": "Composition of the Legislative Councils", "text": "The total number of members in the Legislative Council of a State shall not exceed one-third of the total number of members in the Legislative Assembly of that State.", "keywords": ["legislative council", "composition"]},
            {"number": "172", "title": "Duration of State Legislatures", "text": "Every Legislative Assembly of every State shall continue for five years from the date appointed for its first meeting.", "keywords": ["legislature", "duration", "five years"]},
            {"number": "173", "title": "Qualification for membership of the State Legislature", "text": "A person shall not be qualified to be chosen to fill a seat in the Legislature of a State unless he is a citizen of India and makes an oath or affirmation according to the form set out for the purpose in the Third Schedule.", "keywords": ["qualification", "legislature", "membership"]},
            {"number": "174", "title": "Sessions of the State Legislature", "text": "The Governor shall from time to time summon the House or each House of the Legislature of the State to meet at such time and place as he thinks fit.", "keywords": ["sessions", "legislature", "governor"]},
            {"number": "176", "title": "Special address by the Governor", "text": "The Governor may address the Legislative Assembly or, in the case of a State having a Legislative Council, either House of the Legislature of the State.", "keywords": ["governor", "address", "legislature"]},
            {"number": "178", "title": "The Speaker and Deputy Speaker of the Legislative Assembly", "text": "Every Legislative Assembly of a State shall choose two members of the Assembly to be respectively Speaker and Deputy Speaker thereof.", "keywords": ["speaker", "deputy speaker", "assembly"]},
            {"number": "194", "title": "Powers, privileges, etc., of the Houses of Legislatures and of the members and committees thereof", "text": "The powers, privileges and immunities of a House of the Legislature of a State, and of the members and the committees of a House of such Legislature, shall be such as may from time to time be defined by the Legislature by law.", "keywords": ["privileges", "legislature", "immunity"]},
            {"number": "200", "title": "Assent to Bills", "text": "When a Bill has been passed by the Legislative Assembly of a State or, in the case of a State having a Legislative Council, has been passed by both Houses of the Legislature of the State, it shall be presented to the Governor.", "keywords": ["bill", "assent", "governor"]},
            {"number": "213", "title": "Power of Governor to promulgate Ordinances during recess of Legislature", "text": "If at any time, except when the Legislative Assembly of a State is in session, the Governor is satisfied that circumstances exist which render it necessary for him to take immediate action, he may promulgate such Ordinances as the circumstances appear to him to require.", "keywords": ["ordinance", "governor", "emergency legislation"]},
            {"number": "214", "title": "High Courts for States", "text": "There shall be a High Court for each State.", "keywords": ["high court", "state", "judiciary"]},
            {"number": "215", "title": "High Courts to be courts of record", "text": "Every High Court shall be a court of record and shall have all the powers of such a court including the power to punish for contempt of itself.", "keywords": ["high court", "court of record", "contempt"]},
            {"number": "216", "title": "Constitution of High Courts", "text": "Every High Court shall consist of a Chief Justice and such other Judges as the President may from time to time deem it necessary to appoint.", "keywords": ["high court", "judges", "chief justice"]},
            {"number": "217", "title": "Appointment and conditions of the office of a Judge of a High Court", "text": "Every Judge of a High Court shall be appointed by the President by warrant under his hand and seal.", "keywords": ["judge", "high court", "appointment"]},
            {"number": "226", "title": "Power of High Courts to issue certain writs", "text": "Every High Court shall have power to issue to any person or authority, including in appropriate cases, any Government, within those territories directions, orders or writs, including writs in the nature of habeas corpus, mandamus, prohibition, quo warranto and certiorari.", "keywords": ["writs", "high court", "habeas corpus", "mandamus"]},
            {"number": "227", "title": "Power of superintendence over all courts by the High Court", "text": "Every High Court shall have superintendence over all courts and tribunals throughout the territories in relation to which it exercises jurisdiction.", "keywords": ["superintendence", "high court", "courts"]},
            {"number": "233", "title": "Appointment of district judges", "text": "Appointments of persons to be, and the posting and promotion of, district judges in any State shall be made by the Governor of the State in consultation with the High Court exercising jurisdiction in relation to such State.", "keywords": ["district judge", "appointment", "governor"]}
        ]
    },
    {
        "part": "VIII",
        "title": "The Union Territories",
        "articles": [
            {"number": "239", "title": "Administration of Union territories", "text": "Save as otherwise provided by Parliament by law, every Union territory shall be administered by the President acting, to such extent as he thinks fit, through an administrator to be appointed by him with such designation as he may specify.", "keywords": ["union territory", "administration", "president"]},
            {"number": "239A", "title": "Creation of local Legislatures or Council of Ministers or both for certain Union territories", "text": "Parliament may by law create for the Union territory of Puducherry a body, whether elected or partly nominated and partly elected, to function as a Legislature for the Union territory.", "keywords": ["union territory", "legislature", "puducherry"]},
            {"number": "240", "title": "Power of President to make regulations for certain Union territories", "text": "The President may make regulations for the peace, progress and good government of the Union territory.", "keywords": ["president", "regulations", "union territory"]},
            {"number": "241", "title": "High Courts for Union territories", "text": "Parliament may by law constitute a High Court for a Union territory or declare any court in any such territory to be a High Court for all or any of the purposes of this Constitution.", "keywords": ["high court", "union territory"]},
            {"number": "242", "title": "Coorg", "text": "Repealed by the Constitution (Seventh Amendment) Act, 1956.", "keywords": ["coorg", "repealed"]}
        ]
    },
    {
        "part": "IX",
        "title": "The Panchayats",
        "articles": [
            {"number": "243", "title": "Definitions", "text": "In this Part, unless the context otherwise requires, Panchayat means an institution of self-government constituted under article 243B, for the rural areas.", "keywords": ["panchayat", "definition", "rural", "self-government"]},
            {"number": "243A", "title": "Gram Sabha", "text": "A Gram Sabha may exercise such powers and perform such functions at the village level as the Legislature of a State may, by law, provide.", "keywords": ["gram sabha", "village", "powers"]},
            {"number": "243B", "title": "Constitution of Panchayats", "text": "There shall be constituted in every State, Panchayats at the village, intermediate and district levels.", "keywords": ["panchayat", "constitution", "levels"]},
            {"number": "243C", "title": "Composition of Panchayats", "text": "All the seats in a Panchayat shall be filled by persons chosen by direct election from territorial constituencies in the Panchayat area.", "keywords": ["panchayat", "composition", "elections"]},
            {"number": "243D", "title": "Reservation of seats", "text": "Seats shall be reserved for the Scheduled Castes and the Scheduled Tribes in every Panchayat.", "keywords": ["reservation", "scheduled castes", "scheduled tribes", "panchayat"]},
            {"number": "243E", "title": "Duration of Panchayats", "text": "Every Panchayat shall continue for five years from the date appointed for its first meeting.", "keywords": ["panchayat", "duration", "five years"]},
            {"number": "243F", "title": "Disqualifications for membership", "text": "A person shall be disqualified for being chosen as, and for being, a member of a Panchayat if he is so disqualified by or under any law for the time being in force for the purposes of elections to the Legislature of the State.", "keywords": ["disqualification", "panchayat", "membership"]},
            {"number": "243G", "title": "Powers, authority and responsibilities of Panchayats", "text": "The Legislature of a State may, by law, endow the Panchayats with such powers and authority as may be necessary to enable them to function as institutions of self-government.", "keywords": ["powers", "panchayat", "self-government"]},
            {"number": "243H", "title": "Powers to impose taxes by, and Funds of, the Panchayats", "text": "The Legislature of a State may, by law, authorize a Panchayat to levy, collect and appropriate such taxes, duties, tolls and fees.", "keywords": ["taxes", "panchayat", "funds"]},
            {"number": "243I", "title": "Constitution of Finance Commission to review financial position of Panchayats", "text": "The Governor of a State shall, as soon as may be within one year from the commencement of the Constitution (Seventy-third Amendment) Act, 1992, and thereafter at the expiration of every fifth year, constitute a Finance Commission.", "keywords": ["finance commission", "panchayat", "financial review"]},
            {"number": "243K", "title": "Elections to the Panchayats", "text": "The superintendence, direction and control of the preparation of electoral rolls for, and the conduct of, all elections to the Panchayats shall be vested in the State Election Commission.", "keywords": ["elections", "panchayat", "state election commission"]},
            {"number": "243O", "title": "Bar to interference by courts in electoral matters", "text": "Notwithstanding anything in this Constitution, the validity of any law relating to the delimitation of constituencies or the allotment of seats to such constituencies, made or purporting to be made under article 243K, shall not be called in question in any court.", "keywords": ["elections", "panchayat", "court", "jurisdiction"]}
        ]
    },
    {
        "part": "IXA",
        "title": "The Municipalities",
        "articles": [
            {"number": "243P", "title": "Definitions", "text": "In this Part, unless the context otherwise requires, Municipality means an institution of self-government constituted under article 243Q.", "keywords": ["municipality", "definition", "urban", "self-government"]},
            {"number": "243Q", "title": "Constitution of Municipalities", "text": "There shall be constituted in every State: (a) a Nagar Panchayat for a transitional area; (b) a Municipal Council for a smaller urban area; and (c) a Municipal Corporation for a larger urban area.", "keywords": ["municipality", "nagar panchayat", "municipal council", "municipal corporation"]},
            {"number": "243R", "title": "Composition of Municipalities", "text": "All the seats in a Municipality shall be filled by persons chosen by direct election from the territorial constituencies in the Municipal area.", "keywords": ["municipality", "composition", "elections"]},
            {"number": "243S", "title": "Constitution and composition of Wards Committees", "text": "There shall be constituted Wards Committees, consisting of one or more wards, within the territorial area of a Municipality having a population of three lakhs or more.", "keywords": ["wards committee", "municipality"]},
            {"number": "243T", "title": "Reservation of seats", "text": "Seats shall be reserved for the Scheduled Castes and the Scheduled Tribes in every Municipality.", "keywords": ["reservation", "scheduled castes", "scheduled tribes", "municipality"]},
            {"number": "243U", "title": "Duration of Municipalities", "text": "Every Municipality shall continue for five years from the date appointed for its first meeting.", "keywords": ["municipality", "duration", "five years"]},
            {"number": "243W", "title": "Powers, authority and responsibilities of Municipalities", "text": "The Legislature of a State may, by law, endow the Municipalities with such powers and authority as may be necessary to enable them to function as institutions of self-government.", "keywords": ["powers", "municipality", "self-government"]},
            {"number": "243X", "title": "Power to impose taxes by, and Funds of, the Municipalities", "text": "The Legislature of a State may, by law, authorize a Municipality to levy, collect and appropriate such taxes, duties, tolls and fees.", "keywords": ["taxes", "municipality", "funds"]},
            {"number": "243Y", "title": "Finance Commission", "text": "The Finance Commission constituted under article 243I shall also review the financial position of the Municipalities.", "keywords": ["finance commission", "municipality"]},
            {"number": "243ZE", "title": "Committee for district planning", "text": "There shall be constituted in every State at the district level a District Planning Committee to consolidate the plans prepared by the Panchayats and the Municipalities in the district.", "keywords": ["district planning committee", "panchayat", "municipality"]},
            {"number": "243ZG", "title": "Bar to interference by courts in electoral matters", "text": "Notwithstanding anything in this Constitution, the validity of any law relating to the delimitation of constituencies or the allotment of seats to such constituencies shall not be called in question in any court.", "keywords": ["elections", "municipality", "court"]}
        ]
    }
]

# Extend the parts array
data['parts'].extend(additional_parts)

# Update summary
data['summary']['articles_in_this_database'] = sum(len(part['articles']) for part in data['parts'])
data['summary']['parts_covered'] = [part['part'] for part in data['parts']]

# Save updated file
with open('constitution_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Constitution database expanded!")
print(f"Total articles now: {data['summary']['articles_in_this_database']}")
print(f"Parts covered: {', '.join(data['summary']['parts_covered'])}")
