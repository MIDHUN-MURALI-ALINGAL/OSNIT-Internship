

## Google Hacking Database
## Introduction
- The Google Hacking Database (GHDB) is a collection of
categorized Google search queries (Google Dorks) used to locate
publicly available information on the internet.
- It helps investigators perform targeted searches to find documents,
login pages, security resources, configuration files, and other
indexed content.
- GHDB is widely used in Open Source Intelligence (OSINT) and
cybersecurity for efficient information gathering.
Importance of GHDB in OSINT & Cybersecurity
- Helps discover publicly available information quickly and
accurately.
- Organizes Google Dorks into categories for easier searching and
investigation.
- Supports cybersecurity professionals in identifying exposed public
resources and improving security awareness.
- Enables ethical OSINT investigations using only publicly indexed
information while following legal and ethical guidelines.
## Objectives
- Understand the concept and purpose of the Google Hacking Database
## (GHDB).

- Learn the different categories of Google Dorks and their applications.
- Use GHDB to perform targeted searches for publicly available
information.
- Improve OSINT investigation skills through efficient search techniques.
- Identify documents, websites, login pages, security resources, and
technical documentation using Google Dorks.
- Develop the ability to analyze and verify information collected from
public sources.
Google Hacking Database (GHDB)
- The Google Hacking Database (GHDB) is a collection of
categorized Google Dorks (advanced Google search queries)
used to locate publicly available information on the internet. It
helps OSINT investigators, security researchers, and
cybersecurity professionals perform targeted searches more
efficiently using advanced Google search operators.
## Risks Identified
Potential Risks Discovered Through GHDB Searches
## • Public Documents
o Sensitive reports, manuals, or internal documents may be
indexed by search engines if not properly restricted.
## • Backup Files

o Backup files (e.g., .bak, .old, .zip) may unintentionally
contain source code, configuration settings, or database
information.
## • Login Portals
o Publicly discoverable login pages can reveal administrative
interfaces and become targets for credential attacks if not
adequately secured.
## • Configuration Files
o Exposed configuration files may disclose system settings,
API endpoints, or other technical information useful for
reconnaissance.
## • Directory Listings
o Misconfigured web servers with directory indexing enabled
can expose files and folders that were not intended for public
access.
## • Metadata Leakage
o Documents such as PDFs and Office files may contain
metadata, including author names, software versions, or
document creation details, which can aid OSINT
investigations.
## • Information Disclosure
o Publicly accessible technical details, error messages, or
exposed resources can reveal information about an

organization's infrastructure and technologies, increasing the
risk of targeted attacks.

## Best Security Practices
Recommended Measures to Reduce Information Exposure
## • Disable Directory Listing
o Prevent web servers from displaying the contents of
directories when no default page is present.
## • Remove Backup Files
o Delete or securely store backup files (such as .bak, .zip, .old,
and .sql) so they are not accessible from the web.

## • Restrict Sensitive Documents
o Ensure confidential files are protected with appropriate
access controls and are not publicly indexed by search
engines.

## • Protect Admin Panels
o Secure administrative interfaces using strong passwords,
multi-factor authentication (MFA), IP restrictions, and
regular credential updates.

- Configure robots.txt Carefully
o Use robots.txt to guide search engine crawlers, but never rely
on it to protect sensitive information, as it does not provide
access control.
## • Perform Regular Security Audits
o Periodically review websites, search engine indexing, and
server configurations to identify and remediate exposed
resources.
## • Keep Systems Updated
o Regularly update operating systems, web servers, and
applications to patch known security vulnerabilities.
## • Monitor Public Exposure
o Conduct routine OSINT and GHDB-based assessments on
your own organization to identify publicly accessible
information before attackers do.
## Selected 10 Google Dorks
## Category Example Dork Purpose
Files filetype: pdf site:
example.com
Find PDF files
Login site: example.com inurl:
login
Login pages
Directory intitle: "index of" Open directories
Config Ext: xml site:example.com XML configuration
files

Backup ext :bak Backup files
Database ext : sql SQL dumps
Documents filetype: xlsx Excel documents
Logs ext: log Log files
Password intext: "password" Password references
Admin inurl: admin Admin portals

## Practical Investigation
## Target Company
## Zoom Communications
## Activities Performed

Public PDF Document Search
Query: site: zoom.us filetype: pdf
- Located publicly available user guides, product manuals, and
technical documentation.
## Developer Documentation Search
Query: site: zoom.us "developer"
- Identified the Zoom Developer Platform, SDK documentation, and
integration guides.
API Documentation Search
Query: site: zoom.us inurl: developer "API"
- Found REST API documentation, authentication guides, and
developer references.

## Support Resources Search
Query: site: zoom.us inurl: support
- Accessed the Help Center, FAQs, troubleshooting guides, and user
support articles.
## Security Page Search
Query: site: zoom.us intitle: security
- Located the Zoom Trust Center, security policies, privacy
information, and compliance resources.
## Release Notes Search
Query: site: zoom.us "release notes"
- Found product update announcements, feature improvements, and
version release information.
AI Companion Documentation Search
Query: site: zoom.us "AI Companion"
- Identified AI Companion features, user guides, and official product
documentation
## Findings
Observed Findings (Directly Verified)
- Official Zoom website successfully indexed by Google.
- Public PDF documents such as user guides and manuals were
available.
- Developer documentation and SDK resources were publicly
accessible.
- Support pages including Help Center and FAQs were found.

- Security resources, including the Zoom Trust Center, were
publicly available.
- Privacy Policy and compliance information were accessible.
- Release notes and Zoom AI Companion documentation were
identified.

Inferred Findings (Based on Observations)
- Zoom has strong search engine visibility, making official
resources easy to discover.
- The company maintains well-organized and regularly updated
documentation.
- Public availability of security and privacy resources indicates
transparent security practices.
- Zoom provides a mature developer ecosystem with
comprehensive API and SDK documentation.
- The organization demonstrates a strong commitment to user
support, accessibility, and information transparency.
## Activities Performed:
- Selected Zoom Communications as the target organization.
- Explored the Google Hacking Database (GHDB) to identify
relevant Google Dorks.
- Chose 10 dorks from multiple GHDB categories, including Files,
Login Portals, Sensitive Information, and Directory Listings.
- Performed safe, publicly available Google searches without
attempting unauthorized access.

- Recorded the search results and noted the types of publicly indexed
resources.
- Identified exposed document types such as PDF files, support
documentation, developer resources, and public web pages.
- Analyzed the potential security risks associated with publicly
accessible information.

## Conclusion
- The Google Hacking Database (GHDB) is a valuable resource
for OSINT investigators, cybersecurity professionals, and
security researchers, providing a structured collection of Google
Dorks for targeted information gathering.
- It enables efficient discovery of publicly available information
such as documents, security pages, developer resources, APIs,
login pages, and technical documentation using categorized
Google search queries.
- During the practical investigation of Zoom Communications,
GHDB techniques helped identify official resources, public
documentation, security information, support pages, and developer
materials in an organized and efficient manner.
- Using categorized Google Dorks significantly improves the speed,
accuracy, and precision of OSINT investigations by reducing
irrelevant search results and focusing on specific information.
- GHDB also enhances an investigator's ability to analyze an
organization's digital footprint and understand its search engine
exposure using only publicly indexed information.





