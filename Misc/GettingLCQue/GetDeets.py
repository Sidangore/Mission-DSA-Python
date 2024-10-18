import requests


def leetCode_problem_details_using_graphQL(slug):
    url = 'https://leetcode.com/graphql'

    # The GraphQL query to fetch the problem details
    query = '''
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            title
            content
            difficulty
        }
    }
    '''

    # Set up the JSON payload
    variables = {
        "titleSlug": slug
    }

    # Make the request with headers
    headers = {
        'Content-Type': 'application/json',
        'Referer': f'https://leetcode.com/problems/{slug}/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.36'
    }

    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

    if response.status_code == 200:
        data = response.json()
        question = data.get('data', {}).get('question', {})
        return {
            'title': question.get('title'),
            'content': question.get('content'),
            'difficulty': question.get('difficulty')
        }
    else:
        return f"Failed to fetch the question. Status code: {response.status_code}"


# Example usage
leetcode_slug = 'two-sum'  # This is the slug part of the URL (e.g., "two-sum" for
# https://leetcode.com/problems/two-sum/)
details = leetCode_problem_details_using_graphQL(leetcode_slug)
print(details)
