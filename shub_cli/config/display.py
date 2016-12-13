from prompt_toolkit.styles import style_from_dict
from pygments.token import Token

TABLE_JOB_MODEL = [['Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']]

TABLE_JOBS_MODEL = [['Id', 'Spider', 'Started Time', 'Items', 'Tags', 'State', 'Close Reason', 'Errors', 'Version']]

HC_TABLE_JOBS_MODEL = [['Id', 'Spider', 'Finished Time', 'State', 'Close Reason', 'Errors', 'Logs', 'Version']]

TABLE_SPIDERS_MODEL = [['Id', 'Tags', 'Version', 'Type']]

token_style = style_from_dict({
    Token.ErrorMessage: '#ff0066',
    Token.ShubFileModel: '#ccaa33',
    Token.NoInternetConnection: '#ff0066',
    Token.ShubApiError: '#ff0066',
    Token.ShubApiErrorHintsHeadline: '#ccaa33',
    Token.ShubApiErrorHints1: '#ccaa33',
    Token.ShubApiErrorHints2: '#ccaa33',
    Token.Credentials: '#ccaa33',
    Token.GeneralErrorMessage: '#ff0066',
    Token.GeneralInfoMessage: '#ccaa33',

})

tokens = [
    (Token.ShubApiError, 'Unknown response status from ScrapingHub: badrequest.\n'),
    (Token.ShubApiErrorHintsHeadline, 'Hints:\n\n'),
    (Token.ShubApiErrorHints1, '- Are your credentials [api key, project id] set correctly?\n'),
    (Token.ShubApiErrorHints2, '- Are the job/jobs parameters named and passed corretly?\n'),
    (Token.NoInternetConnection, 'You do not have Internet connection.\n'),
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
     )
]


def create_error_token(message):
    return Token.GeneralErrorMessage, message + '\n'


def create_info_token(message):
    return Token.GeneralInfoMessage, message + '\n'
