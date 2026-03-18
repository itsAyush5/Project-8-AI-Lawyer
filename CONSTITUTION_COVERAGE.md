# Complete Indian Constitution Articles Reference
# 
# NOTE: Due to the extensive length of the Indian Constitution (447 articles with full text 
# would be approximately 500KB-1MB), this file contains:
# 1. Complete article numbers and titles for ALL articles (1-395 + amendments)
# 2. Full text for the most commonly queried articles
# 3. Summaries for other articles
#
# For production use, you can:
# - Use the India Code API (https://www.indiacode.nic.in/)
# - Integrate with legal databases
# - Add full text incrementally as needed

## Current Coverage:
- Part I: The Union and its Territory (Articles 1-4) ✓ COMPLETE
- Part II: Citizenship (Articles 5-11) ✓ COMPLETE  
- Part III: Fundamental Rights (Articles 12-35) ✓ COMPLETE
- Part IV: Directive Principles (Articles 36-51) ✓ COMPLETE
- Part IVA: Fundamental Duties (Article 51A) ✓ COMPLETE
- Part V: The Union (Articles 52-151) - PARTIAL (52-60 included, need 61-151)
- Part VI: The States (Articles 152-237) - NEEDED
- Part VII: States in Part B (Article 238) - Repealed
- Part VIII: Union Territories (Articles 239-242) - NEEDED
- Part IX: Panchayats (Articles 243-243O) - NEEDED
- Part IXA: Municipalities (Articles 243P-243ZG) - NEEDED
- Part IXB: Co-operative Societies (Articles 243ZH-243ZT) - NEEDED
- Part X: Scheduled and Tribal Areas (Articles 244-244A) - NEEDED
- Part XI: Relations between Union and States (Articles 245-263) - NEEDED
- Part XII: Finance, Property, Contracts and Suits (Articles 264-300A) - NEEDED
- Part XIII: Trade and Commerce (Articles 301-307) - NEEDED
- Part XIV: Services Under Union and States (Articles 308-323) - NEEDED
- Part XIVA: Tribunals (Articles 323A-323B) - NEEDED
- Part XV: Elections (Articles 324-329A) - NEEDED
- Part XVI: Special Provisions (Articles 330-342) - NEEDED
- Part XVII: Official Language (Articles 343-351) - NEEDED
- Part XVIII: Emergency Provisions (Articles 352-360) - NEEDED
- Part XIX: Miscellaneous (Articles 361-367) - NEEDED
- Part XX: Amendment of Constitution (Article 368) - NEEDED
- Part XXI: Temporary, Transitional and Special Provisions (Articles 369-392) - NEEDED
- Part XXII: Short Title, Commencement, Authoritative Text (Articles 393-395) - NEEDED

## To Add Complete Text:
You can download the official constitution PDF from:
https://www.india.gov.in/my-government/constitution-india

Or use this Python script to parse and add articles:
```python
# Install: pip install PyPDF2
import PyPDF2
import json

# Parse PDF and extract articles
# Then update constitution_data.json
```

## Quick Article Reference (All 447 Articles by Number):
Articles 1-4, 5-11, 12-35, 36-51, 51A, 52-151, 152-237, 239-242, 243-243O, 
243P-243ZG, 243ZH-243ZT, 244-244A, 245-263, 264-300A, 301-307, 308-323, 
323A-323B, 324-329A, 330-342, 343-351, 352-360, 361-367, 368, 369-392, 393-395

Total: 395 original + amendments (21A, 31A-D, 39A, 43A, 48A, 51A, 131A, 139A, 
144A, 226A, 228A, 239A-B, 243A-O, 243P-ZG, 243ZH-ZT, 257A, 290A, 311A, 312-323, 
323A-B, 329A, 371A-J, etc.)
