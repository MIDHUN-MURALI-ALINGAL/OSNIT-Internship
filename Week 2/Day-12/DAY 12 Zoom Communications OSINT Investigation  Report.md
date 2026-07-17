

Zoom Communications OSINT Investigation  Report

## Objective
- Conduct a comprehensive OSINT investigation of Zoom
Communications using the search intelligence techniques learned
during Week 2.
- Apply advanced Google Dorks to identify publicly available
information, including websites, documents, login portals,
developer resources, and security-related pages.
- Compare findings across multiple search engines and OSINT tools,
including Google Search, Bing Search, and Shodan.
- Analyze Zoom's public digital footprint and document key
observations using ethical and responsible OSINT practices.
- Consolidate the investigation findings into a structured report with
recommendations and best practices for managing publicly
accessible information.
## Tools Used
## Tool Purpose
Google Search Perform advanced Google Dork searches
## Google Hacking Database
## (GHDB)
Reference categorized Google Dorks
Bing Search Compare search results with Google
Shodan Discover publicly visible internet-facing
infrastructure

Python 3 Automate repetitive search tasks
Visual Studio Code Develop and execute Python scripts
GitHub Store project files and documentation



## Google Dorks Used
## No. Google Dork Category Purpose
1 Site: zoom.us Website
## Discovery
Identify the official Zoom
website and indexed pages
2 site: zoom.us
filetype:pdf
## Public
## Documents
Locate publicly available PDF
documents
3 site:  zoom.us
filetype : docx
## Public
## Documents
Search for Microsoft Word
documents
4 site: zoom.us
filetype   : xlsx
## Public
## Documents
Find publicly accessible Excel
files
5 site: zoom.us inurl:
login
Login Portal Identify official login pages
6 site: zoom.us inurl:
admin
Administration Search for administrative pages
7 site:  zoom.us intitle:
"index of"
Directory Listing Check for exposed directory
listings
8 site: zoom.us ext:
xml
## Configuration
## Files
Search for XML configuration
files

9 Site: zoom.us ext:
bak
Backup Files Identify publicly accessible
backup files
10 site: zoom.us ext:
log
Log Files Search for publicly indexed log
files
11 site: zoom.us intext:
## "privacy"
Privacy Locate privacy-related
information
12 site: zoom.us
security
Security Find security documentation
and Trust Center pages
13 site: zoom.us
support
Support Discover Help Center and
support resources
14 site: zoom.us
developer
## Developer
## Resources
Locate API, SDK, and
developer documentation
15 site: zoom.us api API
## Documentation
Search for public API
documentation

## Investigation Findings
## No. Category Findings
## 1
## Official
## Website
Identified the official Zoom website along with
publicly indexed pages and services.
## 2
## Public
## Documents
Located publicly available PDF documents, user
guides, and technical documentation.
## 3
Login Portal Found the official Zoom login portal used for user
authentication.
## 4
## Support
## Resources
Identified the Zoom Help Center, FAQs,
troubleshooting guides, and customer support pages.

## 5
## Developer
## Resources
Located the Zoom Developer Portal, API
documentation, SDKs, and integration resources.
## 6
## Security
## Resources
Found the Zoom Trust Center, security
documentation, and security-related announcements.
## 7
## Privacy
## Information
Located the Privacy Policy, Terms of Service, and
other legal documentation.
## 8
## XML
## Resources
Public XML resources were identified; no sensitive
configuration files were observed.
## 9
Backup Files No publicly indexed backup (.bak) files were
observed during the investigation.
## 10
Log Files No publicly indexed log (.log) files were observed
during the investigation.
## 11
## Search Engine
## Comparison
Google returned the most comprehensive
documentation, Bing indexed additional public
pages, and Shodan provided information about
publicly visible internet-facing infrastructure.
## 12
## Overall
## Assessment
The investigation revealed a well-maintained public
digital footprint with official documentation, support
resources, and developer information, while no
obvious exposure of backup or log files was observed
through the searches performed.

Multi-Engine Comparison
## Tool Information Found
Google Documents, login pages
Bing Additional indexed pages

Shodan SSL certificates, public infrastructure

## Security Observations
- Public documents available
- Login portal publicly accessible
- Developer documentation publicly available
- Security pages accessible
- Privacy documentation available

## Best Practices
- Monitor indexed content.
- Remove unnecessary public files.
- Protect administrative portals.
- Perform regular OSINT reviews.
- Follow ethical search practices.

## Conclusion
- The OSINT investigation of Zoom Communications successfully
demonstrated the practical application of the search intelligence techniques
learned during Week 2. Advanced Google Dorks, the Google Hacking

Database (GHDB), search automation concepts, and multiple search
engines—including Google Search, Bing Search, and Shodan—were
used to identify publicly available information in a structured and ethical
manner.
- The investigation identified official websites, documentation, login
portals, developer resources, support pages, security information, and
privacy documentation. No publicly indexed backup files, log files, or
exposed directory listings were observed during the investigation.
Comparing multiple search platforms provided a broader understanding of
Zoom's public digital footprint.
- Overall, this project strengthened practical OSINT investigation skills,
enhanced search intelligence techniques, and reinforced the importance
of conducting ethical investigations using only publicly available
information. The knowledge and experience gained during Week 2 provide
a strong foundation for future cybersecurity and OSINT investigations
