from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

error_style = style_from_dict({
    Token.ErrorMessage: '#ff0066',
    Token.ShubFileModel: '#ccaa33',
    Token.NoInternetConnection: '#ff0066',
    Token.ShubApiError: '#ff0066',

    Token.ShubApiErrorHintsHeadline: '#ccaa33',
    Token.ShubApiErrorHints1: '#ccaa33',
    Token.ShubApiErrorHints2: '#ccaa33',
})

shub_not_configured_tokens = [
    (Token.ErrorMessage, 'You need to set up your .scrapinghub.yml with a default project and api key:\n'),
    (Token.ShubFileModel,
     '''
     ~/.scrapinghub.yml

     apikeys:
       default: v65a787a987k08k9s797d7s8l98298sw
     projects:
       default: 89090
     \n
     '''
     ),
]

shub_api_error_tokens = [
    (Token.ShubApiError, 'Unknown response status from ScrapingHub: badrequest.\n'),
    (Token.ShubApiErrorHintsHeadline, 'Hints:\n\n'),
    (Token.ShubApiErrorHints1, '- Are your credentials [api key, project id] set correctly?\n'),
    (Token.ShubApiErrorHints2, '- Are the job/jobs parameters named and passed corretly?\n')
]

no_internet_connection_tokens = [
    (Token.NoInternetConnection, 'You do not have Internet connection.\n')
]

TABLE_JOB_MODEL = [['Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']]

TABLE_JOBS_MODEL = [['Id', 'Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']]
