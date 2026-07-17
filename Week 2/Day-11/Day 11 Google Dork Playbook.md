

## Google Dork Playbook

## Target Organization
## Zoom Communications
## Objective
- Organize Google Dorks into logical categories based on their
purpose, such as reconnaissance, document discovery, login
portals, infrastructure, and security resources.
- Create a reusable Google Dork Playbook to support future OSINT
investigations and search intelligence activities.
- Document advanced search operators, search automation
techniques, multi-engine investigation methods, and GHDB-based
searches.
- Establish a structured reference that promotes efficient, ethical, and
repeatable information gathering using publicly available sources.
- Develop a personal knowledge base that can be expanded with new
Google Dorks, search strategies, and OSINT techniques over time.







## Tools Used
## Tool Purpose
Google Search Used to perform advanced searches using Google Dorks to
discover publicly indexed websites, documents, login pages,
and other online resources.
## Google Hacking
## Database
## (GHDB)
Used as a reference library of categorized Google Dorks for
identifying  documents,  login  portals,  configuration  files,
directory listings, and other publicly accessible resources.
Bing Search Used to compare search results with Google and identify
additional  indexed  pages,  cached  content,  and  publicly
available information.
Shodan Used  to  identify  publicly  accessible  internet-connected
assets,  including  IP  addresses,  SSL  certificates,  open
services, and hosting information.
Python 3 Used to automate repetitive Google Dork searches, process
search  queries,  and  generate  search  reports  during  the
Search Automation task.
## Visual   Studio
## Code
Used as the Integrated Development Environment (IDE)
for  writing,  testing,  and  executing  Python  automation
scripts.
GitHub
Used to store, organize, and version-control project
files, reports, scripts, and documentation developed
during the OSINT internship.





## Search Operator Reference
## Operator Purpose Example
site:
Search within a specific
domain
site:zoom.us
filetype: Search specific file types site:zoom.us filetype:pdf
inurl: Search URL keywords site:zoom.us inurl:login
intitle: Search page titles
site:zoom.us
intitle:"security"
intext: Search page content
site:zoom.us
intext:"privacy"
ext: Search file extensions site:zoom.us ext:xml

## Google Dork Categories
## Website Reconnaissance
site: zoom.us
site: zoom.us inurl: about
site: zoom.us inurl: contact
## Purpose
- Identify official website
- Company information
- Contact details


## Public Documents
site: zoom.us filetype: pdf
site:  zoom.us filetype: docx
site: zoom.us filetype: xlsx
## Purpose
- User manuals
- Product documentation
- Public reports
- Technical documents

## Login Portals
site: zoom.us inurl: login
site: zoom.us inurl: signin
site: zoom.us intitle: login
## Purpose
- Discover publicly accessible authentication pages



## Directory Listings
site: zoom.us intitle: "index of"
## Purpose
- Identify indexed directory listings

## Configuration Files
site: zoom.us ext: xml
site: zoom.us ext: conf
site: zoom.us ext: config
## Purpose
- Search for publicly indexed configuration files

## Backup Files
site: zoom.us ext:  bak
site: zoom.us ext:
old
## Purpose
- Locate backup files


## Log Files
site:  zoom.us ext: log
## Purpose
- Identify publicly indexed log files

## Security Resources
site: zoom.us intitle: security
site: zoom.us "bug bounty"
site: zoom.us "Trust Center"
## Purpose
- Security documentation
- Responsible disclosure
- Trust Center resources

## Privacy & Compliance
site: zoom.us privacy
site: zoom.us policy
site: zoom.us terms
## Purpose

- Privacy policy
- Legal documentation
- Compliance information

## Developer Resources
site: zoom.us developer
site: zoom.us API
site: zoom.us SDK
## Purpose
- API documentation
- SDK guides
- Developer platform

GHDB Categories Used

## Category Example Dork
Files filetype: pdf
Login Portals inurl: login
Sensitive Directories intitle: "index of"

Configuration Files ext: xml
Backup Files ext:  bak
Log Files ext: log
Admin Pages inurl:  admin
Privacy Information intext: "privacy"

## Search Automation Summary
## Automation Process
- Read Google Dorks from dorks.txt
- Executed searches automatically
- Generated Google Search URLs
- Logged all queries into results.txt
- Reduced repetitive manual searching
Example automated queries included:
- site: zoom.us filetype: pdf
- site:  zoom.us inurl: login
- site: zoom.us intitle: "index of"
- site: zoom.us ext: xml
- site: zoom.us ext:  log

These automated queries were successfully generated and
recorded in the search report.

Multi-Engine Investigation Summary
## Search
## Engine
## Strength
Google Official websites, documents, support pages
Bing Cached pages, additional indexed results
## Shodan
Public infrastructure, SSL certificates, hosting
details

## Best Practices
- Use advanced search operators responsibly.
- Verify findings using multiple search engines.
- Regularly review publicly indexed content.
- Remove unnecessary public documents.
- Protect login portals with strong authentication.
- Monitor exposed infrastructure.
- Follow ethical and legal OSINT practices.


## Dork Playbook Categories
## Use Case Dork Pattern Adapted Query Purpose
Website Recon site: site:zoom.us Discover official website
Public Documents filetype:pdf site:zoom.us
filetype:pdf
Locate PDF documents
Login Portal inurl:login site:zoom.us inurl:login Find authentication
pages
Directory Listing intitle:"index
of"
site:zoom.us
intitle:"index of"
Identify indexed
directories
## Configuration
## Files
ext:xml site:zoom.us ext:xml Search configuration
files
Backup Files ext:bak site:zoom.us ext:bak Locate backup files
Log Files ext:log site:zoom.us ext:log Find publicly accessible
logs
## Developer
## Resources
developer site:zoom.us developer API and SDK
documentation
## Security
## Resources
security site:zoom.us security Security pages
## Privacy
## Information
privacy site:zoom.us privacy Privacy and legal
documents

## Conclusion
- The Google Dork Playbook consolidates the knowledge
and practical work completed during Week 2 into a
structured reference. It organizes Google Dorks by
category, summarizes search automation, and highlights the

value of using multiple search engines for OSINT
investigations. This playbook serves as a reusable guide for
future public-information gathering while promoting
responsible and ethical search practices.


