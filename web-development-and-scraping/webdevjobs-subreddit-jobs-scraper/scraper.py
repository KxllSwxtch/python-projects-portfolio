#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

# TODO: add an experience field
# TODO: add an optional comments field
# TODO: add sorting


def scrape():
    """
    Gets the data from reddit.com/r/WebDevJobs
    Input (the user will be prompted to enter):
        - Developer Field: front end, backend, back end, full-stack, data, etc.
        - Date Range: last month, week, 2 weeks, 1 year, etc.
    Output:
        A list of all jobs available for the the development field
        and the date range entered with the following fields:
            1. Title
            2. Flair / Topic
            3. Media / Description / Job URL (If no description provided)
            4. Date added
            5. A link to the user who created a job post
    """
    HTML_PARSER = 'html.parser'

    # classes
    classes = {
        'CONTAINER_CLASS': 'rpBJOHq2PR60pnwJlUyP0',
        'JOB_FLAIR': '_2xu1HuBz1Yx6SP10AGVx_I',
    }

    # attributes names
    attrs = {
        'POST_CONTAINER': 'post-container',  # data-testid
        'TITLE': 'title',  # data-adclicklocation
        'MEDIA': 'media',  # data-adclicklocation
        'OUTBOUND-LINK': 'outbound-link',  # data-test-id
        'TIMESTAMP': 'post_timestamp'  # data-testid
    }

    url = 'https://www.reddit.com/r/WebDevJobs/hot/'
    html = requests.get(url, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
    if html.status_code == 200:
        soup = BeautifulSoup(html.content, HTML_PARSER)
        main_container = soup.find(
            'div', attrs={'class': classes['CONTAINER_CLASS']})
        posts = main_container.find_all(
            'div', attrs={'data-testid': attrs['POST_CONTAINER']})

        # separator
        print('\n======================\n')
        for post in posts:
            job_title = post.find(
                'div', attrs={'data-adclicklocation': attrs['TITLE']}).find('h3').text
            job_description = post.find(
                'div', attrs={'data-adclicklocation': attrs['MEDIA']})
            job_link = post.find(
                'a', attrs={'data-testid': attrs['OUTBOUND-LINK']})
            job_flair = post.find(
                'div', attrs={'class': classes['JOB_FLAIR']})
            job_posted_date = post.find(
                'span', attrs={'data-testid': attrs['TIMESTAMP']})

            if '[HIRING]' in job_title:
                print(job_title)

                if job_description is not None:
                    print('Job description: {}'.format(
                        job_description.get_text(separator='\n- ')))
                if job_link is not None:
                    print(f'Job link: {job_link.get("href")}')
                if job_flair is not None:
                    print(f'Flair: {job_flair.text}')
                if job_posted_date is not None:
                    print(f'Job Posted: {job_posted_date.text}')

                # delimiter
                print('\n======================\n')
    else:
        print('Request Error')
        return


if __name__ == '__main__':
    scrape()
