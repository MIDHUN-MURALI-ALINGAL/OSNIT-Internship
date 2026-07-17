

## Advanced Search Techniques

## Target Company
## Zoom Communications
## Objective
- Compare the results obtained from different search engines and
OSINT tools.
- Identify publicly available information related to the target
organization.
- Understand the unique strengths and capabilities of each search
platform.
- Analyze and compare the findings from multiple sources.
- Document key observations, differences, and security-related
insights
## Tools Used
## Tool Purpose
## Google
## Search
Used to discover websites, documents, support pages, and other
publicly indexed information using advanced search operators.
## Bing
## Search
Used  to  compare  search  results,  identify  additional  indexed
pages,  and  discover  content  that  may  not  appear  in  Google
## Search.
Shodan Used  to  identify  publicly  accessible  internet-connected  assets,
including  IP  addresses,  SSL  certificates,  open  services,  and
hosting information.


## Google Investigation
## Queries Used
site: zoom.us

site: zoom.us filetype: pdf

site: zoom.us inurl: login


## Findings
- Official Zoom website
- Support documentation
- PDF documents
- Privacy policy
## • Help Center
- Developer resources





## Bing Investigation
## Queries Used
site: zoom.us

site: zoom.us filetype: pdf

site: zoom.us inurl: login
## Findings
- Official website
- Public PDF documents
- Microsoft indexed pages
- Cached search results
- News articles
- Support resources

## Shodan Investigation
## Search Used
hostname: zoom.us
## Findings
- Public IP addresses

- SSL certificate information
- Hosting provider details
- Internet-facing services
- Network information
- Public service banners
## Security Observations
- Public documents should be reviewed regularly.
- Login portals should be protected with strong
authentication.
- Public infrastructure should be monitored.
- SSL certificates should be kept updated.
- Sensitive information should never be publicly exposed.
## Best Practices
- Monitor publicly indexed content.
- Remove unnecessary public files.
- Secure administrative portals.
- Conduct regular OSINT assessments.
- Review digital footprint periodically.



## Conclusion
- Google provides comprehensive web search capabilities
and is effective for discovering documents, support pages,
and indexed content.
- Bing complements Google by surfacing additional indexed
or cached pages that may not appear in Google results.
- Shodan focuses on publicly visible internet infrastructure
such as IP addresses, SSL certificates, and exposed services
rather than web content.
- Comparing multiple search engines and OSINT tools gives
a broader understanding of an organization's public digital
footprint.
- Using multiple sources together improves the quality of
OSINT investigations while relying only on publicly
available information


