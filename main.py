# # !/usr/bin/python
# # !python
from scraperHelpers import *

parsed_pages = parse_page_data_into_html()

extracted_job_titles = []
extracted_job_descriptions = []
extracted_job_snippets =[]

for page in parsed_pages:
    extracted_job_titles.append(find_jobs_by_header_title(page))
    extracted_job_snippets.append(find_jobs_by_summary(page))

save_jobs_as_txt(extracted_job_titles)
job_summaries = extract_job_descriptions()
save_summaries_as_csv(extracted_job_snippets)
save_titles_as_csv(extracted_job_titles)


